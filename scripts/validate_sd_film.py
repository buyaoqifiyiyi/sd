#!/usr/bin/env python3
"""Deterministic r24 structural and routing validation for SD Film."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = (
    "SKILL.md", "core/pipeline.md", "core/runtime-state.md", "core/rule-priority.md",
    "modules/screenwriter.md", "modules/director.md", "modules/spatial-blocking.md",
    "modules/clip-planning.md", "modules/model-selection.md", "modules/prompt-generation.md", "modules/assets.md",
    "adapters/seedance-2.0.md", "adapters/seedance-2.5.md", "adapters/minimax-h3.md", "adapters/midjourney.md",
    "knowledge/prompt_compilation/minimax_h3_compilation.md",
    "workflows/10_clip_production_workflow.md", "workflows/11_video_generation_workflow.md",
    "templates/20_clip_plan.md", "templates/10_video_prompt.md",
    "references/project_state_contract.md", "rules/automation_mode.md",
    "knowledge/environment_multi_view_reconstruction.md",
)

def read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8-sig")

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
    core = read(root, "core/pipeline.md")
    runtime = read(root, "core/runtime-state.md")
    selection = read(root, "modules/model-selection.md")
    assets = read(root, "modules/assets.md")
    automation = read(root, "rules/automation_mode.md")
    performance = read(root, "knowledge/performance/micro_expression.md")
    projection = read(root, "knowledge/prompt_compilation/state08_projection.md")
    shot_qa = read(root, "knowledge/quality/shot_qa.md")
    character = read(root, "workflows/04_character_asset_workflow.md")
    environment = read(root, "workflows/05_environment_asset_workflow.md")
    environment_reconstruction = read(root, "knowledge/environment_multi_view_reconstruction.md")
    asset_lock = read(root, "references/asset_lock_contract.md")
    spatial_blocking = read(root, "knowledge/spatial_blocking_layer.md")
    prop = read(root, "workflows/06_prop_asset_workflow.md")
    fx = read(root, "workflows/15_fx_asset_workflow.md")
    clip = read(root, "workflows/10_clip_production_workflow.md")
    prompt = read(root, "workflows/11_video_generation_workflow.md")
    state = read(root, "references/project_state_contract.md")
    plan = read(root, "templates/20_clip_plan.md")
    adapter20 = read(root, "adapters/seedance-2.0.md")
    adapter25 = read(root, "adapters/seedance-2.5.md")
    adapter_h3 = read(root, "adapters/minimax-h3.md")
    compiler_h3 = read(root, "knowledge/prompt_compilation/minimax_h3_compilation.md")
    midjourney = read(root, "adapters/midjourney.md")
    camera_router = read(root, "knowledge/camera_language/shot_language_router.md")
    visual_styles = read(root, "knowledge/visual_styles/index.md")
    visual_workflow = read(root, "workflows/07_visual_development_workflow.md")
    character_template = read(root, "templates/04_character_asset_prompt.md")
    required_markers = (
        (core, "STATE-06 后：Model Selection"),
        (runtime, "STATE-06 完成后的 Model Selection 成功后"),
        (selection, "不创建 Clip、也不输出 `KEEP / ADAPT_SPLIT / RETURN`"),
        (clip, "STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner"),
        (clip, "具体窗口和条件只由各自 Adapter 拥有"),
        (prompt, "不选择模型、不创建或拆分 Clip、不调用旧 Compiler"),
        (prompt, "templates/10_video_prompt.md"),
        (state, "Adapter Profile"),
        (plan, "Adapter Profile"),
        (adapter20, "max_seconds: 15"),
        (adapter25, "max_seconds: 30"),
        (adapter25, "23 秒 Natural Unit 经长时长预检 PASS 后保持单 Execution Clip"),
        (adapter_h3, "min_seconds: 4"),
        (adapter_h3, "max_seconds: 15"),
        (adapter_h3, "images_max: 9"),
        (adapter_h3, "videos_max: 3"),
        (adapter_h3, "audio_max: 3"),
        (adapter_h3, "mixed_files_max: 12"),
        (adapter_h3, "two_images: no_automatic_cut"),
        (adapter_h3, "unsupported_without_official_verification"),
        (compiler_h3, "一个 Execution Clip 的生成时长必须为 4—15 秒"),
        (compiler_h3, "官方三段式"),
        (compiler_h3, "非叙事性音乐：N/A"),
        (assets, "本模块是STATE-03图像工具选择与提示词适配的唯一owner"),
        (assets, "### Direct Image Default"),
        (assets, "当前agent的实际图片生成能力决定"),
        (assets, "未明确指定外部图像模型：`Built-in Image`"),
        (assets, "明确指定`Midjourney`：读取`adapters/midjourney.md`"),
        (assets, "明确指定非Midjourney的外部图像模型"),
        (assets, "最小`CHANGE`与完整`PRESERVE`逻辑"),
        (automation, "## FAST Eligible Work"),
        (automation, "## Hard Stops"),
        (automation, "将任何Candidate Image标为Canonical / Active"),
        (state, "Automation Policy: STANDARD / FAST"),
        (performance, "## Behavior Under Pressure"),
        (performance, "Spatial Blocking仍是位置、朝向、距离和接触的唯一owner"),
        (projection, "**Risk-driven Execution Locks**"),
        (shot_qa, "### Risk-driven Prompt Evidence"),
        (midjourney, "只输出可直接粘贴的 Midjourney Prompt"),
        (midjourney, "不调用内置`image_gen`"),
        (midjourney, "不得默认附加`--v`、`--seed`、`--stylize`"),
        (character, "Asset Image Route"),
        (character, "Direct Image Default"),
        (character_template, "#### Combined Character Asset Sheet Prompt"),
        (character_template, "Three-View Prompt"),
        (environment, "Asset Image Route"),
        (prop, "Asset Image Route"),
        (fx, "Asset Image Route"),
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
        (visual_styles, "Project Proposal"),
        (visual_workflow, "Reference-To-System Evidence Gate"),
    )
    for text, marker in required_markers:
        if marker not in text:
            errors.append(f"missing r24 routing marker: {marker}")
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
    print("PASS: r24 structural and routing validation")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
