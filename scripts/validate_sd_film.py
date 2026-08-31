#!/usr/bin/env python3
"""Deterministic structural checks for SD Film projects and STATE-08 prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


PROJECT_FILES = ("project_manifest.json", "project_status.md", "project_bible.md", "asset_registry.md")
PROJECT_LEDGER_FILES = ("execution_ledger.md", "artifact_registry.md")
STATUS_FIELDS = (
    "Status Schema Version",
    "Project ID",
    "Project Name",
    "Current State",
    "State Status",
    "Script Status",
    "Active Workflow",
    "Last Completed Step",
    "Last Successful Checkpoint",
    "Next Workflow",
    "Return Route",
    "Pending Decision",
    "Revision ID",
    "Updated At",
)
STATUS_SECTIONS = (
    "State Control",
    "Completed Tasks",
    "Pending Tasks",
    "Active Artifacts",
    "Confirmed Assets",
    "Visual Direction Lock",
    "Continuity And Open Risks",
    "Review Control",
    "Version History",
)
PORTABLE_FIELDS = (
    "State Routing Contract Version",
    "Portable State Availability",
    "State Source Mode",
    "Canonical Project Root",
    "Portable Snapshot Of",
    "Portable Sync Status",
    "Completed States",
    "State Source",
    "Last Updated",
)
REVIEW_SECTIONS = (
    "Review Identity",
    "Overall Result",
    "Affected IDs",
    "Shot-Level QA",
    "Adjacent-Shot Continuity QA",
    "Problems And Corrective Actions",
    "Return Control",
    "Completion Decision",
)
VOICE_SECTION = "音色特征："
VISUAL_PRODUCTION_STATUSES = ("Prompt Draft", "Prompt Confirmed", "Image Generated", "Asset Confirmed")
SCRIPT_STATUSES = ("Source Material", "Adaptation Draft", "Optimized Proposal", "Production-Locked")
BASE_GLOBAL_SECTIONS = (
    "时长：",
    "画幅：",
    "参考资产：",
    "首帧参考：",
    "尾帧限制：",
    "主风格：",
    "人物一致性：",
    "环境一致性：",
)
GLOBAL_SECTIONS = BASE_GLOBAL_SECTIONS + (VOICE_SECTION,)
ENDING_SECTIONS = ("反向提示词：",)
SHOT_FIELDS = ("景别：", "镜头/机位：", "起始状态：", "画面描述：", "人物动作与情绪：", "空间关系：", "道具状态：", "台词：", "音效：", "镜头结尾状态：")
DIRECTOR_SECTIONS = ("Knowledge Role", "Core Identity", "Narrative Tone", "Emotional Grammar", "Composition", "Camera Movement", "Lens Tendencies", "Lighting", "Color Palette", "Production Design", "Character Blocking", "Performance Direction", "Editing Rhythm", "Sound Design", "Weather / Atmosphere", "Best Use Cases", "Avoid / Misuse", "Style Translation Rules", "Seedance Execution Language", "Combination Rules", "Final Principle")
SEQUENCE_SECTIONS = ("# Sequence Plan", "## Narrative Contract", "## Scene Scope", "## Beat Map", "## Coverage Matrix", "## Generation Units", "## State Ledger", "## Handoff And Risk", "## Completion Check")
CLIP_SECTIONS = ("# Clip Plan", "## Clip Table", "## Clip Detail Cards", "## Cross-Clip Continuity Ledger", "## Knowledge Projection Ledger", "## Coverage And Validation")
SHOT_PLAN_SECTIONS = ("# Shot Execution Plan", "## Shot Order Table", "## Shot Execution Cards", "## Adjacent-Shot Continuity Ledger", "## Coverage And Validation")
CLIP_DETAIL_FIELDS = (
    "包含 Shot：",
    "目标时长：",
    "时长核算：",
    "组织理由：",
    "生成合同：",
    "起始状态：",
    "连续动作：",
    "摄影机与构图路径：",
    "空间关系：",
    "道具连续性：",
    "光影/色彩/FX连续性：",
    "声音连续：",
    "结尾状态：",
    "结尾帧限制：",
    "尾帧用途判定：",
    "下一Clip Handoff：",
    "模型执行风险与安全降级：",
    "知识投影摘要：",
)

MUSIC_PATTERN = re.compile(
    r"背景音乐|配乐|BGM|主题音乐|氛围音乐|歌曲|电影配乐|原声带|节拍|无配乐|\bmusic\b|\bscore\b|\bsoundtrack\b",
    re.IGNORECASE,
)
DEFAULT_NO_BACKGROUND_MUSIC_LINE = "禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。"
SOUND_BED_PATTERN = re.compile(
    r"环境底声|空间底噪|房间底噪|环境声|城市底噪|交通底噪|人群底噪|机械底噪|风声|雨声|水声|虫鸣|鸟鸣|有意静默|近乎静默"
)
SOUND_FOREGROUND_PATTERN = re.compile(
    r"同步前景声|同步动作声|动作声|Foley|拟音|脚步|衣料|呼吸|对白|人声|道具声|剧情内声源|现场声|门声|金属声|玻璃声|车辆?声"
)
SOUND_PLACEHOLDER_PATTERN = re.compile(r"^(?:无|没有|无音效|静音|无声音|有效内容|待定|N/?A|None)[。.]?$", re.IGNORECASE)
VOICE_REFERENCE_PATTERN = re.compile(
    r"Voice\s*Audio\s*Reference|Audio\s*Reference|Voice\s*Reference|音色参考资产|角色音色参考|声音参考资产|人声参考资产|音频参考",
    re.IGNORECASE,
)
VOICE_DESCRIPTOR_PATTERN = re.compile(
    r"Voice\s*characteristics|\bpitch\b|\btimbre\b|\bresonance\b|vocal\s*weight|音高|声线|音域|共鸣|语速|音色质感",
    re.IGNORECASE,
)
REFERENCE_ITEM_PATTERN = re.compile(
    r"(?:CHAR|ENV|PROP|FX)-\d{3}(?:@v\d{3})?|G\d{2}尾帧|角色资产|环境资产|道具资产|FX资产|首帧(?:参考|资产)?|尾帧(?:参考|资产)?|Voice\s*Audio\s*Reference|Audio\s*Reference|Voice\s*Reference|音色参考资产|声音参考资产|音频参考",
    re.IGNORECASE,
)
REFERENCE_CONSTRAINT_PATTERN = re.compile(
    r"用途|锁定|约束|保持|禁止.{0,12}(?:修改|改变)|不得.{0,12}(?:修改|改变)|直接作为|连续性参考|不继承",
    re.IGNORECASE,
)
PSEUDO_VISUAL_REFERENCE_PATTERN = re.compile(
    r"(?:^|\n)\s*(?:\d+[.、]\s*)?[^\n]{0,40}(?:参考说明|文字说明)(?:\s*[｜|:]|[^\n]*用途)",
    re.IGNORECASE,
)
START_FRAME_SOURCE_PATTERN = re.compile(
    r"首帧|第一帧|起始帧|来源|继承|Reference-Only|Direct Start-Frame|Motivated Discontinuity|No Formal Tail Reference|从.{0,40}(?:建立|开始|继续)|Scene初始状态|场景初始状态|非连续继承|不继承|无法直接继承|待确认",
    re.IGNORECASE,
)
END_FRAME_STABLE_PATTERN = re.compile(r"稳定|低动作|停稳|静止|收束")
END_FRAME_INTERFACE_PATTERN = re.compile(r"可读|清楚|可继承|可续接|接口|直接承接|最终收束")
BOUNDARY_CLASS_PATTERN = re.compile(
    r"Continuous\s*Handoff|Motivated\s*Discontinuity|Unresolved\s*Handoff|连续继承|叙事断点|暂定未决|最终收束|本段末镜|无已知下一镜",
    re.IGNORECASE,
)
HIGH_RISK_END_PATTERN = re.compile(r"高速运动|动作未完成|主体严重遮挡|构图不可读")
CONFIRMED_END_EXCEPTION_PATTERN = re.compile(r"剧情明确|剧情要求|上游确认|已确认例外")
POSTER_SECTIONS = (
    "# Poster Design Package",
    "## Poster Brief",
    "## Narrative Promise",
    "## Visual Motif",
    "## Composition System",
    "## Asset And Reference Policy",
    "## Color And Texture",
    "## Typography And Copy",
    "## Layered Production Plan",
    "## Base-Image Prompt",
    "## Typography / Layout Specification",
    "## Composite And Delivery Specification",
    "## Negative Constraints",
    "## Quality Check",
)
MODULE_FILES = (
    "rules/runtime_reload.md",
    "rules/state_source.md",
    "rules/chat_compatibility.md",
    "rules/progression_rules.md",
    "rules/activation_rules.md",
    "rules/completion_gate.md",
    "rules/compatibility_mapping.md",
    "rules/resource_loading.md",
    "knowledge/script_adaptation.md",
    "knowledge/adaptation/short_form_drama_adapter.md",
    "knowledge/fx/index.md",
    "knowledge/fx/physical_effects.md",
    "knowledge/fx/fx_continuity.md",
    "knowledge/performance/index.md",
    "knowledge/performance/micro_expression.md",
    "knowledge/performance/facial_action_language.md",
    "knowledge/performance/emotion_dynamics.md",
    "knowledge/performance/expression_patterns.md",
    "knowledge/performance/expression_image_source_coverage.md",
    "knowledge/performance/dialogue_performance.md",
    "knowledge/performance/group_reaction.md",
    "knowledge/sound_language/index.md",
    "knowledge/sound_language/dialogue_and_lipsync.md",
    "knowledge/sound_language/ambience_and_foley.md",
    "knowledge/sound_language/music_and_silence.md",
    "knowledge/sound_language/sound_continuity.md",
    "knowledge/music_score/index.md",
    "knowledge/music_score/spotting_and_silence.md",
    "knowledge/music_score/music_bible_and_cues.md",
    "knowledge/music_score/seedmusic_prompting.md",
    "workflows/music_router.md",
    "workflows/21_seed_music_score_workflow.md",
    "templates/22_seed_music_score.md",
    "knowledge/transitions/index.md",
    "knowledge/transitions/foundations.md",
    "knowledge/transitions/decision_engine.md",
    "knowledge/transitions/transition_patterns.md",
    "knowledge/transitions/transition_continuity.md",
    "knowledge/transitions/image_source_coverage.md",
    "workflows/15_fx_asset_workflow.md",
    "templates/13_fx_asset_prompt.md",
    "references/module_contracts.md",
    "knowledge/sequence/index.md",
    "knowledge/sequence/coverage_design.md",
    "knowledge/sequence/sequence_continuity.md",
    "knowledge/sequence/generation_unit_design.md",
    "workflows/16_sequence_planning_workflow.md",
    "templates/14_sequence_plan.md",
    "knowledge/clip_planning/index.md",
    "knowledge/clip_planning/foundations.md",
    "knowledge/clip_planning/decision_engine.md",
    "knowledge/clip_planning/continuity_and_projection.md",
    "workflows/10_clip_production_workflow.md",
    "templates/20_clip_plan.md",
    "knowledge/06_shot_execution_plan_rules.md",
    "workflows/10_shot_execution_plan_workflow.md",
    "templates/09_shot_execution_plan.md",
    "knowledge/camera_language/camera_movement/tilt.md",
    "knowledge/camera_language/camera_movement/selection_matrix.md",
    "knowledge/camera_language/camera_angle/dutch_angle.md",
    "knowledge/camera_language/perspective_language/over_shoulder.md",
    "knowledge/camera_language/director_patterns/index.md",
    "knowledge/camera_language/director_patterns/emotional_patterns.md",
    "knowledge/camera_language/director_patterns/dynamic_patterns.md",
    "knowledge/camera_language/image_source_coverage.md",
    "knowledge/camera_language/composition_language/foundations.md",
    "knowledge/camera_language/director_patterns/advanced_composition.md",
    "knowledge/camera_language/director_patterns/action_composition.md",
    "knowledge/camera_language/director_patterns/character_composition.md",
    "knowledge/camera_language/director_patterns/atmosphere_composition.md",
    "knowledge/camera_language/composition_image_source_coverage.md",
    "knowledge/camera_language/lens_language/focal_length_and_perspective.md",
    "knowledge/camera_language/lens_language/focal_length_patterns.md",
    "knowledge/camera_language/lens_language/focal_length_continuity.md",
    "knowledge/camera_language/lens_language/focal_length_image_source_coverage.md",
    "knowledge/camera_language/movement_combinations/index.md",
    "knowledge/camera_language/movement_combinations/foundations.md",
    "knowledge/camera_language/movement_combinations/decision_engine.md",
    "knowledge/camera_language/movement_combinations/combination_patterns.md",
    "knowledge/camera_language/movement_combinations/continuity_and_projection.md",
    "knowledge/camera_language/movement_combinations/image_source_coverage.md",
    "knowledge/prompt_compilation/index.md",
    "knowledge/prompt_compilation/state08_projection.md",
    "knowledge/lighting/index.md",
    "knowledge/lighting/foundations.md",
    "knowledge/lighting/source_patterns.md",
    "knowledge/lighting/lighting_continuity.md",
    "knowledge/lighting/image_source_coverage.md",
    "knowledge/color/index.md",
    "knowledge/color/foundations.md",
    "knowledge/color/tone_patterns.md",
    "knowledge/color/color_continuity.md",
    "knowledge/color/image_source_coverage.md",
    "knowledge/poster_design/index.md",
    "knowledge/poster_design/foundations.md",
    "knowledge/poster_design/composition_and_motif.md",
    "knowledge/poster_design/typography_and_layers.md",
    "knowledge/poster_design/reference_rights_and_qc.md",
    "knowledge/poster_design/genre_tendencies.md",
    "knowledge/poster_design/source_coverage.md",
    "workflows/17_poster_design_workflow.md",
    "templates/15_poster_design_package.md",
    "references/project_state_contract.md",
    "references/asset_lock_contract.md",
    "references/artifact_revision_contract.md",
    "knowledge/quality/index.md",
    "knowledge/quality/shot_qa.md",
    "knowledge/quality/continuity_pair_qa.md",
    "knowledge/quality/execution_risk.md",
    "knowledge/quality/prompt_scorecard.md",
    "knowledge/camera_language/shot_language_router.md",
    "knowledge/visual_styles/director_metadata_contract.md",
    "workflows/18_project_resume_workflow.md",
    "templates/16_review_report.md",
    "templates/17_execution_ledger.md",
    "templates/18_artifact_revision_ledger.md",
    "templates/19_series_status.md",
    "scripts/test_validate_sd_film.py",
    "references/regression_scenarios.md",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def extract_project_id(text: str) -> str | None:
    match = re.search(r"(?:项目\s*ID|Project\s*ID)\s*[：:]\s*`?([^`\s]+)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_label(text: str, label: str) -> str | None:
    match = re.search(rf"(?:^|\n)\s*[-*]?\s*{re.escape(label)}\s*[：:]\s*([^\n]+)", text, re.IGNORECASE)
    return match.group(1).strip().strip("`") if match else None


def report(errors: list[str], warnings: list[str], as_json: bool) -> int:
    payload = {"ok": not errors, "errors": errors, "warnings": warnings}
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print("PASS" if not errors else "FAIL")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARN: {item}")
    return 0 if not errors else 1


def resolve_state_source(active_project_root: Path | None, portable_path: Path | None) -> tuple[str, Path | None]:
    """Resolve the documented Chat/Work state-source priority by actual readability."""
    candidates: tuple[tuple[str, Path | None], ...] = (
        ("ACTIVE_PROJECT_ROOT", active_project_root / "project_status.md" if active_project_root else None),
        ("PORTABLE", portable_path),
    )
    for mode, path in candidates:
        if path is None or not path.is_file():
            continue
        try:
            read_text(path)
        except (OSError, UnicodeError):
            continue
        return mode, path
    return "INITIALIZE_STATE_00", None


def validate_project(root: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    root = root.resolve()
    if not root.is_dir():
        return report([f"Project root does not exist: {root}"], warnings, as_json)
    for name in PROJECT_FILES:
        if not (root / name).is_file():
            errors.append(f"Missing required project file: {name}")
    for name in PROJECT_LEDGER_FILES:
        if not (root / name).is_file():
            errors.append(f"Missing required project ledger: {name}")
    if errors:
        return report(errors, warnings, as_json)
    try:
        manifest = load_json(root / "project_manifest.json")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return report([f"Invalid project_manifest.json: {exc}"], warnings, as_json)
    if manifest.get("schema_version") != 1:
        errors.append("project_manifest.json schema_version must be 1")
    manifest_id = str(manifest.get("project_id", "")).strip()
    if not manifest_id:
        errors.append("project_manifest.json is missing project_id")
    for name in PROJECT_FILES[1:]:
        text = read_text(root / name)
        if "Legacy Project File Pointer" in text:
            errors.append(f"Project Root contains a compatibility pointer instead of project data: {name}")
        file_id = extract_project_id(text)
        if not file_id:
            errors.append(f"Cannot find Project ID in {name}")
        elif manifest_id and file_id != manifest_id:
            errors.append(f"Project ID mismatch in {name}: {file_id} != {manifest_id}")
    status_text = read_text(root / "project_status.md")
    state_match = re.search(r"\bSTATE-(\d{2})\b", status_text)
    if not state_match:
        errors.append("project_status.md does not contain a STATE-00 through STATE-09 value")
    elif not 0 <= int(state_match.group(1)) <= 9:
        errors.append(f"Invalid production state: STATE-{state_match.group(1)}")
    for field in STATUS_FIELDS:
        if extract_label(status_text, field) is None:
            errors.append(f"project_status.md missing state field: {field}")
    schema_version = extract_label(status_text, "Status Schema Version")
    if schema_version != "2":
        errors.append(f"project_status.md Status Schema Version must be 2: found {schema_version}")
    state_status = extract_label(status_text, "State Status")
    if state_status not in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "COMPLETE"}:
        errors.append(f"Invalid State Status: {state_status}")
    script_status = extract_label(status_text, "Script Status")
    if script_status not in SCRIPT_STATUSES:
        errors.append(f"Invalid Script Status: {script_status}")
    revision_id = extract_label(status_text, "Revision ID")
    if revision_id and not re.fullmatch(r"REV-\d{4}", revision_id):
        errors.append(f"Invalid Revision ID: {revision_id}")
    for section in STATUS_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", status_text, re.MULTILINE):
            errors.append(f"project_status.md missing section: {section}")
    pending_match = re.search(
        r"^##\s+Pending Tasks\s*$\n(.*?)(?=^##\s+|\Z)",
        status_text,
        re.MULTILINE | re.DOTALL,
    )
    if pending_match:
        pending_tasks = pending_match.group(1)
        legacy_pending_patterns = {
            "non-canonical STATE-06 label": r"(?im)^\s*-?\s*STATE-06\s+Shot Design\s*$",
            "fixed Storyboard stage": r"(?im)^\s*-?\s*(?:STATE-07\s+)?Storyboard\s*$",
            "non-canonical STATE-08 label": r"(?im)^\s*-?\s*STATE-08\s+Video Generation\s*$",
            "unnumbered Shot Design": r"(?im)^\s*-\s*Shot Design\s*$",
            "unnumbered Video Generation": r"(?im)^\s*-\s*Video Generation\s*$",
        }
        for label, pattern in legacy_pending_patterns.items():
            if re.search(pattern, pending_tasks):
                errors.append(f"project_status.md Pending Tasks contains legacy fixed route: {label}")
    active_workflow = extract_label(status_text, "Active Workflow")
    checkpoint = extract_label(status_text, "Last Successful Checkpoint")
    pending = extract_label(status_text, "Pending Decision")
    if state_status == "IN_PROGRESS" and (not active_workflow or active_workflow.lower() == "none"):
        errors.append("IN_PROGRESS project must have an Active Workflow")
    if state_status == "BLOCKED" and (not pending or pending.lower() == "none"):
        errors.append("BLOCKED project must have a Pending Decision")
    if state_status == "COMPLETE" and (not checkpoint or checkpoint.lower() == "none"):
        errors.append("COMPLETE state must have a Last Successful Checkpoint")
    review_result = extract_label(status_text, "Review Result")
    current_state = extract_label(status_text, "Current State")
    if current_state == "STATE-01" and state_status == "COMPLETE" and script_status != "Production-Locked":
        errors.append("STATE-01 COMPLETE requires Script Status: Production-Locked")
    if current_state and re.fullmatch(r"STATE-0[2-9]", current_state) and script_status != "Production-Locked":
        errors.append(f"{current_state} requires Script Status: Production-Locked")
    if current_state == "STATE-09" and review_result in {"REVISE", "REBUILD"} and state_status == "COMPLETE":
        errors.append("STATE-09 REVISE/REBUILD must not be COMPLETE")
    if current_state == "STATE-09" and review_result == "PASS" and state_status != "COMPLETE":
        errors.append("STATE-09 PASS must be COMPLETE")
    if not manifest.get("project_name"):
        warnings.append("project_manifest.json has no project_name")
    return report(errors, warnings, as_json)


def validate_portable_status(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    path = path.resolve()
    if not path.is_file():
        return report([f"Portable state does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    for field in PORTABLE_FIELDS + STATUS_FIELDS:
        if extract_label(text, field) is None:
            errors.append(f"portable_project_status.md missing field: {field}")
    for section in STATUS_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE):
            errors.append(f"portable_project_status.md missing section: {section}")
    current_state = extract_label(text, "Current State")
    if not current_state or not re.fullmatch(r"STATE-0[0-9]", current_state):
        errors.append(f"Invalid portable Current State: {current_state}")
    schema_version = extract_label(text, "Status Schema Version")
    if schema_version != "2":
        errors.append(f"portable_project_status.md Status Schema Version must be 2: found {schema_version}")
    routing_version = extract_label(text, "State Routing Contract Version")
    if routing_version != "1":
        errors.append(f"portable_project_status.md State Routing Contract Version must be 1: found {routing_version}")
    project_id = extract_label(text, "Project ID")
    if not project_id or not re.fullmatch(r"PROJECT-[A-Z0-9-]+", project_id):
        errors.append(f"Invalid portable Project ID: {project_id}")
    state_status = extract_label(text, "State Status")
    if state_status not in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "COMPLETE"}:
        errors.append(f"Invalid portable State Status: {state_status}")
    script_status = extract_label(text, "Script Status")
    if script_status not in SCRIPT_STATUSES:
        errors.append(f"Invalid portable Script Status: {script_status}")
    if current_state == "STATE-01" and state_status == "COMPLETE" and script_status != "Production-Locked":
        errors.append("Portable STATE-01 COMPLETE requires Script Status: Production-Locked")
    if current_state and re.fullmatch(r"STATE-0[2-9]", current_state) and script_status != "Production-Locked":
        errors.append(f"Portable {current_state} requires Script Status: Production-Locked")
    revision_id = extract_label(text, "Revision ID")
    if not revision_id or not re.fullmatch(r"REV-\d{4}", revision_id):
        errors.append(f"Invalid portable Revision ID: {revision_id}")
    availability = extract_label(text, "Portable State Availability")
    if availability not in {"EMPTY", "READY"}:
        errors.append(f"Invalid Portable State Availability: {availability}")
    sync_status = extract_label(text, "Portable Sync Status")
    if sync_status not in {"SYNCED", "PORTABLE_ONLY", "PENDING"}:
        errors.append(f"Invalid Portable Sync Status: {sync_status}")
    source_mode = extract_label(text, "State Source Mode")
    if source_mode != "PORTABLE":
        errors.append(f"Invalid State Source Mode: {source_mode}")
    active_workflow = extract_label(text, "Active Workflow")
    if active_workflow and active_workflow.lower() != "none" and not re.fullmatch(r"[0-9]{2}_[a-z0-9_]+\.md", active_workflow):
        errors.append(f"Portable Active Workflow must be a workflow filename: {active_workflow}")
    next_workflow = extract_label(text, "Next Workflow")
    if next_workflow not in {"Project Complete / Post", "None"} and (
        not next_workflow or not re.fullmatch(r"[0-9]{2}_[a-z0-9_]+\.md", next_workflow)
    ):
        errors.append(f"Portable Next Workflow must be a workflow filename: {next_workflow}")
    for marker in ("Selected State Source", "Source Selection Reason", "Portable Update Rule"):
        if marker not in text:
            errors.append(f"portable_project_status.md missing routing marker: {marker}")
    return report(errors, warnings, as_json)


def validate_state_routing(root: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    root = root.resolve()
    routing_markers = {
        "SKILL.md": ("STATE-00", "STATE-07 Clip Production", "STATE-08 Clip-based Video Prompt / Video Generation", "rules/state_source.md"),
        "config.md": ("Portable Baseline", "rules/state_source.md", "references/project_state_contract.md"),
        "rules/runtime_reload.md": ("Skill Version", "Build ID", "rules/state_source.md"),
        "rules/state_source.md": ("portable_project_status.md", "Active Project Root", "STATE-00"),
        "rules/chat_compatibility.md": ("portable_project_status.md", "Active Project Root", "STATE-00"),
        "rules/compatibility_mapping.md": ("STATE-07 Clip Production", "STATE-08 Clip-based Video Prompt / Video Generation", "Storyboard"),
        "references/project_workspace.md": ("portable_project_status.md", "Active Project Root", "STATE-00"),
        "references/project_state_contract.md": ("Canonical Portable State Schema", "portable_project_status.md", "STATE-00"),
        "rules/01_pipeline_rules.md": ("rules/state_source.md", "references/project_workspace.md", "rules/chat_compatibility.md"),
        "workflows/01_project_setup_workflow.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
        "workflows/workflow_map.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
        "workflows/18_project_resume_workflow.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
    }
    for relative, required_markers in routing_markers.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing state-routing file: {relative}")
            continue
        text = read_text(path)
        for marker in required_markers:
            if marker not in text:
                errors.append(f"{relative} missing state-routing marker: {marker}")

    # Meaningful ownership checks: marker presence alone does not prove that a
    # global rule still has one owner or that callers preserve its routing.
    markdown_paths: list[Path] = []
    for relative in (
        "SKILL.md",
        "config.md",
        "project_status.md",
        "portable_project_status.md",
        "project_bible.md",
        "asset_registry.md",
    ):
        candidate = root / relative
        if candidate.is_file():
            markdown_paths.append(candidate)
    for directory in ("rules", "workflows", "knowledge", "templates", "references"):
        base = root / directory
        if base.is_dir():
            markdown_paths.extend(base.rglob("*.md"))

    state_source_owner = "rules/state_source.md"
    state_source_example = "references/regression_scenarios.md"
    competing_priority = re.compile(
        r"(?:可访问且Project ID一致的)?Active Project Root/project_status\.md\s*(?:>|→)\s*(?:有效的)?portable_project_status\.md"
    )
    competing_heading = re.compile(r"^##\s+State Source (?:Selection|Authority)\s*$", re.MULTILINE)
    for path in markdown_paths:
        relative = path.relative_to(root).as_posix()
        if relative in {state_source_owner, state_source_example}:
            continue
        text = read_text(path)
        if competing_priority.search(text) or competing_heading.search(text):
            errors.append(
                f"Competing State Source selection rules found in {relative}; "
                f"selection priority is owned only by {state_source_owner}"
            )

    skill_text = read_text(root / "SKILL.md") if (root / "SKILL.md").is_file() else ""
    activation_path = root / "rules" / "activation_rules.md"
    activation_text = read_text(activation_path) if activation_path.is_file() else ""
    audio_router_path = root / "workflows" / "audio_router.md"
    audio_router_text = read_text(audio_router_path) if audio_router_path.is_file() else ""
    voice_workflow_path = root / "workflows" / "20_seed_audio_voice_asset_workflow.md"
    voice_workflow_text = read_text(voice_workflow_path) if voice_workflow_path.is_file() else ""
    audio_invariants = (
        ("SKILL.md", skill_text, "| 用户显式请求声音身份资产 | `workflows/audio_router.md` |"),
        ("rules/activation_rules.md", activation_text, "唯一Router `workflows/audio_router.md`"),
        ("rules/activation_rules.md", activation_text, "ROUTE: AUDIO / SEED-AUDIO Voice Asset"),
        ("workflows/audio_router.md", audio_router_text, "ROUTE: ORIGINAL WORKFLOW"),
        ("workflows/20_seed_audio_voice_asset_workflow.md", voice_workflow_text, "唯一Router：`workflows/audio_router.md`"),
        ("workflows/20_seed_audio_voice_asset_workflow.md", voice_workflow_text, "ROUTE: AUDIO / SEED-AUDIO Voice Asset"),
    )
    for relative, text, marker in audio_invariants:
        if marker not in text:
            errors.append(f"AUDIO unique-router invariant missing in {relative}: {marker}")
    direct_audio_call = re.compile(r"调用.*workflows/20_seed_audio_voice_asset_workflow\.md")
    for path in markdown_paths:
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(read_text(path).splitlines(), start=1):
            if direct_audio_call.search(line) and not (
                "workflows/audio_router.md" in line and ("AUDIO Route" in line or "ROUTE: AUDIO" in line)
            ):
                errors.append(
                    f"Direct AUDIO workflow call bypasses the unique router: {relative}:{line_number}"
                )

    runtime_path = root / "rules" / "runtime_reload.md"
    runtime_text = read_text(runtime_path) if runtime_path.is_file() else ""
    for trigger in ("调用SD", "调用sd", "重新调用SD", "重新加载SD", "按当前Skill继续"):
        if trigger not in skill_text or trigger not in runtime_text:
            errors.append(f"Runtime Reload trigger is not discoverable in both SKILL.md and runtime_reload.md: {trigger}")
    for marker in ("RELOADED", "UNAVAILABLE", "禁止报告`RELOADED`", "实际重新读取权威`SKILL.md`"):
        if marker not in runtime_text:
            errors.append(f"runtime_reload.md missing truthful Reload Status invariant: {marker}")
    if "只有实际重读权威入口并取得版本字段才可报告`RELOADED`" not in skill_text:
        errors.append("SKILL.md Runtime Reload Entry does not prevent false RELOADED status")

    state_contract = root / "references" / "project_state_contract.md"
    state_contract_text = read_text(state_contract) if state_contract.is_file() else ""
    completion_path = root / "rules" / "completion_gate.md"
    completion_text = read_text(completion_path) if completion_path.is_file() else ""
    if "## State Transition Protocol" in state_contract_text:
        errors.append("project_state_contract.md competes with completion_gate.md for transition decisions")
    for marker in ("## State Mutation And Writeback Protocol", "### Apply ENTER Decision", "### Apply COMPLETE Decision"):
        if marker not in state_contract_text:
            errors.append(f"project_state_contract.md missing deterministic mutation contract: {marker}")
    for marker in ("## Transition Decisions", "references/project_state_contract.md", "本规则只决定允许哪一种Transition Decision"):
        if marker not in completion_text:
            errors.append(f"completion_gate.md missing decision-owner invariant: {marker}")

    # A complete user-facing STATE-08 field skeleton may only live in its
    # Template. Other modules may name fields for semantics, but not reproduce
    # the ordered schema as headings.
    state08_schema_headings = ("### 时长：", "### 画幅：", "### 参考资产：", "### 首帧参考：", "### 尾帧限制：")
    for path in markdown_paths:
        relative = path.relative_to(root).as_posix()
        if relative == "templates/10_video_prompt.md":
            continue
        text = read_text(path)
        if all(marker in text for marker in state08_schema_headings):
            errors.append(
                f"Competing STATE-08 final field skeleton found in {relative}; "
                "templates/10_video_prompt.md is the only schema owner"
            )
    for marker in ("### Canonical Portable State Schema", "State Status: NOT_STARTED", "Next Workflow: 01_project_setup_workflow.md", "## State Control"):
        if marker not in state_contract_text:
            errors.append(f"project_state_contract.md missing canonical Portable schema marker: {marker}")
    state_writers = (
        "workflows/01_project_setup_workflow.md",
        "workflows/02_script_analysis_workflow.md",
        "workflows/03_asset_discovery_workflow.md",
        "workflows/04_character_asset_workflow.md",
        "workflows/05_environment_asset_workflow.md",
        "workflows/06_prop_asset_workflow.md",
        "workflows/07_visual_development_workflow.md",
        "workflows/08_scene_breakdown_workflow.md",
        "workflows/09_shot_design_workflow.md",
        "workflows/10_clip_production_workflow.md",
        "workflows/10_storyboard_workflow.md",
        "workflows/11_video_generation_workflow.md",
        "workflows/12_editing_workflow.md",
        "workflows/13_review_workflow.md",
        "workflows/14_series_management_workflow.md",
        "workflows/15_fx_asset_workflow.md",
        "workflows/16_sequence_planning_workflow.md",
        "workflows/17_poster_design_workflow.md",
        "workflows/18_project_resume_workflow.md",
    )
    for relative in state_writers:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing state writer: {relative}")
            continue
        text = read_text(path)
        if "Portable State" not in text and "portable_project_status.md" not in text:
            errors.append(f"State writer does not synchronize or output Portable State: {relative}")
    portable_path = root / "portable_project_status.md"
    if portable_path.is_file():
        portable_text = read_text(portable_path)
        for field in PORTABLE_FIELDS + STATUS_FIELDS:
            if extract_label(portable_text, field) is None:
                errors.append(f"portable_project_status.md missing field: {field}")
        for section in STATUS_SECTIONS:
            if not re.search(rf"^##\s+{re.escape(section)}\s*$", portable_text, re.MULTILINE):
                errors.append(f"portable_project_status.md missing section: {section}")
    else:
        errors.append("Missing state-routing file: portable_project_status.md")
    return report(errors, warnings, as_json)


def validate_registry(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        registry = load_json(path.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return report([f"Invalid registry: {exc}"], warnings, as_json)
    if registry.get("schema_version") != 1:
        errors.append("Registry schema_version must be 1")
    projects = registry.get("projects")
    if not isinstance(projects, list):
        return report(errors + ["Registry projects must be an array"], warnings, as_json)
    seen_ids: set[str] = set()
    seen_roots: set[str] = set()
    for index, item in enumerate(projects, start=1):
        if not isinstance(item, dict):
            errors.append(f"Registry item {index} must be an object")
            continue
        project_id = str(item.get("project_id", "")).strip()
        root_text = str(item.get("root", "")).strip()
        if not project_id:
            errors.append(f"Registry item {index} has no project_id")
        elif project_id in seen_ids:
            errors.append(f"Duplicate project_id in registry: {project_id}")
        seen_ids.add(project_id)
        if not root_text:
            errors.append(f"Registry item {index} has no root")
            continue
        normalized = str(Path(root_text).resolve()).casefold()
        if normalized in seen_roots:
            errors.append(f"Duplicate project root in registry: {root_text}")
        seen_roots.add(normalized)
        if not Path(root_text).is_dir():
            errors.append(f"Registered project root does not exist: {root_text}")
            continue
        manifest_path = Path(root_text) / "project_manifest.json"
        if not manifest_path.is_file():
            errors.append(f"Registered project has no project_manifest.json: {root_text}")
            continue
        try:
            manifest_id = str(load_json(manifest_path).get("project_id", "")).strip()
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid registered project manifest at {root_text}: {exc}")
            continue
        if project_id and manifest_id != project_id:
            errors.append(f"Registry/manifest Project ID mismatch at {root_text}: {project_id} != {manifest_id}")
    return report(errors, warnings, as_json)


def validate_state08(
    path: Path,
    as_json: bool = False,
    clip_plan_path: Path | None = None,
    allow_batch_output: bool = False,
) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    text = read_text(path.resolve())
    package_markers = list(re.finditer(r"^【CLIP标题】\s*$", text, re.MULTILINE))
    if not package_markers:
        errors.append("No independent 【CLIP标题】Gxx Clip Prompt Packages found")
    if len(package_markers) > 1 and not allow_batch_output:
        errors.append(
            "Default STATE-08 delivery is one Clip Prompt Package per checkpoint; multiple Packages require explicit batch authorization"
        )
    package_ids: list[int] = []
    clip_ids: list[int] = []
    shot_numbers: list[int] = []
    package_specs: list[tuple[int, int | None, float | None, list[int]]] = []
    for package_index, marker in enumerate(package_markers):
        package_end = package_markers[package_index + 1].start() if package_index + 1 < len(package_markers) else len(text)
        package = text[marker.start():package_end]
        id_match = re.search(r"^【CLIP标题】\s*\r?\n\s*G(\d{2})\b", package, re.MULTILINE)
        if not id_match:
            errors.append(f"Prompt Package {package_index + 1} must start with a Gxx value immediately after 【CLIP标题】")
            package_number = package_index + 1
        else:
            package_number = int(id_match.group(1))
            package_ids.append(package_number)

        title_end = package.find("【时长】")
        title_text = package[:title_end] if title_end >= 0 else package
        duration_start = package.find("【时长】")
        duration_end = package.find("【画幅】", duration_start + 1)
        duration_text = package[duration_start:duration_end] if duration_start >= 0 and duration_end > duration_start else ""
        clip_number_value: int | None = None
        clip_matches = re.findall(r"来源\s*(?:Clip|CLIP)[-：:]?\s*(\d{3})", title_text, re.IGNORECASE)
        if len(clip_matches) != 1:
            errors.append(f"G{package_number:02d} 【CLIP标题】 must contain exactly one 来源CLIP-xxx")
        else:
            clip_number = int(clip_matches[0])
            clip_number_value = clip_number
            clip_ids.append(clip_number)
            if clip_number != package_number:
                errors.append(f"G{package_number:02d} must map to CLIP-{package_number:03d}, found CLIP-{clip_number:03d}")
        duration_value: float | None = None
        duration_matches = re.findall(r"平台生成时长\s*[：:]\s*(\d+(?:\.\d+)?)\s*秒", duration_text)
        if len(duration_matches) != 1:
            errors.append(f"G{package_number:02d} 【时长】 must contain exactly one 平台生成时长：N秒")
        else:
            duration = float(duration_matches[0])
            duration_value = duration
            if duration < 4 or duration > 15:
                errors.append(f"G{package_number:02d} platform duration must be 4-15 seconds: found {duration:g}")
        if "标题" not in title_text:
            errors.append(f"G{package_number:02d} 【CLIP标题】 must include a human-readable 标题")
        if "包含分镜" not in title_text:
            errors.append(f"G{package_number:02d} 【CLIP标题】 must list 包含分镜")
        listed_shot_match = re.search(r"包含分镜\s*([0-9分镜、,，\s]+)", title_text)
        listed_shots = [int(value) for value in re.findall(r"\d+", listed_shot_match.group(1))] if listed_shot_match else []

        reference_start = package.find("【参考资产】")
        reference_end = package.find("【首帧参考】", reference_start + 1)
        reference_text = package[reference_start:reference_end] if reference_start >= 0 and reference_end > reference_start else ""
        reference_body = reference_text[len("【参考资产】"):].strip() if reference_text.startswith("【参考资产】") else ""
        first_frame_start = package.find("【首帧参考】")
        first_frame_end = package.find("【尾帧限制】", first_frame_start + 1)
        first_frame_text = package[first_frame_start:first_frame_end] if first_frame_start >= 0 and first_frame_end > first_frame_start else ""
        tail_start = package.find("【尾帧限制】")
        tail_end = package.find("【主风格】", tail_start + 1)
        tail_text = package[tail_start + len("【尾帧限制】"):tail_end] if tail_start >= 0 and tail_end > tail_start else ""
        has_voice_reference = bool(VOICE_REFERENCE_PATTERN.search(reference_text))

        cursor = -1
        required_global_sections = BASE_GLOBAL_SECTIONS + (() if has_voice_reference else (VOICE_SECTION,))
        for section in required_global_sections + ENDING_SECTIONS:
            matches = list(re.finditer(rf"^{re.escape(section)}\s*$", package, re.MULTILINE))
            if not matches:
                errors.append(f"G{package_number:02d} missing section: {section}")
                continue
            if len(matches) > 1:
                errors.append(f"G{package_number:02d} duplicate section: {section}")
            position = matches[0].start()
            if position < cursor:
                errors.append(f"G{package_number:02d} section out of order: {section}")
            else:
                cursor = position

        first_shot_position = package.find("【分镜")
        negative_position = package.find("【反向提示词】")
        style_position = package.find("【主风格】")
        for front_section in ("【参考资产】", "【首帧参考】", "【尾帧限制】"):
            front_position = package.find(front_section)
            if front_position >= 0 and style_position >= 0 and front_position > style_position:
                errors.append(f"G{package_number:02d} {front_section} must appear before 【主风格】")
        if first_shot_position >= 0 and negative_position >= 0 and first_shot_position > negative_position:
            errors.append(f"G{package_number:02d} 【反向提示词】 must appear after all 【分镜X】 sections")

        voice_section_matches = list(re.finditer(rf"^{re.escape(VOICE_SECTION)}\s*$", package, re.MULTILINE))
        if has_voice_reference and voice_section_matches:
            errors.append(f"G{package_number:02d} must omit {VOICE_SECTION} when a Voice/Audio Reference is provided")
        if has_voice_reference:
            package_without_reference = package[:reference_start] + package[reference_end:]
            descriptor_match = VOICE_DESCRIPTOR_PATTERN.search(package_without_reference)
            if descriptor_match:
                errors.append(
                    f"G{package_number:02d} contains forbidden textual voice redefinition while using a Voice/Audio Reference: "
                    f"{descriptor_match.group(0)}"
                )
        if re.search(
            r"Storyboard|故事板|分镜板|线稿|漫画格|接触表|联系表|拼图|多画面|多宫格|Shot\s*Execution\s*Plan\s*(?:截图|渲染)|分镜执行表\s*(?:截图|渲染)",
            reference_text,
            re.IGNORECASE,
        ):
            errors.append(
                f"G{package_number:02d} 【参考资产】 contains forbidden Storyboard, multi-panel, line-art, or Shot Execution Plan visual material"
            )
        if not reference_body or SOUND_PLACEHOLDER_PATTERN.fullmatch(reference_body) or reference_body in {"有效内容", "同上"}:
            errors.append(f"G{package_number:02d} 【参考资产】 must explicitly list the references used by this Clip")
        else:
            if not REFERENCE_ITEM_PATTERN.search(reference_body):
                errors.append(
                    f"G{package_number:02d} 【参考资产】 must name at least one Canonical asset, legal frame, or Voice/Audio Reference"
                )
            if not REFERENCE_CONSTRAINT_PATTERN.search(reference_body):
                errors.append(
                    f"G{package_number:02d} 【参考资产】 must state each reference's purpose or locking constraint"
                )

        if not first_frame_text:
            errors.append(f"G{package_number:02d} missing or empty section: 【首帧参考】")
        else:
            first_frame_requirements = {
                "人物位置/朝向/视线": r"人物|角色|秦始皇|侍从|位置|朝向|视线",
                "摄影机起始位置": r"摄影机|镜头起始|机位|轴线侧",
                "景别": r"景别|大全景|全景|中景|近景|特写",
                "主体构图": r"构图|主体|前景|中景|后景",
                "环境": r"环境|场景|竹林|门店|水岸|车厢",
                "道具": r"道具|马车|车帘|持有|状态",
                "动作起始状态": r"动作|起始状态|动作阶段|端坐|行进|静止",
                "光线状态": r"光线|光色|晨光|暖光|综合色温|照明",
            }
            for label, pattern in first_frame_requirements.items():
                if not re.search(pattern, first_frame_text):
                    errors.append(f"G{package_number:02d} 【首帧参考】 missing required {label}")
            if package_number == 1 and not re.search(r"首段|无上一Clip尾帧|Scene初始状态|开场", first_frame_text, re.IGNORECASE):
                errors.append(f"G{package_number:02d} 【首帧参考】 must declare that the first Clip has no previous tail frame")

        shots = list(re.finditer(r"^【分镜(\d+)】\s*$", package, re.MULTILINE))
        if not shots:
            errors.append(f"G{package_number:02d} must contain at least one 【分镜X】")
            continue
        actual_package_shots = [int(shot.group(1)) for shot in shots]
        if listed_shots != actual_package_shots:
            errors.append(
                f"G{package_number:02d} 包含分镜 must exactly match its 【分镜X】 sections: "
                f"listed={listed_shots}, actual={actual_package_shots}"
            )
        package_specs.append((package_number, clip_number_value, duration_value, actual_package_shots))
        first_shot_fields: dict[str, str] = {}
        for shot_index, shot_match in enumerate(shots):
            shot_number = int(shot_match.group(1))
            shot_numbers.append(shot_number)
            if shot_index + 1 < len(shots):
                shot_end = shots[shot_index + 1].start()
            else:
                ending_start = package.find("【反向提示词】", shot_match.end())
                shot_end = ending_start if ending_start >= 0 else len(package)
            shot_segment = package[shot_match.end():shot_end]
            field_cursor = -1
            present_fields: list[tuple[str, re.Match[str]]] = []
            for field in SHOT_FIELDS:
                field_matches = list(re.finditer(rf"^{re.escape(field)}", shot_segment, re.MULTILINE))
                if not field_matches:
                    errors.append(f"G{package_number:02d}/分镜{shot_number} missing field: {field}")
                    continue
                if len(field_matches) > 1:
                    errors.append(f"G{package_number:02d}/分镜{shot_number} duplicate field: {field}")
                field_match = field_matches[0]
                present_fields.append((field, field_match))
                if field_match.start() < field_cursor:
                    errors.append(f"G{package_number:02d}/分镜{shot_number} field out of order: {field}")
                else:
                    field_cursor = field_match.start()
            field_values: dict[str, str] = {}
            for field_index, (field, field_match) in enumerate(present_fields):
                value_end = present_fields[field_index + 1][1].start() if field_index + 1 < len(present_fields) else len(shot_segment)
                field_value = shot_segment[field_match.end():value_end].strip()
                field_values[field] = field_value
                if not field_value:
                    errors.append(f"G{package_number:02d}/分镜{shot_number} field has no content: {field}")
                if field == "音效：":
                    if MUSIC_PATTERN.search(field_value):
                        errors.append(f"G{package_number:02d}/分镜{shot_number} 音效 contains forbidden music instruction")
                    if SOUND_PLACEHOLDER_PATTERN.fullmatch(field_value):
                        errors.append(f"G{package_number:02d}/分镜{shot_number} 音效 may not be empty, silent, or generic placeholder content")
                    if not SOUND_BED_PATTERN.search(field_value):
                        errors.append(f"G{package_number:02d}/分镜{shot_number} 音效 must name a concrete 环境底声/空间底噪 or justified 有意静默")
                    if not SOUND_FOREGROUND_PATTERN.search(field_value):
                        errors.append(f"G{package_number:02d}/分镜{shot_number} 音效 must name at least one synchronized foreground layer such as 动作声、Foley、呼吸、对白 or 剧情内声源")
            if shot_index == 0:
                first_shot_fields = field_values
            start_state = field_values.get("起始状态：", "")
            if start_state and not START_FRAME_SOURCE_PATTERN.search(start_state):
                errors.append(
                    f"G{package_number:02d}/分镜{shot_number} 起始状态 must explicitly state the first-frame source or requirement"
                )
            end_state = field_values.get("镜头结尾状态：", "")
            if end_state:
                if not END_FRAME_STABLE_PATTERN.search(end_state) or not END_FRAME_INTERFACE_PATTERN.search(end_state):
                    errors.append(
                        f"G{package_number:02d}/分镜{shot_number} 镜头结尾状态 must be stable, readable, and usable as a handoff interface"
                    )
                if HIGH_RISK_END_PATTERN.search(end_state) and not CONFIRMED_END_EXCEPTION_PATTERN.search(end_state):
                    errors.append(
                        f"G{package_number:02d}/分镜{shot_number} 镜头结尾状态 contains an unapproved high-risk ending"
                    )
            handoff = field_values.get("与下一镜衔接：", "")
            if handoff and not BOUNDARY_CLASS_PATTERN.search(handoff):
                errors.append(
                    f"G{package_number:02d}/分镜{shot_number} 与下一镜衔接 must declare Continuous Handoff, Motivated Discontinuity, or Unresolved Handoff"
                )
            if shot_index < len(shots) - 1:
                if not re.search(r"同一\s*Clip|同一生成段|段内连续生成", handoff, re.IGNORECASE):
                    errors.append(f"G{package_number:02d}/分镜{shot_number} intra-Clip handoff must state 同一Clip连续生成")

        negative_start = package.find("【反向提示词】")
        tail_token = f"[G{package_number:02d}尾帧]"
        if tail_token not in tail_text or "保存为" not in tail_text:
            errors.append(f"G{package_number:02d} 【尾帧限制】 must save the frame as {tail_token}")
        if not END_FRAME_STABLE_PATTERN.search(tail_text):
            errors.append(f"G{package_number:02d} 【尾帧限制】 must declare a stable end frame")
        tail_requirements = {
            "人物最终位置/动作/视线/情绪": r"人物|角色|秦始皇|侍从|位置|动作|视线|情绪",
            "摄影机最终状态": r"摄影机|机位|景别|构图|焦点",
            "道具最终状态": r"道具|马车|车帘|持有者|左右手|状态",
            "环境最终状态": r"环境|场景|竹林|门店|车厢|光线|光色|天气",
        }
        for label, pattern in tail_requirements.items():
            if not re.search(pattern, tail_text):
                errors.append(f"G{package_number:02d} 【尾帧限制】 missing required {label}")
        if HIGH_RISK_END_PATTERN.search(tail_text) and not CONFIRMED_END_EXCEPTION_PATTERN.search(tail_text):
            errors.append(f"G{package_number:02d} 【尾帧限制】 contains an unapproved high-risk ending")
        if not re.search(r"最后\s*1\s*秒[^\n]*(?:不得|禁止)[^\n]*(?:复杂动作|剧情事件|新动作)", tail_text):
            errors.append(f"G{package_number:02d} 【尾帧限制】 must forbid starting new complex action in the final 1 second")
        tail_use_match = re.search(r"^\s*下一段(?:预计)?用途[：:]\s*(.+)$", tail_text, re.MULTILINE)
        if not tail_use_match:
            errors.append(f"G{package_number:02d} 【尾帧限制】 must declare 下一段预计用途")
        else:
            tail_use = tail_use_match.group(1).strip()
            if not re.search(r"直接作为.+起始帧|仅作为.+连续性参考|不作.+正式参考资产|最终收束", tail_use):
                errors.append(
                    f"G{package_number:02d} 下一段预计用途 must choose direct start-frame, reference-only, no-formal-tail-reference, or final closure"
                )
        negative_text = package[negative_start + len("【反向提示词】"):] if negative_start >= 0 else ""
        negative_lines = [line.strip() for line in negative_text.splitlines() if line.strip()]
        if not negative_lines or negative_lines[0] != DEFAULT_NO_BACKGROUND_MUSIC_LINE:
            errors.append(
                f"G{package_number:02d} 【反向提示词】 first non-empty line must be exactly: "
                f"{DEFAULT_NO_BACKGROUND_MUSIC_LINE}"
            )

        if package_number > 1:
            previous_token = f"[G{package_number - 1:02d}尾帧]"
            start_text = first_shot_fields.get("起始状态：", "")
            no_formal_reference = bool(
                previous_token in first_frame_text
                and re.search(r"不作.*正式参考资产|不作为.*正式参考资产|仅作.*连续性核对", first_frame_text)
            )
            direct_mode = bool(
                previous_token in first_frame_text
                and re.search(r"Direct Start-Frame Handoff|直接继承|直接作为.*首帧|直接作为.*起始帧", first_frame_text, re.IGNORECASE)
            )
            reference_mode = bool(
                previous_token in first_frame_text
                and re.search(r"Reference-Only Handoff|仅作.*连续性参考|仅作为.*连续性参考", first_frame_text, re.IGNORECASE)
            )
            if sum((no_formal_reference, direct_mode, reference_mode)) != 1:
                errors.append(
                    f"G{package_number:02d} 【首帧参考】 must choose exactly one of direct inheritance, reference-only, or no formal tail reference"
                )
            if no_formal_reference:
                if previous_token in reference_text:
                    errors.append(
                        f"G{package_number:02d} cross-scene/no-formal-reference mode must not list {previous_token} in 【参考资产】"
                    )
                if not re.search(r"重建原因|断点|跨场景|新场景", first_frame_text):
                    errors.append(f"G{package_number:02d} no-formal-reference mode must state the scene-break/rebuild reason")
                if not re.search(r"Scene初始状态|Confirmed Asset|已确认.*场景|新场景", first_frame_text, re.IGNORECASE):
                    errors.append(f"G{package_number:02d} cross-scene 【首帧参考】 must name the confirmed new-scene source")
            else:
                if previous_token not in reference_text:
                    errors.append(f"G{package_number:02d} Direct/Reference-Only mode must formally cite {previous_token} in 【参考资产】")
                if previous_token not in start_text:
                    errors.append(f"G{package_number:02d} 起始状态 must cite {previous_token}")
                elif direct_mode and not re.search(r"直接|从该帧|延续该帧", start_text):
                    errors.append(f"G{package_number:02d} 起始状态 must directly continue {previous_token}")
                elif reference_mode and not re.search(r"连续性参考|兼容|重建", start_text):
                    errors.append(f"G{package_number:02d} 起始状态 must reconstruct a compatible boundary from {previous_token}")

    if package_ids and package_ids != list(range(package_ids[0], package_ids[0] + len(package_ids))):
        errors.append(f"Prompt Package IDs in this delivery must be consecutive: found {[f'G{number:02d}' for number in package_ids]}")
    if clip_ids and clip_ids != list(range(clip_ids[0], clip_ids[0] + len(clip_ids))):
        errors.append(f"Clip IDs in this delivery must be consecutive: found {[f'CLIP-{number:03d}' for number in clip_ids]}")
    if shot_numbers and shot_numbers != list(range(shot_numbers[0], shot_numbers[0] + len(shot_numbers))):
        errors.append(f"Shot numbers must be consecutive with no omissions, duplicates, or reordering in this delivery: found {shot_numbers}")
    if package_ids and shot_numbers and len(package_ids) > len(shot_numbers):
        errors.append(
            f"Total Prompt Packages must not exceed Total Formal Shots: packages={len(package_ids)}, shots={len(shot_numbers)}"
        )
    if clip_plan_path is not None:
        resolved_clip_plan = clip_plan_path.resolve()
        if not resolved_clip_plan.is_file():
            errors.append(f"Confirmed Clip Production Plan not found for STATE-08 cross-check: {resolved_clip_plan}")
        else:
            clip_text = read_text(resolved_clip_plan)
            table_start = clip_text.find("## Clip Table")
            table_end = clip_text.find("## Clip Detail Cards", table_start + 1)
            table_text = clip_text[table_start:table_end] if table_start >= 0 and table_end > table_start else ""
            plan_rows = re.findall(
                r"^\|\s*CLIP-(\d{3})\s*\|\s*([^|]+)\|\s*(\d+(?:\.\d+)?)\s*秒\s*\|",
                table_text,
                re.MULTILINE,
            )
            plan_specs = {
                int(clip_number): (float(duration), [int(value) for value in re.findall(r"SHOT-(\d{3})", source_text, re.IGNORECASE)])
                for clip_number, source_text, duration in plan_rows
            }
            for package_number, clip_number, duration, shots in package_specs:
                if clip_number is None or clip_number not in plan_specs:
                    errors.append(f"G{package_number:02d} has no matching Confirmed Clip Production Plan row")
                    continue
                planned_duration, planned_shots = plan_specs[clip_number]
                if duration is None or abs(duration - planned_duration) > 1e-6:
                    errors.append(
                        f"G{package_number:02d} platform duration must equal CLIP-{clip_number:03d} target duration: prompt={duration}, clip_plan={planned_duration:g}"
                    )
                if shots != planned_shots:
                    errors.append(
                        f"G{package_number:02d} shots must equal CLIP-{clip_number:03d}: prompt={shots}, clip_plan={planned_shots}"
                    )
    timeline_patterns = {
        "timecode": r"(?<!\d)\d{1,2}:\d{2}(?::\d{2})?(?!\d)",
        "second range": r"(?<!\d)\d+(?:\.\d+)?\s*[-–—~至到]\s*\d+(?:\.\d+)?\s*秒",
        "numbered second": r"第\s*\d+\s*秒",
        "frame or fps parameter": r"(?<!\d)\d+(?:\.\d+)?\s*(?:fps|帧)(?![\w])",
        "timeline label": r"总时长|总片时长|单镜头时长|单分镜时长|逐镜时长|时间码|时间戳",
    }
    for label, pattern in timeline_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Forbidden timeline expression detected: {label}")
    if re.search(r"(?<![A-Za-z0-9])(?:Shot\s*\d+|S\d{2})(?![A-Za-z0-9])", text, re.IGNORECASE):
        errors.append("Mixed or legacy shot numbering detected; use Gxx packages plus 【分镜X】 only")
    if re.search(r"^(?:Applicable Knowledge Set|Projection Ledger|Scene:|Character:|Action:|Composition:|Camera:|Lighting:|Sound:|Editing:)\s*$", text, re.MULTILINE):
        errors.append("Internal knowledge or projection structure leaked into final STATE-08 output")
    if re.search(r"(?<![A-Za-z0-9])(?:PEX|LGT|FLN|CLR|TRN|CMG)-\d{2}(?![A-Za-z0-9])|(?<![A-Za-z0-9])AU(?:1|2|4|5|6|7|9|10|12|14|15|17|20|23|24|25|26|27|28|43|45)(?![A-Za-z0-9])", text):
        errors.append("Internal lighting, performance, focal-length, color, transition, or movement-combination pattern identifier leaked into final STATE-08 output")
    return report(errors, warnings, as_json)


def validate_state08(
    path: Path,
    as_json: bool = False,
    clip_plan_path: Path | None = None,
    allow_batch_output: bool = False,
) -> int:
    """Validate the fixed STATE-08 Clip contract owned by templates/10_video_prompt.md."""
    errors: list[str] = []
    warnings: list[str] = []
    text = read_text(path.resolve())

    legacy_patterns = (
        r"^【(?:CLIP标题|时长|画幅|参考资产|首帧参考|尾帧限制|主风格|人物一致性|环境一致性|音色特征|反向提示词)】\s*$",
        r"^【分镜\d+】\s*$",
        r"^与下一镜衔接：",
    )
    for pattern in legacy_patterns:
        if re.search(pattern, text, re.MULTILINE):
            errors.append("Legacy or extra STATE-08 field detected; use the fixed template exactly")
            break

    title_pattern = re.compile(r"^#\s+CLIP-(\d{1,3})｜([^\r\n]+?)\s+Seedance视频提示词\s*$", re.MULTILINE)
    package_markers = list(title_pattern.finditer(text))
    if not package_markers:
        errors.append("No fixed '# CLIP-X｜标题 Seedance视频提示词' package found")
    if len(package_markers) > 1 and not allow_batch_output:
        errors.append("Default STATE-08 delivery is one complete Clip per checkpoint; multiple Clips require explicit batch authorization")

    plan_specs: dict[int, tuple[float, list[int]]] = {}
    if clip_plan_path is not None:
        resolved_plan = clip_plan_path.resolve()
        if not resolved_plan.is_file():
            errors.append(f"Confirmed Clip Production Plan not found: {resolved_plan}")
        else:
            plan_text = read_text(resolved_plan)
            row_pattern = re.compile(
                r"^\|\s*CLIP-(\d{3})\s*\|\s*([^|]+)\|\s*(\d+(?:\.\d+)?)\s*秒\s*\|",
                re.MULTILINE | re.IGNORECASE,
            )
            for row in row_pattern.finditer(plan_text):
                clip_number = int(row.group(1))
                shots = [int(value) for value in re.findall(r"SHOT-(\d{3})", row.group(2), re.IGNORECASE)]
                plan_specs[clip_number] = (float(row.group(3)), shots)
            if not plan_specs:
                errors.append("Confirmed Clip Production Plan contains no parsable CLIP rows")

    seen_clips: list[int] = []
    seen_shots: list[int] = []
    placeholder_pattern = re.compile(r"^(?:同上|沿用前文|沿用上一镜|见前文|见上|其余一致|略|有效内容|待定|N/?A|None)\s*[。.]?$", re.IGNORECASE)

    def field_value(segment: str, label: str, next_positions: list[int]) -> str:
        match = re.search(rf"^{re.escape(label)}(.*)$", segment, re.MULTILINE)
        if not match:
            return ""
        end = min((position for position in next_positions if position > match.start()), default=len(segment))
        inline = match.group(1).strip()
        following = segment[match.end():end].strip()
        return "\n".join(part for part in (inline, following) if part).strip()

    for package_index, marker in enumerate(package_markers):
        package_end = package_markers[package_index + 1].start() if package_index + 1 < len(package_markers) else len(text)
        package = text[marker.start():package_end]
        clip_number = int(marker.group(1))
        seen_clips.append(clip_number)
        if not marker.group(2).strip():
            errors.append(f"CLIP-{clip_number:03d} title must contain a human-readable title")

        shot_markers = list(re.finditer(r"^分镜(\d+)\s*$", package, re.MULTILINE))
        if not shot_markers:
            errors.append(f"CLIP-{clip_number:03d} must contain at least one 分镜X")
            continue
        first_shot_pos = shot_markers[0].start()
        negative_matches = list(re.finditer(r"^反向提示词：(.*)$", package, re.MULTILINE))
        if len(negative_matches) != 1:
            errors.append(f"CLIP-{clip_number:03d} must contain exactly one 反向提示词： field")
            negative_pos = len(package)
        else:
            negative_pos = negative_matches[0].start()
            if negative_pos < shot_markers[-1].start():
                errors.append(f"CLIP-{clip_number:03d} 反向提示词： must follow all shots")

        local_title_end = marker.end() - marker.start()
        global_segment = package[local_title_end:first_shot_pos]
        global_matches: list[tuple[str, re.Match[str]]] = []
        cursor = -1
        for label in GLOBAL_SECTIONS:
            matches = list(re.finditer(rf"^{re.escape(label)}", global_segment, re.MULTILINE))
            if len(matches) != 1:
                errors.append(f"CLIP-{clip_number:03d} must contain exactly one global field: {label}")
                continue
            match = matches[0]
            global_matches.append((label, match))
            if match.start() < cursor:
                errors.append(f"CLIP-{clip_number:03d} global field out of order: {label}")
            cursor = match.start()

        global_values: dict[str, str] = {}
        for index, (label, match) in enumerate(global_matches):
            end = global_matches[index + 1][1].start() if index + 1 < len(global_matches) else len(global_segment)
            value = "\n".join(part for part in (match.group(0)[len(label):].strip(), global_segment[match.end():end].strip()) if part).strip()
            global_values[label] = value
            if not value:
                errors.append(f"CLIP-{clip_number:03d} global field has no content: {label}")
            elif placeholder_pattern.fullmatch(value):
                errors.append(f"CLIP-{clip_number:03d} global field uses forbidden shorthand: {label}")

        duration_text = global_values.get("时长：", "")
        duration_matches = re.findall(r"平台生成时长\s*[：:]\s*(\d+(?:\.\d+)?)\s*秒|(?<![\d.])(\d+(?:\.\d+)?)\s*秒", duration_text)
        duration_values = [float(first or second) for first, second in duration_matches]
        if len(duration_values) != 1:
            errors.append(f"CLIP-{clip_number:03d} 时长： must contain exactly one platform duration")
            duration_value = None
        else:
            duration_value = duration_values[0]
            if duration_value < 4 or duration_value > 15:
                errors.append(f"CLIP-{clip_number:03d} platform duration must be 4-15 seconds")

        reference_text = global_values.get("参考资产：", "")
        first_frame_text = global_values.get("首帧参考：", "")
        tail_text = global_values.get("尾帧限制：", "")
        voice_text = global_values.get("音色特征：", "")
        tail_required_yes = bool(re.search(r"Tail\s*Frame\s*Required\s*=\s*YES", first_frame_text, re.IGNORECASE))
        tail_required_no = bool(re.search(r"Tail\s*Frame\s*Required\s*=\s*NO", first_frame_text, re.IGNORECASE))
        tail_pending = bool(re.search(r"待用户提供|待上传", f"{reference_text}\n{first_frame_text}"))
        if tail_required_yes:
            if tail_pending:
                errors.append(
                    f"CLIP-{clip_number:03d} Tail Frame Required = YES is still pending user upload; draft cannot validate as a final executable prompt"
                )
            if not re.search(r"REF-TAIL-\w+｜CLIP-\w+尾帧参考", reference_text):
                errors.append(f"CLIP-{clip_number:03d} Tail Frame Required = YES must include the confirmed REF-TAIL asset in 参考资产：")
            if "以 REF-TAIL-" not in first_frame_text or "为直接承接依据起镜。" not in first_frame_text:
                errors.append(f"CLIP-{clip_number:03d} Tail Frame Required = YES must include the fixed direct-carryover sentence")
        if tail_required_no and re.search(r"REF-TAIL-\w+｜CLIP-\w+尾帧参考", reference_text):
            errors.append(f"CLIP-{clip_number:03d} Tail Frame Required = NO must not formally reference the previous REF-TAIL asset")
        has_voice_reference = bool(VOICE_REFERENCE_PATTERN.search(reference_text))
        if has_voice_reference:
            if not re.search(r"Reference.*锁定|锁定.*Reference|由.*参考资产.*锁定|声音身份.*锁定", voice_text, re.IGNORECASE):
                errors.append(f"CLIP-{clip_number:03d} 音色特征： must state that the Voice/Audio Reference locks voice identity")
            if not re.search(r"不得|不以文字|不再.*文字|禁止.*重定义", voice_text):
                errors.append(f"CLIP-{clip_number:03d} 音色特征： must forbid textual voice redefinition when using a Reference")
        if not reference_text or not first_frame_text or not tail_text:
            errors.append(f"CLIP-{clip_number:03d} 参考资产、首帧参考、尾帧限制 are unconditional and non-empty")
        if reference_text and (not REFERENCE_ITEM_PATTERN.search(reference_text) or not REFERENCE_CONSTRAINT_PATTERN.search(reference_text)):
            errors.append(f"CLIP-{clip_number:03d} 参考资产： must name an actual asset/frame and its use or locking constraint")
        if PSEUDO_VISUAL_REFERENCE_PATTERN.search(reference_text):
            errors.append(
                f"CLIP-{clip_number:03d} 参考资产： contains a text-only pseudo asset; move the constraint to its existing semantic field"
            )
        if first_frame_text and not START_FRAME_SOURCE_PATTERN.search(first_frame_text):
            errors.append(f"CLIP-{clip_number:03d} 首帧参考： must state the first-frame source or handoff mode")
        if tail_text:
            if not END_FRAME_STABLE_PATTERN.search(tail_text) or not END_FRAME_INTERFACE_PATTERN.search(tail_text):
                errors.append(f"CLIP-{clip_number:03d} 尾帧限制： must be stable, readable, and inheritable")
            if not re.search(r"最后\s*1\s*秒[^\n]*(?:不得|禁止)", tail_text):
                errors.append(f"CLIP-{clip_number:03d} 尾帧限制： must forbid new actions in the final 1 second")

        actual_shots = [int(shot.group(1)) for shot in shot_markers]
        seen_shots.extend(actual_shots)
        if actual_shots != sorted(actual_shots) or len(actual_shots) != len(set(actual_shots)):
            errors.append(f"CLIP-{clip_number:03d} shot numbers must be unique and ordered")

        for shot_index, shot_match in enumerate(shot_markers):
            shot_number = int(shot_match.group(1))
            shot_end = shot_markers[shot_index + 1].start() if shot_index + 1 < len(shot_markers) else negative_pos
            shot_segment = package[shot_match.end():shot_end]
            present: list[tuple[str, re.Match[str]]] = []
            cursor = -1
            for label in SHOT_FIELDS:
                matches = list(re.finditer(rf"^{re.escape(label)}", shot_segment, re.MULTILINE))
                if len(matches) != 1:
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} must contain exactly one field: {label}")
                    continue
                match = matches[0]
                present.append((label, match))
                if match.start() < cursor:
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} field out of order: {label}")
                cursor = match.start()
            values: dict[str, str] = {}
            for index, (label, match) in enumerate(present):
                end = present[index + 1][1].start() if index + 1 < len(present) else len(shot_segment)
                value = "\n".join(part for part in (match.group(0)[len(label):].strip(), shot_segment[match.end():end].strip()) if part).strip()
                values[label] = value
                if not value:
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} field has no content: {label}")
                elif placeholder_pattern.fullmatch(value):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} field uses forbidden shorthand: {label}")
            sound = values.get("音效：", "")
            if sound:
                if MUSIC_PATTERN.search(sound):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} 音效 contains forbidden music instruction")
                if not SOUND_BED_PATTERN.search(sound) or not SOUND_FOREGROUND_PATTERN.search(sound):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} 音效 must contain ambience and synchronized foreground sound")
            start_state = values.get("起始状态：", "")
            if start_state and not START_FRAME_SOURCE_PATTERN.search(start_state):
                errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} 起始状态 must identify its first-frame source")
            end_state = values.get("镜头结尾状态：", "")
            if end_state:
                if not END_FRAME_STABLE_PATTERN.search(end_state) or not END_FRAME_INTERFACE_PATTERN.search(end_state):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} 镜头结尾状态 must be stable, readable, and usable as an interface")
                if not BOUNDARY_CLASS_PATTERN.search(end_state):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} 镜头结尾状态 must declare the handoff class")
                if shot_index < len(shot_markers) - 1 and not re.search(r"同一\s*Clip|同一生成段|段内连续生成", end_state, re.IGNORECASE):
                    errors.append(f"CLIP-{clip_number:03d}/分镜{shot_number} intra-Clip ending must state 同一Clip连续生成")

        negative_text = package[negative_matches[0].end():].strip() if negative_matches else ""
        if negative_matches and negative_matches[0].group(1).strip():
            negative_text = "\n".join((negative_matches[0].group(1).strip(), negative_text)).strip()
        negative_lines = [line.strip() for line in negative_text.splitlines() if line.strip()]
        if not negative_lines or negative_lines[0] != DEFAULT_NO_BACKGROUND_MUSIC_LINE:
            errors.append(f"CLIP-{clip_number:03d} 反向提示词： first non-empty line must be exactly the default no-background-music line")

        if clip_number in plan_specs:
            plan_duration, plan_shots = plan_specs[clip_number]
            if duration_value is not None and abs(duration_value - plan_duration) > 1e-6:
                errors.append(f"CLIP-{clip_number:03d} duration does not match Confirmed Clip Production Plan")
            if plan_shots and actual_shots != plan_shots:
                errors.append(f"CLIP-{clip_number:03d} 分镜 list does not match Confirmed Clip Production Plan")
        elif plan_specs:
            errors.append(f"CLIP-{clip_number:03d} is absent from Confirmed Clip Production Plan")

    if len(seen_clips) != len(set(seen_clips)):
        errors.append("Duplicate Clip packages detected")
    if seen_clips != sorted(seen_clips):
        errors.append("Clip packages must be ordered by Clip number")
    if len(seen_shots) != len(set(seen_shots)):
        errors.append("A formal shot appears in more than one Clip package")

    timeline_patterns = {
        "timestamp": r"\b\d{1,2}:\d{2}(?::\d{2})?\b",
        "second range": r"(?<!\d)\d+(?:\.\d+)?\s*[-–—~至到]\s*\d+(?:\.\d+)?\s*秒",
        "numbered second": r"第\s*\d+\s*秒",
        "frame or fps parameter": r"(?<!\d)\d+(?:\.\d+)?\s*(?:fps|帧)(?![\w])",
        "timeline label": r"总时长|总片时长|单镜头时长|单分镜时长|逐镜时长|时间码|时间戳",
    }
    for label, pattern in timeline_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Forbidden timeline expression detected: {label}")
    return report(errors, warnings, as_json)


def validate_clip(
    path: Path,
    as_json: bool = False,
    project_status_path: Path | None = None,
    shot_design_path: Path | None = None,
) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    path = path.resolve()
    if not path.is_file():
        return report([f"Clip Plan not found: {path}"], warnings, as_json)
    text = read_text(path)
    cursor = -1
    for section in CLIP_SECTIONS:
        position = text.find(section)
        if position < 0:
            errors.append(f"Clip Plan missing section: {section}")
        elif position < cursor:
            errors.append(f"Clip Plan section out of order: {section}")
        else:
            cursor = position
    if not re.search(r"^- Status[：:]\s*Confirmed\s*$", text, re.MULTILINE | re.IGNORECASE):
        errors.append("Clip Plan Status must be Confirmed before STATE-08")
    source_artifact_match = re.search(
        r"^- Source Detailed Shot Design Artifact / Portable Checkpoint[：:]\s*(\S.*)$",
        text,
        re.MULTILINE,
    )
    if not source_artifact_match:
        errors.append("Clip Plan must identify its Detailed Shot Design Artifact or Portable Checkpoint")
    if not re.search(
        r"^- Source Detailed Shot Design Status[：:]\s*Confirmed\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    ):
        errors.append("Clip Plan source Detailed Shot Design Status must be Confirmed")
    if not re.search(r"^- Model Duration Window[：:]\s*4\s*[—–-]\s*15\s*秒\s*$", text, re.MULTILINE):
        errors.append("Clip Plan must declare Model Duration Window：4—15秒")
    if not re.search(r"^- Unit Rule[：:].*Shot\s*=.*Clip\s*=.*Total Clips\s*(?:≤|<=)\s*Total Formal Shots.*每个Clip只生成一条连续Prompt", text, re.MULTILINE):
        errors.append("Clip Plan must allow one-or-more source shots and declare Total Clips <= Total Formal Shots")
    if not re.search(
        r"^- Namespace Rule[：:].*Source Script Label.*SCENE.*UNIT.*SHOT.*CLIP.*Confirmed Detailed Shot Design",
        text,
        re.MULTILINE,
    ):
        errors.append("Clip Plan must declare Source Script Label / SCENE / UNIT / SHOT / CLIP namespace isolation")

    table_start = text.find("## Clip Table")
    table_end = text.find("## Clip Detail Cards", table_start + 1)
    table_text = text[table_start:table_end] if table_start >= 0 and table_end > table_start else ""
    row_pattern = re.compile(r"^\|\s*(CLIP-(\d{3}))\s*\|\s*([^|]+)\|\s*(\d+(?:\.\d+)?)\s*秒\s*\|", re.MULTILINE)
    rows = list(row_pattern.finditer(table_text))
    clip_ids = [match.group(1) for match in rows]
    validate_consecutive_ids(clip_ids, "CLIP", errors, "Clip")
    all_shots: list[int] = []
    table_durations: dict[str, float] = {}
    table_shots: dict[str, list[int]] = {}
    for match in rows:
        clip_id = match.group(1)
        source_text = match.group(3)
        duration = float(match.group(4))
        table_durations[clip_id] = duration
        if duration < 4 or duration > 15:
            errors.append(f"{clip_id} duration must be 4-15 seconds: found {duration:g}")
        source_shots = [int(value) for value in re.findall(r"SHOT-(\d{3})", source_text, re.IGNORECASE)]
        table_shots[clip_id] = source_shots
        if not source_shots:
            errors.append(f"{clip_id} must contain at least one source shot")
        if source_shots and source_shots != list(range(source_shots[0], source_shots[0] + len(source_shots))):
            errors.append(f"{clip_id} source shots must be adjacent and consecutive: found {source_shots}")
        all_shots.extend(source_shots)
    if all_shots and all_shots != list(range(1, len(all_shots) + 1)):
        errors.append(f"Formal shots must appear exactly once, in order, from SHOT-001: found {all_shots}")
    source_revision_match = re.search(
        r"^- Source Detailed Shot Design Revision[：:]\s*(\S+)",
        text,
        re.MULTILINE,
    )
    if not source_revision_match:
        errors.append("Clip Plan must identify Source Detailed Shot Design Revision")
    total_shots_match = re.search(r"^- Total Formal Shots[：:]\s*(\d+)\s*$", text, re.MULTILINE)
    total_clips_match = re.search(r"^- Total Clips[：:]\s*(\d+)\s*$", text, re.MULTILINE)
    if not total_shots_match:
        errors.append("Clip Plan must declare Total Formal Shots")
    if not total_clips_match:
        errors.append("Clip Plan must declare Total Clips")
    if total_shots_match:
        declared_shots = int(total_shots_match.group(1))
        if declared_shots != len(all_shots):
            errors.append(f"Total Formal Shots does not match Clip Table: declared={declared_shots}, actual={len(all_shots)}")
    if total_clips_match:
        declared_clips = int(total_clips_match.group(1))
        if declared_clips != len(rows):
            errors.append(f"Total Clips does not match Clip Table: declared={declared_clips}, actual={len(rows)}")
    if total_shots_match and total_clips_match and int(total_clips_match.group(1)) > int(total_shots_match.group(1)):
        errors.append("Total Clips must not exceed Total Formal Shots")

    if (project_status_path is None) != (shot_design_path is None):
        errors.append("Clip source cross-check requires both project status and Detailed Shot Design paths")
    elif project_status_path is None and shot_design_path is None:
        warnings.append(
            "Clip source identity was checked declaratively only; Work/Codex should pass project status and Detailed Shot Design paths"
        )
    else:
        resolved_status = project_status_path.resolve()
        resolved_shot_design = shot_design_path.resolve()
        if not resolved_status.is_file():
            errors.append(f"Project status not found for Clip source cross-check: {resolved_status}")
        if not resolved_shot_design.is_file():
            errors.append(f"Detailed Shot Design not found for Clip source cross-check: {resolved_shot_design}")
        if resolved_status.is_file():
            status_text = read_text(resolved_status)
            current_state_match = re.search(r"^- Current State[：:]\s*STATE-(\d{2})\b", status_text, re.MULTILINE)
            if not current_state_match or int(current_state_match.group(1)) < 7:
                errors.append("Clip Production requires Current State STATE-07 or later")
            completed_match = re.search(
                r"^- Completed States[：:]\s*(.*)$",
                status_text,
                re.MULTILINE,
            )
            if not completed_match or "STATE-06" not in completed_match.group(1):
                errors.append("Clip Production requires STATE-06 in Completed States")
        if resolved_shot_design.is_file():
            shot_text = read_text(resolved_shot_design)
            if not re.search(r"^- Status[：:]\s*Confirmed\s*$", shot_text, re.MULTILINE | re.IGNORECASE):
                errors.append("Detailed Shot Design source must have Status Confirmed")
            artifact_revision_match = re.search(
                r"^- Artifact Revision[：:]\s*(\S+)",
                shot_text,
                re.MULTILINE,
            )
            if not artifact_revision_match:
                errors.append("Detailed Shot Design source must identify Artifact Revision")
            elif source_revision_match and artifact_revision_match.group(1) != source_revision_match.group(1):
                errors.append(
                    "Clip Plan Source Detailed Shot Design Revision does not match the source Artifact Revision"
                )
            formal_shot_rows = [
                int(value)
                for value in re.findall(r"^\|\s*SHOT-(\d{3})\s*\|", shot_text, re.MULTILINE | re.IGNORECASE)
            ]
            if not formal_shot_rows:
                errors.append("Detailed Shot Design source contains no formal SHOT table rows")
            elif formal_shot_rows != list(range(1, len(formal_shot_rows) + 1)):
                errors.append(f"Detailed Shot Design formal SHOT rows are not consecutive: {formal_shot_rows}")
            elif all_shots != formal_shot_rows:
                errors.append(
                    f"Clip Plan SHOT allocation does not exactly match Detailed Shot Design: clip={all_shots}, source={formal_shot_rows}"
                )

    detail_matches = list(re.finditer(r"^###\s+(CLIP-(\d{3}))\s*$", text, re.MULTILINE))
    detail_ids = [match.group(1) for match in detail_matches]
    if clip_ids and detail_ids != clip_ids:
        errors.append(f"Clip Detail Cards must match Clip Table IDs and order: table={clip_ids}, details={detail_ids}")
    for detail_index, detail_match in enumerate(detail_matches):
        clip_id = detail_match.group(1)
        detail_end = detail_matches[detail_index + 1].start() if detail_index + 1 < len(detail_matches) else text.find("## Cross-Clip Continuity Ledger", detail_match.end())
        if detail_end < 0:
            detail_end = len(text)
        segment = text[detail_match.end():detail_end]
        for field in CLIP_DETAIL_FIELDS:
            field_match = re.search(rf"^-\s*{re.escape(field)}\s*(.*)$", segment, re.MULTILINE)
            if not field_match:
                errors.append(f"{clip_id} missing detail field: {field}")
            elif not field_match.group(1).strip():
                errors.append(f"{clip_id} detail field has no content: {field}")
        duration_match = re.search(r"^-\s*目标时长[：:]\s*(\d+(?:\.\d+)?)\s*秒", segment, re.MULTILINE)
        if not duration_match:
            errors.append(f"{clip_id} detail 目标时长 must use N秒")
        elif clip_id in table_durations and float(duration_match.group(1)) != table_durations[clip_id]:
            errors.append(f"{clip_id} detail duration does not match Clip Table")
        source_match = re.search(r"^-\s*包含 Shot[：:]\s*(.*)$", segment, re.MULTILINE)
        detail_source_shots = [int(value) for value in re.findall(r"SHOT-(\d{3})", source_match.group(1), re.IGNORECASE)] if source_match else []
        if clip_id in table_shots and detail_source_shots != table_shots[clip_id]:
            errors.append(f"{clip_id} detail source shots do not match Clip Table")
        accounting_match = re.search(r"^-\s*时长核算[：:]\s*(.*)$", segment, re.MULTILINE)
        if accounting_match:
            accounting_text = accounting_match.group(1)
            shot_duration_pairs = [
                (int(shot), float(duration))
                for shot, duration in re.findall(r"SHOT-(\d{3})\s*[=＝:：]\s*(\d+(?:\.\d+)?)\s*秒", accounting_text, re.IGNORECASE)
            ]
            accounting_shots = [shot for shot, _ in shot_duration_pairs]
            if clip_id in table_shots and accounting_shots != table_shots[clip_id]:
                errors.append(f"{clip_id} 时长核算 must list every source shot once and in order")
            computed_total = sum(duration for _, duration in shot_duration_pairs)
            stated_total_match = re.search(r"合计\s*[=＝:：]\s*(\d+(?:\.\d+)?)\s*秒", accounting_text)
            platform_match = re.search(r"平台生成时长\s*[=＝:：]\s*(\d+(?:\.\d+)?)\s*秒", accounting_text)
            if not shot_duration_pairs or not stated_total_match or not platform_match:
                errors.append(f"{clip_id} 时长核算 must use SHOT-001=N秒；合计=N秒；平台生成时长=N秒")
            else:
                stated_total = float(stated_total_match.group(1))
                platform_duration = float(platform_match.group(1))
                table_duration = table_durations.get(clip_id)
                if abs(computed_total - stated_total) > 1e-6:
                    errors.append(f"{clip_id} source-shot duration sum does not match stated total")
                if table_duration is not None and (
                    abs(stated_total - table_duration) > 1e-6 or abs(platform_duration - table_duration) > 1e-6
                ):
                    errors.append(f"{clip_id} 时长核算 total and platform duration must equal Clip Table target duration")
        g_number = int(detail_match.group(2))
        tail_token = f"[G{g_number:02d}尾帧]"
        if tail_token not in segment or "保存为" not in segment:
            errors.append(f"{clip_id} must save its end frame as {tail_token}")
        sound_match = re.search(r"^-\s*声音连续[：:]\s*(.*)$", segment, re.MULTILINE)
        if sound_match:
            sound_value = sound_match.group(1).strip()
            if MUSIC_PATTERN.search(sound_value):
                errors.append(f"{clip_id} 声音连续 must contain positive production sound only; music bans belong to STATE-08 反向提示词")
            if SOUND_PLACEHOLDER_PATTERN.fullmatch(sound_value) or not SOUND_BED_PATTERN.search(sound_value):
                errors.append(f"{clip_id} 声音连续 must name a concrete environment bed or justified intended silence")
            if not SOUND_FOREGROUND_PATTERN.search(sound_value):
                errors.append(f"{clip_id} 声音连续 must name synchronized foreground sound such as Foley, breath, dialogue, or action sound")
        tail_use_match = re.search(r"^-\s*尾帧用途判定[：:]\s*(.*)$", segment, re.MULTILINE)
        if tail_use_match and not re.search(r"直接作为下一Clip起始帧|仅作为下一Clip连续性参考|不继承|最终收束", tail_use_match.group(1)):
            errors.append(f"{clip_id} 尾帧用途判定 must choose a supported mode")

    knowledge_start = text.find("## Knowledge Projection Ledger")
    validation_start = text.find("## Coverage And Validation", knowledge_start + 1)
    knowledge_text = text[knowledge_start:validation_start] if knowledge_start >= 0 and validation_start > knowledge_start else ""
    knowledge_ids = re.findall(r"^\|\s*(CLIP-\d{3})\s*\|", knowledge_text, re.MULTILINE)
    if clip_ids and knowledge_ids != clip_ids:
        errors.append(f"Knowledge Projection Ledger must contain every Clip exactly once: found {knowledge_ids}")
    return report(errors, warnings, as_json)


def validate_shot_plan(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    path = path.resolve()
    if not path.is_file():
        return report([f"Shot Execution Plan not found: {path}"], warnings, as_json)
    text = read_text(path)

    cursor = -1
    for section in SHOT_PLAN_SECTIONS:
        position = text.find(section)
        if position < 0:
            errors.append(f"Shot Execution Plan missing section: {section}")
        elif position < cursor:
            errors.append(f"Shot Execution Plan section out of order: {section}")
        else:
            cursor = position

    if not re.search(r"^- Status[：:]\s*Confirmed\s*$", text, re.MULTILINE | re.IGNORECASE):
        errors.append("Shot Execution Plan Status must be Confirmed before Clip Planning")
    if not re.search(r"^- Formal Shot Duration Window[：:]\s*4\s*[—–-]\s*15\s*秒\s*$", text, re.MULTILINE):
        errors.append("Shot Execution Plan must declare Formal Shot Duration Window：4—15秒")

    table_start = text.find("## Shot Order Table")
    table_end = text.find("## Shot Execution Cards", table_start + 1)
    table_text = text[table_start:table_end] if table_start >= 0 and table_end > table_start else ""
    table_rows = list(re.finditer(r"^\|\s*(SHOT-(\d{3}))\s*\|(?:[^|]*\|){3}\s*(\d+(?:\.\d+)?)\s*秒(?:[^|]*)\|", table_text, re.MULTILINE))
    table_ids = [match.group(1) for match in table_rows]
    validate_consecutive_ids(table_ids, "SHOT", errors, "Formal Shot")
    table_durations: dict[str, float] = {}
    for match in table_rows:
        shot_id = match.group(1)
        duration = float(match.group(3))
        table_durations[shot_id] = duration
        if duration < 4 or duration > 15:
            errors.append(f"{shot_id} duration must be 4-15 seconds: found {duration:g}")

    card_matches = list(re.finditer(r"^###\s+(SHOT-(\d{3}))\s*$", text, re.MULTILINE))
    card_ids = [match.group(1) for match in card_matches]
    if table_ids and card_ids != table_ids:
        errors.append(f"Shot Execution Cards must match Shot Order Table IDs and order: table={table_ids}, cards={card_ids}")
    for index, card_match in enumerate(card_matches):
        shot_id = card_match.group(1)
        card_end = card_matches[index + 1].start() if index + 1 < len(card_matches) else text.find("## Adjacent-Shot Continuity Ledger", card_match.end())
        if card_end < 0:
            card_end = len(text)
        segment = text[card_match.end():card_end]
        duration_match = re.search(r"^-\s*Planned Execution Duration[：:]\s*(\d+(?:\.\d+)?)\s*秒", segment, re.MULTILINE)
        if not duration_match:
            errors.append(f"{shot_id} must declare Planned Execution Duration：N秒")
            continue
        duration = float(duration_match.group(1))
        if duration < 4 or duration > 15:
            errors.append(f"{shot_id} card duration must be 4-15 seconds: found {duration:g}")
        if shot_id in table_durations and duration != table_durations[shot_id]:
            errors.append(f"{shot_id} card duration does not match Shot Order Table")

    total_match = re.search(r"^- Total Formal Shots[：:]\s*(\d+)\s*$", text, re.MULTILINE)
    if not total_match:
        errors.append("Shot Execution Plan must declare Total Formal Shots")
    elif int(total_match.group(1)) != len(table_rows):
        errors.append(f"Total Formal Shots does not match Shot Order Table: declared={int(total_match.group(1))}, actual={len(table_rows)}")
    return report(errors, warnings, as_json)


def sequence_segment(text: str, start: str, end: str | None) -> str:
    start_pos = text.find(start)
    if start_pos < 0:
        return ""
    content_start = start_pos + len(start)
    end_pos = text.find(end, content_start) if end else len(text)
    return text[content_start:end_pos if end_pos >= 0 else len(text)]


def defined_table_ids(segment: str, prefix: str) -> list[str]:
    return re.findall(rf"^\|\s*({prefix}-\d{{3}})\s*\|", segment, re.MULTILINE)


def validate_consecutive_ids(ids: list[str], prefix: str, errors: list[str], label: str) -> None:
    if not ids:
        errors.append(f"No {label} definitions found")
        return
    if len(ids) != len(set(ids)):
        errors.append(f"Duplicate {label} definitions found: {ids}")
    numbers = [int(item.split("-")[1]) for item in ids]
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        errors.append(f"{label} IDs must be consecutive from {prefix}-001: found {ids}")


def validate_sequence(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    path = path.resolve()
    if not path.is_file():
        return report([f"Sequence plan does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    status_match = re.search(r"^Status:[ \t]*(Planning|Confirmed|Not Applicable)[ \t]*$", text, re.MULTILINE)
    if not status_match:
        errors.append("Status must be Planning, Confirmed or Not Applicable")
    status = status_match.group(1) if status_match else ""
    if not re.search(r"^Project ID:[ \t]*\S.*$", text, re.MULTILINE):
        errors.append("Missing non-empty Project ID")
    if status == "Not Applicable":
        reason = re.search(r"^Not Applicable Reason:\s*(\S.*)$", text, re.MULTILINE)
        if not reason:
            errors.append("Not Applicable plan must include a reason")
        if re.search(r"(?<![A-Z0-9])(?:SEQ|BEAT|COV|UNIT|SHOT)-\d{3}(?!\d)", text):
            errors.append("Not Applicable plan must not allocate production IDs")
        return report(errors, warnings, as_json)
    cursor = -1
    for section in SEQUENCE_SECTIONS:
        position = text.find(section, cursor + 1)
        if position < 0:
            errors.append(f"Missing sequence section: {section}")
        else:
            cursor = position
        if text.count(section) > 1:
            errors.append(f"Duplicate sequence section: {section}")
    sequence_ids = re.findall(r"^Sequence ID:\s*(SEQ-\d{3})\s*$", text, re.MULTILINE)
    if len(sequence_ids) != 1:
        errors.append(f"Sequence plan must define exactly one Sequence ID: found {sequence_ids}")
    beat_segment = sequence_segment(text, "## Beat Map", "## Coverage Matrix")
    coverage_segment = sequence_segment(text, "## Coverage Matrix", "## Generation Units")
    unit_segment = sequence_segment(text, "## Generation Units", "## State Ledger")
    ledger_segment = sequence_segment(text, "## State Ledger", "## Handoff And Risk")
    beat_ids = defined_table_ids(beat_segment, "BEAT")
    coverage_ids = defined_table_ids(coverage_segment, "COV")
    unit_ids = defined_table_ids(unit_segment, "UNIT")
    ledger_unit_ids = defined_table_ids(ledger_segment, "UNIT")
    validate_consecutive_ids(beat_ids, "BEAT", errors, "Beat")
    validate_consecutive_ids(coverage_ids, "COV", errors, "Coverage")
    validate_consecutive_ids(unit_ids, "UNIT", errors, "Generation Unit")
    if set(ledger_unit_ids) != set(unit_ids) or len(ledger_unit_ids) != len(unit_ids):
        errors.append(f"State Ledger UNIT IDs must match Generation Units exactly: units={unit_ids}, ledger={ledger_unit_ids}")
    referenced_beats = set(re.findall(r"\bBEAT-\d{3}\b", coverage_segment))
    for beat_id in beat_ids:
        if beat_id not in referenced_beats:
            errors.append(f"Beat has no Coverage Requirement: {beat_id}")
    known_beats = set(beat_ids)
    for beat_id in referenced_beats:
        if beat_id not in known_beats:
            errors.append(f"Coverage references undefined Beat ID: {beat_id}")
    known_coverage = set(coverage_ids)
    known_units = set(unit_ids)
    unit_references = set(re.findall(r"\b(?:BEAT|COV)-\d{3}\b", unit_segment))
    for item in unit_references:
        if item.startswith("BEAT-") and item not in known_beats:
            errors.append(f"Generation Unit references undefined Beat ID: {item}")
        if item.startswith("COV-") and item not in known_coverage:
            errors.append(f"Generation Unit references undefined Coverage ID: {item}")
    for beat_id in known_beats:
        if beat_id not in unit_references:
            errors.append(f"Beat is not assigned to a Generation Unit: {beat_id}")
    for coverage_id in known_coverage:
        if coverage_id not in unit_references:
            errors.append(f"Coverage Requirement is not assigned to a Generation Unit: {coverage_id}")
    if re.search(r"(?<![A-Z0-9])SHOT-\d{3}(?!\d)", text):
        errors.append("Sequence Plan must not create formal SHOT IDs")
    if "【CLIP标题】" in text or re.search(r"^【分镜\d+】", text, re.MULTILINE):
        errors.append("Sequence Plan contains STATE-08 final Schema content")
    priority_rows = re.findall(r"^\|\s*COV-\d{3}\s*\|([^\n]+)$", coverage_segment, re.MULTILINE)
    for row in priority_rows:
        cells = [cell.strip() for cell in row.split("|")]
        if len(cells) < 3 or cells[1] not in {"Required", "Supporting", "Optional"}:
            errors.append(f"Coverage row has invalid priority: {row.strip()}")
    if not known_units:
        warnings.append("Sequence Plan contains no Generation Units")
    return report(errors, warnings, as_json)


def validate_poster(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    path = path.resolve()
    if not path.is_file():
        return report([f"Poster design package does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    status_match = re.search(r"^Status:[ \t]*(Planning|Confirmed|Not Applicable)[ \t]*$", text, re.MULTILINE)
    if not status_match:
        errors.append("Status must be Planning, Confirmed or Not Applicable")
    status = status_match.group(1) if status_match else ""
    if not re.search(r"^Project ID:[ \t]*\S.*$", text, re.MULTILINE):
        errors.append("Missing non-empty Project ID")
    if status == "Not Applicable":
        if not re.search(r"^Not Applicable Reason:\s*(\S.*)$", text, re.MULTILINE):
            errors.append("Not Applicable poster package must include a reason")
        return report(errors, warnings, as_json)
    cursor = -1
    for section in POSTER_SECTIONS:
        position = text.find(section, cursor + 1)
        if position < 0:
            errors.append(f"Missing poster section: {section}")
        else:
            cursor = position
        if text.count(section) > 1:
            errors.append(f"Duplicate poster section: {section}")
    required_values = {
        "Aspect Ratio / Delivery Format": r"^- Aspect Ratio / Delivery Format:[ \t]*(\S.*)$",
        "Primary Visual Motif": r"^- Primary Visual Motif:[ \t]*(\S.*)$",
        "Primary Composition Model": r"^- Primary Composition Model:[ \t]*(\S.*)$",
    }
    for label, pattern in required_values.items():
        if not re.search(pattern, text, re.MULTILINE):
            errors.append(f"Missing non-empty poster value: {label}")
    if "### Exact Copy Ledger" not in text:
        errors.append("Poster package must include an Exact Copy Ledger")
    for layer in ("Base Layer:", "Type Layer:", "Composite Layer:", "Delivery Versions:", "Layout-spec / Safe-area Record:"):
        if layer not in text:
            errors.append(f"Poster package is missing layered-production field: {layer}")
    if re.search(r"所有.*署名.*梵想美学|固定品牌|默认画幅.*9:16", text):
        errors.append("Poster package leaked source-skill fixed brand or fixed-ratio rules")
    return report(errors, warnings, as_json)


def validate_review(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return report([f"Review report does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    for section in REVIEW_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE):
            errors.append(f"Missing review section: {section}")
    result = extract_label(text, "Result")
    if result not in {"PASS", "REVISE", "REBUILD"}:
        errors.append(f"Invalid Review Result: {result}")
    hard_gate = extract_label(text, "Hard Gate Result")
    if hard_gate not in {"PASS", "FAIL"}:
        errors.append(f"Invalid Hard Gate Result: {hard_gate}")
    if result == "PASS" and hard_gate != "PASS":
        errors.append("Review PASS requires Hard Gate Result PASS")
    score_text = extract_label(text, "Prompt Quality Score（如适用）")
    if score_text and score_text.lower() not in {"n/a", "not applicable"}:
        match = re.search(r"(\d{1,3})", score_text)
        if not match or not 0 <= int(match.group(1)) <= 100:
            errors.append(f"Invalid Prompt Quality Score: {score_text}")
    return_route = extract_label(text, "Return Route")
    if result in {"REVISE", "REBUILD"} and (not return_route or return_route.lower() == "none"):
        errors.append(f"Review {result} requires a Return Route")
    if "| Shot | Result |" in text and not re.search(r"^\|\s*(?:SHOT-|【分镜)\S*\s*\|", text, re.MULTILINE):
        warnings.append("Review report contains no shot-level QA rows")
    return report(errors, warnings, as_json)


def validate_asset_registry(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if path.is_dir():
        path = path / "asset_registry.md"
    if not path.is_file():
        return report([f"Asset registry does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    headings = list(re.finditer(r"^###\s+((?:CHAR|ENV|PROP|FX)-\d{3})\b.*$", text, re.MULTILINE))
    active_by_id: dict[str, int] = {}
    for index, match in enumerate(headings):
        asset_id = match.group(1)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[match.start():end]
        status = extract_label(block, "Status")
        visual_status = extract_label(block, "Visual Production Status")
        if visual_status not in VISUAL_PRODUCTION_STATUSES:
            errors.append(f"{asset_id} has invalid Visual Production Status: {visual_status}")
            continue
        prompt_revision = extract_label(block, "Prompt Revision")
        image_prompts = extract_label(block, "Image Prompts")
        prompt_confirmation = extract_label(block, "Prompt Confirmation")
        candidate_refs = extract_label(block, "Candidate References")
        image_confirmation = extract_label(block, "Image Confirmation")
        canonical_refs = extract_label(block, "Canonical References")
        empty_values = {None, "", "None", "Pending", "N/A", "Not Applicable", "Not Generated"}
        if prompt_revision in empty_values:
            errors.append(f"{asset_id} {visual_status} record missing: Prompt Revision")
        if image_prompts in empty_values:
            errors.append(f"{asset_id} {visual_status} record missing: Image Prompts")
        if visual_status in {"Prompt Confirmed", "Image Generated", "Asset Confirmed"} and prompt_confirmation in empty_values:
            errors.append(f"{asset_id} {visual_status} record missing: Prompt Confirmation")
        if visual_status == "Image Generated":
            if candidate_refs in empty_values:
                errors.append(f"{asset_id} Image Generated record missing: Candidate References")
            if status == "Active":
                errors.append(f"{asset_id} Image Generated must not use Status Active")
            if canonical_refs not in empty_values:
                errors.append(f"{asset_id} Image Generated must not have Canonical References before image confirmation")
        if visual_status == "Asset Confirmed":
            if candidate_refs in empty_values:
                errors.append(f"{asset_id} Asset Confirmed record missing: Candidate References")
            if image_confirmation in empty_values:
                errors.append(f"{asset_id} Asset Confirmed record missing: Image Confirmation")
            if canonical_refs in empty_values:
                errors.append(f"{asset_id} Asset Confirmed record missing: Canonical References")
            if status != "Active":
                errors.append(f"{asset_id} Asset Confirmed requires Status Active")
        if status == "Active" and visual_status != "Asset Confirmed":
            errors.append(f"{asset_id} Status Active requires Visual Production Status Asset Confirmed")
        if status in {"Approved", "Active"}:
            required = ("Active Version", "Immutable Traits", "Mutable State Dimensions", "Approval Basis")
            for field in required:
                if extract_label(block, field) is None:
                    errors.append(f"{asset_id} {status} record missing: {field}")
            refs = canonical_refs
            if refs is None:
                errors.append(f"{asset_id} {status} record missing: Canonical References")
        if status == "Active":
            active_by_id[asset_id] = active_by_id.get(asset_id, 0) + 1
    for asset_id, count in active_by_id.items():
        if count > 1:
            errors.append(f"Asset has multiple Active records: {asset_id}")
    if not headings:
        warnings.append("Asset registry contains no formal asset records yet")
    return report(errors, warnings, as_json)


def validate_artifact_ledger(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if path.is_dir():
        path = path / "artifact_registry.md"
    if not path.is_file():
        return report([f"Artifact ledger does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    for section in ("## Artifacts", "## Dependency Recheck"):
        if section not in text:
            errors.append(f"Artifact ledger missing section: {section}")
    artifact_ids = re.findall(r"^\|\s*(ART-\d{4})\s*\|", text, re.MULTILINE)
    if len(artifact_ids) != len(set(artifact_ids)):
        errors.append("Artifact ledger contains duplicate Artifact IDs")
    for revision in re.findall(r"\bREV-\d{4}\b", text):
        if not re.fullmatch(r"REV-\d{4}", revision):
            errors.append(f"Invalid artifact Revision ID: {revision}")
    return report(errors, warnings, as_json)


def validate_execution_ledger(path: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if path.is_dir():
        path = path / "execution_ledger.md"
    if not path.is_file():
        return report([f"Execution ledger does not exist: {path}"], warnings, as_json)
    text = read_text(path)
    for section in ("## Workflow Runs", "## Generation Attempts", "## Open Recovery Items"):
        if section not in text:
            errors.append(f"Execution ledger missing section: {section}")
    run_ids = re.findall(r"^\|\s*(RUN-\d{4})\s*\|", text, re.MULTILINE)
    if len(run_ids) != len(set(run_ids)):
        errors.append("Execution ledger contains duplicate Run IDs")
    attempt_rows: list[list[str]] = []
    in_attempts = False
    for line in text.splitlines():
        if line.strip() == "## Generation Attempts":
            in_attempts = True
            continue
        if in_attempts and line.startswith("## "):
            break
        if in_attempts and line.startswith("|") and not line.startswith("|---") and "Run ID" not in line:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 10:
                attempt_rows.append(cells)
    failures: dict[tuple[str, str], list[list[str]]] = {}
    for row in attempt_rows:
        target = row[2]
        failure_class = row[6]
        if failure_class and failure_class.lower() not in {"none", "n/a"}:
            failures.setdefault((target, failure_class), []).append(row)
    for (target, failure_class), rows in failures.items():
        rows.sort(key=lambda row: int(row[3]) if row[3].isdigit() else 0)
        if len(rows) >= 2 and rows[1][7].lower() in {"", "none", "n/a"}:
            errors.append(f"Second repeated failure requires Stable Downgrade: {target} / {failure_class}")
        if len(rows) >= 3 and rows[2][5] not in {"Returned Upstream", "Escalated"}:
            errors.append(f"Third repeated failure must return upstream: {target} / {failure_class}")
    return report(errors, warnings, as_json)


def validate_skill(root: Path, as_json: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    root = root.resolve()
    for name in ("SKILL.md", "config.md", "project_registry.json", "portable_project_status.md"):
        if not (root / name).is_file():
            errors.append(f"Missing skill file: {name}")
    for name in ("rules", "workflows", "knowledge", "templates", "references", "scripts"):
        if not (root / name).is_dir():
            errors.append(f"Missing skill directory: {name}")
    for relative in MODULE_FILES:
        if not (root / relative).is_file():
            errors.append(f"Missing production module file: {relative}")
    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        text = read_text(skill_path)
        if len(text.encode("utf-8")) > 18000:
            errors.append("SKILL.md exceeds the modular entrypoint hard limit of 18 KB")
        for forbidden_entrypoint_marker in ("### Canonical Portable State Schema", "Portable State Schema Gate"):
            if forbidden_entrypoint_marker in text:
                errors.append(f"SKILL.md duplicates an external owner: {forbidden_entrypoint_marker}")
        frontmatter_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not frontmatter_match:
            errors.append("SKILL.md has invalid YAML frontmatter boundaries")
        else:
            frontmatter_text = frontmatter_match.group(1)
            pairs = re.findall(r"^([A-Za-z0-9_-]+):\s*(.*)$", frontmatter_text, re.MULTILINE)
            frontmatter = {key: value.strip().strip("\"'") for key, value in pairs}
            allowed = {"name", "description", "license", "allowed-tools", "metadata"}
            unexpected = sorted(set(frontmatter) - allowed)
            if unexpected:
                errors.append(f"SKILL.md frontmatter has unexpected keys: {unexpected}")
            name = frontmatter.get("name", "")
            if name != "sd-film" or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                errors.append("SKILL.md frontmatter must use the valid hyphen-case name: sd-film")
            description = frontmatter.get("description", "")
            if not description:
                errors.append("SKILL.md frontmatter is missing description")
            elif len(description) > 1024 or "<" in description or ">" in description or description.startswith("[TODO:"):
                errors.append("SKILL.md frontmatter description violates length or placeholder rules")
            body = text[frontmatter_match.end():]
            if re.search(r"^[ ]{0,3}\[TODO:[^\n]*\][ \t]*$", body, re.MULTILINE):
                errors.append("SKILL.md contains an unfinished TODO placeholder")
    config_path = root / "config.md"
    if config_path.is_file() and len(read_text(config_path).encode("utf-8")) > 6000:
        errors.append("config.md exceeds the modular configuration hard limit of 6 KB")
    directors = root / "knowledge" / "visual_styles" / "directors"
    if directors.is_dir():
        files = sorted(directors.glob("*.md"))
        if not files:
            warnings.append("No director knowledge files found")
        for path in files:
            text = read_text(path)
            for section in DIRECTOR_SECTIONS:
                if f"## {section}" not in text:
                    errors.append(f"{path.name} missing director section: {section}")
            for marker in ("检索标签", "适用阶段", "使用边界", "核心区分"):
                if marker not in text:
                    errors.append(f"{path.name} missing director metadata marker: {marker}")
    for legacy_name in ("project_status.md", "project_bible.md", "asset_registry.md"):
        legacy_path = root / legacy_name
        if legacy_path.is_file() and "Legacy Project File Pointer" not in read_text(legacy_path):
            errors.append(f"Skill root still contains mutable project data: {legacy_name}")
    routing_errors_before = len(errors)
    routing_core_markers = {
        "SKILL.md": ("rules/state_source.md", "references/project_state_contract.md"),
        "config.md": ("Portable Baseline", "rules/state_source.md"),
        "rules/runtime_reload.md": ("Skill Version", "Build ID"),
        "rules/state_source.md": ("portable_project_status.md", "Active Project Root"),
        "rules/chat_compatibility.md": ("portable_project_status.md", "Active Project Root"),
        "rules/progression_rules.md": ("rules/completion_gate.md", "Last Successful Checkpoint"),
        "rules/activation_rules.md": ("Optional/Auxiliary", "Explicit-Only"),
        "rules/completion_gate.md": ("Completion Gate", "references/project_state_contract.md"),
        "rules/compatibility_mapping.md": ("STATE-07 Clip Production", "Storyboard"),
        "rules/resource_loading.md": ("Template Uniqueness", "workflows/11_video_generation_workflow.md"),
        "references/project_workspace.md": ("portable_project_status.md", "Active Project Root"),
        "references/project_state_contract.md": ("Canonical Portable State Schema", "portable_project_status.md"),
        "rules/01_pipeline_rules.md": ("rules/state_source.md", "references/project_workspace.md", "rules/chat_compatibility.md"),
        "workflows/01_project_setup_workflow.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
        "workflows/workflow_map.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
        "workflows/18_project_resume_workflow.md": ("rules/state_source.md", "references/project_workspace.md", "references/project_state_contract.md"),
    }
    for relative, required_markers in routing_core_markers.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"Chat/Work state routing file missing: {relative}")
            continue
        routing_text = read_text(path)
        for marker in required_markers:
            if marker not in routing_text:
                errors.append(f"Chat/Work state routing marker missing in {relative}: {marker}")
    if len(errors) > routing_errors_before:
        warnings.append("Run the routing validator for the complete state-writer report")
    forbidden_route_patterns = {
        "fixed Storyboard state": r"\bSTATE-07\s*(?:[｜|:]\s*)?Storyboard\b",
        "non-canonical STATE-06 label": r"\bSTATE-06\s+Shot Design\b",
        "non-canonical STATE-08 label": r"\bSTATE-08\s+Video Generation\b",
        "Storyboard inheritance override": r"Storyboard" + r"阶段应继承",
        "main-pipeline denial override": r"并不存在" + r"主流程里的",
    }
    for markdown_path in root.rglob("*.md"):
        markdown_text = read_text(markdown_path)
        for label, pattern in forbidden_route_patterns.items():
            if re.search(pattern, markdown_text, re.IGNORECASE):
                relative = markdown_path.relative_to(root).as_posix()
                errors.append(f"Legacy or overriding route phrase in {relative}: {label}")
    integration_checks = {
        "rules/02_asset_rules.md": ("FX-001", "FX Asset", "Visual Asset Production Gate", "Prompt Draft", "Image Generated", "Reference Asset Eligibility Strengthening", "Reference Selection / Routing", "参考资产按需路由，不是越多越好", "板凳参考说明"),
        "rules/03_prompt_rules.md": ("Prompt Attention / Control Allocation", "不声称能够直接或精准设置模型内部的交叉注意力数值", "提示词不是越长越好", "Blender / Unreal式严格物理仿真器", "高价值视觉关系", "低价值工程精度"),
        "workflows/03_asset_discovery_workflow.md": ("FX Asset Discovery", "15_fx_asset_workflow.md"),
        "workflows/07_visual_development_workflow.md": ("Performance Direction", "facial_action_language.md", "emotion_dynamics.md", "Sound Direction", "knowledge/lighting/index.md", "光源空间锚点", "focal_length_and_perspective.md", "全画幅等效倾向", "knowledge/color/index.md", "绿色—品红偏色", "肤色、眼白", "17_poster_design_workflow.md"),
        "references/module_contracts.md": ("Authority Matrix", "ID Namespace Isolation", "Script Adaptation And Optimization Gate Module Contract", "四种Script Status值合法", "MUSIC / SEED-MUSIC Score Module Contract", "默认模式", "专业Spotting不变量", "SeedMusic不变量", "视频隔离不变量", "STATE-03 Visual Asset Production Contract", "Sequence Module Contract", "Poster Design Module Contract", "Camera Composition Knowledge Contract", "Focal Length Knowledge Contract", "FLN-01至FLN-07", "Camera Movement Combination Knowledge Contract", "CMG-01至CMG-16", "Camera Movement Selection Matrix Knowledge Contract", "Color Knowledge Contract", "CLR-01至CLR-09", "Performance Expression Knowledge Contract", "Lighting Knowledge Contract", "Prompt Compilation Module Contract", "多Clip项目默认每轮只交付当前一个Clip", "Transition Knowledge Contract"),
        "knowledge/script_adaptation.md": ("Optimization Opportunity Report", "User Decision Gate", "Source Essence Extraction", "Adaptation Objective", "Preserve / Compress / Rewrite / Remove Decision", "Screen Translation", "Duration & Dramatic Restructuring", "Adaptation Fidelity Check", "LEVEL 1", "LEVEL 2", "LEVEL 3", "基本不要改剧情", "short_form_drama_adapter.md"),
        "knowledge/adaptation/short_form_drama_adapter.md": ("前3秒", "前30秒", "1个核心事件", "角色功能", "核心欲望", "性格标签", "标志动作", "语言特征", "视觉记忆点", "通常控制在7字左右", "1个主情绪", "爽 / 虐 / 甜 / 惊 / 燃 / 笑 / 悬", "Hook → Setup → Escalation → Payoff → Next Hook", "不是死时间码"),
        "workflows/02_script_analysis_workflow.md": ("Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate", "开场钩子", "核心冲突进入时机", "信息重复", "台词效率", "动作可视化", "人物记忆点", "节奏", "高潮力度", "情绪价值", "结尾Hook", "时长适配", "场景/人物复杂度", "A 无明显优化必要", "B 有轻度优化空间", "C 有明显结构问题", "拒绝优化或改编", "Production Script Proposal输出后必须再次停止", "A — Production Script", "B — Rough Script / First Draft", "C — Source Material", "Adaptation Target Detection", "Script Adaptation", "Adaptation Draft", "short_form_drama_adapter.md", "No Revision / Final Script"),
        "templates/02_script_analysis_prompt.md": ("Optimization Opportunity Report", "问题或已成立依据", "影响", "可优化方向", "是否执行轻度优化？", "是否进入结构优化？", "Input Class", "Adaptation Target", "Adaptation Intensity", "Adapter Load", "Source Essence", "Adaptation Decision", "Adaptation Draft", "Adaptation Fidelity Check", "Production Script Proposal"),
        "workflows/04_character_asset_workflow.md": ("Image Prompt Generation", "Prompt Confirmation Gate", "Image Confirmation Gate", "Visual Production Status: Asset Confirmed"),
        "workflows/05_environment_asset_workflow.md": ("Main Reference Image Prompt", "Required Multi-View Prompts", "Image Generated", "Visual Production Status: Asset Confirmed"),
        "workflows/06_prop_asset_workflow.md": ("Main Reference Image Prompt", "Required State Variant Prompts", "Image Generated", "Visual Production Status: Asset Confirmed"),
        "templates/04_character_asset_prompt.md": ("Three-View Character Sheet Prompt", "Face Close-Up Prompt", "Required State Variant Prompts", "Awaiting User Confirmation", "Asset Confirmed"),
        "templates/05_environment_asset_prompt.md": ("Main Reference Image Prompt", "Required Multi-View Prompts", "Key Area / Detail Prompts", "Awaiting User Confirmation", "Asset Confirmed"),
        "templates/06_prop_asset_prompt.md": ("Main Reference Image Prompt", "Required State Variant Prompts", "Required Detail Prompts", "Awaiting User Confirmation", "Asset Confirmed"),
        "workflows/08_scene_breakdown_workflow.md": ("Sequence Eligibility", "16_sequence_planning_workflow.md", "Source Script Label", "不得创建或预留"),
        "workflows/16_sequence_planning_workflow.md": ("Trigger Gate", "Coverage Matrix", "State Ledger", "不得创建SHOT ID", "UNIT是", "不得创建CLIP ID"),
        "workflows/09_shot_design_workflow.md": ("Professional Detailed Shot Script", "TC IN", "TC OUT", "时长(s)", "画面内容 / 构图", "镜头调度", "摄影机运动 + 人物调度", "光线 / 色彩", "台词 / 旁白 / 口播", "同期声音设计", "AI制作备注", "素材 / 资产", "Performance Goal", "facial_action_language.md", "公开状态与内部泄漏", "Sound Purpose", "FX Behavior", "Coverage Mapping", "Coverage Completion", "Composition Intent", "Camera Language Integrity", "Camera Language Decision Gate", "selection_matrix.md", "实际读取的主运镜原子知识文件", "Focal Length Design", "focal_length_and_perspective.md", "knowledge/color/index.md", "CLR-01至CLR-09", "肤色漂移", "director_patterns/index.md", "knowledge/lighting/index.md", "起始光态", "高风险模式的基础镜头降级方案", "movement_combinations/index.md", "Low-Complexity Compound Path", "knowledge/transitions/", "Outgoing Anchor", "Direct Cut降级", "Source Script Label", "Artifact Revision"),
        "workflows/10_clip_production_workflow.md": ("STATE-07 Clip Production", "Professional Detailed Shot Script", "TC OUT - TC IN = 时长(s)", "画面内容/构图", "镜头调度", "光线/色彩", "Shot", "Clip", "Prompt", "Build Clip Candidates", "Author Clip Execution Contract", "Clip Movement Plan", "主导镜头语言", "超过4个Shot", "连续出现3次", "Duration And Continuity Ledger", "Shot-State Memory", "Clip End-State Record / Next-Clip Carryover", "Character State / Spatial State / Prop State / Camera State / Environment State / Performance State / Continuity Risks / Next-Clip Carryover", "Reference Selection / Routing", "Tail Frame Required = YES / NO", "待用户提供/待上传", "Visual Input Eligibility", "这是不是一张实际会被投喂/引用的视觉资产", "templates/20_clip_plan.md", "每个 Clip", "Source Script Label", "--project-status", "--shot-design"),
        "workflows/10_storyboard_workflow.md": ("Optional / Auxiliary", "不绑定任何固定 STATE", "用户明确要求", "templates/09_storyboard_prompt.md", "不得进入 STATE-08"),
        "workflows/11_video_generation_workflow.md": ("knowledge/performance/", "Attention Shift", "Control / Leakage", "瞳孔地震", "knowledge/sound_language/", "knowledge/fx/", "knowledge/lighting/", "knowledge/color/", "Color Execution", "综合色彩闪变", "focal_length_and_perspective.md", "全画幅等效倾向", "movement_combinations/", "Low-Complexity Compound Path", "Camera Language Decision Hard Gate", "Clip Movement Plan Hard Gate", "selection_matrix.md", "禁止把“缓慢推进”", "Sequence Plan", "Sequence And Unit Continuity", "Sequence Coverage Check", "state08_projection.md", "Semantic Projection Check", "Projection Ledger", "结束光态", "knowledge/transitions/", "禁止生成背景音乐", "Outgoing Anchor", "Clip End-State Record / Next-Clip Carryover", "Reference Selection / Routing", "Tail Frame Required = YES / NO", "待用户提供/待上传", "Visual Input Eligibility", "板凳参考说明", "Single-Clip Checkpoint", "First-Frame Check", "End-Frame Interface Check", "Cross-Clip Continuity Check", "Five-Dimensional Prompt Control Matrix", "Prompt Compression Pass", "Prompt Attention / Compression Check"),
        "workflows/13_review_workflow.md": ("FX Review", "Performance Review", "表情符合角色基线", "公开状态、短暂泄漏", "Sound Review", "Sequence Coverage Review", "Camera Language QA", "Clip End-State Record / Next-Clip Carryover", "Reference Selection / Routing", "人物/道具重置", "相机轴线跳变", "连续慢推", "超过4个Shot", "连续3次", "焦段倾向、摄影机距离", "背景尺度抽动", "主色、辅助色、强调色", "白平衡抽动", "Prompt Attention / Control Allocation", "Blender / Unreal式严格物理仿真器"),
        "templates/01_project_bible_template.md": ("Performance Direction", "角色中性面部", "压抑 / 伪装 / 混合情绪", "FX Direction", "Sound Direction", "FX Continuity", "光源空间锚点与方向", "跨镜光影连续性", "全画幅等效倾向", "焦段不自动等于景别", "绿色—品红偏色", "Color模式语义"),
        "templates/03_asset_discovery_prompt.md": ("正式FX Asset / Inline Effect / 后期合成待定", "15_fx_asset_workflow.md"),
        "templates/08_shot_design_prompt.md": ("Professional Detailed Shot Script Template", "镜号", "TC IN", "TC OUT", "时长(s)", "景别", "焦段", "场景 / 美术", "画面内容 / 构图", "人物动作", "摄影机 / 镜头", "摄影参数", "镜头调度", "光线 / 色彩", "画面特效 / 转场", "台词 / 旁白 / 口播", "同期声音设计", "AI制作备注", "素材 / 资产", "摄影机运动", "人物调度", "镜头结束状态", "前景、中景、背景", "Start Boundary", "End-Frame Constraint", "Next-Shot Handoff", "Director Decision Layer必须读取已经完成的专业分镜表", "templates/10_video_prompt.md", "Artifact Revision", "Source Script Labels"),
        "workflows/music_router.md": ("ROUTE: MUSIC / SEED-MUSIC Score", "ROUTE: ORIGINAL WORKFLOW", "INSTRUMENTAL", "SILENCE / PRODUCTION SOUND ONLY", "CLIP-006"),
        "workflows/21_seed_music_score_workflow.md": ("Optional/Auxiliary", "Explicit Trigger Evidence", "Professional Spotting Pass", "Music Bible", "MUS-CUE-001", "Related Clip(s)", "style + structure", "INSTRUMENTAL", "不得生成SeedMusic Prompt", "固定背景音乐禁令"),
        "knowledge/music_score/index.md": ("Music / Score", "Explicit", "spotting_and_silence.md", "music_bible_and_cues.md", "seedmusic_prompting.md", "STATE-08永久禁止"),
        "knowledge/music_score/spotting_and_silence.md": ("MUSIC CUE", "SILENCE / PRODUCTION SOUND ONLY", "DIEGETIC MUSIC ONLY", "MUSIC OUT", "CARRY-OVER", "Dialogue Protection"),
        "knowledge/music_score/music_bible_and_cues.md": ("Music Bible", "Motif", "Emotional And Rhythmic Strategy", "Transition Cue", "Silence Before And After"),
        "knowledge/music_score/seedmusic_prompting.md": ("Instrumental Music Generation", "style", "structure", "[Verse]: 0s", "no vocals", "Related Clip(s)", "Continuation", "Style Transfer"),
        "templates/22_seed_music_score.md": ("# MUSIC / SEED-MUSIC Score Package", "Explicit Trigger Evidence", "Generation Mode", "## Spotting Map", "SILENCE / PRODUCTION SOUND ONLY", "## Cue Sheet", "MUS-CUE-001", "Related Clip(s)", "style:", "structure:", "[Verse]: 0s", "Clip归属"),
        "references/professional_detailed_shot_script_example.md": ("Professional Detailed Shot Script", "Total Shots：4", "00:00:00.000", "00:00:23.000", "SHOT-001", "SHOT-002", "SHOT-003", "SHOT-004", "摄影机运动", "人物调度", "结束状态", "前景：", "中景：", "背景：", "叙事功能", "Start Boundary", "End-Frame", "Next", "素材 / 资产", "不包含Director Decision Notes或Knowledge Reflection"),
        "templates/20_clip_plan.md": ("# Clip Plan", "Source Detailed Shot Design Artifact / Portable Checkpoint", "Source Detailed Shot Design Status", "Source Detailed Shot Design Revision", "Unit Rule", "Namespace Rule", "包含 Shot", "起始状态", "连续动作", "Clip Movement Plan", "主导镜头语言", "视觉高潮镜头", "最克制镜头", "重复规避", "Seedance复杂度控制", "空间关系", "道具连续性", "结尾状态", "Clip End-State Record / Next-Clip Carryover", "Character State", "Continuity Risks", "Reference Selection / Routing", "Tail Frame Required = YES / NO", "待用户提供/待上传", "Visual Input Eligibility", "NOT ELIGIBLE", "每个Clip只生成一条连续Prompt"),
        "templates/09_storyboard_prompt.md": ("Optional / Auxiliary", "不绑定固定 STATE", "不是 STATE-08", "Production Isolation Note"),
        "templates/14_sequence_plan.md": ("## Beat Map", "## Coverage Matrix", "## Generation Units", "## State Ledger", "No CLIP ID", "UNIT是"),
        "workflows/17_poster_design_workflow.md": ("Trigger Gate", "Poster Brief", "Narrative Promise", "Exact Copy Ledger", "Base-image Prompt", "Rights Gate", "不得标记完成"),
        "templates/15_poster_design_package.md": ("# Poster Design Package", "Aspect Ratio / Delivery Format", "Primary Visual Motif", "Primary Composition Model", "Exact Copy Ledger", "Base Layer:", "Type Layer:", "Composite Layer:", "Delivery Versions:", "Quality Check"),
        "knowledge/poster_design/index.md": ("Activation Gate", "Authority Boundary", "Required Reading"),
        "knowledge/poster_design/typography_and_layers.md": ("Exact Text Rule", "Layered Production Model", "Base-image Prompt"),
        "knowledge/poster_design/reference_rights_and_qc.md": ("Reference Role Classification", "Rights Gate", "Evaluation Rubric"),
        "knowledge/camera_language/index.md": ("Director Shot Patterns", "camera_movement/selection_matrix.md", "movement_combinations/index.md", "image_source_coverage.md", "composition_image_source_coverage.md", "focal_length_image_source_coverage.md"),
        "knowledge/camera_language/composition_language/index.md": ("foundations.md", "低/高机位", "Perspective"),
        "knowledge/camera_language/camera_movement/index.md": ("selection_matrix.md", "禁止未检索", "tilt.md", "Crane vs Tilt"),
        "knowledge/camera_language/camera_movement/selection_matrix.md": ("Module Contract", "Actual Retrieval Gate", "Seedance Stability Levels", "Selection Matrix", "Camera Language Decision Record", "Diverse, Not Chaotic", "超过4个 Shot", "连续出现3次", "STATE-08 Translation Rule"),
        "knowledge/camera_language/camera_angle/index.md": ("dutch_angle.md", "Dutch Angle"),
        "knowledge/camera_language/perspective_language/index.md": ("over_shoulder.md", "Over-the-Shoulder"),
        "knowledge/camera_language/lens_language/focus_and_optics.md": ("Rack Focus", "Optical Zoom", "Dolly Zoom"),
        "knowledge/camera_language/lens_language/framing_and_scale.md": ("Canonical Shot Scale", "Extreme Close-Up"),
        "knowledge/camera_language/lens_language/index.md": ("focal_length_and_perspective.md", "focal_length_patterns.md", "focal_length_continuity.md", "focal_length_image_source_coverage.md", "焦段不自动提升质感"),
        "knowledge/camera_language/lens_language/focal_length_and_perspective.md": ("Core Corrections", "Atomic Lens Model", "14–20mm", "181mm+", "Prompt Compiler", "最终Prompt不输出内部FLN编号"),
        "knowledge/camera_language/lens_language/focal_length_patterns.md": ("FLN-01", "FLN-07", "Selection Rule", "Prompt Quality Gate"),
        "knowledge/camera_language/lens_language/focal_length_continuity.md": ("Continuity Ledger", "Identity And Edge Safety", "Motion Interaction", "STATE-08 Projection"),
        "knowledge/camera_language/director_patterns/index.md": ("Authority Boundary", "Stability Gate", "STATE-08", "advanced_composition.md", "action_composition.md", "character_composition.md", "atmosphere_composition.md"),
        "knowledge/knowledge_application_reflection.md": ("Director / Literary Intent Translation", "保留情绪功能", "至少落到一种可见或可听执行项", "五维未锁定项检查"),
        "knowledge/prompt_compilation/state08_projection.md": ("Fixed-Template Projection Gate", "Global Projection Matrix", "Per-Shot Projection Matrix", "Internal Projection Ledger", "Semantic And Structure Loss Check", "CMG编号", "CLR编号", "FLN编号", "四项硬门槛", "Tail Frame Required = YES / NO", "待用户提供/待上传", "禁止生成背景音乐", "完整Clip", "不得文字重定义", "Prompt Attention / Control Allocation Gate", "Five-Dimensional Prompt Control Matrix", "Director Intent / Literary Intent → Visual Translation → Physical Anchoring → Prompt Compression → Final Clip Prompt", "Blender / Unreal式严格物理仿真"),
        "knowledge/11_seedance_adapter.md": ("state08_projection.md", "主体画面位置", "构图主原子与支持层", "knowledge/color/index.md", "不得输出CLR编号", "focal_length_and_perspective.md", "焦段不自动提高画面质感", "knowledge/lighting/index.md", "LGT模式ID", "knowledge/performance/index.md", "Attention Shift", "PEX/AU编号", "knowledge/camera_language/movement_combinations/", "knowledge/transitions/", "背景音乐", "Delivery Mode Gate", "Four-Part Boundary Gate", "Physical Data Value Rule", "0.137m/s", "Blender / Unreal式物理仿真"),
        "templates/10_video_prompt.md": ("唯一允许的最终模板", "# CLIP-X｜标题 Seedance视频提示词", "七项强制完整性规则", "所有 Clip 必须使用完全相同的字段结构", "不得因为批量输出", "自动分批输出", "参考资产：", "首帧参考：", "尾帧限制：", "音色特征：", "Clip End-State Record / Next-Clip Carryover", "参考资产按需路由，不是越多越好", "Tail Frame Required = YES / NO", "待用户提供/待上传", "Visual Input Eligibility", "这是不是一张实际会被投喂/引用的视觉资产", "板凳参考说明", "每个分镜必须完整重复十个固定字段", "任何已有旧模板", "输出前字段完整性检查", "不得另增“与下一镜衔接”字段", "禁止生成背景音乐", "Prompt Attention / Compression", "Active Character Canonical References", "生成模型不被表述为严格物理仿真器"),
        "knowledge/clip_preflight_check.md": ("Four Global High-Priority Rules", "Visual Input Eligibility Test", "Reference Selection / Routing", "Clip End-State Record / Next-Clip Carryover", "参考资产按需路由，不是越多越好", "NOT ELIGIBLE", "板凳参考说明", "九个Acceptance Scenarios"),
        "knowledge/reference_budget.md": ("Visual Input Eligibility", "0个图片位", "板凳参考说明", "Projected Final Count"),
        "references/regression_scenarios.md": ("R13 Cross-Clip End-State And Reference Routing", "R13-A Same-Shot Direct Continuation", "R13-B New Shot With Tail Position Reference", "R13-C New Shot Without Tail Reference", "Clip End-State Record / Next-Clip Carryover", "R14 Reference Asset Eligibility", "1—5号保持不动", "板凳参考说明", "PROP-BENCH-01", "R15-A Literary Camera Intent", "R15-B Over-Engineered Camera Data", "R15-C Canonical Assets Free Prompt Attention"),
        "knowledge/camera_language/movement_combinations/index.md": ("Foundations", "Decision Engine", "Combination Patterns", "Continuity And Projection", "Image Source Coverage", "Activation Gate"),
        "knowledge/camera_language/movement_combinations/foundations.md": ("Four Execution Classes", "One-Shot Compatibility Test", "Compatibility Matrix", "Split Triggers", "Stability Budget"),
        "knowledge/camera_language/movement_combinations/decision_engine.md": ("Gate 0", "Class A", "Coverage Sequence", "Transition / FX Sequence", "Stable Downgrade", "CMG-xx"),
        "knowledge/camera_language/movement_combinations/continuity_and_projection.md": ("Combination Ledger", "Axis And Screen Direction", "STATE-06 Projection", "STATE-08 Projection", "CMG编号"),
        "knowledge/camera_language/movement_combinations/image_source_coverage.md": ("六张附件", "CMG-01", "CMG-16", "景别表", "Stable Downgrade"),
        "knowledge/transitions/index.md": ("foundations.md", "decision_engine.md", "transition_patterns.md", "transition_continuity.md", "image_source_coverage.md", "Direct Cut", "Unresolved Handoff"),
        "knowledge/transitions/decision_engine.md": ("Gate 0", "Boundary", "One Primary", "Outgoing Anchor", "禁止生成背景音乐", "TRN-01"),
        "knowledge/transitions/transition_continuity.md": ("Transition Ledger", "Cut Point", "STATE-08 Projection", "Direct Cut", "背景音乐"),
        "knowledge/transitions/image_source_coverage.md": ("11 张", "Camera Movement", "Direct Cut", "High-Risk", "背景音乐"),
        "knowledge/performance/index.md": ("facial_action_language.md", "emotion_dynamics.md", "expression_patterns.md", "STATE-08"),
        "knowledge/performance/micro_expression.md": ("Attention Shift / Appraisal", "Expression Is Conditional", "微表情是短暂泄漏"),
        "knowledge/performance/facial_action_language.md": ("FACS-Inspired Action Regions", "Eye And Attention Language", "Conditional Physiology", "Shot-Scale Visibility"),
        "knowledge/performance/emotion_dynamics.md": ("Emotion Is A Process", "Mixed Emotion And Subtext", "Suppression And Leakage", "Performance Continuity Ledger", "Stable Downgrade"),
        "knowledge/performance/expression_patterns.md": ("PEX-01", "PEX-36", "Selection Rule"),
        "knowledge/lighting/index.md": ("Module Contract", "STATE-04", "STATE-08", "source_patterns.md", "lighting_continuity.md"),
        "knowledge/lighting/foundations.md": ("Atomic Lighting Model", "Responsibility Boundary", "低调光", "丁达尔光", "Prompt Quality Gate"),
        "knowledge/lighting/source_patterns.md": ("LGT-01", "LGT-20", "Stable Downgrade"),
        "knowledge/lighting/lighting_continuity.md": ("Continuity Ledger", "Interaction Matrix", "STATE-08 Projection"),
        "knowledge/color/index.md": ("Module Contract", "STATE-04", "STATE-08", "tone_patterns.md", "color_continuity.md"),
        "knowledge/color/foundations.md": ("Core Corrections", "Atomic Color Model", "Responsibility Boundary", "Skin And Neutral Rule", "Prompt Compiler", "Prompt Quality Gate"),
        "knowledge/color/tone_patterns.md": ("CLR-01", "CLR-09", "Selection Rule"),
        "knowledge/color/color_continuity.md": ("Continuity Ledger", "Lighting Interaction", "STATE-08 Projection", "Stable Downgrade"),
        "SKILL.md": ("Skill Version", "Build ID", "## System Role", "## Production Pipeline", "## STATE Overview", "## Global Priority", "## Activation Entry", "## Runtime Reload Entry", "## Main Workflow Routing", "## Auxiliary Workflow Routing", "## External Rules Index", "## Essential Invariants", "STATE-07 Clip Production", "STATE-08 Clip-based Video Prompt / Video Generation", "templates/10_video_prompt.md"),
        "rules/runtime_reload.md": ("Reload Sequence", "Skill Definition", "Project Context", "Compatibility Mapping Result"),
        "rules/state_source.md": ("Selection Priority", "当前可验证的Project Context", "Project ID不一致", "Storyboard只能"),
        "rules/chat_compatibility.md": ("普通Chat不是缩减模式", "Portable Execution", "Behavior Parity"),
        "rules/progression_rules.md": ("Advance Gate", "Authorization Boundary", "纯推进命令"),
        "rules/activation_rules.md": ("Intent Is Goal, Not Current State", "Optional Storyboard Isolation", "AUDIO / SEED-AUDIO Explicit-Only"),
        "rules/completion_gate.md": ("Completion Decision", "STATE-03", "STATE-07", "STATE-08", "Persistence"),
        "rules/compatibility_mapping.md": ("Preservation Set", "Canonical Route", "Legacy Storyboard Mislabel Mapping", "Portable Schema Migration"),
        "rules/resource_loading.md": ("Loading Order", "Actual Read Gate", "Responsibility Boundaries", "Template Uniqueness"),
        "references/project_state_contract.md": ("Canonical Portable State Schema", "State Status: NOT_STARTED", "Next Workflow: 01_project_setup_workflow.md", "## State Control"),
        "references/project_state_contract.md": ("State Status", "Last Successful Checkpoint", "Review Result", "Revision ID", "Source Material", "Adaptation Draft", "Optimized Proposal", "Production-Locked"),
        "references/asset_lock_contract.md": ("Active Version", "Canonical Reference", "Immutable Traits", "Supersedes"),
        "references/artifact_revision_contract.md": ("Generation Run Record", "Retry Isolation", "Based On", "Accepted"),
        "knowledge/quality/index.md": ("shot_qa.md", "continuity_pair_qa.md", "execution_risk.md", "prompt_scorecard.md"),
        "knowledge/camera_language/shot_language_router.md": ("Routing Order", "Execution Risk", "Stable Downgrade"),
        "workflows/18_project_resume_workflow.md": ("Trigger Gate", "Last Safe Checkpoint", "Retry Decision", "不得"),
        "templates/16_review_report.md": ("Shot-Level QA", "Adjacent-Shot Continuity QA", "Return Control", "Completion Decision"),
    }
    for relative, required_terms in integration_checks.items():
        path = root / relative
        if not path.is_file():
            continue
        text = read_text(path)
        for term in required_terms:
            if term not in text:
                errors.append(f"{relative} is missing module integration marker: {term}")
    pattern_specs = (
        ("knowledge/camera_language/director_patterns/emotional_patterns.md", "EMO-", 20),
        ("knowledge/camera_language/director_patterns/dynamic_patterns.md", "DYN-", 20),
        ("knowledge/camera_language/director_patterns/advanced_composition.md", "ADV-C", 16),
        ("knowledge/camera_language/director_patterns/action_composition.md", "ACT-C", 16),
        ("knowledge/camera_language/director_patterns/character_composition.md", "CHR-C", 16),
        ("knowledge/camera_language/director_patterns/atmosphere_composition.md", "ATM-C", 16),
        ("knowledge/lighting/source_patterns.md", "LGT-", 20),
        ("knowledge/performance/expression_patterns.md", "PEX-", 36),
        ("knowledge/camera_language/lens_language/focal_length_patterns.md", "FLN-", 7),
        ("knowledge/color/tone_patterns.md", "CLR-", 9),
        ("knowledge/transitions/transition_patterns.md", "TRN-", 30),
        ("knowledge/camera_language/movement_combinations/combination_patterns.md", "CMG-", 16),
    )
    for relative, id_prefix, expected_count in pattern_specs:
        path = root / relative
        if not path.is_file():
            continue
        ids = re.findall(rf"^\| ({re.escape(id_prefix)}\d{{2}}) \|", read_text(path), re.MULTILINE)
        expected = [f"{id_prefix}{number:02d}" for number in range(1, expected_count + 1)]
        if ids != expected:
            errors.append(f"{relative} must define {id_prefix}01 through {id_prefix}{expected_count:02d} exactly once: found {ids}")
    image_coverage = root / "knowledge" / "camera_language" / "image_source_coverage.md"
    if image_coverage.is_file():
        coverage_rows = []
        for line in read_text(image_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源术语"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 80:
            errors.append(f"Image source coverage must contain exactly 80 source rows: found {len(coverage_rows)}")
        for marker in ("推近压迫镜头", "过肩镜头 Over-the-Shoulder", "顶视旋落镜头", "快速推进变焦"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Image source coverage is missing representative source term: {marker}")
    composition_coverage = root / "knowledge" / "camera_language" / "composition_image_source_coverage.md"
    if composition_coverage.is_file():
        coverage_rows = []
        for line in read_text(composition_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源术语"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 80:
            errors.append(f"Composition image source coverage must contain exactly 80 source rows: found {len(coverage_rows)}")
        for marker in ("居中对称构图", "消失点压缩构图", "坠物压境构图", "远近同框异步构图", "顶部压顶构图"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Composition image source coverage is missing representative source term: {marker}")
    lighting_coverage = root / "knowledge" / "lighting" / "image_source_coverage.md"
    if lighting_coverage.is_file():
        coverage_rows = []
        for line in read_text(lighting_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源术语"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 20:
            errors.append(f"Lighting image source coverage must contain exactly 20 source rows: found {len(coverage_rows)}")
        for marker in ("黄金时刻光", "伦勃朗光", "丁达尔光", "反光板光", "水下光", "火光"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Lighting image source coverage is missing representative source term: {marker}")
    expression_coverage = root / "knowledge" / "performance" / "expression_image_source_coverage.md"
    if expression_coverage.is_file():
        coverage_rows = []
        for line in read_text(expression_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 8:
            errors.append(f"Expression image source coverage must contain exactly 8 source rows: found {len(coverage_rows)}")
        for marker in ("坚定", "惊讶", "哭泣", "微笑", "妒忌", "瞳孔地震", "泪水", "公开状态"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Expression image source coverage is missing representative source term: {marker}")
    focal_coverage = root / "knowledge" / "camera_language" / "lens_language" / "focal_length_image_source_coverage.md"
    if focal_coverage.is_file():
        coverage_rows = []
        for line in read_text(focal_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源图片"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 3:
            errors.append(f"Focal-length image source coverage must contain exactly 3 source rows: found {len(coverage_rows)}")
        for marker in ("14", "18", "24", "35", "50", "85", "135", "200mm"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Focal-length image source coverage is missing representative source term: {marker}")
    color_coverage = root / "knowledge" / "color" / "image_source_coverage.md"
    if color_coverage.is_file():
        coverage_rows = []
        for line in read_text(color_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源图片"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 3:
            errors.append(f"Color image source coverage must contain exactly 3 source rows: found {len(coverage_rows)}")
        for marker in ("冷色调", "暖色调", "青橙", "高饱和", "低饱和", "暗黑", "霓虹", "糖果", "小清新"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Color image source coverage is missing representative source term: {marker}")
    movement_combo_coverage = root / "knowledge" / "camera_language" / "movement_combinations" / "image_source_coverage.md"
    if movement_combo_coverage.is_file():
        coverage_rows = []
        for line in read_text(movement_combo_coverage).splitlines():
            if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 来源图片"):
                continue
            coverage_rows.append(line)
        if len(coverage_rows) != 6:
            errors.append(f"Movement-combination image source coverage must contain exactly 6 source rows: found {len(coverage_rows)}")
        for marker in ("常规对手戏", "悲伤崩溃", "法术战斗", "常规打斗", "时间流逝", "POV"):
            if not any(marker in row for row in coverage_rows):
                errors.append(f"Movement-combination image source coverage is missing representative source term: {marker}")
    video_template = root / "templates" / "10_video_prompt.md"
    if video_template.is_file():
        template_text = read_text(video_template)
        for section in GLOBAL_SECTIONS + ENDING_SECTIONS:
            if section not in template_text:
                errors.append(f"STATE-08 template is missing canonical section: {section}")
        for field in SHOT_FIELDS:
            if field not in template_text:
                errors.append(f"STATE-08 template is missing canonical shot field: {field}")
        for invariant in (
            "# CLIP-X｜标题 Seedance视频提示词",
            "平台生成时长",
            "每个分镜必须完整重复十个固定字段",
            "合法首尾帧",
            "下一 Clip 预计如何继承或重建",
            "A【同镜头连续承接",
            "B【新镜头参考型",
            "C【新镜头且无需尾帧",
            "同镜头连续承接用途",
            "空间/站位/景别参考用途",
            "B不得使用A类",
            "最后 1 秒不得",
            "禁止生成背景音乐",
            "完整 Clip 之后分批",
            "任何已有旧模板",
            "输出前字段完整性检查",
        ):
            if invariant not in template_text:
                errors.append(f"STATE-08 template is missing Clip package invariant: {invariant}")
    workflow_map = root / "workflows" / "workflow_map.md"
    if workflow_map.is_file():
        state_rows = [int(value) for value in re.findall(r"^\|\s*STATE-(\d{2})\s*\|", read_text(workflow_map), re.MULTILINE)]
        if state_rows != list(range(10)):
            errors.append(f"Main Workflow Table must contain STATE-00 through STATE-09 exactly once: found {state_rows}")
    template_owners = {
        "workflows/01_project_setup_workflow.md": ("templates/00_project_start_template.md",),
        "workflows/02_script_analysis_workflow.md": ("templates/02_script_analysis_prompt.md",),
        "workflows/03_asset_discovery_workflow.md": ("templates/03_asset_discovery_prompt.md",),
        "workflows/04_character_asset_workflow.md": ("templates/04_character_asset_prompt.md",),
        "workflows/05_environment_asset_workflow.md": ("templates/05_environment_asset_prompt.md",),
        "workflows/06_prop_asset_workflow.md": ("templates/06_prop_asset_prompt.md",),
        "workflows/07_visual_development_workflow.md": ("templates/01_project_bible_template.md",),
        "workflows/08_scene_breakdown_workflow.md": ("templates/07_scene_design_prompt.md",),
        "workflows/09_shot_design_workflow.md": ("templates/08_shot_design_prompt.md",),
        "workflows/10_clip_production_workflow.md": ("templates/20_clip_plan.md",),
        "workflows/10_storyboard_workflow.md": ("templates/09_storyboard_prompt.md",),
        "workflows/11_video_generation_workflow.md": ("templates/10_video_prompt.md",),
        "workflows/12_editing_workflow.md": ("templates/12_edit_prompt.md",),
        "workflows/13_review_workflow.md": ("templates/16_review_report.md",),
        "workflows/14_series_management_workflow.md": ("templates/19_series_status.md",),
        "workflows/15_fx_asset_workflow.md": ("templates/13_fx_asset_prompt.md",),
        "workflows/16_sequence_planning_workflow.md": ("templates/14_sequence_plan.md",),
        "workflows/17_poster_design_workflow.md": ("templates/15_poster_design_package.md",),
        "workflows/18_project_resume_workflow.md": ("templates/17_execution_ledger.md", "templates/18_artifact_revision_ledger.md"),
    }
    for workflow_relative, templates in template_owners.items():
        workflow_path = root / workflow_relative
        if not workflow_path.is_file():
            continue
        workflow_text = read_text(workflow_path)
        for template_relative in templates:
            if template_relative not in workflow_text:
                errors.append(f"{workflow_relative} does not declare template owner: {template_relative}")
    reference_pattern = re.compile(r"(?:knowledge|workflows|templates|rules|references|scripts)/[A-Za-z0-9_./-]+\.(?:md|py|json)")
    missing_references: set[str] = set()
    for markdown_path in root.rglob("*.md"):
        for relative in reference_pattern.findall(read_text(markdown_path)):
            target = root / Path(relative)
            if not target.is_file():
                missing_references.add(relative)
    for relative in sorted(missing_references):
        errors.append(f"Broken internal file reference: {relative}")
    return report(errors, warnings, as_json)


def init_project(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    registry_path = Path(args.registry).resolve()
    try:
        registry = load_json(registry_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL\nERROR: Invalid registry: {exc}")
        return 1
    projects = registry.get("projects")
    if registry.get("schema_version") != 1 or not isinstance(projects, list):
        print("FAIL\nERROR: Registry must use schema_version 1 and contain a projects array")
        return 1
    normalized_root = str(root).casefold()
    for item in projects:
        if not isinstance(item, dict):
            continue
        if str(item.get("project_id", "")).strip() == args.project_id:
            print(f"FAIL\nERROR: Project ID already exists in registry: {args.project_id}")
            return 1
        if str(Path(str(item.get("root", ""))).resolve()).casefold() == normalized_root:
            print(f"FAIL\nERROR: Project root already exists in registry: {root}")
            return 1
    if root.exists() and any(root.iterdir()):
        print(f"FAIL\nERROR: Refusing to overwrite non-empty project root: {root}")
        return 1
    root.mkdir(parents=True, exist_ok=True)
    created = date.today().isoformat()
    manifest = {"schema_version": 1, "project_id": args.project_id, "project_name": args.name, "project_type": args.project_type, "created_at": created, "source_material": args.source_material or "待登记"}
    (root / "project_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    status_text = f"""# SD Film Project Status

