#!/usr/bin/env python3
"""Validate a read-only Mir3 System.db export."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--database", required=True)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()

    snapshot_path = Path(args.snapshot)
    database_path = Path(args.database)
    if not snapshot_path.is_file():
        fail(f"snapshot does not exist: {snapshot_path}")
    if not database_path.is_file():
        fail(f"database does not exist: {database_path}")

    try:
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read snapshot: {exc}")

    required_top_level = {"database", "items", "monsters", "sets"}
    missing = required_top_level.difference(snapshot)
    if missing:
        fail(f"missing top-level key(s): {', '.join(sorted(missing))}")
    if not isinstance(snapshot["database"], dict):
        fail("database must be an object")

    for collection_name in ("items", "monsters", "sets"):
        collection = snapshot[collection_name]
        if not isinstance(collection, list) or not collection:
            fail(f"{collection_name} must be a non-empty array")
        indexes = []
        for entry in collection:
            if not isinstance(entry, dict) or "index" not in entry:
                fail(f"{collection_name} entries must contain index")
            indexes.append(entry["index"])
        if len(indexes) != len(set(indexes)):
            fail(f"{collection_name} contains duplicate index values")

    snapshot_sha = snapshot["database"].get("sha256")
    actual_sha = sha256(database_path)
    expected_sha = args.expected_sha256.lower()
    if not isinstance(snapshot_sha, str):
        fail("database.sha256 must be a string")
    if not (snapshot_sha.lower() == actual_sha == expected_sha):
        fail(
            "database SHA-256 mismatch: "
            f"snapshot={snapshot_sha}, actual={actual_sha}, expected={expected_sha}"
        )

    print("verification passed")


if __name__ == "__main__":
    main()
