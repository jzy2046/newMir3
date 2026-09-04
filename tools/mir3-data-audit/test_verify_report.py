#!/usr/bin/env python3
"""Regression checks for complete Mir3 comparison-report verification."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "tools" / "mir3-data-audit" / "verify_snapshot.py"
EMPTY_DELETE_TEXT = "当前没有满足严格证据条件的建议删除候选。"
REQUIRED_HEADINGS = (
    "# 传奇3 光通 1.45 数据完整对比报告",
    "## 口径与安全说明",
    "## 快照绑定信息",
    "## 数量汇总",
    "## 来源表",
    "## 官方物品完整表",
    "## 本服物品完整对比表",
    "## 官方怪物完整表",
    "## 本服怪物完整对比表",
    "## 官方套装表",
    "## 本服套装对比表",
    "## 建议删除候选",
    "## 版本不确定项",
)


def snapshot_document(*, include_unknown: bool = False) -> dict:
    items = [{"index": 1, "name": "Later Item", "itemType": "Weapon", "requiredClass": "All", "requiredAmount": 1, "image": 2}]
    if include_unknown:
        items.append({"index": 2, "name": "Mystery", "itemType": "Weapon", "requiredClass": "All", "requiredAmount": 1, "image": 3})
    return {
        "database": {"path": "Database/System.db", "sha256": "abc", "exportedAt": "2026-09-04T00:00:00Z"},
        "items": items,
        "monsters": [{"index": 8, "name": "Wolf", "level": 4, "ai": 3, "image": 4, "isBoss": False}],
        "sets": [{"index": 9, "name": "Starter Set", "groups": [{"name": "main", "requiredNumItems": 1, "items": ["Later Item"]}]}],
    }


def reference_document(*, excluded: bool = False) -> dict:
    reference = {
        "scope": {"game": "传奇3", "operator": "光通", "version": "1.45", "policy": "strict-evidence"},
        "sources": [], "items": [], "monsters": [], "sets": [],
    }
    if excluded:
        reference["sources"] = [{
            "id": "s1", "title": "Evidence", "url": "https://example.invalid", "level": 1,
            "notes": "evidence", "versions": ["1.50"], "categories": ["items", "version-history"],
            "locator": "p1",
        }]
        reference["items"] = [{
            "name": "Later Item", "aliases": [], "status": "excluded-later-version", "sourceIds": ["s1"],
            "notes": "later", "category": "Weapon", "introducedVersion": "1.50",
        }]
    return reference


def report_document(snapshot: dict, *, deletion_rows: list[str] | None = None) -> str:
    lines = list(REQUIRED_HEADINGS[:-2])
    for kind, singular in (("items", "item"), ("monsters", "monster"), ("sets", "set")):
        lines.extend(f"<!-- local:{singular}:{entry['index']} -->" for entry in snapshot[kind])
    lines.extend((
        "## 建议删除候选",
        "| 类型 | 快照索引 | 数据库原名 | 官方名称 | 判断依据 |",
        "| --- | ---: | --- | --- | --- |",
    ))
    if deletion_rows:
        lines.extend(deletion_rows)
    else:
        lines.append(EMPTY_DELETE_TEXT)
    lines.append("## 版本不确定项")
    return "\n\n".join(lines) + "\n"


def run_case(name: str, snapshot: dict, reference: dict, report: str, success: bool) -> None:
    with tempfile.TemporaryDirectory(prefix="mir3-report-verify-") as directory:
        root = Path(directory)
        snapshot_path = root / "snapshot.json"
        reference_path = root / "reference.json"
        report_path = root / "report.md"
        snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
        reference_path.write_text(json.dumps(reference), encoding="utf-8")
        report_path.write_text(report, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(VERIFY), "--snapshot", str(snapshot_path), "--reference", str(reference_path),
             "--report", str(report_path)],
            capture_output=True, text=True, check=False,
        )
        if success:
            if result.returncode != 0:
                raise AssertionError(f"{name} unexpectedly failed: {result.stderr}")
        elif result.returncode != 1 or not result.stderr.startswith("verification failed:") or "Traceback" in result.stderr:
            raise AssertionError(f"{name} did not fail cleanly: rc={result.returncode}, stderr={result.stderr!r}")


def main() -> None:
    snapshot = snapshot_document()
    reference = reference_document()
    valid = report_document(snapshot)
    run_case("valid-minimal", snapshot, reference, valid, success=True)

    run_case("missing-marker", snapshot, reference, valid.replace("<!-- local:item:1 -->", ""), success=False)
    run_case("duplicate-marker", snapshot, reference, valid + "<!-- local:item:1 -->\n", success=False)
    run_case("extra-marker", snapshot, reference, valid + "<!-- local:item:999 -->\n", success=False)
    run_case("wrong-marker-type", snapshot, reference, valid.replace("local:item:1", "local:quest:1"), success=False)
    run_case("missing-section", snapshot, reference, valid.replace("## 来源表", ""), success=False)

    excluded_snapshot = snapshot_document(include_unknown=True)
    excluded_reference = reference_document(excluded=True)
    excluded_report = report_document(excluded_snapshot, deletion_rows=[
        "| 物品 | 1 | Later Item | Later Item | later evidence |",
    ])
    run_case("valid-excluded", excluded_snapshot, excluded_reference, excluded_report, success=True)
    run_case(
        "unknown-mixed-into-delete-candidates",
        excluded_snapshot,
        excluded_reference,
        excluded_report.replace(
            "| 物品 | 1 | Later Item | Later Item | later evidence |",
            "| 物品 | 1 | Later Item | Later Item | later evidence |\n| 物品 | 2 | Mystery | - | unknown |",
        ),
        success=False,
    )

    bad_snapshot = copy.deepcopy(snapshot)
    bad_snapshot["items"][0]["index"] = True
    run_case("snapshot-index-bool", bad_snapshot, reference, valid, success=False)
    print("comparison report verifier regression checks passed")


if __name__ == "__main__":
    main()
