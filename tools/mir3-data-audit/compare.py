#!/usr/bin/env python3
"""Compare a read-only Mir3 System.db snapshot with an evidence reference."""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


KINDS = ("items", "monsters", "sets")
REFERENCE_STATUSES = {"confirmed-145", "uncertain-version", "excluded-later-version"}
REFERENCE_SCOPE = {"game": "传奇3", "operator": "光通", "version": "1.45", "policy": "strict-evidence"}
REFERENCE_CATEGORIES = {"items", "monsters", "sets", "version-history"}


class CompareError(ValueError):
    """An input or output error that must be reported without a traceback."""


class CompareArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise CompareError(message)


def normalize_name(name: str) -> str:
    """Normalize only compatibility forms and Unicode whitespace for exact lookup."""
    return "".join(character for character in unicodedata.normalize("NFKC", name) if not character.isspace())


def build_reference_index(reference: dict[str, Any]) -> dict[str, dict[str, dict[str, Any]]]:
    """Index official formal names and explicit aliases, rejecting ambiguity."""
    if not isinstance(reference, dict):
        raise CompareError("reference must be a JSON object")
    result: dict[str, dict[str, dict[str, Any]]] = {kind: {} for kind in KINDS}
    for kind in KINDS:
        entries = reference.get(kind)
        if not isinstance(entries, list):
            raise CompareError(f"reference.{kind} must be an array")
        for position, entry in enumerate(entries):
            label = f"reference.{kind}[{position}]"
            if not isinstance(entry, dict):
                raise CompareError(f"{label} must be an object")
            name = require_non_empty_string(entry.get("name"), f"{label}.name")
            aliases = entry.get("aliases")
            if not isinstance(aliases, list) or not all(isinstance(alias, str) and alias.strip() for alias in aliases):
                raise CompareError(f"{label}.aliases must be an array of non-empty strings")
            status = entry.get("status")
            if status not in REFERENCE_STATUSES:
                raise CompareError(f"{label}.status is invalid")
            for candidate, match_kind in [(name, "exact"), *[(alias, "alias") for alias in aliases]]:
                normalized = normalize_name(candidate)
                if not normalized:
                    raise CompareError(f"{label} has an empty normalized name")
                if normalized in result[kind]:
                    previous = result[kind][normalized]["entry"]["name"]
                    raise CompareError(
                        f"ambiguous {kind} normalized name {normalized!r}: {previous!r} conflicts with {name!r}"
                    )
                result[kind][normalized] = {"entry": entry, "match_kind": match_kind}
    return result


def match_record(record: str | dict[str, Any], kind: str,
                 reference_index: dict[str, dict[str, dict[str, Any]]]) -> dict[str, Any]:
    """Match a local name exactly against an official name or explicit alias only."""
    if kind not in KINDS:
        raise CompareError(f"unknown record type: {kind}")
    name = record.get("name") if isinstance(record, dict) else record
    if not isinstance(name, str):
        raise CompareError(f"local {kind} name must be a string")
    found = reference_index.get(kind, {}).get(normalize_name(name))
    if found is None:
        return {
            "entry": None, "match_kind": "unmatched", "judgment": "版本不确定",
            "basis": "未在官方正式名称或显式别名中找到精确匹配", "delete_candidate": False,
        }
    entry = found["entry"]
    status = entry["status"]
    match_kind = found["match_kind"]
    if status == "confirmed-145":
        judgment = "确认保留" if match_kind == "exact" else "疑似同物异名"
    elif status == "uncertain-version":
        judgment = "版本不确定"
    else:
        judgment = "确认非1.45/建议删除"
    basis = {
        "exact": "与官方正式名称精确匹配",
        "alias": "与官方显式别名精确匹配",
    }[match_kind] + f"；官方条目状态：{status}"
    if status == "excluded-later-version":
        basis += f"；引入版本：{entry['introducedVersion']}"
    return {
        "entry": entry, "match_kind": match_kind, "judgment": judgment, "basis": basis,
        "delete_candidate": status == "excluded-later-version",
    }


