#!/usr/bin/env python3
"""Validate a read-only Mir3 System.db export."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


class VerificationArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        fail(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_mapping(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: object, label: str, *, non_empty: bool = False) -> list:
    if not isinstance(value, list):
        fail(f"{label} must be an array")
    if non_empty and not value:
        fail(f"{label} must not be empty")
    return value


def require_field(mapping: dict, field: str, label: str) -> object:
    if field not in mapping:
        fail(f"{label}.{field} is required")
    return mapping[field]


def require_string(value: object, label: str) -> str:
    if not isinstance(value, str):
        fail(f"{label} must be a string")
    return value


def require_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        fail(f"{label} must be an integer")
    return value


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label} must be a boolean")
    return value


def validate_indexes(entries: list, label: str) -> None:
    indexes = []
    for position, entry in enumerate(entries):
        mapping = require_mapping(entry, f"{label}[{position}]")
        indexes.append(require_int(require_field(mapping, "index", f"{label}[{position}]"), f"{label}[{position}].index"))
    if len(indexes) != len(set(indexes)):
        fail(f"{label} contains duplicate index values")


def validate_items(items: list) -> None:
    validate_indexes(items, "items")
    for position, item in enumerate(items):
        mapping = require_mapping(item, f"items[{position}]")
        label = f"items[{position}]"
        require_string(require_field(mapping, "name", label), f"{label}.name")
        require_string(require_field(mapping, "itemType", label), f"{label}.itemType")
        require_string(require_field(mapping, "requiredClass", label), f"{label}.requiredClass")
        require_int(require_field(mapping, "requiredAmount", label), f"{label}.requiredAmount")
        require_int(require_field(mapping, "image", label), f"{label}.image")


def validate_monsters(monsters: list) -> None:
    validate_indexes(monsters, "monsters")
    for position, monster in enumerate(monsters):
        mapping = require_mapping(monster, f"monsters[{position}]")
        label = f"monsters[{position}]"
        require_string(require_field(mapping, "name", label), f"{label}.name")
        require_int(require_field(mapping, "level", label), f"{label}.level")
        require_int(require_field(mapping, "ai", label), f"{label}.ai")
        require_int(require_field(mapping, "image", label), f"{label}.image")
        require_bool(require_field(mapping, "isBoss", label), f"{label}.isBoss")


def validate_sets(sets: list) -> None:
    validate_indexes(sets, "sets")
    for position, set_info in enumerate(sets):
        mapping = require_mapping(set_info, f"sets[{position}]")
        label = f"sets[{position}]"
        require_string(require_field(mapping, "name", label), f"{label}.name")
        groups = require_list(require_field(mapping, "groups", label), f"{label}.groups")
        for group_position, group in enumerate(groups):
            group_mapping = require_mapping(group, f"{label}.groups[{group_position}]")
            group_label = f"{label}.groups[{group_position}]"
            require_string(require_field(group_mapping, "name", group_label), f"{group_label}.name")
            require_int(require_field(group_mapping, "requiredNumItems", group_label), f"{group_label}.requiredNumItems")
            item_names = require_list(require_field(group_mapping, "items", group_label), f"{group_label}.items")
            for item_position, item_name in enumerate(item_names):
                require_string(item_name, f"{group_label}.items[{item_position}]")


def validate(snapshot: object, database_path: Path, expected_sha: str) -> None:
    document = require_mapping(snapshot, "snapshot")
    for key in ("database", "items", "monsters", "sets"):
        require_field(document, key, "snapshot")

    database = require_mapping(document["database"], "database")
    database_label = require_string(require_field(database, "path", "database"), "database.path")
    if database_label != "Database/System.db":
        fail("database.path must be Database/System.db")
    snapshot_sha = require_string(require_field(database, "sha256", "database"), "database.sha256")
    require_string(require_field(database, "exportedAt", "database"), "database.exportedAt")
    items = require_list(document["items"], "items", non_empty=True)
    monsters = require_list(document["monsters"], "monsters", non_empty=True)
    sets = require_list(document["sets"], "sets", non_empty=True)
    validate_items(items)
    validate_monsters(monsters)
    validate_sets(sets)

    actual_sha = sha256(database_path)
    if not (snapshot_sha.lower() == actual_sha == expected_sha.lower()):
        fail(
            "database SHA-256 mismatch: "
            f"snapshot={snapshot_sha}, actual={actual_sha}, expected={expected_sha.lower()}"
        )


def main() -> None:
    parser = VerificationArgumentParser()
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
    except (OSError, json.JSONDecodeError) as exception:
        fail(f"cannot read snapshot: {exception}")
    validate(snapshot, database_path, args.expected_sha256)
    print("verification passed")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exception:
        fail(str(exception))
