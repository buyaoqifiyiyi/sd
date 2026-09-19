#!/usr/bin/env python3
"""Deterministic completeness validator for STATE-05/06/07 user-facing artifacts.

`scripts/validate_prompt_package.py` guards the STATE-08 Prompt; nothing guarded the
three artifacts before it, so a delivery could hand over a one-line stub for the
分镜表 or the Scene Breakdown and still look finished. Measured case: a FAST project
delivered

    Detailed Shot Design
    SHOT-001 女孩窗边按灭手机；SHOT-002 她走向楼梯；SHOT-003 空走廊；…

as its 分镜表, and a two-bullet list as its Scene Breakdown. Both are summaries of a
Template, not the Template.

Ownership:
  - Field names, order and mandatory-ness belong to the selected Template:
    `templates/07_scene_design_prompt.md` (Scene Breakdown),
    `templates/08_shot_design_prompt.md` (分镜表: the 5-column default form, or the
    18-column full record when the user explicitly asked for 完整版专业分镜),
    `templates/20_clip_plan.md` (Clip表: the 6-column user-facing form).
  - This script asserts structure and minimal non-emptiness only. It does not judge
    whether the content is any good, and passing it is not a substitute for the
    semantic Output QA each Template describes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCENE_ID_RE = re.compile(r"SCENE-(\d{3})")
SHOT_ID_RE = re.compile(r"SHOT-(\d{3})")
CLIP_ID_RE = re.compile(r"CLIP-(\d{3})")

# templates/07 — per-Scene Scene Directing Brief (colon stripped; matched after
# whitespace normalization) plus the sections that must appear in the document.
SCENE_BRIEF_LABELS = (
    "Dramatic/Relationship/Information/PerformanceBeatMap",
    "AudienceStart→EndState",
    "DramaticGeography/SpatialEvolution",
    "Reveal/WithholdTiming",
    "SceneCameraStrategy",
    "RhythmIntent",
)
SCENE_DOCUMENT_SECTIONS = (
    "SceneVisualBrief",
    "SpatialDesign",
    "LightingDesign",
    "ColorDesign",
    "AssetUsage",
    "SourceTraceability",
    "SequencePlanningDecision",
)

# templates/08 — the default user-facing 分镜表, and the full professional record.
SHOT_COLUMNS_DEFAULT = ("镜号", "画面与动作", "画面表达", "连续性", "资源")
SHOT_COLUMNS_FULL = (
    "镜号", "TC IN", "TC OUT", "时长(s)", "景别", "焦段", "场景 / 美术",
    "画面内容 / 构图", "人物动作", "摄影机 / 镜头", "摄影参数", "镜头调度",
    "光线 / 色彩", "画面特效 / 转场", "台词 / 旁白 / 口播", "同期声音设计",
    "AI制作备注", "素材 / 资产",
)

# templates/20 — default user-facing Clip表.
CLIP_COLUMNS = ("Clip ID", "包含镜号", "核心画面/动作", "时长", "起止承接", "资源")

# Clip时长只接受整数秒。取证：BytePlus ModelArk《Dreamina Seedance 2.5 tutorial》的
# `duration` 参数——"unit: seconds"，[4, 30] 范围内为整数秒（-1 表示由模型自选），
# 小数秒只出现在 video editing 任务继承源片时长的情形。取证日期 2026-09-19。
CLIP_DURATION_RE = re.compile(r"^\s*(\d+)\s*秒\s*$")

EXPECTED_KINDS = ("scene-breakdown", "shot-design", "clip-plan")
MIN_CELL_CHARS = 2
MIN_LABEL_CONTENT_CHARS = 4


def normalize(text: str) -> str:
    """Whitespace-insensitive form for label matching (labels are prose-shaped)."""
    return re.sub(r"\s+", "", text)


def split_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_separator_row(line: str) -> bool:
    cells = split_cells(line)
    return bool(cells) and all(set(cell) <= {"-", ":"} for cell in cells if cell)


def find_table(text: str, columns: tuple[str, ...]) -> tuple[list[str], list[list[str]]] | None:
    """First Markdown table whose header row matches `columns` exactly."""
    lines = text.splitlines()
    wanted = [normalize(column) for column in columns]
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        header = split_cells(line)
        if [normalize(cell) for cell in header] != wanted:
            continue
        rows: list[list[str]] = []
        for candidate in lines[index + 1:]:
            if not candidate.strip().startswith("|"):
                break
            if is_separator_row(candidate):
                continue
            rows.append(split_cells(candidate))
        return header, rows
    return None


def collect_ids(text: str, pattern: re.Pattern[str]) -> list[str]:
    seen: list[str] = []
    for match in pattern.finditer(text):
        value = match.group(0)
        if value not in seen:
            seen.append(value)
    return seen


def check_contiguous(ids: list[str], label: str) -> list[str]:
    errors: list[str] = []
    if not ids:
        errors.append(f"未找到任何{label}")
        return errors
    expected = [f"{label.split('-')[0]}-{index:03d}" for index in range(1, len(ids) + 1)]
    if ids != expected:
        errors.append(f"{label}编号必须从001连续且不重复，当前为 {ids}")
    return errors


def check_scene_breakdown(text: str) -> list[str]:
    errors: list[str] = []
    ids = collect_ids(text, SCENE_ID_RE)
    errors.extend(check_contiguous(ids, "SCENE-001"))
    normalized = normalize(text)
    for section in SCENE_DOCUMENT_SECTIONS:
        if section not in normalized:
            errors.append(f"缺少Template区块：{section}（Scene Breakdown不得以摘要形态提交）")
    # Per-Scene Brief: every required label must appear inside each Scene block,
    # and carry readable content after it.
    for position, scene in enumerate(ids):
        start = text.find(scene)
        end = text.find(ids[position + 1]) if position + 1 < len(ids) else len(text)
        block = text[start:end]
        block_norm = normalize(block)
        for label in SCENE_BRIEF_LABELS:
            if label not in block_norm:
                errors.append(f"{scene} 缺少Scene Directing Brief子项：{label}")
                continue
            tail = block_norm.split(label, 1)[1]
            for other in SCENE_BRIEF_LABELS:
                if other in tail:
                    tail = tail.split(other, 1)[0]
            if len(tail) < MIN_LABEL_CONTENT_CHARS:
                errors.append(f"{scene} 的 {label} 没有写出内容")
    return errors


def check_shot_design(text: str) -> list[str]:
    errors: list[str] = []
    default = find_table(text, SHOT_COLUMNS_DEFAULT)
    full = find_table(text, SHOT_COLUMNS_FULL)
    if default is None and full is None:
        errors.append(
            "缺少分镜表：需要默认5列表（镜号 / 画面与动作 / 画面表达 / 连续性 / 资源）"
            "或完整十八列专业分镜表；一行一句的分镜清单不是Template交付物"
        )
        return errors
    columns, rows = full if full is not None else default
    errors.extend(check_contiguous(collect_ids(text, SHOT_ID_RE), "SHOT-001"))
    if not rows:
        errors.append("分镜表没有数据行")
    for row in rows:
        if len(row) != len(columns):
            errors.append(f"分镜行列数({len(row)})与表头({len(columns)})不一致：{' / '.join(row[:2])}")
            continue
        shot = row[0] or "(无镜号)"
        if not SHOT_ID_RE.fullmatch(shot):
            errors.append(f"分镜表镜号列必须写正式SHOT-xxx：{shot}")
        for column, value in zip(columns, row):
            if len(value) < MIN_CELL_CHARS:
                errors.append(f"{shot} 的`{column}`为空；每格必须独立可读，不得留空或写‘同上’")
    return errors


def check_clip_plan(text: str) -> list[str]:
    errors: list[str] = []
    table = find_table(text, CLIP_COLUMNS)
    if table is None:
        errors.append(
            "缺少Clip表：需要默认6列表（Clip ID / 包含镜号 / 核心画面/动作 / 时长 / 起止承接 / 资源）；"
            "一句“执行规划完成”不是Template交付物"
        )
        return errors
    columns, rows = table
    ids = collect_ids(text, CLIP_ID_RE)
    errors.extend(check_contiguous(ids, "CLIP-001"))
    if not rows:
        errors.append("Clip表没有数据行")
    table_ids: list[str] = []
    for row in rows:
        if len(row) != len(columns):
            errors.append(f"Clip行列数({len(row)})与表头({len(columns)})不一致：{' / '.join(row[:2])}")
            continue
        clip = row[0] or "(无Clip ID)"
        table_ids.append(clip)
        if not CLIP_ID_RE.fullmatch(clip):
            errors.append(f"Clip表第一列必须写正式CLIP-xxx：{clip}")
        for index, (column, value) in enumerate(zip(columns, row)):
            if column == "资源":
                continue
            if len(value) < MIN_CELL_CHARS:
                errors.append(f"{clip} 的`{column}`为空；Clip表必须逐Clip可核对")
        if not SHOT_ID_RE.search(row[1]):
            errors.append(f"{clip} 的`包含镜号`未引用任何正式SHOT-xxx")
        if "时长" in columns:
            duration = row[columns.index("时长")]
            if not CLIP_DURATION_RE.fullmatch(duration):
                errors.append(
                    f"{clip} 的`时长`必须是整数秒（如 `8秒`）：{duration or '(空)'}；"
                    "平台`duration`参数只接受[4,30]整数秒，小数秒只属于video editing任务继承源片的时长"
                )
    return errors


CHECKS = {
    "scene-breakdown": check_scene_breakdown,
    "shot-design": check_shot_design,
    "clip-plan": check_clip_plan,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_file", type=Path)
    parser.add_argument("--kind", required=True, choices=list(EXPECTED_KINDS))
    args = parser.parse_args()

    try:
        raw = args.artifact_file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(f"INVALID: 无法读取 UTF-8 交付物: {exc}", file=sys.stderr)
        return 1

    errors = CHECKS[args.kind](raw)
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1

    print(f"VALID: {args.kind} 交付物通过完整性校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
