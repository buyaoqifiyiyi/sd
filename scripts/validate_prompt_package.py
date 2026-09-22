#!/usr/bin/env python3
"""Deterministic validator for a delivered STATE-08 video Prompt Package.

This script guards the *deliverable*, not the skill scaffold: it checks that a
produced Prompt package actually follows the selected final template
before the package is handed to the user. The body carries no title line and no
duration/format declaration: a package is located by file name (`G0N_CLIP-XXX.md`)
and delivery order, and `时长` is recovered from the Seedance 2.5 timeline's last
stage boundary. Structural/routing validation of the
skill itself stays owned by `scripts/validate_sd_film.py`.

Ownership:
  - Field names, order and mandatory-ness are owned by the selected Template:
    `templates/10_video_prompt.md` (Seedance 2.0),
    `templates/12_seedance_25_video_prompt.md` (Seedance 2.5),
    `templates/13_minimax_h3_video_prompt.md` (MiniMax H3).
  - `Clip ID`, `标题`, `目标时长`, `分辨率` and `宽高比` are production-plan /
    platform facts owned by STATE-07's Confirmed Clip Production Plan; they are
    never declared in the Prompt body. Seedance 2.0 and MiniMax H3 keep a
    `时长：` field because they have no time-line structure to carry it; Seedance
    2.5 has no title, `时长：` or `画幅：` field at all -- its target duration is
    the end boundary of the last time-line stage. That last boundary is the only
    one carrying the platform's whole-second `duration` constraint; intermediate
    stage boundaries are prompt text and may be fractional (`[0—3.2秒]`), so the
    equality with the confirmed duration stays a STATE-07/STATE-08 context check
    rather than a single-file assertion here.
  - This validator only asserts deterministically checkable facts. Beyond field
    structure it also asserts content-form rules that used to rely on the reader
    noticing: Canonical reference entries keep the
    `<Asset ID>｜<资产名>` form (no package file extension; a View Code or Purpose
    suffix when one Asset ID carries several images), the `主风格` field
    carries no generic negative list (`禁止` / `不要` / `避免` / `不做` / `拒绝` /
    `不得`), and a confirmed asset name that appears nowhere in the body while
    the body carries a close variant of it is reported as `已确认资产名逐字保留`.
    That last one is the semantic rule that a confirmed name is never rewritten
    or replaced by a synonym; a name under four characters is left alone because
    short Chinese names overlap by chance, a variant counts only when it shares a
    run of four characters with the confirmed name, and every report names the
    matching text so the judgement stays visible instead of silent. It also WARNs -- without blocking -- when `主风格` names none of the
    four Aesthetic Decision Lock dimensions, when a Seedance 2.5 time line of
    three or more stages is one uniform small/smooth drift (a single camera plan
    wearing several stage labels), and when a cutting or multi-space Clip cites
    only the master environment view (`_ENV-01`), and when a Clip plays along a
    glazed or reflective plane with neither a covering view nor a text lock on
    which side the subject is on, because all of these stay semantic judgements.
    It does not judge artistic quality, and passing it is not a substitute for the
    semantic Output QA described by each Template.
"""
from __future__ import annotations

import argparse
import re
import sys
from decimal import Decimal
from pathlib import Path

NO_BGM_SENTENCE = (
    "禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，"
    "只保留台词、环境声、动作音效和必要的自然声音。"
)

