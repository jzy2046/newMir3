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


def run_cli_failure(name: str, arguments: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(VERIFY), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 1 or not result.stderr.startswith("verification failed:") or "Traceback" in result.stderr:
        raise AssertionError(f"{name} did not fail cleanly: rc={result.returncode}, stderr={result.stderr!r}")


def empty_reference() -> dict:
    return {
        "scope": {"game": "传奇3", "operator": "光通", "version": "1.45", "policy": "strict-evidence"},
        "sources": [],
        "items": [],
        "monsters": [],
        "sets": [],
    }


def one_source(*, level: int = 1, versions: list[str] | None = None, categories: list[str] | None = None) -> dict:
    reference = empty_reference()
    reference["sources"] = [{
        "id": "s1",
        "title": "官方资料",
        "url": "https://example.test/source",
        "level": level,
        "notes": "用于测试",
        "versions": ["1.45"] if versions is None else versions,
        "categories": ["items", "monsters", "sets", "version-history"] if categories is None else categories,
        "locator": "正文第1段",
    }]
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


def one_monster() -> dict:
    reference = one_source()
    reference["monsters"] = [{
        "name": "测试怪物",
        "aliases": [],
        "status": "confirmed-145",
        "sourceIds": ["s1"],
        "notes": "可核验",
        "area": "测试地图",
    }]
    return reference


def one_set() -> dict:
    reference = one_source()
    reference["sets"] = [{
        "name": "测试套装",
        "aliases": [],
        "status": "confirmed-145",
        "sourceIds": ["s1"],
        "notes": "可核验",
        "items": ["测试物品"],
    }]
    return reference


def one_excluded(version: str = "1.46", *, level: int = 1) -> dict:
    reference = one_source(
        level=level,
        versions=[version],
        categories=["items", "version-history"],
    )
    reference["items"] = [{
        "name": "后续物品",
        "aliases": [],
        "status": "excluded-later-version",
        "sourceIds": ["s1"],
        "notes": "明确后续版本引入",
        "category": "weapon",
        "introducedVersion": version,
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
    run_cli_failure("partial-snapshot-mode", ["--snapshot", "snapshot.json"])
    run_cli_failure(
        "mixed-reference-and-snapshot-mode",
        ["--reference", str(ROOT / "audit" / "mir3-145" / "official-reference.json"), "--snapshot", "snapshot.json"],
    )
    run_cli_failure("no-arguments", [])

    run_reference("valid-empty", empty_reference(), success=True)
    run_reference("scope-wrong", {**empty_reference(), "scope": {"game": "传奇2", "operator": "光通", "version": "1.45", "policy": "strict-evidence"}}, success=False)

    duplicate_source = one_source()
    duplicate_source["sources"].append(copy.deepcopy(duplicate_source["sources"][0]))
    run_reference("duplicate-source-id", duplicate_source, success=False)

    illegal_level = one_source()
    illegal_level["sources"][0]["level"] = 4
    run_reference("illegal-level", illegal_level, success=False)

    for field in ("id", "title", "url", "notes", "locator"):
        blank_source = one_source()
        blank_source["sources"][0][field] = "  "
        run_reference(f"blank-source-{field}", blank_source, success=False)
    blank_versions = one_source(versions=[])
    run_reference("empty-source-versions", blank_versions, success=False)
    blank_version_value = one_source(versions=["  "])
    run_reference("blank-source-version-value", blank_version_value, success=False)
    blank_categories = one_source(categories=[])
    run_reference("empty-source-categories", blank_categories, success=False)
    illegal_category = one_source(categories=["quests"])
    run_reference("illegal-source-category", illegal_category, success=False)
    blank_category_value = one_source(categories=["  "])
    run_reference("blank-source-category-value", blank_category_value, success=False)

    category_mismatch = one_item()
    category_mismatch["sources"][0]["categories"] = ["monsters"]
    run_reference("record-category-mismatch", category_mismatch, success=False)
    for factory, collection in ((one_monster, "monsters"), (one_set, "sets")):
        mismatched = factory()
        mismatched["sources"][0]["categories"] = ["items"]
        run_reference(f"{collection}-category-mismatch", mismatched, success=False)

    uncertain_level3 = one_source(level=3, categories=["items"], versions=["unknown"])
    uncertain_level3["items"] = copy.deepcopy(one_item()["items"])
    uncertain_level3["items"][0]["status"] = "uncertain-version"
    run_reference("uncertain-level3-only", uncertain_level3, success=True)

    confirmed_level3 = one_source(level=3, categories=["items"], versions=["1.45"])
    confirmed_level3["items"] = copy.deepcopy(one_item()["items"])
    run_reference("confirmed-level3-only", confirmed_level3, success=False)

    excluded_level3 = one_excluded(level=3)
    run_reference("excluded-level3-only", excluded_level3, success=False)
    excluded_without_history = one_excluded()
    excluded_without_history["sources"][0]["categories"] = ["items"]
    run_reference("excluded-without-version-history", excluded_without_history, success=False)
    run_reference("excluded-at-1.45", one_excluded("1.45"), success=False)
    run_reference("excluded-at-1.4", one_excluded("1.4"), success=False)
    run_reference("excluded-at-1.45.0", one_excluded("1.45.0"), success=False)
    run_reference("excluded-at-1.45.0.0", one_excluded("1.45.0.0"), success=False)
    run_reference("excluded-illegal-version", one_excluded("v1.46"), success=False)
    run_reference("excluded-at-1.45.1", one_excluded("1.45.1"), success=True)
    run_reference("excluded-at-1.46", one_excluded("1.46"), success=True)
    run_reference("excluded-at-2.0", one_excluded("2.0"), success=True)

    blank_item_name = one_item()
    blank_item_name["items"][0]["name"] = "  "
    run_reference("blank-item-name", blank_item_name, success=False)
    blank_item_notes = one_item()
    blank_item_notes["items"][0]["notes"] = "  "
    run_reference("blank-item-notes", blank_item_notes, success=False)
    blank_item_category = one_item()
    blank_item_category["items"][0]["category"] = "  "
    run_reference("blank-item-category", blank_item_category, success=False)
    blank_alias = one_item()
    blank_alias["items"][0]["aliases"] = ["  "]
    run_reference("blank-item-alias", blank_alias, success=False)
    blank_monster_area = one_monster()
    blank_monster_area["monsters"][0]["area"] = "  "
    run_reference("blank-monster-area", blank_monster_area, success=False)
    blank_set_name = one_set()
    blank_set_name["sets"][0]["name"] = "  "
    run_reference("blank-set-name", blank_set_name, success=False)
    blank_set_notes = one_set()
    blank_set_notes["sets"][0]["notes"] = "  "
    run_reference("blank-set-notes", blank_set_notes, success=False)
    blank_set_item = one_set()
    blank_set_item["sets"][0]["items"] = ["  "]
    run_reference("blank-set-item-name", blank_set_item, success=False)

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