## State Control

- Status Schema Version：2
- Project ID：{args.project_id}
- Project Name：{args.name}
- Current State：STATE-00
- State Status：COMPLETE
- Script Status：Source Material
- Active Workflow：None
- Last Completed Step：STATE-00 Project Setup
- Last Successful Checkpoint：REV-0001｜Project workspace initialized
- Next Workflow：02_script_analysis_workflow.md
- Return Route：None
- Pending Decision：None
- Revision ID：REV-0001
- Updated At：{created}

## Completed Tasks

- Project Setup

## Pending Tasks

- STATE-01 through STATE-09

## Active Artifacts

- project_manifest.json / project_bible.md / asset_registry.md / project_status.md｜REV-0001｜Accepted

## Confirmed Assets

- None

## Visual Direction Lock

- Pending STATE-04

## Continuity And Open Risks

- No approved assets yet

## Review Control

- Review Result：NOT_REVIEWED
- Affected IDs：None
- Return Route：None
- Recheck Scope：None
- Review Artifact：None

## Version History

- REV-0001｜{created}｜STATE-00 Project Setup
"""
    (root / "project_status.md").write_text(status_text, encoding="utf-8")
    (root / "project_bible.md").write_text(f"# SD Film Project Bible\n\n- 项目 ID：{args.project_id}\n- 项目名称：{args.name}\n- 项目类型：{args.project_type}\n- 当前阶段：STATE-00 Project Initialized\n- 输入素材：{args.source_material or '待登记'}\n\n其余视觉、资产与连续性信息待对应 Workflow 确认。\n", encoding="utf-8")
    (root / "asset_registry.md").write_text(f"# SD Film Asset Registry\n\n- 项目 ID：{args.project_id}\n- 当前阶段：STATE-00 Project Initialized\n\n正式资产记录服从references/asset_lock_contract.md；当前无Active资产。每条正式视觉资产必须同时记录版本Status与Visual Production Status。\n\nVisual Production Status固定顺序：Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed。\n\n## Character\n\nPlanning\n\n## Environment\n\nPlanning\n\n## Prop\n\nPlanning\n\n## FX\n\nPlanning\n", encoding="utf-8")
    (root / "execution_ledger.md").write_text(f"# Execution Ledger\n\n- Project ID：{args.project_id}\n- Current Revision：REV-0001\n- Last Successful Checkpoint：STATE-00 Project Setup\n\n## Workflow Runs\n\n| Run ID | Workflow | State | Start Revision | Result Revision | Status | Checkpoint | Affected IDs | Return Route | Timestamp |\n|---|---|---|---|---|---|---|---|---|---|\n| RUN-0001 | 01_project_setup_workflow.md | STATE-00 | None | REV-0001 | Accepted | Project workspace initialized | None | None | {created} |\n\n## Generation Attempts\n\nNone。\n\n## Open Recovery Items\n\nNone。\n", encoding="utf-8")
    (root / "artifact_registry.md").write_text(f"# Artifact Revision Ledger\n\n- Project ID：{args.project_id}\n\n## Artifacts\n\n| Artifact ID | Type | Path | Revision ID | Status | Based On | Affected IDs | Validation | Supersedes | Invalidates | Created By | Created At |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| ART-0001 | Project Core | project_manifest.json / project_bible.md / asset_registry.md / project_status.md | REV-0001 | Accepted | Source Material | Project | Project validation required | None | None | 01_project_setup_workflow.md | {created} |\n\n## Dependency Recheck\n\nNone。\n", encoding="utf-8")
    projects.append({"project_id": args.project_id, "project_name": args.name, "root": str(root), "lifecycle": "active"})
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS\nCreated project workspace: {root}\nRegistered project in: {registry_path}")
    return 0


def validate_music_package(path: Path, as_json: bool = False) -> int:
    """Validate the explicit MUSIC / SEED-MUSIC package and native prompt blocks."""
    errors: list[str] = []
    warnings: list[str] = []
    text = read_text(path.resolve())

    required_sections = (
        "# MUSIC / SEED-MUSIC Score Package",
        "## Module Routing Record",
        "## Scope And Music Strategy",
        "## Spotting Map",
        "## Music Bible / Motif Map",
        "## Cue Sheet",
        "## SeedMusic Prompt Blocks",
        "## Review",
    )
    for section in required_sections:
        if section not in text:
            errors.append(f"Missing Music Package section: {section}")

    if not re.search(r"^\s*-\s*Route:\s*`?MUSIC / SEED-MUSIC Score`?\s*$", text, re.MULTILINE):
        errors.append("Music Package must record Route: MUSIC / SEED-MUSIC Score")
    trigger = re.search(r"^\s*-\s*Explicit Trigger Evidence:\s*(.+)$", text, re.MULTILINE)
    if not trigger or not trigger.group(1).strip():
        errors.append("Music Package must record non-empty Explicit Trigger Evidence")
    deliverable_match = re.search(r"^\s*-\s*Requested Deliverable:\s*(.+)$", text, re.MULTILINE)
    requested_deliverable = deliverable_match.group(1).strip() if deliverable_match else ""

    mode_match = re.search(r"^\s*-\s*Generation Mode:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
    mode = mode_match.group(1).strip() if mode_match else ""
    allowed_modes = {"INSTRUMENTAL", "VOICE TEXTURE", "LYRICS / SONG"}
    if mode not in allowed_modes:
        errors.append("Generation Mode must be INSTRUMENTAL, VOICE TEXTURE, or LYRICS / SONG")
    if mode != "INSTRUMENTAL":
        vocal_evidence = re.search(r"^\s*-\s*Explicit Vocal / Lyrics Evidence:\s*(.+)$", text, re.MULTILINE)
        if not vocal_evidence or not vocal_evidence.group(1).strip():
            errors.append("Non-instrumental mode requires Explicit Vocal / Lyrics Evidence")

    if "MUSIC CUE" not in text:
        warnings.append("Spotting Map contains no MUSIC CUE; no SeedMusic prompt may be necessary")
    if "SILENCE / PRODUCTION SOUND ONLY" not in text:
        errors.append("Spotting Map must contain at least one SILENCE / PRODUCTION SOUND ONLY decision within the scope or at an adjacent cue boundary")

    headings = list(re.finditer(r"^###\s+(MUS-CUE-(\d{3}))｜([^｜\n]+)｜(.+?)SeedMusic(?:纯音乐)?提示词\s*$", text, re.MULTILINE))
    cue_ids = [match.group(1) for match in headings]
    if len(cue_ids) != len(set(cue_ids)):
        errors.append("SeedMusic prompt Cue IDs must be unique")

    for index, heading in enumerate(headings):
        cue_id = heading.group(1)
        trace = heading.group(3).strip()
        segment_end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        segment = text[heading.end():segment_end]
        if "CLIP" in trace.upper() and not re.fullmatch(r"CLIP-\d{3}(?:—CLIP-\d{3})?", trace, re.IGNORECASE):
            errors.append(f"{cue_id} Clip trace must use CLIP-XXX or CLIP-XXX—CLIP-XXX")
        if "CLIP" in trace.upper() and not re.search(r"^\s*-\s*Related Clip\(s\):\s*.*CLIP-\d{3}", segment, re.MULTILINE | re.IGNORECASE):
            errors.append(f"{cue_id} must repeat its Clip trace in Related Clip(s)")

        blocks = re.findall(r"```text\s*\n(.*?)\n```", segment, re.DOTALL | re.IGNORECASE)
        if len(blocks) != 1:
            errors.append(f"{cue_id} must contain exactly one text execution block")
            continue
        block = blocks[0].strip()
        if re.search(r"CLIP-\d{3}|Related Clip|Narrative Use|Target Duration", block, re.IGNORECASE):
            errors.append(f"{cue_id} execution block contains delivery metadata")
        if len(re.findall(r"^style:\s*$", block, re.MULTILINE | re.IGNORECASE)) != 1:
            errors.append(f"{cue_id} execution block must contain exactly one style: label")
        if len(re.findall(r"^structure:\s*$", block, re.MULTILINE | re.IGNORECASE)) != 1:
            errors.append(f"{cue_id} execution block must contain exactly one structure: label")
            continue
        style_part, structure_part = re.split(r"^structure:\s*$", block, maxsplit=1, flags=re.MULTILINE | re.IGNORECASE)
        if mode == "INSTRUMENTAL":
            required_exclusions = ("instrumental only", "no vocals", "no lyrics", "no choir", "no humming", "no vocalise")
            for exclusion in required_exclusions:
                if exclusion not in style_part.lower():
                    errors.append(f"{cue_id} INSTRUMENTAL style missing exclusion: {exclusion}")
        structure_lines = [line.strip() for line in structure_part.splitlines() if line.strip()]
        times: list[float] = []
        for line in structure_lines:
            match = re.fullmatch(r"\[(Verse|Chorus|Bridge|Outro)\]:\s*(\d+(?:\.\d+)?)s", line, re.IGNORECASE)
            if not match:
                errors.append(f"{cue_id} invalid SeedMusic structure line: {line}")
                continue
            times.append(float(match.group(2)))
        if not times:
            errors.append(f"{cue_id} structure must contain at least one timed section")
        elif times[0] != 0:
            errors.append(f"{cue_id} first structure timestamp must be 0s")
        elif any(current <= previous for previous, current in zip(times, times[1:])):
            errors.append(f"{cue_id} structure timestamps must be strictly increasing")

    if re.search(r"Prompt|提示词", requested_deliverable, re.IGNORECASE) and "MUSIC CUE" in text and not headings:
        errors.append("Music Package has MUSIC CUE decisions but no SeedMusic prompt block")
    return report(errors, warnings, as_json)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("project", "registry", "sequence", "shotplan", "clip", "poster", "state08", "review", "asset", "artifact", "execution", "portable", "routing", "skill", "music"):
        sub = subparsers.add_parser(name)
        sub.add_argument("path")
        sub.add_argument("--json", action="store_true", dest="as_json")
        if name == "state08":
            sub.add_argument("--clip-plan", required=True, help="Confirmed Clip Production Plan used for duration and shot-list cross-check")
            sub.add_argument(
                "--batch-output",
                action="store_true",
                help="Allow multiple Clip Prompt Packages only when the user explicitly requested batch output in the current request",
            )
        if name == "clip":
            sub.add_argument(
                "--project-status",
                help="Selected project_status.md used to verify STATE-06 completion and STATE-07-or-later routing",
            )
            sub.add_argument(
                "--shot-design",
                help="Confirmed Professional Detailed Shot Script used to verify revision and formal SHOT allocation",
            )
    init = subparsers.add_parser("init")
    init.add_argument("--root", required=True)
    init.add_argument("--registry", required=True)
    init.add_argument("--project-id", required=True)
    init.add_argument("--name", required=True)
    init.add_argument("--project-type", required=True)
    init.add_argument("--source-material")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    path = Path(getattr(args, "path", "."))
    if args.command == "project":
        return validate_project(path, args.as_json)
    if args.command == "registry":
        return validate_registry(path, args.as_json)
    if args.command == "state08":
        return validate_state08(path, args.as_json, Path(args.clip_plan), args.batch_output)
    if args.command == "music":
        return validate_music_package(path, args.as_json)
    if args.command == "sequence":
        return validate_sequence(path, args.as_json)
    if args.command == "shotplan":
        return validate_shot_plan(path, args.as_json)
    if args.command == "clip":
        return validate_clip(
            path,
            args.as_json,
            Path(args.project_status) if args.project_status else None,
            Path(args.shot_design) if args.shot_design else None,
        )
    if args.command == "poster":
        return validate_poster(path, args.as_json)
    if args.command == "review":
        return validate_review(path, args.as_json)
    if args.command == "asset":
        return validate_asset_registry(path, args.as_json)
    if args.command == "artifact":
        return validate_artifact_ledger(path, args.as_json)
    if args.command == "execution":
        return validate_execution_ledger(path, args.as_json)
    if args.command == "portable":
        return validate_portable_status(path, args.as_json)
    if args.command == "routing":
        return validate_state_routing(path, args.as_json)
    if args.command == "skill":
        return validate_skill(path, args.as_json)
    if args.command == "init":
        return init_project(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