def escape_markdown(value: object) -> str:
    """Keep untrusted data inside one Markdown table cell without emitting HTML."""
    text = str(value)
    text = text.replace("\\", "\\\\")
    text = text.replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (text.replace("|", "\\|").replace("!", "\\!").replace("[", "\\[")
            .replace("]", "\\]").replace("(", "\\(").replace(")", "\\)"))


def render_markdown(snapshot: dict[str, Any], reference: dict[str, Any], sources_markdown: str) -> str:
    """Render the full, evidence-preserving comparison report without writing files."""
    validate_snapshot(snapshot)
    validate_reference_document(reference)
    if not isinstance(sources_markdown, str):
        raise CompareError("sources markdown must be text")
    index = build_reference_index(reference)
    lines: list[str] = [
        "# 传奇3 光通 1.45 数据完整对比报告",
        "",
        "## 口径与安全说明",
        "",
        "- 仅以官方正式名称及其显式别名做 Unicode NFKC 与 Unicode 空白归一化后的精确匹配；不做繁简转换或模糊匹配。",
        "- 未匹配或证据版本不确定均标为“版本不确定”，不得仅因缺少资料建议删除；仅有明确后续版本排除证据的条目进入删除候选。",
        "- 本报告为只读快照比对，未修改 System.db、快照、官方参考或来源文档。",
        "",
        "## 快照绑定信息",
        "",
        "| System.db逻辑路径 | SHA-256 | exportedAt |",
        "| --- | --- | --- |",
        f"| {escape_markdown(snapshot['database']['path'])} | {escape_markdown(snapshot['database']['sha256'])} | {escape_markdown(snapshot['database']['exportedAt'])} |",
        "",
        "## 数量汇总",
        "",
        "| 类型 | 本服快照数 | 官方参考数 | 确认保留 | 疑似同物异名 | 建议删除 | 版本不确定 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    all_matches: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = {}
    for kind in KINDS:
        matches = [(record, match_record(record, kind, index)) for record in sorted(snapshot[kind], key=lambda row: row["index"])]
        all_matches[kind] = matches
        count = Counter(match["judgment"] for _, match in matches)
        lines.append(
            f"| {kind_label(kind)} | {len(matches)} | {len(reference[kind])} | "
            f"{count['确认保留']} | {count['疑似同物异名']} | {count['确认非1.45/建议删除']} | {count['版本不确定']} |"
        )
    lines.extend(["", "## 来源表", "", "| 来源ID | 标题 | 链接 | 级别 | 版本 | 分类 | 定位 | 说明 |", "| --- | --- | --- | ---: | --- | --- | --- | --- |"])
    for source in reference["sources"]:
        lines.append(
            "| " + " | ".join(escape_markdown(source[field]) for field in ("id", "title", "url", "level"))
            + " | " + escape_markdown(", ".join(source["versions"]))
            + " | " + escape_markdown(", ".join(source["categories"]))
            + " | " + escape_markdown(source["locator"])
            + " | " + escape_markdown(source["notes"]) + " |"
        )
    lines.append(f"| 输入来源文档 | 已读取 | - | - | - | - | - | {escape_markdown(sources_markdown)} |")
    lines.extend(render_official_table("items", reference["items"]))
    lines.extend(render_local_table("items", all_matches["items"], index["items"]))
    lines.extend(render_official_table("monsters", reference["monsters"]))
    lines.extend(render_local_table("monsters", all_matches["monsters"], index["items"]))
    lines.extend(render_official_table("sets", reference["sets"]))
    lines.extend(render_local_table("sets", all_matches["sets"], index["items"]))
    lines.extend(render_summary_table("建议删除候选", all_matches, lambda match: match["delete_candidate"]))
    lines.extend(render_summary_table("版本不确定项", all_matches, lambda match: match["judgment"] == "版本不确定"))
    return "\n".join(lines) + "\n"


def render_official_table(kind: str, entries: list[dict[str, Any]]) -> list[str]:
    heading = {"items": "官方物品完整表", "monsters": "官方怪物完整表", "sets": "官方套装表"}[kind]
    field = {"items": "category", "monsters": "area", "sets": "items"}[kind]
    rows = ["", f"## {heading}", "", "| 正式名 | 别名 | 类别/区域/组成 | 状态 | 引入版本 | 来源ID | 说明 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for entry in entries:
        detail = entry[field] if kind != "sets" else ", ".join(entry[field])
        rows.append("| " + " | ".join((
            escape_markdown(entry["name"]), escape_markdown(", ".join(entry["aliases"])),
            escape_markdown(detail), escape_markdown(entry["status"]), escape_markdown(entry.get("introducedVersion", "—")),
            escape_markdown(", ".join(entry["sourceIds"])), escape_markdown(entry["notes"]),
        )) + " |")
    return rows


def render_local_table(kind: str, records: list[tuple[dict[str, Any], dict[str, Any]]],
                       item_index: dict[str, dict[str, Any]]) -> list[str]:
    heading = {"items": "本服物品完整对比表", "monsters": "本服怪物完整对比表", "sets": "本服套装对比表"}[kind]
    extras = {
        "items": "本地字段（类型/职业/需求/图像）",
        "monsters": "本地字段（等级/AI/图像/Boss）",
        "sets": "数据库组成 | 官方组成 | 差异/缺失部件",
    }[kind]
    separator = " | ".join(["---:"] + ["---"] * (10 if kind == "sets" else 8))
    rows = ["", f"## {heading}", "", f"| 快照索引 | 数据库原名 | 官方1.45名称 | 匹配状态 | 匹配方式 | 判断依据 | 证据来源 | 处理建议 | {extras} |", f"| {separator} |"]
    for record, match in records:
        entry = match["entry"]
        official_name = entry["name"] if entry else "-"
        source_ids = ", ".join(entry["sourceIds"]) if entry else "-"
        action = match["judgment"]
        marker = f"<!-- local:{kind[:-1]}:{record['index']} -->"
        common = [
            f"{marker}{record['index']}", record["name"], official_name, action, match["match_kind"],
            match["basis"], source_ids, action,
        ]
        if kind == "items":
            common.append(f"{record['itemType']}/{record['requiredClass']}/{record['requiredAmount']}/{record['image']}")
        elif kind == "monsters":
            common.append(f"{record['level']}/{record['ai']}/{record['image']}/{record['isBoss']}")
        else:
            local_components = set_components(record)
            official_components = list(entry["items"]) if entry else []
            common.extend((
                local_components,
                ", ".join(official_components) if entry else "-",
                component_difference(set_component_names(record), official_components, item_index) if entry else "无官方对照",
            ))
        rows.append("| " + " | ".join(escape_markdown(value) if position else value for position, value in enumerate(common)) + " |")
    return rows


def render_summary_table(heading: str, matches: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]], predicate: Any) -> list[str]:
    rows = ["", f"## {heading}", "", "| 类型 | 快照索引 | 数据库原名 | 官方名称 | 判断依据 |", "| --- | ---: | --- | --- | --- |"]
    for kind in KINDS:
        for record, match in matches[kind]:
            if predicate(match):
                official_name = match["entry"]["name"] if match["entry"] else "-"
                rows.append("| " + " | ".join(escape_markdown(value) for value in (
                    kind_label(kind), record["index"], record["name"], official_name, match["basis"],
                )) + " |")
    return rows