# Production-plan / platform facts (`Clip ID`, `标题`, `目标时长`, `分辨率`,
# `宽高比`) are owned by STATE-07's Confirmed Clip Production Plan and located by
# file name and delivery order, never declared in the Prompt body. No template
# carries a title heading, a `时长：` or a `画幅：` field any more; Seedance 2.5 has
# no length field at all, so its target duration is the end boundary of the last
# time-line stage, while 2.0 and H3 keep their target duration in the Clip Plan
# only. A body that re-declares any of these drifts back into self-certifying
# plan values.
BODY_PROHIBITED_RE = re.compile(r"^\s*(?:时长|画幅)\s*[：:]", re.M)
SHOT_HEADER = re.compile(r"^分镜\s*(\d+)\s*$")
SHOT_FIELD = re.compile(r"^([^：:]{1,12})：")
# 这条正则就是"分镜/阶段块内不得出现`维度：`行"的来源：`block_names` 把块内每一行
# `名称：`都收进字段名列表，再与十字段或六项字段逐项比对，多一条少一条都报错。
# 因此块内的编号子项（如表演八维）必须写成`1 时间｜…`这类不带冒号的形式——
# 模板里同一条约定写在 `templates/12_seedance_25_video_prompt.md` 的
# `**阶段内编号维度**`与 `templates/10_video_prompt.md` 的对应分镜段落。
# Stage boundaries are text inside the prompt body, not a platform parameter. The
# platform `duration` owns the Clip length in whole seconds, so only the *last*
# stage's end boundary inherits that constraint (it carries the target duration);
# intermediate boundaries may be fractional (`[0—3.2秒]`).
STAGE_HEADER = re.compile(
    r"^\[(?:第)?\s*(\d+(?:\.\d+)?)\s*[—\-–~至]\s*(\d+(?:\.\d+)?)\s*秒\]\s*$"
)
# Seedance 2.5 duration window (`templates/12_seedance_25_video_prompt.md`): the
# regular API path is 4—30s and 16—30s needs a strict pre-check PASS; only the
# Dreamina web surface reaches 30—180s. The last stage's end boundary is what
# carries the target duration now that the body declares no `时长：`.
SEEDANCE_25_MIN_SECONDS = 4
SEEDANCE_25_MAX_SECONDS = 30
SEEDANCE_25_LONG_SECONDS = 180
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
    "通用负向清单按 Negative Placement 收束到末尾唯一反向提示词段，"
    "内容相关约束写在它所约束的阶段"
)

SHOT_FIELDS_20 = [
    "景别", "镜头/机位", "起始状态", "画面描述", "人物动作与情绪",
    "空间关系", "道具状态", "台词", "音效", "镜头结尾状态",
]
GLOBALS_20 = [
    "参考资产", "首帧参考", "尾帧限制",
    "主风格", "人物一致性", "环境一致性",
]
STAGE_FIELDS_25 = [
    "画面与镜头", "人物动作与情绪", "空间与道具", "台词", "音效", "阶段结尾状态",
]
GLOBALS_25 = [
    "多模态参考资产", "参考素材职责与优先级", "首帧参考",
    "尾帧限制", "主风格", "全局叙事与画面设定", "全局一致性与执行约束", "时间线",
]
GLOBALS_H3 = [
    "参考素材说明", "核心创意", "画面过程说明", "反向提示词",
]
# Each template's first body field, which is also the first global field. The
# title line and the `时长：` / `画幅：` fields were removed from all three
# templates: `Clip ID`, `标题`, `目标时长`, `分辨率` and `宽高比` are owned by
# STATE-07's Confirmed Clip Production Plan, so a Prompt Package opens with its
# first body field and is located by file name and delivery order instead.
FIRST_GLOBAL_BY_MODEL = {
    "seedance-2.0": "参考资产",
    "seedance-2.5": "多模态参考资产",
    "minimax-h3": "参考素材说明",
}

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


def confirmed_asset_names(lines: list[str], model: str) -> list[tuple[str, str]]:
    """Return the `(Asset ID, 资产名)` pairs declared in the reference field.

    A second reader of the same block `check_reference_entries` validates, so the
    delivery-time name check below does not re-derive the entry syntax and cannot
    drift from it. Entries that name a platform attachment slot, a `REF-` asset or
    a user-provided frame carry no Asset ID and are simply absent here.
    """
    field = REFERENCE_FIELD_BY_MODEL[model]
    position = marker_positions(lines, [field]).get(field, -1)
    if position < 0:
        return []
    stop_names = [
        name for name in GLOBALS_20 + GLOBALS_25 + GLOBALS_H3 if name != field
    ]
    block = section_text(lines, position, stop_names)
    names: list[tuple[str, str]] = []
    for raw in block.splitlines():
        match = ASSET_ENTRY_RE.match(raw.strip())
        if not match:
            continue
        asset_id, remainder = match.group(1), match.group(2).strip()
        if not remainder.startswith("｜"):
            continue
        name = remainder[1:].split("｜", 1)[0]
        name = re.split(r"[；;]", name, maxsplit=1)[0].strip()
        if name:
            names.append((asset_id, name))
    return names


