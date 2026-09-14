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
  - This validator only asserts deterministically checkable facts. Beyond field
    structure it also asserts two content-form rules that used to rely on the
    reader noticing: Canonical reference entries keep the
    `<Asset ID>｜<资产名>` form (no package file extension; a View Code or Purpose
    suffix when one Asset ID carries several images), and the `主风格` field
    carries no generic negative list (`禁止` / `不要` / `避免` / `不做` / `拒绝` /
    `不得`). It also WARNs -- without blocking -- when `主风格` names none of the
    four Aesthetic Decision Lock dimensions, and when a Seedance 2.5 time line of
    three or more stages is one uniform small/smooth drift (a single camera plan
    wearing several stage labels), because both stay semantic judgements. It does
    not judge artistic quality, and passing it is not a substitute for the semantic
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

# Canonical reference-entry form (`references/asset_package.md`):
#   `<Asset ID>｜<资产名>` (+ `_<View Code>` / `_<Purpose>` when one Asset ID
#   carries several Canonical images). The package file name, extension included,
#   never enters the prompt. Entries starting with `REF-*`, `Project Color
#   Reference（非资产）` or a user-provided frame keep their own registered names.
ASSET_ENTRY_RE = re.compile(
    r"^(?:-\s*)?(?:@(?:图片|视频|音频)\d+\s*[：:]\s*)?"
    r"((?:BOARD-)?(?:CHAR|ENV|PROP|FX)-\d{3})(.*)$"
)
REFERENCE_FIELD_BY_MODEL = {
    "seedance-2.0": "参考资产",
    "seedance-2.5": "多模态参考资产",
    "minimax-h3": "参考素材说明",
}
FILE_EXTENSION_RE = re.compile(r"\.(?:png|jpe?g|webp|gif|bmp|tiff?|heic)\s*$", re.I)
PURPOSE_OR_VIEW_SUFFIX_RE = re.compile(
    r"_(?:ENV-\d{2}|EXT|Identity|Costume|Scale|Layout|Material|State|FX Phase)\s*$"
)
NEGATIVE_STYLE_TOKENS = ("禁止", "不要", "避免", "不做", "拒绝", "不得")
# The establishing `主风格` must carry the four Aesthetic Decision Lock dimensions
# (`### 主风格 Minimum Content Rule`). Naming them in the field is what makes the
# requirement checkable at delivery time; a field that names none of them is not
# attempting the structure at all. Later delta-only Clips keep the anchors, so this
# stays a WARNING: partial coverage and phrasing still need human judgement.
STYLE_LOCK_LABELS = (
    "反差与光比结构",
    "色彩对抗关系",
    "构图主张",
    "视觉母题与变化轨迹",
)
# Multi-stage one-take Clips must show an observation hierarchy: adjacent stages
# differ recognisably in distance / angle / direction / speed / stillness.
# A time line where every stage is qualified as a small, smooth drift is a single
# camera plan (in practice a locked-off master shot) wearing five labels. This stays
# a WARNING because a deliberately still film is a legitimate choice and the token
# test cannot judge whether the stillness serves the drama.
CAMERA_SMALLNESS_TOKENS = (
    "极小幅", "极小", "极缓", "极慢", "很慢", "平稳", "轻缓", "缓慢", "轻微",
)
CAMERA_CONTRAST_MARKERS = (
    "静止", "不动", "固定机位", "固定不动", "锁定机位", "停住", "停驻", "反向", "反转",
    "加速", "提速", "快速", "迅速", "大幅", "明显变化", "拉开", "推近", "升起", "升高",
    "俯冲", "环绕", "横移", "跟拍", "跟随", "猛推", "急推",
)
NEGATION_PREFIXES = ("不", "无", "没", "未", "勿")


def contains_unnegated(text: str, tokens: tuple[str, ...]) -> bool:
    """True when a token appears and is not negated right before it.

    Camera plans are full of negated statements ("机位不摇晃"、"不切换、不环绕"), and a
    naive substring test reads them as the opposite of what they say.
    """
    for token in tokens:
        start = 0
        while True:
            index = text.find(token, start)
            if index == -1:
                break
            prefix = text[max(0, index - 2):index]
            if not any(negation in prefix for negation in NEGATION_PREFIXES):
                return True
            start = index + 1
    return False
