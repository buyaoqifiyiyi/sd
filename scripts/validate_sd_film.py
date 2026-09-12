#!/usr/bin/env python3
"""Deterministic r82 structural, routing and readability validation for SD Film."""
# Skill维护层：只在修改本Skill时读取，不参与影视生产。
from __future__ import annotations

import argparse
import re
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
    "references/context_budget.md",
    "references/asset_package.md",
    "references/maintenance_self_check.md",
    "references/maintenance_self_check_protocol.md",
    "references/regression_scenarios.md",
    "references/regression_scenarios_craft.md",
    "references/regression_scenarios_system.md",
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
NON_SKILL_DIRS = {".git", ".workbuddy", "tmp", "__pycache__", ".venv", "node_modules"}

SELF_CHECK_DIMENSIONS = (
    "Duplicate Rule Check", "Conflict Check", "Terminology Drift Check", "Rule Ownership Check",
    "Prompt Pollution Check", "Routing Integrity Check", "Template Consistency Check",
    "Reference Integrity Check", "State / Continuity Compatibility Check", "User Guide Sync Check",
    "Regression Check", "Change Classification Check", "Runtime Claim / Legacy Recovery Check",
    "Standalone Skill Discovery Check", "Context Budget Check",
    "Claim / Evidence Credibility Check",
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
    ("references/asset_package.md", "普通 Chat / Portable 模式"),
    ("references/asset_package.md", "## Asset Image Naming"),
    ("references/asset_package.md", "## Final Prompt Correspondence"),
    ("references/asset_package.md", "## Package Location And Source Rule"),
    ("references/asset_package.md", "## Optional Interoperable Tooling"),
    ("references/asset_package.md", "`_MANIFEST.md`"),
)

PACKAGE_CONSUMERS = (
    ("config.md", "references/asset_package.md"),
    ("rules/02_asset_rules.md", "references/asset_package.md"),
    ("rules/completion_gate.md", "references/asset_package.md"),
    ("references/project_workspace.md", "references/asset_package.md"),
    ("references/module_contracts_production.md", "references/asset_package.md"),
    ("modules/assets.md", "references/asset_package.md"),
)

PACKAGE_NON_OWNERS = (
    "rules/02_asset_rules.md",
    "rules/completion_gate.md",
    "references/project_workspace.md",
    "references/module_contracts_production.md",
    "modules/assets.md",
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
    for duplicate in duplicate_sd_film_entries(root):
        errors.append(
            f"duplicate SD Film discovery entry inside the canonical root: {duplicate}; "
            "remove or relocate staging copies"
        )
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
        (selection, "不创建Clip、也不输出`KEEP / ADAPT_SPLIT / RETURN`"),
        (selection, "Project Video Model Preference"),
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
        (visual_workflow, "# Medium Profile Gate"),
        (visual_workflow, "不得写入焦段毫米数、光比比值或器材"),
        (script_analysis, "媒介剖面与目标形式是两根独立的轴"),
        (knowledge_index, "## Persistent Medium Profile"),
        (project_bible, "未确认写 `Pending`"),
        (contracts_knowledge, "## Medium Profile Knowledge Contract"),
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
        (assets, "## Asset Naming And Delivery Package"),
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
    errors.extend(check_no_project_registry(root))
    errors.extend(check_reachability(root))
    errors.extend(check_internal_references(root))
    errors.extend(check_read_scope_sections(root))
    errors.extend(check_line_endings(root))
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, required=True)
    parser.add_argument(
        "--report", action="store_true",
        help="also print the periodic size and readability audit (sizes, index, reviews)",
    )
    args = parser.parse_args()
    errors = validate_skill(args.skill_root)
    if args.report:
        print(build_report(args.skill_root))
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: r82 structural, routing and readability validation")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
