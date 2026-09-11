#!/usr/bin/env python3
"""Regression tests for the r49 SD Film validator."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_sd_film.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)

PKG_SPEC = importlib.util.spec_from_file_location(
    "package_validator", ROOT / "scripts" / "validate_prompt_package.py"
)
package_validator = importlib.util.module_from_spec(PKG_SPEC)
assert PKG_SPEC and PKG_SPEC.loader
PKG_SPEC.loader.exec_module(package_validator)

class R34RegressionTests(unittest.TestCase):
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

    def test_director_mapping_reaches_fx_sequence_clip_and_prompt(self) -> None:
        director = (ROOT / "modules/director.md").read_text(encoding="utf-8-sig")
        fx = (ROOT / "workflows/15_fx_asset_workflow.md").read_text(encoding="utf-8-sig")
        sequence = (ROOT / "workflows/16_sequence_planning_workflow.md").read_text(encoding="utf-8-sig")
        clip = (ROOT / "workflows/10_clip_production_workflow.md").read_text(encoding="utf-8-sig")
        prompt = (ROOT / "workflows/11_video_generation_workflow.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("STATE-00 Project Director Baseline", director)
        self.assertIn("STATE-08 Director-to-Prompt Translation", director)
        self.assertIn("当前FX的视觉重点、遮挡/Reveal与后果呈现功能", fx)
        self.assertIn("已确认Scene Director Intent、Information Presentation与Rhythm Intent", sequence)
        self.assertIn("当前Natural Unit覆盖的Director Decision Notes与Clip-level投影", clip)
        self.assertIn("当前Clip的1—3个已确认导演优先级", prompt)
        self.assertIn("R23-K Cross-stage Director Consumption", scenarios)

    def test_multistage_clip_cannot_default_to_flat_following(self) -> None:
        router = (ROOT / "knowledge/camera_language/shot_language_router.md").read_text(encoding="utf-8-sig")
        plan = (ROOT / "templates/20_clip_plan.md").read_text(encoding="utf-8-sig")
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        review = (ROOT / "workflows/13_review_workflow.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Adjacent Observation Contrast And Deliberate Repetition", router)
        self.assertIn("阶段间观察层次", plan)
        self.assertIn("只保留同一摄影机逻辑", plan)
        self.assertIn("同一台摄影机自然跟随 / 保持前进方向 / 轻微推进", projection)
        self.assertIn("多阶段Clip的实际成片是否保留Clip Movement Plan中的观察层次", review)
        self.assertIn("R23-L Multi-stage Clip", scenarios)

    def test_visual_grammar_baseline_keeps_scene_delta_directable(self) -> None:
        director = (ROOT / "knowledge/director_decision_layer.md").read_text(encoding="utf-8-sig")
        visual = (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")
        scene = (ROOT / "workflows/08_scene_breakdown_workflow.md").read_text(encoding="utf-8-sig")
        review = (ROOT / "workflows/13_review_workflow.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Visual Grammar Baseline And Scene Delta", director)
        self.assertIn("色彩的导演功能是“权限”而非默认滤镜", director)
        self.assertIn("Visual Grammar Baseline", visual)
        self.assertIn("当前空间的戏剧功能", scene)
        self.assertIn("Baseline漂移返回STATE-04", review)
        self.assertIn("R23-M Visual Grammar", scenarios)

    def test_project_color_reference_is_conditional_and_non_asset(self) -> None:
        styles = (ROOT / "knowledge/visual_styles/index.md").read_text(encoding="utf-8-sig")
        visual = (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")
        asset_rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/12_seedance_25_video_prompt.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Project Color Reference Route", styles)
        self.assertIn("不会获得资产ID", styles)
        self.assertIn("Project Color Reference Route", visual)
        self.assertIn("Project Color Reference`；它是非资产项目视觉参考", asset_rules)
        self.assertIn("Project Color Reference（非资产）", projection)
        self.assertIn("唯一Primary Role只能是综合色相 / 明度 / 饱和度 / 强调色占比", template)
        self.assertIn("R23-N Project Color Reference", scenarios)
        self.assertIn("Project Color Reference`进入视觉开发", guide)

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

    def test_formal_fx_template_tracks_physical_drivers_variants_and_boundaries(self) -> None:
        template = (ROOT / "templates/13_fx_asset_prompt.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/15_fx_asset_workflow.md").read_text(encoding="utf-8-sig")
        for marker in (
            "## Reference Assets And Visual Variant Policy",
            "Primary Visual Reference:",
            "Allowed State Variants:",
            "Immutable Visual Anchors:",
            "Variant Transition Conditions:",
            "### Physical Drivers",
            "Wind / Gravity / Flow:",
            "Emitter / Fuel / Power Condition:",
            "Collision / Adhesion / Accumulation:",
            "## FX State Ledger",
            "Boundary (Shot / Clip / Frame):",
            "Affected Asset State:",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, template)
        self.assertIn("记录可见的物理驱动", workflow)
        self.assertIn("FX State Ledger在每个边界记录可继承状态", workflow)

    def test_builtin_image_requires_selection_and_actual_generation_capability(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        character = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("Direct Image Default", assets)
        self.assertIn("仅已选择Built-in Image且当前环境实际可用时", character)
        self.assertIn("不得因环境可生成而跳过图像模型选择或Prompt确认", rules)

    def test_project_models_are_selected_once_early_then_clip_capability_is_verified(self) -> None:
        setup = (ROOT / "workflows/01_project_setup_workflow.md").read_text(encoding="utf-8-sig")
        image_selection = (ROOT / "modules/image-model-selection.md").read_text(encoding="utf-8-sig")
        video_selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        state = (ROOT / "references/project_state_contract.md").read_text(encoding="utf-8-sig")
        self.assertIn("Project Model Selection Gate", setup)
        self.assertIn("Project Model Selection Proposal", image_selection)
        self.assertIn("STATE-06后读取Confirmed Detailed Shot Design", video_selection)
        self.assertIn("Project Image Model Default", state)
        self.assertIn("Project Video Model Preference", state)

    def test_required_sketch_is_bound_to_real_model_input_or_blocks_honestly(self) -> None:
        preflight = (ROOT / "knowledge/clip_preflight_check.md").read_text(encoding="utf-8-sig")
        two = (ROOT / "templates/10_video_prompt.md").read_text(encoding="utf-8-sig")
        twofive = (ROOT / "templates/12_seedance_25_video_prompt.md").read_text(encoding="utf-8-sig")
        h3 = (ROOT / "templates/13_minimax_h3_video_prompt.md").read_text(encoding="utf-8-sig")
        budget = (ROOT / "knowledge/reference_budget.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("Required Sketch Submission Binding", preflight)
        self.assertIn("实际提交图片输入", two)
        self.assertIn("真实`@图片N`", twofive)
        self.assertIn("仅能在All-Reference模式以真实`@图片N`提交", h3)
        self.assertIn("Submission Compatibility=`FAIL`", budget)
        self.assertIn("R34 Required Sketch Submission Binding Regression", scenarios)
        self.assertIn("Final=`NONE`不预留草图位", budget)
        self.assertIn("Signature不变时复用同一个已确认图", preflight)

    def test_every_asset_workflow_calls_the_single_image_route_owner(self) -> None:
        workflows = (
            "workflows/04_character_asset_workflow.md",
            "workflows/05_environment_asset_workflow.md",
            "workflows/06_prop_asset_workflow.md",
            "workflows/15_fx_asset_workflow.md",
        )
        for relative in workflows:
            self.assertIn("Asset Image Route", (ROOT / relative).read_text(encoding="utf-8-sig"))

    def test_asset_discovery_routes_only_important_props_before_state_03(self) -> None:
        discovery = (ROOT / "workflows/03_asset_discovery_workflow.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/03_asset_discovery_prompt.md").read_text(encoding="utf-8-sig")
        prop = (ROOT / "workflows/06_prop_asset_workflow.md").read_text(encoding="utf-8-sig")
        completion = (ROOT / "rules/completion_gate.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        for marker in ("Important Prop Completeness Pass", "Important Prop Candidate", "Prop Production Route", "No important PROP asset required"):
            with self.subTest(marker=marker):
                self.assertIn(marker, discovery)
        self.assertIn("普通环境陈设、背景装饰、无特写/无状态连续性的通用消耗品", discovery)
        self.assertIn("# Prop Completeness Ledger", template)
        self.assertIn("不要逐项收录所有可见物件", template)
        self.assertIn("Not A Formal PROP Asset", template)
        self.assertIn("Prop Completeness Ledger", prop)
        self.assertIn("Prop Completeness Ledger", completion)
        self.assertIn("R09-D Prop Discovery Completeness", scenarios)
        self.assertIn("两盏台灯与普通报纸", scenarios)
        self.assertIn("不进入台账、Registry或STATE-03待办", scenarios)

    def test_core_character_asset_is_one_combined_reference_sheet(self) -> None:
        workflow = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/04_character_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("Image Model Selection Gate", workflow)
        self.assertIn("Candidate Reference", workflow)
        self.assertIn("#### Combined Character Asset Sheet Prompt", template)
        self.assertIn("Three-View Prompt", template)

    def test_core_prop_main_reference_is_a_single_horizontal_four_panel_sheet(self) -> None:
        workflow = (ROOT / "workflows/06_prop_asset_workflow.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/06_prop_asset_prompt.md").read_text(encoding="utf-8-sig")
        builtin = (ROOT / "templates/24_builtin_image_asset_prompt.md").read_text(encoding="utf-8-sig")
        midjourney = (ROOT / "templates/14_midjourney_asset_prompt.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("Main 1", workflow)
        self.assertIn("covered by Main 1", template)
        self.assertIn("four-panel prop sheet", builtin)
        self.assertIn("four-panel prop sheet", midjourney)
        self.assertIn("prop-001-main-sheet-c01.png", scenarios)

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
        for alias in ("调用sd", "调用SD", "用SD Film", "重新调用sd", "恢复旧项目", "继续之前的项目"):
            with self.subTest(alias=alias):
                self.assertIn(alias, skill)
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

    def test_fast_mode_runs_a_continuous_reversible_chain_but_keeps_hard_stops(self) -> None:
        automation = (ROOT / "rules/automation_mode.md").read_text(encoding="utf-8-sig")
        progression = (ROOT / "rules/progression_rules.md").read_text(encoding="utf-8-sig")
        activation = (ROOT / "rules/activation_rules.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        for text in (automation, activation, guide):
            with self.subTest(text=text[:32]):
                self.assertIn("尽量少确认", text)
        self.assertIn("## FAST Continuous Chain", automation)
        self.assertIn("STATE-04 → STATE-05 → STATE-06 → STATE-07 → STATE-08", automation)
        self.assertIn("完整视频Prompt", automation)
        self.assertIn("外部生成包", automation)
        self.assertIn("FAST Continuous Chain", progression)
        self.assertIn("`STANDARD`本轮停在草图", progression)
        self.assertIn("`FAST`在草图验证、注册和用途说明后同轮编译", progression)
        self.assertIn("R30-B FAST Carries Verified Internal Work Through Prompt Delivery", scenarios)
        self.assertIn("R30-C FAST Stops At Non-Reversible Boundaries", scenarios)

    def test_candidate_triage_keeps_one_valid_output_and_only_deletes_safe_temporary_files(self) -> None:
        asset_rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        sketch = (ROOT / "knowledge/clip_preflight_check.md").read_text(encoding="utf-8-sig")
        automation = (ROOT / "rules/automation_mode.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        for text in (asset_rules, sketch):
            with self.subTest(text=text[:32]):
                self.assertIn("NEEDS_USER_SELECTION", text)
                self.assertIn("已核验精确路径", text)
                self.assertIn("不得自动删除", text)
        self.assertIn("Candidate Output Triage / Cleanup", automation)
        self.assertIn("保留的Candidate ID", guide)
        self.assertIn("R31-A Asset Run Keeps One Valid Candidate And Removes Extras", scenarios)
        self.assertIn("R31-C Sketch Failure Is Removed Before Registration", scenarios)

    def test_unified_delivery_packages_preserve_stages_templates_and_hard_stops(self) -> None:
        automation = (ROOT / "rules/automation_mode.md").read_text(encoding="utf-8-sig")
        progression = (ROOT / "rules/progression_rules.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        for text in (automation, guide):
            with self.subTest(text=text[:32]):
                self.assertIn("Preproduction Package", text)
                self.assertIn("Execution Package", text)
                self.assertIn("Asset Candidate Package", text)
        self.assertIn("不替代任何未展示Artifact的确认", automation)
        self.assertIn("原有完整Template", automation)
        self.assertIn("立即截断包", automation)
        self.assertIn("Unified Delivery Packages", progression)
        self.assertIn("R32-A FAST Aggregates Preproduction And Execution", scenarios)
        self.assertIn("R32-B Hard Stop Truncates The Package", scenarios)
        self.assertIn("R32-C Standard Mode Aggregates Only Already-Legal Results", scenarios)

    def test_seedance_25_and_h3_surface_main_style_without_breaking_their_templates(self) -> None:
        twofive = (ROOT / "templates/12_seedance_25_video_prompt.md").read_text(encoding="utf-8-sig")
        h3 = (ROOT / "templates/13_minimax_h3_video_prompt.md").read_text(encoding="utf-8-sig")
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        h3_compiler = (ROOT / "knowledge/prompt_compilation/minimax_h3_compilation.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("尾帧限制：\n\n主风格：\n", twofive)
        self.assertIn("### 主风格：", twofive)
        self.assertIn("独立、无条件的项目视觉入口", twofive)
        self.assertIn("核心创意：\n主风格：", h3)
        self.assertIn("不新增顶级`主风格：`段落", h3)
        self.assertIn("独立`主风格：`", projection)
        self.assertIn("第一行固定为`主风格：`", h3_compiler)
        self.assertIn("R33-A Seedance 2.5 Has A Dedicated Main Style Field", scenarios)
        self.assertIn("R33-B H3 Keeps Three-Part Structure", scenarios)

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

    def test_declared_existing_assets_are_listed_not_solicited(self) -> None:
        asset_rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        discovery = (ROOT / "workflows/03_asset_discovery_workflow.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/03_asset_discovery_prompt.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("### User-Declared Existing Assets", asset_rules)
        self.assertIn("资产可用性声明", asset_rules)
        self.assertIn("声明不等于登记", asset_rules)
        self.assertIn("已有（用户声明）", asset_rules)
        self.assertIn("## Declared-Existing Asset Handling｜Internal", discovery)
        self.assertIn("禁止向用户索取、催交或要求补齐资产文件", discovery)
        self.assertIn("已有（用户声明）", template)
        self.assertIn("R35 Declared-Existing Asset Handling Regression", scenarios)
        self.assertIn("不索取、不催交、不逐项盘问", scenarios)

    def test_aesthetic_decision_lock_requires_exclusive_choices(self) -> None:
        director = (ROOT / "knowledge/director_decision_layer.md").read_text(encoding="utf-8-sig")
        visual = (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")
        bible = (ROOT / "templates/01_project_bible_template.md").read_text(encoding="utf-8-sig")
        scorecard = (ROOT / "knowledge/quality/prompt_scorecard.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("# Aesthetic Decision Lock Gate", visual)
        self.assertIn("被放弃的选项", visual)
        self.assertIn("Aesthetic Decision Lock", director)
        self.assertIn("视觉母题与变化轨迹（", bible)
        self.assertIn("Aesthetic Decision Lock", scorecard)
        self.assertIn("R49 Aesthetic Decision Lock Regression", scenarios)
        self.assertIn("不新增竞争区域或平行Schema", visual)
        self.assertIn("缺少被放弃的选项视为尚未做出决定", bible)
        self.assertIn("不能替代人工审美判断", scorecard)

    def test_aesthetic_decision_lock_reaches_state08_projection(self) -> None:
        projection = (ROOT / "knowledge/prompt_compilation/state08_projection.md").read_text(encoding="utf-8-sig")
        prompt = (ROOT / "workflows/11_video_generation_workflow.md").read_text(encoding="utf-8-sig")
        scenarios = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("| Aesthetic Decision Lock（STATE-04） | 主风格；画面描述；环境一致性 |", projection)
        self.assertIn("反差与光比结构的程度及其变化节点", projection)
        self.assertIn("Aesthetic Decision Lock的四项决定同样必须落成固定字段中的可见语义", projection)
        self.assertIn("不因`Source Carries State`而默认省略", projection)
        self.assertIn(
            "Aesthetic Decision Lock（反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹）",
            prompt,
        )
        self.assertIn("R50 Aesthetic Decision Lock Projection Regression", scenarios)

class R47PromptPackageValidatorTests(unittest.TestCase):
    """The delivered STATE-08 Prompt Package validator must accept conformant
    packages and reject structurally broken ones."""

    def build_20(self, *, shot_two: bool = False, voice: bool = False, ref_tail: str = "") -> str:
        shots = [1] if not shot_two else [1, 2]
        body = []
        for number in shots:
            body.append(
                f"分镜{number}\n"
                "景别：中景\n"
                "镜头/机位：50mm倾向，眼平高度，固定机位\n"
                "起始状态：人物坐于堂屋左侧\n"
                "画面描述：先抬眼，再抬耳勺；后景有人在柜台后擦杯\n"
                "人物动作与情绪：目光落在耳勺上，呼吸放浅\n"
                "空间关系：人物位于画面左侧三分之一\n"
                "道具状态：PROP-001，右手持有\n"
                "台词：无\n"
                "音效：市集底声与耳勺轻碰声\n"
                "镜头结尾状态：Continuous Handoff，保持坐姿\n"
            )
        voice_line = "音色特征：低沉男声\n" if voice else ""
        return (
            "# CLIP-001｜掏耳 Seedance 2.0视频提示词\n"
            "时长：8秒\n"
            "画幅：16:9横屏\n\n"
            "参考资产：\n"
            f"CHAR-001｜吴御史｜实际提交图片输入\n{ref_tail}"
            "首帧参考：C【新镜头且无需尾帧】另起新镜头\n"
            "尾帧限制：人物停在中景右侧\n\n"
            "主风格：低饱和胶片质感\n"
            "人物一致性：CHAR-001@v003\n"
            "环境一致性：ENV-002@v001\n"
            f"{voice_line}\n"
            + "\n".join(body) +
            "\n反向提示词：\n"
            "禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。\n"
        )

    def check(self, text: str, model: str = "seedance-2.0", allow_voice: bool = False) -> list[str]:
        errors, _ = package_validator.validate(text, model, allow_voice)
        return errors

    def test_conformant_package_passes(self) -> None:
        self.assertEqual(self.check(self.build_20()), [])
        self.assertEqual(self.check(self.build_20(shot_two=True)), [])

    def test_unauthorized_voice_field_is_rejected(self) -> None:
        findings = self.check(self.build_20(voice=True))
        self.assertTrue(any("音色特征" in item for item in findings))

    def test_voice_field_is_allowed_only_with_explicit_authorization(self) -> None:
        findings = self.check(self.build_20(voice=True), allow_voice=True)
        self.assertFalse(any("音色特征" in item for item in findings))

    def test_non_contiguous_shot_numbering_is_rejected(self) -> None:
        text = self.build_20(shot_two=True).replace("分镜2", "分镜3")
        findings = self.check(text)
        self.assertTrue(any("分镜编号" in item for item in findings))

    def test_empty_shot_field_is_rejected(self) -> None:
        text = self.build_20().replace("起始状态：人物坐于堂屋左侧", "起始状态：")
        findings = self.check(text)
        self.assertTrue(any("空值字段" in item for item in findings))

    def test_ref_tail_requires_declared_usage(self) -> None:
        without_usage = self.build_20(ref_tail="REF-TAIL-01｜CLIP-000尾帧参考\n")
        self.assertTrue(any("REF-TAIL" in item for item in self.check(without_usage)))
        with_usage = self.build_20(
            ref_tail="REF-TAIL-01｜CLIP-000尾帧参考（同镜头连续承接用途）\n"
        )
        self.assertFalse(any("REF-TAIL" in item for item in self.check(with_usage)))

    def test_missing_no_bgm_sentence_is_rejected(self) -> None:
        text = self.build_20().replace("禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，"
                                       "只保留台词、环境声、动作音效和必要的自然声音。", "注意保持一致性。")
        findings = self.check(text)
        self.assertTrue(any("无BGM" in item for item in findings))

    def test_json_package_is_rejected(self) -> None:
        findings = self.check("{\"clip\": \"CLIP-001\"}")
        self.assertTrue(any("JSON" in item for item in findings))

    def test_seedance_25_stages_must_be_contiguous(self) -> None:
        text = (
            "# CLIP-001｜掏耳 Seedance 2.5视频提示词\n"
            "时长：10秒\n画幅：16:9横屏\n\n"
            "多模态参考资产：\n- @图片1：CHAR-001\n"
            "参考素材职责与优先级：\n- 身份由 CHAR-001 承担\n"
            "首帧参考：C\n尾帧限制：稳定\n\n"
            "主风格：低饱和胶片\n"
            "全局叙事与画面设定：一句话\n"
            "全局一致性与执行约束：轴线保持\n\n"
            "时间线：\n"
            "[0—4秒]\n画面与镜头：a\n人物动作与情绪：b\n空间与道具：c\n台词：无\n音效：d\n阶段结尾状态：e\n"
            "[6—10秒]\n画面与镜头：a\n人物动作与情绪：b\n空间与道具：c\n台词：无\n音效：d\n阶段结尾状态：e\n\n"
            "全局限制与反向提示词：\n"
            + package_validator.NO_BGM_SENTENCE + "\n"
        )
        errors, _ = package_validator.validate(text, "seedance-2.5", False)
        self.assertTrue(any("阶段" in item for item in errors))

    def test_minimax_h3_requires_fixed_last_line(self) -> None:
        text = (
            "# CLIP-001｜掏耳 MiniMax H3视频提示词\n"
            "时长：8秒\n画幅：16:9横屏\n\n"
            "参考素材说明：\n- @图片1：CHAR-001\n"
            "核心创意：\n主风格：低饱和胶片\n一句话\n"
            "画面过程说明：开始、过程、结束\n\n"
            "反向提示词：\n" + package_validator.NO_BGM_SENTENCE + "\n\n"
            "非叙事性音乐：N/A\n"
        )
        self.assertEqual(package_validator.validate(text, "minimax-h3", False)[0], [])
        broken = text.replace("非叙事性音乐：N/A\n", "")
        errors, _ = package_validator.validate(broken, "minimax-h3", False)
        self.assertTrue(any("最后一行" in item for item in errors))

    def test_package_validator_is_registered_and_documented(self) -> None:
        required = ROOT / "scripts" / "validate_prompt_package.py"
        self.assertTrue(required.is_file())
        source = (ROOT / "scripts" / "validate_sd_film.py").read_text(encoding="utf-8")
        self.assertIn("scripts/validate_prompt_package.py", source)
        for relative in (
            "templates/10_video_prompt.md",
            "templates/12_seedance_25_video_prompt.md",
            "templates/13_minimax_h3_video_prompt.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("validate_prompt_package.py", text, relative)
        contracts = (ROOT / "references" / "module_contracts.md").read_text(encoding="utf-8")
        self.assertIn("validate_prompt_package.py", contracts)


if __name__ == "__main__":
    unittest.main()