# A reference entry carrying only a platform attachment slot (`图片1`) or nothing
# names no asset at all, so no file in the package can ever be mapped to it.
PLATFORM_ENTRY_RE = re.compile(
    r"^(?:-\s*)?@(?:图片|视频|音频)\d+\s*[：:]\s*(.*)$"
)
PLATFORM_PLACEHOLDER_RE = re.compile(r"^(?:图片|视频|音频|附件)\s*\d*$")
GENERIC_NEGATIVE_RULE = (
    "主风格：不得保留通用负向清单（出现“{token}”）；"
    "这类约束按 Negative Placement 收束到末尾唯一反向提示词段"
)

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


def check_reference_entries(lines: list[str], model: str) -> list[str]:
    """Canonical reference entries keep the `<Asset ID>｜<资产名>` form.

    Two deterministic failures this catches, both observed in a delivered package:
    a package file name with its extension pasted into the reference name
    (`PROP-001｜Identity.png`), and one Asset ID used for several Canonical images
    without a View Code or Purpose suffix, which makes the entry unmappable back to
    a file. Entries that start with `REF-*`, `Project Color Reference（非资产）` or
    a user-provided frame keep their own registered names and stay exempt; whether
    the *meaning* of a reference entry is right remains a human judgement.
    """
    errors: list[str] = []
    field = REFERENCE_FIELD_BY_MODEL[model]
    position = marker_positions(lines, [field]).get(field, -1)
    if position < 0:
        return errors
    stop_names = [
        name for name in GLOBALS_20 + GLOBALS_25 + GLOBALS_H3 if name != field
    ]
    block = section_text(lines, position, stop_names)
    entries: list[tuple[str, str]] = []
    for raw in block.splitlines():
        platform = PLATFORM_ENTRY_RE.match(raw.strip())
        if platform:
            value = re.split(r"[；;]", platform.group(1), maxsplit=1)[0].strip()
            if not value:
                errors.append("参考条目缺少引用名；必须写 `<资产ID>｜<资产名>` 或该素材的登记名")
            elif PLATFORM_PLACEHOLDER_RE.match(value):
                errors.append(
                    f"参考条目只写了平台附件位（{value}）；必须写 `<资产ID>｜<资产名>` 或该素材的登记名"
                )
        match = ASSET_ENTRY_RE.match(raw.strip())
        if not match:
            continue
        asset_id, remainder = match.group(1), match.group(2).strip()
        if not remainder.startswith("｜"):
            errors.append(
                f"参考条目 {asset_id} 缺少引用名形态；必须是 `<资产ID>｜<资产名>`（分隔符为全角｜）"
            )
            continue
        # An entry reads `<Asset ID>｜<资产名>；用途：…；锁定 / 保持：…`, so the name
        # ends at the first `｜` (extra clause) or `；` (purpose clause).
        name = remainder[1:].split("｜", 1)[0]
        name = re.split(r"[；;]", name, maxsplit=1)[0].strip()
        entries.append((asset_id, name))
    counts: dict[str, int] = {}
    for asset_id, _ in entries:
        counts[asset_id] = counts.get(asset_id, 0) + 1
    for asset_id, name in entries:
        if not name:
            errors.append(f"参考条目 {asset_id}｜ 缺少资产名；引用名必须是 `<资产ID>｜<资产名>`")
            continue
        if FILE_EXTENSION_RE.search(name):
            errors.append(
                f"参考条目 {asset_id}｜{name} 携带文件扩展名；"
                "包内文件名不进入 Prompt 引用名，只写资产名与 View Code / Purpose"
            )
        if (
            counts[asset_id] > 1
            and not asset_id.startswith("BOARD-")
            and not PURPOSE_OR_VIEW_SUFFIX_RE.search(name)
        ):
            errors.append(
                f"参考条目 {asset_id}｜{name} 在同一 Prompt 中出现 {counts[asset_id]} 次，"
                "必须补 View Code 或 Purpose 后缀（如 `_ENV-01`、`_Identity`、`_State`）以区分是哪一张"
            )
    return errors


def style_field_text(lines: list[str], model: str) -> str:
    """The `主风格` content: its own section, or the H3 style line only.

    H3 keeps `主风格：` inside `核心创意：`, whose second line carries subject and
    camera work -- that line is out of scope for style-field assertions.
    """
    if model == "minimax-h3":
        return "\n".join(
            line for line in lines if line.strip().startswith(("主风格：", "主风格:"))
        )
    position = marker_positions(lines, ["主风格"]).get("主风格", -1)
    if position < 0:
        return ""
    return section_text(
        lines, position, [name for name in GLOBALS_20 + GLOBALS_25 if name != "主风格"]
    )


