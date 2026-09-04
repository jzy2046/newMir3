"""Regression tests for the strict Mir3 1.45 comparison report."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMPARE = ROOT / "tools" / "mir3-data-audit" / "compare.py"


def load_compare():
    if not COMPARE.is_file():
        raise AssertionError("compare.py must provide the Mir3 comparison CLI")
    specification = importlib.util.spec_from_file_location("mir3_compare", COMPARE)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


class CompareApiTests(unittest.TestCase):
    def test_normalize_name_uses_nfkc_and_removes_unicode_whitespace(self) -> None:
        compare = load_compare()
        self.assertEqual("金创药(小)", compare.normalize_name("　金 创\t药（小）\n"))

    def test_match_record_maps_exact_alias_and_reference_statuses(self) -> None:
        compare = load_compare()
        reference = reference_document(
            items=[
                entry("Iron Sword", aliases=["铁剑"], status="confirmed-145"),
                entry("Maybe Sword", status="uncertain-version"),
                entry("Later Sword", status="excluded-later-version"),
            ]
        )
        index = compare.build_reference_index(reference)
        self.assertEqual("确认保留", compare.match_record("Iron Sword", "items", index)["judgment"])
        self.assertEqual("疑似同物异名", compare.match_record("铁剑", "items", index)["judgment"])
        self.assertEqual("版本不确定", compare.match_record("Maybe Sword", "items", index)["judgment"])
        self.assertEqual("确认非1.45/建议删除", compare.match_record("Later Sword", "items", index)["judgment"])

    def test_unknown_record_is_not_a_delete_candidate(self) -> None:
        compare = load_compare()
        result = compare.match_record("No evidence", "items", compare.build_reference_index(reference_document()))
        self.assertEqual("版本不确定", result["judgment"])
        self.assertFalse(result["delete_candidate"])

    def test_conflicting_normalized_official_names_or_aliases_are_rejected(self) -> None:
        compare = load_compare()
        reference = reference_document(items=[entry("铁剑"), entry("另一把剑", aliases=["铁 剑"])])
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            compare.build_reference_index(reference)


class MarkdownReportTests(unittest.TestCase):
    def test_report_contains_complete_sections_and_official_only_entry(self) -> None:
        compare = load_compare()
        report = compare.render_markdown(snapshot_document(), reference_document(
            items=[entry("Iron Sword"), entry("Official only")],
            monsters=[entry("Wolf", category="North")],
            sets=[entry("Starter Set", items=["Iron Sword", "Helm"])],
        ), "# source notes")
        for heading in (
            "官方物品完整表", "本服物品完整对比表", "官方怪物完整表", "本服怪物完整对比表",
            "官方套装表", "本服套装对比表", "建议删除候选", "版本不确定项",
        ):
            self.assertIn(heading, report)
        self.assertIn("Official only", report)

    def test_each_local_row_has_one_stable_marker(self) -> None:
        compare = load_compare()
        report = compare.render_markdown(snapshot_document(), reference_document(), "sources")
        for marker in ("<!-- local:item:7 -->", "<!-- local:monster:8 -->", "<!-- local:set:9 -->"):
            self.assertEqual(1, report.count(marker), marker)

    def test_set_report_shows_component_difference(self) -> None:
        compare = load_compare()
        report = compare.render_markdown(snapshot_document(), reference_document(
            sets=[entry("Starter Set", items=["Iron Sword", "Helm"])]
        ), "sources")
        self.assertIn("缺少：Helm", report)

    def test_set_components_use_explicit_item_aliases(self) -> None:
        compare = load_compare()
        snapshot = snapshot_document()
        snapshot["sets"][0]["groups"][0]["items"] = ["铁剑"]
        report = compare.render_markdown(snapshot, reference_document(
            items=[entry("Iron Sword", aliases=["铁剑"])],
            sets=[entry("Starter Set", items=["Iron Sword"])]
        ), "sources")
        self.assertIn("组成一致", report)

    def test_empty_set_group_name_from_exporter_is_rendered(self) -> None:
        compare = load_compare()
        snapshot = snapshot_document()
        snapshot["sets"][0]["groups"][0]["name"] = ""
        report = compare.render_markdown(snapshot, reference_document(), "sources")
        self.assertIn("\\(1\\): Iron Sword", report)

    def test_data_and_source_text_cannot_break_markdown_or_inject_html(self) -> None:
        compare = load_compare()
        snapshot = snapshot_document(item_name="bad|line\\name\n<script>&")
        reference = reference_document(sources=[{
            "id": "src|1", "title": "source<script>&", "url": "https://example.invalid/a|b", "level": 1,
            "versions": ["1.45"], "categories": ["items"], "locator": "p\n1", "notes": "x\\y",
        }])
        report = compare.render_markdown(snapshot, reference, "source <tag>&")
        self.assertIn("bad\\|line\\\\name\\n&lt;script&gt;&amp;", report)
        self.assertNotIn("<script>", report)
        self.assertIn("source&lt;script&gt;&amp;", report)
        self.assertIn("source &lt;tag&gt;&amp;", report)
        self.assertIn("https://example.invalid/a\\|b", report)
        link_report = compare.render_markdown(snapshot_document(item_name="[name](https://bad.invalid)"), reference_document(), "sources")
        self.assertIn("\\[name\\]\\(https://bad.invalid\\)", link_report)


class CompareCliTests(unittest.TestCase):
    def test_cli_rejects_existing_output_and_invalid_json_cleanly(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mir3-compare-test-") as directory:
            root = Path(directory)
            snapshot = root / "snapshot.json"
            reference = root / "reference.json"
            sources = root / "sources.md"
            output = root / "report.md"
            snapshot.write_text(json.dumps(snapshot_document()), encoding="utf-8")
            reference.write_text(json.dumps(reference_document()), encoding="utf-8")
            sources.write_text("sources", encoding="utf-8")
            output.write_text("already exists", encoding="utf-8")
            result = run_cli(snapshot, reference, sources, output)
            self.assertEqual(1, result.returncode)
            self.assertTrue(result.stderr.startswith("compare failed:"))

            invalid = root / "invalid.json"
            invalid.write_text("{", encoding="utf-8")
            fresh_output = root / "fresh.md"
            result = run_cli(invalid, reference, sources, fresh_output)
            self.assertEqual(1, result.returncode)
            self.assertTrue(result.stderr.startswith("compare failed:"))
            self.assertNotIn("Traceback", result.stderr)

    def test_cli_rejects_non_145_scope_and_unproven_delete_evidence(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mir3-compare-test-") as directory:
            root = Path(directory)
            snapshot = root / "snapshot.json"
            reference = root / "reference.json"
            sources = root / "sources.md"
            output = root / "report.md"
            snapshot.write_text(json.dumps(snapshot_document()), encoding="utf-8")
            sources.write_text("sources", encoding="utf-8")
            wrong_scope = reference_document()
            wrong_scope["scope"]["version"] = "1.46"
            reference.write_text(json.dumps(wrong_scope), encoding="utf-8")
            result = run_cli(snapshot, reference, sources, output)
            self.assertEqual(1, result.returncode)
            self.assertFalse(output.exists())

            unproven = reference_document(items=[entry("Later Sword", status="excluded-later-version")])
            reference.write_text(json.dumps(unproven), encoding="utf-8")
            result = run_cli(snapshot, reference, sources, output)
            self.assertEqual(1, result.returncode)
            self.assertFalse(output.exists())


def entry(name: str, *, aliases: list[str] | None = None, status: str = "confirmed-145",
          category: str = "Weapon", items: list[str] | None = None) -> dict:
    result = {"name": name, "aliases": aliases or [], "status": status, "sourceIds": ["src-1"], "notes": "evidence"}
    if items is not None:
        result["items"] = items
    elif category == "North":
        result["area"] = category
    else:
        result["category"] = category
    if status == "excluded-later-version":
        result["introducedVersion"] = "1.50"
    return result


def reference_document(*, items: list[dict] | None = None, monsters: list[dict] | None = None,
                       sets: list[dict] | None = None, sources: list[dict] | None = None) -> dict:
    return {
        "scope": {"game": "传奇3", "operator": "光通", "version": "1.45", "policy": "strict-evidence"},
        "sources": sources if sources is not None else [{
            "id": "src-1", "title": "Official source", "url": "https://example.invalid", "level": 1,
            "versions": ["1.45"], "categories": ["items", "monsters", "sets"], "locator": "p. 1", "notes": "evidence",
        }],
        "items": items or [], "monsters": monsters or [], "sets": sets or [],
    }


def snapshot_document(item_name: str = "Iron Sword") -> dict:
    return {
        "database": {"path": "Database/System.db", "sha256": "abc", "exportedAt": "2026-09-04T00:00:00Z"},
        "items": [{"index": 7, "name": item_name, "itemType": "Weapon", "requiredClass": "All", "requiredAmount": 1, "image": 2}],
        "monsters": [{"index": 8, "name": "Wolf", "level": 4, "ai": 3, "image": 4, "isBoss": False}],
        "sets": [{"index": 9, "name": "Starter Set", "groups": [{"name": "main", "requiredNumItems": 1, "items": ["Iron Sword"]}]}],
    }


def run_cli(snapshot: Path, reference: Path, sources: Path, output: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(COMPARE), "--snapshot", str(snapshot), "--reference", str(reference),
         "--sources", str(sources), "--output", str(output)],
        capture_output=True, text=True, check=False,
    )


if __name__ == "__main__":
    unittest.main()
