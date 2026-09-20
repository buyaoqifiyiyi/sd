#!/usr/bin/env python3
"""Deterministic structural, routing, readability and landing-coverage validation for SD Film.

No release number is hard-coded here: the version lives in `SKILL.md` only, so this
header cannot drift out of date on its own.
"""
# Skill维护层：只在修改本Skill时读取，不参与影视生产。
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED = (
    "SKILL.md", "core/pipeline.md", "core/runtime-state.md", "core/rule-priority.md",
    "modules/screenwriter.md", "modules/director.md", "modules/spatial-blocking.md",
    "modules/clip-planning.md", "modules/model-selection.md", "modules/image-model-selection.md", "modules/prompt-generation.md", "modules/assets.md",
    "adapters/seedance-2.0.md", "adapters/seedance-2.5.md", "adapters/minimax-h3.md", "adapters/gpt-image.md", "adapters/midjourney.md",
    "knowledge/prompt_compilation/minimax_h3_compilation.md",
    "workflows/01_project_setup_workflow.md", "workflows/10_clip_production_workflow.md", "workflows/11_video_generation_workflow.md",
    "templates/00_project_start_template.md", "templates/20_clip_plan.md", "templates/10_video_prompt.md", "templates/12_seedance_25_video_prompt.md", "templates/13_minimax_h3_video_prompt.md", "templates/14_midjourney_asset_prompt.md", "templates/24_gpt_image_asset_prompt.md",
    "templates/25_look_frame_prompt.md",
    "references/module_contracts.md",
    "references/module_contracts_production.md",
    "references/module_contracts_auxiliary.md",
    "references/module_contracts_knowledge.md",
    "references/project_state_contract.md", "rules/automation_mode.md", "rules/02_asset_rules.md",
    "knowledge/environment_multi_view_reconstruction.md", "knowledge/clip_preflight_check.md", "knowledge/reference_budget.md",
    "knowledge/quality/aesthetic_judgement.md",
    "knowledge/medium_profiles.md",
    "knowledge/platform_profiles.md",
    "references/context_budget.md",
    "references/asset_package.md",
    "references/maintenance_self_check.md",
    "references/maintenance_self_check_protocol.md",
    "references/regression_scenarios.md",
    "references/regression_scenarios_craft.md",
    "references/regression_scenarios_director.md",
    "references/regression_scenarios_system.md",
    "references/regression_scenarios_parameters.md",
    "references/regression_scenarios_maintenance.md",
    "references/recovery_guards.md",
    "scripts/validate_prompt_package.py",
    "scripts/build_asset_package.py",
)

BUDGET_TARGET_BYTES = 50 * 1024
BUDGET_CEILING_BYTES = 100 * 1024
SKILL_ENTRY_MAX_BYTES = 12 * 1024
SKILL_ENTRY_MAX_LINES = 120
LEDGER_CLASSES = ("COMPOSITE", "INTEGRAL", "NON_RUNTIME")
NON_SKILL_DIRS = {".git", ".workbuddy", ".zcode", "tmp", "__pycache__", ".venv", "node_modules"}

SELF_CHECK_DIMENSIONS = (
    "Duplicate Rule Check", "Conflict Check", "Terminology Drift Check", "Rule Ownership Check",
    "Prompt Pollution Check", "Routing Integrity Check", "Template Consistency Check",
    "Reference Integrity Check", "State / Continuity Compatibility Check", "User Guide Sync Check",
    "Regression Check", "Change Classification Check", "Runtime Claim / Legacy Recovery Check",
    "Standalone Skill Discovery Check", "Context Budget Check",
    "Claim / Evidence Credibility Check",
    "Stage-To-Prompt Landing Coverage Check",
    "FAST Invariant And Delivery Receipt Check",
)

MAIN_WORKFLOWS = (
    ("01_project_setup_workflow.md", "STATE-00"),
    ("02_script_analysis_workflow.md", "STATE-01"),
    ("03_asset_discovery_workflow.md", "STATE-02"),
    ("04_character_asset_workflow.md", "STATE-03"),
    ("05_environment_asset_workflow.md", "STATE-03"),
    ("06_prop_asset_workflow.md", "STATE-03"),
    ("07_visual_development_workflow.md", "STATE-04"),
    ("08_scene_breakdown_workflow.md", "STATE-05"),
    ("09_shot_design_workflow.md", "STATE-06"),
    ("10_clip_production_workflow.md", "STATE-07"),
    ("11_video_generation_workflow.md", "STATE-08"),
    ("13_review_workflow.md", "STATE-09"),
    ("15_fx_asset_workflow.md", "STATE-03"),
)

WORKFLOW_STATE_RE = re.compile(r"^当前阶段：\n+\s*(STATE-\d\d)", re.M)
WORKFLOW_POSITION_RE = re.compile(r"^# Workflow Position\s*$", re.M)
WORKFLOW_ROUTE_FIELDS = ("下一阶段：", "对应下一Workflow：")
WORKFLOW_ROUTE_OWNER = "workflows/workflow_map.md"
MAIN_STATE_COUNT = 10
PIPELINE_RESTATEMENT_RE = re.compile(r"^#\s(Next Workflow|Workflow Relationship)\s*$", re.M)
COMPLETION_GATE_HEADING_RE = re.compile(r"^# Completion Gate\s*$", re.M)
LEGACY_STATUS_HEADING_RE = re.compile(r"^# State Update\s*$", re.M)
WORKFLOW_REF_RE = re.compile(r"\b(\d\d_[a-z0-9_]+_workflow)\.md")
MAIN_STATE_OF_WORKFLOW = dict(MAIN_WORKFLOWS)
# Auxiliary / conditional / resume / legacy workflows do not own a main STATE, so a
# main workflow may point at them without restating the pipeline route.
AUXILIARY_WORKFLOWS = frozenset(
    {
        "10_storyboard_workflow.md",
        "12_editing_workflow.md",
        "14_series_management_workflow.md",
        "16_sequence_planning_workflow.md",
        "17_poster_design_workflow.md",
        "18_project_resume_workflow.md",
        "20_seed_audio_voice_asset_workflow.md",
        "21_seed_music_score_workflow.md",
        "22_reference_film_study_workflow.md",
        "10_shot_execution_plan_workflow.md",
        "19_clip_planning_workflow.md",
    }
)
FINAL_PRINCIPLE_RE = re.compile(r"^#\sFinal Principle\s*$", re.M)
FINAL_PRINCIPLE_MAX_BYTES = 150
INTERNAL_PATH_REF_RE = re.compile(
    r"(?:templates|references|knowledge|rules|workflows|core|modules|adapters|scripts|agents)"
    r"/[A-Za-z0-9_./\-]+\.(?:md|py|json|yaml)"
)

def read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8-sig")

def duplicate_sd_film_entries(root: Path) -> list[str]:
    """Find nested entries that a recursive skill discovery scan could register."""
    canonical = (root / "SKILL.md").resolve()
    duplicates: list[str] = []
    for candidate in root.rglob("SKILL.md"):
        if candidate.resolve() == canonical or ".git" in candidate.parts:
            continue
        try:
            contents = candidate.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        if re.search(r"^name:\s*sd-film\s*$", contents, re.MULTILINE):
            duplicates.append(candidate.relative_to(root).as_posix())
    return sorted(duplicates)

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

def read_size_ledger_rows(root: Path) -> list[dict[str, str]]:
    """Size Index rows keyed by its own header, so column order can change."""
    rows: list[dict[str, str]] = []
    header: list[str] | None = None
    for line in read(root, "references/context_budget.md").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            header = None
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if header is None:
            if cells and cells[0] == "File":
                header = cells
            continue
        if all(set(cell) <= {"-"} for cell in cells if cell) and any(cells):
            continue
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return rows

def _column(row: dict[str, str], prefix: str) -> str:
    for key, value in row.items():
        if key.lower().startswith(prefix):
            return value
    return ""

def read_size_ledger(root: Path) -> dict[str, str]:
    """The Size Index rows as {relative path: file class}."""
    return {row["File"]: _column(row, "class") for row in read_size_ledger_rows(root)}

def read_ledger_sizes(root: Path) -> dict[str, float]:
    """Declared size in KB per ledger row, so a stale ledger is detectable."""
    declared: dict[str, float] = {}
    for row in read_size_ledger_rows(root):
        found = re.search(r"([\d.]+)\s*KB", _column(row, "size"), re.I)
        if found:
            declared[row["File"]] = float(found.group(1))
    return declared

def read_ledger_reviews(root: Path) -> dict[str, str]:
    """Review-by date per ledger row."""
    return {row["File"]: _column(row, "review") for row in read_size_ledger_rows(root)}

def check_ledger_sizes(entries, declared, tolerance: float = 0.20) -> list[str]:
    """The ledger records a size per entry; if reality drifts past tolerance the
    ledger is stale and no longer describes what it claims to describe."""
    errors: list[str] = []
    sizes = dict(entries)
    for relative, recorded in declared.items():
        if relative not in sizes:
            continue
        actual = sizes[relative] / 1024
        if recorded > 0 and abs(actual - recorded) / recorded > tolerance:
            errors.append(
                f"context budget ledger size is stale for {relative} "
                f"(recorded {recorded} KB, actual {actual:.1f} KB); update the ledger"
            )
    return errors

def _shipped_text_files(root: Path) -> list[str]:
    shipped: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in REACHABILITY_TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if any(part in NON_SKILL_DIRS for part in relative.parts):
            continue
        if ".pre-" in path.name or "backup" in path.name.lower():
            continue
        shipped.append(relative.as_posix())
    return shipped


def unreachable_shipped_files(root: Path) -> list[str]:
    """Shipped files outside every read path, exemptions excluded.

    Returns the same set `check_reachability` would fail on, so the periodic
    audit can show the backlog instead of only the blocking case.
    """
    shipped = _shipped_text_files(root)
    reachable = _reachable_files(root, shipped)
    return [
        relative for relative in sorted(set(shipped) - reachable)
        if relative not in REACHABILITY_ALLOWED_UNREACHABLE
        and not declares_maintenance(root / relative)
    ]


def exempt_unreachable_files(root: Path) -> list[tuple[str, str]]:
    """Unreachable files that are exempt on purpose, with the reason.

    Reported alongside the blocking list so a green run still shows what was
    skipped -- an exemption nobody can see is indistinguishable from a miss.
    """
    shipped = _shipped_text_files(root)
    reachable = _reachable_files(root, shipped)
    out: list[tuple[str, str]] = []
    for relative in sorted(set(shipped) - reachable):
        if relative in REACHABILITY_ALLOWED_UNREACHABLE:
            out.append((relative, "non-runtime doc"))
        elif declares_maintenance(root / relative):
            out.append((relative, MAINTENANCE_MARKER))
    return out


def build_report(root: Path) -> str:
    entries = sorted(scan_markdown(root), key=lambda item: -item[1])
    ledger = read_size_ledger(root)
    total = sum(size for _, size in entries)
    lines = [
        "SD Film Size And Readability Report",
        f"  files {len(entries)}   total {total / 1024:.0f} KB"
        f"   review line {BUDGET_TARGET_BYTES // 1024} KB   ceiling {BUDGET_CEILING_BYTES // 1024} KB",
        "",
        "  largest files (UTF-8 bytes)",
    ]
    for relative, size in entries[:10]:
        mark = f"  [{ledger[relative]}]" if relative in ledger else ""
        lines.append(
            f"    {size / 1024:7.1f} KB  {size * 100 / BUDGET_CEILING_BYTES:5.1f}% of ceiling"
            f"  {relative}{mark}"
        )
    over = [(r, s) for r, s in entries if s > BUDGET_TARGET_BYTES]
    lines += ["", f"  past the review line: {len(over)}   (informational, not a defect)"]
    for relative, size in over:
        lines.append(f"    {ledger.get(relative, 'not indexed'):12s} {size / 1024:7.1f} KB  {relative}")
    pending = unindexed_over_review_line(root)
    if pending:
        lines += ["", f"  runtime files past the review line with no read entry yet: {len(pending)}"]
        for relative in pending:
            lines.append(f"    {relative}")
    reviews = read_ledger_reviews(root)
    if reviews:
        lines += ["", "  review by"]
        for relative, when in sorted(reviews.items()):
            lines.append(f"    {when:12s} {relative}")

    # Orphan content: exists, ships, and no read path can reach it. The validator
    # fails on these; the report also lists the exemptions so the periodic audit
    # can see what was skipped on purpose rather than trusting a green run.
    orphans = unreachable_shipped_files(root)
    lines += ["", f"  unreachable (no read path): {len(orphans)}"
                 "   (blocking when non-zero)"]
    for relative in orphans:
        lines.append(f"    {(root / relative).stat().st_size / 1024:7.1f} KB  {relative}")
    allowed = exempt_unreachable_files(root)
    if allowed:
        lines += ["", f"  unreachable but declared exempt: {len(allowed)}"]
        for relative, reason in allowed:
            lines.append(f"    {reason:20s} {relative}")
    return "\n".join(lines)

def check_context_budget(entries, ledger) -> list[str]:
    """Only the ceiling blocks a commit. Crossing the review line is a prompt to
    look at how the file is read, so an unindexed file past it becomes a report
    item rather than a failure. A stale or dangling index entry still fails, so
    the index never decays into a standing list."""
    errors: list[str] = []
    sizes = dict(entries)
    ledger = dict(ledger)
    for relative, size in entries:
        if size > BUDGET_CEILING_BYTES:
            errors.append(
                f"file reached the size ceiling ({size} > {BUDGET_CEILING_BYTES} bytes), "
                f"split it: {relative}"
            )
    for relative, file_class in sorted(ledger.items()):
        if file_class not in LEDGER_CLASSES:
            errors.append(f"size index has an unknown class ({file_class}): {relative}")
        if relative not in sizes:
            errors.append(f"size index points at a missing markdown file: {relative}")
        elif sizes[relative] <= BUDGET_TARGET_BYTES:
            errors.append(
                f"size index entry is stale ({sizes[relative]} bytes, back within the review line), "
                f"remove it: {relative}"
            )
    return errors

def declares_non_runtime(path: Path) -> bool:
    """A file no workflow reads cannot lose rules to its own length, so it sits
    outside the review line — but it has to declare that about itself."""
    return "非运行时文件" in path.read_text(encoding="utf-8-sig")

def unindexed_over_review_line(root: Path) -> list[str]:
    """Runtime files past the review line that the Size Index does not describe
    yet. Reported by --report so the periodic audit can fill the entry in; it is
    never a failure, because length alone is not a defect."""
    ledger = read_size_ledger(root)
    pending: list[str] = []
    for relative, size in scan_markdown(root):
        if size <= BUDGET_TARGET_BYTES or relative in ledger:
            continue
        if declares_non_runtime(root / relative):
            continue
        pending.append(relative)
    return pending

def check_read_entries(rows) -> list[str]:
    """An entry nobody can follow is worth less than no entry, so every runtime
    entry has to say where to start reading."""
    errors: list[str] = []
    for row in rows:
        relative = row.get("File", "")
        if _column(row, "class") == "NON_RUNTIME":
            continue
        if not _column(row, "read").strip():
            errors.append(f"a size index entry must state its read entry: {relative}")
    return errors

def section_after(text: str, match: "re.Match[str]") -> str:
    """The body of a matched heading, up to the next level-1 heading."""
    following = re.search(r"^# ", text[match.end():], re.M)
    if following:
        return text[match.end():match.end() + following.start()]
    return text[match.end():]

