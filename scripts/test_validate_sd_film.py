from __future__ import annotations

import io
import argparse
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import validate_sd_film as validator


def run_quiet(function, *args) -> int:
    with redirect_stdout(io.StringIO()):
        return function(*args)


VALID_SOUND = "环境底声：室内空调低频底噪与轻微房间反射；同步前景声：呼吸、衣料Foley与脚步声跟随动作；声音尾部：房间底噪持续承接下一镜"


def valid_global_section(section: str) -> str:
    if section == "参考资产：":
        return "参考资产：CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。"
    return f"{section}有效内容"


def make_state08_global_sections(
    package_number: int,
    clip_number: int,
    shots: str,
    duration: str,
    *,
    title: str = "测试Clip",
    reference: str | None = None,
    first_frame: str | None = None,
    tail_use: str = "最终收束",
    include_voice: bool = False,
) -> str:
    previous_token = f"[G{package_number - 1:02d}尾帧]"
    if reference is None:
        reference = "CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。"
        if package_number > 1:
            reference += f"\n{previous_token}合法尾帧；用途：直接作为本段首帧；锁定空间、动作、道具、光色与摄影机边界。"
    if first_frame is None:
        if package_number == 1:
            handoff = "首段，无上一Clip尾帧；从已确认Scene初始状态建立。"
        else:
            handoff = f"Direct Start-Frame Handoff：{previous_token}直接继承为本段首帧。"
        first_frame = (
            f"上一Clip尾帧承接判定：{handoff}"
            "人物位于画面左侧、身体朝右并看向前方；摄影机从轴线同侧低机位起始；"
            "中景，主体保持左侧构图与清楚前中后景；环境为已确认室内场景；"
            "道具保持原状态；动作起始状态为静止；光线状态延续柔和侧光。"
        )
    sections = [
        f"# CLIP-{clip_number:03d}｜{title} Seedance视频提示词",
        f"时长：平台生成时长：{duration}秒",
        "画幅：16:9，横屏，真人写实",
        f"参考资产：{reference}",
        f"首帧参考：{first_frame}",
        (
            f"尾帧限制：保存为[G{package_number:02d}尾帧]：人物最终位置稳定、动作完成、视线与情绪清楚；"
            "摄影机最终机位、景别、构图和焦点稳定；道具最终状态明确；环境与光线最终状态连续；"
            "画面清楚可冻结、可继承。最后1秒不得开启新复杂动作或剧情事件。"
            f"\n下一段预计用途：{tail_use}"
        ),
        "主风格：电影级写实，自然光，克制表演",
        "人物一致性：CHAR-001身份、脸型、发型、服装和身体比例保持一致",
        "环境一致性：已确认环境结构、轴线、背景与光线方向保持一致",
    ]
    if include_voice:
        sections.append("音色特征：当前视频模型使用已授权的CHAR-001 Voice Reference；speaker映射为CHAR-001。")
    return "\n".join(sections)


def make_shot_fields(
    handoff: str = "Unresolved Handoff：本段末镜，无已知下一镜，形成最终收束。",
    sound: str = VALID_SOUND,
    start_state: str = "第一帧来源：从已确认Scene初始状态建立。",
    end_state: str = "主要动作完成后进入低动作稳定状态；主体清楚可读，可作为下一Clip接口。",
) -> str:
    values = {
        "景别：": "中景。",
        "镜头/机位：": "轴线同侧固定机位，焦点锁定人物。",
        "起始状态：": start_state,
        "画面描述：": "人物抬眼看向画面右侧，随后停稳。",
        "人物动作与情绪：": "呼吸平稳，视线移动后由平静转为警觉。",
        "空间关系：": "人物位于画面左侧朝右，摄影机保持轴线同侧。",
        "道具状态：": "本镜头无关键道具变化。",
        "台词：": "无。",
        "音效：": sound,
        "镜头结尾状态：": f"{end_state} {handoff}",
    }
    return "\n".join(f"{field}{values[field]}" for field in validator.SHOT_FIELDS)


def make_clip_detail_fields(source: str, duration: str, accounting: str, tail: str = "保存为[G01尾帧]") -> str:
    values = {
        "包含 Shot：": source,
        "目标时长：": duration,
        "时长核算：": accounting,
        "声音连续：": VALID_SOUND,
        "结尾帧限制：": tail,
        "尾帧用途判定：": "最终收束",
    }
    return "\n".join(f"- {field}{values.get(field, '有效内容')}" for field in validator.CLIP_DETAIL_FIELDS)


