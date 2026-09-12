#!/usr/bin/env python3
"""Regression tests for the r81 SD Film validator."""
# Skill维护层：只在修改本Skill时读取，不参与影视生产。
from __future__ import annotations
import importlib.util
import tempfile
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
    "references/regression_scenarios_maintenance.md",
    "references/recovery_guards.md",
)

def regression_corpus() -> str:
    """The regression set is split across five files; assertions target the set."""
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
        gpt_image_adapter = (ROOT / "adapters/gpt-image.md").read_text(encoding="utf-8-sig")
        gpt_image_template = (ROOT / "templates/24_gpt_image_asset_prompt.md").read_text(encoding="utf-8-sig")
        midjourney = (ROOT / "adapters/midjourney.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/14_midjourney_asset_prompt.md").read_text(encoding="utf-8-sig")
        video_selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        self.assertIn("不得默认选择GPT Image、Midjourney或任何第三方服务", assets)
        self.assertIn("## Available Choices", selection)
        self.assertIn("不得默认选择GPT Image、Midjourney或其他模型", selection)
        self.assertIn("prompt_output_template: templates/24_gpt_image_asset_prompt.md", gpt_image_adapter)
        self.assertIn("## GPT Image Prompt Package", gpt_image_template)
        self.assertIn("只输出可直接粘贴的 Midjourney Prompt", midjourney)
        self.assertIn("不调用`GPT Image`", midjourney)
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

    def test_gpt_image_requires_selection_and_actual_generation_capability(self) -> None:
        assets = (ROOT / "modules/assets.md").read_text(encoding="utf-8-sig")
        character = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("Direct Image Default", assets)
        self.assertIn("仅已选择GPT Image且当前环境实际可用时", character)
        self.assertIn("不得因环境可生成而跳过图像模型选择或Prompt确认", rules)

    def test_production_setup_is_confirmed_after_script_lock_and_before_assets(self) -> None:
        setup = (ROOT / "workflows/01_project_setup_workflow.md").read_text(encoding="utf-8-sig")
        script = (ROOT / "workflows/02_script_analysis_workflow.md").read_text(encoding="utf-8-sig")
        image_selection = (ROOT / "modules/image-model-selection.md").read_text(encoding="utf-8-sig")
        video_selection = (ROOT / "modules/model-selection.md").read_text(encoding="utf-8-sig")
        state = (ROOT / "references/project_state_contract.md").read_text(encoding="utf-8-sig")
        # STATE-00 must not ask for models or style; it only points at the post-script gate.
        self.assertNotIn("Project Model Selection Gate", setup)
        self.assertIn("Production Setup Gate", setup)
        self.assertIn("## 07 Production Setup Gate", script)
        self.assertIn("`Script Status: Production-Locked`之后、STATE-01 Completion Gate通过之前", script)
        self.assertIn("Project Style Baseline", script)
        self.assertIn("Production Setup Proposal", image_selection)
        self.assertIn("STATE-06后读取Confirmed Detailed Shot Design", video_selection)
        self.assertIn("Project Image Model Default", state)
        self.assertIn("Project Video Model Preference", state)
        self.assertIn("Project Style Baseline", state)

    def test_asset_batch_image_round_submits_the_whole_batch_in_one_pass(self) -> None:
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        character = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        adapter = (ROOT / "adapters/gpt-image.md").read_text(encoding="utf-8-sig")
        self.assertIn("同一轮内提交整批全部图片", rules)
        self.assertIn("不得逐张生成后停顿", rules)
        self.assertIn("Core外观参考图同样整批提交、整批确认", rules)
        self.assertIn("整批生成该批次全部外观参考图", character)
        self.assertIn("不得逐张生成后停顿", character)
        self.assertIn("不得逐张串行生成后停顿", adapter)

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
        builtin = (ROOT / "templates/24_gpt_image_asset_prompt.md").read_text(encoding="utf-8-sig")
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
        self.assertIn("不得默认选择GPT Image、Midjourney或任何第三方服务", assets)
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

    def test_nested_staging_skill_entry_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "SKILL.md").write_text("---\nname: sd-film\n---\n", encoding="utf-8")
            staging = root / "tmp" / "sd-push" / "SKILL.md"
            staging.parent.mkdir(parents=True)
            staging.write_text("---\nname: sd-film\n---\n", encoding="utf-8")
            self.assertEqual(
                validator.duplicate_sd_film_entries(root),
                ["tmp/sd-push/SKILL.md"],
            )

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

    def test_environment_view_set_covers_lateral_eye_level_and_demotes_oblique(self) -> None:
        """ENV-03 必须覆盖最常用的侧向平视；约45°斜俯由默认必出项降为按需扩展。

        根因：原基础集里平视只有0°与180°，而真实拍摄的主镜常来自垂直于关系轴线的侧向机位；
        两张俯视占用了必出名额，且俯视作为画面参考会把下游机位带高。
        """
        reconstruction = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/05_environment_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("`ENV-03` Lateral View", reconstruction)
        self.assertIn("侧向平视", reconstruction)
        self.assertIn("`ENV-03｜Lateral View", template)
        self.assertIn("侧向平视", template)
        self.assertNotIn("`ENV-03` Oblique Overhead View", reconstruction)
        self.assertNotIn("Oblique Overhead View（默认约45°）", template)
        self.assertIn("约45°斜俯由默认必出项降为按需扩展", reconstruction)
        self.assertIn("约45°斜俯不是默认项", template)

    def test_environment_direction_anchor_contract_precedes_env01(self) -> None:
        """背向与侧向区域在 ENV-01 中不存在信息：必须先把360°方位锚点写成文本契约再逐View重建。

        该契约是 `Major Spatial Anchors` 的事前写法，不新增 Registry 字段、不新增确认 Gate。
        """
        reconstruction = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/05_environment_asset_prompt.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/05_environment_asset_workflow.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Direction Anchor Contract｜方向锚点契约", reconstruction)
        self.assertIn("在生成`ENV-01`**之前**", reconstruction)
        self.assertIn("不新增Registry字段、不新增确认Gate", reconstruction)
        self.assertIn("按方位写定完整360°空间锚点", template)
        self.assertIn("360°空间锚点", workflow)

    def test_environment_topdown_is_verification_not_frame_reference(self) -> None:
        """ENV-04 只作几何校验；默认不得进入下游画面参考位，避免把机位带高。"""
        reconstruction = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        budget = (ROOT / "knowledge/reference_budget.md").read_text(encoding="utf-8-sig")
        self.assertIn("只作空间校验用途", reconstruction)
        self.assertIn("`ENV-04`默认不进入画面参考位", reconstruction)
        self.assertIn("`ENV-04`默认不进入画面参考位", budget)
        self.assertIn("摄影机高度确实落在高位俯视区间", budget)

    def test_environment_view_form_is_not_restated_outside_its_owner(self) -> None:
        """环境View形态只在 environment_multi_view_reconstruction.md 定义；流程层只允许指针。"""
        forbidden = ("Lateral View", "Oblique Overhead", "Top-Down Spatial View", "Reverse View")
        workflow = (ROOT / "workflows/05_environment_asset_workflow.md").read_text(encoding="utf-8-sig")
        for token in forbidden:
            self.assertNotIn(token, workflow, f"workflows/05 复述了环境View形态：{token}")
        owner = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        self.assertIn("`ENV-03` Lateral View", owner)

    def test_environment_views_after_the_master_are_delivered_in_one_round(self) -> None:
        """母参考确认后，其余方位视图必须同轮连续出齐、只做一次图片批次确认。

        根因：累积约束原本写成“每一步先完成现有双确认”，于是 ENV-02 必须先被用户确认
        才能作为 ENV-03 的输入，出图退化成一张一张停。累积约束约束的是生成输入，不是确认次数。
        """
        owner = (ROOT / "knowledge/environment_multi_view_reconstruction.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/05_environment_asset_workflow.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/05_environment_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("不得为每个View插入一次用户确认往返", owner)
        self.assertIn("无需等待用户先确认ENV-02", owner)
        self.assertIn("ENV-01 + ENV-02 → ENV-03", owner)
        self.assertIn("ENV-01 + ENV-02 + ENV-03 → ENV-04", owner)
        self.assertIn("不逐View停顿等待确认", workflow)
        self.assertIn("只在整组这一层做一次图片批次确认", workflow)
        self.assertIn("View之间的累积输入不构成逐项用户确认，不得逐View停顿", rules)
        self.assertIn("只在整组就绪后做一次图片批次确认", template)

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


class R60LookFrameTests(unittest.TestCase):
    """A decision made without ever seeing the result is a bet, not a decision.
    The look frame adds the missing step: try a few frames, look, then lock.
    Its whole safety property is that it must never enter the asset chain."""

    def _gate(self) -> str:
        return (ROOT / "workflows/07_visual_development_workflow.md").read_text(encoding="utf-8-sig")

    def _template(self) -> str:
        return (ROOT / "templates/25_look_frame_prompt.md").read_text(encoding="utf-8-sig")

    def test_look_frame_sits_between_draft_and_lock(self) -> None:
        gate = self._gate()
        self.assertIn("# Look Frame Gate", gate)
        self.assertIn("草案成形之后、正式锁定之前", gate)
        self.assertIn("那不是决定，是赌注", gate)
        self.assertLess(
            gate.index("# Aesthetic Decision Lock Gate"),
            gate.index("# Look Frame Gate"),
        )

    def test_look_frame_never_enters_the_asset_chain(self) -> None:
        template = self._template()
        self.assertIn("非生产视觉材料", template)
        self.assertIn("不得进入 STATE-08【参考资产】", template)
        self.assertIn("登记为 Canonical Asset", template)
        gate = self._gate()
        self.assertIn("不写入项目状态", gate)
        self.assertIn("不新增工件 ID 或 STATE", gate)

    def test_look_frame_stays_separate_from_ref_sketch(self) -> None:
        template = self._template()
        self.assertIn("与 REF-SKETCH 的边界", template)
        self.assertIn("无性别技术调度人偶", template)
        self.assertIn("不得共用模板", template)

    def test_look_frame_budget_is_capped(self) -> None:
        template = self._template()
        self.assertIn("1—3 张", template)
        self.assertIn("超过 3 张视为未做取舍", template)

    def test_look_frame_never_lets_the_system_judge_beauty(self) -> None:
        for text in (self._template(), self._gate()):
            with self.subTest(source="closure"):
                self.assertIn("判断必须由用户给出", text)
        self.assertIn("不得声称做过试片", self._template())

    def test_forbidden_actions_no_longer_block_the_look_frame(self) -> None:
        gate = self._gate()
        self.assertIn("Look Frame 试片帧不属于 Storyboard 视觉材料", gate)
        self.assertIn("生成任何其他提前视觉材料", gate)

    def test_generation_prohibitions_name_the_look_frame(self) -> None:
        output_rules = (ROOT / "rules/05_output_rules.md").read_text(encoding="utf-8-sig")
        prompt_rules = (ROOT / "rules/03_prompt_rules.md").read_text(encoding="utf-8-sig")
        self.assertEqual(output_rules.count("Look Frame试片帧"), 2)
        self.assertIn("Look Frame试片帧", prompt_rules)

    def test_director_layer_and_contract_own_it(self) -> None:
        director = (ROOT / "knowledge/director_decision_layer.md").read_text(encoding="utf-8-sig")
        contracts = (ROOT / "references/module_contracts.md").read_text(encoding="utf-8-sig")
        self.assertIn("四维度从草案到锁定之间允许执行一次可选`Look Frame`", director)
        self.assertIn("与其可选`Look Frame`由Director层拥有", contracts)


class R60AestheticJudgementTests(unittest.TestCase):
    """Two of the hundred points used to ask only whether the Lock was copied.
    Copying a rule is not the same as making a choice visible."""

    def _scorecard(self) -> str:
        return (ROOT / "knowledge/quality/prompt_scorecard.md").read_text(encoding="utf-8-sig")

    def test_scorecard_points_at_the_single_owner_instead_of_copying_it(self) -> None:
        """The criteria now live in one place; the scorecard must reference it,
        not keep a second full copy that can drift."""
        card = self._scorecard()
        self.assertIn("### Aesthetic Criteria｜两项审美维度的评分依据", card)
        self.assertIn("唯一由`knowledge/quality/aesthetic_judgement.md`拥有；本文件只引用，不复制其正文", card)
        for criterion in ("视觉重心唯一", "明暗有层级", "色彩有主从", "取舍可见", "不平均"):
            with self.subTest(criterion=criterion):
                self.assertNotIn(criterion, card)

    def test_restating_the_lock_is_not_enough(self) -> None:
        card = self._scorecard()
        self.assertIn("取舍在Prompt里是否可见", card)
        self.assertIn("不得只复述Lock的措辞", card)

    def test_hard_gate_requires_visible_tradeoff_evidence(self) -> None:
        card = self._scorecard()
        self.assertIn("未写出可见取舍证据", card)

    def test_the_honest_limit_is_still_declared(self) -> None:
        """Scoring still cannot judge taste; the remaining half belongs to the
        look frame and to the user at review, and saying so is the point."""
        card = self._scorecard()
        self.assertIn("本评分仍不能替代人工审美判断", card)
        self.assertIn("由STATE-04的`Look Frame`与STATE-09的用户Review承担", card)

    def test_weights_are_unchanged(self) -> None:
        card = self._scorecard()
        self.assertIn("| Story / Shot Purpose Fidelity | 15 |", card)
        self.assertIn("| Spatial / Action / Boundary Continuity | 20 |", card)
        self.assertIn("| Seedance Stability And Risk Downgrade | 15 |", card)
        self.assertIn("| Template / Semantic Projection Discipline | 5 |", card)


class R61AestheticJudgementAtReviewTests(unittest.TestCase):
    """Review could find "you did not follow the decision" but never "the
    decision was wrong". It also had no aesthetic criterion at all - the word
    appeared once, and only to forbid keeping a shot for looking good."""

    def _owner(self) -> str:
        return (ROOT / "knowledge/quality/aesthetic_judgement.md").read_text(encoding="utf-8-sig")

    def _review(self) -> str:
        return (ROOT / "workflows/13_review_workflow.md").read_text(encoding="utf-8-sig")

    def test_criteria_have_exactly_one_owner(self) -> None:
        owner = self._owner()
        for criterion in ("视觉重心唯一", "明暗有层级", "色彩有主从", "取舍可见", "不平均", "景深 / 清晰度有意图"):
            with self.subTest(criterion=criterion):
                self.assertIn(criterion, owner)
        for other in ("knowledge/quality/prompt_scorecard.md",
                      "workflows/13_review_workflow.md"):
            text = (ROOT / other).read_text(encoding="utf-8-sig")
            with self.subTest(other=other):
                self.assertIn("knowledge/quality/aesthetic_judgement.md", text)
                self.assertNotIn("视觉重心唯一", text)
                self.assertNotIn("明暗有层级", text)

    def test_the_system_never_judges_beauty(self) -> None:
        for name, text in (
            ("owner", self._owner()),
            ("review workflow", self._review()),
            ("review template", (ROOT / "templates/16_review_report.md").read_text(encoding="utf-8-sig")),
        ):
            with self.subTest(source=name):
                self.assertIn("系统只输出观察", text)
                self.assertIn("用户", text)

    def test_passing_the_criteria_is_not_proof_of_beauty(self) -> None:
        self.assertIn("六条全过不等于好看", self._owner())
        self.assertIn("六条全过不等于好看", self._review())

    def test_review_gains_a_return_path_to_state04(self) -> None:
        review = self._review()
        self.assertIn("## Aesthetic Judgement", review)
        self.assertIn("返回STATE-04重做该维度", review)
        self.assertLess(
            review.index("## Aesthetic Judgement"),
            review.index("## Director QA Return Route"),
        )

    def test_aesthetics_does_not_add_a_failure_class(self) -> None:
        """The existing classes are already orthogonal; a new one would fork
        the whole failure taxonomy for one dimension."""
        template = (ROOT / "templates/16_review_report.md").read_text(encoding="utf-8-sig")
        self.assertIn("不新增Failure Class", template)
        self.assertIn("美学决定本身被判定不成立或选错时记DIRECTING FAILURE", template)

    def test_review_template_blocks_pass_without_the_user_verdict(self) -> None:
        template = (ROOT / "templates/16_review_report.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Aesthetic Judgement（对照STATE-04 Aesthetic Decision Lock）", template)
        self.assertIn("`PENDING_USER`", template)
        self.assertIn("Overall Result也不得判为`PASS`", template)
        self.assertIn("系统不得代填本项", template)

    def test_review_is_the_only_reader_allowed_back_into_the_look_frame(self) -> None:
        template = (ROOT / "templates/25_look_frame_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("**唯一例外**", template)
        self.assertIn("STATE-09 Review 可以把它作为**当初美学决定的对照参照**读取", template)
        self.assertIn("不得据此重新生成资产", template)

    def test_consistency_review_stays_separate_from_judgement(self) -> None:
        review = self._review()
        self.assertIn("与`# 10 Style Review`的一致性检查正交", review)
        owner = self._owner()
        self.assertIn("与「一致性检查」的区别", owner)


def workflow_body(state: str) -> str:
    return (
        "# Workflow Position\n\n"
        f"当前阶段：\n{state}\n\n"
        "前置阶段、下一阶段与对应下一 Workflow 的唯一 owner：\n"
        "`workflows/workflow_map.md`\n\n"
        "# Completion Gate\n\n"
        "前置工件已确认，本阶段可完成。\n"
    )

def write_main_workflows(root: Path, overrides: dict[str, str] | None = None) -> None:
    overrides = overrides or {}
    for name, state in validator.MAIN_WORKFLOWS:
        path = root / "workflows" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(overrides.get(name, workflow_body(state)), encoding="utf-8")

class R68WorkflowRoutingIntegrityTests(unittest.TestCase):
    """r65 unified the Workflow Position blocks and r67 removed the tail restatement.
    These tests hold that line, and each one proves a new validator check fires."""

    def test_active_skill_passes_both_new_checks(self) -> None:
        self.assertEqual(validator.check_workflow_routing(ROOT), [])
        self.assertEqual(validator.check_internal_references(ROOT), [])

    def test_every_main_workflow_self_declares_its_state(self) -> None:
        for name, state in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            match = validator.WORKFLOW_STATE_RE.search(text)
            self.assertIsNotNone(match, f"{name} has no 当前阶段 declaration")
            self.assertEqual(match.group(1), state, name)

    def test_route_owner_is_the_single_declared_source(self) -> None:
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            self.assertIn(validator.WORKFLOW_ROUTE_OWNER, text, name)

    def test_position_blocks_carry_no_route_fields(self) -> None:
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            position = validator.WORKFLOW_POSITION_RE.search(text)
            self.assertIsNotNone(position, name)
            block = validator.section_after(text, position)
            for field in validator.WORKFLOW_ROUTE_FIELDS:
                self.assertNotIn(field, block, f"{name} restates {field}")

    def test_workflows_do_not_restate_the_pipeline_order(self) -> None:
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            self.assertIsNone(validator.PIPELINE_RESTATEMENT_RE.search(text), name)

    def test_remaining_final_principles_are_one_line_mottos(self) -> None:
        kept: list[str] = []
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            for motto in validator.FINAL_PRINCIPLE_RE.finditer(text):
                section = validator.section_after(text, motto)
                self.assertLessEqual(
                    len(section.encode("utf-8")),
                    validator.FINAL_PRINCIPLE_MAX_BYTES,
                    f"{name} Final Principle is no longer a motto",
                )
                kept.append(name)
        self.assertEqual(
            sorted(kept),
            sorted([
                "05_environment_asset_workflow.md",
                "06_prop_asset_workflow.md",
                "13_review_workflow.md",
            ]),
            "only the three stage-level mottos may keep a Final Principle section",
        )

    def test_fixture_is_clean_before_mutating(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_main_workflows(root)
            self.assertEqual(validator.check_workflow_routing(root), [])

    def test_wrong_state_declaration_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_main_workflows(
                root, {"11_video_generation_workflow.md": workflow_body("STATE-07")}
            )
            self.assertIn(
                "workflows/11_video_generation_workflow.md must self-declare "
                "当前阶段 STATE-08, found STATE-07",
                validator.check_workflow_routing(root),
            )

    def test_missing_state_declaration_leaves_a_pipeline_gap(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_main_workflows(root, {"10_clip_production_workflow.md": "# Clip Production\n"})
            errors = validator.check_workflow_routing(root)
            self.assertIn(
                "workflows/10_clip_production_workflow.md must self-declare "
                "当前阶段 STATE-07, found nothing",
                errors,
            )
            self.assertIn("main pipeline state STATE-07 has no self-declaring workflow", errors)

    def test_route_field_inside_position_block_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = (
                "# Workflow Position\n\n当前阶段：\nSTATE-04\n\n"
                "`workflows/workflow_map.md`\n\n下一阶段：\nSTATE-05 Scene Breakdown\n\n"
                "# Completion Gate\n\n前置工件已确认。\n"
            )
            write_main_workflows(root, {"07_visual_development_workflow.md": body})
            errors = validator.check_workflow_routing(root)
            self.assertTrue(
                any("must not restate 下一阶段：" in error and "07_visual" in error for error in errors),
                errors,
            )

    def test_missing_route_owner_pointer_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = "# Workflow Position\n\n当前阶段：\nSTATE-05\n"
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertIn(
                "workflows/08_scene_breakdown_workflow.md must route to "
                "workflows/workflow_map.md instead of restating the next workflow",
                validator.check_workflow_routing(root),
            )

    def test_missing_position_block_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = "当前阶段：\nSTATE-06\n\n`workflows/workflow_map.md`\n"
            write_main_workflows(root, {"09_shot_design_workflow.md": body})
            self.assertIn(
                "workflows/09_shot_design_workflow.md is missing its Workflow Position block",
                validator.check_workflow_routing(root),
            )

    def test_restated_pipeline_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-04") + "\n# Workflow Relationship\n\nScript Analysis\n"
            write_main_workflows(root, {"07_visual_development_workflow.md": body})
            errors = validator.check_workflow_routing(root)
            self.assertTrue(any("Workflow Relationship" in error for error in errors), errors)

    def test_oversized_final_principle_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-09") + "\n# Final Principle\n\n" + "复述。" * 80 + "\n"
            write_main_workflows(root, {"13_review_workflow.md": body})
            errors = validator.check_workflow_routing(root)
            self.assertTrue(
                any("Final Principle must stay a one-line motto" in error for error in errors),
                errors,
            )

    def test_dangling_internal_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "rules").mkdir()
            (root / "rules" / "sample.md").write_text(
                "见 `templates/does_not_exist.md`。\n", encoding="utf-8"
            )
            self.assertEqual(
                validator.check_internal_references(root),
                ["dangling internal reference: templates/does_not_exist.md (in rules/sample.md)"],
            )

    def test_scratch_directories_are_not_scanned_for_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            scratch = root / "tmp"
            scratch.mkdir()
            (scratch / "note.md").write_text("见 `rules/gone.md`。\n", encoding="utf-8")
            self.assertEqual(validator.check_internal_references(root), [])


class R72ClosingBlockAndRouteRestatementTests(unittest.TestCase):
    """The closing block has to be findable under one name in every stage, and the next
    stage's workflow name belongs to the route owner alone. Both are mutation-tested."""

    def test_every_main_workflow_has_exactly_one_completion_gate(self) -> None:
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            self.assertEqual(
                len(validator.COMPLETION_GATE_HEADING_RE.findall(text)), 1, name
            )

    def test_no_main_workflow_keeps_the_retired_state_update_heading(self) -> None:
        for name, _ in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            self.assertIsNone(validator.LEGACY_STATUS_HEADING_RE.search(text), name)

    def test_active_skill_names_no_other_stage_workflow(self) -> None:
        for name, state in validator.MAIN_WORKFLOWS:
            text = (ROOT / "workflows" / name).read_text(encoding="utf-8-sig")
            for reference in validator.WORKFLOW_REF_RE.finditer(text):
                target = reference.group(1) + ".md"
                if target == name or target in validator.AUXILIARY_WORKFLOWS:
                    continue
                self.assertEqual(
                    validator.MAIN_STATE_OF_WORKFLOW.get(target),
                    state,
                    f"{name} names {target}, which belongs to another stage",
                )

    def test_missing_completion_gate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = "# Workflow Position\n\n当前阶段：\nSTATE-05\n\n`workflows/workflow_map.md`\n"
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertIn(
                "workflows/08_scene_breakdown_workflow.md must carry exactly one "
                "`# Completion Gate` closing block, found 0",
                validator.check_workflow_routing(root),
            )

    def test_duplicate_completion_gate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-05") + "\n# Completion Gate\n\n第二个收尾块。\n"
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertIn(
                "workflows/08_scene_breakdown_workflow.md must carry exactly one "
                "`# Completion Gate` closing block, found 2",
                validator.check_workflow_routing(root),
            )

    def test_retired_state_update_heading_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-05") + "\n# State Update\n\n- Next Workflow：X\n"
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertIn(
                "workflows/08_scene_breakdown_workflow.md must name its state writeback "
                "`# Status Update`; `# State Update` is retired so the block stays retrievable",
                validator.check_workflow_routing(root),
            )

    def test_naming_another_stage_workflow_is_rejected(self) -> None:
        """The r67 cleanup only caught the `# Next Workflow` heading form; a stage name
        written inline or inside a code block slipped through until r72."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-05") + "\n下一步：\n\n```text\n09_shot_design_workflow.md\n```\n"
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertIn(
                "workflows/08_scene_breakdown_workflow.md must not name another stage's "
                "workflow (09_shot_design_workflow.md); workflows/workflow_map.md "
                "is the single route owner",
                validator.check_workflow_routing(root),
            )

    def test_auxiliary_workflow_reference_is_allowed(self) -> None:
        """Storyboard / resume / conditional planning do not own a main STATE, so a stage
        may point at them without becoming a second copy of the route."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = (
                workflow_body("STATE-05")
                + "\n按需调用`workflows/16_sequence_planning_workflow.md`与"
                "`workflows/18_project_resume_workflow.md`。\n"
            )
            write_main_workflows(root, {"08_scene_breakdown_workflow.md": body})
            self.assertEqual(validator.check_workflow_routing(root), [])

    def test_own_state_workflow_reference_is_allowed(self) -> None:
        """STATE-03 has four asset workflows; naming a sibling is not a route copy."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            body = workflow_body("STATE-03") + "\n同阶段的其余资产Workflow见`06_prop_asset_workflow.md`。\n"
            write_main_workflows(root, {"05_environment_asset_workflow.md": body})
            self.assertEqual(validator.check_workflow_routing(root), [])


class BatchDeliveryTests(unittest.TestCase):
    """Batched asset delivery: one owner for the definition, one for the confirmation semantics."""

    def _fixture(self, root: Path, overrides: dict[str, str] | None = None) -> None:
        overrides = overrides or {}
        relatives = set(validator.BATCH_DELIVERY_CONSUMERS)
        relatives |= set(validator.BATCH_DELIVERY_NON_OWNERS)
        relatives |= set(validator.CONFIRMATION_NON_OWNERS)
        relatives.add(validator.BATCH_DELIVERY_OWNER)
        relatives.add(validator.CONFIRMATION_OWNER)
        for relative in relatives:
            text = overrides.get(relative)
            if text is None:
                if relative == validator.BATCH_DELIVERY_OWNER:
                    text = validator.BATCH_DELIVERY_SECTION + "\n"
                elif relative == validator.CONFIRMATION_OWNER:
                    text = validator.CONFIRMATION_SECTION + "\n"
                else:
                    text = "Asset Batch Delivery\n"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def test_fixture_is_clean_before_mutating(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root)
            self.assertEqual(validator.check_batch_delivery_ownership(root), [])

    def test_missing_owner_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {validator.BATCH_DELIVERY_OWNER: "no section here\n"})
            self.assertIn(
                f"{validator.BATCH_DELIVERY_OWNER} must own the "
                f"{validator.BATCH_DELIVERY_SECTION} section",
                validator.check_batch_delivery_ownership(root),
            )

    def test_consumer_without_routing_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = "workflows/05_environment_asset_workflow.md"
            self._fixture(root, {target: "no batch routing here\n"})
            self.assertIn(
                f"batch delivery must route to its owner: {target}",
                validator.check_batch_delivery_ownership(root),
            )

    def test_second_owner_of_the_batch_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = "workflows/04_character_asset_workflow.md"
            self._fixture(
                root,
                {target: "Asset Batch Delivery\n" + validator.BATCH_DELIVERY_SECTION + "\n"},
            )
            self.assertIn(
                f"Asset Batch Delivery must not be re-owned: {target}",
                validator.check_batch_delivery_ownership(root),
            )

    def test_reowned_confirmation_semantics_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {"rules/02_asset_rules.md": validator.CONFIRMATION_SECTION + "\n"})
            self.assertIn(
                "confirmation semantics must stay with their owner: rules/02_asset_rules.md",
                validator.check_batch_delivery_ownership(root),
            )

    def test_active_skill_splits_batch_definition_from_confirmation(self) -> None:
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        progression = (ROOT / "rules/progression_rules.md").read_text(encoding="utf-8-sig")
        self.assertIn(validator.BATCH_DELIVERY_SECTION, rules)
        self.assertIn(validator.CONFIRMATION_SECTION, progression)
        self.assertNotIn(validator.CONFIRMATION_SECTION, rules)
        self.assertIn("Prompt Draft不得触发图片生成", rules)
        self.assertIn("未经批次展示的Candidate不得因用户沉默", rules)

    def test_asset_workflows_and_templates_carry_the_batch_envelope(self) -> None:
        for relative in (
            "workflows/04_character_asset_workflow.md",
            "workflows/05_environment_asset_workflow.md",
            "workflows/06_prop_asset_workflow.md",
            "workflows/15_fx_asset_workflow.md",
        ):
            self.assertIn("分批交付", (ROOT / relative).read_text(encoding="utf-8-sig"), relative)
        for relative in (
            "templates/04_character_asset_prompt.md",
            "templates/05_environment_asset_prompt.md",
            "templates/06_prop_asset_prompt.md",
        ):
            self.assertIn(
                "### Asset Batch Envelope",
                (ROOT / relative).read_text(encoding="utf-8-sig"),
                relative,
            )


class DeliveryModeTests(unittest.TestCase):
    """Image Delivery Mode: one owner for the mode, capability-based routing everywhere else."""

    def _fixture(self, root: Path, overrides: dict[str, str] | None = None) -> None:
        overrides = overrides or {}
        relatives = {relative for relative, _ in validator.DELIVERY_MODE_CONSUMERS}
        relatives |= set(validator.DELIVERY_MODE_NON_OWNERS)
        relatives.add(validator.DELIVERY_MODE_OWNER)
        for relative in relatives:
            text = overrides.get(relative)
            if text is None:
                markers = [
                    marker
                    for consumer, marker in validator.DELIVERY_MODE_CONSUMERS
                    if consumer == relative
                ]
                if relative == validator.DELIVERY_MODE_OWNER:
                    text = validator.DELIVERY_MODE_SECTION + "\n"
                elif markers:
                    text = "\n".join(markers) + "\n"
                else:
                    text = "unrelated content\n"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def test_fixture_is_clean_before_mutating(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root)
            self.assertEqual(validator.check_delivery_mode_ownership(root), [])

    def test_missing_owner_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {validator.DELIVERY_MODE_OWNER: "no mode section\n"})
            self.assertIn(
                f"{validator.DELIVERY_MODE_OWNER} must own the "
                f"{validator.DELIVERY_MODE_SECTION} section",
                validator.check_delivery_mode_ownership(root),
            )

    def test_consumer_without_routing_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = "core/runtime-state.md"
            self._fixture(root, {target: "no delivery mode view\n"})
            self.assertIn(
                f"image delivery mode must route to its owner: {target}",
                validator.check_delivery_mode_ownership(root),
            )

    def test_second_owner_of_the_mode_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = "rules/02_asset_rules.md"
            self._fixture(
                root,
                {target: "Image Delivery Mode\n" + validator.DELIVERY_MODE_SECTION + "\n"},
            )
            self.assertIn(
                f"Image Delivery Mode must not be re-owned: {target}",
                validator.check_delivery_mode_ownership(root),
            )

    def test_active_skill_routes_the_mode_from_production_setup_to_batch(self) -> None:
        mode = (ROOT / "modules/image-model-selection.md").read_text(encoding="utf-8-sig")
        script = (ROOT / "workflows/02_script_analysis_workflow.md").read_text(encoding="utf-8-sig")
        setup = (ROOT / "workflows/01_project_setup_workflow.md").read_text(encoding="utf-8-sig")
        state = (ROOT / "references/project_state_contract.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        self.assertIn("`AUTO`（默认）", mode)
        self.assertIn("`DIRECT_IMAGE`", mode)
        self.assertIn("`PROMPT_ONLY`", mode)
        self.assertIn("不得用历史会话、其他平台或上一次运行的能力推断本轮环境", mode)
        self.assertIn("Image Delivery Mode", script)
        self.assertNotIn("Image Delivery Mode", setup)
        self.assertIn("Image Delivery Mode: AUTO / DIRECT_IMAGE / PROMPT_ONLY", state)
        self.assertIn("`Automation Policy: FAST`或`Image Delivery Mode: DIRECT_IMAGE`", rules)
        self.assertIn("不得伪造生成结果", rules)


class R71CharacterSheetNeutralityTests(unittest.TestCase):
    """正式角色资产设定图的五区结构，以及资产参考画面中性化的单一 owner。"""

    def test_character_sheet_is_five_panels_with_a_neutral_front_panel(self) -> None:
        template = (ROOT / "templates/04_character_asset_prompt.md").read_text(encoding="utf-8-sig")
        workflow = (ROOT / "workflows/04_character_asset_workflow.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("五区域角色设定图", template)
        self.assertIn("**正面区**", template)
        self.assertIn("共用同一人物尺度", template)
        self.assertIn("面部唯一来源", template)
        self.assertIn("发落的权威载体", template)
        self.assertIn("可执行的渲染锚", template)
        self.assertIn("Expression Sheet Prompt", template)
        self.assertIn("不得把正面区缺少头部与头发判定为出图失败并补齐", template)
        self.assertNotIn("四分区", template)
        self.assertNotIn("四个区域", template)
        self.assertIn("`templates/04_character_asset_prompt.md`为唯一权威", workflow)
        self.assertIn("不是出图遗漏", guide)

    def test_asset_form_is_not_restated_outside_its_owner(self) -> None:
        """资产的区域形态只在 templates/04 定义；流程层与规则层只允许指针，不得复述形态。"""
        forbidden = ("上排三区", "下排双", "上排三个等宽", "下排两个更大", "五区角色资产图（")
        checkers = (
            "workflows/04_character_asset_workflow.md",
            "workflows/03_asset_discovery_workflow.md",
            "rules/02_asset_rules.md",
        )
        for rel in checkers:
            text = (ROOT / rel).read_text(encoding="utf-8-sig")
            for token in forbidden:
                self.assertNotIn(token, text, f"{rel} 复述了资产形态：{token}")
        owner = (ROOT / "templates/04_character_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("**上排三个等宽等高的全身区**", owner)
        self.assertIn("**下排两个更大的头肩特写区**", owner)

    def test_adapter_templates_track_the_owner_form(self) -> None:
        """编译层（Midjourney / GPT Image）必须与 owner 的五区形态同步，不得回退到四区旧形态。"""
        stale = ("四个区域", "四区写成", "头肩特写区和一个", "三视图 + 面部特写")
        for rel in ("templates/14_midjourney_asset_prompt.md",
                    "templates/24_gpt_image_asset_prompt.md"):
            text = (ROOT / rel).read_text(encoding="utf-8-sig")
            self.assertIn("上排三个", text, f"{rel} 未同步五区上排")
            self.assertIn("下排两个", text, f"{rel} 未同步五区下排")
            for token in stale:
                self.assertNotIn(token, text, f"{rel} 残留旧形态：{token}")

    def test_three_view_terminology_is_retired(self) -> None:
        """流程是 外观参考图 -> 正式角色资产图；「三视图」不再是本Skill的产物，全库不得再引用。"""
        skip_dirs = {"tmp", ".workbuddy", ".git"}
        offenders = []
        for path in sorted(ROOT.rglob("*.md")):
            rel = path.relative_to(ROOT)
            if set(rel.parts) & skip_dirs or path.suffix == ".backup":
                continue
            if path.name.endswith(".backup"):
                continue
            if "三视图" in path.read_text(encoding="utf-8-sig", errors="ignore"):
                offenders.append(str(rel))
        self.assertEqual(offenders, [], f"残留「三视图」旧称：{offenders}")

    def test_neutrality_reaches_both_compile_layer_templates(self) -> None:
        """中性化必须抵达两个编译层模板：它们是最终Prompt正文 owner，规则到不了就等于没写。

        同时确认两模板都把 Environment 排除在中性化之外，避免把场景身份也中性化掉。
        """
        for rel in ("templates/14_midjourney_asset_prompt.md",
                    "templates/24_gpt_image_asset_prompt.md"):
            text = (ROOT / rel).read_text(encoding="utf-8-sig")
            self.assertIn("## Background And Lighting By Asset Category", text, f"{rel} 缺类别分流节")
            self.assertIn("Reference Neutrality", text, f"{rel} 未指向判据 owner")
            self.assertIn("必须中性化", text, f"{rel} 未声明 CHAR/PROP 需中性化")
            self.assertIn("不得中性化", text, f"{rel} 未排除 Environment")
            self.assertIn("均匀柔和", text, f"{rel} 未给出可执行光线表述")
            self.assertIn("环境化", text, f"{rel} 未声明否定表述须环境化")
        # 判据本体仍只有 rules/02 一个 owner，编译层不得复制其完整正文
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        self.assertEqual(rules.count("### Reference Neutrality｜参考画面中性化"), 1)
        for rel in ("templates/14_midjourney_asset_prompt.md",
                    "templates/24_gpt_image_asset_prompt.md"):
            text = (ROOT / rel).read_text(encoding="utf-8-sig")
            self.assertNotIn("### Reference Neutrality｜参考画面中性化", text)

    def test_neutrality_keywords_stay_in_sync_across_layers(self) -> None:
        """编译层投影了判据要点，存在漂移风险：判据被改写而编译层未同步时必须报警。

        这里只做要点级同步检查，不要求措辞一致；命中失败即提示人工复核两处是否需要一起改。
        """
        keywords = ("均匀柔和", "中性单色", "环境化")
        layers = ("rules/02_asset_rules.md",
                  "templates/14_midjourney_asset_prompt.md",
                  "templates/24_gpt_image_asset_prompt.md")
        for rel in layers:
            text = (ROOT / rel).read_text(encoding="utf-8-sig")
            for kw in keywords:
                self.assertIn(kw, text, f"{rel} 缺失中性化要点「{kw}」——判据与编译层可能已漂移")

    def test_reference_neutrality_is_single_owner_and_environment_exempt(self) -> None:
        asset_rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        lock = (ROOT / "references/asset_lock_contract.md").read_text(encoding="utf-8-sig")
        scenarios = regression_corpus()
        heading = "### Reference Neutrality｜参考画面中性化"
        self.assertEqual(asset_rules.count(heading), 1)
        self.assertIn("**不适用于`Environment`资产**", asset_rules)
        self.assertIn("否定表述必须环境化", asset_rules)
        self.assertIn("没有墙、没有设备、没有地面", asset_rules)
        self.assertIn("发落分布", lock)
        self.assertIn("禁止给正面区补画头部或头发", scenarios)

    def test_five_panel_sheet_is_scoped_to_light_generated_media(self) -> None:
        """五区结构只适用于画面由光生成的媒介；2D 绘制媒介被明确排除。"""
        template = (ROOT / "templates/04_character_asset_prompt.md").read_text(encoding="utf-8-sig")
        profiles = (ROOT / "knowledge/medium_profiles.md").read_text(encoding="utf-8-sig")
        self.assertIn("**媒介适用条件**", template)
        self.assertIn("`live_action` / `3d_animation`", template)
        self.assertIn("媒介为`2d_anime`时**不适用**", template)
        self.assertIn("不得套用面部单源逻辑", template)
        self.assertIn("资产形态也随媒介分化", profiles)
        self.assertIn("`2d_anime` **不套用**该结构", profiles)
        self.assertIn("本文件只声明适用档位", profiles)


class GptImageNamingTests(unittest.TestCase):
    """图像模型名已改用 GPT Image：文件与引用须同步，且旧名不得回潮。"""

    # 拆分书写，避免本文件自身被自己的检查模式命中（自指）。
    LEGACY_TOKENS = (
        "Built" + "-in Image",
        "内置" + "Image",
        "内置" + "图像",
        "内置" + "图片",
        "built" + "-in-image",
        "24_" + "builtin",
        "builtin" + "_image",
    )

    LEGACY_ADAPTER = "adapters/built" + "-in-image.md"
    LEGACY_TEMPLATE = "templates/24_" + "builtin" + "_image_asset_prompt.md"

    def test_legacy_model_name_is_fully_retired(self) -> None:
        skip_dirs = {"tmp", ".workbuddy", ".git"}
        offenders = []
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT)
            if set(rel.parts) & skip_dirs or ".backup" in path.name:
                continue
            if path.suffix not in {".md", ".py", ".json", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
            for token in self.LEGACY_TOKENS:
                if token in text:
                    offenders.append(f"{rel} :: {token}")
        self.assertEqual(offenders, [], f"旧模型名残留：{offenders}")

    def test_adapter_and_template_are_renamed_and_linked(self) -> None:
        self.assertTrue((ROOT / "adapters/gpt-image.md").exists())
        self.assertTrue((ROOT / "templates/24_gpt_image_asset_prompt.md").exists())
        self.assertFalse((ROOT / self.LEGACY_ADAPTER).exists())
        self.assertFalse((ROOT / self.LEGACY_TEMPLATE).exists())
        adapter = (ROOT / "adapters/gpt-image.md").read_text(encoding="utf-8-sig")
        template = (ROOT / "templates/24_gpt_image_asset_prompt.md").read_text(encoding="utf-8-sig")
        self.assertIn("prompt_output_template: templates/24_gpt_image_asset_prompt.md", adapter)
        self.assertIn("## GPT Image Prompt Package", template)
        self.assertIn("`adapters/gpt-image.md`", template)

    def test_verified_capability_boundary_is_recorded(self) -> None:
        """GPT Image 的分辨率能力随版本分化；16:9 与 2K/4K 的可行性必须可从 Skill 内查到。"""
        adapter = (ROOT / "adapters/gpt-image.md").read_text(encoding="utf-8-sig")
        self.assertIn("## Verified Capability Boundary", adapter)
        self.assertIn("gpt-image-2", adapter)
        self.assertIn("3840", adapter)
        self.assertIn("做不了16:9", adapter)
        self.assertIn("2026-04-21", adapter)

    def test_delivery_route_enum_keeps_its_own_name(self) -> None:
        """`Built-in Candidate Generation` 是 Image Delivery Route 枚举，不是模型名，不随改名变动。"""
        state = (ROOT / "references/project_state_contract.md").read_text(encoding="utf-8-sig")
        self.assertIn("Built-in Candidate Generation", state)
        self.assertIn("GPT Image", state)


class R73RouteMapEntryAndGuardScopeTests(unittest.TestCase):
    """Two things the r73 change made explicit: the route owner states an entry boundary
    for every stage it routes, and the routing guard's writeback rule is a name guard,
    not a presence requirement."""

    def test_route_map_declares_required_boundary_for_every_main_state(self) -> None:
        """STATE-03 was the only stage whose entry had to be reconstructed from a
        neighbour's Next route; the route owner now states all ten directly."""
        text = (ROOT / "workflows/workflow_map.md").read_text(encoding="utf-8-sig")
        sections = {}
        current = None
        for line in text.splitlines():
            if line.startswith("### STATE-"):
                current = line[len("### "):].split()[0]
                sections[current] = []
            elif current is not None:
                sections[current].append(line)
        states = {state for _, state in validator.MAIN_WORKFLOWS}
        self.assertEqual(
            states, set(sections), "route map STATE sections drifted from MAIN_WORKFLOWS"
        )
        for state in sorted(sections):
            self.assertIn(
                "- Required boundary：",
                "\n".join(sections[state]),
                f"{state} 缺 Required boundary：入口边界只能由路由唯一 owner 给出",
            )

    def test_writeback_rule_is_a_name_guard_not_a_presence_requirement(self) -> None:
        """A full set of main workflows carrying no writeback block passes outright.
        If this ever fails, the guard grew a presence requirement and the Routing
        Integrity Check sentence in the protocol has to be widened with it."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_main_workflows(root)
            self.assertEqual(validator.check_workflow_routing(root), [])


class R73ReadScopeIndexTests(unittest.TestCase):
    """`# Read Scope` is how a hub file stays readable without being read whole.
    An index that points at a section which no longer exists is a broken read path,
    so it is guarded exactly like a dangling file reference."""

    HUB_FILES = (
        "workflows/workflow_map.md",
        "references/project_state_contract.md",
        "knowledge/director_decision_layer.md",
        "knowledge/screenplay_development.md",
        "knowledge/clip_preflight_check.md",
        "knowledge/reference_budget.md",
        "references/asset_lock_contract.md",
        "knowledge/spatial_blocking_layer.md",
        "knowledge/medium_profiles.md",
        "rules/automation_mode.md",
        "rules/02_asset_rules.md",
        "rules/04_consistency_rules.md",
        "rules/progression_rules.md",
        "knowledge/camera_language/camera_movement/selection_matrix.md",
        "knowledge/environment_multi_view_reconstruction.md",
        "references/project_workspace.md",
    )

    def test_every_read_scope_names_only_existing_sections(self) -> None:
        self.assertEqual(validator.check_read_scope_sections(ROOT), [])

    def test_the_reused_hub_files_all_declare_a_read_scope(self) -> None:
        """These ten are each reused by three or more stages; every one of them has to
        stay indexed, otherwise the read cost multiplies by the stage count again."""
        for relative in self.HUB_FILES:
            with self.subTest(hub=relative):
                text = (ROOT / relative).read_text(encoding="utf-8-sig")
                self.assertIsNotNone(
                    validator.READ_SCOPE_HEADING_RE.search(text),
                    f"{relative} 缺 `# Read Scope`",
                )

    def test_read_scope_pointing_at_a_missing_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "hub.md").write_text(
                "# Hub\n\n# Read Scope\n\n| 事项 | 只读 |\n|---|---|\n"
                "| 路由 | `## Main Routing` |\n\n---\n\n## Main Routing\n",
                encoding="utf-8",
            )
            self.assertEqual(validator.check_read_scope_sections(root), [])
            (root / "hub.md").write_text(
                "# Hub\n\n# Read Scope\n\n| 事项 | 只读 |\n|---|---|\n"
                "| 路由 | `## Renamed Section` |\n\n---\n\n## Main Routing\n",
                encoding="utf-8",
            )
            self.assertIn(
                "Read Scope points at a missing section: ## Renamed Section (in hub.md)",
                validator.check_read_scope_sections(root),
            )


    def test_read_budget_carries_a_project_scope_gate(self) -> None:
        """条件性资源在条件不成立时不得读取——这是最大的一项读取节省，所以它必须
        是一条可被指认的规则，而不是散落在各 Workflow 里的措辞。"""
        loading = (ROOT / "rules/resource_loading.md").read_text(encoding="utf-8-sig")
        self.assertIn("### Project Scope Gate｜项目范围门", loading)
        for domain in (
            "knowledge/fx/",
            "knowledge/sound_language/",
            "knowledge/sequence/",
            "knowledge/transitions/",
            "knowledge/performance/",
            "knowledge/visual_styles/",
            "knowledge/environment_multi_view_reconstruction.md",
            "rules/automation_mode.md",
            "rules/runtime_reload.md",
        ):
            with self.subTest(domain=domain):
                self.assertIn(domain, loading)
        self.assertIn("不确定即读", loading)


    def test_shipped_text_files_use_lf(self) -> None:
        """CR 不承载规则却按字节计费，而且混合换行符会把一处单行改动放大成整文件
        diff（实测 30 行真改动显示成 2,600 行）。两者都是纯损耗。"""
        self.assertEqual(validator.check_line_endings(ROOT), [])


class R73EvidenceCredibilityDimensionTests(unittest.TestCase):
    """维护层第 16 项：用来判断改动是否成立的**证据本身**必须可信。

    它被加进来，是因为本轮出现了四个“显然能省 token”的判断、三个被实测否掉，
    以及一个自身有缺陷却稳定报告“毫无变化”的测量工具。
    """

    def test_run_card_lists_sixteen_dimensions(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        for index in range(1, 17):
            with self.subTest(index=index):
                self.assertIn(f"\n| {index} | ", card)
        self.assertNotIn("\n| 17 | ", card)

    def test_summary_template_carries_the_new_line(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("Claim / Evidence Credibility: PASS / FIXED / WARN", card)

    def test_protocol_dimension_sixteen_names_its_four_checks(self) -> None:
        criteria = (ROOT / "references/maintenance_self_check_protocol.md").read_text(
            encoding="utf-8-sig"
        )
        self.assertIn("**Claim / Evidence Credibility Check**", criteria)
        for marker in ("宣称 vs 实现", "测量工具先自证", "权威来源核对", "实测与投影必须分开标注"):
            with self.subTest(marker=marker):
                self.assertIn(marker, criteria)
        self.assertIn("先普查它是否含有别处不存在的独有内容", criteria)

    def test_size_method_is_owned_once_and_routed_from_the_card(self) -> None:
        """体量改动的方法由 context_budget 拥有；短卡只路由，不复制步骤。"""
        budget = (ROOT / "references/context_budget.md").read_text(encoding="utf-8-sig")
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("## 体量改动的方法｜Measure Before You Move", budget)
        self.assertIn("Measure Before You Move", card)
        for section in ("### 读取足迹的两个口径", "### 已实测排除的方向", "### 仍然有效的方向"):
            with self.subTest(section=section):
                self.assertIn(section, budget)
        # 排除清单若不写明“要重新提出就得给新证据”，就会退化成一份没人看的清单
        self.assertIn("必须给出与上表不同的新证据", budget)
        self.assertIn("不得混用", budget)


PACKAGE_BUILDER_SPEC = importlib.util.spec_from_file_location(
    "asset_package_builder", ROOT / "scripts" / "build_asset_package.py"
)
asset_package_builder = importlib.util.module_from_spec(PACKAGE_BUILDER_SPEC)
assert PACKAGE_BUILDER_SPEC and PACKAGE_BUILDER_SPEC.loader
PACKAGE_BUILDER_SPEC.loader.exec_module(asset_package_builder)


class R76DeliveryPackageTests(unittest.TestCase):
    """生产交付包：形态只有一个 owner，命名与“Prompt ↔ 包内文件”一一对应可机械核验。"""

    def _fixture(self, root: Path, overrides: dict[str, str] | None = None) -> None:
        overrides = overrides or {}
        relatives = {relative for relative, _ in validator.PACKAGE_CONSUMERS}
        relatives |= set(validator.PACKAGE_NON_OWNERS)
        relatives |= {relative for relative, _ in validator.REFERENCE_OWNER_MARKERS}
        for relative in relatives:
            text = overrides.get(relative)
            if text is None:
                markers = [
                    marker
                    for owner, marker in validator.REFERENCE_OWNER_MARKERS
                    if owner == relative
                ]
                markers += [
                    marker
                    for consumer, marker in validator.PACKAGE_CONSUMERS
                    if consumer == relative
                ]
                text = "\n".join(markers) + "\n" if markers else "unrelated content\n"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def test_fixture_is_clean_before_mutating(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root)
            self.assertEqual(validator.check_reference_ownership(root), [])

    def test_missing_owner_marker_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {"references/asset_package.md": "no naming contract here\n"})
            self.assertIn(
                "references/asset_package.md is missing the delivery package marker: "
                "## Asset Image Naming",
                validator.check_reference_ownership(root),
            )

    def test_consumer_without_routing_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {"config.md": "unrelated content\n"})
            self.assertIn(
                "delivery package must route to its owner: config.md",
                validator.check_reference_ownership(root),
            )

    def test_second_copy_of_the_naming_shape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = "rules/02_asset_rules.md"
            self._fixture(
                root,
                {target: "references/asset_package.md\n<Asset ID>｜<Purpose>.ext\n"},
            )
            self.assertIn(
                f"asset image naming shape must stay with its owner: {target}",
                validator.check_reference_ownership(root),
            )

    def test_active_skill_routes_the_package_to_one_owner(self) -> None:
        owner = (ROOT / "references/asset_package.md").read_text(encoding="utf-8-sig")
        rules = (ROOT / "rules/02_asset_rules.md").read_text(encoding="utf-8-sig")
        gate = (ROOT / "rules/completion_gate.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        self.assertIn("参考资产", owner)
        self.assertIn("一一对应", owner)
        self.assertIn("包内**不含**最终视频Prompt", owner)
        self.assertIn("references/asset_package.md", rules)
        self.assertIn("命名在该时点锁定", rules)
        self.assertIn("生产交付包由`references/asset_package.md`拥有", gate)
        self.assertIn("生产交付包", guide)
        # 命名形态不得被其他文件复述成第二份规范
        self.assertNotIn("<Asset ID>｜<Purpose>", rules)
        self.assertNotIn("<Asset ID>｜<Purpose>", gate)
        # 该能力必须有覆盖正反例的回归场景，否则它只是“写了一条规定”
        scenarios = regression_corpus()
        self.assertIn("## R36 Production Delivery Package Regression", scenarios)
        for marker in ("R36-A", "R36-B", "R36-C", "R36-D", "R36-E"):
            with self.subTest(marker=marker):
                self.assertIn(marker, scenarios)

    def test_access_precondition_is_owned_once_and_routed(self) -> None:
        """打包有环境前提：只有具备真实文件访问能力的 Work / Codex 本地环境才产包与zip。"""
        owner = (ROOT / "references/asset_package.md").read_text(encoding="utf-8-sig")
        gate = (ROOT / "rules/completion_gate.md").read_text(encoding="utf-8-sig")
        guide = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8-sig")
        builder = (ROOT / "scripts/build_asset_package.py").read_text(encoding="utf-8-sig")
        self.assertIn("## Access Precondition", owner)
        self.assertIn("普通 Chat / Portable 模式", owner)
        self.assertIn("判据是能力，不是平台名", owner)
        self.assertIn("不产zip、不产包目录", owner)
        self.assertIn("未打包", owner)
        # 降级阶梯必须包含“不能读”的最弱一档，且永远不许伪造
        self.assertIn("只交付命名映射表", owner)
        self.assertIn("降级不是`BLOCKED`", owner)
        self.assertIn("只在具备真实文件访问能力的Work / Codex本地环境执行", gate)
        self.assertIn("普通Chat / Portable模式不产zip", gate)
        self.assertIn("普通 Chat", guide)
        # 前提形态不得被第二处复述成完整阶梯
        self.assertNotIn("## Access Precondition", gate)
        self.assertIn("precondition", builder.lower())


class R76PackageBuilderTests(unittest.TestCase):
    """可选构建器必须与资产包规范互操作：命名、清单、zip 与对应性检查。"""

    PIXEL = bytes.fromhex(
        "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489"
        "0000000a49444154789c6360000002000100ffff03000006000557bfabd4000000"
        "0049454e44ae426082"
    )

    REGISTRY = """# Asset Registry

## CHAR-001 林夏

Asset ID: CHAR-001
Asset Tier: Core
Status: Active
Active Version: v001
Canonical References: CHAR-001｜Identity.png（用途：Identity，绑定 v001）
Visual Production Status: Asset Confirmed
Confirmed Status: Yes
Approved By / Approval Basis: User Confirmed
Approved At: 2026-09-01

## ENV-002 雨夜街头

Asset ID: ENV-002
Asset Tier: Core
Status: Active
Active Version: v003
Canonical References: ENV-002｜Layout_ENV-01.png（用途：Layout，绑定 v003）
Visual Production Status: Asset Confirmed
Confirmed Status: Yes
Approved By / Approval Basis: Auto-accepted under FAST

## FX-004 雨幕

Asset ID: FX-004
Asset Tier: Not Applicable
Status: Active
Active Version: v001
Canonical References: FX-004｜FX Phase.png（用途：FX Phase，绑定 v001）
Visual Production Status: Asset Confirmed
Confirmed Status: Yes
Approved By / Approval Basis: User Confirmed

## PROP-777 未确认道具

Asset ID: PROP-777
Asset Tier: Core
Status: Candidate
Active Version: v001
Canonical References: PROP-777｜Material.png（用途：Material，绑定 v001）
Visual Production Status: Image Generated
Confirmed Status: No
"""

    PROMPT = """# CLIP-001｜雨夜重逢

参考资产：
- CHAR-001｜Identity.png｜锁定林夏身份
- ENV-002｜Layout_ENV-01.png｜锁定空间结构
- FX-004｜FX Phase.png｜锁定雨幕形态
"""

    def _project(self, root: Path) -> Path:
        project = root / "PROJECT-DEMO-001"
        (project / "assets").mkdir(parents=True)
        (project / "asset_registry.md").write_text(self.REGISTRY, encoding="utf-8", newline="\n")
        for name in ("CHAR-001｜Identity.png", "ENV-002｜Layout_ENV-01.png",
                     "FX-004｜FX Phase.png", "PROP-777｜Material.png"):
            (project / "assets" / name).write_bytes(self.PIXEL)
        # Present but never confirmed: it must be reported, not packaged.
        (project / "01_script_analysis_locked.md").write_text("# locked\n", encoding="utf-8", newline="\n")
        (project / "07_clip_production_plan.md").write_text(
            "# Clip Plan\n\nConfirmed Status: Yes\nApproved By / Approval Basis: User Confirmed\n",
            encoding="utf-8", newline="\n",
        )
        return project

    def _build(self, project: Path, prompt: Path | None = None) -> dict:
        return asset_package_builder.Builder(
            asset_package_builder.argparse.Namespace(
                project_root=str(project),
                registry=None,
                project_id=None,
                project_name="雨夜重逢",
                version="001",
                output=str(project.parent / "PROJECT-DEMO-001_packages" / "001"),
                no_zip=False,
                check_prompt=str(prompt) if prompt is not None else None,
            )
        ).run()

    def test_builder_stages_every_confirmed_asset_under_its_locked_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            project = self._project(Path(temp_dir))
            result = self._build(project)
            self.assertEqual(result["errors"], [], result["errors"])
            package = Path(str(result["package_root"]))
            for name in ("CHAR-001｜Identity.png", "ENV-002｜Layout_ENV-01.png", "FX-004｜FX Phase.png"):
                with self.subTest(name=name):
                    self.assertTrue((package / "02_assets").rglob(name).__next__().is_file())
            self.assertIn("CHAR-001｜Identity.png", (package / "02_assets/CHAR/_MANIFEST.md").read_text(encoding="utf-8"))
            self.assertIn("ENV-002｜Layout_ENV-01.png", (package / "02_assets/ENV/_MANIFEST.md").read_text(encoding="utf-8"))
            self.assertIn("FX-004｜FX Phase.png", (package / "02_assets/FX/_MANIFEST.md").read_text(encoding="utf-8"))
            manifest = (package / "00_MANIFEST.md").read_text(encoding="utf-8")
            self.assertIn("包内不含最终视频Prompt", manifest)
            self.assertTrue(Path(str(result["archive"])).is_file())

    def test_unconfirmed_work_is_reported_not_packaged(self) -> None:
        """用户认可的才进包：Registry里存在不等于可以打包。"""
        with tempfile.TemporaryDirectory() as temp_dir:
            project = self._project(Path(temp_dir))
            result = self._build(project)
            package = Path(str(result["package_root"]))
            packaged = sorted(path.name for path in (package / "02_assets").rglob("*.png"))
            # PROP-777 is present in the registry and on disk, but Confirmed Status: No.
            self.assertNotIn("PROP-777｜Material.png", packaged)
            self.assertTrue(
                any("PROP-777" in item and "未确认" in item
                    for item in result["excluded"]),
                result["excluded"],
            )
            # A file that exists in the project root without any confirmation record.
            self.assertTrue(
                any("01_script/01_script_analysis_locked.md" in item
                    and "缺确认记录" in item for item in result["excluded"]),
                result["excluded"],
            )
            index = (package / "00_INDEX.md").read_text(encoding="utf-8")
            self.assertIn("## 未确认／未打包", index)
            self.assertIn("PROP-777", index)
            self.assertFalse((package / "01_script/01_script_analysis_locked.md").exists())

    def test_admission_marks_fast_auto_acceptance_separately(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            project = self._project(Path(temp_dir))
            result = self._build(project)
            package = Path(str(result["package_root"]))
            manifest = (package / "00_MANIFEST.md").read_text(encoding="utf-8")
            env_manifest = (package / "02_assets/ENV/_MANIFEST.md").read_text(encoding="utf-8")
            self.assertIn("User Confirmed", manifest)
            self.assertIn("Auto-accepted under FAST", manifest)
            self.assertIn("Auto-accepted under FAST", env_manifest)

    def test_batch_confirmation_without_objection_is_admitted(self) -> None:
        """用户没提异议就是认可：已展示批次 + 未指出问题 = 确认，不需要“确认”措辞。"""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = self._project(root)
            registry = (project / "asset_registry.md").read_text(encoding="utf-8")
            registry = registry.replace(
                "Approved By / Approval Basis: User Confirmed",
                "Confirmation: Exception-Based Batch Confirmation — 用户未指出问题，按推进表达确认该批次",
            )
            (project / "asset_registry.md").write_text(registry, encoding="utf-8", newline="\n")
            result = self._build(project)
            self.assertEqual(result["errors"], [], result["errors"])
            package = Path(str(result["package_root"]))
            packaged = sorted(path.name for path in (package / "02_assets").rglob("*.png"))
            self.assertIn("CHAR-001｜Identity.png", packaged)
            self.assertIn("FX-004｜FX Phase.png", packaged)
            self.assertNotIn("PROP-777｜Material.png", packaged)
            manifest = (package / "00_MANIFEST.md").read_text(encoding="utf-8")
            self.assertIn("Confirmed (batch, no objection)", manifest)
            # The batch rule still needs the item to have been shown and confirmed.
            self.assertTrue(
                any("PROP-777" in item and "未确认" in item for item in result["excluded"]),
                result["excluded"],
            )

    def test_unconfirmed_clip_table_blocks_the_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            project = self._project(Path(temp_dir))
            (project / "07_clip_production_plan.md").write_text(
                "# Clip Plan\n\nConfirmed Status: No\n", encoding="utf-8", newline="\n"
            )
            result = self._build(project)
            self.assertTrue(
                any("package gate not met" in item and "06_clips" in item
                    for item in result["errors"]),
                result["errors"],
            )

    def test_prompt_correspondence_accepts_a_matching_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = self._project(root)
            prompt = root / "prompt.md"
            prompt.write_text(self.PROMPT, encoding="utf-8", newline="\n")
            result = self._build(project, prompt)
            self.assertEqual(result["errors"], [], result["errors"])
            # The fixture only contains script/clip sources, so the "no source file"
            # notes are correct behaviour; the correspondence check itself must pass.
            self.assertEqual(
                [item for item in result["warnings"] if "not referenced by this prompt" in item],
                [],
                result["warnings"],
            )

    def test_prompt_correspondence_rejects_an_unpackaged_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = self._project(root)
            prompt = root / "prompt.md"
            prompt.write_text(
                self.PROMPT + "- PROP-999｜Material.png｜不存在的文件\n",
                encoding="utf-8", newline="\n",
            )
            result = self._build(project, prompt)
            self.assertIn(
                "compiled prompt references a file that is not in the package: PROP-999｜Material.png",
                result["errors"],
            )

    def test_builder_blocks_an_off_convention_file_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = self._project(root)
            (project / "assets" / "CHAR-001｜identity_shot.png").write_bytes(self.PIXEL)
            (project / "asset_registry.md").write_text(
                self.REGISTRY.replace(
                    "Canonical References: CHAR-001｜Identity.png（用途：Identity，绑定 v001）",
                    "Canonical References: CHAR-001｜identity_shot.png（用途：Identity，绑定 v001）",
                ),
                encoding="utf-8", newline="\n",
            )
            result = self._build(project)
            self.assertTrue(
                any("does not follow the naming contract" in item for item in result["errors"]),
                result["errors"],
            )

    def test_builder_blocks_a_missing_reference_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = self._project(root)
            (project / "assets" / "ENV-002｜Layout_ENV-01.png").unlink()
            result = self._build(project)
            self.assertTrue(
                any("no readable file in the project root" in item for item in result["errors"]),
                result["errors"],
            )


class R77NoProjectRegistryTests(unittest.TestCase):
    """Skill 是工具，不是项目仓库：登记能力被移除后，守卫必须真的能拦住它复活。"""

    def _fixture(self, root: Path, overrides: dict[str, str] | None = None) -> None:
        overrides = overrides or {}
        for relative in validator.NO_PROJECT_REGISTRY_SOURCES:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(overrides.get(relative, "# unrelated content\n"), encoding="utf-8")

    def test_fixture_is_clean_before_mutating(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root)
            self.assertEqual(validator.check_no_project_registry(root), [])

    def test_reintroduced_registry_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(root, {"index.md": "├── project_registry.json\n"})
            self.assertIn(
                "project registration must stay removed: project_registry (in index.md)",
                validator.check_no_project_registry(root),
            )

    def test_reintroduced_init_command_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(
                root,
                {"references/project_workspace.md": "validate_sd_film.py init --registry x.json\n"},
            )
            self.assertIn(
                "project registration must stay removed: `--registry` command "
                "(in references/project_workspace.md)",
                validator.check_no_project_registry(root),
            )

    def test_reintroduced_registration_table_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._fixture(
                root,
                {"rules/state_source.md": "`project_registry.json` 只负责登记项目。\n"},
            )
            errors = validator.check_no_project_registry(root)
            self.assertTrue(any("project_registry" in item for item in errors), errors)

    def test_active_skill_states_the_removal_and_keeps_no_registry_file(self) -> None:
        workspace = (ROOT / "references/project_workspace.md").read_text(encoding="utf-8-sig")
        source = (ROOT / "rules/state_source.md").read_text(encoding="utf-8-sig")
        self.assertIn("本Skill不维护项目登记表", workspace)
        self.assertIn("本Skill不维护项目登记表", source)
        self.assertIn("Skill安装目录只保存通用定义，不是项目仓库", workspace)
        self.assertFalse((ROOT / "project_registry.json").exists())
        self.assertEqual(validator.check_no_project_registry(ROOT), [])
        # 该移除必须有正反例回归场景，否则下一个人只会看到“文件没了”
        scenarios = regression_corpus()
        self.assertIn("## R37 No Project Registration Regression", scenarios)
        for marker in ("R37-A", "R37-B"):
            with self.subTest(marker=marker):
                self.assertIn(marker, scenarios)


class R78ReachabilityTests(unittest.TestCase):
    """反向守卫：发布出去的内容必须能被读到，或者自己声明为什么不参与生产。

    Reference Integrity 只查"指向不存在的文件"。这个查另一半：
    文件存在但没有任何读取路径——`project_registry` 和 13 个史前概览就是这么攒出来的。
    """

    def test_active_skill_has_no_unreachable_file(self) -> None:
        self.assertEqual(validator.check_reachability(ROOT), [])

    def test_planted_orphan_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "knowledge").mkdir()
            (root / "SKILL.md").write_text("# entry\n", encoding="utf-8")
            (root / "config.md").write_text("# config\n", encoding="utf-8")
            (root / "knowledge" / "orphan.md").write_text("# orphan\n", encoding="utf-8")
            errors = validator.check_reachability(root)
            self.assertTrue(
                any("knowledge/orphan.md" in item for item in errors), errors
            )

    def test_declared_maintenance_file_is_exempt(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "knowledge").mkdir()
            (root / "SKILL.md").write_text("# entry\n", encoding="utf-8")
            (root / "config.md").write_text("# config\n", encoding="utf-8")
            (root / "knowledge" / "declared.md").write_text(
                f"# declared\n\n> {validator.MAINTENANCE_MARKER}：只在修改本Skill时读取，不参与影视生产。\n",
                encoding="utf-8",
            )
            self.assertEqual(validator.check_reachability(root), [])

    def test_reachable_file_through_a_reference_is_not_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "rules").mkdir()
            (root / "SKILL.md").write_text(
                "# entry\n\n见 `rules/pointed_at.md`。\n", encoding="utf-8"
            )
            (root / "config.md").write_text("# config\n", encoding="utf-8")
            (root / "rules" / "pointed_at.md").write_text("# target\n", encoding="utf-8")
            self.assertEqual(validator.check_reachability(root), [])

    def test_active_skill_declares_the_maintenance_layer(self) -> None:
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        protocol = (ROOT / "references/maintenance_self_check_protocol.md").read_text(
            encoding="utf-8-sig"
        )
        self.assertIn("只在修改本Skill时读取", card)
        self.assertIn("check_reachability", protocol)
        # 运行时资源不得被标成维护层
        for relative in (
            "references/artifact_revision_contract.md",
            "references/skill_experience_contract.md",
            "references/professional_detailed_shot_script_example.md",
        ):
            with self.subTest(relative=relative):
                text = (ROOT / relative).read_text(encoding="utf-8-sig")
                self.assertNotIn(validator.MAINTENANCE_MARKER, text)
                self.assertIn("运行时资源", text)

    def test_run_card_carries_the_orphan_check_as_a_required_item(self) -> None:
        """死文件检查是维护层的固定基线，不是"跑脚本时顺带"。

        只有正向检查时，内容会安静地攒成没人读的历史遗留——本Skill 已发生过两次。
        """
        card = (ROOT / "references/maintenance_self_check.md").read_text(encoding="utf-8-sig")
        self.assertIn("| 孤儿内容与不可达文件 |", card)
        self.assertIn("check_reachability", card)
        self.assertIn("豁免清单必须可见", card)
        self.assertIn("已经发生过两次", card)
        protocol = (ROOT / "references/maintenance_self_check_protocol.md").read_text(
            encoding="utf-8-sig"
        )
        self.assertIn("孤儿检查同样适用于文件，且每次必做", protocol)

    def test_report_lists_orphans_and_their_exemptions(self) -> None:
        """报告要同时给出阻断清单与豁免清单：只看绿灯分不清跳过和漏掉。"""
        report = validator.build_report(ROOT)
        self.assertIn("unreachable (no read path)", report)
        self.assertIn("blocking when non-zero", report)
        self.assertIn("unreachable but declared exempt", report)
        self.assertIn("USER_GUIDE.md", report)
        self.assertEqual(validator.unreachable_shipped_files(ROOT), [])
        exempt = dict(validator.exempt_unreachable_files(ROOT))
        self.assertEqual(exempt.get("USER_GUIDE.md"), "non-runtime doc")

    def test_report_lists_a_planted_orphan(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "knowledge").mkdir()
            (root / "references").mkdir()
            (root / "SKILL.md").write_text("# entry\n", encoding="utf-8")
            (root / "config.md").write_text(
                "# config\n\n- Context Budget: `references/context_budget.md`\n",
                encoding="utf-8",
            )
            # build_report also reads the size ledger, so the fixture carries it.
            (root / "references" / "context_budget.md").write_text(
                "# Context Budget\n\n## Size Index\n\n"
                "| File | Class | Size (r60) | Read Entry | Review By |\n"
                "|---|---|---|---|---|\n",
                encoding="utf-8",
            )
            (root / "knowledge" / "dead.md").write_text("# dead\n", encoding="utf-8")
            self.assertEqual(validator.unreachable_shipped_files(root), ["knowledge/dead.md"])
            report = validator.build_report(root)
            self.assertIn("unreachable (no read path): 1", report)
            self.assertIn("knowledge/dead.md", report)

    def test_reference_guard_declares_its_blind_spot(self) -> None:
        """删文件后不能只信 validator：裸文件名引用不在它的射程内。

        r79 删除 8 个来源覆盖表时，正是一条反引号裸名引用靠人工 grep 才发现。
        """
        source = (ROOT / "scripts/validate_sd_film.py").read_text(encoding="utf-8-sig")
        protocol = (ROOT / "references/maintenance_self_check_protocol.md").read_text(
            encoding="utf-8-sig"
        )
        for marker in (
            "Declared reach",
            "deliberately out of scope",
            "grep the corpus for the name by hand",
            "shots/director_decision_notes.md",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, source)
        for marker in ("射程必须写清", "裸文件名", "必须自己全库grep一次文件名"):
            with self.subTest(marker=marker):
                self.assertIn(marker, protocol)
        # 删除后的覆盖表不得再被任何 index 按名字引用
        index_text = "".join(
            path.read_text(encoding="utf-8-sig") for path in (ROOT / "knowledge").rglob("index.md")
        )
        self.assertNotIn("image_source_coverage", index_text)
        self.assertNotIn("source_coverage.md", index_text)


if __name__ == "__main__":
    unittest.main()