def check_workflow_routing(root: Path) -> list[str]:
    """Routing Integrity Check: a workflow file declares which STATE it belongs to
    and nothing else. Stage order, predecessor and next workflow belong to
    workflows/workflow_map.md, so a second copy here can only drift."""
    errors: list[str] = []
    workflows = root / "workflows"
    covered: set[str] = set()
    for name, declared in MAIN_WORKFLOWS:
        path = workflows / name
        if not path.is_file():
            errors.append(f"main workflow is missing: workflows/{name}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        match = WORKFLOW_STATE_RE.search(text)
        found = match.group(1) if match else None
        if found != declared:
            errors.append(
                f"workflows/{name} must self-declare 当前阶段 {declared}, found {found or 'nothing'}"
            )
        if found:
            covered.add(found)
        position = WORKFLOW_POSITION_RE.search(text)
        if not position:
            errors.append(f"workflows/{name} is missing its Workflow Position block")
        else:
            for field in WORKFLOW_ROUTE_FIELDS:
                if field in section_after(text, position):
                    errors.append(
                        f"workflows/{name} must not restate {field} inside Workflow Position; "
                        f"{WORKFLOW_ROUTE_OWNER} is the single route owner"
                    )
        if WORKFLOW_ROUTE_OWNER not in text:
            errors.append(
                f"workflows/{name} must route to {WORKFLOW_ROUTE_OWNER} "
                "instead of restating the next workflow"
            )
        for restatement in PIPELINE_RESTATEMENT_RE.finditer(text):
            errors.append(
                f"workflows/{name} must not restate the pipeline order or the next workflow: "
                f"{restatement.group(1)}"
            )
        # A closing block has to be findable by one name in every stage, otherwise a
        # reader (or a runner) cannot locate the completion criteria mechanically.
        gate_headings = COMPLETION_GATE_HEADING_RE.findall(text)
        if len(gate_headings) != 1:
            errors.append(
                f"workflows/{name} must carry exactly one `# Completion Gate` closing block, "
                f"found {len(gate_headings)}"
            )
        if LEGACY_STATUS_HEADING_RE.search(text):
            errors.append(
                f"workflows/{name} must name its state writeback `# Status Update`; "
                "`# State Update` is retired so the block stays retrievable"
            )
        # The next stage's workflow name belongs to the route owner; naming it here is a
        # second copy of the pipeline route and will drift.
        for reference in WORKFLOW_REF_RE.finditer(text):
            target = reference.group(1) + ".md"
            if target == name or target in AUXILIARY_WORKFLOWS:
                continue
            if MAIN_STATE_OF_WORKFLOW.get(target) != declared:
                errors.append(
                    f"workflows/{name} must not name another stage's workflow "
                    f"({target}); {WORKFLOW_ROUTE_OWNER} is the single route owner"
                )
        for motto in FINAL_PRINCIPLE_RE.finditer(text):
            measured = len(section_after(text, motto).encode("utf-8"))
            if measured > FINAL_PRINCIPLE_MAX_BYTES:
                errors.append(
                    f"workflows/{name} Final Principle must stay a one-line motto "
                    f"({measured} > {FINAL_PRINCIPLE_MAX_BYTES} bytes)"
                )
    for index in range(MAIN_STATE_COUNT):
        state = f"STATE-{index:02d}"
        if state not in covered:
            errors.append(f"main pipeline state {state} has no self-declaring workflow")
    return errors

READ_SCOPE_HEADING_RE = re.compile(r"^# Read Scope\s*$", re.M)
READ_SCOPE_BLOCK_END_RE = re.compile(r"^(?:---\s*$|#{1,6} )", re.M)
READ_SCOPE_SECTION_RE = re.compile(r"`(#{1,3}) ([^`\n]+?)`")

def _normalize_heading(text: str) -> str:
    return " ".join(text.split())

def check_read_scope_sections(root: Path) -> list[str]:
    """A `# Read Scope` block is an index: every section it names has to exist in that
    same file. Pointing at a section that no longer exists sends the reader nowhere —
    the same failure class as a dangling file reference, so it gets the same guard."""
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if relative.parts[0] in NON_SKILL_DIRS:
            continue
        text = path.read_text(encoding="utf-8-sig")
        match = READ_SCOPE_HEADING_RE.search(text)
        if not match:
            continue
        block = text[match.end():]
        end = READ_SCOPE_BLOCK_END_RE.search(block)
        if end:
            block = block[:end.start()]
        headings = {
            _normalize_heading(line) for line in text.splitlines() if line.startswith("#")
        }
        for level, name in READ_SCOPE_SECTION_RE.findall(block):
            target = _normalize_heading(f"{level} {name}")
            if target not in headings:
                errors.append(
                    f"Read Scope points at a missing section: {target} "
                    f"(in {relative.as_posix()})"
                )
    return errors

TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml"}

def check_line_endings(root: Path) -> list[str]:
    """Line endings carry no rule but they are billed, and a mixed file turns one
    edited line into a whole-file diff (measured: 30 real lines shown as 2,600).
    Both are pure loss, so the corpus stays LF-only."""
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if set(relative.parts) & NON_SKILL_DIRS:
            continue
        if b"\r" in path.read_bytes():
            errors.append(f"text file must use LF line endings: {relative.as_posix()}")
    return errors

BOM_PREFIXES = (
    (b"\xef\xbb\xbf", "UTF-8 BOM"),
    (b"\xff\xfe", "UTF-16 LE BOM"),
    (b"\xfe\xff", "UTF-16 BE BOM"),
)


def check_encoding_prefix(root: Path) -> list[str]:
    """Shipped text files stay BOM-less UTF-8.

    Every reader here uses `utf-8-sig`, so a BOM is semantically invisible -- which
    is exactly why it survives: no rule check, no reference check and no size
    check notices it, while it rewrites the first line of every diff and splits
    the corpus into two byte conventions. Measured case: a PowerShell round-trip
    of one file added `EF BB BF` while all 273 other shipped files stayed clean.
    """
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if set(relative.parts) & NON_SKILL_DIRS:
            continue
        head = path.read_bytes()[:3]
        for prefix, label in BOM_PREFIXES:
            if head.startswith(prefix):
                errors.append(f"text file must stay BOM-less UTF-8: {relative.as_posix()} ({label})")
                break
    return errors

def check_internal_references(root: Path) -> list[str]:
    """Reference Integrity Check: every skill-root path a document points at has to
    exist, otherwise the read path it describes is already broken.

    Declared reach (so the next maintainer knows what this does NOT cover): only
    references carrying a skill directory prefix -- `rules/…`, `knowledge/…` and
    the rest of `INTERNAL_PATH_REF_RE`. A **bare** file name (`foo.md`) is
    deliberately out of scope, because a bare name never means a shipped skill
    file: shipped references are always written with their directory. Bare names
    in these documents mean project-root artifacts
    (`shots/director_decision_notes.md`, `artifact_registry.md`), which exist only
    inside a project and cannot be verified from the skill root. Consequence: after
    deleting or renaming anything, grep the corpus for the name by hand -- a green
    validator does not prove there is no dangling reference.
    """
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if relative.parts[0] in NON_SKILL_DIRS:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for reference in sorted(set(INTERNAL_PATH_REF_RE.findall(text))):
            if not (root / reference).exists():
                errors.append(
                    f"dangling internal reference: {reference} (in {relative.as_posix()})"
                )
    return errors

BATCH_DELIVERY_OWNER = "rules/02_asset_rules.md"
BATCH_DELIVERY_SECTION = "### Asset Batch Delivery"
BATCH_DELIVERY_CONSUMERS = (
    "workflows/04_character_asset_workflow.md",
    "workflows/05_environment_asset_workflow.md",
    "workflows/06_prop_asset_workflow.md",
    "workflows/15_fx_asset_workflow.md",
    "templates/04_character_asset_prompt.md",
    "templates/05_environment_asset_prompt.md",
    "templates/06_prop_asset_prompt.md",
    "modules/assets.md",
)
BATCH_DELIVERY_NON_OWNERS = (
    "workflows/04_character_asset_workflow.md",
    "workflows/05_environment_asset_workflow.md",
    "workflows/06_prop_asset_workflow.md",
    "templates/04_character_asset_prompt.md",
    "templates/05_environment_asset_prompt.md",
    "templates/06_prop_asset_prompt.md",
    "modules/assets.md",
    "rules/automation_mode.md",
    "references/module_contracts_production.md",
)
CONFIRMATION_OWNER = "rules/progression_rules.md"
CONFIRMATION_SECTION = "### Exception-Based Batch Confirmation"
CONFIRMATION_NON_OWNERS = (
    "rules/02_asset_rules.md",
    "rules/automation_mode.md",
    "references/module_contracts_production.md",
    "templates/04_character_asset_prompt.md",
    "workflows/04_character_asset_workflow.md",
)


DELIVERY_MODE_OWNER = "modules/image-model-selection.md"
DELIVERY_MODE_SECTION = "## Image Delivery Mode"
DELIVERY_MODE_CONSUMERS = (
    ("modules/assets.md", "Image Delivery Mode"),
    ("rules/02_asset_rules.md", "Image Delivery Mode"),
    ("rules/automation_mode.md", "Image Delivery Mode"),
    ("references/project_state_contract.md", "Image Delivery Mode"),
    ("references/module_contracts_production.md", "Image Delivery Mode"),
    ("workflows/01_project_setup_workflow.md", "图像交付形态"),
    ("workflows/02_script_analysis_workflow.md", "图像交付形态"),
    ("workflows/04_character_asset_workflow.md", "Image Delivery Mode"),
    ("workflows/05_environment_asset_workflow.md", "DIRECT_IMAGE"),
    ("workflows/06_prop_asset_workflow.md", "DIRECT_IMAGE"),
    ("workflows/15_fx_asset_workflow.md", "Image Delivery Mode"),
    ("templates/00_project_start_template.md", "图像交付形态"),
    ("core/runtime-state.md", "IMAGE_DELIVERY_MODE"),
    ("USER_GUIDE.md", "DIRECT_IMAGE"),
)
DELIVERY_MODE_NON_OWNERS = (
    "rules/02_asset_rules.md",
    "modules/assets.md",
    "rules/automation_mode.md",
    "references/project_state_contract.md",
    "references/module_contracts_production.md",
    "workflows/01_project_setup_workflow.md",
    "USER_GUIDE.md",
)


def check_delivery_mode_ownership(root: Path) -> list[str]:
    """Image delivery mode is a project-level choice owned by one module and routed everywhere else."""
    errors: list[str] = []
    owner_text = read(root, DELIVERY_MODE_OWNER)
    if DELIVERY_MODE_SECTION not in owner_text:
        errors.append(f"{DELIVERY_MODE_OWNER} must own the {DELIVERY_MODE_SECTION} section")
    for relative, marker in DELIVERY_MODE_CONSUMERS:
        if marker not in read(root, relative):
            errors.append(f"image delivery mode must route to its owner: {relative}")
    for relative in DELIVERY_MODE_NON_OWNERS:
        if DELIVERY_MODE_SECTION in read(root, relative):
            errors.append(f"Image Delivery Mode must not be re-owned: {relative}")
    return errors


def check_batch_delivery_ownership(root: Path) -> list[str]:
    """Batch delivery has one owner for its definition and one for its confirmation semantics."""
    errors: list[str] = []
    if BATCH_DELIVERY_SECTION not in read(root, BATCH_DELIVERY_OWNER):
        errors.append(f"{BATCH_DELIVERY_OWNER} must own the {BATCH_DELIVERY_SECTION} section")
    for relative in BATCH_DELIVERY_CONSUMERS:
        if "Asset Batch Delivery" not in read(root, relative):
            errors.append(f"batch delivery must route to its owner: {relative}")
    for relative in BATCH_DELIVERY_NON_OWNERS:
        if BATCH_DELIVERY_SECTION in read(root, relative):
            errors.append(f"Asset Batch Delivery must not be re-owned: {relative}")
    if CONFIRMATION_SECTION not in read(root, CONFIRMATION_OWNER):
        errors.append(f"{CONFIRMATION_OWNER} must own the {CONFIRMATION_SECTION} section")
    for relative in CONFIRMATION_NON_OWNERS:
        if CONFIRMATION_SECTION in read(root, relative):
            errors.append(f"confirmation semantics must stay with their owner: {relative}")
    return errors


REFERENCE_OWNER_MARKERS = (
    ("references/asset_package.md", "## Package Timing And Delivery"),
    ("references/asset_package.md", "## Package Admission｜只收已认可的"),
    ("references/asset_package.md", "不作为入选证据"),
    ("references/asset_package.md", "不得事后补确认"),
    ("references/asset_package.md", "## Access Precondition"),
    ("references/asset_package.md", "未落盘不等于缺失"),
    ("references/asset_package.md", "确认效力不取决于该工件是否已被写成文件"),
    ("references/asset_package.md", "zip 是同一个包目录的压缩搬运形态"),
    ("references/asset_package.md", "## Non-Canonical Reference Naming"),
    ("references/asset_package.md", "## Design Material Naming"),
    ("references/asset_package.md", "`07_references/`"),
    ("references/asset_package.md", "`08_design/`"),
    ("references/asset_package.md", "系统内部参考材料"),
    ("references/asset_package.md", "归档位置不改变资格规则"),
    ("references/asset_package.md", "包是 Clip 表确认时点的快照"),
    ("references/asset_package.md", "STATE-08提示词撰写阶段新增的草图与尾帧不在失效条件之列"),
    ("USER_GUIDE.md", "07_references"),
    ("references/asset_package.md", "普通 Chat / Portable 模式"),
    ("references/asset_package.md", "## Asset Image Naming"),
    ("references/asset_package.md", "## Final Prompt Correspondence"),
    ("references/asset_package.md", "## Package Location And Source Rule"),
    ("references/asset_package.md", "## Optional Interoperable Tooling"),
    ("references/asset_package.md", "`_MANIFEST.md`"),
    ("references/asset_package.md", "清单必须一行一个文件，且可读可对应"),
    ("references/asset_package.md", "不得把同一Asset ID的多张Canonical图合并成一行"),
    ("references/asset_package.md", "View角色"),
    ("references/project_workspace.md", "要求交付生产交付包等同于要求保存或归档"),
)

PACKAGE_CONSUMERS = (
    ("config.md", "references/asset_package.md"),
    ("rules/02_asset_rules.md", "references/asset_package.md"),
    ("rules/completion_gate.md", "references/asset_package.md"),
    ("references/project_workspace.md", "references/asset_package.md"),
    ("references/module_contracts_production.md", "references/asset_package.md"),
    ("modules/assets.md", "references/asset_package.md"),
    ("workflows/11_video_generation_workflow.md", "references/asset_package.md"),
)

PACKAGE_NON_OWNERS = (
    "rules/02_asset_rules.md",
    "rules/completion_gate.md",
    "references/project_workspace.md",
    "references/module_contracts_production.md",
    "modules/assets.md",
    "workflows/11_video_generation_workflow.md",
)

PACKAGE_NAMING_SHAPE_RE = re.compile(r"<Asset ID>｜<Purpose>")


def check_reference_ownership(root: Path) -> list[str]:
    """Two distinct ownership guards for the production delivery package.

    1. The package's shape (naming form, package tree, correspondence rules)
       lives in exactly one file: `references/asset_package.md`. Everywhere
       else keeps a pointer, never a second copy of the shape.
    2. The single required reference file is reachable from the project
       runtime entrypoints, so it cannot become orphaned content.
    """
    errors: list[str] = []
    for relative, marker in REFERENCE_OWNER_MARKERS:
        if marker not in read(root, relative):
            errors.append(f"{relative} is missing the delivery package marker: {marker}")
    for relative, marker in PACKAGE_CONSUMERS:
        if marker not in read(root, relative):
            errors.append(f"delivery package must route to its owner: {relative}")
    for relative in PACKAGE_NON_OWNERS:
        text = read(root, relative)
        if PACKAGE_NAMING_SHAPE_RE.search(text):
            errors.append(f"asset image naming shape must stay with its owner: {relative}")
        if re.search(r"^#+ .*Production Delivery Package", text, re.M):
            errors.append(f"production delivery package section must stay with its owner: {relative}")
    return errors


STAGE_LANDING_OWNER = "knowledge/prompt_compilation/state08_projection.md"
STAGE_LANDING_MATRIX_START = "## Global Projection Matrix"
STAGE_LANDING_MATRIX_END = "## Serialization Rules"
STAGE_LANDING_MIN_ROWS = 12
STAGE_LANDING_SOURCES = tuple(f"STATE-{index:02d}" for index in range(8))
# A row may tag several stages in one compact run (`STATE-00/01/04`); expanding
# the run keeps the table readable without letting a stage hide behind a slash.
STAGE_LANDING_RUN_RE = re.compile(r"STATE-(\d\d(?:/\d\d)*)")
STAGE_LANDING_ROW_MARKERS = (
    "Writer Intent / Writer Beat / Setup-Payoff（STATE-01",
    "Director Intent / Director Decision Notes（STATE-00/01/04/05/06/07）",
    "Scene Breakdown / Scene Directing Brief（STATE-05）",
)


def check_stage_landing_coverage(root: Path) -> list[str]:
    """Every completed stage must name where its work lands in the final prompt.

    The projection owner's matrices are the only landing list: its
    `## Applicability Gate` requires each applicable module to leave evidence in
    a field the matrix names. A stage whose confirmed design appears in no row is
    therefore only *assumed* to reach the prompt through "downstream inherits
    it" -- which is how a locked design silently misses the output while every
    other check still passes (STATE-05's Scene Directing Brief was exactly that
    gap). Deterministic scope: the matrices exist, each main STATE-00..07 is
    named inside them, the row floor holds, and the Writer / Director / Scene
    source rows that carry intent and scene design are still present. Whether a
    given landing is semantically correct stays a human judgement -- this check
    never proves that a field's content is right.
    """
    errors: list[str] = []
    text = read(root, STAGE_LANDING_OWNER)
    start = text.find(STAGE_LANDING_MATRIX_START)
    if start == -1:
        errors.append(
            f"{STAGE_LANDING_OWNER} must own the {STAGE_LANDING_MATRIX_START} section"
        )
        return errors
    end = text.find(STAGE_LANDING_MATRIX_END, start)
    region = text[start:end] if end > start else text[start:]
    landing_states: set[str] = set()
    for run in STAGE_LANDING_RUN_RE.findall(region):
        for part in run.split("/"):
            landing_states.add(f"STATE-{part}")
    for state in STAGE_LANDING_SOURCES:
        if state not in landing_states:
            errors.append(
                f"{state} has no named landing row in the prompt projection matrices; "
                "a confirmed stage design must not rely on downstream inheritance"
            )
    rows = 0
    for line in region.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 3 or cells[0] in ("来源知识", "来源"):
            continue
        if all(set(cell) <= {"-"} for cell in cells if cell):
            continue
        rows += 1
    if rows < STAGE_LANDING_MIN_ROWS:
        errors.append(
            f"{STAGE_LANDING_OWNER} dropped below {STAGE_LANDING_MIN_ROWS} projection rows "
            f"({rows}); landing coverage may not be fixed by deleting rows"
        )
    for marker in STAGE_LANDING_ROW_MARKERS:
        if marker not in region:
            errors.append(f"{STAGE_LANDING_OWNER} is missing the stage landing row: {marker}")
    return errors


FAST_INVARIANT_MARKERS = (
    ("rules/automation_mode.md", "FAST只自动确认，不减少流程与产物"),
    ("rules/automation_mode.md", "不是阶段、检查或交付物本身"),
    ("rules/automation_mode.md", "用户可见交付清单也不因FAST而缩短"),
    ("rules/automation_mode.md", "合并的只是展示切片，不是阶段本身"),
    ("rules/automation_mode.md", "### Delivery Receipt｜交付收据"),
    ("rules/automation_mode.md", "`本轮完整输出`"),
    ("rules/automation_mode.md", "`已在Accepted Artifact`"),
    ("rules/automation_mode.md", "`待交付`"),
    ("rules/automation_mode.md", "收据只做交付核对"),
    ("rules/automation_mode.md", "生产交付包必须单列一行"),
    ("rules/automation_mode.md", "**不使用`已在Accepted Artifact`**"),
    ("rules/automation_mode.md", "最终Prompt交付轮的收据必须包含`Prompt纪律自检`条目"),
    ("rules/automation_mode.md", "不把自检升为Hard Gate"),
    ("USER_GUIDE.md", "`Prompt纪律自检`"),
    ("references/asset_package.md", "包必须在交付收据里**单列一行**"),
    ("rules/05_output_rules.md", "本清单与各件产物的完整性不因`Automation Policy: FAST`而改变"),
    ("rules/05_output_rules.md", "### Delivery Receipt｜交付收据"),
    ("references/project_state_contract.md", "仅有一句“已完成×××”声明不构成证据"),
    ("references/module_contracts_auxiliary.md", "自动接受的是确认，不是工件"),
    ("USER_GUIDE.md", "自动模式只是自动确认，不减少流程与产物"),
)


def check_fast_invariant_and_receipt(root: Path) -> list[str]:
    """FAST may only auto-confirm: the invariant and its receipt stay in every home.

    Measured failure this guards: a FAST project collapsed STATE-05/06/07 into one
    sentence (“已完成场景、镜头与执行规划”) and went straight to the prompt, so the
    missing artifacts were invisible. The rules already forbade it -- what was
    missing was one stated invariant plus a receipt that makes a missing artifact
    visible at delivery time, and both had to survive in several files at once.
    Deterministic scope: every sentence and receipt state label is present in the
    file that owns it. Whether a given delivery followed them stays a runtime
    judgement (R32-D / R32-E).
    """
    errors: list[str] = []
    for relative, marker in FAST_INVARIANT_MARKERS:
        if marker not in read(root, relative):
            errors.append(
                f"{relative} lost the FAST auto-confirm invariant or receipt text: {marker}"
            )
    return errors


# Standalone invocation is the easiest capability to over-read as "skip the
# pipeline". Every home must keep both halves -- "an independently run unit still
# meets its own Entry Gate" and "its output is a real artifact but is not counted
# as progress" -- because dropping the second half from any one file turns a
# single-stage run into a silently completed stage.
STANDALONE_INVOCATION_MARKERS = (
    ("rules/activation_rules.md", "## Standalone Invocation｜独立调用"),
    ("rules/activation_rules.md", "Standalone Module Invocation"),
    ("rules/activation_rules.md", "Standalone Stage Invocation"),
    ("rules/activation_rules.md", "不是顺序豁免"),
    ("rules/activation_rules.md", "**不计入项目进度**"),
    ("rules/activation_rules.md", "**产物不降级**"),
    ("rules/activation_rules.md", "**不扩张授权**"),
    ("rules/activation_rules.md", "不是`DRY RUN`"),
    ("workflows/workflow_map.md", "| 独立调用 |"),
    ("workflows/workflow_map.md", "`## Standalone Invocation｜独立调用`"),
    ("rules/progression_rules.md", "独立调用不是推进命令"),
    ("references/project_state_contract.md", "### Apply STANDALONE Invocation Writeback"),
    ("references/project_state_contract.md", "**不写入`Completed States`**"),
    ("SKILL.md", "独立调用"),
    ("USER_GUIDE.md", "只调用一个模块或一个阶段（独立调用）"),
    ("USER_GUIDE.md", "但不计入项目进度"),
)


# The 完整版专业分镜 path failed once in a way every check called healthy: the user
# asked for the complete 18-column record, the guarded artifact stayed the 5-column
# default, and the remaining batches arrived as a condensed summary table. "Complete"
# now means every Shot in one canonical file, and that is asserted mechanically
# instead of promised in prose.
FULL_SHOT_DELIVERY_MARKERS = (
    ("rules/05_output_rules.md", "### 完整版专业分镜 Delivery Gate"),
    ("rules/05_output_rules.md", "完整版的“完整”指**镜**，不是指**列**"),
    ("rules/05_output_rules.md", "05_shots/06_detailed_shot_design.md"),
    ("rules/05_output_rules.md", "--kind shot-design-full"),
    ("rules/05_output_rules.md", "不得用压缩摘要表代替任一镜的十八列"),
    ("templates/08_shot_design_prompt.md", "--kind shot-design-full"),
    ("templates/08_shot_design_prompt.md", "06_detailed_shot_design.md"),
)
FULL_SHOT_VALIDATOR_MARKERS = (
    "shot-design-full",
    "check_shot_design_full",
    "SHOT_FULL_FILE_NAMES",
    "完整版不完整",
)


# The asset canvas default is one rule with two category values, and every asset
# template and workflow routes to it. Before r97 the ratio lived only in an empty
# `画幅/分辨率/交付规格：` field, so "character 9:16 / everything else 16:9" had no
# single owner and could drift file by file.
ASSET_CANVAS_RATIO_OWNER = "rules/02_asset_rules.md"
ASSET_CANVAS_RATIO_SECTION = "## Asset Canvas Ratio Default｜资产图画幅默认"
ASSET_CANVAS_RATIO_ROUTE = "Asset Canvas Ratio Default｜资产图画幅默认"
ASSET_CANVAS_RATIO_OWNER_MARKERS = ("人物类`9:16`竖版", "其他类`16:9`横版")
ASSET_CANVAS_RATIO_ROUTED_FILES = (
    "templates/04_character_asset_prompt.md",
    "templates/05_environment_asset_prompt.md",
    "templates/06_prop_asset_prompt.md",
    "templates/13_fx_asset_prompt.md",
    "modules/assets.md",
    "workflows/04_character_asset_workflow.md",
    "workflows/05_environment_asset_workflow.md",
    "workflows/06_prop_asset_workflow.md",
)
ASSET_CANVAS_RATIO_CATEGORY_DEFAULTS = (
    ("templates/04_character_asset_prompt.md", "人物类`9:16`竖版", "人物类`16:9`"),
    ("templates/05_environment_asset_prompt.md", "其他类`16:9`横版", "其他类`9:16`"),
    ("templates/06_prop_asset_prompt.md", "其他类`16:9`横版", "其他类`9:16`"),
    ("templates/13_fx_asset_prompt.md", "其他类`16:9`横版", "其他类`9:16`"),
)
ASSET_CANVAS_RATIO_SYNTAX = (
    ("templates/14_midjourney_asset_prompt.md", "`--ar 9:16`"),
    ("templates/24_gpt_image_asset_prompt.md", "1152×2048"),
    ("adapters/gpt-image.md", "1152×2048"),
    ("USER_GUIDE.md", "9:16 竖版"),
    ("USER_GUIDE.md", "16:9 横版"),
)

REGRESSION_CORPUS = (
    "references/regression_scenarios.md",
    "references/regression_scenarios_craft.md",
    "references/regression_scenarios_prompt.md",
    "references/regression_scenarios_director.md",
    "references/regression_scenarios_system.md",
    "references/regression_scenarios_parameters.md",
    "references/regression_scenarios_maintenance.md",
    "references/regression_scenarios_delivery.md",
)
REGRESSION_ID_RE = re.compile(r"^## (R\d+[A-Z]?)\b", re.M)
REGRESSION_SUB_ID_RE = re.compile(r"^### (R\d+[A-Z]?-[A-Z0-9]+)\b", re.M)


def check_regression_ids(root: Path) -> list[str]:
    """One regression ID belongs to exactly one file in the corpus.

    Measured case: two new scenarios were appended to the maintenance file under
    R64/R65, which the craft file already owned. The corpus is addressed by ID
    ("see R48-M"), so a duplicate silently sends the reader to a different
    scenario, and every range line in the index stays plausible while it happens.

    Deterministic scope: top-level IDs and sub-IDs are each unique across the
    corpus, and every corpus file is listed in its index. It does not judge
    whether a scenario is well written, nor whether an ID's number matches the
    range its index row declares.
    """
    errors: list[str] = []
    texts: dict[str, str] = {}
    owners: dict[str, str] = {}
    sub_owners: dict[str, str] = {}
    for relative in REGRESSION_CORPUS:
        if not (root / relative).is_file():
            errors.append(f"regression corpus file is missing: {relative}")
            continue
        text = read(root, relative)
        texts[relative] = text
        for identifier in REGRESSION_ID_RE.findall(text):
            if identifier in owners:
                errors.append(
                    f"regression ID {identifier} is defined twice: "
                    f"{owners[identifier]} and {relative}"
                )
            else:
                owners[identifier] = relative
        for identifier in REGRESSION_SUB_ID_RE.findall(text):
            if identifier in sub_owners:
                errors.append(
                    f"regression sub-ID {identifier} is defined twice: "
                    f"{sub_owners[identifier]} and {relative}"
                )
            else:
                sub_owners[identifier] = relative
    index = texts.get(REGRESSION_CORPUS[0], "")
    for relative in REGRESSION_CORPUS[1:]:
        if Path(relative).name not in index:
            errors.append(f"{relative} is not listed in the regression file index")
    return errors


def check_standalone_invocation(root: Path) -> list[str]:
    """A standalone run produces a real artifact without counting as progress.

    Deterministic scope: each sentence is present in the file that owns it. The
    check does not judge whether a given run obeyed the contract -- that stays a
    runtime judgement, like the FAST invariant's.
    """
    errors: list[str] = []
    for relative, marker in STANDALONE_INVOCATION_MARKERS:
        if marker not in read(root, relative):
            errors.append(
                f"{relative} lost the standalone-invocation contract text: {marker}"
            )
    return errors


def check_full_shot_delivery_contract(root: Path) -> list[str]:
    """完整版专业分镜 is a file delivery, and "complete" means every Shot.

    Measured gap: the user asked for 完整版专业分镜; the guarded artifact stayed the
    5-column default, the eighteen-column rows existed only in chat and only for two
    batches, the rest arrived as a condensed summary table, and every existing check
    passed -- `--kind shot-design` accepts either form and never asks how many Shots
    the project has. Nothing in the skill said what makes a 完整版 complete.

    Deterministic scope: the delivery gate text stays in the rule that owns output
    form, the template routes to it and to the new validator kind, and the canonical
    file name plus the new kind still exist in the validator. It does not judge
    whether a given delivery honoured the gate.
    """
    errors: list[str] = []
    for relative, marker in FULL_SHOT_DELIVERY_MARKERS:
        if marker not in read(root, relative):
            errors.append(f"{relative} lost the 完整版分镜 delivery contract text: {marker}")
    validator = root / "scripts" / "validate_delivery_artifacts.py"
    if not validator.is_file():
        errors.append("complete-form delivery validator is missing: scripts/validate_delivery_artifacts.py")
        return errors
    source = validator.read_text(encoding="utf-8-sig")
    for marker in FULL_SHOT_VALIDATOR_MARKERS:
        if marker not in source:
            errors.append(f"validate_delivery_artifacts.py lost the complete-form gate: {marker}")
    return errors


def check_asset_canvas_ratio_default(root: Path) -> list[str]:
    """Asset images have one per-category canvas default and one owner for it.

    Measured gap: "人物资产图9:16、其他资产图16:9" existed only as an empty
    `画幅/分辨率/交付规格：` field, so the ratio was re-decided in every file (or
    silently dropped) with nothing to compare against.

    Deterministic scope: the owner section and both category defaults are present,
    every asset template / workflow routes to that section, each category template
    declares its own default and not the other category's, and the executable model
    forms (GPT Image pixel sizes, Midjourney `--ar`) stay in place. It does not
    judge what ratio a given generation actually produced, nor whether a user
    exception was honoured.
    """
    errors: list[str] = []
    owner_path = root / ASSET_CANVAS_RATIO_OWNER
    if not owner_path.is_file():
        errors.append(f"asset canvas ratio owner is missing: {ASSET_CANVAS_RATIO_OWNER}")
        return errors
    owner = read(root, ASSET_CANVAS_RATIO_OWNER)
    if ASSET_CANVAS_RATIO_SECTION not in owner:
        errors.append(
            f"{ASSET_CANVAS_RATIO_OWNER} must own the asset canvas default section: "
            f"{ASSET_CANVAS_RATIO_SECTION}"
        )
    for marker in ASSET_CANVAS_RATIO_OWNER_MARKERS:
        if marker not in owner:
            errors.append(
                f"{ASSET_CANVAS_RATIO_OWNER} lost the asset canvas default: {marker}"
            )
    for relative in ASSET_CANVAS_RATIO_ROUTED_FILES:
        if not (root / relative).is_file():
            continue
        if ASSET_CANVAS_RATIO_ROUTE not in read(root, relative):
            errors.append(f"{relative} must route to the asset canvas default owner")
    for relative, expected, contradictory in ASSET_CANVAS_RATIO_CATEGORY_DEFAULTS:
        if not (root / relative).is_file():
            continue
        text = read(root, relative)
        if expected not in text:
            errors.append(f"{relative} must declare its asset canvas default: {expected}")
        if contradictory in text:
            errors.append(
                f"{relative} declares the other category's asset canvas default: {contradictory}"
            )
    for relative, marker in ASSET_CANVAS_RATIO_SYNTAX:
        if not (root / relative).is_file():
            continue
        if marker not in read(root, relative):
            errors.append(f"{relative} lost the executable canvas syntax: {marker}")
    return errors


# The reference-film study route: one standalone analysis task whose measurement
# layer is a vendored third-party engine. Before this route existed, an agent asked
# to "learn how this video was shot" had a read order, a three-class evidence gate
# and a list of things not to read -- but nothing that produced shot boundaries or
# durations, so every timecode in the study was an eyeball estimate. The gap is
# closed by a workflow that owns the procedure and a knowledge section that owns
# the measurement discipline; several files have to keep pointing at them or the
# route silently reverts.
REFERENCE_FILM_WORKFLOW = "workflows/22_reference_film_study_workflow.md"
REFERENCE_FILM_TEMPLATE = "templates/26_reference_film_study_report.md"
REFERENCE_FILM_MEASUREMENT_OWNER = "knowledge/visual_styles/index.md"
REFERENCE_FILM_MEASUREMENT_SECTION = "#### Measured Boundary And Motion｜边界与运动量实测"
REFERENCE_FILM_VENDOR = "scripts/reference-film/vendor/README.md"
REFERENCE_FILM_ENGINE = "scripts/reference-film/vendor/video-shots/scripts/video-shots.mjs"
REFERENCE_FILM_COMPOSE_WIN = "scripts/reference-film/compose-win.mjs"
# Every consumer that has to keep routing to the measurement layer: the activation
# boundary, the read budget, the route owner, and the capability overview.
REFERENCE_FILM_ROUTED_FILES = (
    "rules/activation_rules.md",
    "rules/resource_loading.md",
    "workflows/workflow_map.md",
    "README.md",
)
# Vocabulary bridge: the engine's `size` enum is the same ladder the skill already
# owns in camera_language. If the bridge is dropped, an English enum key reaches a
# Chinese production term with nothing mapping between them.
REFERENCE_FILM_SIZE_BRIDGE = (
    ("`extreme-wide`", "大全景"),
    ("`wide`", "全景"),
    ("`medium`", "中景"),
    ("`medium-close`", "中近景"),
    ("`close`", "近景"),
    ("`extreme-close`", "大特写"),
    ("`none`", "不适用"),
)
# The one-way motion gate and the manual fallback are the two claims that make the
# measurement layer honest. Losing either turns "measured" back into "asserted".
REFERENCE_FILM_MEASUREMENT_MARKERS = (
    "`strong` 声称却实测接近 0 → 拦",
    "`still` 声称而实测偏高 → 不拦，只出提示",
    "纯人工拉片",
)
REFERENCE_FILM_WORKFLOW_MARKERS = (
    "shots.json",
    "track.json",
    "validate",
    "EF BB BF",
    "compose-win.mjs",
)
REFERENCE_FILM_TEMPLATE_SECTIONS = (
    "# Execution Condition｜执行条件",
    "# Shot Table｜逐镜表",
    "# Three-Layer Conclusion｜结论分层",
)


def check_reference_film_study(root: Path) -> list[str]:
    """The reference-film study route keeps its workflow, measurement owner and consumers.

    Deterministic scope: the workflow / template / measurement section / vendored
    provenance file all exist; the size-vocabulary bridge still maps the engine's
    enum onto the skill's canonical shot scale; the one-way motion gate, the manual
    fallback and the platform facts are still written down; and the activation rule,
    read budget, route owner and README still point at the route.

    It does NOT prove the engine runs, that a gate actually blocked anything, or
    that a study reported honest numbers -- those are runtime behaviour, covered by
    R87 and by the engine's own selftest.
    """
    errors: list[str] = []
    for relative in (REFERENCE_FILM_WORKFLOW, REFERENCE_FILM_TEMPLATE,
                     REFERENCE_FILM_VENDOR, REFERENCE_FILM_ENGINE,
                     REFERENCE_FILM_COMPOSE_WIN):
        if not (root / relative).is_file():
            errors.append(f"reference-film study route is missing a file: {relative}")
    if not (root / REFERENCE_FILM_MEASUREMENT_OWNER).is_file():
        errors.append(f"reference-film measurement owner is missing: {REFERENCE_FILM_MEASUREMENT_OWNER}")
        return errors

    measurement = read(root, REFERENCE_FILM_MEASUREMENT_OWNER)
    if REFERENCE_FILM_MEASUREMENT_SECTION not in measurement:
        errors.append(
            f"{REFERENCE_FILM_MEASUREMENT_OWNER} must own the measured-boundary section: "
            f"{REFERENCE_FILM_MEASUREMENT_SECTION}"
        )
    for marker in REFERENCE_FILM_MEASUREMENT_MARKERS:
        if marker not in measurement:
            errors.append(
                f"{REFERENCE_FILM_MEASUREMENT_OWNER} lost the measurement discipline: {marker}"
            )
    for enum_key, canonical in REFERENCE_FILM_SIZE_BRIDGE:
        if enum_key not in measurement or canonical not in measurement:
            errors.append(
                f"{REFERENCE_FILM_MEASUREMENT_OWNER} lost the shot-scale bridge: "
                f"{enum_key} -> {canonical}"
            )

    if (root / REFERENCE_FILM_WORKFLOW).is_file():
        workflow = read(root, REFERENCE_FILM_WORKFLOW)
        for marker in REFERENCE_FILM_WORKFLOW_MARKERS:
            if marker not in workflow:
                errors.append(f"{REFERENCE_FILM_WORKFLOW} lost a required step: {marker}")
    if (root / REFERENCE_FILM_TEMPLATE).is_file():
        template = read(root, REFERENCE_FILM_TEMPLATE)
        for heading in REFERENCE_FILM_TEMPLATE_SECTIONS:
            if heading not in template:
                errors.append(f"{REFERENCE_FILM_TEMPLATE} lost a report section: {heading}")

    for relative in REFERENCE_FILM_ROUTED_FILES:
        if not (root / relative).is_file():
            continue
        text = read(root, relative)
        if "22_reference_film_study_workflow.md" not in text:
            errors.append(
                f"{relative} must route to the reference-film study workflow; "
                f"{REFERENCE_FILM_WORKFLOW} is not discoverable from it"
            )
    return errors


def roster_section(text: str, heading: str) -> str:
    """The body of one `## heading` section.

    Registrations are read from the roster table only: a prose mention of the
    same path elsewhere in the owner file is a cross-reference, not a second
    registration. The heading is matched at line start, because these files also
    name their own sections inside the `# Read Scope` table at the top.
    """
    marker = "\n" + heading
    at = text.find(marker)
    if at == -1:
        if not text.startswith(heading):
            return ""
        start = len(heading)
    else:
        start = at + len(marker)
    end = text.find("\n## ", start)
    return text[start:] if end == -1 else text[start:end]


GENRE_INDEX = "knowledge/genre/index.md"
GENRE_DIR = "knowledge/genre"
GENRE_ROSTER_RE = re.compile(r"knowledge/genre/(\d{2}_[a-z_]+\.md)")
GENRE_SCHEMA_SECTIONS = (
    "## Genre Promise｜类型承诺",
    "## Information Discipline｜信息与悬念纪律",
    "## Camera Tendencies｜镜头倾向",
    "## Performance And Reaction｜表演与反应",
    "## Sound And Silence｜声音与留白",
    "## Rhythm And Cutting｜节奏与剪辑",
    "## Model Execution Notes｜模型执行提示",
    "## Pairs And Tensions｜组合与张力",
    "## When Not To Apply｜反公式边界与失败信号",
)
GENRE_INDEX_REQUIREMENTS = (
    ("## The Roster", "roster table"),
    ("## Loading Rule", "loading rule"),
    ("## Shared Genre File Schema", "shared schema"),
    ("## Anti-Formula Discipline｜反公式边界", "anti-formula discipline"),
    ("## Orthogonality", "orthogonality"),
    ("Genre Profile: PENDING", "pending discipline"),
    ("推定类型", "no genre inference"),
    ("禁止固定节拍模型", "no beat model"),
    ("禁止冲突公式", "no conflict formula"),
    ("禁止覆盖上游", "upstream intent wins"),
    ("与类型正交", "orthogonality statement"),
    ("禁止非剧情内配乐", "no non-diegetic score"),
    ("Story First", "shared invariant"),
    ("Canonical", "shared invariant"),
    ("Template字段", "no new template field"),
)
GENRE_ROUTING = (
    ("knowledge/00_knowledge_index.md", "## Persistent Genre Profile", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", GENRE_INDEX, "knowledge index discovery entry"),
    ("rules/resource_loading.md", f"`{GENRE_DIR}/`", "project scope gate row"),
    ("references/module_contracts_knowledge.md", "## Genre Profile Knowledge Contract", "module contract"),
    ("workflows/07_visual_development_workflow.md", GENRE_INDEX, "STATE-04 entry gate"),
)


def check_genre_knowledge(root: Path) -> list[str]:
    """The registered genre profiles must be routable, complete and anti-formula.

    Measured risk: this module only works if three set comparisons hold -- the
    roster and the directory agree, every profile file carries all nine shared
    sections, and the anti-formula discipline is still on the page. The third is
    the one that decays silently: R24-J forbids turning a genre into a beat
    model, and a profile that only lists "what this genre does" reads as a recipe
    even when the surrounding rules say otherwise.

    Deterministic scope: registration, section presence, route presence, and the
    fixed invariants. It does not judge whether a tendency is well chosen, nor
    whether a production actually followed it.
    """
    errors: list[str] = []
    if not (root / GENRE_INDEX).is_file():
        return [f"genre profile index is missing: {GENRE_INDEX}"]
    index = read(root, GENRE_INDEX)
    registered = GENRE_ROSTER_RE.findall(roster_section(index, "## The Roster"))
    present = sorted(
        path.name for path in (root / GENRE_DIR).glob("*.md") if path.name != "index.md"
    )
    if len(set(registered)) != len(registered):
        errors.append("the genre roster registers the same profile file twice")
    for name in sorted(set(registered)):
        if name not in present:
            errors.append(f"genre roster points at a missing profile file: {GENRE_DIR}/{name}")
    for name in present:
        if name not in registered:
            errors.append(f"genre profile file is not registered in the roster: {GENRE_DIR}/{name}")
        text = read(root, f"{GENRE_DIR}/{name}")
        for section in GENRE_SCHEMA_SECTIONS:
            if section not in text:
                errors.append(f"{GENRE_DIR}/{name} is missing the shared genre section: {section}")
        if "禁止非剧情内配乐" not in text:
            errors.append(
                f"{GENRE_DIR}/{name} must keep the rule that non-diegetic score never "
                "enters a video prompt"
            )
    for needle, label in GENRE_INDEX_REQUIREMENTS:
        if needle not in index:
            errors.append(f"{GENRE_INDEX} must keep the {label}: {needle}")
    for relative, needle, label in GENRE_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"genre profile routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the genre profile {label}: {needle}")
    return errors


ANIME_INDEX = "knowledge/anime_language/index.md"
ANIME_DIR = "knowledge/anime_language"
ANIME_ROSTER_RE = re.compile(r"knowledge/anime_language/(\d{2}_[a-z_]+\.md)")
ANIME_ATOM_SECTIONS = (
    "## Purpose And Owner",
    "## Executable Vocabulary｜可执行词汇",
    "## Conditions And Anti-Use｜成立条件与反用",
    "## Prompt Translation｜Prompt 转译",
    "## Failure Signals｜失败信号",
)
ANIME_INDEX_REQUIREMENTS = (
    ("## The Roster", "roster table"),
    ("## Loading Rule", "loading rule"),
    ("## Shared Atom Schema", "shared atom schema"),
    ("## Shared Invariants", "shared invariants"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("唯一owner", "single camera-language owner"),
    ("不是第二套路由", "not a second camera-language route"),
    ("焦段毫米数", "banned live-action quantities"),
    ("3d_animation", "explicit non-trigger"),
    ("新增任何字段", "no new prompt field"),
)
ANIME_ROUTING = (
    ("knowledge/00_knowledge_index.md", "## Persistent Drawn-Medium Language", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", ANIME_INDEX, "knowledge index discovery entry"),
    ("knowledge/camera_language/index.md", "## Medium Branch｜媒介分支", "camera-language medium branch"),
    ("knowledge/camera_language/index.md", ANIME_INDEX, "camera-language redirect"),
    ("knowledge/medium_profiles.md", ANIME_INDEX, "medium-profile equivalent owner"),
    ("rules/resource_loading.md", f"`{ANIME_DIR}/`", "project scope gate row"),
    ("references/module_contracts_knowledge.md", "## Drawn-Medium Language Knowledge Contract", "module contract"),
    ("workflows/07_visual_development_workflow.md", ANIME_INDEX, "STATE-04 entry gate"),
    ("workflows/09_shot_design_workflow.md", ANIME_INDEX, "STATE-06 resource list"),
    ("templates/04_character_asset_prompt.md", "#### 2D Character Asset Sheet Prompt｜设定集与画风锚\n", "2D asset structure heading"),
    ("templates/04_character_asset_prompt.md", "设定集QA", "2D asset QA branch"),
)


def check_anime_language(root: Path) -> list[str]:
    """The drawn-medium language must stay registered, complete and reachable.

    Measured risk: `2d_anime` was declared a first-class tier while the only
    "equivalent expressions" it pointed at were two table rows, and the template
    it named as the owner of the 2D asset form contained a negation instead of a
    structure. Both failure modes are silent -- the prompt still renders, it just
    renders live-action optics into a drawn medium.

    Deterministic scope: registration, five sections per atom, the index
    requirements, and the routing points that keep the redirect discoverable. It
    does not judge whether an equivalent expression is well chosen.
    """
    errors: list[str] = []
    if not (root / ANIME_INDEX).is_file():
        return [f"drawn-medium language index is missing: {ANIME_INDEX}"]
    index = read(root, ANIME_INDEX)
    registered = ANIME_ROSTER_RE.findall(roster_section(index, "## The Roster"))
    present = sorted(
        path.name for path in (root / ANIME_DIR).glob("*.md") if path.name != "index.md"
    )
    if len(set(registered)) != len(registered):
        errors.append("the drawn-medium roster registers the same atom twice")
    for name in sorted(set(registered)):
        if name not in present:
            errors.append(f"drawn-medium roster points at a missing atom: {ANIME_DIR}/{name}")
    for name in present:
        if name not in registered:
            errors.append(f"drawn-medium atom is not registered in the roster: {ANIME_DIR}/{name}")
        text = read(root, f"{ANIME_DIR}/{name}")
        for section in ANIME_ATOM_SECTIONS:
            if section not in text:
                errors.append(f"{ANIME_DIR}/{name} is missing the shared atom section: {section}")
        if "本档禁止写入" not in text:
            errors.append(
                f"{ANIME_DIR}/{name} must keep framing its equivalents as replacements "
                "for quantities this medium forbids"
            )
    for needle, label in ANIME_INDEX_REQUIREMENTS:
        if needle not in index:
            errors.append(f"{ANIME_INDEX} must keep the {label}: {needle}")
    for relative, needle, label in ANIME_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"drawn-medium routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the drawn-medium {label}: {needle}")
    return errors


VERTICAL_ATOM = "knowledge/camera_language/composition_language/vertical_framing.md"
VERTICAL_REQUIREMENTS = (
    ("## Purpose And Owner", "purpose and owner block"),
    ("交付画幅 ≠ 相机画幅", "delivery-versus-camera format distinction"),
    ("推定交付画幅", "no inferred delivery format"),
    ("过肩前后错位", "vertical two-shot layout"),
    ("不得裁切转换", "no crop conversion"),
    ("不虚构数值", "no invented platform numbers"),
)
VERTICAL_ROUTING = (
    ("knowledge/camera_language/composition_language/index.md", "- [Vertical Framing](vertical_framing.md)", "composition library entry"),
    ("knowledge/camera_language/index.md", "交付画幅与竖屏构图", "camera-language category list"),
    ("knowledge/00_knowledge_index.md", VERTICAL_ATOM, "knowledge index discovery entry"),
    ("rules/resource_loading.md", f"`{VERTICAL_ATOM}`", "project scope gate row"),
    ("workflows/09_shot_design_workflow.md", VERTICAL_ATOM, "STATE-06 resource list"),
    ("references/module_contracts_knowledge.md", f"`{VERTICAL_ATOM}`", "composition contract invariant"),
)


def check_vertical_framing(root: Path) -> list[str]:
    """The delivery aspect must stay owned, routable and non-inferable.

    Measured risk: 9:16 is a first-class delivery format (character assets
    default to it, the short-drama adapter targets it), yet nothing owned how a
    narrow frame changes composition -- and "项目已确认交付规格" was cited as an
    overriding authority in a dozen places without an owner. Left alone, a
    vertical project gets horizontal blocking inside a narrow frame, or a crop
    presented as delivery. The Prompt body no longer declares the format at all
    (`画幅：` was removed from every template as a platform parameter chosen at
    generation time), so this atom is now the only place the composition
    discipline lives.

    Deterministic scope: the atom exists, keeps its distinguishing clauses, and
    is registered and routed. It does not judge whether a vertical shot is well
    composed.
    """
    errors: list[str] = []
    if not (root / VERTICAL_ATOM).is_file():
        return [f"vertical framing atom is missing: {VERTICAL_ATOM}"]
    atom = read(root, VERTICAL_ATOM)
    for needle, label in VERTICAL_REQUIREMENTS:
        if needle not in atom:
            errors.append(f"{VERTICAL_ATOM} must keep the {label}: {needle}")
    for relative, needle, label in VERTICAL_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"vertical framing routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the vertical framing {label}: {needle}")
    return errors


DELIVERY_SPEC_SOURCE = "templates/01_project_bible_template.md"
DELIVERY_SPEC_REQUIREMENTS = (
    ("## Delivery Spec｜交付规格", "delivery spec section"),
    ("项目已确认交付规格", "the term it owns"),
    ("唯一记录位置与定义owner", "single-owner statement"),
    ("未确认时保持`UNSELECTED`", "unconfirmed state"),
    ("反推交付规格", "no inference from reference material"),
)
DELIVERY_SPEC_ROUTING = (
    ("rules/02_asset_rules.md", DELIVERY_SPEC_SOURCE, "asset canvas ratio route"),
    ("knowledge/camera_language/composition_language/vertical_framing.md", DELIVERY_SPEC_SOURCE, "vertical framing trigger route"),
    ("rules/resource_loading.md", "## Delivery Spec｜交付规格", "scope gate evidence"),
)


def check_delivery_spec(root: Path) -> list[str]:
    """`项目已确认交付规格` must have exactly one owner and one record.

    Measured case: a dozen adapters, templates and workflows let "用户当前明确
    例外或项目已确认交付规格优先" override their defaults, but nothing defined
    the term and no template recorded it -- so the override pointed at a fact the
    project could not hold. The defaults still worked, which is why it stayed
    invisible: the override branch was simply unreachable.

    Deterministic scope: the owning section exists, keeps its distinguishing
    clauses, and the main consumers route to it. It does not judge a delivery
    spec's content.
    """
    errors: list[str] = []
    if not (root / DELIVERY_SPEC_SOURCE).is_file():
        return [f"delivery spec owner file is missing: {DELIVERY_SPEC_SOURCE}"]
    owner = read(root, DELIVERY_SPEC_SOURCE)
    for needle, label in DELIVERY_SPEC_REQUIREMENTS:
        if needle not in owner:
            errors.append(f"{DELIVERY_SPEC_SOURCE} must keep the {label}: {needle}")
    for relative, needle, label in DELIVERY_SPEC_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"delivery spec consumer is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must route the {label} to {DELIVERY_SPEC_SOURCE}")
    return errors


