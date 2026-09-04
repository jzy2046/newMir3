#!/usr/bin/env python3
"""Regression checks for the official Mir3 1.45 reference schema."""

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "tools" / "mir3-data-audit" / "verify_snapshot.py"


def run_reference(name: str, reference: object, success: bool) -> subprocess.CompletedProcess:
    with tempfile.TemporaryDirectory(prefix="mir3-reference-test-") as directory:
        reference_path = Path(directory) / f"{name}.json"
        reference_path.write_text(json.dumps(reference), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(VERIFY), "--reference", str(reference_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if success:
            if result.returncode != 0:
                raise AssertionError(f"{name} unexpectedly failed: {result.stderr}")
        elif result.returncode != 1 or not result.stderr.startswith("verification failed:") or "Traceback" in result.stderr:
            raise AssertionError(f"{name} did not fail cleanly: rc={result.returncode}, stderr={result.stderr!r}")
        return result


def empty_reference() -> dict:
    return {
        "scope": {"game": "传奇3", "operator": "光通", "version": "1.45", "policy": "strict-evidence"},
        "sources": [],
        "items": [],
        "monsters": [],
        "sets": [],
    }


def one_source() -> dict:
    reference = empty_reference()
    reference["sources"] = [{"id": "s1", "title": "官方资料", "url": "https://example.test/source", "level": 1, "notes": "用于测试"}]
    return reference


def one_item() -> dict:
    reference = one_source()
    reference["items"] = [{
        "name": "测试物品",
        "aliases": ["测试剑"],
        "status": "confirmed-145",
        "sourceIds": ["s1"],
        "notes": "可核验",
        "category": "weapon",
    }]
    return reference


def run_snapshot_regression() -> None:
    with tempfile.TemporaryDirectory(prefix="mir3-snapshot-test-") as directory:
        directory_path = Path(directory)
        database = directory_path / "System.db"
        database.write_bytes(b"test database")
        database_sha = hashlib.sha256(database.read_bytes()).hexdigest()
        snapshot = {
            "database": {"path": "Database/System.db", "sha256": database_sha, "exportedAt": "2026-09-04T00:00:00Z"},
            "items": [{"index": 1, "name": "item", "itemType": "Nothing", "requiredClass": "All", "requiredAmount": 0, "image": 0}],
            "monsters": [{"index": 1, "name": "monster", "level": 1, "ai": 1, "image": 1, "isBoss": False}],
            "sets": [{"index": 1, "name": "set", "groups": [{"name": "group", "requiredNumItems": 1, "items": ["item"]}]}],
        }
        snapshot_path = directory_path / "snapshot.json"
        snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(VERIFY), "--snapshot", str(snapshot_path), "--database", str(database), "--expected-sha256", database_sha],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise AssertionError(f"snapshot validation regressed: {result.stderr}")


def main() -> None:
    run_reference("valid-empty", empty_reference(), success=True)
    run_reference("scope-wrong", {**empty_reference(), "scope": {"game": "传奇2", "operator": "光通", "version": "1.45", "policy": "strict-evidence"}}, success=False)

    duplicate_source = one_source()
    duplicate_source["sources"].append(copy.deepcopy(duplicate_source["sources"][0]))
    run_reference("duplicate-source-id", duplicate_source, success=False)

    illegal_level = one_source()
    illegal_level["sources"][0]["level"] = 4
    run_reference("illegal-level", illegal_level, success=False)

    duplicate_name = one_item()
    duplicate_name["items"].append(copy.deepcopy(duplicate_name["items"][0]))
    run_reference("duplicate-item-name", duplicate_name, success=False)

    dangling_source = one_item()
    dangling_source["items"][0]["sourceIds"] = ["missing"]
    run_reference("dangling-source-id", dangling_source, success=False)

    empty_source_ids = one_item()
    empty_source_ids["items"][0]["sourceIds"] = []
    run_reference("empty-source-ids", empty_source_ids, success=False)

    illegal_status = one_item()
    illegal_status["items"][0]["status"] = "confirmed"
    run_reference("illegal-status", illegal_status, success=False)

    excluded_without_version = one_item()
    excluded_without_version["items"][0]["status"] = "excluded-later-version"
    run_reference("excluded-without-introduced-version", excluded_without_version, success=False)

    wrong_type = one_item()
    wrong_type["items"][0]["aliases"] = "测试剑"
    run_reference("wrong-field-type", wrong_type, success=False)

    run_snapshot_regression()
    print("reference verifier regression checks passed")


if __name__ == "__main__":
    main()