def set_components(record: dict[str, Any]) -> str:
    return "; ".join(
        f"{group['name']}({group['requiredNumItems']}): " + ", ".join(group["items"])
        for group in record["groups"]
    )


def set_component_names(record: dict[str, Any]) -> list[str]:
    return [item for group in record["groups"] for item in group["items"]]


def component_difference(local_names: list[str], official_components: list[str],
                         item_index: dict[str, dict[str, Any]]) -> str:
    local_keys = [canonical_item_name(name, item_index) for name in local_names]
    official_keys = [canonical_item_name(name, item_index) for name in official_components]
    local_counts = Counter(local_keys)
    official_counts = Counter(official_keys)
    missing_budget = official_counts - local_counts
    extra_budget = local_counts - official_counts
    missing = consume_difference(official_components, official_keys, missing_budget)
    extras = consume_difference(local_names, local_keys, extra_budget)
    messages = []
    if missing:
        messages.append("缺少：" + ", ".join(missing))
    if extras:
        messages.append("本服额外：" + ", ".join(extras))
    return "；".join(messages) if messages else "组成一致"


def canonical_item_name(name: str, item_index: dict[str, dict[str, Any]]) -> str:
    found = item_index.get(normalize_name(name))
    return normalize_name(found["entry"]["name"] if found else name)


