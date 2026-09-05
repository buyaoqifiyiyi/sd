#!/usr/bin/env python3
"""Deterministic r12 structural and routing validation for SD Film."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = (
    "SKILL.md", "core/pipeline.md", "core/runtime-state.md", "core/rule-priority.md",
    "modules/screenwriter.md", "modules/director.md", "modules/spatial-blocking.md",
    "modules/clip-planning.md", "modules/model-selection.md", "modules/prompt-generation.md",
    "adapters/seedance-2.0.md", "adapters/seedance-2.5.md",
    "workflows/10_clip_production_workflow.md", "workflows/11_video_generation_workflow.md",
    "templates/20_clip_plan.md", "templates/10_video_prompt.md",
    "references/project_state_contract.md",
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
    clip = read(root, "workflows/10_clip_production_workflow.md")
    prompt = read(root, "workflows/11_video_generation_workflow.md")
    state = read(root, "references/project_state_contract.md")
    plan = read(root, "templates/20_clip_plan.md")
    adapter20 = read(root, "adapters/seedance-2.0.md")
    adapter25 = read(root, "adapters/seedance-2.5.md")
    required_markers = (
        (core, "STATE-06 后：Model Selection"),
        (runtime, "STATE-06 完成后的 Model Selection 成功后"),
        (selection, "不创建 Clip、也不输出 `KEEP / ADAPT_SPLIT / RETURN`"),
        (clip, "STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner"),
        (clip, "2.0：4–15 秒；23 秒 Unit 必须拆分"),
        (clip, "2.5：4–30 秒；23 秒经 Long-duration Preflight PASS 保持单 Clip；34 秒拆分"),
        (prompt, "不选择模型、不创建或拆分 Clip、不调用旧 Compiler"),
        (prompt, "templates/10_video_prompt.md"),
        (state, "Adapter Profile"),
        (plan, "Adapter Profile"),
        (adapter20, "max_seconds: 15"),
        (adapter25, "max_seconds: 30"),
        (adapter25, "23 秒 Natural Unit 经长时长预检 PASS 后保持单 Execution Clip"),
    )
    for text, marker in required_markers:
        if marker not in text:
            errors.append(f"missing r12 routing marker: {marker}")
    for relative in ("modules/screenwriter.md", "modules/director.md", "modules/storyboard.md"):
        text = read(root, relative)
        if re.search(r"Seedance|Kling|Timeline|4.?15|4.?30", text, re.I):
            errors.append(f"upstream module contains model-specific rule: {relative}")
    for text, label in ((state, "state contract"), (plan, "clip template")):
        if "Model Compilation Template" in text or "Model Execution Lock Status" in text:
            errors.append(f"legacy compiler field remains active in {label}")
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
    print("PASS: r12 structural and routing validation")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
