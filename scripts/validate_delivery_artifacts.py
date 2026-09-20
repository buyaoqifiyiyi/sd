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

Later measured case, same family, one level deeper: the user explicitly asked for
`完整版专业分镜`, so the 18-column record was the requested deliverable — but the
guarded artifact was the 5-column default table, the 18-column rows lived only in
chat and only for the first two batches, and the remaining batches were handed over
as a condensed summary table. Nothing failed, because `--kind shot-design` accepts
either form and never asks how many Shots the project has. `check_shot_design_full`
below is that missing question: a 完整版 delivery is complete only when every
declared Shot is present in one canonical file.

Ownership:
  - Field names, order and mandatory-ness belong to the selected Template:
    `templates/07_scene_design_prompt.md` (Scene Breakdown),
    `templates/08_shot_design_prompt.md` (分镜表: the 5-column default form, or the
    18-column full record when the user explicitly asked for 完整版专业分镜),
    `templates/20_clip_plan.md` (Clip表: the 6-column user-facing form).
  - `--kind shot-design` is the default-form gate consumed by the packaging path.
    `--kind shot-design-full` is the 完整版 gate: it additionally requires the
    single-issue, all-Shots-present form; the delivery contract that makes it
    mandatory lives in `rules/05_output_rules.md`
    (`### 完整版专业分镜 Delivery Gate`).
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

# 完整版专业分镜：用户显式要求`完整版专业分镜`时的正式交付文件形态。名称不是提示，
# 而是打包与复核的定位键——用户与打包器都在`05_shots/`里按这个名字找它。
SHOT_FULL_FILE_NAMES = ("06_detailed_shot_design.md", "08_detailed_shot_design.md")

# 正文里声明总镜数时必须与表格行数一致；缺少声明不是错误（项目状态才是真源）。
SHOT_TOTAL_RES = (
    re.compile(r"Total\s*Shots\s*[:：]\s*(\d+)", re.IGNORECASE),
    re.compile(r"共\s*(\d+)\s*镜"),
    re.compile(r"(\d+)\s*镜完整"),
)

# 时间码形态：完整版每行必须可复算，`TC OUT - TC IN = 时长(s)`。
TIMECODE_RE = re.compile(r"^(\d{1,2}):(\d{2}):(\d{2})\.(\d{3})$")
DURATION_CELL_RE = re.compile(r"^\d+(?:\.\d+)?$")

EXPECTED_KINDS = ("scene-breakdown", "shot-design", "shot-design-full", "clip-plan")
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


def check_table_rows(columns: tuple[str, ...], rows: list[list[str]], label: str) -> list[str]:
    """Shape and minimal content of one table's data rows."""
    errors: list[str] = []
    if not rows:
        errors.append(f"{label}没有数据行")
    for row in rows:
        if len(row) != len(columns):
            errors.append(f"{label}列数({len(row)})与表头({len(columns)})不一致：{' / '.join(row[:2])}")
            continue
        shot = row[0] or "(无镜号)"
        if not SHOT_ID_RE.fullmatch(shot):
            errors.append(f"{label}镜号列必须写正式SHOT-xxx：{shot}")
        for column, value in zip(columns, row):
            if len(value) < MIN_CELL_CHARS:
                errors.append(f"{shot} 的`{column}`为空；每格必须独立可读，不得留空或写‘同上’")
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
    errors.extend(check_table_rows(columns, rows, "分镜表"))
    return errors


def declared_total_shots(text: str) -> int | None:
    """The Shot total the document itself declares, if it declares one."""
    for pattern in SHOT_TOTAL_RES:
        match = pattern.search(text)
        if match:
            return int(match.group(1))
    return None


def timecode_seconds(value: str) -> float | None:
    match = TIMECODE_RE.match(value.strip())
    if not match:
        return None
    hours, minutes, seconds, milliseconds = (int(part) for part in match.groups())
    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000