def consume_difference(names: list[str], normalized_names: list[str], budget: Counter[str]) -> list[str]:
    result = []
    for name, normalized in zip(names, normalized_names):
        if budget[normalized]:
            result.append(name)
            budget[normalized] -= 1
    return result


def kind_label(kind: str) -> str:
    return {"items": "物品", "monsters": "怪物", "sets": "套装"}[kind]


def require_non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CompareError(f"{label} must be a non-empty string")
    return value


def require_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CompareError(f"{label} must be an integer")
    return value


def normalized_numeric_version(version: str) -> tuple[int, ...] | None:
    pieces = version.split(".")
    if not pieces or any(not piece.isdecimal() for piece in pieces):
        return None
    result = [int(piece) for piece in pieces]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def validate_snapshot(snapshot: object) -> None:
    if not isinstance(snapshot, dict):
        raise CompareError("snapshot must be a JSON object")
    database = snapshot.get("database")
    if not isinstance(database, dict):
        raise CompareError("snapshot.database must be an object")
    for field in ("path", "sha256", "exportedAt"):
        require_non_empty_string(database.get(field), f"snapshot.database.{field}")
    validators = {
        "items": (("name", str), ("itemType", str), ("requiredClass", str), ("requiredAmount", int), ("image", int)),
        "monsters": (("name", str), ("level", int), ("ai", int), ("image", int), ("isBoss", bool)),
        "sets": (("name", str), ("groups", list)),
    }
    for kind, fields in validators.items():
        records = snapshot.get(kind)
        if not isinstance(records, list):
            raise CompareError(f"snapshot.{kind} must be an array")
        indexes = set()
        for position, record in enumerate(records):
            label = f"snapshot.{kind}[{position}]"
            if not isinstance(record, dict):
                raise CompareError(f"{label} must be an object")
            index = require_int(record.get("index"), f"{label}.index")
            if index in indexes:
                raise CompareError(f"snapshot.{kind} contains duplicate index {index}")
            indexes.add(index)
            for field, type_ in fields:
                value = record.get(field)
                if type_ is int:
                    require_int(value, f"{label}.{field}")
                elif not isinstance(value, type_):
                    raise CompareError(f"{label}.{field} has an invalid type")
            if kind == "sets":
                validate_set_groups(record["groups"], label)


def validate_set_groups(groups: list[Any], label: str) -> None:
    for position, group in enumerate(groups):
        group_label = f"{label}.groups[{position}]"
        if not isinstance(group, dict):
            raise CompareError(f"{group_label} must be an object")
        if not isinstance(group.get("name"), str):
            raise CompareError(f"{group_label}.name must be a string")
        require_int(group.get("requiredNumItems"), f"{group_label}.requiredNumItems")
        items = group.get("items")
        if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
            raise CompareError(f"{group_label}.items must be an array of strings")


