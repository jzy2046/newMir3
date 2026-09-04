#!/usr/bin/env python3
"""Regression checks for strict snapshot validation."""

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "tools" / "mir3-data-audit" / "verify_snapshot.py"


def run_case(name: str, snapshot: dict, database: Path, expected_sha: str, success: bool) -> None:
    snapshot_path = database.parent / f"{name}.json"
    snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(VERIFY), "--snapshot", str(snapshot_path), "--database", str(database),
         "--expected-sha256", expected_sha],
        capture_output=True,
        text=True,
        check=False,
    )
    if success:
        if result.returncode != 0:
            raise AssertionError(f"{name} unexpectedly failed: {result.stderr}")
        return
    if result.returncode != 1 or not result.stderr.startswith("verification failed:"):
        raise AssertionError(f"{name} did not fail cleanly: rc={result.returncode}, stderr={result.stderr!r}")


def run_text_case(name: str, snapshot_text: str, database: Path, expected_sha: str) -> None:
    snapshot_path = database.parent / f"{name}.json"
    snapshot_path.write_text(snapshot_text, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(VERIFY), "--snapshot", str(snapshot_path), "--database", str(database),
         "--expected-sha256", expected_sha],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 1 or not result.stderr.startswith("verification failed:") or "Traceback" in result.stderr:
        raise AssertionError(f"{name} did not fail cleanly: rc={result.returncode}, stderr={result.stderr!r}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="mir3-verify-test-") as directory:
        database = Path(directory) / "System.db"
        database.write_bytes(b"test database")
        database_sha = hashlib.sha256(database.read_bytes()).hexdigest()
        valid = {
            "database": {"path": "Database/System.db", "sha256": database_sha, "exportedAt": "2026-09-04T00:00:00Z"},
            "items": [{"index": 1, "name": "item", "itemType": "Nothing", "requiredClass": "All", "requiredAmount": 0, "image": 0}],
            "monsters": [{"index": 1, "name": "monster", "level": 1, "ai": 1, "image": 1, "isBoss": False}],
            "sets": [{"index": 1, "name": "set", "groups": [{"name": "group", "requiredNumItems": 1, "items": ["item"]}]}],
        }
        run_case("valid", valid, database, database_sha, success=True)
        run_text_case("invalid-json", "{", database, database_sha)

        for name, mutation in (
            ("scalar-document", None),
            ("database-not-object", {**valid, "database": []}),
            ("items-not-array", {**valid, "items": {}}),
            ("monsters-empty", {**valid, "monsters": []}),
            ("sets-entry-not-object", {**valid, "sets": [1]}),
        ):
            run_case(name, mutation, database, database_sha, success=False)

        for top_level_field in ("database", "items", "monsters", "sets"):
            missing = copy.deepcopy(valid)
            del missing[top_level_field]
            run_case(f"missing-{top_level_field}", missing, database, database_sha, success=False)

        wrong_database_path = copy.deepcopy(valid)
        wrong_database_path["database"]["path"] = "/private/machine/Database/System.db"
        run_case("unstable-database-path", wrong_database_path, database, database_sha, success=False)

        field_types = {
            ("database", "path"): 1,
            ("database", "sha256"): 1,
            ("database", "exportedAt"): 1,
            ("items", 0, "index"): True,
            ("items", 0, "name"): 1,
            ("items", 0, "itemType"): 1,
            ("items", 0, "requiredClass"): 1,
            ("items", 0, "requiredAmount"): True,
            ("items", 0, "image"): True,
            ("monsters", 0, "index"): True,
            ("monsters", 0, "name"): 1,
            ("monsters", 0, "level"): True,
            ("monsters", 0, "ai"): True,
            ("monsters", 0, "image"): True,
            ("monsters", 0, "isBoss"): 1,
            ("sets", 0, "index"): True,
            ("sets", 0, "name"): 1,
            ("sets", 0, "groups"): {},
            ("sets", 0, "groups", 0, "name"): 1,
            ("sets", 0, "groups", 0, "requiredNumItems"): True,
            ("sets", 0, "groups", 0, "items"): {},
            ("sets", 0, "groups", 0, "items", 0): 1,
        }
        for number, (path, wrong_value) in enumerate(field_types.items()):
            malformed = copy.deepcopy(valid)
            target = malformed
            for part in path[:-1]:
                target = target[part]
            target[path[-1]] = wrong_value
            run_case(f"wrong-type-{number}", malformed, database, database_sha, success=False)

            if isinstance(path[-1], str):
                missing = copy.deepcopy(valid)
                target = missing
                for part in path[:-1]:
                    target = target[part]
                del target[path[-1]]
                run_case(f"missing-field-{number}", missing, database, database_sha, success=False)

        cases = (
            ("unhashable-index", ("items", 0, "index"), []),
        )
        for name, path, value in cases:
            malformed = copy.deepcopy(valid)
            target = malformed
            for part in path[:-1]:
                target = target[part]
            target[path[-1]] = value
            run_case(name, malformed, database, database_sha, success=False)

    print("snapshot verifier regression checks passed")


if __name__ == "__main__":
    main()
