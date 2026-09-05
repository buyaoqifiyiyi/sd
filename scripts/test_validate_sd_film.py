#!/usr/bin/env python3
"""Regression tests for the r13 SD Film validator."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_sd_film.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)

class R13RegressionTests(unittest.TestCase):
    def test_active_skill_passes(self) -> None:
        self.assertEqual(validator.validate_skill(ROOT), [])

    def test_2_0_and_2_5_are_isolated(self) -> None:
        two = (ROOT / "adapters/seedance-2.0.md").read_text(encoding="utf-8-sig")
        twofive = (ROOT / "adapters/seedance-2.5.md").read_text(encoding="utf-8-sig")
        self.assertIn("max_seconds: 15", two)
        self.assertIn("max_seconds: 30", twofive)
        self.assertIn("23 秒 Natural Unit", twofive)

    def test_state_07_owns_clip_decision(self) -> None:
        selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/10_clip_production_workflow.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("先形成 Natural Unit，再输出", selection)
        self.assertIn("唯一决策 owner", workflow)

    def test_asset_image_route_defaults_to_builtin_and_isolates_midjourney(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        midjourney = (ROOT / "adapters/midjourney.md").read_text(encoding="utf-8-sig")
        video_selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        self.assertIn("未明确指定外部图像模型：`Built-in Image`", assets)
        self.assertIn("明确指定`Midjourney`：读取`adapters/midjourney.md`", assets)
        self.assertIn("只输出可直接粘贴的 Midjourney Prompt", midjourney)
        self.assertIn("不调用内置`image_gen`", midjourney)
        self.assertNotIn("Midjourney", video_selection)

    def test_every_asset_workflow_calls_the_single_image_route_owner(self) -> None:
        workflows = (
            "workflows/04_character_asset_workflow.md",
            "workflows/05_environment_asset_workflow.md",
            "workflows/06_prop_asset_workflow.md",
            "workflows/15_fx_asset_workflow.md",
        )
        for relative in workflows:
            self.assertIn("modules/assets.md`的Asset Image Route", (ROOT / relative).read_text(encoding="utf-8-sig"))

if __name__ == "__main__":
    unittest.main()
