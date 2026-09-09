#!/usr/bin/env python3
"""Regression tests for the r30 SD Film validator."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_sd_film.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)

class R30RegressionTests(unittest.TestCase):
    def test_active_skill_passes(self) -> None:
        self.assertEqual(validator.validate_skill(ROOT), [])

    def test_2_0_and_2_5_are_isolated(self) -> None:
        two = (ROOT / "adapters/seedance-2.0.md").read_text(encoding="utf-8-sig")
        twofive = (ROOT / "adapters/seedance-2.5.md").read_text(encoding="utf-8-sig")
        self.assertIn("max_seconds: 15", two)
        self.assertIn("max_seconds: 30", twofive)
        self.assertIn("23 秒 Natural Unit", twofive)

    def test_seedance_25_exposes_timestamp_and_multimodal_audits_without_claiming_web_features_for_api(self) -> None:
        adapter = (ROOT / "adapters/seedance-2.5.md").read_text(encoding="utf-8-sig")
        compiler = (ROOT / "knowledge/prompt_compilation/seedance_25_compilation.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/12_seedance_25_video_prompt.md").read_text(encoding="utf-8-sig")
        state = (ROOT / "references/project_state_contract.md").read_text(encoding="utf-8-sig")
        self.assertIn("timestamp_text_control", adapter)
        self.assertIn("combined: 50", adapter)
        self.assertIn("pure_audio_driver: supported", adapter)
        self.assertIn("Dreamina Web专有", adapter)
        self.assertIn("唯一Primary Role", compiler)
        self.assertIn("参考素材职责与优先级", template)
        self.assertIn("时间线：", template)
        self.assertIn("Delivery Surface: STANDARD / DREAMINA_WEB", state)
        self.assertIn("Reference Capacity Audit: SEEDANCE_25_CAPABILITY", state)

    def test_minimax_h3_is_explicit_and_does_not_inherit_seedance_features(self) -> None:
        h3 = (ROOT / "adapters/minimax-h3.md").read_text(encoding="utf-8-sig")
        compiler = (ROOT / "knowledge/prompt_compilation/minimax_h3_compilation.md").read_text(encoding="utf-8-sig")
        self.assertIn("min_seconds: 4", h3)
        self.assertIn("max_seconds: 15", h3)
        self.assertIn("images_max: 9", h3)
        self.assertIn("videos_max: 3", h3)
        self.assertIn("audio_max: 3", h3)
        self.assertIn("mixed_files_max: 12", h3)
        self.assertIn("two_images: no_automatic_cut", h3)
        self.assertIn("unsupported_without_official_verification", h3)
        self.assertIn("Seedance_Video_Extension", h3)
        self.assertIn("4—15 秒", compiler)
        self.assertIn("官方三段式", compiler)
        self.assertIn("非叙事性音乐：N/A", compiler)

    def test_every_supported_model_has_an_isolated_final_prompt_template(self) -> None:
        adapter20 = (ROOT / "adapters/seedance-2.0.md").read_text(encoding="utf-8-sig")
        adapter25 = (ROOT / "adapters/seedance-2.5.md").read_text(encoding="utf-8-sig")
        adapter_h3 = (ROOT / "adapters/minimax-h3.md").read_text(encoding="utf-8-sig")
        h3_template = (ROOT / "templates/13_minimax_h3_video_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("templates/10_video_prompt.md", adapter20)
        self.assertIn("prompt_output_template: templates/12_seedance_25_video_prompt.md", adapter25)
        self.assertIn("prompt_output_template: templates/13_minimax_h3_video_prompt.md", adapter_h3)
        self.assertIn("参考素材说明：", h3_template)
        self.assertIn("核心创意：", h3_template)
        self.assertIn("非叙事性音乐：N/A", h3_template)

    def test_state_07_owns_clip_decision(self) -> None:
        selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/10_clip_production_workflow.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("先形成 Natural Unit，再输出", selection)
        self.assertIn("唯一决策 owner", workflow)

    def test_asset_image_model_selection_has_no_default_and_isolates_templates(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        selection = (ROOT / "modules/image-model-selection.md").read_text(encoding="utf-8-sig")
        builtin_adapter = (ROOT / "adapters/built-in-image.md").read_text(encoding="utf-8-sig")
        builtin_template = (ROOT / "templates/24_builtin_image_asset_prompt.md").read_text(encoding="utf-8-sig")
        midjourney = (ROOT / "adapters/midjourney.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/14_midjourney_asset_prompt.md").read_text(encoding="utf-8-sig")
        video_selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        self.assertIn("不得默认选择Built-in Image、Midjourney或任何第三方服务", assets)
        self.assertIn("## Available Choices", selection)
        self.assertIn("不得默认选择Built-in Image、Midjourney或其他模型", selection)
        self.assertIn("prompt_output_template: templates/24_builtin_image_asset_prompt.md", builtin_adapter)
        self.assertIn("## Built-in Image Prompt Package", builtin_template)
        self.assertIn("只输出可直接粘贴的 Midjourney Prompt", midjourney)
        self.assertIn("不调用内置`image_gen`", midjourney)
        self.assertIn("prompt_output_template: templates/14_midjourney_asset_prompt.md", midjourney)
        self.assertIn("## Midjourney Prompt Package", template)
        self.assertIn("## Asset-Specific Compilation", template)
        self.assertIn("--v`、`--q`、`--s`、`--seed`", template)
        self.assertNotIn("Midjourney", video_selection)

    def test_external_image_models_require_isolated_templates_before_adapter_routing(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        contracts = (ROOT / "references/module_contracts.md").read_text(encoding="utf-8-sig")
        workflow_map = (ROOT / "workflows/workflow_map.md").read_text(encoding="utf-8-sig")
        category_templates = (
            "templates/04_character_asset_prompt.md",
            "templates/05_environment_asset_prompt.md",
            "templates/06_prop_asset_prompt.md",
            "templates/13_fx_asset_prompt.md",
        )
        self.assertIn("独立`prompt_output_template`", assets)
        self.assertIn("## Image Model Prompt Template Isolation", contracts)
        self.assertIn("templates/14_midjourney_asset_prompt.md", workflow_map)
        for relative in category_templates:
            with self.subTest(template=relative):
                self.assertIn("Image Prompt Output Template", (ROOT / relative).read_text(encoding="utf-8-sig"))

    def test_builtin_image_requires_selection_and_actual_generation_capability(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        character = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("Direct Image Default", assets)
        self.assertIn("仅已选择Built-in Image且当前环境实际可用时", character)
        self.assertIn("不得因环境可生成而跳过图像模型选择或Prompt确认", rules)

    def test_every_asset_workflow_calls_the_single_image_route_owner(self) -> None:
        workflows = (
            "workflows/04_character_asset_workflow.md",
            "workflows/05_environment_asset_workflow.md",
            "workflows/06_prop_asset_workflow.md",
            "workflows/15_fx_asset_workflow.md",
        )
        for relative in workflows:
            self.assertIn("Asset Image Route", (ROOT / relative).read_text(encoding="utf-8-sig"))

    def test_core_character_asset_is_one_combined_reference_sheet(self) -> None:
        workflow = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/04_character_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("Image Model Selection Gate", workflow)
        self.assertIn("Candidate Reference", workflow)
        self.assertIn("#### Combined Character Asset Sheet Prompt", template)
        self.assertIn("Three-View Prompt", template)

    def test_acting_strategy_is_additive_and_respects_blocking_owner(self) -> None:
        performance = (ROOT / "knowledge/performance/micro_expression.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Behavior Under Pressure", performance)
        self.assertIn("不得补写未成立的目标、冲突、台词或剧情转折", performance)
        self.assertIn("Spatial Blocking仍是位置、朝向、距离和接触的唯一owner", performance)

    def test_risk_locks_are_conditional_and_do_not_create_prompt_schema(self) -> None:
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        shot_qa = (ROOT / "knowledge/quality/shot_qa.md").read_text(encoding="utf-8-sig")
        self.assertIn("**Risk-driven Execution Locks**", projection)
        self.assertIn("风险不存在时不添加通用锁", projection)
        self.assertIn("### Risk-driven Prompt Evidence", shot_qa)
        self.assertIn("templates/10_video_prompt.md", projection)

    def test_external_image_route_remains_explicit_and_capability_neutral(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("明确指定其他图像模型", assets)
        self.assertIn("不得默认选择Built-in Image、Midjourney或任何第三方服务", assets)
        self.assertIn("不假设平台能力", guide)

    def test_legacy_recovery_matrix_static_contract(self) -> None:
        runtime = (ROOT / "rules/runtime_reload.md").read_text(encoding="utf-8-sig")
        state_source = (ROOT / "rules/state_source.md").read_text(encoding="utf-8-sig")
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        expectations = {
            "LR-R1": (runtime, "Work escalation"),
            "LR-R2": (state_source, "Skill Source与State Source不得混淆"),
            "LR-R3": (runtime, "旧对话Skill摘要不得标成Current Skill"),
            "LR-R4": (runtime, "Compatibility Mapping"),
            "LR-R5": (runtime, "Backfill missing intent, do not remake confirmed production."),
            "LR-R6": (projection, "Blocking Signature"),
            "LR-R7": (runtime, "STATE-08"),
            "LR-R8": (runtime, "Reload Status"),
            "LR-R9": (runtime, "Work escalation"),
            "LR-R10": (runtime, "普通`下一步 / 继续`"),
        }
        for case, (text, marker) in expectations.items():
            with self.subTest(case=case):
                self.assertIn(marker, text)

    def test_standalone_discovery_matrix_static_contract(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8-sig")
        self.assertIn("name: sd-film", skill)
        self.assertIn("$sd-film", guide)
        self.assertIn("@`选择器只显示Plugin", guide)
        self.assertIn("allow_implicit_invocation: true", metadata)

    def test_fast_mode_is_explicit_and_preserves_hard_stops(self) -> None:
        automation = (ROOT / "rules/automation_mode.md").read_text(encoding="utf-8-sig")
        completion = (ROOT / "rules/completion_gate.md").read_text(encoding="utf-8-sig")
        asset_lock = (ROOT / "references/asset_lock_contract.md").read_text(encoding="utf-8-sig")
        self.assertIn("只有用户当前明确说", automation)
        self.assertIn("## Hard Stops", automation)
        self.assertIn("Production Script Proposal", automation)
        self.assertIn("Candidate Image", automation)
        self.assertIn("图片与Production Script Proposal不在替代范围内", completion)
        self.assertIn("FAST不得替代该图片确认", asset_lock)

    def test_advance_synonyms_confirm_the_current_explicit_checkpoint(self) -> None:
        progression = (ROOT / "rules/progression_rules.md").read_text(encoding="utf-8-sig")
        script = (ROOT / "workflows/02_script_analysis_workflow.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        for command in ("下一步", "下一个", "继续", "往后做", "接着做", "next", "proceed", "好的"):
            with self.subTest(command=command):
                self.assertIn(command, progression)
        self.assertIn("即为确认当前检查点", progression)
        self.assertIn("不提交外部服务", progression)
        self.assertIn("推进表达按`rules/progression_rules.md`确认该Proposal", script)
        self.assertIn("其他同义推进表达也直接视为确认", guide)

    def test_environment_multi_view_reconstruction_is_state03_additive(self) -> None:
        reconstruction = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/05_environment_asset_workflow.md").read_text(encoding="utf-8-sig")
        lock = (ROOT / "references/asset_lock_contract.md").read_text(encoding="utf-8-sig")
        blocking = (ROOT / "knowledge/spatial_blocking_layer.md").read_text(encoding="utf-8-sig")
        self.assertIn("不是新模块、STATE、Registry 或最终 Prompt Schema", reconstruction)
        self.assertIn("ENV-01 + ENV-02 → ENV-03", reconstruction)
        self.assertIn("ENV-01 + ENV-02 + ENV-03 → ENV-04", reconstruction)
        self.assertIn("Spatial Reconstruction: Full / Partial / Not Required", workflow)
        self.assertIn("### Environment Spatial Lock", lock)
        self.assertIn("ENV-04是STATE-03已确认的Environment Canonical布局视角", blocking)

    def test_prompt_quality_rules_strengthen_existing_owners_without_new_style_system(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        performance = (ROOT / "knowledge/performance/micro_expression.md").read_text(encoding="utf-8-sig")
        camera = (ROOT / "knowledge/camera_language/shot_language_router.md").read_text(encoding="utf-8-sig")
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Prompt Evidence Ordering", assets)
        self.assertIn("### Micro-action Timing And Hierarchy", performance)
        self.assertIn("### Layered Depth And Readability", camera)
        self.assertIn("### Prompt Evidence Specificity", projection)
        self.assertIn("不新增Prompt字段", assets)
        self.assertIn("不构成自动编舞、同步口型或新增剧情动作", performance)
        self.assertIn("不得写成无空间依据的数字缩放或漂浮运镜", camera)
        self.assertIn("不能替代主体、空间、动作、时间顺序或光源依据", projection)

    def test_reference_research_distinguishes_observation_from_project_proposal(self) -> None:
        styles = (ROOT / "knowledge/visual_styles/index.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Reference-To-System Evidence Gate", styles)
        self.assertIn("Observable Reference Evidence", styles)
        self.assertIn("Project Proposal", styles)
        self.assertIn("Unknown / Not Transferable", styles)
        self.assertIn("不新建最终Prompt字段或独立Style Bible Schema", styles)
        self.assertIn("Reference-To-System Evidence Gate", workflow)

if __name__ == "__main__":
    unittest.main()