def validate_reference_document(reference: object) -> None:
    if not isinstance(reference, dict):
        raise CompareError("reference must be a JSON object")
    for field in ("scope", "sources", *KINDS):
        if field not in reference:
            raise CompareError(f"reference.{field} is required")
    if not isinstance(reference["scope"], dict):
        raise CompareError("reference.scope must be an object")
    for field, expected in REFERENCE_SCOPE.items():
        if reference["scope"].get(field) != expected:
            raise CompareError(f"reference.scope.{field} must be {expected}")
    if not isinstance(reference["sources"], list):
        raise CompareError("reference.sources must be an array")
    source_ids = set()
    for position, source in enumerate(reference["sources"]):
        label = f"reference.sources[{position}]"
        if not isinstance(source, dict):
            raise CompareError(f"{label} must be an object")
        for field in ("id", "title", "url", "locator", "notes"):
            require_non_empty_string(source.get(field), f"{label}.{field}")
        level = require_int(source.get("level"), f"{label}.level")
        if level not in (1, 2, 3):
            raise CompareError(f"{label}.level must be 1, 2, or 3")
        for field in ("versions", "categories"):
            values = source.get(field)
            if not isinstance(values, list) or not all(isinstance(value, str) and value.strip() for value in values):
                raise CompareError(f"{label}.{field} must be an array of non-empty strings")
        if any(category not in REFERENCE_CATEGORIES for category in source["categories"]):
            raise CompareError(f"{label}.categories contains an invalid category")
        if source["id"] in source_ids:
            raise CompareError(f"reference.sources contains duplicate id {source['id']!r}")
        source_ids.add(source["id"])
    build_reference_index(reference)
    for kind in KINDS:
        for position, entry in enumerate(reference[kind]):
            label = f"reference.{kind}[{position}]"
            references = entry.get("sourceIds")
            if not isinstance(references, list) or not references or not all(isinstance(value, str) for value in references):
                raise CompareError(f"{label}.sourceIds must be a non-empty array of strings")
            if any(value not in source_ids for value in references):
                raise CompareError(f"{label}.sourceIds references an unknown source")
            referenced_sources = [source for source in reference["sources"] if source["id"] in references]
            if not any(kind in source["categories"] for source in referenced_sources):
                raise CompareError(f"{label} has no source categorized for {kind}")
            require_non_empty_string(entry.get("notes"), f"{label}.notes")
            field = {"items": "category", "monsters": "area", "sets": "items"}[kind]
            if kind == "sets":
                values = entry.get(field)
                if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                    raise CompareError(f"{label}.items must be an array of strings")
            else:
                require_non_empty_string(entry.get(field), f"{label}.{field}")
            status = entry["status"]
            if status == "confirmed-145" and not any(
                source["level"] in (1, 2) and "1.45" in source["versions"] and kind in source["categories"]
                for source in referenced_sources
            ):
                raise CompareError(f"{label} lacks level 1/2 evidence for 1.45")
            if status == "excluded-later-version":
                introduced = require_non_empty_string(entry.get("introducedVersion"), f"{label}.introducedVersion")
                normalized = normalized_numeric_version(introduced)
                if normalized is None or normalized <= (1, 45):
                    raise CompareError(f"{label}.introducedVersion must be later than 1.45")
                if not any(
                    source["level"] in (1, 2) and kind in source["categories"] and introduced in source["versions"]
                    for source in referenced_sources
                ) or not any(
                    source["level"] in (1, 2) and "version-history" in source["categories"] and introduced in source["versions"]
                    for source in referenced_sources
                ):
                    raise CompareError(f"{label} lacks level 1/2 evidence for {introduced}")
            elif "introducedVersion" in entry:
                raise CompareError(f"{label}.introducedVersion is only allowed for excluded-later-version")


def load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise CompareError(f"{label} does not exist: {path}")
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exception:
        raise CompareError(f"cannot read {label}: {exception}") from exception
    if not isinstance(document, dict):
        raise CompareError(f"{label} must be a JSON object")
    return document


def main(argv: list[str] | None = None) -> int:
    parser = CompareArgumentParser(prog="compare.py", add_help=True)
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--reference", required=True)
    parser.add_argument("--sources", required=True)
    parser.add_argument("--output", required=True)
    try:
        args = parser.parse_args(argv)
        snapshot_path = Path(args.snapshot)
        reference_path = Path(args.reference)
        sources_path = Path(args.sources)
        output_path = Path(args.output)
        snapshot = load_json(snapshot_path, "snapshot")
        reference = load_json(reference_path, "reference")
        if not sources_path.is_file():
            raise CompareError(f"sources does not exist: {sources_path}")
        try:
            sources_markdown = sources_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exception:
            raise CompareError(f"cannot read sources: {exception}") from exception
        report = render_markdown(snapshot, reference, sources_markdown)
        with output_path.open("x", encoding="utf-8", newline="\n") as output:
            output.write(report)
    except (CompareError, OSError) as exception:
        print(f"compare failed: {exception}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