def longest_common_run(left: str, right: str) -> int:
    """Length of the longest run of characters shared by both strings.

    `difflib.SequenceMatcher` is not a substitute here: for
    `沈砚青色长衫` / `沈砚藏青长` it reports a longest match of two even with
    `autojunk=False`, because it aligns matching *blocks* rather than searching
    for the longest contiguous run, and that is exactly the pair this check has to
    separate. Strings here are a handful of characters, so the direct scan costs
    nothing and returns the number the rule actually means.
    """
    best = 0
    for start in range(len(left)):
        for end in range(start + best + 1, len(left) + 1):
            if left[start:end] in right:
                best = end - start
            else:
                # A longer span is missing, so this start position is done -- but
                # the next start may still extend past `best`.
                break
    return best


def check_confirmed_asset_names(lines: list[str], model: str) -> list[str]:
    """A confirmed asset name the body never uses verbatim, while a close variant appears.

    The rule that a confirmed entity name is carried into the Prompt unchanged --
    never rewritten, translated or swapped for a synonym -- is semantic, but its
    common failure is not: the reference entry keeps the Canonical name while the
    body silently renames the subject, and a reader scanning for a rename finds
    nothing because both strings look natural. A name that appears nowhere while
    a long variant of it does is that failure, and it is deterministic.

    Names shorter than four characters stay out, because two- and three-character
    Chinese names overlap by chance (`林薇` inside `林薇安`) and a check that fires
    on those trains its reader to ignore it. The required common run is four
    characters, which is where a deliberate rename separates from an incidental
    overlap in names of the length this library actually carries.
    """
    field = REFERENCE_FIELD_BY_MODEL[model]
    position = marker_positions(lines, [field]).get(field, -1)
    if position < 0:
        return []
    stop_names = [
        name for name in GLOBALS_20 + GLOBALS_25 + GLOBALS_H3 if name != field
    ]
    block = section_text(lines, position, stop_names)
    # The declaration itself is not the body: counting its lines would satisfy the
    # check by reading the very entry that declares the name.
    body = "\n".join(lines[position + len(block.splitlines()) :])
    errors: list[str] = []
    for asset_id, name in confirmed_asset_names(lines, model):
        if name in body or len(name) < 4:
            continue
        required = min(4, len(name) - 1)
        variants: set[str] = set()
        for run in re.findall(r"[\u4e00-\u9fff]{2,}", body):
            # Compare sliding windows, not whole runs: a name may appear inside a
            # longer Chinese clause, and a whole-run comparison would never match.
            for size in range(len(name) - 1, required - 1, -1):
                for start in range(0, len(run) - size + 1):
                    window = run[start : start + size]
                    if window in variants or window == name:
                        continue
                    if longest_common_run(window, name) >= required:
                        variants.add(window)
        if variants:
            # Longest first: the informative variant is the longest shared run, and
            # its own substrings would otherwise crowd it out of the report.
            listed = "、".join(sorted(variants, key=lambda item: (-len(item), item))[:3])
            errors.append(
                f"已确认资产名逐字保留：{asset_id}｜{name} 未在正文逐字出现，"
                f"正文出现近似写法“{listed}”；已确认名称不得改写、翻译或替换为同义词"
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
    Pass keep generic prohibitions in the single trailing 反向提示词 section while
    content-related constraints live in the stage they govern; either way a
    generic list left in the style field duplicates that control and splits
    ownership.
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


def check_environment_view_coverage(lines: list[str], model: str) -> list[str]:
    """Warn when a multi-space or cutting Clip cites only the master ENV view.

    Measured case: the package held four views per space, the prompt cited
    `ENV-00X｜…_ENV-01` only, and the generated clip broke wardrobe/space
    continuity ("参考图不够导致穿帮" -- the图 existed, they were simply not routed).
    The routing rule that owns this is `rules/02_asset_rules.md`'s 路由覆盖不变量;
    this stays a WARNING because one master view is legitimate for a simple,
    axis-stable Clip, and the script cannot judge whether the risk exists.
    """
    field = REFERENCE_FIELD_BY_MODEL[model]
    position = marker_positions(lines, [field]).get(field, -1)
    if position < 0:
        return []
    stop_names = [name for name in GLOBALS_20 + GLOBALS_25 + GLOBALS_H3 if name != field]
    block = section_text(lines, position, stop_names)
    env_views: dict[str, set[str]] = {}
    for raw in block.splitlines():
        match = ASSET_ENTRY_RE.match(raw.strip())
        if not match:
            continue
        asset_id, remainder = match.group(1), match.group(2)
        if not asset_id.startswith("ENV-"):
            continue
        view_match = re.search(r"_(ENV-\d{2}|EXT)\b", remainder)
        if view_match:
            env_views.setdefault(asset_id, set()).add(view_match.group(1).upper())
    if not env_views:
        return []
    stages = stage_camera_lines(lines)
    cuts = any(
        marker in "\n".join(stages) for marker in ("切到", "切至", "切换", "转场", "切场")
    )
    if not cuts and len(env_views) < 2:
        return []
    incomplete = [
        asset_id
        for asset_id, views in env_views.items()
        if views and not (views - {"ENV-01"})
    ]
    if not incomplete:
        return []
    return [
        "环境参考只出现母参考（`_ENV-01`），没有反向或侧向视图："
        f"{'、'.join(sorted(incomplete))}；本Clip存在切场或跨两个空间，"
        "反向背景、门窗朝向与轴线仅靠文字难以锁死——请按`rules/02_asset_rules.md`的路由覆盖不变量"
        "确认是否需要补 `_ENV-02` / `_ENV-03`。本条只提示，不阻断交付"
    ]


# `镜` alone is NOT a plane token: `画面与镜头`/`运镜`/`分镜` appear in every stage of
# every Clip, so a bare `镜` matched the shot-language field and made this warning fire
# on 10/10 Clips of a film with no mirror in it. Mirror/reflection evidence is the
# compounds below (`镜子`/`镜面`/`反光镜`/`倒影`/`反射`/`反光`), never the bare character.
PLANE_TOKENS = ("玻璃", "窗", "镜面", "镜子", "反光镜", "幕墙", "栏杆", "反光", "倒影", "反射", "映出")
# `内侧`/`外侧` only count when the plane word sits right in front of them:
# `校门内侧` is a place name, `窗内侧` is a side lock.
PLANE_ADJACENT_SIDE_RE = re.compile(r"(?:玻璃|窗|镜面|镜子|反光镜|幕墙|栏杆|门框|墙)(?:的)?(?:内|外)侧")
PLANE_LOCK_MARKERS = (
    "哪一侧", "同一侧", "不穿越", "不穿过", "只作前景遮挡", "前景遮挡",
    "正常镜像", "不表现反射", "不做反射", "无反射",
)
PLANE_LOCK_WINDOW = 24


def has_plane_lock(text: str) -> bool:
    """True when a plane token carries a side or reflection lock."""
    if PLANE_ADJACENT_SIDE_RE.search(text):
        return True
    for marker in PLANE_LOCK_MARKERS:
        start = 0
        while True:
            index = text.find(marker, start)
            if index == -1:
                break
            window = text[
                max(0, index - PLANE_LOCK_WINDOW): index + len(marker) + PLANE_LOCK_WINDOW
            ]
            if any(token in window for token in PLANE_TOKENS):
                return True
            start = index + 1
    return False


def check_plane_and_reflection_lock(lines: list[str], model: str) -> list[str]:
    """Warn when a Clip plays along a glazed/reflective plane without a lock.

    Measured case: a corridor Clip had the actor walking beside a window band, the
    reference set cited only the master view, and the text never said which side of
    the glass she was on or whether reflections were intended. The result put her
    body on both sides of the window plane -- a sleeve and a body silhouette visible
    inside the glass, i.e. penetrating a fixed structure with a duplicate copy.
    `rules/02_asset_rules.md` owns the routing/lock rule; this stays a WARNING
    because a plane may legitimately need no lock (it is pure background).
    """
    text = "\n".join(lines)
    if not any(token in text for token in PLANE_TOKENS):
        return []
    if has_plane_lock(text):
        return []
    field = REFERENCE_FIELD_BY_MODEL[model]
    position = marker_positions(lines, [field]).get(field, -1)
    if position < 0:
        return []
    stop_names = [name for name in GLOBALS_20 + GLOBALS_25 + GLOBALS_H3 if name != field]
    block = section_text(lines, position, stop_names)
    env_views: dict[str, set[str]] = {}
    for raw in block.splitlines():
        match = ASSET_ENTRY_RE.match(raw.strip())
        if not match or not match.group(1).startswith("ENV-"):
            continue
        view_match = re.search(r"_(ENV-\d{2}|EXT)\b", match.group(2))
        if view_match:
            env_views.setdefault(match.group(1), set()).add(view_match.group(1).upper())
    master_only = [
        asset_id for asset_id, views in env_views.items() if views and not (views - {"ENV-01"})
    ]
    if not env_views or not master_only:
        return []
    return [
        "本Clip出现窗 / 玻璃 / 镜面或反射平面，环境参考只列母参考（"
        + "、".join(sorted(master_only))
        + "），且文字里没有锁定“人物在结构的哪一侧”与反射策略；"
        "固定结构穿透与反射副本是常见失败——请按`rules/02_asset_rules.md`的固定平面与反射不变量"
        "补反向 / 侧向View，或在相应字段写明平面关系与反射是否表现。本条只提示，不阻断交付"
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


def format_seconds(value: Decimal) -> str:
    """Render a stage boundary as `3` / `3.2` (no trailing zeros, no `.0`)."""
    return f"{value.normalize():f}"


def check_stages(lines: list[str], stop_index: int) -> list[str]:
    errors: list[str] = []
    headers = [(i, STAGE_HEADER.match(line.strip())) for i, line in enumerate(lines)
               if STAGE_HEADER.match(line.strip())]
    if not headers:
        errors.append("时间线未找到“[第N—M秒]”阶段结构")
        return errors
    spans = [(Decimal(match.group(1)), Decimal(match.group(2))) for _, match in headers]
    previous_end: Decimal | None = None
    contiguous = True
    for start, end in spans:
        if end <= start:
            errors.append(
                f"阶段区间 {format_seconds(start)}—{format_seconds(end)} 秒不合法"
            )
        if previous_end is not None and start != previous_end:
            contiguous = False
        previous_end = end
    if not contiguous:
        errors.append(
            "时间线阶段必须严格递进且无重叠/断档，当前为 "
            + "、".join(f"{format_seconds(a)}—{format_seconds(b)}" for a, b in spans)
        )
    # Seedance 2.5 has no `时长：` field: the target duration is the end boundary of
    # the last stage, and that boundary is the single place inside the prompt that
    # carries the platform `duration` constraint -- so it must be whole seconds.
    # Intermediate boundaries stay free text. Whether the last boundary *equals*
    # STATE-07's confirmed duration needs the plan and stays a STATE-07/STATE-08
    # context check, never a value invented from the file alone.
    last_end = spans[-1][1]
    if last_end != last_end.to_integral_value():
        errors.append(
            f"时间线末阶段的末端边界 {format_seconds(last_end)} 秒必须是整数秒；"
            "平台`duration`参数只接受整数秒，而该边界同时承担STATE-07确认的目标时长"
            "（中间阶段边界可以是小数）"
        )
    elif not SEEDANCE_25_MIN_SECONDS <= last_end <= SEEDANCE_25_LONG_SECONDS:
        errors.append(
            f"时间线末阶段的末端边界 {format_seconds(last_end)} 秒不是有效目标时长；"
            f"常规为{SEEDANCE_25_MIN_SECONDS}—{SEEDANCE_25_MAX_SECONDS}秒"
            f"（网页端Long Video可到{SEEDANCE_25_LONG_SECONDS}秒），且必须等于STATE-07确认的目标时长"
        )
    for position, (line_index, _) in enumerate(headers):
        if position + 1 < len(headers):
            stop = headers[position + 1][0]
        else:
            stop = stop_index if stop_index > line_index else len(lines)
        names = block_names(lines, line_index + 1, stop)
        if names != STAGE_FIELDS_25:
            errors.append(
                f"时间线阶段 {format_seconds(spans[position][0])}—"
                f"{format_seconds(spans[position][1])}秒 的六项字段缺失、超量或顺序错误，"
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
    if titles:
        errors.append(
            "Prompt Package 不得出现标题行；`Clip ID`与`标题`属于STATE-07的"
            "Confirmed Clip Production Plan，Prompt以文件名与交付顺序定位"
        )

    if BODY_PROHIBITED_RE.search(text):
        errors.append(
            "Prompt正文不得声明`时长：`或`画幅：`；`目标时长`、`分辨率`与`宽高比`"
            "由STATE-07的Confirmed Clip Production Plan拥有"
            + (
                "，Seedance 2.5的目标时长由时间线末阶段的末端边界承担"
                if model == "seedance-2.5"
                else "，本模型的目标时长只在Clip Plan中声明"
            )
        )

    first_field = FIRST_GLOBAL_BY_MODEL[model]
    if marker_positions(line_list, [first_field])[first_field] != 0:
        errors.append(f"第一条字段必须是 {first_field}：，其前不得出现标题行、时长或画幅等计划信息")

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
    errors.extend(check_confirmed_asset_names(line_list, model))
    errors.extend(check_style_field_negatives(line_list, model))
    warnings.extend(check_style_lock_labels(line_list, model))
    warnings.extend(check_camera_contrast(line_list, model))
    warnings.extend(check_environment_view_coverage(line_list, model))
    warnings.extend(check_plane_and_reflection_lock(line_list, model))

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


def demo() -> None:
    """Self-check for the rule added here: `check_confirmed_asset_names`.

    A minimal body is enough: the check reads only the reference field and the
    lines after it. It runs on every invocation, so the rule cannot rot silently.
    """
    # Anchored pairs, so the rule cannot pass by accident.
    assert longest_common_run("沈砚青色长衫", "青色长衫") == 4
    assert longest_common_run("沈砚青色长衫", "沈砚青色长衫") == 6
    assert longest_common_run("林薇", "林薇安") == 2
    assert longest_common_run("沈砚青色长衫", "藏青长") == 1

    named = [
        "参考资产：",
        "- PROP-004｜沈砚青色长衫；用途：造型基准；锁定 / 保持：颜色与领口",
        "首帧参考：",
        "画面描述：",
        "沈砚青色长衫的下摆扫过门槛。",
    ]
    assert not check_confirmed_asset_names(named, "seedance-2.0"), "逐字保留的名称被误报"

    renamed = list(named)
    renamed[-1] = "沈砚青色长袍的下摆扫过门槛。"
    issues = check_confirmed_asset_names(renamed, "seedance-2.0")
    assert len(issues) == 1, f"近似改名未被检出: {issues}"
    assert "青色长袍" in issues[0], f"报错未点名匹配文本: {issues[0]}"

    # Short names overlap by chance in Chinese, so a shorter variant stays silent
    # rather than training the reader to ignore this check.
    short = [
        "参考资产：",
        "- CHAR-001｜林薇；用途：身份基准",
        "首帧参考：",
        "画面描述：",
        "林薇安抬手按住门框。",
    ]
    assert not check_confirmed_asset_names(short, "seedance-2.0"), "短名碰撞被误报"


if __name__ == "__main__":
    demo()
    raise SystemExit(main())
