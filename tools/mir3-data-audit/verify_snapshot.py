#!/usr/bin/env python3
"""Validate a read-only Mir3 System.db export."""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from itertools import zip_longest
from pathlib import Path
from typing import Any


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


def require_non_empty_string(value: object, label: str) -> str:
    result = require_string(value, label)
    if not result.strip():
        fail(f"{label} must not be empty")
    return result


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


REFERENCE_SCOPE = {
    "game": "传奇3",
    "operator": "光通",
    "version": "1.45",
    "policy": "strict-evidence",
}
REFERENCE_STATUSES = {"confirmed-145", "uncertain-version", "excluded-later-version"}


REFERENCE_CATEGORIES = {"items", "monsters", "sets", "version-history"}

REPORT_HEADINGS = (
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
_COMPARE_RENDERER: Any | None = None


def normalized_numeric_version(version: str) -> tuple[int, ...] | None:
    if re.fullmatch(r"\d+(?:\.\d+)*", version) is None:
        return None
    parts = [int(part) for part in version.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def validate_reference_source(source: object, position: int) -> dict:
    label = f"sources[{position}]"
    mapping = require_mapping(source, label)
    source_id = require_non_empty_string(require_field(mapping, "id", label), f"{label}.id")
    require_non_empty_string(require_field(mapping, "title", label), f"{label}.title")
    require_non_empty_string(require_field(mapping, "url", label), f"{label}.url")
    level = require_int(require_field(mapping, "level", label), f"{label}.level")
    if level not in (1, 2, 3):
        fail(f"{label}.level must be 1, 2, or 3")
    require_non_empty_string(require_field(mapping, "notes", label), f"{label}.notes")
    versions = require_list(require_field(mapping, "versions", label), f"{label}.versions", non_empty=True)
    for version_position, version in enumerate(versions):
        require_non_empty_string(version, f"{label}.versions[{version_position}]")
    categories = require_list(require_field(mapping, "categories", label), f"{label}.categories", non_empty=True)
    for category_position, category in enumerate(categories):
        category = require_non_empty_string(category, f"{label}.categories[{category_position}]")
        if category not in REFERENCE_CATEGORIES:
            fail(f"{label}.categories[{category_position}] is invalid")
    require_non_empty_string(require_field(mapping, "locator", label), f"{label}.locator")
    return mapping


def validate_reference_entry(entry: object, position: int, label: str, sources: dict[str, dict], extra_field: str) -> str:
    mapping = require_mapping(entry, f"{label}[{position}]")
    entry_label = f"{label}[{position}]"
    name = require_non_empty_string(require_field(mapping, "name", entry_label), f"{entry_label}.name")
    aliases = require_list(require_field(mapping, "aliases", entry_label), f"{entry_label}.aliases")
    for alias_position, alias in enumerate(aliases):
        require_non_empty_string(alias, f"{entry_label}.aliases[{alias_position}]")
    status = require_non_empty_string(require_field(mapping, "status", entry_label), f"{entry_label}.status")
    if status not in REFERENCE_STATUSES:
        fail(f"{entry_label}.status is invalid")
    references = require_list(require_field(mapping, "sourceIds", entry_label), f"{entry_label}.sourceIds", non_empty=True)
    referenced_sources = []
    for source_position, source_id in enumerate(references):
        source_id = require_non_empty_string(source_id, f"{entry_label}.sourceIds[{source_position}]")
        if source_id not in sources:
            fail(f"{entry_label}.sourceIds[{source_position}] references unknown source {source_id!r}")
        referenced_sources.append(sources[source_id])
    if not any(label in source["categories"] for source in referenced_sources):
        fail(f"{entry_label} has no source categorized for {label}")
    require_non_empty_string(require_field(mapping, "notes", entry_label), f"{entry_label}.notes")
    if status == "excluded-later-version":
        introduced_version = require_non_empty_string(
            require_field(mapping, "introducedVersion", entry_label),
            f"{entry_label}.introducedVersion",
        )
        normalized_version = normalized_numeric_version(introduced_version)
        if normalized_version is None:
            fail(f"{entry_label}.introducedVersion must be a numeric dotted version")
        if normalized_version <= (1, 45):
            fail(f"{entry_label}.introducedVersion must be later than 1.45")
        if not any(
            source["level"] in (1, 2)
            and label in source["categories"]
            and introduced_version in source["versions"]
            for source in referenced_sources
        ):
            fail(f"{entry_label} lacks level 1/2 evidence for {introduced_version}")
        if not any(
            source["level"] in (1, 2)
            and "version-history" in source["categories"]
            and introduced_version in source["versions"]
            for source in referenced_sources
        ):
            fail(f"{entry_label} lacks level 1/2 version-history evidence for {introduced_version}")
    elif "introducedVersion" in mapping:
        fail(f"{entry_label}.introducedVersion is only allowed for excluded-later-version")
    if label != "sets":
        require_non_empty_string(require_field(mapping, extra_field, entry_label), f"{entry_label}.{extra_field}")
    if status == "confirmed-145" and not any(
        source["level"] in (1, 2) and "1.45" in source["versions"] and label in source["categories"]
        for source in referenced_sources
    ):
        fail(f"{entry_label} lacks level 1/2 evidence for 1.45")
    return name


def validate_reference(reference: object) -> None:
    document = require_mapping(reference, "reference")
    for key in ("scope", "sources", "items", "monsters", "sets"):
        require_field(document, key, "reference")

    scope = require_mapping(document["scope"], "scope")
    for key, expected in REFERENCE_SCOPE.items():
        value = require_string(require_field(scope, key, "scope"), f"scope.{key}")
        if value != expected:
            fail(f"scope.{key} must be {expected}")

    raw_sources = require_list(document["sources"], "sources")
    sources = {}
    for position, source in enumerate(raw_sources):
        source = validate_reference_source(source, position)
        source_id = source["id"]
        if source_id in sources:
            fail(f"sources contains duplicate id {source_id!r}")
        sources[source_id] = source

    for label, extra_field in (("items", "category"), ("monsters", "area")):
        entries = require_list(document[label], label)
        names = set()
        for position, entry in enumerate(entries):
            name = validate_reference_entry(entry, position, label, sources, extra_field)
            if name in names:
                fail(f"{label} contains duplicate name {name!r}")
            names.add(name)

    sets = require_list(document["sets"], "sets")
    names = set()
    for position, entry in enumerate(sets):
        name = validate_reference_entry(entry, position, "sets", sources, "items")
        entry_label = f"sets[{position}]"
        item_names = require_list(require_mapping(entry, entry_label)["items"], f"{entry_label}.items")
        for item_position, item_name in enumerate(item_names):
            require_non_empty_string(item_name, f"{entry_label}.items[{item_position}]")
        if name in names:
            fail(f"sets contains duplicate name {name!r}")
        names.add(name)


def validate_snapshot_document(snapshot: object) -> tuple[dict, str]:
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
    return document, snapshot_sha


def validate(snapshot: object, database_path: Path, expected_sha: str) -> None:
    _, snapshot_sha = validate_snapshot_document(snapshot)

    actual_sha = sha256(database_path)
    if not (snapshot_sha.lower() == actual_sha == expected_sha.lower()):
        fail(
            "database SHA-256 mismatch: "
            f"snapshot={snapshot_sha}, actual={actual_sha}, expected={expected_sha.lower()}"
        )


def compare_renderer() -> Any:
    global _COMPARE_RENDERER
    if _COMPARE_RENDERER is None:
        compare_path = Path(__file__).with_name("compare.py")
        specification = importlib.util.spec_from_file_location("mir3_report_canonical_compare", compare_path)
        if specification is None or specification.loader is None:
            fail("cannot load canonical report renderer")
        module = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(module)
        _COMPARE_RENDERER = module
    return _COMPARE_RENDERER


def validate_report(report: object, snapshot: object, reference: object, sources_text: object) -> None:
    report_text = require_non_empty_string(report, "report")
    sources = require_string(sources_text, "sources")
    snapshot_document, _ = validate_snapshot_document(snapshot)
    reference_document = require_mapping(reference, "reference")
    validate_reference(reference_document)
    report_lines = report_text.splitlines()
    for heading in REPORT_HEADINGS:
        if report_lines.count(heading) != 1:
            fail(f"report must contain required heading exactly once: {heading}")

    marker_pattern = re.compile(r"<!-- local:(item|monster|set):(-?\d+) -->")
    broad_markers = re.findall(r"<!--\s*local:[^>]*-->", report_text)
    exact_markers = marker_pattern.findall(report_text)
    if len(broad_markers) != len(exact_markers):
        fail("report contains a malformed local record marker")
    actual = Counter((kind, int(index)) for kind, index in exact_markers)
    expected = Counter(
        (kind[:-1], require_int(record["index"], f"{kind} index"))
        for kind in ("items", "monsters", "sets")
        for record in snapshot_document[kind]
    )
    if actual != expected:
        fail("report local record markers do not exactly match the snapshot")
    try:
        canonical = compare_renderer().render_markdown(snapshot_document, reference_document, sources)
    except Exception as exception:
        fail(f"cannot render canonical report: {exception}")
    if report_text != canonical:
        for line_number, (actual_line, canonical_line) in enumerate(
            zip_longest(report_text.splitlines(), canonical.splitlines()),
            start=1,
        ):
            if actual_line != canonical_line:
                fail(f"report differs from canonical output at line {line_number}")
        fail("report differs from canonical output")


def load_json_document(path_value: str, label: str) -> object:
    path = Path(path_value)
    if not path.is_file():
        fail(f"{label} does not exist: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exception:
        fail(f"cannot read {label}: {exception}")


def load_report(path_value: str) -> str:
    path = Path(path_value)
    if not path.is_file():
        fail(f"report does not exist: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exception:
        fail(f"cannot read report: {exception}")


def load_sources(path_value: str) -> str:
    path = Path(path_value)
    if not path.is_file():
        fail(f"sources does not exist: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exception:
        fail(f"cannot read sources: {exception}")


def main() -> None:
    parser = VerificationArgumentParser()
    parser.add_argument("--reference")
    parser.add_argument("--snapshot")
    parser.add_argument("--database")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--report")
    parser.add_argument("--sources")
    args = parser.parse_args()

    snapshot_validation_values = (args.database, args.expected_sha256)
    if any(value is not None for value in snapshot_validation_values) and not all(
        value is not None for value in (args.snapshot, *snapshot_validation_values)
    ):
        fail("snapshot validation requires --snapshot, --database, and --expected-sha256")
    if args.report is not None and (args.snapshot is None or args.reference is None or args.sources is None):
        fail("report validation requires --snapshot, --reference, --sources, and --report")
    if args.sources is not None and args.report is None:
        fail("--sources is only allowed with --report")
    if args.snapshot is not None and args.report is None and not all(
        value is not None for value in snapshot_validation_values
    ):
        fail("snapshot validation requires --snapshot, --database, and --expected-sha256")
    if all(value is None for value in (args.snapshot, args.reference, args.report)):
        fail("provide snapshot validation, --reference, or report validation arguments")

    snapshot = load_json_document(args.snapshot, "snapshot") if args.snapshot is not None else None
    reference = load_json_document(args.reference, "reference") if args.reference is not None else None
    if args.database is not None:
        database_path = Path(args.database)
        if not database_path.is_file():
            fail(f"database does not exist: {database_path}")
        validate(snapshot, database_path, args.expected_sha256)
    if reference is not None:
        validate_reference(reference)
    if args.report is not None:
        validate_report(load_report(args.report), snapshot, reference, load_sources(args.sources))
    print("verification passed")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exception:
        fail(str(exception))
