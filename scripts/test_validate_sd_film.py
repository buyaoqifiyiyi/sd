#!/usr/bin/env python3
"""Regression tests for the r12 SD Film validator."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_sd_film.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)

class R12RegressionTests(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
