#!/usr/bin/env python3
"""Deterministic r52 structural, routing and context-budget validation for SD Film."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = (
    "SKILL.md", "core/pipeline.md", "core/runtime-state.md", "core/rule-priority.md",
    "modules/screenwriter.md", "modules/director.md", "modules/spatial-blocking.md",
    "modules/clip-planning.md", "modules/model-selection.md", "modules/image-model-selection.md", "modules/prompt-generation.md", "modules/assets.md",
    "adapters/seedance-2.0.md", "adapters/seedance-2.5.md", "adapters/minimax-h3.md", "adapters/built-in-image.md", "adapters/midjourney.md",
    "knowledge/prompt_compilation/minimax_h3_compilation.md",
    "workflows/01_project_setup_workflow.md", "workflows/10_clip_production_workflow.md", "workflows/11_video_generation_workflow.md",
    "templates/00_project_start_template.md", "templates/20_clip_plan.md", "templates/10_video_prompt.md", "templates/12_seedance_25_video_prompt.md", "templates/13_minimax_h3_video_prompt.md", "templates/14_midjourney_asset_prompt.md", "templates/24_builtin_image_asset_prompt.md",
    "references/project_state_contract.md", "rules/automation_mode.md", "rules/02_asset_rules.md",
    "knowledge/environment_multi_view_reconstruction.md", "knowledge/clip_preflight_check.md", "knowledge/reference_budget.md",
    "references/context_budget.md",
    "references/maintenance_self_check.md",
    "references/maintenance_self_check_protocol.md",
    "references/regression_scenarios.md",
    "references/regression_scenarios_craft.md",
    "references/regression_scenarios_system.md",
    "references/recovery_guards.md",
    "scripts/validate_prompt_package.py",
)

BUDGET_TARGET_BYTES = 50 * 1024
BUDGET_CEILING_BYTES = 100 * 1024
SKILL_ENTRY_MAX_BYTES = 12 * 1024
SKILL_ENTRY_MAX_LINES = 120
LEDGER_CLASSES = ("COMPOSITE", "INTEGRAL", "NON_RUNTIME")
NON_SKILL_DIRS = {".git", ".workbuddy", "tmp", "__pycache__", ".venv", "node_modules"}

SELF_CHECK_DIMENSIONS = (
    "Duplicate Rule Check", "Conflict Check", "Terminology Drift Check", "Rule Ownership Check",
    "Prompt Pollution Check", "Routing Integrity Check", "Template Consistency Check",
    "Reference Integrity Check", "State / Continuity Compatibility Check", "User Guide Sync Check",
    "Regression Check", "Change Classification Check", "Runtime Claim / Legacy Recovery Check",
    "Standalone Skill Discovery Check", "Context Budget Check",
)

def read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8-sig")

def size_bytes(path: Path) -> int:
    return len(path.read_bytes().decode("utf-8-sig").encode("utf-8"))

def scan_markdown(root: Path) -> list[tuple[str, int]]:
    """Every markdown file that ships with the skill, sized in UTF-8 bytes.

    Bytes, not lines: this corpus is 31%-57% blank lines, so a line count
    overstates size and misjudges paragraph-dense files.
    """
    entries: list[tuple[str, int]] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part in NON_SKILL_DIRS for part in relative.parts[:-1]):
            continue
        entries.append((relative.as_posix(), size_bytes(path)))
    return entries

def read_size_ledger(root: Path) -> dict[str, str]:
    """The Size Ledger rows as {relative path: file class}."""
    ledger: dict[str, str] = {}
    for line in read(root, "references/context_budget.md").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].endswith(".md"):
            ledger[cells[0]] = cells[1]
    return ledger

def check_context_budget(entries, ledger) -> list[str]:
    """A file that outgrows the target must be registered with a known class; a
    registered file that shrinks back within target must be unregistered. Both
    drifts are reported, so the ledger never decays into a standing exemption."""
    errors: list[str] = []
    sizes = dict(entries)
    ledger = dict(ledger)
    for relative, size in entries:
        if size > BUDGET_CEILING_BYTES:
            errors.append(
                f"file reached the context budget ceiling ({size} > {BUDGET_CEILING_BYTES} bytes), "
                f"split it: {relative}"
            )
        elif size > BUDGET_TARGET_BYTES and relative not in ledger:
            errors.append(
                f"file exceeds the context budget target ({size} > {BUDGET_TARGET_BYTES} bytes) "
                f"but is not registered in references/context_budget.md: {relative}"
            )
    for relative, file_class in sorted(ledger.items()):
        if file_class not in LEDGER_CLASSES:
            errors.append(f"context budget ledger has an unknown class ({file_class}): {relative}")
        if relative not in sizes:
            errors.append(f"context budget ledger points at a missing markdown file: {relative}")
        elif sizes[relative] <= BUDGET_TARGET_BYTES:
            errors.append(
                f"context budget ledger entry is stale ({sizes[relative]} bytes, back within target), "
                f"remove it: {relative}"
            )
    return errors

def validate_skill(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors
    skill = read(root, "SKILL.md")
    version = re.search(r"Skill Version:\s*(\S+)", skill)
    build = re.search(r"Build ID:\s*(\S+)", skill)
    if not version or not build or build.group(1) != f"sd-film-{version.group(1)}":
        errors.append("Skill Version and Build ID must match")
    if len(skill.encode("utf-8")) > 8000:
        errors.append("SKILL.md must remain a compact routing entrypoint")
    for alias in ("调用sd", "调用SD", "用SD Film", "重新调用sd", "恢复旧项目", "继续之前的项目"):
        if alias not in skill:
            errors.append(f"SKILL.md is missing discovery alias: {alias}")
    core = read(root, "core/pipeline.md")
    runtime = read(root, "core/runtime-state.md")
    selection = read(root, "modules/model-selection.md")
    image_selection = read(root, "modules/image-model-selection.md")
    assets = read(root, "modules/assets.md")
    automation = read(root, "rules/automation_mode.md")
    asset_rules = read(root, "rules/02_asset_rules.md")
    user_guide = read(root, "USER_GUIDE.md")
    progression = read(root, "rules/progression_rules.md")
    completion = read(root, "rules/completion_gate.md")
    performance = read(root, "knowledge/performance/micro_expression.md")
    projection = read(root, "knowledge/prompt_compilation/state08_projection.md")
    shot_qa = read(root, "knowledge/quality/shot_qa.md")
    character = read(root, "workflows/04_character_asset_workflow.md")
    environment = read(root, "workflows/05_environment_asset_workflow.md")
    environment_reconstruction = read(root, "knowledge/environment_multi_view_reconstruction.md")
    asset_lock = read(root, "references/asset_lock_contract.md")
    spatial_blocking = read(root, "knowledge/spatial_blocking_layer.md")
    prop = read(root, "workflows/06_prop_asset_workflow.md")
    discovery = read(root, "workflows/03_asset_discovery_workflow.md")
    fx = read(root, "workflows/15_fx_asset_workflow.md")
    clip = read(root, "workflows/10_clip_production_workflow.md")
    prompt = read(root, "workflows/11_video_generation_workflow.md")
    state = read(root, "references/project_state_contract.md")
    plan = read(root, "templates/20_clip_plan.md")
    adapter20 = read(root, "adapters/seedance-2.0.md")
    adapter25 = read(root, "adapters/seedance-2.5.md")
    profile25 = read(root, "knowledge/seedance_25_profile.md")
    compiler25 = read(root, "knowledge/prompt_compilation/seedance_25_compilation.md")
    reference_budget = read(root, "knowledge/reference_budget.md")
    prompt_template = read(root, "templates/10_video_prompt.md")
    prompt_template25 = read(root, "templates/12_seedance_25_video_prompt.md")
    prompt_template_h3 = read(root, "templates/13_minimax_h3_video_prompt.md")
    adapter_h3 = read(root, "adapters/minimax-h3.md")
    compiler_h3 = read(root, "knowledge/prompt_compilation/minimax_h3_compilation.md")
    midjourney = read(root, "adapters/midjourney.md")
    builtin_image = read(root, "adapters/built-in-image.md")
    midjourney_template = read(root, "templates/14_midjourney_asset_prompt.md")
    builtin_image_template = read(root, "templates/24_builtin_image_asset_prompt.md")
    camera_router = read(root, "knowledge/camera_language/shot_language_router.md")
    visual_styles = read(root, "knowledge/visual_styles/index.md")
    visual_workflow = read(root, "workflows/07_visual_development_workflow.md")
    project_bible = read(root, "templates/01_project_bible_template.md")
    director_layer = read(root, "knowledge/director_decision_layer.md")
    scorecard = read(root, "knowledge/quality/prompt_scorecard.md")
    character_template = read(root, "templates/04_character_asset_prompt.md")
    environment_template = read(root, "templates/05_environment_asset_prompt.md")
    prop_template = read(root, "templates/06_prop_asset_prompt.md")
    fx_template = read(root, "templates/13_fx_asset_prompt.md")
    project_setup = read(root, "workflows/01_project_setup_workflow.md")
    project_start_template = read(root, "templates/00_project_start_template.md")
    preflight = read(root, "knowledge/clip_preflight_check.md")
    required_markers = (
        (core, "STATE-00：一次确认项目图像模型默认项与视频模型偏好"),
        (runtime, "PROJECT_IMAGE_MODEL_DEFAULT"),
        (selection, "不创建Clip、也不输出`KEEP / ADAPT_SPLIT / RETURN`"),
        (selection, "Project Video Model Preference"),
        (image_selection, "Project Model Selection Proposal"),
        (project_setup, "### Project Model Selection Gate"),
        (project_start_template, "# Project Model Preferences"),
        (state, "Project Image Model Default"),
        (state, "Project Video Model Preference"),
        (state, "REF-SKETCH Submission Compatibility"),
        (clip, "STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner"),
        (clip, "具体窗口和条件只由各自 Adapter 拥有"),
        (prompt, "不选择模型、不创建或拆分 Clip、不调用旧 Compiler"),
        (prompt, "templates/10_video_prompt.md"),
        (state, "Adapter Profile"),
        (plan, "Adapter Profile"),
        (adapter20, "max_seconds: 15"),
        (adapter25, "max_seconds: 30"),
        (adapter25, "23 秒 Natural Unit 经长时长预检 PASS 后保持单 Execution Clip"),
        (adapter25, "default_capacity_limit"),
        (adapter25, "prompt_output_template: templates/12_seedance_25_video_prompt.md"),
        (adapter25, "timestamp_text_control"),
        (adapter25, "Dreamina Web专有"),
        (adapter20, "actual_image_input_in_existing_reference_assets"),
        (adapter25, "actual_image_at_picture_n"),
        (profile25, "Timestamp And Dreamina Surface Boundary"),
        (compiler25, "唯一Primary Role"),
        (reference_budget, "合计50项"),
        (prompt_template25, "## 唯一允许的最终模板"),
        (prompt_template25, "参考素材职责与优先级"),
        (prompt_template25, "时间线："),
        (prompt_template25, "### 主风格："),
        (prompt_template25, "独立、无条件的项目视觉入口"),
        (adapter_h3, "prompt_output_template: templates/13_minimax_h3_video_prompt.md"),
        (prompt_template_h3, "参考素材说明："),
        (prompt_template_h3, "核心创意："),
        (prompt_template_h3, "核心创意：\n主风格："),
        (prompt_template_h3, "非叙事性音乐：N/A"),
        (adapter_h3, "min_seconds: 4"),
        (adapter_h3, "max_seconds: 15"),
        (adapter_h3, "images_max: 9"),
        (adapter_h3, "videos_max: 3"),
        (adapter_h3, "audio_max: 3"),
        (adapter_h3, "mixed_files_max: 12"),
        (adapter_h3, "two_images: no_automatic_cut"),
        (adapter_h3, "unsupported_without_official_verification"),
        (adapter_h3, "incompatible_modes: [start_or_end_frame, start_end_frame, video_edit]"),
        (compiler_h3, "一个 Execution Clip 的生成时长必须为 4—15 秒"),
        (compiler_h3, "官方三段式"),
        (compiler_h3, "非叙事性音乐：N/A"),
        (prompt_template, "实际提交图片输入"),
        (prompt_template25, "REF-SKETCH-XX @图片N"),
        (prompt_template_h3, "REF-SKETCH-XX @图片N"),
        (preflight, "### Required Sketch Submission Binding"),
        (preflight, "不得声称“已使用/已提交草图”"),
        (reference_budget, "Submission Compatibility=`FAIL`"),
        (assets, "本模块是STATE-03图像工具路由与提示词适配的唯一owner"),
        (assets, "### Image Model Selection Gate"),
        (assets, "不得默认选择Built-in Image、Midjourney或任何第三方服务"),
        (assets, "`Built-in Image`：读取`adapters/built-in-image.md`"),
        (assets, "`Midjourney`：读取`adapters/midjourney.md`"),
        (assets, "明确指定其他图像模型"),
        (assets, "最小`CHANGE`与完整`PRESERVE`逻辑"),
        (image_selection, "## Available Choices"),
        (image_selection, "不得默认选择Built-in Image、Midjourney或其他模型"),
        (image_selection, "下一步`、`下一个`、`继续`"),
        (image_selection, "Image Model Selection Scope"),
        (state, "Selected Image Model: Built-in Image / Midjourney / UNSELECTED"),
        (builtin_image, "prompt_output_template: templates/24_builtin_image_asset_prompt.md"),
        (builtin_image_template, "## Built-in Image Prompt Package"),
        (automation, "## FAST Eligible Work"),
        (automation, "## FAST Continuous Chain"),
        (automation, "尽量少确认"),
        (automation, "完整视频Prompt"),
        (automation, "Candidate Output Triage / Cleanup"),
        (automation, "## Unified Delivery Packages"),
        (automation, "Preproduction Package"),
        (automation, "Execution Package"),
        (automation, "Asset Candidate Package"),
        (automation, "## Hard Stops"),
        (automation, "将任何Candidate Image标为Canonical / Active"),
        (progression, "## Confirmation Input Semantics"),
        (progression, "任何语义上表示继续推进的表达"),
        (progression, "不提交外部服务"),
        (completion, "确认输入语义由`rules/progression_rules.md`唯一拥有"),
        (state, "Automation Policy: STANDARD / FAST"),
        (performance, "## Behavior Under Pressure"),
        (performance, "Spatial Blocking仍是位置、朝向、距离和接触的唯一owner"),
        (projection, "**Risk-driven Execution Locks**"),
        (shot_qa, "### Risk-driven Prompt Evidence"),
        (midjourney, "只输出可直接粘贴的 Midjourney Prompt"),
        (midjourney, "不调用内置`image_gen`"),
        (midjourney, "prompt_output_template: templates/14_midjourney_asset_prompt.md"),
        (midjourney_template, "## Midjourney Prompt Package"),
        (midjourney_template, "## Parameter And Syntax Discipline"),
        (midjourney_template, "--v`、`--q`、`--s`、`--seed`、`--chaos`、`--raw`、`--niji"),
        (midjourney_template, "## Asset-Specific Compilation"),
        (assets, "独立`prompt_output_template`"),
        (character, "Asset Image Route"),
        (character, "Image Model Selection Gate"),
        (character_template, "#### Combined Character Asset Sheet Prompt"),
        (character_template, "Three-View Prompt"),
        (character_template, "Image Prompt Output Template"),
        (environment_template, "Image Prompt Output Template"),
        (prop_template, "Image Prompt Output Template"),
        (prop_template, "1×4横版道具设定图"),
        (prop_template, "covered by Main 1×4 Prop Sheet"),
        (builtin_image_template, "four-panel prop sheet"),
        (midjourney_template, "four-panel prop sheet"),
        (fx_template, "Image Prompt Output Template"),
        (fx_template, "## Reference Assets And Visual Variant Policy"),
        (fx_template, "Primary Visual Reference:"),
        (fx_template, "Immutable Visual Anchors:"),
        (fx_template, "### Physical Drivers"),
        (fx_template, "Wind / Gravity / Flow:"),
        (fx_template, "## FX State Ledger"),
        (fx_template, "Boundary (Shot / Clip / Frame):"),
        (environment, "Asset Image Route"),
        (prop, "Asset Image Route"),
        (prop, "Main 1×4 Prop Sheet"),
        (prop, "正面、侧面、背面、关键细节"),
        (discovery, "## Important Prop Completeness Pass"),
        (discovery, "Important Prop Candidate"),
        (discovery, "Prop Production Route"),
        (discovery, "No important PROP asset required"),
        (prop, "Prop Completeness Ledger"),
        (completion, "Prop Completeness Ledger"),
        (fx, "Asset Image Route"),
        (fx, "记录可见的物理驱动"),
        (fx, "FX State Ledger在每个边界记录可继承状态"),
        (environment, "Spatial Reconstruction: Full / Partial / Not Required"),
        (environment_reconstruction, "ENV-01 + ENV-02 → ENV-03"),
        (environment_reconstruction, "ENV-01 + ENV-02 + ENV-03 → ENV-04"),
        (environment_reconstruction, "最相关2–4张"),
        (asset_lock, "### Environment Spatial Lock"),
        (spatial_blocking, "ENV-04是STATE-03已确认的Environment Canonical布局视角"),
        (assets, "### Prompt Evidence Ordering"),
        (performance, "### Micro-action Timing And Hierarchy"),
        (camera_router, "### Layered Depth And Readability"),
        (projection, "### Prompt Evidence Specificity"),
        (visual_styles, "### Reference-To-System Evidence Gate"),
        (visual_styles, "Observable Reference Evidence"),
        (visual_styles, "### Project Color Reference Route"),
        (asset_rules, "Project Color Reference`；它是非资产项目视觉参考"),
        (asset_rules, "### Candidate Output Triage And Cleanup"),
        (asset_rules, "### User-Declared Existing Assets"),
        (asset_rules, "NEEDS_USER_SELECTION"),
        (asset_rules, "聊天历史中的图片无法由系统直接删除"),
        (user_guide, "Project Color Reference`进入视觉开发"),
        (visual_styles, "Project Proposal"),
        (visual_workflow, "Reference-To-System Evidence Gate"),
        (visual_workflow, "# Aesthetic Decision Lock Gate"),
        (visual_workflow, "被放弃的选项"),
        (visual_workflow, "视觉母题与变化轨迹"),
        (director_layer, "Aesthetic Decision Lock"),
        (project_bible, "Aesthetic Decision Lock"),
        (project_bible, "视觉母题与变化轨迹（"),
        (scorecard, "Aesthetic Decision Lock"),
        (projection, "Aesthetic Decision Lock"),
        (projection, "反差与光比结构的程度及其变化节点"),
        (prompt, "Aesthetic Decision Lock"),
    )
    for text, marker in required_markers:
        if marker not in text:
            errors.append(f"missing r49 routing marker: {marker}")
    for relative in ("modules/screenwriter.md", "modules/director.md", "modules/storyboard.md"):
        text = read(root, relative)
        if re.search(r"Seedance|Kling|Timeline|4.?15|4.?30", text, re.I):
            errors.append(f"upstream module contains model-specific rule: {relative}")
    for text, label in ((state, "state contract"), (plan, "clip template")):
        if "Model Compilation Template" in text or "Model Execution Lock Status" in text:
            errors.append(f"legacy compiler field remains active in {label}")
    if "Midjourney" in selection or "Built-in Image" in selection:
        errors.append("video model selection must not own asset image routing")
    for relative in ("modules/screenwriter.md", "modules/director.md", "modules/storyboard.md"):
        text = read(root, relative)
        if re.search(r"Midjourney|Built-in Image|image_gen", text, re.I):
            errors.append(f"upstream module contains asset image routing: {relative}")
    entry_lines = skill.count("\n")
    if entry_lines > SKILL_ENTRY_MAX_LINES:
        errors.append(
            f"SKILL.md must stay a compact routing entrypoint ({entry_lines} > {SKILL_ENTRY_MAX_LINES} lines)"
        )
    entry_bytes = size_bytes(root / "SKILL.md")
    if entry_bytes > SKILL_ENTRY_MAX_BYTES:
        errors.append(
            f"SKILL.md must stay a compact routing entrypoint ({entry_bytes} > {SKILL_ENTRY_MAX_BYTES} bytes)"
        )
    card = read(root, "references/maintenance_self_check.md")
    criteria = read(root, "references/maintenance_self_check_protocol.md")
    contracts = read(root, "references/module_contracts.md")
    for dimension in SELF_CHECK_DIMENSIONS:
        if dimension not in card:
            errors.append(f"maintenance run card is missing the check dimension: {dimension}")
        if dimension not in criteria:
            errors.append(f"maintenance protocol is missing the criteria for: {dimension}")
    if "references/context_budget.md" not in card:
        errors.append("the maintenance run card must route the context budget to its single owner")
    if "references/context_budget.md" not in criteria:
        errors.append("the maintenance protocol must route the context budget to its single owner")
    for guard in ("Runtime Recovery Regression Protection", "Standalone Skill Discovery Guard"):
        if guard not in criteria:
            errors.append(f"maintenance protocol is missing the guard: {guard}")
    if "\n## Skill Update Self-Check" in contracts:
        errors.append("module_contracts.md must not re-own the maintenance self-check")
    if "references/maintenance_self_check.md" not in contracts:
        errors.append("module_contracts.md must route Skill maintenance QA to its owner")
    if "非运行时文件" not in user_guide:
        errors.append("USER_GUIDE.md must declare itself a non-runtime document")
    ledger = read_size_ledger(root)
    for relative, file_class in ledger.items():
        if file_class == "NON_RUNTIME" and "非运行时文件" not in read(root, relative):
            errors.append(f"a NON_RUNTIME ledger entry must declare itself in-file: {relative}")
    errors.extend(check_context_budget(scan_markdown(root), ledger))
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, required=True)
    args = parser.parse_args()
    errors = validate_skill(args.skill_root)
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: r52 structural, routing and context-budget validation")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
