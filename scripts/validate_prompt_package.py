#!/usr/bin/env python3
"""Deterministic validator for a delivered STATE-08 video Prompt Package.

This script guards the *deliverable*, not the skill scaffold: it checks that a
produced `# CLIP-X｜...` package actually follows the selected final template
before the package is handed to the user. Structural/routing validation of the
skill itself stays owned by `scripts/validate_sd_film.py`.

Ownership:
  - Field names, order and mandatory-ness are owned by the selected Template:
    `templates/10_video_prompt.md` (Seedance 2.0),
    `templates/12_seedance_25_video_prompt.md` (Seedance 2.5),
    `templates/13_minimax_h3_video_prompt.md` (MiniMax H3).
  - This validator only asserts deterministically checkable facts. It does not
    judge artistic quality and passing it is not a substitute for the semantic
    Output QA described by each Template.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NO_BGM_SENTENCE = (
    "禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，"
    "只保留台词、环境声、动作音效和必要的自然声音。"
)

TITLE_PATTERN = re.compile(r"^#\s*CLIP-[^｜|]*[｜|].*视频提示词\s*$")
SHOT_HEADER = re.compile(r"^分镜\s*(\d+)\s*$")
SHOT_FIELD = re.compile(r"^([^：:]{1,12})：")
STAGE_HEADER = re.compile(r"^\[(?:第)?\s*(\d+)\s*[—\-–~至]\s*(\d+)\s*秒\]\s*$")
REF_TAIL_USAGE = ("同镜头连续承接用途", "空间/站位/景别参考用途")

SHOT_FIELDS_20 = [
    "景别", "镜头/机位", "起始状态", "画面描述", "人物动作与情绪",
    "空间关系", "道具状态", "台词", "音效", "镜头结尾状态",
]
GLOBALS_20 = [
    "时长", "画幅", "参考资产", "首帧参考", "尾帧限制",
    "主风格", "人物一致性", "环境一致性",
]
STAGE_FIELDS_25 = [
    "画面与镜头", "人物动作与情绪", "空间与道具", "台词", "音效", "阶段结尾状态",
]
GLOBALS_25 = [
    "时长", "画幅", "多模态参考资产", "参考素材职责与优先级", "首帧参考",
    "尾帧限制", "主风格", "全局叙事与画面设定", "全局一致性与执行约束", "时间线",
]
GLOBALS_H3 = [
    "时长", "画幅", "参考素材说明", "核心创意", "画面过程说明", "反向提示词",
]

VOICE_FIELD = "音色特征"
H3_LAST_LINE = "非叙事性音乐：N/A"


class Package(str):
    """Marker type kept for readability of the parser signatures."""


def strip_fence(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 2 and lines[-1].strip() == "```":
            return "\n".join(lines[1:-1]).strip()
    return stripped


def marker_positions(lines: list[str], names: list[str]) -> dict[str, int]:
    """Return the first line index of each `名字：` field, or -1 when absent."""
    found: dict[str, int] = {}
    for index, line in enumerate(lines):
        stripped = line.strip()
        for name in names:
            if name in found:
                continue
            if stripped.startswith(f"{name}：") or stripped.startswith(f"{name}:"):
                found[name] = index
    return {name: found.get(name, -1) for name in names}


def check_order(lines: list[str], globals_: list[str]) -> list[str]:
    errors: list[str] = []
    positions = marker_positions(lines, globals_)
    for name, index in positions.items():
        if index < 0:
            errors.append(f"缺少全局字段: {name}：")
    present = [(name, index) for name, index in positions.items() if index >= 0]
    ordered = [name for name, _ in sorted(present, key=lambda item: item[1])]
    if ordered != [name for name in globals_ if name in ordered]:
        errors.append("全局字段顺序错误，当前为: " + " → ".join(ordered))
    return errors


def section_text(lines: list[str], start: int, stop_names: list[str]) -> str:
    end = len(lines)
    for index in range(start + 1, len(lines)):
        stripped = lines[index].strip()
        if any(stripped.startswith(f"{name}：") or stripped.startswith(f"{name}:") for name in stop_names):
            end = index
            break
        if SHOT_HEADER.match(stripped) or STAGE_HEADER.match(stripped):
            end = index
            break
    return "\n".join(lines[start:end])


def check_ref_tail(lines: list[str], model: str) -> list[str]:
    errors: list[str] = []
    asset_field = "多模态参考资产" if model == "seedance-2.5" else "参考资产"
    positions = marker_positions(lines, [asset_field])
    start = positions.get(asset_field, -1)
    if start < 0:
        return errors
    block = section_text(lines, start, ["首帧参考"])
    if "REF-TAIL" not in block:
        return errors
    if not any(usage in block for usage in REF_TAIL_USAGE):
        errors.append(
            "参考资产出现 REF-TAIL，但未标明“同镜头连续承接用途”或“空间/站位/景别参考用途”"
        )
    return errors


def block_names(lines: list[str], start: int, stop: int) -> list[str]:
    chunk = [line.strip() for line in lines[start: stop]]
    chunk = [line for line in chunk if line and line != "……"]
    return [SHOT_FIELD.match(line).group(1) for line in chunk if SHOT_FIELD.match(line)]


def check_shot_draft(lines: list[str], stop_index: int) -> tuple[list[str], list[int]]:
    errors: list[str] = []
    headers = [(i, int(SHOT_HEADER.match(line.strip()).group(1)))
               for i, line in enumerate(lines) if SHOT_HEADER.match(line.strip())]
    numbers = [number for _, number in headers]
    if not numbers:
        errors.append("未找到“分镜N”结构")
        return errors, []
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"分镜编号必须从1连续且不重复，当前为 {numbers}")
    for position, (line_index, number) in enumerate(headers):
        if position + 1 < len(headers):
            stop = headers[position + 1][0]
        else:
            stop = stop_index if stop_index > line_index else len(lines)
        names = block_names(lines, line_index + 1, stop)
        if names != SHOT_FIELDS_20:
            errors.append(
                f"分镜{number} 的十个字段缺失、超量或顺序错误，当前为: {' → '.join(names) or '空'}"
            )
        for line in (lines[line_index + 1: stop]):
            stripped = line.strip()
            if SHOT_FIELD.match(stripped) and stripped.endswith("："):
                errors.append(f"分镜{number} 存在空值字段: {stripped}")
    return errors, numbers


def check_stages(lines: list[str], stop_index: int) -> list[str]:
    errors: list[str] = []
    headers = [(i, STAGE_HEADER.match(line.strip())) for i, line in enumerate(lines)
               if STAGE_HEADER.match(line.strip())]
    if not headers:
        errors.append("时间线未找到“[第N—M秒]”阶段结构")
        return errors
    spans = [(int(match.group(1)), int(match.group(2))) for _, match in headers]
    previous_end: int | None = None
    contiguous = True
    for start, end in spans:
        if end <= start:
            errors.append(f"阶段区间 {start}—{end} 秒不合法")
        if previous_end is not None and start != previous_end:
            contiguous = False
        previous_end = end
    if not contiguous:
        errors.append(f"时间线阶段必须严格递进且无重叠/断档，当前为 {spans}")
    for position, (line_index, _) in enumerate(headers):
        if position + 1 < len(headers):
            stop = headers[position + 1][0]
        else:
            stop = stop_index if stop_index > line_index else len(lines)
        names = block_names(lines, line_index + 1, stop)
        if names != STAGE_FIELDS_25:
            errors.append(
                f"时间线阶段 {spans[position]} 的六项字段缺失、超量或顺序错误，"
                f"当前为: {' → '.join(names) or '空'}"
            )
    return errors


def validate(text: str, model: str, allow_voice_field: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    lines = text.splitlines()
    line_list = lines

    content = [line.strip() for line in line_list if line.strip()]
    if not content:
        return ["Prompt Package 为空"], warnings
    if content[0].startswith(("{", "[")) and not STAGE_HEADER.match(content[0]):
        errors.append("最终 Prompt Package 不得使用 JSON 格式")

    titles = [line for line in line_list if line.strip().startswith("#")]
    if not titles or not TITLE_PATTERN.match(titles[0].strip()):
        errors.append("缺少合法标题行: # CLIP-X｜标题 <模型>视频提示词")

    voice_present = any(
        re.match(rf"^{VOICE_FIELD}\s*[：:]", line.strip()) for line in line_list
    )
    if voice_present and not allow_voice_field:
        errors.append(
            f"出现 {VOICE_FIELD}：但未显式授权声音控制；该字段只在用户明确要求时插入"
        )

    terminal = "全局限制与反向提示词" if model == "seedance-2.5" else "反向提示词"
    terminal_index = marker_positions(line_list, [terminal]).get(terminal, -1)

    if model == "minimax-h3":
        errors.extend(check_order(line_list, GLOBALS_H3))
        tail = [line.strip() for line in line_list if line.strip()]
        if not tail or tail[-1] != H3_LAST_LINE:
            errors.append(f"最后一行必须是 {H3_LAST_LINE}")
        positions = marker_positions(line_list, ["核心创意", "主风格"])
        if positions.get("主风格", -1) < positions.get("核心创意", -1):
            errors.append("核心创意：的第一行必须是 主风格：")
        errors.extend(check_ref_tail(line_list, model))
    elif model == "seedance-2.5":
        errors.extend(check_order(line_list, GLOBALS_25))
        errors.extend(check_stages(line_list, terminal_index))
        errors.extend(check_ref_tail(line_list, model))
    else:
        errors.extend(check_order(line_list, GLOBALS_20))
        shot_errors, shot_numbers = check_shot_draft(line_list, terminal_index)
        errors.extend(shot_errors)
        if not shot_numbers:
            warnings.append("没有可核对的分镜数量")
        errors.extend(check_ref_tail(line_list, model))

    if terminal_index < 0:
        errors.append(f"缺少终段字段: {terminal}：")
    else:
        tail_lines = [line.strip() for line in line_list[terminal_index:]]
        body = "\n".join(tail_lines)
        if NO_BGM_SENTENCE not in body:
            errors.append(f"{terminal}：未包含固定的无BGM禁令首句")
        for line in tail_lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#") or SHOT_HEADER.match(stripped) or STAGE_HEADER.match(stripped):
                errors.append(f"{terminal}：之后不得再出现正文、分镜或其他字段")
                break

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt_file", type=Path)
    parser.add_argument(
        "--model",
        required=True,
        choices=["seedance-2.0", "seedance-2.5", "minimax-h3"],
    )
    parser.add_argument(
        "--allow-voice-field",
        action="store_true",
        help="用户明确要求把声音/音色控制写入当前视频模型 Prompt 时使用",
    )
    args = parser.parse_args()

    try:
        raw = args.prompt_file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(f"INVALID: 无法读取 UTF-8 Prompt Package: {exc}", file=sys.stderr)
        return 1

    errors, warnings = validate(strip_fence(raw), args.model, args.allow_voice_field)

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1

    print(f"VALID: {args.model} Prompt Package 通过结构校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
