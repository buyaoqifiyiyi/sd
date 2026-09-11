#!/usr/bin/env python3
"""Regression tests for the r60 SD Film validator."""
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

MODULE_CONTRACT_FILES = (
    "references/module_contracts.md",
    "references/module_contracts_production.md",
    "references/module_contracts_auxiliary.md",
    "references/module_contracts_knowledge.md",
)

REGRESSION_FILES = (
    "references/regression_scenarios.md",
    "references/regression_scenarios_craft.md",
    "references/regression_scenarios_system.md",
    "references/recovery_guards.md",
)

def regression_corpus() -> str:
    """The regression set is split across four files; assertions target the set."""
    return "\n".join(
        (ROOT / relative).read_text(encoding="utf-8-sig") for relative in REGRESSION_FILES
    )

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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        scenarios = regression_corpus()
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
        criteria = (ROOT / "references" / "maintenance_self_check_protocol.md").read_text(encoding="utf-8")
        self.assertIn("validate_prompt_package.py", criteria)


class R50ContextBudgetTests(unittest.TestCase):
    """Length is a signal, not a quota: the review line tells you to check how a
    file is read, the ceiling blocks a commit, and an index entry nobody can
    follow is worth less than none. Only the last two are failures."""

    def test_active_skill_stays_within_budget(self) -> None:
        findings = validator.check_context_budget(
            validator.scan_markdown(ROOT), validator.read_size_ledger(ROOT)
        )
        self.assertEqual(findings, [])

    def test_index_covers_the_runtime_files_past_the_review_line(self) -> None:
        ledger = validator.read_size_ledger(ROOT)
        for relative, size in validator.scan_markdown(ROOT):
            if size <= validator.BUDGET_TARGET_BYTES or relative in ledger:
                continue
            with self.subTest(relative=relative):
                self.assertTrue(
                    validator.declares_non_runtime(ROOT / relative),
                    f"{relative} is past the review line and is not indexed",
                )

    def test_skill_entry_stays_compact(self) -> None:
        raw = (ROOT / "SKILL.md").read_bytes().decode("utf-8-sig").encode("utf-8")
        self.assertLessEqual(len(raw), validator.SKILL_ENTRY_MAX_BYTES)
        self.assertLessEqual(raw.count(b"\n"), validator.SKILL_ENTRY_MAX_LINES)

    def test_unregistered_oversized_file_is_not_a_failure(self) -> None:
        findings = validator.check_context_budget([("huge/thing.md", 60 * 1024)], {})
        self.assertEqual(findings, [])

    def test_review_line_crossing_is_advisory(self) -> None:
        self.assertEqual(validator.unindexed_over_review_line(ROOT), [])

    def test_index_entry_must_state_its_read_entry(self) -> None:
        findings = validator.check_read_entries(
            [{"File": "big/thing.md", "Class": "INTEGRAL", "Read Entry": ""}]
        )
        self.assertTrue(any("read entry" in item for item in findings))

    def test_non_runtime_entry_needs_no_read_entry(self) -> None:
        findings = validator.check_read_entries(
            [{"File": "guide.md", "Class": "NON_RUNTIME", "Read Entry": ""}]
        )
        self.assertEqual(findings, [])

    def test_non_runtime_file_sits_outside_the_review_line(self) -> None:
        self.assertTrue(validator.declares_non_runtime(ROOT / "USER_GUIDE.md"))
        self.assertNotIn("USER_GUIDE.md", validator.read_size_ledger(ROOT))

    def test_registered_oversized_file_is_accepted(self) -> None:
        self.assertEqual(
            validator.check_context_budget(
                [("huge/thing.md", 60 * 1024)], {"huge/thing.md": "INTEGRAL"}
            ),
            [],
        )

    def test_ceiling_violation_is_rejected_even_when_registered(self) -> None:
        findings = validator.check_context_budget(
            [("huge/thing.md", 110 * 1024)], {"huge/thing.md": "COMPOSITE"}
        )
        self.assertTrue(any("ceiling" in item for item in findings))

    def test_stale_ledger_entry_is_rejected(self) -> None:
        findings = validator.check_context_budget(
            [("small/thing.md", 10 * 1024)], {"small/thing.md": "INTEGRAL"}
        )
        self.assertTrue(any("stale" in item for item in findings))

    def test_ledger_entry_pointing_at_a_missing_file_is_rejected(self) -> None:
        findings = validator.check_context_budget([], {"gone/thing.md": "INTEGRAL"})
        self.assertTrue(any("missing" in item for item in findings))

    def test_unknown_ledger_class_is_rejected(self) -> None:
        findings = validator.check_context_budget(
            [("big/thing.md", 60 * 1024)], {"big/thing.md": "MAYBE_LATER"}
        )
        self.assertTrue(any("unknown class" in item for item in findings))

    def test_self_check_dimension_and_its_single_owner_are_wired(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(encoding="utf-8-sig")
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        for text in (card, criteria):
            with self.subTest(text=text[:40]):
                self.assertIn("Context Budget Check", text)
                self.assertIn("references/context_budget.md", text)
        self.assertIn("Context Budget: PASS / FIXED / WARN", card)
        self.assertIn("## Size Index", budget)
        self.assertIn("Ceiling", budget)

    def test_size_never_justifies_parallel_rule_files(self) -> None:
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        self.assertIn("本纪律不构成新增文件的理由", budget)
        self.assertIn("rules/resource_loading.md", budget)


class R51MaintenanceSelfCheckExtractionTests(unittest.TestCase):
    """The maintenance QA protocol was extracted out of the module contract so the
    path that must be read on every single change is short. module_contracts owns
    module interfaces only and must not silently re-grow its own copy."""

    def test_run_card_and_criteria_are_separate_and_complete(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(encoding="utf-8-sig")
        for dimension in validator.SELF_CHECK_DIMENSIONS:
            with self.subTest(dimension=dimension):
                self.assertIn(dimension, card)
                self.assertIn(dimension, criteria)

    def test_module_contracts_stops_owning_the_self_check(self) -> None:
        contracts = (ROOT / "references/module_contracts.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("\n## Skill Update Self-Check", contracts)
        self.assertNotIn("### Check Dimensions", contracts)
        self.assertNotIn("### Required Self-Check Summary", contracts)
        self.assertIn("references/maintenance_self_check.md", contracts)
        self.assertIn("references/maintenance_self_check_protocol.md", contracts)

    def test_split_module_contracts_left_the_ledger_clean(self) -> None:
        ledger = validator.read_size_ledger(ROOT)
        for relative in MODULE_CONTRACT_FILES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)
                self.assertNotIn(relative, ledger)

    def test_skill_entry_routes_to_the_run_card(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        self.assertIn("references/maintenance_self_check.md", skill)
        self.assertIn("references/maintenance_self_check_protocol.md", skill)

    def test_user_guide_declares_itself_non_runtime(self) -> None:
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("非运行时文件", guide)

    def test_resource_loading_owns_a_read_budget(self) -> None:
        loading = (ROOT / "rules/resource_loading.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Read Budget", loading)
        self.assertIn("references/maintenance_self_check.md", loading)
        self.assertIn("references/context_budget.md", loading)

    def test_seedance_duration_window_stops_being_restated_in_the_knowledge_layer(self) -> None:
        knowledge = (ROOT / "knowledge/11_seedance_adapter.md").read_text(encoding="utf-8-sig")
        adapter20 = (ROOT / "adapters/seedance-2.0.md").read_text(encoding="utf-8-sig")
        adapter25 = (ROOT / "adapters/seedance-2.5.md").read_text(encoding="utf-8-sig")
        self.assertIn("max_seconds: 15", adapter20)
        self.assertIn("max_seconds: 30", adapter25)
        for stale in ("Seedance 2.0为4—15秒", "2.0为4—15秒", "2.5为4—30秒", "允许用户选择4—30秒Clip"):
            with self.subTest(stale=stale):
                self.assertNotIn(stale, knowledge)
        self.assertIn("Adapter的`duration`", knowledge)


class R52SizeMetricAndRegressionSplitTests(unittest.TestCase):
    """Size is measured in bytes, not lines: this corpus is 31%-57% blank lines,
    so a line count overstates size and misjudges paragraph-dense files. And the
    composite regression set was split so reading one scenario no longer costs
    the whole 130 KB corpus."""

    def test_size_is_measured_in_bytes_not_lines(self) -> None:
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Metric", budget)
        self.assertIn("主度量是 UTF-8 字节数，不是行数", budget)
        self.assertIn("## File Classes", budget)
        for file_class in validator.LEDGER_CLASSES:
            with self.subTest(file_class=file_class):
                self.assertIn(file_class, budget)

    def test_regression_set_is_split_with_a_single_index(self) -> None:
        index = (ROOT / "references/regression_scenarios.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Regression File Index", index)
        for relative in REGRESSION_FILES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)
                self.assertIn(relative, index)

    def test_no_regression_file_costs_the_whole_corpus(self) -> None:
        sizes = dict(validator.scan_markdown(ROOT))
        for relative in REGRESSION_FILES:
            with self.subTest(relative=relative):
                self.assertLessEqual(sizes[relative], validator.BUDGET_TARGET_BYTES)

    def test_recovery_guards_are_no_longer_buried_in_the_scenario_corpus(self) -> None:
        guards = (ROOT / "references/recovery_guards.md").read_text(encoding="utf-8-sig")
        for case in ("LR-R1", "LR-R10", "SD-R1", "SD-R5"):
            with self.subTest(case=case):
                self.assertIn(case, guards)
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(encoding="utf-8-sig")
        for text in (card, criteria):
            with self.subTest(text=text[:40]):
                self.assertIn("references/recovery_guards.md", text)

    def test_every_scenario_family_survives_the_split(self) -> None:
        corpus = regression_corpus()
        for scenario in ("R09", "R15", "R23", "R24", "R27", "R48", "R52",
                         "Deterministic Expectations"):
            with self.subTest(scenario=scenario):
                self.assertIn(scenario, corpus)

    def test_whole_skill_still_fits_its_own_budget(self) -> None:
        self.assertEqual(
            validator.check_context_budget(
                validator.scan_markdown(ROOT), validator.read_size_ledger(ROOT)
            ),
            [],
        )


class R53LongTermBudgetMaintenanceTests(unittest.TestCase):
    """The budget only holds if it prevents growth as well as measuring it: a
    prevent layer, an enforce layer, a recurring audit, and a module-contract
    split that leaves the ledger describing only genuinely integral files."""

    def test_module_contracts_are_split_and_absent_from_the_ledger(self) -> None:
        ledger = validator.read_size_ledger(ROOT)
        sizes = dict(validator.scan_markdown(ROOT))
        for relative in MODULE_CONTRACT_FILES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)
                self.assertLessEqual(sizes[relative], validator.BUDGET_TARGET_BYTES)
                self.assertNotIn(relative, ledger)

    def test_authority_and_owner_list_stay_in_the_framework_file(self) -> None:
        frame = (ROOT / "references/module_contracts.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Authority Matrix", frame)
        self.assertIn("## Stable Interface Rules", frame)
        self.assertIn("## Module Contract File Index", frame)
        for relative in MODULE_CONTRACT_FILES[1:]:
            with self.subTest(relative=relative):
                self.assertIn(relative, frame)

    def test_split_files_do_not_re_own_the_authority_matrix(self) -> None:
        for relative in MODULE_CONTRACT_FILES[1:]:
            text = (ROOT / relative).read_text(encoding="utf-8-sig")
            with self.subTest(relative=relative):
                self.assertNotIn("## Authority Matrix", text)
                self.assertIn("references/module_contracts.md", text)

    def test_every_module_contract_section_survived_the_split(self) -> None:
        corpus = "\n".join(
            (ROOT / relative).read_text(encoding="utf-8-sig") for relative in MODULE_CONTRACT_FILES
        )
        for section in (
            "Stable Interface Rules", "Authority Matrix",
            "Screenwriter Module, Adaptation And Analysis Gate Contract",
            "STATE-03 Visual Asset Production Contract", "Prompt Compilation Module Contract",
            "Clip Production Module Contract", "Project State And Recovery Contract",
            "Shot Language Router Contract", "Clip Preflight Check Module Contract",
            "MUSIC / SEED-MUSIC Score Module Contract", "AUDIO / SEED-AUDIO Voice Asset Module Contract",
            "Skill Experience Module Contract", "Poster Design Module Contract",
            "Sequence Module Contract", "Fast Automation Policy Contract",
            "Performance Expression Knowledge Contract", "Transition Knowledge Contract",
            "Focal Length Knowledge Contract", "Color Knowledge Contract",
            "Camera Movement Combination Knowledge Contract", "Camera Composition Knowledge Contract",
            "Camera Movement Selection Matrix Knowledge Contract", "Lighting Knowledge Contract",
            "Quality Knowledge Contract",
        ):
            with self.subTest(section=section):
                self.assertIn(section, corpus)

    def test_periodic_audit_report_is_produced(self) -> None:
        report = validator.build_report(ROOT)
        for marker in ("SD Film Size And Readability Report", "largest files",
                       "past the review line", "review by"):
            with self.subTest(marker=marker):
                self.assertIn(marker, report)

    def test_stale_ledger_size_is_rejected(self) -> None:
        findings = validator.check_ledger_sizes(
            [("big/thing.md", 80 * 1024)], {"big/thing.md": 50.0}
        )
        self.assertTrue(any("stale" in item for item in findings))

    def test_duplicate_rule_check_also_requires_consolidation_judgement(self) -> None:
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(encoding="utf-8-sig")
        for marker in ("必须显式判定是否存在可合并或可退役的既有规则",
                       "merge_existing", "deprecate/remove", "Additive By Default"):
            with self.subTest(marker=marker):
                self.assertIn(marker, criteria)

    def test_current_ledger_sizes_are_accurate(self) -> None:
        self.assertEqual(
            validator.check_ledger_sizes(
                validator.scan_markdown(ROOT), validator.read_ledger_sizes(ROOT)
            ),
            [],
        )


class R55ToolIndependentSelfMaintenanceTests(unittest.TestCase):
    """The self-check has to travel with the skill files, not with the machine:
    another agent, another platform, no Python, no cron — the rules must still
    be readable and executable by hand."""

    def test_skill_entry_declares_self_maintenance_up_front(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Self-Maintenance", skill)
        self.assertLess(skill.index("## Self-Maintenance"), skill.index("## Modules"))
        for marker in ("归属判定", "可达性判定", "减法判定", "纯文本的", "Skill Version"):
            with self.subTest(marker=marker):
                self.assertIn(marker, skill)

    def test_run_card_guards_writing_before_it_audits_after(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Before You Write", card)
        self.assertLess(card.index("## Before You Write"), card.index("## Trigger"))
        for marker in ("确认这是正式修改", "归属判定", "可达性判定", "减法判定",
                       "读文件即可完成的人工判断"):
            with self.subTest(marker=marker):
                self.assertIn(marker, card)

    def test_verification_separates_manual_baseline_from_optional_tooling(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        for marker in ("手工执行（任何环境都必须做）", "有工具时的加固",
                       "左列在任何环境下都必须完成；右列只是本机可选加固"):
            with self.subTest(marker=marker):
                self.assertIn(marker, card)

    def test_protocol_is_declared_manually_executable(self) -> None:
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(encoding="utf-8-sig")
        for marker in ("本协议是纯文本、人工可执行的", "不得以“缺少工具”为由降低检查强度"):
            with self.subTest(marker=marker):
                self.assertIn(marker, criteria)

    def test_chain_puts_judgement_before_the_edit(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("Before You Write: ownership / size / subtraction judgement", card)
        self.assertLess(
            card.index("Before You Write: ownership"),
            card.index("Apply minimal change"),
        )

    def test_self_maintenance_is_not_delegated_to_tooling(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        section = skill[skill.index("## Self-Maintenance"):skill.index("## Modules")]
        self.assertIn("不依赖任何脚本、工具或外部服务即可手工执行", section)
        self.assertIn("换了别的Agent", section)

    def test_original_check_layer_identity_survives_the_move(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        section = skill[skill.index("## Self-Maintenance"):skill.index("## Modules")]
        self.assertIn("Skill Update Self-Check / Change Safety Checklist", section)
        self.assertIn("不构成第二套检查体系", section)
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("Skill Update Self-Check / Change Safety Checklist", card)
        self.assertIn("唯一权威来源", card)

    def test_there_is_only_one_check_system_entry(self) -> None:
        owners = [p for p in (
            "references/maintenance_self_check.md",
            "references/maintenance_self_check_protocol.md",
        ) if (ROOT / p).is_file()]
        self.assertEqual(len(owners), 2)
        # 旧位置不得再保留一份可执行的并行副本
        contracts = (ROOT / "references/module_contracts.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("### Check Dimensions", contracts)
        self.assertNotIn("### Required Self-Check Summary", contracts)


class R56MaintenanceConsolidationTests(unittest.TestCase):
    """One maintenance system, one owner per rule body. The judgement set that
    must happen before writing is described once — not three times."""

    def test_system_map_exposes_every_member(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Maintenance System Map", card)
        for member in ("SKILL.md", "maintenance_self_check_protocol.md",
                       "context_budget.md", "recovery_guards.md", "module_contracts.md"):
            with self.subTest(member=member):
                self.assertIn(member, card)
        self.assertIn("分层关系，不是并行副本", card)

    def test_budget_file_no_longer_owns_the_maintenance_layers(self) -> None:
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("## Long-Term Maintenance", budget)
        for leaked in ("### 1. Prevent", "### 2. Enforce", "### 3. Audit", "### 4. Debt Policy"):
            with self.subTest(leaked=leaked):
                self.assertNotIn(leaked, budget)
        self.assertIn("## Budget Discipline", budget)
        self.assertIn("变厚必须给出入口", budget)

    def test_write_time_judgement_has_a_single_full_description(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        for marker in ("归属判定", "可达性判定", "减法判定"):
            with self.subTest(marker=marker):
                self.assertIn(marker, card)
        # 体量文件不得再写一遍完整的归属／重复判定正文
        self.assertNotIn("先归位，再新增", budget)
        self.assertNotIn("正文不复制", budget)

    def test_the_three_layers_live_in_the_run_card(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        for layer in ("Prevent｜写之前", "Enforce｜改的时候", "Audit｜周期性"):
            with self.subTest(layer=layer):
                self.assertIn(layer, card)

    def test_skill_entry_positions_itself_as_summary_only(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        section = skill[skill.index("## Self-Maintenance"):skill.index("## Modules")]
        self.assertIn("本节只列**不变量**", section)
        self.assertIn("Maintenance System Map", section)


class R57MediumProfileTests(unittest.TestCase):
    """A medium is not a genre. Live action, 3D and 2D share one narrative core
    but not one camera language, so the axis has to be named, routed, and
    carried by the field that already exists rather than a new one."""

    def _profiles(self) -> str:
        return (ROOT / "knowledge/medium_profiles.md").read_text(encoding="utf-8-sig")

    def test_exactly_three_profiles_are_defined(self) -> None:
        text = self._profiles()
        for profile in ("`live_action`", "`3d_animation`", "`2d_anime`"):
            with self.subTest(profile=profile):
                self.assertIn(profile, text)
        self.assertIn("不得新增第四档或改名", text)

    def test_each_layer_has_its_own_divergence_table(self) -> None:
        text = self._profiles()
        for layer in ("## Screenwriter Layer", "## Director Layer", "## Aesthetic Layer"):
            with self.subTest(layer=layer):
                self.assertIn(layer, text)

    def test_drawn_medium_bans_optical_parameters(self) -> None:
        text = self._profiles()
        self.assertIn("**`2d_anime` 禁止项**", text)
        for banned in ("焦段毫米数", "光比比值", "真实景深"):
            with self.subTest(banned=banned):
                self.assertIn(banned, text)

    def test_medium_is_orthogonal_to_genre(self) -> None:
        text = self._profiles()
        self.assertIn("媒介与Genre正交", text)
        self.assertIn("不改变Genre承诺", text)

    def test_medium_never_creates_prompt_fields(self) -> None:
        text = self._profiles()
        self.assertIn("不因媒介新增任何字段", text)
        self.assertIn("不改变任何Model Adapter能力", text)

    def test_medium_field_is_reused_not_duplicated(self) -> None:
        bible = (ROOT / "templates/01_project_bible_template.md").read_text(encoding="utf-8-sig")
        self.assertEqual(bible.count("媒介形式"), 1)
        self.assertIn("未确认写 `Pending`", bible)

    def test_unconfirmed_medium_stays_pending(self) -> None:
        setup = (ROOT / "workflows/01_project_setup_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("# Medium Profile｜Internal", setup)
        self.assertIn("不得默认取`2d_anime`或`live_action`", setup)
        self.assertIn("不得把它登记为已确认真人剧", setup)

    def test_medium_route_reaches_script_analysis(self) -> None:
        script = (ROOT / "workflows/02_script_analysis_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("媒介剖面与目标形式是两根独立的轴", script)

    def test_medium_gate_precedes_the_aesthetic_lock(self) -> None:
        visual = (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("# Medium Profile Gate", visual)
        self.assertLess(
            visual.index("# Medium Profile Gate"),
            visual.index("# Aesthetic Decision Lock Gate"),
        )

    def test_medium_profile_is_discoverable_from_the_knowledge_index(self) -> None:
        index = (ROOT / "knowledge/00_knowledge_index.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Persistent Medium Profile", index)
        self.assertIn("knowledge/medium_profiles.md", index)

    def test_medium_profile_has_a_registered_owner_contract(self) -> None:
        contracts = (ROOT / "references/module_contracts_knowledge.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Medium Profile Knowledge Contract", contracts)
        self.assertIn("knowledge/medium_profiles.md", contracts)

    def test_medium_profile_stays_within_the_new_file_budget(self) -> None:
        size = len((ROOT / "knowledge/medium_profiles.md").read_bytes())
        self.assertLess(size, validator.BUDGET_TARGET_BYTES * 0.6)


class R59ShotDesignBreakdownTests(unittest.TestCase):
    """Shot size is a taxonomy with one owner, and rhythm intent is a scene
    fact that needs a recorded field. Both were only half-wired: the shot-size
    list lived twice with different lengths, and the sequence planner read a
    rhythm intent that no template recorded."""

    def _shot_design(self) -> str:
        return (ROOT / "workflows/09_shot_design_workflow.md").read_text(encoding="utf-8-sig")

    def _scale_section(self) -> str:
        text = self._shot_design()
        start = text.index("## Shot Size")
        return text[start:text.index("## Camera Movement", start)]

    def test_shot_size_is_routed_to_its_single_owner(self) -> None:
        text = self._shot_design()
        self.assertIn(
            "景别选择必须读取`knowledge/camera_language/lens_language/framing_and_scale.md`", text
        )
        self.assertIn(
            "规范景别由`knowledge/camera_language/lens_language/framing_and_scale.md`唯一拥有",
            text,
        )

    def test_inline_shot_scale_matches_the_canonical_owner(self) -> None:
        """A short inline list next to the authoritative step is a near-at-hand
        authority: it silently drops the two most-used sizes."""
        section = self._scale_section()
        for size in ("大全景。", "远景。", "全景。", "中景。", "中近景。", "近景。", "特写。", "大特写。"):
            with self.subTest(size=size):
                self.assertIn(size, section)
        for extra in ("局部镜头。", "细节插入镜头。"):
            with self.subTest(extra=extra):
                self.assertIn(extra, section)

    def test_inline_scale_refuses_to_be_a_second_owner(self) -> None:
        section = self._scale_section()
        self.assertIn("不得维护平行景别清单", section)

    def test_shot_scale_has_a_registered_owner_contract(self) -> None:
        contracts = (ROOT / "references/module_contracts_knowledge.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Shot Size And Framing Knowledge Contract", contracts)
        self.assertIn(
            "规范景别的唯一owner是`knowledge/camera_language/lens_language/framing_and_scale.md`",
            contracts,
        )
        self.assertIn("不维护平行景别清单", contracts)

    def test_rhythm_intent_has_a_recorded_field(self) -> None:
        """The sequence planner reads a confirmed rhythm intent; that intent
        has to be recorded somewhere or its consumer is orphaned."""
        scene_template = (ROOT / "templates/07_scene_design_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("Rhythm Intent（节奏结构", scene_template)
        self.assertIn("Scene Camera Strategy", scene_template)

    def test_scene_breakdown_is_what_writes_the_rhythm_intent(self) -> None:
        breakdown = (ROOT / "workflows/08_scene_breakdown_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Scene Rhythm Intent Projection", breakdown)
        self.assertIn("Scene Directing Brief", breakdown)
        self.assertIn("已把已确认Rhythm Intent投影为节奏结构", breakdown)

    def test_rhythm_projection_never_pre_commits_a_shot_count(self) -> None:
        """The existing doctrine forbids fixing shot count before the shots are
        designed. A rhythm section must not smuggle that decision back in."""
        breakdown = (ROOT / "workflows/08_scene_breakdown_workflow.md").read_text(encoding="utf-8-sig")
        section = breakdown[
            breakdown.index("## Scene Rhythm Intent Projection"):breakdown.index("## Source Label Normalization")
        ]
        self.assertIn("不在本阶段预定", section)
        self.assertIn("不写景别、焦段、机位、运镜路径、具体镜头数量", section)
        self.assertIn("未确认Rhythm Intent时写`Pending`", section)

    def test_rhythm_consumer_points_at_the_recorded_field(self) -> None:
        sequence = (ROOT / "workflows/16_sequence_planning_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("`templates/07_scene_design_prompt.md`的`Scene Directing Brief`", sequence)
        self.assertIn("本阶段不重新产生节奏意图", sequence)

    def test_rhythm_intent_field_is_declared_by_the_director_owner(self) -> None:
        director = (ROOT / "knowledge/director_decision_layer.md").read_text(encoding="utf-8-sig")
        self.assertIn("供条件性Sequence Planning与STATE-06消费", director)
        self.assertIn("不预定镜头数量", director)

    def test_storyboard_stays_a_side_route_of_the_shot_template(self) -> None:
        """A storyboard is a separate auxiliary route, not a richer version of
        the shot table; conflating them is how it leaks into generation."""
        shot_template = (ROOT / "templates/08_shot_design_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("旁路而不是升级档", shot_template)
        self.assertIn("workflows/10_storyboard_workflow.md", shot_template)
        self.assertIn("不进入STATE-07 / STATE-08参考资产", shot_template)

    def test_rhythm_projection_declares_where_it_is_recorded(self) -> None:
        """The projection guard used to claim it added no user-visible field,
        which stopped being true once the Scene Directing Brief recorded it.
        The guard that matters is no second schema and no new IDs."""
        breakdown = (ROOT / "workflows/08_scene_breakdown_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("其投影只落在`templates/07_scene_design_prompt.md`既有的`Scene Directing Brief`区块内", breakdown)
        self.assertIn("不创建第二套输出Schema、新STATE或SHOT / CLIP", breakdown)
        self.assertNotIn("不新增用户可见固定字段", breakdown)

    def test_shot_budget_is_not_introduced_anywhere(self) -> None:
        """Fixing shot count before the shots exist is explicitly forbidden, so
        no fix may smuggle a budget into the scene stage."""
        for relative in ("workflows/08_scene_breakdown_workflow.md", "templates/07_scene_design_prompt.md"):
            text = (ROOT / relative).read_text(encoding="utf-8-sig")
            with self.subTest(relative=relative):
                self.assertNotIn("Shot Budget", text)

    def test_user_guide_separates_the_three_shot_delivery_forms(self) -> None:
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("分镜的三种形态", guide)
        self.assertIn("默认分镜表", guide)
        self.assertIn("完整版专业分镜", guide)
        self.assertIn("Storyboard 视觉分镜板", guide)


if __name__ == "__main__":
    unittest.main()