class ValidatorRegressionTests(unittest.TestCase):
    def test_portable_initialized_alias_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (Path(__file__).resolve().parents[1] / "portable_project_status.md").read_text(encoding="utf-8")
            path.write_text(canonical.replace("State Status：NOT_STARTED", "State Status：INITIALIZED"), encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_portable_ready_state_status_alias_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (Path(__file__).resolve().parents[1] / "portable_project_status.md").read_text(encoding="utf-8")
            path.write_text(canonical.replace("State Status：NOT_STARTED", "State Status：READY"), encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_custom_chat_portable_summary_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            path.write_text(
                """# SD Film Portable Project Status
## Portable State Metadata
State Source: Portable State
## Current State
Current State: STATE-00 Project Setup
## State Status
State Status: INITIALIZED
## Next Workflow
Next Workflow: Project Setup Workflow
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_portable_natural_language_next_workflow_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (Path(__file__).resolve().parents[1] / "portable_project_status.md").read_text(encoding="utf-8")
            path.write_text(
                canonical.replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：Project Setup Workflow"),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_state_source_prefers_readable_active_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            active = root / "project"
            active.mkdir()
            active_status = active / "project_status.md"
            portable = root / "portable_project_status.md"
            active_status.write_text("active", encoding="utf-8")
            portable.write_text("portable", encoding="utf-8")
            self.assertEqual(validator.resolve_state_source(active, portable), ("ACTIVE_PROJECT_ROOT", active_status))

    def test_state_source_falls_back_to_portable_when_root_is_unavailable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            portable = root / "portable_project_status.md"
            portable.write_text("portable", encoding="utf-8")
            self.assertEqual(validator.resolve_state_source(root / "missing", portable), ("PORTABLE", portable))

    def test_ordinary_chat_continues_from_portable_current_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            portable = root / "portable_project_status.md"
            canonical = (Path(__file__).resolve().parents[1] / "portable_project_status.md").read_text(encoding="utf-8")
            portable.write_text(
                canonical.replace("Current State：STATE-00", "Current State：STATE-05")
                .replace("State Status：NOT_STARTED", "State Status：COMPLETE")
                .replace("Script Status：Source Material", "Script Status：Production-Locked")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：09_shot_design_workflow.md"),
                encoding="utf-8",
            )
            mode, selected = validator.resolve_state_source(root / "missing", portable)
            self.assertEqual(mode, "PORTABLE")
            self.assertEqual(selected, portable)
            self.assertEqual(validator.extract_label(selected.read_text(encoding="utf-8"), "Current State"), "STATE-05")
            self.assertEqual(validator.extract_label(selected.read_text(encoding="utf-8"), "Next Workflow"), "09_shot_design_workflow.md")

    def test_portable_required_progression_fields_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (Path(__file__).resolve().parents[1] / "portable_project_status.md").read_text(encoding="utf-8")
            path.write_text(canonical.replace("- Completed States：None\n", ""), encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_state_source_initializes_state_00_when_both_are_unavailable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertEqual(
                validator.resolve_state_source(root / "missing", root / "missing-portable.md"),
                ("INITIALIZE_STATE_00", None),
            )

    def test_installed_portable_state_passes(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        self.assertEqual(
            run_quiet(validator.validate_portable_status, skill_root / "portable_project_status.md", True),
            0,
        )

    def test_novel_outline_reports_adaptation_need_before_short_form_adaptation(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        adapter = (skill_root / "knowledge" / "adaptation" / "short_form_drama_adapter.md").read_text(encoding="utf-8")
        self.assertIn("C — Source Material", workflow)
        self.assertIn("Optimization Opportunity Report → User Decision Gate", workflow)
        self.assertIn("不得生成Adaptation Draft", workflow)
        self.assertIn("用户已明确同意优化/改编", workflow)
        self.assertIn("Adaptation Target Detection", workflow)
        self.assertIn("短剧、竖屏剧情或1—3分钟剧情视频", workflow)
        self.assertIn("前3秒", adapter)
        self.assertIn("Hook → Setup → Escalation → Payoff → Next Hook", adapter)

        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (skill_root / "portable_project_status.md").read_text(encoding="utf-8")
            adaptation_state = (
                canonical.replace("Current State：STATE-00", "Current State：STATE-01")
                .replace("State Status：NOT_STARTED", "State Status：IN_PROGRESS")
                .replace("Script Status：Source Material", "Script Status：Adaptation Draft")
                .replace("Active Workflow：01_project_setup_workflow.md", "Active Workflow：02_script_analysis_workflow.md")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：02_script_analysis_workflow.md")
                .replace("Pending Decision：等待项目输入", "Pending Decision：继续Screenwriting Optimization")
            )
            path.write_text(adaptation_state, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 0)

            invalid_state_02 = adaptation_state.replace("Current State：STATE-01", "Current State：STATE-02")
            path.write_text(invalid_state_02, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_rough_script_stops_at_optimization_opportunity_report(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        template = (skill_root / "templates" / "02_script_analysis_prompt.md").read_text(encoding="utf-8")
        self.assertIn("Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate", workflow)
        self.assertIn("报告输出后必须停止", workflow)
        self.assertIn("不得输出任何改写后的剧本正文", workflow)
        self.assertIn("开场钩子", template)
        self.assertIn("场景/人物复杂度", template)
        self.assertIn("是否执行轻度优化？", template)

        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (skill_root / "portable_project_status.md").read_text(encoding="utf-8")
            report_state = (
                canonical.replace("Current State：STATE-00", "Current State：STATE-01")
                .replace("State Status：NOT_STARTED", "State Status：IN_PROGRESS")
                .replace("Active Workflow：01_project_setup_workflow.md", "Active Workflow：02_script_analysis_workflow.md")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：02_script_analysis_workflow.md")
                .replace("Pending Decision：等待项目输入", "Pending Decision：是否执行轻度优化")
            )
            path.write_text(report_state, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 0)

            invalid_state_02 = report_state.replace("Current State：STATE-01", "Current State：STATE-02")
            path.write_text(invalid_state_02, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_reject_optimization_locks_original_script(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        self.assertIn("拒绝优化或改编", workflow)
        self.assertIn("不把它自动改编成标准剧本", workflow)
        self.assertIn("将用户原始版本原样登记为`Script Status: Production-Locked`", workflow)

        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (skill_root / "portable_project_status.md").read_text(encoding="utf-8")
            locked_state = (
                canonical.replace("Current State：STATE-00", "Current State：STATE-01")
                .replace("State Status：NOT_STARTED", "State Status：COMPLETE")
                .replace("Script Status：Source Material", "Script Status：Production-Locked")
                .replace("Active Workflow：01_project_setup_workflow.md", "Active Workflow：02_script_analysis_workflow.md")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：03_asset_discovery_workflow.md")
                .replace("Last Successful Checkpoint：None", "Last Successful Checkpoint：Original Script Locked After Optimization Rejection")
                .replace("Pending Decision：等待项目输入", "Pending Decision：None")
            )
            path.write_text(locked_state, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 0)

    def test_explicit_opt_in_stops_again_at_proposal_confirmation(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        self.assertIn("只有用户明确表示“优化”“继续优化”“进入优化”", workflow)
        self.assertIn("Production Script Proposal输出后必须再次停止", workflow)
        self.assertIn("单独的“继续”“下一步”“好的”", workflow)

        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (skill_root / "portable_project_status.md").read_text(encoding="utf-8")
            proposal_state = (
                canonical.replace("Current State：STATE-00", "Current State：STATE-01")
                .replace("State Status：NOT_STARTED", "State Status：IN_PROGRESS")
                .replace("Script Status：Source Material", "Script Status：Optimized Proposal")
                .replace("Active Workflow：01_project_setup_workflow.md", "Active Workflow：02_script_analysis_workflow.md")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：02_script_analysis_workflow.md")
                .replace("Pending Decision：等待项目输入", "Pending Decision：等待用户确认Production Script Proposal")
            )
            path.write_text(proposal_state, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 0)

            invalid_state_02 = proposal_state.replace("Current State：STATE-01", "Current State：STATE-02")
            path.write_text(invalid_state_02, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 1)

    def test_explicit_locked_script_skips_adaptation_and_rewrite(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        self.assertIn("Route LOCK — No Revision / Final Script", workflow)
        self.assertIn("不执行Script Adaptation、Screenwriting Optimization或Directorial Interpretation", workflow)

        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "portable_project_status.md"
            canonical = (skill_root / "portable_project_status.md").read_text(encoding="utf-8")
            locked_state = (
                canonical.replace("Current State：STATE-00", "Current State：STATE-01")
                .replace("State Status：NOT_STARTED", "State Status：COMPLETE")
                .replace("Script Status：Source Material", "Script Status：Production-Locked")
                .replace("Active Workflow：01_project_setup_workflow.md", "Active Workflow：02_script_analysis_workflow.md")
                .replace("Next Workflow：01_project_setup_workflow.md", "Next Workflow：03_asset_discovery_workflow.md")
                .replace("Last Successful Checkpoint：None", "Last Successful Checkpoint：No-Revision Script Analysis Complete")
                .replace("Pending Decision：等待项目输入", "Pending Decision：None")
            )
            path.write_text(locked_state, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_portable_status, path, True), 0)

    def test_creation_brief_routes_to_director_first_screenplay_generation(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        setup = (skill_root / "workflows" / "01_project_setup_workflow.md").read_text(encoding="utf-8")
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        knowledge = (skill_root / "knowledge" / "screenplay_development.md").read_text(encoding="utf-8")
        template = (skill_root / "templates" / "02_script_analysis_prompt.md").read_text(encoding="utf-8")

        self.assertIn("Creation Brief", setup)
        self.assertIn("Existing Script / Material", setup)
        self.assertIn("同时上传剧本并说“调用sd”", setup)
        self.assertIn("Idea / Brief / Concept → Minimum Project Intent Gate", workflow)
        self.assertIn("不得要求用户先去普通Chat写完整剧本", workflow)
        self.assertIn("Creation Brief不得输出Optimization Opportunity Report", workflow)
        self.assertIn("Director-first Story Development", knowledge)
        self.assertIn("Directable Screenplay QA", knowledge)
        self.assertIn("Creation Brief Route", template)
        self.assertIn("不得提前加入SHOT", template)

    def test_directable_screenplay_qa_is_script_level_not_shot_design(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        knowledge = (skill_root / "knowledge" / "screenplay_development.md").read_text(encoding="utf-8")
        for marker in (
            "Scene Purpose",
            "Audience Experience",
            "Character Objective / Conflict",
            "Relationship Change",
            "Visual Action",
            "Performance Opportunity",
            "Spatial Dramaturgy / Blocking Potential",
            "Information Strategy",
            "Rhythm Curve",
            "AIGC Directability",
        ):
            self.assertIn(marker, knowledge)
        self.assertIn("不全局要求少对白", knowledge)
        self.assertIn("35mm、特写、推镜、摇镜", knowledge)
        self.assertIn("最终剧本必须仍是可独立阅读的剧本", knowledge)

    def test_explicit_direct_optimization_and_script_revision_gates(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        workflow = (skill_root / "workflows" / "02_script_analysis_workflow.md").read_text(encoding="utf-8")
        self.assertIn("直接优化剧本 / 分析并优化 / 直接改写 / 按指定范围优化", workflow)
        self.assertIn("不在User Decision Gate重复询问", workflow)
        self.assertIn("修改这一场 / 改台词 / 调整人物线 / 改结局", workflow)
        self.assertIn("保持Script Development", workflow)
        self.assertIn("若已明确确认并完成STATE-01，则“下一步”按状态合同进入STATE-02", workflow)

    def test_director_thinking_continuity_reaches_scene_and_shot_without_schema_pollution(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        director = (skill_root / "knowledge" / "director_decision_layer.md").read_text(encoding="utf-8")
        scene = (skill_root / "workflows" / "08_scene_breakdown_workflow.md").read_text(encoding="utf-8")
        shot = (skill_root / "workflows" / "09_shot_design_workflow.md").read_text(encoding="utf-8")
        self.assertIn("STATE-01 Writer → Director Handoff / Scene Presentation Intent → STATE-05 Scene Projection → STATE-06 Director Decision Notes", director)
        self.assertIn("不要求把相同规则复制进每个Workflow", director)
        self.assertIn("Upstream Writer Intent And Director Intent Projection", scene)
        self.assertIn("不新增用户可见固定字段", scene)
        self.assertIn("Production-Locked Directable Screenplay", shot)
        self.assertIn("Writer事实决定镜头需要承载什么，Director决定观众如何经历", shot)
        self.assertIn("不从中提取Camera参数", shot)

    def test_installed_chat_work_routing_passes(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        self.assertEqual(run_quiet(validator.validate_state_routing, skill_root, True), 0)

    def test_modular_skill_entrypoint_stays_small_and_route_only(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        skill_path = skill_root / "SKILL.md"
        skill = skill_path.read_text(encoding="utf-8")
        self.assertLessEqual(len(skill.encode("utf-8")), 18000)
        self.assertLessEqual(len((skill_root / "config.md").read_text(encoding="utf-8").encode("utf-8")), 6000)
        for marker in (
            "## System Role",
            "## Production Pipeline",
            "## STATE Overview",
            "## Global Priority",
            "## Activation Entry",
            "## Runtime Reload Entry",
            "## Main Workflow Routing",
            "## Auxiliary Workflow Routing",
            "## External Rules Index",
        ):
            self.assertIn(marker, skill)
        self.assertNotIn("### Canonical Portable State Schema", skill)
        self.assertNotIn("TC IN\n2.", skill)

    def test_skill_update_self_check_is_routed_and_validated(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        contract = (skill_root / "references" / "module_contracts.md").read_text(encoding="utf-8")
        guide = (skill_root / "USER_GUIDE.md").read_text(encoding="utf-8")
        self.assertIn("Skill Update Self-Check / Change Safety Checklist", skill)
        for dimension in (
            "Duplicate Rule Check",
            "Conflict Check",
            "Terminology Drift Check",
            "Rule Ownership Check",
            "Prompt Pollution Check",
            "Routing Integrity Check",
            "Template Consistency Check",
            "Reference Integrity Check",
            "State / Continuity Compatibility Check",
            "User Guide Sync Check",
            "Regression Check",
            "Change Classification Check",
        ):
            self.assertIn(dimension, contract)
        for repair_policy in (
            "Detection scope is Skill-wide",
            "Every finding requires disposition",
            "SAFE_LOCAL",
            "CONTROLLED_CROSS_MODULE",
            "HIGH_RISK / DECISION_REQUIRED",
            "不能再使用“与本次修改无关”作为延期理由",
        ):
            self.assertIn(repair_policy, contract)
        self.assertIn("Skill Update Self-Check / Change Safety Checklist", guide)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_screenwriter_module_writer_intelligence_eleven_regressions(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]

        def source(relative: str) -> str:
            return (skill_root / relative).read_text(encoding="utf-8-sig")

        owner = source("knowledge/screenplay_development.md")
        for marker in (
            "Screenwriter Module / Writer Intelligence Layer",
            "WRITER INTENT PACKET", "Project-level", "Scene-level", "Beat-level",
            "Story Logic / Causality", "Character Engine", "Scene Value Change",
            "Writer Beat Is Not A Shot", "Dialogue / Subtext",
            "Setup / Payoff And Information Architecture", "Writer → Director Handoff",
        ):
            self.assertIn(marker, owner)

        contracts = source("references/module_contracts.md")
        self.assertIn("Screenwriter Module Contract", contracts)
        self.assertIn("Writer Beat不等于Shot", contracts)
        self.assertIn("Information Architecture", contracts)
        self.assertIn("Information Presentation", contracts)

        cross_stage = {
            "workflows/08_scene_breakdown_workflow.md": (
                "Writer Beat Map", "Value / Relationship / Information Change",
            ),
            "workflows/09_shot_design_workflow.md": (
                "Writer Beat / Writer obligation", "Writer Beat ≠ Shot",
            ),
            "workflows/10_clip_production_workflow.md": (
                "Clip Boundary不得错误切断Writer Beat", "Setup / Payoff timing",
            ),
            "knowledge/prompt_compilation/state08_projection.md": (
                "Writer Intent Preservation Gate", "Writer + Director Intent Preservation QA",
            ),
            "workflows/12_editing_workflow.md": (
                "Writer Rhythm Protection", "reaction logic",
            ),
            "workflows/13_review_workflow.md": (
                "Story Review", "WRITING FAILURE", "DIRECTING FAILURE",
                "GENERATION FAILURE", "EDITING FAILURE",
            ),
        }
        for relative, markers in cross_stage.items():
            text = source(relative)
            for marker in markers:
                self.assertIn(marker, text, relative)

        regressions = source("references/regression_scenarios.md")
        evidence = {
            "A": ("Rainy-night Two-woman Reunion", "不出现焦段、机位、运镜"),
            "B": ("Diagnose Before Rewrite", "causality", "User Decision Gate"),
            "C": ("Convenience Action Rejected", "Trigger → Character Interpretation"),
            "D": ("Subtext Opportunity", "Surface Meaning → Subtext → Hidden Objective"),
            "E": ("No State Change", "weak / replaceable scene"),
            "F": ("Timing Survives Production", "提前暴露"),
            "G": ("Writer Beat Is Not Shot", "一个Shot、多个Shot"),
            "H": ("Preserve Both Authorities", "Camera仍只来自Director Decision"),
            "I": ("Unmotivated Behavior Is Writing Failure", "返回STATE-01"),
            "J": ("No Universal Conflict Formula", "不共享强制冲突密度"),
            "K": ("Continue / Reload / Re-entry Preserved", "Accepted Take Canon"),
        }
        letters = "ABCDEFGHIJK"
        starts = {letter: regressions.index(f"### R24-{letter}") for letter in letters}
        deterministic = regressions.index("## Deterministic Expectations")
        for index, letter in enumerate(letters):
            end = starts[letters[index + 1]] if index + 1 < len(letters) else deterministic
            scenario = regressions[starts[letter]:end]
            self.assertIn("输入：", scenario, letter)
            self.assertIn("PASS：", scenario, letter)
            self.assertIn("FAIL：", scenario, letter)
            for marker in evidence[letter]:
                self.assertIn(marker, scenario, letter)

        final_template = source("templates/10_video_prompt.md")
        for leaked_writer_field in (
            "WRITER INTENT PACKET：", "Writer Intent Preservation Gate：",
        ):
            self.assertNotIn(leaked_writer_field, final_template)
        skill = source("SKILL.md")
        self.assertNotIn("STATE-10", skill)
        self.assertLessEqual(len(skill.encode("utf-8")), 18000)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_skill_validator_rejects_version_build_mismatch(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            skill_path = copied / "SKILL.md"
            skill_text = skill_path.read_text(encoding="utf-8")
            build_line = next(line for line in skill_text.splitlines() if line.startswith("Build ID:"))
            skill_path.write_text(
                skill_text.replace(build_line, "Build ID: sd-film-version-mismatch"),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

    def test_standalone_skill_discovery_contract_is_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = skill.split("---", 2)[1]
        for alias in (
            "调用sd", "调用SD", "用SD Film", "重新调用sd", "恢复旧项目", "继续之前的项目",
        ):
            self.assertIn(alias, frontmatter)
        metadata = (skill_root / "agents" / "openai.yaml").read_text(encoding="utf-8")
        for marker in (
            'display_name: "SD Film"',
            '$sd-film',
            "allow_implicit_invocation: true",
        ):
            self.assertIn(marker, metadata)
        contracts = (skill_root / "references" / "module_contracts.md").read_text(encoding="utf-8")
        regressions = (skill_root / "references" / "regression_scenarios.md").read_text(encoding="utf-8")
        guide = (skill_root / "USER_GUIDE.md").read_text(encoding="utf-8")
        self.assertIn("### Standalone Skill Discovery Guard", contracts)
        discovery_matrix = regressions.split(
            "## R26 Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)", 1
        )[1].split("## Deterministic Expectations", 1)[0]
        starts = {index: discovery_matrix.index(f"### SD-R{index} ") for index in range(1, 6)}
        expected = {
            1: ("$HOME/.agents/skills/sd", "只保留一个", "两个用户级位置"),
            2: ("description保留六个启动别名", "allow_implicit_invocation: true", "false"),
            3: ("$sd-film", "@`选择器只显示Plugin", "display_name`误当作`@`注册"),
            4: ("网页端、移动端", "不擅自改做Plugin", "虚假承诺"),
            5: ("重启桌面应用或新建Chat", "rules/runtime_reload.md", "第二套activation"),
        }
        for index in range(1, 6):
            end = starts[index + 1] if index < 5 else len(discovery_matrix)
            scenario = discovery_matrix[starts[index]:end]
            for marker in ("输入：", "PASS：", "FAIL：", *expected[index]):
                self.assertIn(marker, scenario, f"SD-R{index}")
        for marker in ("@`选择器只显示Plugin", "$sd-film", ".agents\\skills\\sd"):
            self.assertIn(marker, guide)
        for relative in (
            "USER_GUIDE.md",
            "references/module_contracts.md",
            "references/regression_scenarios.md",
        ):
            self.assertNotIn("@SD Film", (skill_root / relative).read_text(encoding="utf-8"), relative)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_skill_validator_rejects_disabled_implicit_invocation(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            metadata = copied / "agents" / "openai.yaml"
            metadata.write_text(
                metadata.read_text(encoding="utf-8").replace(
                    "allow_implicit_invocation: true",
                    "allow_implicit_invocation: false",
                ),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

    def test_skill_validator_rejects_missing_chat_discovery_alias(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            skill_path = copied / "SKILL.md"
            skill_text = skill_path.read_text(encoding="utf-8")
            skill_path.write_text(
                skill_text.replace("“继续之前的项目”", "“继续过往项目”", 1),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

    def test_skill_validator_rejects_missing_openai_yaml(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            (copied / "agents" / "openai.yaml").unlink()
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

    def test_cross_clip_tail_frame_abc_contract_is_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        template = (skill_root / "templates" / "10_video_prompt.md").read_text(encoding="utf-8")
        consistency = (skill_root / "rules" / "04_consistency_rules.md").read_text(encoding="utf-8")
        for marker in (
            "A【同镜头连续承接",
            "B【新镜头参考型",
            "C【新镜头且无需尾帧",
            "同镜头连续承接用途",
            "空间/站位/景别参考用途",
            "待用户提供/待上传、未确认",
        ):
            self.assertIn(marker, template)
            self.assertIn(marker, consistency)
        self.assertIn("以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。", template)
        self.assertIn("B不得使用A类", template)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_cross_clip_end_state_and_reference_routing_are_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        files = {
            relative: (skill_root / relative).read_text(encoding="utf-8")
            for relative in (
                "rules/02_asset_rules.md",
                "rules/04_consistency_rules.md",
                "knowledge/clip_preflight_check.md",
                "workflows/10_clip_production_workflow.md",
                "workflows/11_video_generation_workflow.md",
                "workflows/13_review_workflow.md",
                "templates/20_clip_plan.md",
                "templates/10_video_prompt.md",
                "references/regression_scenarios.md",
            )
        }
        for relative in (
            "rules/04_consistency_rules.md",
            "knowledge/clip_preflight_check.md",
            "workflows/10_clip_production_workflow.md",
            "workflows/11_video_generation_workflow.md",
            "workflows/13_review_workflow.md",
            "templates/20_clip_plan.md",
            "templates/10_video_prompt.md",
            "references/regression_scenarios.md",
        ):
            self.assertIn("Clip End-State Record / Next-Clip Carryover", files[relative])
        for marker in (
            "Character State",
            "Spatial State",
            "Prop State",
            "Camera State",
            "Environment State",
            "Performance State",
            "Continuity Risks",
            "Next-Clip Carryover",
        ):
            self.assertIn(marker, files["templates/20_clip_plan.md"])
        for relative in (
            "rules/02_asset_rules.md",
            "knowledge/clip_preflight_check.md",
            "workflows/10_clip_production_workflow.md",
            "workflows/11_video_generation_workflow.md",
            "workflows/13_review_workflow.md",
            "templates/20_clip_plan.md",
        ):
            self.assertIn("Reference Selection / Routing", files[relative])
        regression = files["references/regression_scenarios.md"]
        self.assertIn("R13-A Same-Shot Direct Continuation", regression)
        self.assertIn("R13-B New Shot With Tail Position Reference", regression)
        self.assertIn("R13-C New Shot Without Tail Reference", regression)
        case_a = regression.split("### R13-A Same-Shot Direct Continuation", 1)[1].split("### R13-B", 1)[0]
        case_b = regression.split("### R13-B New Shot With Tail Position Reference", 1)[1].split("### R13-C", 1)[0]
        case_c = regression.split("### R13-C New Shot Without Tail Reference", 1)[1].split("---", 1)[0]
        for marker in (
            "A Direct",
            "Tail Frame Required = YES",
            "Character Canonical",
            "Environment Canonical",
            "Prop Canonical",
            "同镜头连续承接用途",
            "不重置坐姿",
        ):
            self.assertIn(marker, case_a)
        for marker in (
            "B Reference-Only",
            "Tail Frame Required = YES",
            "空间/站位/景别参考用途",
            "另起新镜头重新构图",
            "不使用A的固定Direct句",
        ):
            self.assertIn(marker, case_b)
        for marker in (
            "C Not Required",
            "Tail Frame Required = NO",
            "不列、不预留`REF-TAIL`",
            "Environment Canonical",
            "Prop Canonical",
            "Top-down Map不进入参考资产",
        ):
            self.assertIn(marker, case_c)
        self.assertIn("Shot-State Memory", files["rules/04_consistency_rules.md"])
        self.assertIn("Shot-State Memory", files["workflows/10_clip_production_workflow.md"])
        self.assertIn("参考资产按需路由，不是越多越好", files["rules/02_asset_rules.md"])
        self.assertNotIn("Scene Anchor`资产", files["rules/02_asset_rules.md"])
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_prompt_attention_translation_and_physical_data_contract_is_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        files = {
            relative: (skill_root / relative).read_text(encoding="utf-8")
            for relative in (
                "rules/03_prompt_rules.md",
                "knowledge/knowledge_application_reflection.md",
                "knowledge/prompt_compilation/state08_projection.md",
                "knowledge/11_seedance_adapter.md",
                "workflows/11_video_generation_workflow.md",
                "workflows/13_review_workflow.md",
                "templates/10_video_prompt.md",
                "references/regression_scenarios.md",
            )
        }
        projection = files["knowledge/prompt_compilation/state08_projection.md"]
        for marker in (
            "Prompt Attention / Control Allocation Gate",
            "Five-Dimensional Prompt Control Matrix",
            "Subject & Physical Motion",
            "Environment & Emotional Lighting",
            "Optics & Camera Choreography",
            "Timeline & State Evolution",
            "Aesthetic Medium & Rendering",
            "Style Label Expansion Rule",
            "Executable Style Carrier Rule",
            "Style Label → Project-specific Style Meaning → Executable Style Carriers → Prompt Compression",
            "具象化后不得默认强制删除",
            "Style State And Delta Compression",
            "默认选择3—5个",
            "Writer Intent → Director Intent → Visual Translation → Physical Anchoring → Prompt Compression → Final Clip Prompt",
            "Blender / Unreal式严格物理仿真",
        ):
            self.assertIn(marker, projection)
        template = files["templates/10_video_prompt.md"]
        self.assertIn("Prompt Attention / Compression", template)
        self.assertIn("Active Character Canonical References", template)
        self.assertIn("Active Environment Canonical References", template)
        regression = files["references/regression_scenarios.md"]
        for marker in (
            "R15-A Literary Camera Intent",
            "R15-B Over-Engineered Camera Data",
            "R15-C Canonical Assets Free Prompt Attention",
            "R15-D Director Style Label Expansion",
            "R15-E Cinematic Live-action Label Expansion",
            "R15-F Stable Project Style Delta",
            "R15-G Action-Heavy Clip Style Compression",
            "镜头像终于鼓起勇气一样靠近她",
            "0.137m/s",
            "CHAR-001@v003",
            "岩井俊二式青春电影氛围",
            "电影级真人青春短片质感",
        ):
            self.assertIn(marker, regression)
        case_d = regression.split("### R15-D Director Style Label Expansion", 1)[1].split(
            "### R15-E Cinematic Live-action Label Expansion", 1
        )[0]
        for marker in (
            "可以保留`岩井俊二式青春电影氛围`",
            "Project-specific Style Meaning",
            "3—5个（或更少）高价值carriers",
            "名称完全冗余时允许省略",
            "具象化后不默认删除",
            "规定carriers足够后必须删除导演名",
        ):
            self.assertIn(marker, case_d)
        case_e = regression.split("### R15-E Cinematic Live-action Label Expansion", 1)[1].split(
            "### R15-F Stable Project Style Delta", 1
        )[0]
        for marker in (
            "可以保留`电影级真人青春短片质感`",
            "真实演员自然肤质与皮肤细节",
            "自然曝光关系和真实暗部层次",
            "浅景深",
            "轻微胶片颗粒",
            "受控高光或克制的镜头动态",
        ):
            self.assertIn(marker, case_e)
        case_f = regression.split("### R15-F Stable Project Style Delta", 1)[1].split(
            "### R15-G Action-Heavy Clip Style Compression", 1
        )[0]
        for marker in (
            "Source Carries State, Prompt Carries Delta",
            "只补",
            "当前delta与风险",
            "不复制CLIP-001的完整",
            "正式Style Source不可访问或含义发生变化",
        ):
            self.assertIn(marker, case_f)
        case_g = regression.split("### R15-G Action-Heavy Clip Style Compression", 1)[1].split(
            "## R16 Delta / Budget / Scope / Canon / Authority / Retake", 1
        )[0]
        for marker in (
            "主体、动作、空间、时间顺序、摄影机路径、道具状态与Handoff优先",
            "1—3个或更少高价值carriers",
            "一个仍有统一锚定价值的重要标签可以保留",
            "具象化后默认删除导演名",
            "固定Template字段仍完整",
            "以压缩为由删除Template字段",
        ):
            self.assertIn(marker, case_g)
        for content in files.values():
            self.assertNotIn("具体carriers已足够时名称是否已删除", content)
            self.assertNotIn("其余导演名、审美词与装饰性材质描述在Prompt Compression中删除", content)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_global_runtime_rules_are_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        for relative in (
            "rules/runtime_reload.md",
            "rules/state_source.md",
            "rules/chat_compatibility.md",
            "rules/progression_rules.md",
            "rules/activation_rules.md",
            "rules/completion_gate.md",
            "rules/compatibility_mapping.md",
            "rules/resource_loading.md",
        ):
            self.assertTrue((skill_root / relative).is_file(), relative)

    def test_verified_reuse_preserves_runtime_and_final_gates(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        rule = (skill_root / "rules" / "resource_loading.md").read_text(encoding="utf-8")
        for marker in (
            "## Verified Reuse Register",
            "不创建新的State Source、项目缓存、Completion Gate或最终输出Schema",
            "每次Workflow开始、恢复、保存、推进或重载仍必须按`rules/state_source.md`实际选择State Source",
            "显式Reload仍完整遵守`rules/runtime_reload.md`",
            "不确定是否受影响时默认废弃",
            "Completion Checklist、`rules/completion_gate.md`和Template完整性检查",
        ):
            self.assertIn(marker, rule)

    def test_routing_validator_rejects_competing_state_source_owner(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            workspace = copied / "references" / "project_workspace.md"
            workspace.write_text(
                workspace.read_text(encoding="utf-8")
                + "\nActive Project Root/project_status.md > portable_project_status.md\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_audio_router_bypass(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            activation = copied / "rules" / "activation_rules.md"
            activation.write_text(
                activation.read_text(encoding="utf-8")
                + "\n显式声音请求直接调用`workflows/20_seed_audio_voice_asset_workflow.md`。\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_untruthful_reload_contract(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            runtime = copied / "rules" / "runtime_reload.md"
            runtime.write_text(
                runtime.read_text(encoding="utf-8").replace("禁止报告`RELOADED`", "可以报告`RELOADED`"),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_missing_chat_hot_reload_trigger(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            runtime = copied / "rules" / "runtime_reload.md"
            runtime.write_text(
                runtime.read_text(encoding="utf-8").replace("重新调用sd", "reentry-token-removed"),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_missing_reload_evidence(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            runtime = copied / "rules" / "runtime_reload.md"
            runtime.write_text(
                runtime.read_text(encoding="utf-8").replace("Owner Files Resolved", "Owner Files Unknown"),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_missing_workflow_reentry_contract(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            runtime = copied / "rules" / "runtime_reload.md"
            runtime.write_text(
                runtime.read_text(encoding="utf-8").replace(
                    "Current Skill + Current Project Context + Current User Task",
                    "Previous output only",
                ),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_runtime_reentry_r1_old_prompt_cannot_bypass_state08_entry(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        regressions = (skill_root / "references" / "regression_scenarios.md").read_text(encoding="utf-8")
        for marker in ("Previous Assistant Output", "Reference Selection / Routing", "Prompt Compiler", "Final QA"):
            self.assertIn(marker, runtime)
        self.assertIn("### R12-I Old Prompt Does Not Bypass STATE-08 Entry", regressions)

    def test_runtime_reentry_r2_stable_confirmed_sketch_is_reused(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        preflight = (skill_root / "knowledge" / "clip_preflight_check.md").read_text(encoding="utf-8")
        self.assertIn("`KEEP`并复用", runtime)
        self.assertIn("普通Prompt优化", preflight)
        self.assertIn("必须复用原草图", preflight)

    def test_runtime_reentry_r3_material_blocking_change_is_reassessed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        preflight = (skill_root / "knowledge" / "clip_preflight_check.md").read_text(encoding="utf-8")
        self.assertIn("Blocking发生实质变化必须执行Reassessment", runtime)
        for marker in ("REPLACE with REF-SKETCH-XX-v2", "RETIRE sketch", "CREATE new sketch"):
            self.assertIn(marker, preflight)

    def test_runtime_reentry_r4_updated_skill_and_owner_are_reread(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        for marker in ("Loaded Skill Version", "Loaded Build ID", "Owner Files Resolved", "Last Routed Workflow"):
            self.assertIn(marker, runtime)
        self.assertIn("Latest Successfully Loaded Current Skill Definition", runtime)

    def test_runtime_reentry_r5_plain_next_does_not_force_reload(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        progression = (skill_root / "rules" / "progression_rules.md").read_text(encoding="utf-8")
        self.assertIn("普通的“继续”“下一步”不是重载触发词", runtime)
        self.assertIn("收到纯推进命令时", progression)

    def test_runtime_reentry_r6_unavailable_load_reports_fallback(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        for marker in ("UNAVAILABLE", "Fallback Source", "不能声称已按current Skill完成Re-entry"):
            self.assertIn(marker, runtime)

    def test_runtime_reentry_r7_ordinary_chat_does_not_default_to_work(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        runtime = (skill_root / "rules" / "runtime_reload.md").read_text(encoding="utf-8")
        self.assertIn("普通Chat不是本地文件模式的降级版", runtime)
        self.assertIn("普通制作执行不得默认要求Work", runtime)

    def test_legacy_recovery_lr_r1_to_r10_are_executable_contracts(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        regressions = (skill_root / "references" / "regression_scenarios.md").read_text(encoding="utf-8")
        starts = {
            index: regressions.index(f"### LR-R{index} ")
            for index in range(1, 11)
        }
        dry_runs = regressions.index("### R25 Dry-run Coverage")
        expected = {
            1: ("Ordinary Chat Recovery Must Not Default to Work", "Current Accessible Skill + Current Verifiable Project Context", "不要求Work"),
            2: ("Skill / Project Sources Are Independent", "Portable Project State", "source不同即失败"),
            3: ("Historical Skill Is Never Authority", "Latest Successfully Loaded Current Skill Definition", "legacy mapping hint"),
            4: ("Legacy State Maps Forward", "当前Pipeline", "不从STATE-00重启"),
            5: ("Intent Backfill Is Additive", "Legacy Intent Backfill", "不自动失效"),
            6: ("Confirmed Visual Anchors Persist", "Blocking Signature", "KEEP"),
            7: ("STATE-08 Resume Re-enters Workflow", "Reference Selection / Routing", "Prompt Compiler → Final QA"),
            8: ("Claim Gate Honesty", "UNAVAILABLE", "不声称"),
            9: ("Work Escalation Only On True Need", "Portable State或Current Verifiable Project Context足够", "A继续普通Chat"),
            10: ("Plain Next Does Not Force Full Recovery", "rules/progression_rules.md", "不重复全量reload"),
        }
        for index in range(1, 11):
            end = starts[index + 1] if index < 10 else dry_runs
            scenario = regressions[starts[index]:end]
            for marker in ("输入：", "PASS：", "FAIL：", *expected[index]):
                self.assertIn(marker, scenario, f"LR-R{index}")

    def test_legacy_recovery_dry_run_matrix_covers_a_to_h(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        regressions = (skill_root / "references" / "regression_scenarios.md").read_text(encoding="utf-8")
        section = regressions.split("### R25 Dry-run Coverage", 1)[1].split("## Deterministic Expectations", 1)[0]
        for letter, marker in {
            "A": "old conversation + current accessible Skill + context only",
            "B": "current Skill + portable_project_status",
            "C": "current Skill unavailable",
            "D": "STATE-08 CLIP-04 + confirmed assets/sketch",
            "E": "old state names",
            "F": "Director / Screenwriter schema changed",
            "G": "only 下一步",
            "H": "all current / portable / context sources insufficient",
        }.items():
            self.assertIn(f"- {letter} `", section, letter)
            self.assertIn(marker, section, letter)

    def test_runtime_recovery_regression_protection_is_unconditional(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        contracts = (skill_root / "references" / "module_contracts.md").read_text(encoding="utf-8")
        protection = contracts.split("### Runtime Recovery Regression Protection", 1)[1].split(
            "### Required Self-Check Summary", 1
        )[0]
        for marker in (
            "Unconditional Chat Runtime Startup And Recovery Guard",
            "无论修改任何文件、模块、文案、Template、Knowledge、测试、Validator或仅修正拼写",
            "每次正式修改都必须运行它们",
            "SKILL.md` activation / routing",
            "Runtime Reload / Workflow Re-entry",
            "State Source / Portable State",
            "Project Setup / project status schema",
            "Pipeline / STATE rename",
            "Screenwriter Module / WRITER INTENT PACKET",
            "Director Module / DIRECTOR INTENT PACKET",
            "STATE-07 / STATE-08 Current Object",
            "USER_GUIDE.md` recovery commands",
            "ordinary Chat vs Work routing",
            "“本轮改的不是recovery文件”为由跳过",
            "scripts/validate_sd_film.py skill <skill-root>",
            "scripts/test_validate_sd_film.py",
        ):
            self.assertIn(marker, protection)

        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        guide = (skill_root / "USER_GUIDE.md").read_text(encoding="utf-8")
        regressions = (skill_root / "references" / "regression_scenarios.md").read_text(encoding="utf-8")
        self.assertIn("无论改动是否涉及runtime", skill)
        self.assertIn("不得以Diff范围、文件类型", skill)
        self.assertIn("即使只修改文案、Knowledge、Template或拼写", guide)
        self.assertIn("每次正式修改SD Film都必须完整运行LR-R1至LR-R10", regressions)

    def test_routing_validator_rejects_competing_legacy_recovery_owner(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            director = copied / "knowledge" / "director_decision_layer.md"
            director.write_text(
                director.read_text(encoding="utf-8")
                + "\n## Legacy Project Recovery Integrity\nDirector owns Work escalation.\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_missing_legacy_intent_backfill(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            runtime = copied / "rules" / "runtime_reload.md"
            runtime.write_text(
                runtime.read_text(encoding="utf-8").replace(
                    "Backfill missing intent, do not remake confirmed production.",
                    "Remake confirmed production.",
                ),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_skill_validator_always_runs_chat_startup_recovery_guard(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            regressions = copied / "references" / "regression_scenarios.md"
            regressions.write_text(
                regressions.read_text(encoding="utf-8").replace(
                    "### LR-R1 Ordinary Chat Recovery Must Not Default to Work",
                    "### Removed Ordinary Chat Recovery Contract",
                ),
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

    def test_routing_validator_rejects_completion_owner_overlap(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            contract = copied / "references" / "project_state_contract.md"
            contract.write_text(
                contract.read_text(encoding="utf-8") + "\n## State Transition Protocol\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_routing_validator_rejects_competing_state08_schema(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            workflow = copied / "workflows" / "11_video_generation_workflow.md"
            workflow.write_text(
                workflow.read_text(encoding="utf-8")
                + "\n### 时长：\n### 画幅：\n### 参考资产：\n### 首帧参考：\n### 尾帧限制：\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state_routing, copied, True), 1)

    def test_portable_schema_is_owned_by_state_contract(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        contract = (skill_root / "references" / "project_state_contract.md").read_text(encoding="utf-8")
        self.assertIn("### Canonical Portable State Schema", contract)
        self.assertIn("State Status: NOT_STARTED", contract)
        self.assertIn("Next Workflow: 01_project_setup_workflow.md", contract)
        self.assertIn("## State Control", contract)

    def test_init_creates_state_v2_and_ledgers(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            registry = base / "registry.json"
            registry.write_text('{"schema_version": 1, "projects": []}', encoding="utf-8")
            root = base / "project"
            args = argparse.Namespace(
                root=str(root),
                registry=str(registry),
                project_id="PROJECT-INIT-001",
                name="Init Test",
                project_type="Short",
                source_material="Brief",
            )
            self.assertEqual(run_quiet(validator.init_project, args), 0)
            self.assertEqual(run_quiet(validator.validate_project, root, True), 0)

    def test_valid_project_state_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project_id = "PROJECT-TEST-001"
            (root / "project_manifest.json").write_text(
                json.dumps({"schema_version": 1, "project_id": project_id, "project_name": "Test"}),
                encoding="utf-8",
            )
            status = f"""# SD Film Project Status

## State Control
- Status Schema Version：2
- Project ID：{project_id}
- Project Name：Test
- Current State：STATE-00
- State Status：COMPLETE
- Script Status：Source Material
- Active Workflow：None
- Last Completed Step：STATE-00 Project Setup
- Last Successful Checkpoint：REV-0001
- Next Workflow：02_script_analysis_workflow.md
- Return Route：None
- Pending Decision：None
- Revision ID：REV-0001
- Updated At：2026-08-24

## Completed Tasks
Project Setup
## Pending Tasks
STATE-01
## Active Artifacts
Core files
## Confirmed Assets
None
## Visual Direction Lock
Pending
## Continuity And Open Risks
None
## Review Control
- Review Result：NOT_REVIEWED
## Version History
REV-0001
"""
            (root / "project_status.md").write_text(status, encoding="utf-8")
            (root / "project_bible.md").write_text(f"# Bible\n\n- Project ID：{project_id}\n", encoding="utf-8")
            (root / "asset_registry.md").write_text(f"# Registry\n\n- Project ID：{project_id}\n", encoding="utf-8")
            (root / "execution_ledger.md").write_text(f"# Execution\n\n- Project ID：{project_id}\n", encoding="utf-8")
            (root / "artifact_registry.md").write_text(f"# Artifacts\n\n- Project ID：{project_id}\n", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_project, root, True), 0)

            legacy_status = status.replace(
                "STATE-01",
                "- STATE-06 " + "Shot Design\n"
                "- STATE-07 " + "Storyboard\n"
                "- STATE-08 " + "Video Generation",
            )
            (root / "project_status.md").write_text(legacy_status, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_project, root, True), 1)

    def test_character_environment_prop_confirmed_asset_closure_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "asset_registry.md"
            blocks = []
            for asset_id, name, image_prompts, refs in (
                ("CHAR-001", "林遥", "Three-view; Face close-up; State variants Not Required", "char-turnaround.png; char-face.png"),
                ("ENV-001", "海边气象站", "Main reference; Reverse view; Console key area", "env-main.png; env-reverse.png; env-console.png"),
                ("PROP-001", "风暴数据记录器", "Main reference; Alarm state; Port detail", "prop-main.png; prop-alarm.png; prop-port.png"),
            ):
                blocks.append(
                    f"""### {asset_id} {name}
- Status：Active
- Visual Production Status：Asset Confirmed
- Active Version：v001
- Prompt Revision：P-v001
- Image Prompts：{image_prompts}
- Prompt Confirmation：用户确认P-v001
- Candidate References：{refs}
- Image Confirmation：用户确认全部候选图
- Canonical References：{refs}
- Immutable Traits：已锁定
- Mutable State Dimensions：仅剧情授权状态
- Approval Basis：用户图片确认
"""
                )
            path.write_text("# Asset Registry\n\n" + "\n".join(blocks), encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_asset_registry, path, True), 0)

    def test_character_environment_prop_each_passes_all_four_visual_stages(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "asset_registry.md"
            cases = (
                ("CHAR-001", "Three-view; Face close-up; State variants Not Required", "char-c01.png"),
                ("ENV-001", "Main reference; Reverse view; Key area", "env-c01.png"),
                ("PROP-001", "Main reference; Alarm state; Port detail", "prop-c01.png"),
            )
            for asset_id, prompts, candidate in cases:
                snapshots = (
                    f"""### {asset_id} test
- Status：Planning
- Visual Production Status：Prompt Draft
- Prompt Revision：P-v001
- Image Prompts：{prompts}
""",
                    f"""### {asset_id} test
- Status：Generating
- Visual Production Status：Prompt Confirmed
- Prompt Revision：P-v001
- Image Prompts：{prompts}
- Prompt Confirmation：用户确认P-v001
""",
                    f"""### {asset_id} test
- Status：Candidate
- Visual Production Status：Image Generated
- Prompt Revision：P-v001
- Image Prompts：{prompts}
- Prompt Confirmation：用户确认P-v001
- Candidate References：{candidate}
""",
                    f"""### {asset_id} test
- Status：Active
- Visual Production Status：Asset Confirmed
- Active Version：v001
- Prompt Revision：P-v001
- Image Prompts：{prompts}
- Prompt Confirmation：用户确认P-v001
- Candidate References：{candidate}
- Image Confirmation：用户确认{candidate}
- Canonical References：{candidate}
- Immutable Traits：已锁定
- Mutable State Dimensions：仅剧情授权状态
- Approval Basis：用户图片确认
""",
                )
                for snapshot in snapshots:
                    path.write_text("# Asset Registry\n\n" + snapshot, encoding="utf-8")
                    self.assertEqual(run_quiet(validator.validate_asset_registry, path, True), 0)

    def test_image_generated_asset_cannot_be_active_or_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "asset_registry.md"
            path.write_text(
                """# Asset Registry

### CHAR-001 林遥
- Status：Active
- Visual Production Status：Image Generated
- Active Version：v001
- Prompt Revision：P-v001
- Image Prompts：Three-view; Face close-up
- Prompt Confirmation：用户确认P-v001
- Candidate References：char-c01.png
- Canonical References：char-c01.png
- Immutable Traits：已锁定
- Mutable State Dimensions：None
- Approval Basis：Pending image confirmation
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_asset_registry, path, True), 1)

    def test_prompt_confirmed_requires_separate_prompt_confirmation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "asset_registry.md"
            path.write_text(
                """# Asset Registry

### PROP-001 风暴数据记录器
- Status：Generating
- Visual Production Status：Prompt Confirmed
- Prompt Revision：P-v001
- Image Prompts：Main reference; Alarm state; Port detail
- Prompt Confirmation：Pending
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_asset_registry, path, True), 1)

    def test_review_revise_requires_return_route(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review.md"
            sections = "\n".join(f"## {name}\n" for name in validator.REVIEW_SECTIONS)
            path.write_text(
                f"{sections}\nResult：REVISE\nHard Gate Result：FAIL\nPrompt Quality Score（如适用）：70/100\nReturn Route：None\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_review, path, True), 1)

    def test_review_pass_requires_hard_gate_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review.md"
            sections = "\n".join(f"## {name}\n" for name in validator.REVIEW_SECTIONS)
            path.write_text(
                f"{sections}\nResult：PASS\nHard Gate Result：FAIL\nPrompt Quality Score（如适用）：95/100\nReturn Route：None\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_review, path, True), 1)

    def test_valid_review_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review.md"
            sections = "\n".join(f"## {name}\n" for name in validator.REVIEW_SECTIONS)
            path.write_text(
                f"{sections}\nResult：PASS\nHard Gate Result：PASS\nPrompt Quality Score（如适用）：92/100\nReturn Route：None\n",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_review, path, True), 0)

    def test_valid_state08_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1、分镜2", "10")
            fields_1 = make_shot_fields("Continuous Handoff：同一Clip连续生成到分镜2，直接继承稳定结尾。")
            fields_2 = make_shot_fields()
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{fields_1}\n分镜2\n{fields_2}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_valid_single_shot_state08_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10")
            fields = make_shot_fields()
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_positive_first_body_and_single_final_negative_prompt_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10").replace(
                "主风格：电影级写实，自然光，克制表演",
                "主风格：岩井俊二式潮湿夏日青春气质；柔散自然窗光、低饱和灰绿与米白色关系、安静观察式摄影、克制含蓄表演与简洁自然镜头调度。",
            )
            fields = make_shot_fields()
            ending = (
                f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}\n"
                "禁止广告式摆拍与无动机炫技运镜。"
            )
            path.write_text(f"{global_text}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_generic_negative_constraint_in_body_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10").replace(
                "主风格：电影级写实，自然光，克制表演",
                "主风格：禁止夸张微笑、甜宠式表演、广告摆拍、MV慢动作与炫技运镜。",
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_negative_prompt_must_be_final_field_and_paragraph(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10")
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}\n\n说明：后续继续补充正文。"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_local_physical_continuity_positive_constraint_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10")
            fields = make_shot_fields().replace(
                "道具状态：本镜头无关键道具变化。",
                "道具状态：左手持续握住伞柄，整个动作链与结尾状态均保持左手持有。",
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_clip03_state_once_voice_omission_and_compressed_negative_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            reference = (
                "1. CHAR-001@v001角色资产；用途：锁定林夏身份与外观。\n"
                "2. CHAR-002@v001角色资产；用途：锁定许栀身份与外观。\n"
                "3. ENV-002@v001环境资产；用途：锁定旧音乐教室、钢琴、唯一横向长琴凳与窗户结构。\n"
                "4. PROP-001@v001道具资产；用途：锁定乐谱纸张尺寸与材质。\n"
                "5. REF-TAIL-02｜CLIP-02尾帧参考；用途：同镜头连续承接用途，锁定起始姿态、左右与构图。"
            )
            first_frame = (
                "视觉连续；A Direct；Tail Frame Required = YES；"
                "以 REF-TAIL-02｜CLIP-02尾帧参考 为直接承接依据起镜。"
                "林夏在左、许栀在右，共同坐在唯一一张横向长琴凳；摄影机位于轴线同侧，"
                "中景保持教室、钢琴、窗户与阴雨柔光，乐谱位于钢琴边缘，动作从姿态调整前开始。"
            )
            global_text = make_state08_global_sections(
                3,
                3,
                "1、2、3",
                "12",
                title="落下的乐谱与四个单音",
                reference=reference,
                first_frame=first_frame,
            ).replace(
                "人物一致性：CHAR-001身份、脸型、发型、服装和身体比例保持一致",
                "人物一致性：CHAR-001与CHAR-002的身份、年龄感、发型、服装和身体比例保持一致",
            ).replace(
                "环境一致性：已确认环境结构、轴线、背景与光线方向保持一致",
                "环境一致性：ENV-002旧音乐教室结构、唯一横向长琴凳、阴雨天气与柔散窗光保持一致",
            )
            fields_1 = make_shot_fields(
                "Continuous Handoff：同一Clip连续生成到分镜2，继承共坐状态。",
                sound="雨声与风声形成环境底声；同步动作声为衣料与木质轻响；声音尾部持续承接。",
                start_state="第一帧来源：直接继承REF-TAIL-02｜CLIP-02尾帧参考的左右、姿态、道具与轴线。",
            ).replace(
                "轴线同侧固定机位，焦点锁定人物。",
                "轴线同侧固定中景，以同一长琴凳和两人之间的窄负空间形成克制共享构图；先Hold共同朝前，不在信息Beat前运动。",
            ).replace(
                "人物抬眼看向画面右侧，随后停稳。",
                "两人完成姿态调整，双脚落地并形成正常并排坐姿；观众第一眼先确认共同朝前和未被打破的关系距离。",
            )
            fields_2 = make_shot_fields(
                "Continuous Handoff：同一Clip连续生成到分镜3，乐谱留在地面。",
                sound="雨声与风声形成环境底声；同步动作声为纸张滑动与落地轻响；声音尾部持续承接。",
                start_state="第一帧来源：继承分镜1结尾的并排坐姿、左右、道具与轴线。",
            ).replace(
                "轴线同侧固定机位，焦点锁定人物。",
                "泄漏前保持固定；许栀视线回收后才触发极轻微横移，沿轴线同侧移动并停止在仍保留两人窄负空间的共同朝前构图。",
            ).replace(
                "人物抬眼看向画面右侧，随后停稳。",
                "乐谱滑落到木地板，两人低头后重新朝前；许栀仅以一次gaze-only leakage短暂看向林夏，头部与肩线不转，林夏尚未察觉。先看落地乐谱，第二注意目标才是许栀的视线。",
            ).replace(
                "呼吸平稳，视线移动后由平静转为警觉。",
                "许栀屏住半拍呼吸，视线短暂泄漏后立即压回前方；林夏保持克制，没有同步反应或提前确认。",
            )
            fields_3 = make_shot_fields(
                sound="雨声形成环境底声；同步动作声为四个有明显停顿的轻短钢琴单音；声音尾部以雨声收束。",
                start_state="第一帧来源：继承分镜2结尾的共坐状态、左右、地面乐谱与轴线。",
                end_state="四个独立单音完成，人物与乐谱状态稳定；主体清楚可读，可作为下一Clip接口。",
            ).replace(
                "轴线同侧固定机位，焦点锁定人物。",
                "横移停止后保持Static，不再靠近；共享画面压住确认，给Delayed Reaction和最后一个单音后的Pause留出时间。",
            ).replace(
                "人物抬眼看向画面右侧，随后停稳。",
                "林夏停一拍后才以一次变浅的呼吸回应，仍不转头；两人交替各按两次单键，完成四个独立单音后继续共同朝前停稳。",
            ).replace(
                "呼吸平稳，视线移动后由平静转为警觉。",
                "林夏的Delayed Reaction只通过呼吸和指尖停顿泄漏，许栀不追加强度；最后一个单音后共同Hold，关系被确认但不公开表演。",
            )
            ending = (
                f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}\n"
                "座椅结构分裂或人物左右互换、人物离座或拾取乐谱、肢体异常、演奏范围自动扩展、"
                "人物身份或环境结构漂移、夸张表演或炫技摄影。"
            )
            prompt = f"{global_text}\n分镜1\n{fields_1}\n分镜2\n{fields_2}\n分镜3\n{fields_3}\n{ending}"
            self.assertEqual(prompt.count("共同坐在唯一一张横向长琴凳"), 1)
            self.assertEqual(prompt.count("反向提示词："), 1)
            self.assertTrue(prompt.rstrip().endswith("夸张表演或炫技摄影。"))
            for required in (
                "共同朝前", "gaze-only leakage", "第一眼", "第二注意目标",
                "Hold", "Delayed Reaction", "共享构图", "才触发极轻微横移",
                "停止在", "尚未察觉", "Pause",
            ):
                self.assertIn(required, prompt)
            for forbidden in ("音色特征：", "Voice Profile", "Voice Reference", "Audio Reference", "猫", "吉他", "手机", "磁带"):
                self.assertNotIn(forbidden, prompt)
            for internal_label in (
                "DIRECTOR INTENT PACKET", "Task Dominance", "Director-to-Prompt Translation Pass",
                "BUILD / HOLD / PEAK / RELEASE", "PL1", "PL2", "PL3",
            ):
                self.assertNotIn(internal_label, prompt)
            path.write_text(prompt, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_reference_asset_eligibility_regression(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            reference_1_to_5 = (
                "1. 林夏.png｜林夏-基础形象；用途：锁定林夏外观。\n"
                "2. 许栀.png｜许栀-基础形象；用途：锁定许栀外观。\n"
                "3. ENV-02｜窗台钢琴区域教室全景；用途：锁定环境结构。\n"
                "4. REF-TAIL-02｜CLIP-02尾帧参考；用途：锁定人物坐姿、左右站位、肩膀距离、钢琴与窗户空间关系及雨天光线。\n"
                "5. 乐谱参考资产；用途：固定纸张尺寸、材质、印刷内容与旧化程度。"
            )
            pseudo_asset = (
                "6. 板凳参考说明｜用途：锁定两人共坐同一张板凳；"
                "不是两把椅子，不是两张琴凳，不允许拆分座位。"
            )
            fields = make_shot_fields()
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"

            invalid_global = make_state08_global_sections(
                1, 1, "1", "10", reference=f"{reference_1_to_5}\n{pseudo_asset}"
            )
            path.write_text(f"{invalid_global}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

            valid_global = make_state08_global_sections(1, 1, "1", "10", reference=reference_1_to_5)
            path.write_text(f"{valid_global}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_tail_required_yes_with_confirmed_asset_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            reference = (
                "CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。\n"
                "REF-TAIL-001｜CLIP-001尾帧参考；用途：直接承接上一Clip最终有效尾帧；"
                "锁定人物姿态、位置、朝向、距离、构图、机位、环境、光线、天气、道具与情绪。"
            )
            first_frame = (
                "Tail Frame Required = YES；Direct Start-Frame Handoff；"
                "以 REF-TAIL-001｜CLIP-001尾帧参考 为直接承接依据起镜。"
                "人物位于画面左侧、身体朝右并看向前方；摄影机从轴线同侧低机位起始；"
                "中景，主体保持左侧构图与清楚前中后景；环境、天气、道具、动作、光线与情绪逐项继承。"
            )
            global_text = make_state08_global_sections(
                2, 2, "2", "10", reference=reference, first_frame=first_frame
            )
            fields = make_shot_fields(
                start_state="第一帧来源：直接继承REF-TAIL-001｜CLIP-001尾帧参考的人物、空间、道具与轴线。"
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜2\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_tail_required_yes_pending_upload_is_rejected_as_final(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            first_frame = (
                "Tail Frame Required = YES；Direct Start-Frame Handoff；"
                "REF-TAIL-001｜CLIP-001尾帧参考：待用户提供/待上传。"
                "人物位于画面左侧、身体朝右并保持上一Clip文字End State。"
            )
            global_text = make_state08_global_sections(2, 2, "2", "10", first_frame=first_frame)
            fields = make_shot_fields(start_state="第一帧来源：等待上一Clip最终有效尾帧上传后确定。")
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜2\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_multiple_packages_require_explicit_batch_override(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_1 = make_state08_global_sections(1, 1, "1", "8", tail_use="直接作为G02起始帧")
            global_2 = make_state08_global_sections(2, 2, "2", "8")
            fields_1 = make_shot_fields(
                handoff="Continuous Handoff：Direct Cut进入G02，人物、道具与轴线连续继承。"
            )
            fields_2 = make_shot_fields(
                start_state="第一帧来源：直接从[G01尾帧]延续该帧人物、空间、道具与轴线。"
            )
            ending_1 = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            ending_2 = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(
                f"{global_1}\n分镜1\n{fields_1}\n{ending_1}\n{global_2}\n分镜2\n{fields_2}\n{ending_2}",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, True), 0)

    def test_state08_single_later_clip_is_a_valid_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "prompt.md"
            clip_plan = root / "clip.md"
            clip_plan.write_text(
                """# Clip Plan
## Clip Table
| Clip ID | 来源分镜（逐项列出） | 目标时长 | 生成方式 |
|---|---|---:|---|
| CLIP-001 | SHOT-001 | 8秒 | 单镜 |
| CLIP-002 | SHOT-002 | 8秒 | 单镜 |
## Clip Detail Cards
""",
                encoding="utf-8",
            )
            global_text = make_state08_global_sections(
                2,
                2,
                "2",
                "8",
                reference=(
                    "CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。\n"
                    "[G01尾帧]合法尾帧；用途：仅作为本段连续性参考；锁定人物、空间、道具与轴线。"
                ),
                first_frame=(
                    "上一Clip尾帧承接判定：Reference-Only Handoff；[G01尾帧]仅作连续性参考，兼容重建机位。"
                    "人物位于画面左侧、身体朝右并保持视线；摄影机从轴线同侧新机位起始；中景，主体构图保持清楚前中后景；"
                    "环境为已确认室内场景；道具保持原状态；动作起始状态连续；光线状态延续柔和侧光。"
                ),
            )
            fields = make_shot_fields(
                start_state="第一帧来源：以[G01尾帧]作为连续性参考，重建兼容机位并保持人物、道具与轴线。"
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜2\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True, clip_plan), 0)

    def test_state08_front_lock_sections_must_precede_style(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "8")
            misplaced = global_text.replace(
                "【参考资产】\nCHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。\n",
                "",
            ).replace(
                "【人物一致性】",
                "【参考资产】\nCHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。\n【人物一致性】",
            )
            ending = f"【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{misplaced}\n【分镜1】\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_cross_scene_tail_is_continuity_check_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            first_frame = (
                "上一Clip尾帧承接判定：Motivated Discontinuity / No Formal Tail Reference；"
                "上一[G01尾帧]不作本段正式参考资产，仅作人物身份与视觉连续性核对；跨场景断点，"
                "重建原因：进入已确认的新场景；从新场景Confirmed Asset与Scene初始状态建立。"
                "人物位于画面右侧、身体朝左并看向门内；摄影机从新场景轴线同侧平视机位起始；"
                "中景，主体构图保持清楚前中后景；环境为已确认新场景；道具保持上一剧情结果；"
                "动作起始状态为静止观察；光线状态改用新场景已确认暖光。"
            )
            global_text = make_state08_global_sections(
                2,
                2,
                "2",
                "8",
                reference="CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。",
                first_frame=first_frame,
            )
            fields = make_shot_fields(start_state="第一帧来源：从已确认新场景Scene初始状态建立，不继承旧场景空间。")
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜2\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_cross_scene_rejects_formal_previous_tail_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            first_frame = (
                "上一Clip尾帧承接判定：Motivated Discontinuity / No Formal Tail Reference；"
                "上一[G01尾帧]不作本段正式参考资产，仅作人物身份与视觉连续性核对；跨场景断点，"
                "重建原因：进入已确认的新场景；从新场景Confirmed Asset与Scene初始状态建立。"
                "人物位于画面右侧、身体朝左并看向门内；摄影机从新场景轴线同侧平视机位起始；"
                "中景，主体构图保持清楚前中后景；环境为已确认新场景；道具保持上一剧情结果；"
                "动作起始状态为静止观察；光线状态改用新场景已确认暖光。"
            )
            global_text = make_state08_global_sections(
                2,
                2,
                "2",
                "8",
                reference=(
                    "CHAR-001@v001角色资产；用途：锁定人物身份、脸型、发型与服装并保持一致。\n"
                    "[G01尾帧]合法尾帧；用途：作为本段正式参考资产锁定空间。"
                ),
                first_frame=first_frame,
            )
            fields = make_shot_fields(start_state="第一帧来源：从已确认新场景Scene初始状态建立。")
            ending = f"【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜2】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_reference_assets_must_be_explicit_and_constraining(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：8秒；Clip独立生成"
                if section == "【生成段】"
                else ("【参考资产】\n有效内容" if section == "【参考资产】" else valid_global_section(section))
                for section in validator.GLOBAL_SECTIONS
            )
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_first_frame_source_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：8秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            fields = make_shot_fields(start_state="人物站在画面左侧。")
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_high_risk_end_frame_is_rejected_without_story_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：8秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            fields = make_shot_fields(end_state="主体仍在高速运动，动作未完成，构图不可读。")
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：高速运动且动作未完成\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_handoff_must_declare_boundary_class(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：8秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            fields = make_shot_fields(handoff="镜头结束后进入下一镜。")
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_explicit_voice_reference_accepts_conditional_voice_field(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(
                1,
                1,
                "1",
                "10",
                reference="Voice Reference：CHAR-001-VOICE-REF；用途：只锁定声音身份并保持一致，不作为视觉参考。",
                include_voice=True,
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, False, True), 0)

    def test_state08_voice_field_without_current_request_authorization_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10", include_voice=True)
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, False, True), 0)

    def test_state08_voice_reference_without_explicit_control_field_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(
                1,
                1,
                "1",
                "10",
                reference="Audio Reference：CHAR-001-VOICE-REF；用途：当前视频声音控制；授权状态：Confirmed。",
                include_voice=False,
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_voice_reference_rejects_voice_descriptor_in_dialogue(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(
                1,
                1,
                "1",
                "10",
                reference="Voice Reference：CHAR-001-VOICE-REF；用途：当前视频声音控制；授权状态：Confirmed。",
                include_voice=True,
            )
            fields = make_shot_fields().replace("台词：无。", "台词：角色以偏慢语速轻声说：‘你好。’")
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_without_voice_request_omits_voice_field_and_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10", include_voice=False)
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_confirmed_voice_source_is_not_serialized_without_current_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 3, "1", "10", include_voice=False)
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            prompt = f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}"
            for forbidden in ("音色特征：", "Voice Profile", "Voice Reference", "Audio Reference", "No Voice Asset"):
                self.assertNotIn(forbidden, prompt)
            path.write_text(prompt, encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_seed_audio_template_is_compatible_not_claimed_official_fixed_schema(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        template = (skill_root / "templates" / "21_seed_audio_voice_asset.md").read_text(encoding="utf-8")
        for required in (
            "SD Film为Seed Audio 1.0组织的兼容模板",
            "Character / Speaker Identity",
            "Voice Description",
            "Emotional Tone",
            "Delivery / Prosody",
            "Dialogue / Spoken Content",
            "Timing",
            "Acoustic Environment / Ambience",
            "Key Sound Effects",
            "Reference Audio",
        ):
            self.assertIn(required, template)
        self.assertNotIn("Target duration: approximately 15 seconds", template)
        self.assertNotIn("Generate speech only.", template)

    def test_state08_timeline_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(valid_global_section(section) for section in validator.GLOBAL_SECTIONS)
            fields = "\n".join(f"{field}有效内容" for field in validator.SHOT_FIELDS)
            ending = f"【结尾帧要求】\n稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}\n总时长5秒", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_storyboard_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1、分镜2；平台生成时长：6秒；Clip独立生成"
                if section == "【生成段】"
                else ("【参考资产】\nStoryboard分镜板.png" if section == "【参考资产】" else valid_global_section(section))
                for section in validator.GLOBAL_SECTIONS
            )
            fields_1 = "\n".join(
                f"{field}{'同一Clip连续生成到分镜2' if field == '与下一镜衔接：' else '有效内容'}"
                for field in validator.SHOT_FIELDS
            )
            fields_2 = "\n".join(f"{field}有效内容" for field in validator.SHOT_FIELDS)
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields_1}\n【分镜2】\n{fields_2}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_valid_clip_plan_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "clip.md"
            detail_fields = make_clip_detail_fields(
                "SHOT-001 + SHOT-002",
                "10秒",
                "SHOT-001=5秒 + SHOT-002=5秒；合计=10秒；平台生成时长=10秒",
            )
            path.write_text(
                f"""# Clip Plan
- Project ID：PROJECT-TEST
- Status：Confirmed
- Source Detailed Shot Design Artifact / Portable Checkpoint：shots/detailed.md
- Source Detailed Shot Design Status：Confirmed
- Source Detailed Shot Design Revision：REV-0001
- Model Duration Window：4—15秒
- Total Formal Shots：2
- Total Clips：1
- Unit Rule：Shot = 导演镜头设计单位；Clip = AI视频生成执行单位；每个Shot且仅进入一个Clip；Total Clips ≤ Total Formal Shots；STATE-08每个Clip只生成一条连续Prompt
- Namespace Rule：Source Script Label ≠ SCENE ≠ UNIT ≠ SHOT ≠ CLIP；只有Confirmed Detailed Shot Design中的正式SHOT可进入Clip

## Clip Table
| Clip ID | 来源分镜（逐项列出） | 目标时长 | 生成方式 | 合并依据 | 入口锚点 | 出口/尾帧 | 下一Clip连接 |
|---|---|---:|---|---|---|---|---|
| CLIP-001 | SHOT-001 + SHOT-002 | 10秒 | 连续生成 | 有效 | 有效 | 保存为[G01尾帧] | 收尾 |

## Clip Detail Cards
### CLIP-001
{detail_fields}

## Cross-Clip Continuity Ledger
None

## Knowledge Projection Ledger
| Clip ID | Camera/Composition | Movement Combination | Lens/Focus | Performance | Lighting/Color | Transition | Sound | FX | Prompt Evidence Target |
|---|---|---|---|---|---|---|---|---|---|
| CLIP-001 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 |

## Coverage And Validation
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_clip, path, True), 0)

            project_status = Path(temp) / "project_status.md"
            shot_design = Path(temp) / "detailed.md"
            project_status.write_text(
                "- Current State：STATE-07\n- Completed States：STATE-00, STATE-01, STATE-02, STATE-03, STATE-04, STATE-05, STATE-06\n",
                encoding="utf-8",
            )
            shot_design.write_text(
                """# Professional Detailed Shot Script
- Status：Confirmed
- Artifact Revision：REV-0001
| 镜号 | TC IN | TC OUT |
|---|---|---|
| SHOT-001 | 00:00:00.000 | 00:00:05.000 |
| SHOT-002 | 00:00:05.000 | 00:00:10.000 |
""",
                encoding="utf-8",
            )
            self.assertEqual(
                run_quiet(validator.validate_clip, path, True, project_status, shot_design),
                0,
            )

            project_status.write_text(
                "- Current State：STATE-06\n- Completed States：STATE-00, STATE-01, STATE-02, STATE-03, STATE-04, STATE-05\n",
                encoding="utf-8",
            )
            self.assertEqual(
                run_quiet(validator.validate_clip, path, True, project_status, shot_design),
                1,
            )

            project_status.write_text(
                "- Current State：STATE-07\n- Completed States：STATE-00, STATE-01, STATE-02, STATE-03, STATE-04, STATE-05, STATE-06\n",
                encoding="utf-8",
            )
            shot_design.write_text(
                shot_design.read_text(encoding="utf-8").replace("REV-0001", "REV-0002"),
                encoding="utf-8",
            )
            self.assertEqual(
                run_quiet(validator.validate_clip, path, True, project_status, shot_design),
                1,
            )

    def test_single_shot_clip_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "clip.md"
            detail_fields = make_clip_detail_fields(
                "SHOT-001",
                "6秒",
                "SHOT-001=6秒；合计=6秒；平台生成时长=6秒",
            )
            path.write_text(
                f"""# Clip Plan
- Project ID：PROJECT-TEST
- Status：Confirmed
- Source Detailed Shot Design Artifact / Portable Checkpoint：shots/detailed.md
- Source Detailed Shot Design Status：Confirmed
- Source Detailed Shot Design Revision：REV-0001
- Model Duration Window：4—15秒
- Total Formal Shots：1
- Total Clips：1
- Unit Rule：Shot = 导演镜头设计单位；Clip = AI视频生成执行单位；每个Shot且仅进入一个Clip；Total Clips ≤ Total Formal Shots；STATE-08每个Clip只生成一条连续Prompt
- Namespace Rule：Source Script Label ≠ SCENE ≠ UNIT ≠ SHOT ≠ CLIP；只有Confirmed Detailed Shot Design中的正式SHOT可进入Clip

## Clip Table
| Clip ID | 来源分镜（逐项列出） | 目标时长 | 生成方式 | 合并依据 | 入口锚点 | 出口/尾帧 | 下一Clip连接 |
|---|---|---:|---|---|---|---|---|
| CLIP-001 | SHOT-001 | 6秒 | 连续生成 | 有效 | 有效 | 保存为[G01尾帧] | 收尾 |

## Clip Detail Cards
### CLIP-001
{detail_fields}

## Cross-Clip Continuity Ledger
None

## Knowledge Projection Ledger
| Clip ID | Camera/Composition | Movement Combination | Lens/Focus | Performance | Lighting/Color | Transition | Sound | FX | Prompt Evidence Target |
|---|---|---|---|---|---|---|---|---|---|
| CLIP-001 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 | 有效 |

## Coverage And Validation
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_clip, path, True), 0)

    def test_valid_shot_plan_duration_window_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "shot_plan.md"
            path.write_text(
                """# Shot Execution Plan
- Project ID：PROJECT-TEST
- Status：Confirmed
- Source Shot Design Revision：REV-0001
- Total Formal Shots：1
- Formal Shot Duration Window：4—15秒

## Shot Order Table
| Shot ID | Scene / Sequence | Coverage / UNIT | 镜头目的 | 目标时长 | Start Boundary | End-Frame Constraint | Next-Shot Handoff |
|---|---|---|---|---:|---|---|---|
| SHOT-001 | SCENE-001 | UNIT-001 | 有效 | 10秒 | 有效 | 有效 | 收尾 |

## Shot Execution Cards
### SHOT-001
- Planned Execution Duration：10秒
- End-Frame Constraint：有效

## Adjacent-Shot Continuity Ledger
None

## Coverage And Validation
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_shot_plan, path, True), 0)

    def test_shot_plan_out_of_range_duration_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "shot_plan.md"
            path.write_text(
                """# Shot Execution Plan
- Project ID：PROJECT-TEST
- Status：Confirmed
- Source Shot Design Revision：REV-0001
- Total Formal Shots：1
- Formal Shot Duration Window：4—15秒

## Shot Order Table
| Shot ID | Scene / Sequence | Coverage / UNIT | 镜头目的 | 目标时长 | Start Boundary | End-Frame Constraint | Next-Shot Handoff |
|---|---|---|---|---:|---|---|---|
| SHOT-001 | SCENE-001 | UNIT-001 | 有效 | 16秒 | 有效 | 有效 | 收尾 |

## Shot Execution Cards
### SHOT-001
- Planned Execution Duration：16秒

## Adjacent-Shot Continuity Ledger
None

## Coverage And Validation
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_shot_plan, path, True), 1)

    def test_background_music_ban_must_be_first_negative_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1、分镜2；平台生成时长：10秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            fields_1 = "\n".join(
                f"{field}{'同一Clip连续生成到分镜2' if field == '与下一镜衔接：' else '有效内容'}"
                for field in validator.SHOT_FIELDS
            )
            fields_2 = "\n".join(f"{field}有效内容" for field in validator.SHOT_FIELDS)
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n禁止换脸。\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields_1}\n【分镜2】\n{fields_2}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_background_music_is_always_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10")
            sound = "环境底声：室内水声。同步前景声：脚步与衣料摩擦。背景音乐：用户明确要求的轻柔主题音乐。声音尾部：水声延续。"
            ending = "反向提示词：禁止换脸。"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields(sound=sound)}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_valid_instrumental_seedmusic_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "music.md"
            path.write_text(
                """# MUSIC / SEED-MUSIC Score Package
## Module Routing Record
- Route: `MUSIC / SEED-MUSIC Score`
- Explicit Trigger Evidence: 用户要求为CLIP-006规划配乐
- Requested Scope: CLIP-006
- Requested Deliverable: SeedMusic Prompt
- Generation Mode: `INSTRUMENTAL`
## Scope And Music Strategy
有效
## Spotting Map
| Range | Decision |
|---|---|
| CLIP-005尾部 | SILENCE / PRODUCTION SOUND ONLY |
| CLIP-006 | MUSIC CUE |
## Music Bible / Motif Map
有效
## Cue Sheet
| Cue ID | Related Clip(s) |
|---|---|
| MUS-CUE-001 | CLIP-006 |
## SeedMusic Prompt Blocks
### MUS-CUE-001｜CLIP-006｜克制揭示 SeedMusic纯音乐提示词
- Related Clip(s): `CLIP-006`
- Generation Mode: `INSTRUMENTAL`
```text
style:
instrumental only; no vocals, no singing, no lyrics, no spoken word, no rap, no choir, no humming, no vocalise; music only, no dialogue, ambience, Foley or sound effects; restrained chamber strings, low pulse, unresolved harmony

structure:
[Verse]: 0s
[Bridge]: 8s
[Outro]: 14s
```
## Review
- [x] 已检查
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_music_package, path, True), 0)

    def test_seedmusic_structure_must_start_at_zero_and_increase(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "music.md"
            path.write_text(
                """# MUSIC / SEED-MUSIC Score Package
## Module Routing Record
- Route: `MUSIC / SEED-MUSIC Score`
- Explicit Trigger Evidence: 输出配乐提示词
- Requested Deliverable: SeedMusic Prompt
- Generation Mode: `INSTRUMENTAL`
## Scope And Music Strategy
有效
## Spotting Map
MUSIC CUE；SILENCE / PRODUCTION SOUND ONLY
## Music Bible / Motif Map
有效
## Cue Sheet
MUS-CUE-001
## SeedMusic Prompt Blocks
### MUS-CUE-001｜CLIP-006｜错误时间 SeedMusic纯音乐提示词
- Related Clip(s): CLIP-006
```text
style:
instrumental only; no vocals, no lyrics, no choir, no humming, no vocalise

structure:
[Verse]: 3s
[Bridge]: 2s
```
## Review
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_music_package, path, True), 1)

    def test_music_plan_only_does_not_require_prompt_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "music-plan.md"
            path.write_text(
                """# MUSIC / SEED-MUSIC Score Package
## Module Routing Record
- Route: `MUSIC / SEED-MUSIC Score`
- Explicit Trigger Evidence: 只规划哪里配乐与哪里留白
- Requested Deliverable: Spotting Plan
- Generation Mode: `INSTRUMENTAL`
## Scope And Music Strategy
有效
## Spotting Map
MUSIC CUE；SILENCE / PRODUCTION SOUND ONLY
## Music Bible / Motif Map
有效
## Cue Sheet
MUS-CUE-001
## SeedMusic Prompt Blocks
本轮不生成提示词。
## Review
有效
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_music_package, path, True), 0)

    def test_state08_generic_sound_placeholder_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：10秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            fields = make_shot_fields(sound="有效内容")
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_duration_must_match_confirmed_clip_plan(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            prompt = root / "prompt.md"
            clip_plan = root / "clip.md"
            clip_plan.write_text(
                """# Clip Plan
## Clip Table
| Clip ID | 来源分镜（逐项列出） | 目标时长 | 生成方式 |
|---|---|---:|---|
| CLIP-001 | 分镜1 | 10秒 | 单镜 |
## Clip Detail Cards
""",
                encoding="utf-8",
            )
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：9秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.GLOBAL_SECTIONS
            )
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            prompt.write_text(f"{global_text}\n【分镜1】\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, prompt, True, clip_plan), 1)

    def test_visual_blocking_sketch_clip_prompt_gate_is_installed(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        files = {
            relative: (skill_root / relative).read_text(encoding="utf-8")
            for relative in (
                "knowledge/clip_preflight_check.md",
                "knowledge/spatial_blocking_layer.md",
                "knowledge/reference_budget.md",
                "references/ref_sketch_master.md",
                "rules/04_consistency_rules.md",
                "workflows/10_clip_production_workflow.md",
                "workflows/11_video_generation_workflow.md",
                "templates/10_video_prompt.md",
                "references/regression_scenarios.md",
            )
        }
        preflight = files["knowledge/clip_preflight_check.md"]
        for marker in (
            "Visual Blocking Risk Pre-Assessment",
            "Before-Single-Clip-Prompt Gate",
            "Final = NONE",
            "Final = REQUIRED",
            "S-SKETCH / Spatial Sketch",
            "P-SKETCH / Pose Sketch",
            "A-SKETCH / Action Sketch",
            "Sketch Validation Gate And Reference Authority",
            "Sketch Persistence / Blocking Canon",
            "Visual Anchor State / Blocking Signature",
            "KEEP existing sketch",
            "REPLACE with REF-SKETCH-XX-v2",
            "RETIRE sketch",
            "CREATE new sketch",
            "REF-SKETCH-MASTER",
            "Sketch Presentation Authority",
            "Master Template carries sketch language; Current Clip data carries blocking content.",
            "Technical Director Blocking Sheet",
            "Template Content Leakage Check",
            "Character Appearance Leakage Check",
            "FAIL = Character Appearance Leakage / Identity Contamination",
            "Text Contract Fallback",
        ):
            self.assertIn(marker, preflight)
        master = files["references/ref_sketch_master.md"]
        for marker in (
            "Asset Status：`REGISTERED`",
            "Persistent Asset Path：`assets/ref_sketch_master.png`",
            "REF-SKETCH-MASTER",
            "Sketch Presentation Authority",
            "Neutral Mannequin Representation Rule",
            "Template Content Leakage Check",
            "Character Appearance Leakage Check",
            "REF-SKETCH-XX",
        ):
            self.assertIn(marker, master)
        spatial = files["knowledge/spatial_blocking_layer.md"]
        self.assertIn(
            "Position → Torso Orientation → Shoulder Orientation → Head Orientation → Gaze Direction",
            spatial,
        )
        self.assertIn("Side-by-side → Face-to-face", spatial)
        self.assertIn("Previous Blocking State + Current Shot Delta = Current Blocking State", spatial)
        self.assertIn("Visual Blocking Authority", files["rules/04_consistency_rules.md"])
        self.assertIn("REF-SKETCH", files["templates/10_video_prompt.md"])
        self.assertIn("普通Prompt Rewrite", files["workflows/11_video_generation_workflow.md"])
        self.assertIn("Final Assessment=`REQUIRED`", files["knowledge/reference_budget.md"])
        regression = files["references/regression_scenarios.md"]
        for marker in (
            "R19-A CLIP-04 First Prompt Requires One Confirmed S+P Anchor",
            "R19-B Prompt Rewrite Reuses Anchor; Blocking Reconstruction Reassesses",
            "R19-C Simple Single Person Is NONE",
            "R19-D A3 Action May Use A-SKETCH Or Combined Anchor",
            "R20-A Piano Pair Uses Technical Blocking Sheet Language",
            "R20-B Three People Around A Table Has No Template Content Leakage",
            "R20-C A3 Action Remains Technical Previs",
            "R20-D Simple Head Turn Still Returns NONE",
            "R20-E Prompt Rewrite Reuses Current Sketch Without Recalling Master",
            "R20-F Character Appearance Leakage Is A Hard Failure",
        ):
            self.assertIn(marker, regression)
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)

    def test_ref_sketch_master_registration_requires_a_real_asset(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "sd"
            shutil.copytree(skill_root, copied)
            asset_path = copied / "assets" / "ref_sketch_master.png"
            asset_path.unlink()
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 1)

            shutil.copy2(skill_root / "assets" / "ref_sketch_master.png", asset_path)
            self.assertEqual(run_quiet(validator.validate_skill, copied, True), 0)

    def test_visual_blocking_layout_gate_passes_technical_sheet_and_rejects_storyboard_drift(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            candidate = temp_root / "candidate.png"
            shutil.copy2(skill_root / "assets" / "ref_sketch_master.png", candidate)
            evidence = {
                "schema_version": 1,
                "clip_id": "CLIP-004",
                "assessment": "REQUIRED",
                "route": "TECHNICAL_VISUAL_BLOCKING_SKETCH",
                "generator_template": "templates/23_visual_blocking_sketch_prompt.md",
                "sketch_type": "S+P",
                "master_input_mode": "VISUAL_REFERENCE",
                "master_asset_path": "assets/ref_sketch_master.png",
                "image_path": str(candidate),
                "blocking_signature": "Characters=A,B; Topology=Side-by-side; Shared Facing=Forward; Same Seat; Gaze Delta=B to A",
                "spatial_top_down_required": True,
                "layout": {
                    "main_blocking_panel": True,
                    "character_role_labels": True,
                    "direction_gaze_movement_annotation": True,
                    "spatial_top_down_diagram": True,
                    "camera_information": True,
                    "blocking_movement_notes_or_permission": True,
                    "usage_authority_note": True,
                },
                "artistic_storyboard_drift": False,
                "template_content_leakage": False,
                "neutral_mannequin_representation": True,
                "character_appearance_leakage": False,
                "blocking_match": True,
                "registration_status": "CONFIRMED",
            }
            evidence_path = temp_root / "evidence.json"
            evidence_path.write_text(json.dumps(evidence, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(
                run_quiet(validator.validate_ref_sketch_evidence, evidence_path, skill_root, True),
                0,
            )

            evidence["artistic_storyboard_drift"] = True
            evidence["layout"]["spatial_top_down_diagram"] = False
            evidence_path.write_text(json.dumps(evidence, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(
                run_quiet(validator.validate_ref_sketch_evidence, evidence_path, skill_root, True),
                1,
            )

            evidence["artistic_storyboard_drift"] = False
            evidence["layout"]["spatial_top_down_diagram"] = True
            evidence["character_appearance_leakage"] = True
            evidence_path.write_text(json.dumps(evidence, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(
                run_quiet(validator.validate_ref_sketch_evidence, evidence_path, skill_root, True),
                1,
            )

            evidence["character_appearance_leakage"] = False
            evidence["neutral_mannequin_representation"] = False
            evidence_path.write_text(json.dumps(evidence, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(
                run_quiet(validator.validate_ref_sketch_evidence, evidence_path, skill_root, True),
                1,
            )

    def test_visual_blocking_layout_gate_none_does_not_generate(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            evidence_path = Path(temp) / "none.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "clip_id": "CLIP-005",
                        "assessment": "NONE",
                        "route": "NONE",
                        "registration_status": "NONE",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                run_quiet(validator.validate_ref_sketch_evidence, evidence_path, skill_root, True),
                0,
            )

    def test_second_repeated_failure_requires_downgrade(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "execution_ledger.md"
            path.write_text(
                """# Execution Ledger

## Workflow Runs

None

## Generation Attempts

| Run ID | Prompt Revision | SHOT / UNIT | Attempt | Risk Level | Result | Failure Class | Stable Downgrade | Accepted Output | Review ID |
|---|---|---|---:|---|---|---|---|---|---|
| RUN-0001 | REV-0001 | SHOT-001 | 1 | L3 | FAIL | Camera / Focus Error | None | None | None |
| RUN-0002 | REV-0002 | SHOT-001 | 2 | L3 | FAIL | Camera / Focus Error | None | None | None |

## Open Recovery Items

None
""",
                encoding="utf-8",
            )
            self.assertEqual(run_quiet(validator.validate_execution_ledger, path, True), 1)

    def test_director_module_camera_language_end_to_end_contract(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]

        def source(relative: str) -> str:
            return (skill_root / relative).read_text(encoding="utf-8-sig")

        director = source("knowledge/director_decision_layer.md")
        for marker in (
            "Director Module / Director Intelligence Layer",
            "DIRECTOR INTENT PACKET",
            "Project-level",
            "Scene-level",
            "Shot-level",
            "Clip-level",
            "Task Dominance Router",
            "Camera Movement Trigger",
            "Dramatic Execution Unit",
            "Director-to-Prompt Boundary",
            "Director's Cut Review",
        ):
            self.assertIn(marker, director)

        camera = source("knowledge/camera_language/index.md")
        for marker in (
            "Camera Language Module",
            "Composition Direction",
            "Camera Movement Direction",
            "Lens / Distance Direction",
            "Shot Rhythm Direction",
            "Cross-stage Mapping",
            "Camera Movement Trigger",
        ):
            self.assertIn(marker, camera)

        workflow_markers = {
            "workflows/01_project_setup_workflow.md": ("Project Director Baseline",),
            "workflows/02_script_analysis_workflow.md": (
                "Screenwriter Module Continuity", "Writer → Director Boundary",
            ),
            "workflows/03_asset_discovery_workflow.md": ("Director-led Asset Function Pass",),
            "workflows/04_character_asset_workflow.md": ("Director-led Character Presence Pass",),
            "workflows/05_environment_asset_workflow.md": ("Director-led Environment Function Pass",),
            "workflows/06_prop_asset_workflow.md": ("Director-led Prop Function Pass",),
            "workflows/07_visual_development_workflow.md": (
                "Visual Dramaturgy / Mise-en-scène", "Visual Arc",
            ),
            "workflows/08_scene_breakdown_workflow.md": (
                "Writer Beat Map And Director Dramatic Geography", "Scene Camera Strategy",
            ),
            "workflows/09_shot_design_workflow.md": (
                "如果删掉这个SHOT，观众会损失什么", "Camera Movement Trigger",
            ),
            "workflows/10_clip_production_workflow.md": (
                "Dramatic Execution Unit", "Clip Camera Continuity / Visual Rhythm",
            ),
            "workflows/11_video_generation_workflow.md": (
                "Director-to-Prompt Translation Pass", "Writer + Director Intent Preservation QA",
            ),
            "workflows/12_editing_workflow.md": ("Editorial Decision Pass",),
            "workflows/13_review_workflow.md": (
                "Technical Review", "Director's Cut Review",
                "KEEP", "RE-EDIT", "REGENERATE", "REDIRECT",
            ),
        }
        for relative, markers in workflow_markers.items():
            workflow = source(relative)
            for marker in markers:
                self.assertIn(marker, workflow, relative)

        translation = source("knowledge/prompt_compilation/state08_projection.md")
        for marker in (
            "Dramatic Priority Extraction", "Audience Attention Hierarchy",
            "Performance Beat Translation", "Composition Function Translation",
            "Camera Motivation Translation", "Information Timing Translation",
            "Spatial & Relationship Translation", "Rhythm Translation",
            "Sound Function Translation", "Prompt Compression", "Writer + Director Intent Preservation QA",
            "共同朝前", "gaze泄漏",
        ):
            self.assertIn(marker, translation)

        regressions = source("references/regression_scenarios.md")
        scenario_evidence = {
            "A": ("Rainy-night Two-woman Reunion", "Audience Experience", "不出现Shot List"),
            "B": ("Visual Development", "Visual Dramaturgy / Mise-en-scène", "Visual Arc"),
            "C": ("40-second Two-person Scene", "Scene Camera Strategy", "没有创建SHOT / CLIP"),
            "D": ("Glance Beat", "Audience Attention", "Trigger / Stop"),
            "E": ("Suspicion To Confirmation", "Dramatic Execution Unit", "Camera Continuity / Visual Rhythm"),
            "F": ("Piano Pair", "gaze-only leakage", "不输出Director理论"),
            "G": ("Action-dominant Wuxia Clip", "Action PREVIS A3", "空间可读性"),
            "H": ("Technically Correct, Dramatically Early", "Director's Cut Review", "绝不Disposition=`KEEP`"),
            "I": ("Continue Is Not Reload", "不触发全量Runtime Reload", "Shot-State Memory"),
            "J": ("Three Shots Have Three Functions", "建立、隐藏/泄漏、确认", "慢推+浅景深"),
        }
        scenario_starts = {
            letter: regressions.index(f"### R23-{letter}") for letter in "ABCDEFGHIJ"
        }
        for index, letter in enumerate("ABCDEFGHIJ"):
            end = (
                scenario_starts["ABCDEFGHIJ"[index + 1]]
                if index + 1 < 10
                else regressions.index("## Deterministic Expectations")
            )
            scenario = regressions[scenario_starts[letter]:end]
            self.assertIn("输入：", scenario, letter)
            self.assertIn("PASS：", scenario, letter)
            self.assertIn("FAIL：", scenario, letter)
            for marker in scenario_evidence[letter]:
                self.assertIn(marker, scenario, letter)

        final_template = source("templates/10_video_prompt.md")
        self.assertIn("# CLIP-X｜标题 Seedance视频提示词", final_template)
        self.assertIn("音色特征：", final_template)
        self.assertIn("条件字段", final_template)
        for leaked_internal_field in (
            "DIRECTOR INTENT PACKET：", "Task Dominance：",
            "Director-to-Prompt Translation Pass：", "Scene Camera Strategy：",
        ):
            self.assertNotIn(leaked_internal_field, final_template)

        self.assertEqual(run_quiet(validator.validate_skill, skill_root, True), 0)


if __name__ == "__main__":
    unittest.main()