def check_shot_design_full(text: str) -> list[str]:
    """完整版专业分镜 gate.

    The question `--kind shot-design` cannot ask: does this one file carry the whole
    film in the eighteen-column form the user asked for? A batch, a partial set or a
    condensed summary is reported as incomplete instead of passing as 完整版.
    """
    errors: list[str] = []
    tables: list[tuple[list[str], list[list[str]]]] = []
    lines = text.splitlines()
    wanted = [normalize(column) for column in SHOT_COLUMNS_FULL]
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        if [normalize(cell) for cell in split_cells(line)] != wanted:
            continue
        rows: list[list[str]] = []
        for candidate in lines[index + 1:]:
            if not candidate.strip().startswith("|"):
                break
            if is_separator_row(candidate):
                continue
            rows.append(split_cells(candidate))
        tables.append((SHOT_COLUMNS_FULL, rows))

    if not tables:
        errors.append(
            "完整版专业分镜必须以十八列完整记录交付（镜号 / TC IN / TC OUT / 时长(s) / 景别 / "
            "焦段 / 场景 / 美术 / 画面内容 / 构图 / 人物动作 / 摄影机 / 镜头 / 摄影参数 / "
            "镜头调度 / 光线 / 色彩 / 画面特效 / 转场 / 台词 / 旁白 / 口播 / 同期声音设计 / "
            "AI制作备注 / 素材 / 资产）；默认5列表不能充当完整版，"
            "逐批交付的中间状态也不是完整版"
        )
        return errors

    rows: list[list[str]] = []
    for columns, table_rows in tables:
        errors.extend(check_table_rows(columns, table_rows, "完整版分镜表"))
        rows.extend(row for row in table_rows if len(row) == len(columns))

    if not rows:
        errors.append("完整版分镜表没有数据行")
        return errors

    shot_ids = [row[0] for row in rows]
    if len(set(shot_ids)) != len(shot_ids):
        errors.append(f"完整版分镜表存在重复镜号或同一镜被拆到多张表：{shot_ids}")
    errors.extend(check_contiguous(shot_ids, "SHOT-001"))

    expected_total = declared_total_shots(text)
    if expected_total is not None and expected_total != len(rows):
        errors.append(
            f"完整版不完整：正文声明 Total Shots: {expected_total}，"
            f"但十八列表只交付 {len(rows)} 个Shot——完成版必须一次包含全部已确认Shot，"
            "不得留待下一轮补交或改用摘要表"
        )

    body_ids = collect_ids(text, SHOT_ID_RE)
    strays = [shot for shot in body_ids if shot not in shot_ids]
    if strays:
        errors.append(f"正文出现未在任何十八列行中定义的镜号：{strays}")

    # 时间码连续性（仅在每行都给出可解析时间码时校验；字段缺失交由单元格非空检查报出）。
    previous_out: float | None = None
    for row in rows:
        if len(row) != len(SHOT_COLUMNS_FULL):
            continue
        shot, duration_cell = row[0], row[3]
        start, end = timecode_seconds(row[1]), timecode_seconds(row[2])
        if start is None or end is None or not DURATION_CELL_RE.match(duration_cell):
            previous_out = None
            continue
        if round(end - start, 3) != round(float(duration_cell), 3):
            errors.append(
                f"{shot} 时间码不可复算：`TC OUT - TC IN` = {round(end - start, 3)}s，"
                f"`时长(s)` = {duration_cell}"
            )
        if previous_out is not None and round(start, 3) != round(previous_out, 3):
            errors.append(f"{shot} 时间码断档：上一镜结束于 {previous_out}s，本镜从 {start}s 开始")
        previous_out = end

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
    "shot-design-full": check_shot_design_full,
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

    errors: list[str] = []
    if args.kind == "shot-design-full" and args.artifact_file.name not in SHOT_FULL_FILE_NAMES:
        errors.append(
            "完整版专业分镜必须保存为 `05_shots/06_detailed_shot_design.md`"
            "（或 `08_detailed_shot_design.md`）：文件名是用户与打包器在 `05_shots/` 里定位"
            f"完整版的键，当前为 `{args.artifact_file.name}`"
        )
    errors.extend(CHECKS[args.kind](raw))
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1

    print(f"VALID: {args.kind} 交付物通过完整性校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