PERIOD_INDEX = "knowledge/period_and_place/index.md"
PERIOD_DIR = "knowledge/period_and_place"
PERIOD_ROSTER_RE = re.compile(r"knowledge/period_and_place/(\d{2}_[a-z_]+\.md)")
PERIOD_ATOM_SECTIONS = (
    "## Purpose And Owner",
    "## Visible Constraints｜可见约束",
    "## Conditions And Anti-Use｜成立条件与反用",
    "## Uncertainty Marking｜不确定项标注",
    "## Failure Signals｜失败信号",
)
PERIOD_INDEX_REQUIREMENTS = (
    ("## The Roster", "roster table"),
    ("## Loading Rule", "loading rule"),
    ("## Evidence Discipline｜考据纪律", "evidence discipline"),
    ("## Shared Atom Schema", "shared atom schema"),
    ("## Shared Invariants", "shared invariants"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("Period And Place: PENDING", "pending discipline"),
    ("推定", "no inference of era or place"),
    ("一等禁项", "hard stop on real people, bodies and brands"),
    ("不得把常识当史实", "common sense is not history"),
    ("反刻板", "anti-stereotype discipline"),
    ("不新增Template字段", "no new template field"),
    ("knowledge/visual_styles/", "style-versus-fact boundary"),
)
PERIOD_ROUTING = (
    ("knowledge/00_knowledge_index.md", "## Persistent Period And Place", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", PERIOD_INDEX, "knowledge index discovery entry"),
    ("rules/resource_loading.md", f"`{PERIOD_DIR}/`", "project scope gate row"),
    ("references/module_contracts_knowledge.md", "## Period And Place Knowledge Contract", "module contract"),
    ("workflows/07_visual_development_workflow.md", PERIOD_INDEX, "STATE-04 entry gate"),
    ("templates/01_project_bible_template.md", PERIOD_INDEX, "World Building field pointer"),
)


def check_period_and_place(root: Path) -> list[str]:
    """Era and place must constrain visible facts without inventing them.

    Measured gap: `## Time Period` and `## Location System` were collected at
    STATE-00/01 and passed to five workflows, but no knowledge owned what they
    constrain -- so "时代背景" was a recorded fact with no judge, and the only
    era-related rules anywhere were style-layer prohibitions ("don't turn a
    director reference into a costume drama"), which answer a different question.

    Deterministic scope: registration, five sections per atom, the index
    requirements that keep evidence classes and the anti-stereotype rule alive,
    and the routing points. It does not judge whether a period detail is correct.
    """
    errors: list[str] = []
    if not (root / PERIOD_INDEX).is_file():
        return [f"period and place index is missing: {PERIOD_INDEX}"]
    index = read(root, PERIOD_INDEX)
    registered = PERIOD_ROSTER_RE.findall(roster_section(index, "## The Roster"))
    present = sorted(
        path.name for path in (root / PERIOD_DIR).glob("*.md") if path.name != "index.md"
    )
    if len(set(registered)) != len(registered):
        errors.append("the period and place roster registers the same atom twice")
    for name in sorted(set(registered)):
        if name not in present:
            errors.append(f"period and place roster points at a missing atom: {PERIOD_DIR}/{name}")
    for name in present:
        if name not in registered:
            errors.append(f"period and place atom is not registered in the roster: {PERIOD_DIR}/{name}")
        text = read(root, f"{PERIOD_DIR}/{name}")
        for section in PERIOD_ATOM_SECTIONS:
            if section not in text:
                errors.append(f"{PERIOD_DIR}/{name} is missing the shared atom section: {section}")
        if "不可确认" not in text:
            errors.append(
                f"{PERIOD_DIR}/{name} must keep the unverifiable-evidence class"
            )
    for needle, label in PERIOD_INDEX_REQUIREMENTS:
        if needle not in index:
            errors.append(f"{PERIOD_INDEX} must keep the {label}: {needle}")
    for relative, needle, label in PERIOD_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"period and place routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the period and place {label}: {needle}")
    return errors


BRANDED_INDEX = "knowledge/branded_content/index.md"
BRANDED_DIR = "knowledge/branded_content"
CLIENT_BRIEF_SECTION = "# Client Brief｜客户与商业 brief"
COMMERCIAL_FACT_GATE = "## Client Brief And Commercial Fact Gate｜客户与商业事实门"
BRANDED_ROSTER_RE = re.compile(r"knowledge/branded_content/(\d{2}_[a-z_]+\.md)")
BRANDED_ATOM_SECTIONS = (
    "## Purpose And Owner",
    "## Executable Vocabulary｜可执行词汇",
    "## Conditions And Anti-Use｜成立条件与反用",
    "## Commercial Fact Boundary｜商业事实边界",
    "## Failure Signals｜失败信号",
)
BRANDED_INDEX_REQUIREMENTS = (
    ("## The Roster", "roster table"),
    ("## Loading Rule", "loading rule"),
    ("## Shared Atom Schema", "shared atom schema"),
    ("## Commercial Fact Discipline｜商业事实纪律", "commercial fact discipline"),
    ("## Orthogonality", "orthogonality"),
    ("## Shared Invariants", "shared invariants"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("一等禁项", "hard stop on commercial facts"),
    ("不得推定", "no inference of commercial intent"),
    ("不新建节拍模型", "no second rhythm model"),
    ("不新增Template字段", "no new template field"),
    ("后期叠加", "post-production overlay route for text-accurate elements"),
    ("workflows/03_asset_discovery_workflow.md", "asset-side triage route"),
)
BRANDED_ROUTING = (
    ("knowledge/00_knowledge_index.md", "## Persistent Branded Content", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", BRANDED_INDEX, "knowledge index discovery entry"),
    ("rules/resource_loading.md", f"`{BRANDED_DIR}/`", "project scope gate row"),
    ("references/module_contracts_knowledge.md", "## Branded Content Knowledge Contract", "module contract"),
    ("knowledge/writer/script_adaptation.md", BRANDED_INDEX, "adaptation target route"),
    ("workflows/07_visual_development_workflow.md", BRANDED_INDEX, "STATE-04 entry gate"),
    ("templates/00_project_start_template.md", CLIENT_BRIEF_SECTION, "client brief intake section"),
)


def check_branded_content(root: Path) -> list[str]:
    """Brand work must translate the brief without inventing commercial facts.

    Measured gap: 品牌需求 is a first-class STATE-00 input and STATE-01 lists it for
    the Creation Brief branch, but every brand-related rule in the corpus was a
    *boundary* (asset triage, Hard Stop) -- nothing owned how a confirmed brand
    requirement becomes framing, product role and legibility. Meanwhile the
    short-drama adapter explicitly declared ads Not Applicable, so a brand brief
    had a target form with no owner at all.

    Deterministic scope: registration, five sections per atom, the index
    requirements that keep the fact discipline and the no-second-rhythm-model
    rule alive, and the routing points. It does not judge a creative treatment.
    """
    errors: list[str] = []
    if not (root / BRANDED_INDEX).is_file():
        return [f"branded content index is missing: {BRANDED_INDEX}"]
    index = read(root, BRANDED_INDEX)
    registered = BRANDED_ROSTER_RE.findall(roster_section(index, "## The Roster"))
    present = sorted(
        path.name for path in (root / BRANDED_DIR).glob("*.md") if path.name != "index.md"
    )
    if len(set(registered)) != len(registered):
        errors.append("the branded content roster registers the same atom twice")
    for name in sorted(set(registered)):
        if name not in present:
            errors.append(f"branded content roster points at a missing atom: {BRANDED_DIR}/{name}")
    for name in present:
        if name not in registered:
            errors.append(f"branded content atom is not registered in the roster: {BRANDED_DIR}/{name}")
        text = read(root, f"{BRANDED_DIR}/{name}")
        for section in BRANDED_ATOM_SECTIONS:
            if section not in text:
                errors.append(f"{BRANDED_DIR}/{name} is missing the shared atom section: {section}")
    for needle, label in BRANDED_INDEX_REQUIREMENTS:
        if needle not in index:
            errors.append(f"{BRANDED_INDEX} must keep the {label}: {needle}")
    for relative, needle, label in BRANDED_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"branded content routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the branded content {label}: {needle}")
    return errors


AUDIENCE_OWNER = "knowledge/audience_profiles.md"
AUDIENCE_REQUIREMENTS = (
    ("## Selection And Ownership", "profile selection and ownership"),
    ("## Suitability Layer", "suitability layer"),
    ("## Comprehension Layer", "comprehension layer"),
    ("## Performance And Sound Layer", "performance and sound layer"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("## Validator-Checkable Invariants", "validator-checkable invariants"),
    ("preschool", "preschool profile"),
    ("children_family", "children and family profile"),
    ("general", "general profile"),
    ("不得推定受众", "no audience inference"),
    ("可模仿性", "imitation-risk criterion"),
    ("外部事实", "external rating facts"),
    ("禁止非剧情内配乐", "no non-diegetic score"),
)
DOC_OWNER = "knowledge/adaptation/documentary_adapter.md"
PLATFORM_OWNER = "knowledge/platform_profiles.md"
PLATFORM_REQUIREMENTS = (
    ("## Purpose And Boundary", "purpose and boundary"),
    ("## Selection And Ownership", "profile field selection and ownership"),
    ("## Profile Fields｜平台剖面字段", "platform profile fields"),
    ("## Note Window Layer｜注意窗口", "note window layer"),
    ("## Completion And Series Layer｜完播与系列", "completion and series layer"),
    ("## Conversion Landing Layer｜转化落点", "conversion landing layer"),
    ("## Silent Playback And Packaging Layer｜静音与包装", "silent playback and packaging layer"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("## Validator-Checkable Invariants", "validator-checkable invariants"),
    ("不得推定平台", "no platform inference"),
    ("Platform Profile: PENDING", "pending platform profile"),
    ("外部事实", "platform facts are external"),
    ("不新建节拍模型", "no second rhythm model"),
    ("short_form_drama_adapter.md", "short-drama rhythm owner route"),
    ("禁止非剧情内配乐", "no non-diegetic score"),
)
DOC_REQUIREMENTS = (
    ("## Purpose And Trigger", "purpose and trigger"),
    ("## Hard Gates", "hard gates"),
    ("### 1. Source Reality Gate", "source reality gate"),
    ("## Claim-to-Source Ledger", "claim-to-source ledger"),
    ("## Generated-Image Provenance｜生成影像的来源标注", "generated-image provenance"),
    ("## Acceptance Checklist", "acceptance checklist"),
    ("不得被呈现为档案", "generated footage never poses as archive"),
    ("Hard Stop", "hard stop on real subjects"),
    ("禁止非剧情内配乐", "no non-diegetic score"),
)
SECONDARY_ROUTING = (
    ("knowledge/00_knowledge_index.md", "## Persistent Audience Profile", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", AUDIENCE_OWNER, "audience discovery entry"),
    ("knowledge/00_knowledge_index.md", DOC_OWNER, "documentary discovery entry"),
    ("knowledge/00_knowledge_index.md", "## Persistent Platform Profile", "knowledge index section"),
    ("knowledge/00_knowledge_index.md", PLATFORM_OWNER, "platform discovery entry"),
    ("knowledge/00_knowledge_index.md", "05_commercial_format.md", "commercial format discovery entry"),
    ("rules/resource_loading.md", f"`{AUDIENCE_OWNER}`", "audience scope gate row"),
    ("rules/resource_loading.md", f"`{DOC_OWNER}`", "documentary scope gate row"),
    ("rules/resource_loading.md", f"`{PLATFORM_OWNER}`", "platform scope gate row"),
    ("knowledge/writer/script_adaptation.md", DOC_OWNER, "adaptation target route"),
    ("knowledge/writer/screenplay_development.md", "Commercial Objective And Writer Beat", "writer commercial objective section"),
    ("references/module_contracts_knowledge.md", "## Audience Profile Knowledge Contract", "audience contract"),
    ("references/module_contracts_knowledge.md", "## Documentary And Non-Fiction Knowledge Contract", "documentary contract"),
    ("references/module_contracts_knowledge.md", "## Platform Profile Knowledge Contract", "platform contract"),
)


def check_audience_and_non_fiction(root: Path) -> list[str]:
    """Audience suitability, documentary discipline and platform profiles must keep their gates.

    Measured gap: 受众 was captured by STATE-01 but no knowledge owned what it
    changes, so suitability and comprehension were improvised per project; and
    纪实 had no owner at all -- the short-drama adapter declared it Not
    Applicable, which left non-fiction with a target form and no discipline for
    sources, reconstruction or generated footage passing as archive. 交付渠道
    had the same shape: the corpus repeatedly said platform facts must come from
    the user and refused to guess them, but nothing owned what an *already
    confirmed* platform changes about the note window, the ending obligation or
    the conversion landing -- so the only platform-shaped knowledge was the
    short-drama adapter's fixed 3s/30s gates.

    Deterministic scope: all three owner files exist and keep their
    distinguishing gates, and their routing is in place. It does not judge a
    treatment, and it does not encode any platform's mechanism -- encoding those
    would contradict the rule this check protects.
    """
    errors: list[str] = []
    for owner, requirements, label in (
        (AUDIENCE_OWNER, AUDIENCE_REQUIREMENTS, "audience profile"),
        (DOC_OWNER, DOC_REQUIREMENTS, "documentary adapter"),
        (PLATFORM_OWNER, PLATFORM_REQUIREMENTS, "platform profile"),
    ):
        if not (root / owner).is_file():
            errors.append(f"{label} owner file is missing: {owner}")
            continue
        text = read(root, owner)
        for needle, requirement in requirements:
            if needle not in text:
                errors.append(f"{owner} must keep the {requirement}: {needle}")
    for relative, needle, label in SECONDARY_ROUTING:
        if not (root / relative).is_file():
            errors.append(f"audience/documentary routing file is missing: {relative}")
            continue
        if needle not in read(root, relative):
            errors.append(f"{relative} must keep the {label}: {needle}")
    return errors


def check_self_check_dimension_count(user_guide: str) -> list[str]:
    """USER_GUIDE.md self-reports the number of maintenance check dimensions.

    Measured drift: the run card grew to 18 dimensions while USER_GUIDE.md still
    told readers to run 17, so a reader could finish the listed set and believe the
    self-check was complete. Deterministic scope: only the stated count, not which
    dimensions were actually run.
    """
    count = f"{len(SELF_CHECK_DIMENSIONS)}项"
    if count in user_guide:
        return []
    return [f"USER_GUIDE.md must state the current self-check dimension count: {count}"]


NO_PROJECT_REGISTRY_SOURCES = (
    "SKILL.md",
    "config.md",
    "index.md",
    "rules/state_source.md",
    "rules/chat_compatibility.md",
    "references/project_workspace.md",
    "workflows/01_project_setup_workflow.md",
)
# The removed capability and the wording that described it: a project index or
# registration table, the `init --registry` command that never existed, and the
# registry-named uniqueness claim. A tool may not grow a project repository back.
#
# The table patterns describe the *positive* claim only ("the registry holds /
# lives in / each entry contains ..."). The skill documents the removal itself
# ("本Skill不维护项目登记表：…"), and a pattern that also matched that sentence
# would fire on the very text that forbids it -- a guard that rejects its own
# counter-statement is worse than none.
NO_PROJECT_REGISTRY_PATTERNS = (
    ("project_registry", re.compile(r"project_registry")),
    ("`--registry` command", re.compile(r"--registry")),
    ("registry-held project ID", re.compile(r"Project ID\s*在\s*`?[^`\s]*registr", re.I)),
    ("registration table as the subject", re.compile(r"(登记表|注册表)\s*(?:只负责|负责|中)")),
    ("registry record fields", re.compile(r"每个登记项包含")),
)

REACHABILITY_ROOTS = ("SKILL.md", "config.md")
MAINTENANCE_MARKER = "Skill维护层"
# Declared exceptions: a file that is neither reachable nor a maintenance
# declaration, but whose exclusion is itself documented.
REACHABILITY_ALLOWED_UNREACHABLE = frozenset({"USER_GUIDE.md"})
REACHABILITY_TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml"}
REACHABILITY_INDEX_NAME_RE = re.compile(r"[A-Za-z0-9_\-./]+\.md")


def declares_maintenance(path: Path) -> bool:
    """A file that says of itself: read only when changing this skill."""
    return MAINTENANCE_MARKER in path.read_text(encoding="utf-8-sig")


def _reachable_files(root: Path, shipped: list[str]) -> set[str]:
    """Walk the read graph from the entry points.

    A path reference pulls in its target; an index file also publishes the bare
    names it lists. The walk passes through a maintenance declaration -- we know
    where it is, we just do not count it as evidence that *other* content is
    reachable from production.
    """
    known = set(shipped)
    reachable: set[str] = set()
    frontier = [rel for rel in REACHABILITY_ROOTS if rel in known]
    while frontier:
        current = frontier.pop()
        if current in reachable or current not in known:
            continue
        reachable.add(current)
        text = (root / current).read_text(encoding="utf-8-sig", errors="replace")
        found = set(INTERNAL_PATH_REF_RE.findall(text))
        if "index" in Path(current).name:
            base = Path(current).parent
            for name in REACHABILITY_INDEX_NAME_RE.findall(text):
                found.add((base / name).as_posix())
                found.add((Path("knowledge") / name).as_posix())
                found.add(name)
        for reference in found:
            reference = reference.lstrip("./")
            if reference in known and reference not in reachable:
                frontier.append(reference)
    return reachable


FRONTMATTER_BLOCK_RE = re.compile(
    r"\A---\r?\n(?P<body>.*?)(?:\r?\n)---[ \t]*(?:\r?\n|\Z)", re.DOTALL
)
FRONTMATTER_ENTRY_RE = re.compile(
    r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*):[ \t]+(?P<value>\S.*)$"
)

def quoted_scalar_end(value: str) -> int | None:
    """Index just past the closing quote of a quoted YAML scalar, or None.

    Double quotes end at the first unescaped `"`; single quotes end at the first
    `'` that is not part of a doubled `''`.
    """
    if value[:1] == "'":
        index = 1
        while index < len(value):
            if value[index] == "'":
                if value[index + 1:index + 2] == "'":
                    index += 2
                    continue
                return index + 1
            index += 1
        return None
    index = 1
    while index < len(value):
        if value[index] == "\\":
            index += 2
            continue
        if value[index] == '"':
            return index + 1
        index += 1
    return None

def check_skill_frontmatter(contents: str, relative: str = "SKILL.md") -> list[str]:
    """The discovery entry must survive a YAML parse, not just a substring search.

    Measured case: r95 rewrote `description` with straight quotes inside the
    already double-quoted scalar -- `（用户只说"学习这个视频怎么拍"也应激活）`.
    YAML ends the scalar at that first inner quote, the frontmatter stops
    parsing, and the host drops the skill from its list with nothing to read:
    the skill is simply gone. `name: sd-film` and all six aliases are still
    substrings of the file, so the alias, name and duplicate-entry checks all
    stayed green while the entry was unusable.

    Deterministic scope: the block opens and closes, every line is a top-level
    `key: value` entry, a quoted scalar closes exactly at the end of its line,
    and `name` / `description` are both present with `name: sd-film`. It is not
    a YAML parser and does not judge the values themselves.
    """
    block = FRONTMATTER_BLOCK_RE.match(contents)
    if block is None:
        return [f"{relative} must open with a closed --- frontmatter block"]
    errors: list[str] = []
    fields: dict[str, str] = {}
    malformed: set[str] = set()
    for number, raw_line in enumerate(block.group("body").split("\n"), start=2):
        line = raw_line.rstrip("\r")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        entry = FRONTMATTER_ENTRY_RE.match(line)
        if entry is None:
            errors.append(
                f"{relative} line {number} is not a `key: value` frontmatter entry, "
                f"so the discovery metadata cannot be parsed: {line.strip()!r}"
            )
            continue
        key = entry.group("key")
        value = entry.group("value").rstrip()
        if value[:1] in {'"', "'"}:
            end = quoted_scalar_end(value)
            if end is None or value[end:].strip():
                malformed.add(key)
                errors.append(
                    f"{relative} line {number} keeps text after the closing quote of "
                    f"{key}; YAML ends the scalar early and the host drops the skill "
                    f"silently: {value!r}"
                )
                continue
            fields[key] = value[1:end - 1]
        else:
            fields[key] = value
    if "name" not in malformed and fields.get("name") != "sd-film":
        errors.append(f"{relative} frontmatter must declare `name: sd-film`")
    if "description" not in malformed and not fields.get("description"):
        errors.append(f"{relative} frontmatter must declare a non-empty `description`")
    return errors

def check_reachability(root: Path) -> list[str]:
    """Every shipped file must be findable, or say why it is exempt.

    Reference Integrity catches a pointer to a missing file. This is the other
    half: content that exists but no read path can reach. Unread content is lost
    content, so it has to be either reachable or explicitly declared -- the
    maintenance layer declares itself, and everything else is a finding.
    """
    errors: list[str] = []
    shipped: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in REACHABILITY_TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if any(part in NON_SKILL_DIRS for part in relative.parts):
            continue
        if ".pre-" in path.name or "backup" in path.name.lower():
            continue
        shipped.append(relative.as_posix())
    reachable = _reachable_files(root, shipped)
    for relative in sorted(set(shipped) - reachable):
        if relative in REACHABILITY_ALLOWED_UNREACHABLE:
            continue
        if declares_maintenance(root / relative):
            continue
        errors.append(
            f"unreachable shipped file: {relative} has no read path; "
            f"route it, declare it {MAINTENANCE_MARKER}, or remove it"
        )
    return errors


def check_no_project_registry(root: Path) -> list[str]:
    """The skill is a tool, not a project repository: it holds no project index."""
    errors: list[str] = []
    for relative in NO_PROJECT_REGISTRY_SOURCES:
        text = read(root, relative)
        for label, pattern in NO_PROJECT_REGISTRY_PATTERNS:
            if pattern.search(text):
                errors.append(f"project registration must stay removed: {label} (in {relative})")
    return errors


CRAFT_OWNER = "knowledge/writer/screenplay_development.md"
CRAFT_MANUAL_SECTIONS = (
    "### 结构操作",
    "### 人物构建",
    "### 场景与对白技法",
)
CRAFT_ENTRY_RE = re.compile(r"^\*\*[^*]+\*\*$")
CRAFT_ENTRY_MARKERS = (
    ("成立条件：", "an applicability condition"),
    ("反用场景：", "a counter-indication"),
    ("失效信号：", "a failure signal"),
)
CRAFT_MIN_ENTRIES = 20
CRAFT_GATE_MARKERS = (
    ("变化可指认", "the identifiable-change item"),
    ("人物选择可追因", "the traceable-choice item"),
    ("场面不可随意互换", "the non-interchangeable-scene item"),
    ("台词具备行动", "the dialogue-as-action item"),
    ("结尾状态已改变", "the changed-end-state item"),
)
CRAFT_FORMULA_BOUNDARY = (
    ("## Craft And Formula｜工艺与公式", "boundary section"),
    ("Craft｜工艺", "craft row"),
    ("Formula｜公式", "formula row"),
    ("不延伸", "non-extension of the ban to the writer craft manual"),
)


def check_screenplay_craft(root: Path) -> list[str]:
    """The Writer craft layer must stay conditional, falsifiable and formula-free.

    Measured risk: this is the one knowledge domain that carries no mechanically
    checked invariant. Three properties have to hold together, and each one can
    decay silently:

    - `knowledge/writer/screenplay_development.md` carries a craft manual whose every
      entry declares 成立条件 / 反用场景 / 失效信号. An entry that loses its
      conditions reads as a recipe even when the surrounding prose denies it.
    - the manual still declares itself non-Gate, so it cannot silently become a
      hard gate or a duration requirement.
    - `knowledge/genre/index.md` still separates Craft from Formula after the
      ban on beat models, so the ban cannot be read as covering dramaturgy.

    Deterministic scope: section presence, per-entry marker parity, the
    non-Gate declaration, and the Craft/Formula boundary. It does not judge
    whether an entry's condition is well chosen or whether a scene obeyed it.
    """
    errors: list[str] = []
    if not (root / CRAFT_OWNER).is_file():
        return [f"writer craft owner is missing: {CRAFT_OWNER}"]
    owner = read(root, CRAFT_OWNER)
    manual = roster_section(owner, "## Craft Manual｜工艺手册")
    if not manual:
        errors.append(f"{CRAFT_OWNER} is missing the craft manual section")
    for heading in CRAFT_MANUAL_SECTIONS:
        if heading not in manual:
            errors.append(f"craft manual is missing section: {heading}")
    entries: list[list[str]] = []
    current: list[str] | None = None
    for line in manual.split("\n"):
        stripped = line.strip()
        if CRAFT_ENTRY_RE.match(stripped):
            current = [stripped]
            entries.append(current)
        elif stripped.startswith("###"):
            current = None
        elif current is not None:
            current.append(stripped)
    if len(entries) < CRAFT_MIN_ENTRIES:
        errors.append(
            "craft manual carries too few entries to be a manual: "
            f"{len(entries)} < {CRAFT_MIN_ENTRIES}"
        )
    for marker, label in CRAFT_ENTRY_MARKERS:
        missing = [
            index + 1
            for index, block in enumerate(entries)
            if not any(marker in line for line in block)
        ]
        if missing:
            errors.append(
                f"craft entries missing {label} ({marker.strip()}): "
                f"entries {missing[:5]} of {len(entries)}"
            )
    if "不是配方" not in manual or "不拥有Camera Language" not in manual:
        errors.append(
            "craft manual no longer declares itself a non-formula, "
            "non-camera owner: the recipe guard is gone"
        )
    gate = roster_section(owner, "## Directable Screenplay Gate｜可失败判定")
    if not gate:
        errors.append(f"{CRAFT_OWNER} is missing the fail-able screenplay gate")
    for marker, label in CRAFT_GATE_MARKERS:
        if marker not in gate:
            errors.append(f"fail-able screenplay gate is missing {label}: {marker}")
    boundaries = (
        ("不得成为Gate、硬门或时长要求", "craft manual is no longer forbidden to become a gate"),
        ("指不到即不得输出", "proposal may be emitted without the gate being locatable"),
        (COMMERCIAL_FACT_GATE, "the client brief and commercial fact gate is gone"),
        ("转化动作是Payoff，不是落版", "the conversion-as-payoff obligation is gone"),
        ("客户方终审人只决定客户侧由谁确认", "the approval-chain boundary is gone"),
    )
    for marker, message in boundaries:
        if marker not in owner:
            errors.append(message)
    triage = "workflows/03_asset_discovery_workflow.md"
    if not (root / triage).is_file():
        errors.append(f"commercial fact triage file is missing: {triage}")
    elif "**分类对象是客户已提供的商业事实**" not in read(root, triage):
        errors.append(
            f"{triage} no longer scopes the triage to client-provided facts: "
            "it would read as an intake mechanism it does not own"
        )
    genre_boundary = read(root, GENRE_INDEX)
    for marker, label in CRAFT_FORMULA_BOUNDARY:
        if marker not in genre_boundary:
            errors.append(f"Craft/Formula boundary is missing {label}: {marker}")
    return errors


WRITER_INDEX = "knowledge/writer/index.md"
WRITER_INDEX_REQUIREMENTS = (
    ("## Purpose And Boundary", "purpose and boundary"),
    ("## Module Contract", "module contract"),
    ("## The Roster", "roster table"),
    ("### Growth Boundary｜体量边界", "growth boundary"),
    ("## Requirement Router｜需求路由", "requirement router"),
    ("## Shared File Schema", "shared file schema"),
    ("## Validator-Checkable Invariants", "validator-checkable invariants"),
    ("## Non-Applicable Rule", "non-applicable rule"),
    ("## Return Routing", "return routing"),
    ("不创建主STATE", "no new main STATE"),
    ("不新增Template字段", "no new template field"),
    ("不新建节拍模型", "no second rhythm model"),
)
WRITER_LAYER_FILES = (
    "knowledge/writer/screenplay_development.md",
    "knowledge/writer/screenwriting_optimization.md",
    "knowledge/writer/script_adaptation.md",
    "knowledge/writer/directorial_interpretation.md",
    "knowledge/adaptation/short_form_drama_adapter.md",
)
# The short-form adapter predates the shared schema; these are its equivalents.
WRITER_FILE_SCHEMA_EQUIVALENTS = {
    "knowledge/adaptation/short_form_drama_adapter.md": (
        ("## Purpose And Trigger", "Read Scope / Module Contract equivalent"),
        ("## Acceptance Checklist", "Completion Check equivalent"),
    ),
}


def check_writer_layer(root: Path) -> list[str]:
    """The writer layer is a routed domain, not a pile of files.

    Measured risk: this layer is invoked once per brand and per brief, so its
    value is whether one call lands on the right rules. Three properties carry
    that, and each decays silently:

    - `knowledge/writer/index.md` exists and still routes a confirmed
      requirement to the exact file and section that must be read. Without it
      the only way in is reading the whole 45 KB owner and judging by hand.
    - every registered writer file keeps the shared schema (Read Scope, Module
      Contract, Completion Check, boundary statement), so an agent that is
      routed to a file can navigate inside it.
    - the router does not become a third load site for the short-form adapter,
      whose loader is fixed at two workflow steps.

    Deterministic scope: file presence, roster-to-file correspondence, section
    presence and the single-load-site rule. It does not judge whether a route is
    well chosen or whether a script honoured it.
    """
    errors: list[str] = []
    if not (root / WRITER_INDEX).is_file():
        return [f"writer layer index is missing: {WRITER_INDEX}"]
    index = read(root, WRITER_INDEX)
    for marker, label in WRITER_INDEX_REQUIREMENTS:
        if marker not in index:
            errors.append(f"{WRITER_INDEX} is missing the {label}: {marker}")
    registered = {path for path in WRITER_LAYER_FILES if path in index}
    for relative in WRITER_LAYER_FILES:
        if not (root / relative).is_file():
            errors.append(f"writer layer file is missing: {relative}")
            continue
        if relative not in index:
            errors.append(f"{relative} is not registered in {WRITER_INDEX}'s roster")
        if relative == "knowledge/adaptation/short_form_drama_adapter.md":
            continue
        text = read(root, relative)
        for marker, label in (
            ("# Read Scope", "read scope"),
            ("## Module Contract", "module contract"),
            ("## Completion Check", "completion check"),
        ):
            if marker not in text:
                errors.append(f"{relative} is missing its {label}: {marker}")
    if not registered:
        errors.append(f"{WRITER_INDEX}'s roster registers no writer layer file")
    for relative, equivalents in WRITER_FILE_SCHEMA_EQUIVALENTS.items():
        if not (root / relative).is_file():
            continue
        text = read(root, relative)
        for marker, label in equivalents:
            if marker not in text:
                errors.append(f"{relative} lost its {label}: {marker}")
    if "本文件是路由说明，**不是第三个加载入口**" not in index:
        errors.append(
            f"{WRITER_INDEX} no longer disclaims being a load site for the "
            "short-form adapter: the two-entry rule would read as three"
        )
    if "不得把\"有品牌\"等同于\"有客户\"" not in index:
        errors.append(
            f"{WRITER_INDEX} no longer separates commission context from brand "
            "intent: self-initiated branded work would read as commissioned"
        )
    if "不产生第二个确认主体" not in index:
        errors.append(
            f"{WRITER_INDEX} lost the single-confirmation-subject rule for "
            "self-initiated branded work"
        )
    growth = "### Growth Boundary｜体量边界"
    if growth not in index:
        errors.append(f"{WRITER_INDEX} is missing the growth boundary note: {growth}")
    else:
        owner_path = root / CRAFT_OWNER
        if owner_path.is_file():
            owner_bytes = owner_path.stat().st_size
            measured = re.search(
                r"(\d{2},\d{3})\s*B\s*=\s*复核线", roster_section(index, growth)
            )
            if owner_bytes > BUDGET_TARGET_BYTES and measured is None:
                errors.append(
                    f"{CRAFT_OWNER} is {owner_bytes} B, past the "
                    f"{BUDGET_TARGET_BYTES} B review line, but {WRITER_INDEX} carries no "
                    "dated slimming record: growth past the line is silent"
                )
    owner = read(root, CRAFT_OWNER)
    if "不得把\"有品牌\"等同于\"有客户\"" not in owner:
        errors.append(
            f"{CRAFT_OWNER} no longer separates commission context from brand "
            "intent in the commercial fact gate"
        )
    start_template = "templates/00_project_start_template.md"
    if not (root / start_template).is_file():
        errors.append(f"project start template is missing: {start_template}")
    else:
        template = read(root, start_template)
        for marker, label in (
            ("交付语境", "commission context field"),
            ("self_initiated", "self-initiated value"),
            ("client_commissioned", "client-commissioned value"),
            ("不产生第二个确认主体", "single-confirmation-subject rule"),
            ("制作建议｜待确认", "maker-proposed delivery spec route"),
            ("制作不得声称建议值\"符合\"任何未确认的平台机制", "platform-fact boundary"),
        ):
            if marker not in template:
                errors.append(
                    f"{start_template} client brief lost its {label}: {marker}"
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
    # Entry 体量只由 SKILL_ENTRY_MAX_BYTES / SKILL_ENTRY_MAX_LINES 约束，其唯一
    # owner 是 references/context_budget.md。此处曾硬编码 `> 8000`，比该 owner
    # 声明的 12 KB 更严，等于把 Entry 预算静默收紧三分之一：文档说还有余量，
    # 校验器却报错，维护者只能靠读脚本才能发现真正的门槛。
    for alias in ("调用sd", "调用SD", "用SD Film", "重新调用sd", "恢复旧项目", "继续之前的项目"):
        if alias not in skill:
            errors.append(f"SKILL.md is missing discovery alias: {alias}")
    for duplicate in duplicate_sd_film_entries(root):
        errors.append(
            f"duplicate SD Film discovery entry inside the canonical root: {duplicate}; "
            "remove or relocate staging copies"
        )
    errors.extend(check_skill_frontmatter(skill))
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
    gpt_image = read(root, "adapters/gpt-image.md")
    midjourney_template = read(root, "templates/14_midjourney_asset_prompt.md")
    gpt_image_template = read(root, "templates/24_gpt_image_asset_prompt.md")
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
    medium_profiles = read(root, "knowledge/medium_profiles.md")
    knowledge_index = read(root, "knowledge/00_knowledge_index.md")
    script_analysis = read(root, "workflows/02_script_analysis_workflow.md")
    contracts_knowledge = read(root, "references/module_contracts_knowledge.md")
    contracts_production = read(root, "references/module_contracts_production.md")
    shot_design = read(root, "workflows/09_shot_design_workflow.md")
    scene_breakdown = read(root, "workflows/08_scene_breakdown_workflow.md")
    scene_template = read(root, "templates/07_scene_design_prompt.md")
    shot_template = read(root, "templates/08_shot_design_prompt.md")
    sequence_planning = read(root, "workflows/16_sequence_planning_workflow.md")
    framing_scale = read(root, "knowledge/camera_language/lens_language/framing_and_scale.md")
    visual_workflow_r61 = read(root, "workflows/07_visual_development_workflow.md")
    look_frame_template = read(root, "templates/25_look_frame_prompt.md")
    output_rules = read(root, "rules/05_output_rules.md")
    prompt_rules = read(root, "rules/03_prompt_rules.md")
    contracts_framework = read(root, "references/module_contracts.md")
    aesthetic = read(root, "knowledge/quality/aesthetic_judgement.md")
    review_workflow = read(root, "workflows/13_review_workflow.md")
    review_template = read(root, "templates/16_review_report.md")
    budget_doc = read(root, "references/context_budget.md")
    required_markers = (
        (core, "STATE-01 Production Setup：Script锁定后一次确认项目图像模型默认项"),
        (runtime, "PROJECT_IMAGE_MODEL_DEFAULT"),
        (selection, "不输出`KEEP / ADAPT_SPLIT / RETURN`"),
        (selection, "Project Video Model Preference"),
        (selection, "Project Video Model Lock: PREFERENCE"),
        (selection, "`REQUIRED`：该Clip确实使用了所选模型的独占能力"),
        (selection, "## Cost Alternative Note"),
        (selection, "## Total Production Cost｜总生产成本"),
        (selection, "不得凭模型名称猜测重试率"),
        (selection, "待运行证据"),
        (selection, "Model Planning Envelope"),
        (selection, "不得读取尚未创建的 Clip 数据"),
        (selection, "Clip不是模型选择的前置输入，而是模型锁定后的产物"),
        (selection, "## Clip Adequacy Verification｜Clip适用性验证（STATE-07第三遍，不是模型选择）"),
        (selection, "`OVERQUALIFIED`不阻断交付"),
        (clip, "没有`Selected Model`、`Adapter Revision`与`Model Planning Envelope`时，**不得创建任何 Execution Clip**"),
        (clip, "第一遍｜Natural Unit（不套用任何时长切法）"),
        (clip, "第二遍｜模型适配（在已锁定 Envelope 内）"),
        (clip, "不得因为"),
        (clip, "而提前切碎完整动作链"),
        (clip, "第三遍｜逐Clip复核（Clip草案形成后）"),
        (clip, "Model Lock Revision"),
        (clip, "刻意交叉剪辑"),
        (selection, "不得填入任何数值或区间"),
        (selection, "预期成本 = 单次生成价格 × 预计尝试次数"),
        (selection, "## Mixed-Model Boundary"),
        (state, "Project Video Model Lock: PREFERENCE / HARD"),
        (image_selection, "Production Setup Proposal"),
        (project_setup, "Production Setup Gate"),
        (script_analysis, "## 07 Production Setup Gate"),
        (state, "Project Style Baseline"),
        (runtime, "PROJECT_STYLE_BASELINE"),
        (asset_rules, "同一轮内提交整批全部图片"),
        (character, "整批生成该批次全部外观参考图"),
        (project_start_template, "# Project Model Preferences"),
        (state, "Project Image Model Default"),
        (state, "Project Video Model Preference"),
        (state, "REF-SKETCH Submission Compatibility"),
        (clip, "STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner"),
        (clip, "长时能力利用审计｜Long-Duration Capability Utilization"),
        (clip, "必须评估合并"),
        (clip, "Duration Underutilized"),
        (clip, "Continuity Fragmentation"),
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
        (assets, "不得默认选择GPT Image、Midjourney或任何第三方服务"),
        (assets, "`GPT Image`：读取`adapters/gpt-image.md`"),
        (assets, "`Midjourney`：读取`adapters/midjourney.md`"),
        (assets, "明确指定其他图像模型"),
        (assets, "最小`CHANGE`与完整`PRESERVE`逻辑"),
        (image_selection, "## Available Choices"),
        (image_selection, "不得默认选择GPT Image、Midjourney或其他模型"),
        (image_selection, "下一步`、`下一个`、`继续`"),
        (image_selection, "Image Model Selection Scope"),
        (state, "Selected Image Model: GPT Image / Midjourney / UNSELECTED"),
        (gpt_image, "prompt_output_template: templates/24_gpt_image_asset_prompt.md"),
        (gpt_image_template, "## GPT Image Prompt Package"),
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
        (automation, "交付轮的终点就是Prompt本身"),
        (progression, "## Confirmation Input Semantics"),
        (progression, "任何语义上表示继续推进的表达"),
        (progression, "不提交外部服务"),
        (progression, "交付轮的终点是Prompt本身"),
        (prompt, "不追加外发授权往返"),
        (completion, "确认输入语义由`rules/progression_rules.md`唯一拥有"),
        (state, "Automation Policy: STANDARD / FAST"),
        (performance, "## Behavior Under Pressure"),
        (performance, "Spatial Blocking仍是位置、朝向、距离和接触的唯一owner"),
        (projection, "**Risk-driven Execution Locks**"),
        (shot_qa, "### Risk-driven Prompt Evidence"),
        (midjourney, "只输出可直接粘贴的 Midjourney Prompt"),
        (midjourney, "不调用`GPT Image`"),
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
        (gpt_image_template, "four-panel prop sheet"),
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
        (environment_reconstruction, "不得为每个View插入一次用户确认往返"),
        (environment_reconstruction, "无需等待用户先确认ENV-02"),
        (environment, "不逐View停顿等待确认"),
        (asset_rules, "View之间的累积输入不构成逐项用户确认，不得逐View停顿"),
        (environment_reconstruction, "最相关2–4张"),
        (environment_reconstruction, "`ENV-03` Lateral View"),
        (environment_reconstruction, "## Direction Anchor Contract｜方向锚点契约"),
        (environment_reconstruction, "约45°斜俯由默认必出项降为按需扩展"),
        (environment, "方向锚点"),
        (reference_budget, "`ENV-04`默认不进入画面参考位"),
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
        (medium_profiles, "## Screenwriter Layer"),
        (medium_profiles, "## Director Layer"),
        (medium_profiles, "## Aesthetic Layer"),
        (medium_profiles, "**`2d_anime` 禁止项**"),
        (medium_profiles, "媒介与Genre正交"),
        (medium_profiles, "`live_action`、`3d_animation`、`2d_anime`"),
        (project_setup, "# Medium Profile｜Internal"),
        (project_setup, "不得把它登记为已确认真人剧"),
        (project_setup, "本阶段不询问"),
        (project_setup, "不得穿过STATE-02资产发现与STATE-03的媒介相关资产生产"),
        (visual_workflow, "# Medium Profile Gate"),
        (visual_workflow, "不得写入焦段毫米数、光比比值或器材"),
        (visual_workflow, "不得在本阶段首次向用户提出媒介问题"),
        (script_analysis, "媒介剖面与目标形式是两根独立的轴"),
        (script_analysis, "媒介形式：`live_action`（真人 / 实拍）"),
        (script_analysis, "### Target Form Confirmation｜目标形式确认"),
        (script_analysis, "Project Information → 目标形式"),
        (script_analysis, "必须在本Proposal中询问一次"),
        (script_analysis, "媒介仍为`Pending`时不得进入STATE-02"),
        (runtime, "MEDIUM_PROFILE"),
        (state, "Medium Form: live_action / 3d_animation / 2d_anime / PENDING"),
        (asset_rules, "媒介前提"),
        (project_start_template, "# Medium Form"),
        (knowledge_index, "## Persistent Medium Profile"),
        (project_bible, "未确认写 `Pending`"),
        (contracts_knowledge, "## Medium Profile Knowledge Contract"),
        (contracts_knowledge, "确认与写入发生在STATE-01的`Production Setup Gate`"),
        (contracts_knowledge, "不得新增第四档或改名"),
        (budget_doc, "## Size Index"),
        (budget_doc, "目标是可达性，不是尺寸"),
        (budget_doc, "复核线不是配额"),
        (budget_doc, "## 可达性纪律"),
        (budget_doc, "无孤儿内容"),
        (budget_doc, "不在本纪律管辖内"),
        (framing_scale, "## Canonical Shot Scale"),
        (framing_scale, "中近景 / Medium Close-Up"),
        (framing_scale, "大特写 / Extreme Close-Up"),
        (shot_design, "景别选择必须读取`knowledge/camera_language/lens_language/framing_and_scale.md`"),
        (shot_design, "规范景别由`knowledge/camera_language/lens_language/framing_and_scale.md`唯一拥有"),
        (shot_design, "中近景。"),
        (shot_design, "大特写。"),
        (shot_design, "细节插入镜头。"),
        (contracts_knowledge, "## Shot Size And Framing Knowledge Contract"),
        (contracts_knowledge, "规范景别的唯一owner是`knowledge/camera_language/lens_language/framing_and_scale.md`"),
        (contracts_knowledge, "不维护平行景别清单"),
        (scene_breakdown, "## Scene Rhythm Intent Projection"),
        (scene_breakdown, "不在本阶段预定"),
        (scene_template, "Rhythm Intent（节奏结构"),
        (director_layer, "供条件性Sequence Planning与STATE-06消费"),
        (sequence_planning, "`templates/07_scene_design_prompt.md`的`Scene Directing Brief`"),
        (shot_template, "旁路而不是升级档"),
        (visual_workflow_r61, "# Look Frame Gate"),
        (visual_workflow_r61, "草案成形之后、正式锁定之前"),
        (visual_workflow_r61, "那不是决定，是赌注"),
        (visual_workflow_r61, "非生产视觉材料"),
        (visual_workflow_r61, "不得声称做过试片"),
        (look_frame_template, "非生产视觉材料"),
        (look_frame_template, "与 REF-SKETCH 的边界"),
        (look_frame_template, "不得进入 STATE-08【参考资产】"),
        (look_frame_template, "判断必须由用户给出"),
        (output_rules, "Look Frame试片帧"),
        (prompt_rules, "Look Frame试片帧"),
        (scorecard, "### Aesthetic Criteria｜两项审美维度的评分依据"),
        (scorecard, "唯一由`knowledge/quality/aesthetic_judgement.md`拥有；本文件只引用，不复制其正文"),
        (scorecard, "本评分仍不能替代人工审美判断"),
        (scorecard, "由STATE-04的`Look Frame`与STATE-09的用户Review承担"),
        (director_layer, "四维度从草案到锁定之间允许执行一次可选`Look Frame`"),
        (contracts_framework, "STATE-04的`Aesthetic Decision Lock`与其可选`Look Frame`由Director层拥有"),
        (aesthetic, "审美判据与判定纪律的唯一owner"),
        (aesthetic, "系统只输出观察，不输出审美结论"),
        (aesthetic, "六条全过不等于好看"),
        (aesthetic, "## 两个消费点（同一个owner，两个对象）"),
        (review_workflow, "## Aesthetic Judgement"),
        (review_workflow, "一致性检查问「有没有执行已确认的设定」，答对了也可能难看"),
        (review_workflow, "对照问句：Aesthetic Decision Lock里"),
        (review_workflow, "系统只输出观察，不输出审美结论"),
        (review_workflow, "未获得时记`PENDING_USER`"),
        (review_workflow, "返回STATE-04重做该维度，可选择性重跑Look Frame"),
        (review_template, "## Aesthetic Judgement（对照STATE-04 Aesthetic Decision Lock）"),
        (review_template, "系统不得代填本项"),
        (review_template, "审美不合格也按根因分流，**不新增Failure Class**"),
        (asset_rules, "### Asset Batch Delivery"),
        (asset_rules, "同一资产类别（CHAR / ENV / PROP / FX）"),
        (asset_rules, "不逐个资产停顿"),
        (progression, "### Exception-Based Batch Confirmation"),
        (progression, "不得以“用户没有提出异议”替代展示"),
        (character, "Asset Batch Delivery"),
        (environment, "Asset Batch Delivery"),
        (prop, "Asset Batch Delivery"),
        (fx, "Asset Batch Delivery"),
        (character_template, "### Asset Batch Envelope"),
        (environment_template, "### Asset Batch Envelope"),
        (prop_template, "### Asset Batch Envelope"),
        (assets, "批次是路由与交付的默认单位"),
        (contracts_production, "批次交付：STATE-03以批次为默认生产与确认单位"),
        (automation, "本节只拥有FAST下的聚合展示触发"),
        (image_selection, "## Image Delivery Mode"),
        (image_selection, "`AUTO`不是猜测"),
        (state, "Image Delivery Mode: AUTO / DIRECT_IMAGE / PROMPT_ONLY"),
        (runtime, "IMAGE_DELIVERY_MODE"),
        (project_start_template, "图像交付形态："),
        (script_analysis, "图像交付形态：`AUTO`"),
        (asset_rules, "`Image Delivery Mode: DIRECT_IMAGE`"),
        (automation, "由`modules/image-model-selection.md`拥有"),
        (assets, "Image Delivery Route"),
        (character, "Image Delivery Mode: DIRECT_IMAGE"),
        (environment, "DIRECT_IMAGE"),
        (prop, "DIRECT_IMAGE"),
        (fx, "Image Delivery Mode: DIRECT_IMAGE"),
        (user_guide, "DIRECT_IMAGE"),
        (user_guide, "PROMPT_ONLY"),
        (user_guide, "不维护项目登记表"),
        (asset_rules, "命名在该时点锁定，不得原地改名"),
        (asset_rules, "未绑定文件名的图片不得进入最终视频Prompt的参考条目"),
        (completion, "生产交付包由`references/asset_package.md`拥有"),
        (prompt, "## Package Timing And Delivery"),
        (prompt, "不得静默略过交付包"),
        (assets, "## Asset Naming And Delivery Package"),
        (scene_template, "scripts/validate_delivery_artifacts.py"),
        (shot_template, "scripts/validate_delivery_artifacts.py"),
        (plan, "scripts/validate_delivery_artifacts.py"),
        (contracts_production, "交付包：已确认生产物的分类打包"),
        (contracts_production, "每个Clip的`参考资产：`（或对应模型的参考字段）为每个实际投喂的视觉条目写出"),
    )
    for text, marker in required_markers:
        if marker not in text:
            errors.append(f"missing r49 routing marker: {marker}")
    errors.extend(check_batch_delivery_ownership(root))
    errors.extend(check_delivery_mode_ownership(root))
    for relative in ("modules/screenwriter.md", "modules/director.md", "modules/storyboard.md"):
        text = read(root, relative)
        if re.search(r"Seedance|Kling|Timeline|4.?15|4.?30", text, re.I):
            errors.append(f"upstream module contains model-specific rule: {relative}")
    for text, label in ((state, "state contract"), (plan, "clip template")):
        if "Model Compilation Template" in text or "Model Execution Lock Status" in text:
            errors.append(f"legacy compiler field remains active in {label}")
    if "Midjourney" in selection or "GPT Image" in selection:
        errors.append("video model selection must not own asset image routing")
    for relative in ("modules/screenwriter.md", "modules/director.md", "modules/storyboard.md"):
        text = read(root, relative)
        if re.search(r"Midjourney|GPT Image|image_gen", text, re.I):
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
    errors.extend(check_self_check_dimension_count(user_guide))
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
    entries = scan_markdown(root)
    errors.extend(check_context_budget(entries, ledger))
    errors.extend(check_read_entries(read_size_ledger_rows(root)))
    errors.extend(check_ledger_sizes(entries, read_ledger_sizes(root)))
    errors.extend(check_workflow_routing(root))
    errors.extend(check_reference_ownership(root))
    errors.extend(check_stage_landing_coverage(root))
    errors.extend(check_fast_invariant_and_receipt(root))
    errors.extend(check_standalone_invocation(root))
    errors.extend(check_full_shot_delivery_contract(root))
    errors.extend(check_asset_canvas_ratio_default(root))
    errors.extend(check_reference_film_study(root))
    errors.extend(check_genre_knowledge(root))
    errors.extend(check_screenplay_craft(root))
    errors.extend(check_writer_layer(root))
    errors.extend(check_anime_language(root))
    errors.extend(check_vertical_framing(root))
    errors.extend(check_delivery_spec(root))
    errors.extend(check_period_and_place(root))
    errors.extend(check_branded_content(root))
    errors.extend(check_audience_and_non_fiction(root))
    errors.extend(check_regression_ids(root))
    errors.extend(check_no_project_registry(root))
    errors.extend(check_reachability(root))
    errors.extend(check_internal_references(root))
    errors.extend(check_read_scope_sections(root))
    errors.extend(check_line_endings(root))
    errors.extend(check_encoding_prefix(root))
    return errors

def _png_dimensions(path: Path) -> tuple[int, int] | None:
    """(width, height) out of a PNG IHDR chunk, or None when it is not a readable PNG."""
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
    except OSError:
        return None
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return (int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big"))


def _sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


SKETCH_REQUIRED_FIELDS = (
    "schema_version", "clip_id", "assessment", "route", "generator_template",
    "sketch_type", "master_input_mode", "image_path",
    "blocking_signature", "layout",
)
# `master_asset_path` is required only when the run actually consumed the master. A
# rebound record (`NONE_REBIND`) is a derived record and must NOT claim a master input,
# so requiring the field unconditionally would reject the honest form and force a false
# `VISUAL_REFERENCE` claim instead.
SKETCH_LAYOUT_KEYS = (
    "main_blocking_panel", "character_role_labels",
    "direction_gaze_movement_annotation", "spatial_top_down_diagram",
    "camera_information", "blocking_movement_notes_or_permission",
    "usage_authority_note",
)
SKETCH_SKETCH_TYPES = ("S", "P", "A", "S+P", "S+A", "P+A", "S+P+A", "Combined")
SKETCH_FORBIDDEN_TRUE = (
    "artistic_storyboard_drift", "template_content_leakage",
    "character_appearance_leakage",
)


def validate_sketch_evidence(evidence_path: Path, skill_root: Path | None = None) -> tuple[list[str], list[str]]:
    """Deterministic assertions for a REF-SKETCH candidate's evidence record.

    Owner of the evidence schema is `templates/23_visual_blocking_sketch_prompt.md`;
    this function only checks what can be decided without looking at the picture:
    field presence and vocabulary, self-consistency between assessment / route /
    registration status, the layout blocks the template requires, the forbidden
    drift and contamination flags, and — when the registration record and the
    bitmap are next to the evidence file — the registered SHA-256 and pixel
    dimensions. Judging whether the mannequins really are neutral, whether the
    blocking really matches, and whether the sheet reads as a technical diagram
    stays a mandatory human visual inspection.
    """
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = json.loads(evidence_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as exc:
        return [f"草图证据不可读: {exc}"], warnings
    except json.JSONDecodeError as exc:
        return [f"草图证据不是合法JSON: {exc}"], warnings
    if not isinstance(data, dict):
        return ["草图证据必须是JSON对象（templates/23 的 Candidate Evidence Record）"], warnings

    for field in SKETCH_REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"草图证据缺少字段: {field}")

    if data.get("schema_version") != 1:
        errors.append(f"schema_version 必须为 1，当前为 {data.get('schema_version')!r}")

    clip_id = data.get("clip_id")
    if not isinstance(clip_id, str) or not re.fullmatch(r"CLIP-\d+", clip_id):
        errors.append(f"clip_id 必须是正式 CLIP-xxx: {clip_id!r}")

    assessment = data.get("assessment")
    route = data.get("route")
    registration = data.get("registration_status")
    if assessment not in ("REQUIRED", "NONE"):
        errors.append(f"assessment 只允许 REQUIRED / NONE: {assessment!r}")
    if assessment == "NONE":
        if route != "NONE" or registration != "NONE":
            errors.append("assessment=NONE 时必须 route=NONE 且 registration_status=NONE")
    elif assessment == "REQUIRED":
        if route != "TECHNICAL_VISUAL_BLOCKING_SKETCH":
            errors.append(
                "assessment=REQUIRED 时 route 必须是 TECHNICAL_VISUAL_BLOCKING_SKETCH，"
                f"当前为 {route!r}"
            )
        if registration not in ("CONFIRMED", "PENDING"):
            errors.append(
                f"assessment=REQUIRED 时 registration_status 只允许 CONFIRMED / PENDING: {registration!r}"
            )

    if data.get("generator_template") != "templates/23_visual_blocking_sketch_prompt.md":
        errors.append(
            "generator_template 必须指向 templates/23_visual_blocking_sketch_prompt.md，"
            f"当前为 {data.get('generator_template')!r}；草图不得由Storyboard模板生成"
        )

    sketch_type = data.get("sketch_type")
    if sketch_type not in SKETCH_SKETCH_TYPES:
        errors.append(f"sketch_type 不在允许集合内: {sketch_type!r}")

    signature = data.get("blocking_signature")
    if not isinstance(signature, str) or not signature.strip():
        errors.append("blocking_signature 不得为空：草图必须绑定当前Clip的Blocking Signature")

    layout = data.get("layout")
    if isinstance(layout, dict):
        for key in SKETCH_LAYOUT_KEYS:
            if layout.get(key) is not True:
                errors.append(f"layout.{key} 必须为 true：技术调度表缺少该必需区域")
    else:
        errors.append("layout 必须是对象，并逐项声明模板要求的区域")

    for flag in SKETCH_FORBIDDEN_TRUE:
        if data.get(flag) is not False:
            errors.append(f"{flag} 必须为 false：该项为 true 时草图固定 FAIL，不得注册")

    if data.get("neutral_mannequin_representation") is not True:
        errors.append("neutral_mannequin_representation 必须为 true：人物必须是无性别技术调度人偶")
    if data.get("blocking_match") is not True:
        errors.append("blocking_match 必须为 true：草图与当前Blocking Signature不一致时不得注册")

    master_mode = data.get("master_input_mode")
    master_path = data.get("master_asset_path")
    if master_mode in ("VISUAL_REFERENCE", "TEXT_CONTRACT_FALLBACK"):
        if not isinstance(master_path, str) or not master_path.strip():
            errors.append(f"master_input_mode={master_mode} 时必须记录实际母版路径")
            master_path = ""
    if master_mode == "VISUAL_REFERENCE":
        if isinstance(master_path, str) and master_path.strip():
            # `references/ref_sketch_master.md` owns this path and resolves it from the
            # SKILL root, never from the current working directory: a plain
            # `Path(master_path).is_file()` would pass whenever the validator happens to
            # be run from the skill root, which is exactly the claim being checked.
            candidates: list[Path] = []
            if skill_root is not None:
                candidates.append(skill_root / master_path)
            candidates.append(evidence_path.parent / master_path)
            if not any(candidate.is_file() for candidate in candidates):
                errors.append(
                    f"master_input_mode=VISUAL_REFERENCE 但母版文件不可读: {master_path}；"
                    "应改记 TEXT_CONTRACT_FALLBACK 并写明失败来源"
                )
    elif master_mode == "TEXT_CONTRACT_FALLBACK":
        warnings.append("母版走TEXT_CONTRACT_FALLBACK：最终交付不得声称使用了视觉母版")
    elif master_mode == "NONE_REBIND":
        # A rebound sketch is a derived record: the bitmap already exists and was confirmed
        # under its old Clip, so it never consumed the sketch master. Claiming
        # VISUAL_REFERENCE here would be a false claim; what it must prove instead is that it
        # came from a real source record, unchanged. The hash chains are checked below, after
        # the bitmap itself has been resolved.
        source = data.get("source_reference")
        if not (isinstance(source, str) and source.strip()):
            warnings.append("master_input_mode=NONE_REBIND 但未写 source_reference，源记录未经核验")
    else:
        errors.append(
            "master_input_mode 只允许 VISUAL_REFERENCE / TEXT_CONTRACT_FALLBACK / NONE_REBIND: "
            f"{master_mode!r}"
        )

    image_path = data.get("image_path")
    image_file: Path | None = None
    if not isinstance(image_path, str) or not image_path.strip():
        errors.append("image_path 不得为空：REQUIRED候选必须有真实可读图片")
    else:
        candidate = Path(image_path)
        if candidate.is_absolute() or ".." in candidate.parts:
            errors.append(f"image_path 必须是项目内相对路径: {image_path}")
        else:
            for base in (evidence_path.parent, Path.cwd()):
                if (base / candidate).is_file():
                    image_file = base / candidate
                    break
            if candidate.suffix.lower() != ".png":
                errors.append(f"草图必须是PNG: {image_path}")
            if image_file is None:
                errors.append(f"草图文件不存在或不可读: {image_path}")

    if master_mode == "NONE_REBIND":
        # Two chains must both hold: rebind record <- source record, and
        # rebind record <- the actual bitmap. Checking only the source record would let an
        # edit of both files swap the picture unnoticed; checking only the bitmap would let
        # the source provenance drift.
        source = data.get("source_reference")
        source_sha = ""
        if isinstance(source, str) and source.strip():
            source_file = evidence_path.parent / f"{source}_evidence.json"
            if source_file.is_file():
                try:
                    source_data = json.loads(source_file.read_text(encoding="utf-8-sig"))
                    source_sha = str(source_data.get("sha256", "")).upper()
                except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                    warnings.append(f"重绑定源记录不可读（{source_file.name}）：{exc}")
            else:
                warnings.append(f"重绑定源记录不存在：{source_file.name}，母版输入未经核验")
        own_sha = str(data.get("sha256", "")).upper()
        captured = str(data.get("source_sha256", "")).upper()
        if captured:
            if source_sha and captured != source_sha:
                errors.append(
                    "重绑定记录捕获的源哈希与源记录不一致（重绑定记录 ← 源记录 链断）: "
                    f"捕获 {captured} / 源记录 {source_sha}"
                )
            if own_sha and captured != own_sha:
                errors.append(
                    "重绑定记录自身声明的哈希与其捕获的源哈希不一致: "
                    f"捕获 {captured} / 本记录 {own_sha}"
                )
            if image_file is not None:
                actual = _sha256_of(image_file)
                if actual != captured:
                    errors.append(
                        "重绑定位图与其捕获的源哈希不一致（位图已被替换）: "
                        f"捕获 {captured} / 实际 {actual}"
                    )
        else:
            warnings.append(
                "master_input_mode=NONE_REBIND 但未写 source_sha256：位图是否与源记录一致未经核验"
            )
        if source_sha and own_sha and source_sha != own_sha:
            errors.append(
                "重绑定必须与源记录指向同一份位图: "
                f"源 {source_sha} / 本记录 {own_sha}"
            )

    registration_path = evidence_path.parent / (
        evidence_path.name.replace("_evidence.json", "_registration.md")
    )
    if registration_path.is_file() and image_file is not None:
        record = registration_path.read_text(encoding="utf-8-sig")
        sha_match = re.search(r"SHA256[^\n]*?([0-9A-Fa-f]{64})", record)
        if sha_match:
            actual = _sha256_of(image_file)
            if actual != sha_match.group(1).upper():
                errors.append(
                    "草图SHA-256与登记记录不一致: "
                    f"登记 {sha_match.group(1).upper()} / 实际 {actual}"
                )
        else:
            warnings.append("登记记录没有SHA256，图片完整性未经确定性核验")
        dim_match = re.search(r"Dimensions[^\n]*?(\d+)\s*[×x]\s*(\d+)", record)
        if dim_match:
            actual_dims = _png_dimensions(image_file)
            if actual_dims is None:
                warnings.append("无法解析PNG尺寸，尺寸登记未经确定性核验")
            elif actual_dims != (int(dim_match.group(1)), int(dim_match.group(2))):
                errors.append(
                    "草图尺寸与登记记录不一致: "
                    f"登记 {dim_match.group(1)}×{dim_match.group(2)} / 实际 {actual_dims[0]}×{actual_dims[1]}"
                )
        else:
            warnings.append("登记记录没有Dimensions，尺寸登记未经确定性核验")
    elif not registration_path.is_file():
        warnings.append(f"未找到登记记录 {registration_path.name}，图片完整性与注册状态未经核验")

    warnings.append(
        "射程：本命令不判断人偶是否真的中性、Blocking是否真的匹配、画面是否为技术调度表——"
        "那三项仍须人工视觉检查"
    )
    return errors, warnings


def run_sketch_validation(evidence_path: Path, skill_root: Path | None = None) -> int:
    errors, warnings = validate_sketch_evidence(evidence_path, skill_root)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 草图证据通过确定性校验（人工视觉检查仍不可省略）")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--skill-root", type=Path, default=Path.cwd(),
        help="skill root for the default full validation (default: current directory); "
             "the `sketch` subcommand validates a project-side evidence file and ignores it",
    )
    parser.add_argument("--skill-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--report", action="store_true",
        help="also print the periodic size and readability audit (sizes, index, reviews)",
    )
    subparsers = parser.add_subparsers(dest="command")
    sketch = subparsers.add_parser(
        "sketch", parents=[common],
        help="validate a REF-SKETCH Candidate Evidence Record (templates/23)",
    )
    sketch.add_argument("evidence", type=Path)
    sketch.add_argument(
        "--report", action="store_true",
        help="accepted for command-form symmetry; the sketch check has no size report",
    )
    args = parser.parse_args()
    if args.command == "sketch":
        return run_sketch_validation(args.evidence, args.skill_root)
    errors = validate_skill(args.skill_root)
    if args.report:
        print(build_report(args.skill_root))
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: structural, routing, readability and landing-coverage validation")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
