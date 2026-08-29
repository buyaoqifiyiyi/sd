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
        return "参考资产：CHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。"
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
    include_voice: bool = True,
) -> str:
    previous_token = f"[G{package_number - 1:02d}尾帧]"
    if reference is None:
        reference = "CHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。"
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
    if "Voice Reference" in reference or "Audio Reference" in reference:
        sections.append("音色特征：由参考资产中的Voice/Audio Reference锁定声音身份；不以文字重新定义音高、声线、音域、共鸣、语速或音色质感。")
    else:
        sections.append("音色特征：无对白；本字段保留，听觉叙事由环境声、动作声与呼吸声承担。")
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
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, None, True), 0)

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
                    "CHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。\n"
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
                reference="CHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。",
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
                    "CHAR-001@v001角色资产；用途：锁定人物身份；禁止模型修改脸型、发型与服装。\n"
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

    def test_state08_voice_reference_keeps_fixed_voice_field(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(
                1,
                1,
                "1",
                "10",
                reference="Voice Reference：CHAR-001-VOICE-REF；用途：只锁定声音身份，不作为视觉参考；禁止模型修改声音身份。",
                include_voice=True,
            )
            ending = f"反向提示词：{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 0)

    def test_state08_voice_reference_rejects_voice_characteristics_section(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：10秒；Clip独立生成"
                if section == "【生成段】"
                else (
                    "【参考资产】\nAudio Reference：CHAR-001-VOICE-REF；只锁定声音身份，不作为视觉参考。"
                    if section == "【参考资产】"
                    else ("【音色特征】\n中低音、语速偏慢。" if section == validator.VOICE_SECTION else valid_global_section(section))
                )
                for section in validator.GLOBAL_SECTIONS
            )
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_voice_reference_rejects_voice_descriptor_in_dialogue(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：10秒；Clip独立生成"
                if section == "【生成段】"
                else (
                    "【参考资产】\nVoice Reference：CHAR-001-VOICE-REF；只锁定声音身份，不作为视觉参考。"
                    if section == "【参考资产】"
                    else valid_global_section(section)
                )
                for section in validator.BASE_GLOBAL_SECTIONS
            )
            fields = make_shot_fields().replace("台词：有效内容", "台词：角色以偏慢语速轻声说：‘你好。’")
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{fields}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

    def test_state08_without_voice_reference_requires_voice_characteristics(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = "\n".join(
                "【生成段】\nG01；来源CLIP-001；包含分镜1；平台生成时长：10秒；Clip独立生成"
                if section == "【生成段】" else valid_global_section(section)
                for section in validator.BASE_GLOBAL_SECTIONS
            )
            ending = f"【结尾帧要求】\n保存为[G01尾帧]：稳定结束\n下一段用途：最终收束\n【反向提示词】\n{validator.DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            path.write_text(f"{global_text}\n【分镜1】\n{make_shot_fields()}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)

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

    def test_explicit_background_music_exception_is_clip_scoped(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "prompt.md"
            global_text = make_state08_global_sections(1, 1, "1", "10")
            sound = "环境底声：室内水声。同步前景声：脚步与衣料摩擦。背景音乐：用户明确要求的轻柔主题音乐。声音尾部：水声延续。"
            ending = "反向提示词：禁止换脸。"
            path.write_text(f"{global_text}\n分镜1\n{make_shot_fields(sound=sound)}\n{ending}", encoding="utf-8")
            self.assertEqual(run_quiet(validator.validate_state08, path, True), 1)
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, {1}), 0)
            self.assertEqual(run_quiet(validator.validate_state08, path, True, None, {2}), 1)

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


if __name__ == "__main__":
    unittest.main()