def check_style_field_negatives(lines: list[str], model: str) -> list[str]:
    """`主风格` carries executable style, not a generic negative list.

    `## Field Ownership Assignment / State Once Gate` and the Negative Placement
    Pass move generic prohibitions into the single trailing 反向提示词 section;
    leaving them in the style field duplicates that control and splits ownership.
    Deterministic scope is a fixed token list inside the 主风格 content
    (禁止 / 不要 / 避免 / 不做 / 拒绝 / 不得, the rule's own "同义负向约束" set);
    the fix is to rewrite the boundary positively. Bare `不X` phrasings and other
    paraphrases stay outside this list because the four locks legitimately write
    what they ruled out -- those need human judgement, not a token ban.
    """
    errors: list[str] = []
    text = style_field_text(lines, model)
    for token in NEGATIVE_STYLE_TOKENS:
        if token in text:
            errors.append(GENERIC_NEGATIVE_RULE.format(token=token))
    return errors


def check_style_lock_labels(lines: list[str], model: str) -> list[str]:
    """Warn when the `主风格` field names none of the four lock dimensions.

    Non-blocking on purpose: the rule requires the four dimensions once when the
    style is established and their anchors afterwards, and a delta-only Clip may
    phrase them compactly. Naming none of the four means no reader -- or reviewer --
    can verify the field against the Aesthetic Decision Lock, which is exactly the
    failure that reached delivery twice. Partial naming is not flagged here and
    stays a checklist judgement.
    """
    text = style_field_text(lines, model)
    if not text:
        return []
    if any(label in text for label in STYLE_LOCK_LABELS):
        return []
    return [
        "主风格：未出现四项Aesthetic Decision Lock维度名（"
        + " / ".join(STYLE_LOCK_LABELS)
        + "）；建立轮必须各写一次，后续Clip保留可核查锚点。本条只提示，不阻断交付"
    ]


def stage_camera_lines(lines: list[str]) -> list[str]:
    """`画面与镜头` of every time-line stage, in order."""
    headers = [index for index, line in enumerate(lines) if STAGE_HEADER.match(line.strip())]
    cameras: list[str] = []
    for position, index in enumerate(headers):
        stop = headers[position + 1] if position + 1 < len(headers) else len(lines)
        for line in lines[index + 1: stop]:
            stripped = line.strip()
            if stripped.startswith(("画面与镜头：", "画面与镜头:")):
                cameras.append(stripped)
                break
    return cameras


def check_camera_contrast(lines: list[str], model: str) -> list[str]:
    """Warn when a multi-stage one-take Clip is one uniform drift.

    Scope: Seedance 2.5 time lines with at least three stages, where no stage states
    stillness, a stop, a reversal, a fast move or a clear change of magnitude, and at
    least half of the stages qualify the movement as small / smooth. Movement *types*
    may well differ ("后退 / 弧移 / 低降 / 靠近 / 后移") while the amplitude stays
    uniformly sub-perceptual -- that is the measured case this catches: the delivered
    clip was a locked-off two-shot for its whole 30 seconds. Negated camera statements
    ("不摇晃"、"不环绕") are read as negations, two-stage Clips pass silently, and the
    heuristic never claims to judge whether stillness serves the drama.
    """
    if model != "seedance-2.5":
        return []
    stages = stage_camera_lines(lines)
    if len(stages) < 3:
        return []
    if any(contains_unnegated(stage, CAMERA_CONTRAST_MARKERS) for stage in stages):
        return []
    small = sum(
        1 for stage in stages if contains_unnegated(stage, CAMERA_SMALLNESS_TOKENS)
    )
    if small * 2 < len(stages):
        return []
    return [
        f"时间线{len(stages)}个阶段的运镜语汇同质（每段都写作极/平稳类小幅缓动，"
        "没有任何一段写明静止、停驻、反向或幅度变化）；一镜到底只约束“不切”，"
        "不约束镜头内运动层次——请确认相邻阶段在距离 / 角度 / 方向 / 速度 / 是否静止上"
        "至少一项可指认不同。本条只提示，不阻断交付"
    ]


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

    errors.extend(check_reference_entries(line_list, model))
    errors.extend(check_style_field_negatives(line_list, model))
    warnings.extend(check_style_lock_labels(line_list, model))
    warnings.extend(check_camera_contrast(line_list, model))

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
