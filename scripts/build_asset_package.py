#!/usr/bin/env python3
"""Optional deterministic builder for the SD Film production delivery package.

This script is *optional hardening* for `references/asset_package.md`: it copies
already-confirmed files by category, enforces the stable asset image filename
convention, writes the manifest/index, produces a zip, and checks the
one-to-one correspondence between a compiled video prompt's reference assets
and the packaged files.

What it does NOT do: it never invents a file, path, controlled ID or
confirmation state; it never edits, renames or moves anything inside the
project root; it never calls an image or video model or submits anything to an
external service. A blocked item is reported, never silently dropped.

Precondition: this tool only runs where the project root is actually readable
and the package location is writable (Work / Codex local mode). In a portable
Chat session with no local file access, deliver the text manifest and naming map
from `references/asset_package.md` instead, marked as "not packed" -- never
claim a package or zip exists.

Usage::

    build_asset_package.py --project-root <dir> [--registry <file>]
        [--project-id <id>] [--project-name <name>] [--version 001]
        [--output <dir>] [--no-zip] [--check-prompt <compiled-prompt.md>]
        [--json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------- contracts

ASSET_KINDS = {
    "CHAR": ("CHAR", "02_assets/CHAR", ("Identity", "Costume", "Scale", "State")),
    "ENV": ("ENV", "02_assets/ENV", ("Layout", "Material", "State")),
    "PROP": ("PROP", "02_assets/PROP", ("Identity", "Material", "Scale", "State")),
    "FX": ("FX", "02_assets/FX", ("FX Phase", "State")),
}
ALLOWED_PURPOSES = frozenset(
    purpose for _kind, _folder, purposes in ASSET_KINDS.values() for purpose in purposes
)
BOARD_PREFIX = "BOARD-"
# Environment views are named by the View IDs the multi-view contract already
# owns (`ENV-01` Master / `ENV-02` Reverse / `ENV-03` Lateral / `ENV-04` Top-Down)
# plus an extension View, so a file name never invents a second vocabulary.
VIEW_CODES = ("ENV-01", "ENV-02", "ENV-03", "ENV-04", "EXT")
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp")

CATEGORIES = (
    ("01_script", "Script"),
    ("02_assets", "Assets"),
    ("03_visual_development", "Visual Development"),
    ("04_scenes", "Scenes"),
    ("05_shots", "Shots"),
    ("06_clips", "Clips"),
)

# Files that carry the package's own bookkeeping and are therefore not assets.
BOOKKEEPING = re.compile(r"(^|/)(00_INDEX\.md|00_MANIFEST\.md|_MANIFEST\.md)$")
SEPARATOR = "｜"


def asset_id_kind(asset_id: str) -> str | None:
    """`CHAR-001` -> `CHAR`; anything outside the four namespaces -> None."""
    for kind in ASSET_KINDS:
        if asset_id.startswith(kind + "-"):
            return kind
    return None


def expected_filename(asset_id: str, purpose: str, view: str = "", suffix: str = ".png") -> str:
    """The one filename form `references/asset_package.md` allows.

    `ENV-002｜Layout_ENV-03.png` names the third view of environment ENV-002;
    `CHAR-001｜Identity.png` names a single-purpose character reference.
    """
    if asset_id.startswith(BOARD_PREFIX):
        return f"{asset_id}{SEPARATOR}{purpose}{suffix}"
    tail = f"{purpose}_{view}" if view else purpose
    return f"{asset_id}{SEPARATOR}{tail}{suffix}"


def filename_conforms(filename: str) -> tuple[list[str], list[str]]:
    """Split a filename into (hard violations, soft notes).

    Hard violations block the package because the final prompt could not cite
    the file unambiguously. Soft notes are legal-but-noteworthy forms: a bare
    `ENV-00X｜Layout` is the legitimate mother reference of the multi-view
    contract, so it is reported rather than rejected.
    """
    hard: list[str] = []
    soft: list[str] = []
    stem, dot, suffix = filename.rpartition(".")
    if not dot or ("." + suffix).lower() not in IMAGE_SUFFIXES:
        return [f"not an allowed image suffix: {filename}"], soft
    if SEPARATOR not in stem:
        return [f"missing the `{SEPARATOR}` separator: {filename}"], soft
    asset_id, purpose = stem.split(SEPARATOR, 1)
    if asset_id.startswith(BOARD_PREFIX):
        if not purpose:
            hard.append(f"support board file is missing its Item ID: {filename}")
        return hard, soft
    kind = asset_id_kind(asset_id)
    if kind is None:
        return [f"unknown asset ID namespace: {asset_id}"], soft
    allowed = ASSET_KINDS[kind][2]
    # Purposes are matched as whole values first, so a multi-word purpose such as
    # `FX Phase` is never mis-read as `Purpose-View`.
    if purpose in allowed:
        if kind == "ENV" and purpose == "Layout":
            soft.append(f"ENV Layout without an explicit view (mother reference): {filename}")
        return hard, soft
    if purpose in ALLOWED_PURPOSES:
        hard.append(f"purpose {purpose!r} is not allowed for {kind}: {filename}")
        return hard, soft
    base, underscore, view = purpose.partition("_")
    if base not in allowed:
        hard.append(f"purpose {base!r} is not allowed for {kind}: {filename}")
    if not underscore:
        hard.append(f"unknown purpose form: {filename}")
        return hard, soft
    if underscore and (kind != "ENV" or view not in VIEW_CODES):
        hard.append(f"view code {view!r} is not allowed here: {filename}")
    return hard, soft


# ---------------------------------------------------------------- registry


# A locked file name as it must appear in a registry record and in a compiled
# prompt: one of our ID namespaces, the separator, a purpose (no separator
# characters), and an image extension. Multi-word purposes such as `FX Phase`
# are matched whole, so the name is never truncated at the space.
LOCKED_FILENAME_RE = re.compile(
    r"((?:CHAR|ENV|PROP|FX|BOARD-[A-Za-z]+)-\d+" + re.escape(SEPARATOR)
    + r"[^｜|/\\\s]*?(?:\s[A-Za-z][^｜|/\\\s]*)?\.(?:png|jpg|jpeg|webp))",
    re.I,
)

# The stable reference name as it appears in a compiled prompt's reference
# field: `<Asset ID>｜<asset title>`, optionally followed by `_<View Code>`.
# Full locked file names are matched by LOCKED_FILENAME_RE and removed from the
# text before this pattern runs, so it only ever sees the short form. The asset
# ID is the mapping key; a View Code tail is what disambiguates an asset ID that
# owns several canonical images.
REFERENCE_NAME_RE = re.compile(
    r"((?:CHAR|ENV|PROP|FX|BOARD-[A-Za-z]+)-\d+)"
    + re.escape(SEPARATOR)
    + r"([^｜|/\\\s；;，,。、（）()\[\]]*)",
    re.I,
)
VIEW_CODE_TAIL_RE = re.compile(r"_(ENV|EXT)-\d{2}$", re.I)


class Asset:
    def __init__(self, asset_id: str, title: str) -> None:
        self.asset_id = asset_id
        self.title = title
        self.status = ""
        self.active_version = ""
        self.references: list[str] = []
        self.text = ""

    @property
    def kind(self) -> str | None:
        if self.asset_id.startswith(BOARD_PREFIX):
            return "SUPPORT"
        return asset_id_kind(self.asset_id)


def _field(text: str, *names: str) -> str:
    # Field names may carry separators (`Approved By / Approval Basis`), and the
    # value may contain brackets (`（用途：…）`), so neither side is word-bounded.
    for name in names:
        match = re.search(rf"^[ \t\-*]*{re.escape(name)}[ \t]*[:：][ \t]*(.+?)[ \t]*$", text, re.M)
        if match:
            return match.group(1).strip()
    return ""


def parse_registry(path: Path) -> list[Asset]:
    """Split the asset registry on its level-2 headings and read the leaf fields."""
    text = path.read_text(encoding="utf-8-sig")
    chunks = re.split(r"^##[ \t]+", text, flags=re.M)[1:]
    assets: list[Asset] = []
    for chunk in chunks:
        lines = chunk.splitlines()
        if not lines:
            continue
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        asset_id = _field(body, "Asset ID") or title.split()[0].strip("`*")
        asset = Asset(asset_id, title)
        asset.status = _field(body, "Status")
        asset.active_version = _field(body, "Active Version")
        # Keep the heading too: an Exception-Based Batch Confirmation marker is
        # often recorded on the heading line of the confirmed item.
        asset.text = chunk
        for reference in LOCKED_FILENAME_RE.findall(body):
            if reference not in asset.references:
                asset.references.append(reference)
        assets.append(asset)
    return assets


# ---------------------------------------------------------------- category sources

SOURCE_MAP = (
    ("01_script", (
        "01_script_analysis_locked.md", "01_script_locked.md", "01_production_script.md",
        "02_script_analysis.md",
    )),
    ("03_visual_development", (
        "project_bible.md", "03_visual_direction.md", "03_visual_development.md",
        "03_aesthetic_decision_lock.md", "07_project_color_reference.md",
    )),
    ("04_scenes", (
        "04_scene_breakdown.md", "05_scene_breakdown.md", "14_sequence_plan.md",
    )),
    ("05_shots", (
        "06_detailed_shot_design.md", "08_detailed_shot_design.md", "09_storyboard.md",
    )),
    ("06_clips", (
        "07_clip_production_plan.md", "10_clip_plan.md", "20_clip_plan.md",
    )),
)


# ---------------------------------------------------------------- admission

# Only work the user actually approved may enter the package. These markers are
# the traceable confirmation records the skill already writes; a file that
# carries none of them is reported as not packed instead of being shipped.
#
# Silence is a confirmation, not an absence of one: under the skill's
# Exception-Based Batch Confirmation, a batch that was actually shown and whose
# items are individually checkable is confirmed when the user advances without
# pointing at a problem. That is why batch markers count as a real basis -- what
# does NOT count is work the user never got to see.
ACCEPTANCE_MARKERS = (
    ("Auto-accepted under FAST", ("auto-accepted under fast", "auto accepted under fast")),
    # Checked before the per-item markers: a batch record legitimately contains
    # confirmation wording, and the more specific basis is the batch one.
    ("Confirmed (batch, no objection)", (
        "batch confirmed", "batch confirmation", "no objection", "未指出问题", "批次确认",
        "exception-based batch confirmation", "exception based batch confirmation",
    )),
    ("User Confirmed", (
        "approved by", "approval basis", "confirmed status: yes", "confirmed:basis",
        "user confirmed", "用户确认", "已确认", "确认通过", "confirmed by user",
    )),
)
ASSET_CONFIRMED_VALUES = ("yes", "confirmed", "asset confirmed", "true")
ASSET_UNCONFIRMED_VALUES = ("no", "not confirmed", "pending", "candidate", "draft", "not started")

# 06_clips is a gate condition of the package, not a file category: the Clip
# table has to be confirmed before the package exists at all.
CLIP_SOURCE_CANDIDATES = ("07_clip_production_plan.md", "10_clip_plan.md", "20_clip_plan.md")


def confirmation_basis(text: str) -> str | None:
    """Return the traceable acceptance basis carried by a record, if any."""
    lowered = text.lower()
    for label, markers in ACCEPTANCE_MARKERS:
        if any(marker in lowered for marker in markers):
            return label
    return None


def asset_is_confirmed(asset: Asset, text: str) -> tuple[bool, str]:
    """An asset enters the package only with a real confirmation record.

    The record may be the asset's own approval field or a batch confirmation
    carried in the same record block.
    """
    confirmed = _field(text, "Confirmed Status").lower()
    approved = _field(
        text, "Approved By / Approval Basis", "Approval Basis", "Approved By",
    )
    if confirmed not in ASSET_CONFIRMED_VALUES:
        if confirmed in ASSET_UNCONFIRMED_VALUES or not confirmed:
            return False, f"{asset.asset_id}: 未确认 (Confirmed Status: {confirmed or 'missing'})"
        return False, f"{asset.asset_id}: unreadable Confirmed Status ({confirmed})"
    if not approved and confirmation_basis(text) is None:
        return False, f"{asset.asset_id}: 缺确认记录 (confirmed without an approval or batch record)"
    return True, preferred_basis(text)


def preferred_basis(text: str) -> str:
    """FAST auto-acceptance is reported distinctly from the user's own confirmation."""
    return confirmation_basis(text) or "User Confirmed"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


class Builder:
    def __init__(self, args: argparse.Namespace) -> None:
        self.project_root = Path(args.project_root).resolve()
        self.registry_path = Path(args.registry).resolve() if args.registry else self.project_root / "asset_registry.md"
        self.project_id = args.project_id or self.project_root.name
        self.project_name = args.project_name or ""
        self.version = args.version
        self.package_name = self._package_name()
        self.output_dir = Path(args.output).resolve() if args.output else self.project_root.parent / f"{self.project_id}_packages" / self.version
        self.package_root = self.output_dir / self.package_name
        self.make_zip = not args.no_zip
        self.check_prompt = Path(args.check_prompt).resolve() if args.check_prompt else None
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.records: list[dict[str, str]] = []
        self.excluded: list[str] = []

    def _package_name(self) -> str:
        label = self.project_name.strip() or self.project_id
        safe = re.sub(r'[\\/:*?"<>|]', "_", label).strip()
        return f"{self.project_id}_{safe}_ProductionPackage_v{self.version}"

    # -- reporting

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    # -- build steps

    def asset_index(self) -> dict[str, list[Path]]:
        """Index every image file under the project root by bare file name.

        A registry canonical reference is normally a bare, locked file name
        while the real file can sit in any project subdirectory, so resolution
        is by name. Two different files sharing one name is an ambiguity, not a
        choice: it is reported so the operator resolves it.
        """
        index: dict[str, list[Path]] = {}
        for path in sorted(self.project_root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in IMAGE_SUFFIXES:
                continue
            # Exclusions are relative to the project root: a project may legally
            # live under a folder that happens to be named `tmp` or `.git`.
            relative = path.relative_to(self.project_root)
            if any(part in {".git", "tmp", "__pycache__"} for part in relative.parts[:-1]):
                continue
            index.setdefault(path.name, []).append(path)
        return index

    def stage_assets(self, assets: list[Asset]) -> None:
        """Copy confirmed asset images under their locked filenames.

        An asset that the user never confirmed is reported as not packed; it is
        never packaged on the strength of existing in the registry.
        """
        index = self.asset_index()
        for asset in assets:
            admitted, why = asset_is_confirmed(asset, asset.text)
            if not admitted:
                self.excluded.append(why)
                continue
            basis = preferred_basis(asset.text)
            if not asset.references:
                self.excluded.append(f"{asset.asset_id}: no canonical reference file registered")
                continue
            locked_name = Path(asset.references[0]).name
            matches = index.get(locked_name, [])
            if len(matches) > 1:
                self.error(
                    f"{asset.asset_id}: file name is ambiguous, {len(matches)} files share it: "
                    + ", ".join(str(item) for item in matches)
                )
                continue
            if not matches:
                self.error(
                    f"{asset.asset_id}: confirmed asset has no readable file in the project root "
                    f"({locked_name})"
                )
                continue
            hard, soft = filename_conforms(locked_name)
            for note in soft:
                self.warn(f"{asset.asset_id}: {note}")
            if hard:
                self.error(
                    f"{asset.asset_id}: canonical file name does not follow the naming contract: "
                    f"{locked_name} ({'; '.join(hard)})"
                )
                continue
            kind = asset.kind
            if kind == "SUPPORT":
                folder = "02_assets/SUPPORT"
            elif kind:
                folder = ASSET_KINDS[kind][1]
            else:
                self.error(f"{asset.asset_id}: unknown asset namespace, cannot classify")
                continue
            target = self.package_root / folder / locked_name
            self._copy(
                matches[0], target, "Assets", asset.asset_id,
                asset.active_version or asset.status, basis,
            )
            for extra in asset.references[1:]:
                extra_name = Path(extra).name
                extra_matches = index.get(extra_name, [])
                if len(extra_matches) != 1:
                    self.error(
                        f"{asset.asset_id}: additional canonical reference is not uniquely readable "
                        f"({extra_name})"
                    )
                    continue
                hard_extra, _ = filename_conforms(extra_name)
                if hard_extra:
                    self.error(
                        f"{asset.asset_id}: additional canonical file name does not follow the "
                        f"naming contract: {extra_name} ({'; '.join(hard_extra)})"
                    )
                    continue
                self._copy(
                    extra_matches[0], self.package_root / folder / extra_name, "Assets",
                    asset.asset_id, asset.active_version or asset.status, basis,
                )
        self._write_category_manifests(assets)

    def stage_category_files(self) -> None:
        """Admit a category file only with a traceable acceptance record.

        A file that exists in the project root but was never accepted is
        reported as not packed -- existing is not the same as being approved.
        """
        for folder, candidates in SOURCE_MAP:
            hits = 0
            for name in candidates:
                source = self.project_root / name
                if not source.is_file():
                    continue
                text = source.read_text(encoding="utf-8-sig", errors="replace")
                basis = preferred_basis(text) if confirmation_basis(text) else ""
                if not basis:
                    self.excluded.append(f"{folder}/{name}: 从未展示或未确认（缺确认记录）")
                    continue
                self._copy(
                    source, self.package_root / folder / name, folder, name, "", basis,
                )
                hits += 1
            if not hits:
                self.warn(f"{folder}: nothing admitted (missing or unconfirmed)")

    def clip_table_state(self) -> str:
        """`06_clips` is the package's gate condition, so it gets its own verdict."""
        for name in CLIP_SOURCE_CANDIDATES:
            source = self.project_root / name
            if not source.is_file():
                continue
            text = source.read_text(encoding="utf-8-sig", errors="replace")
            if confirmation_basis(text):
                return "confirmed"
            self.excluded.append(f"06_clips/{name}: 从未展示或未确认（缺确认记录）")
            return "unconfirmed"
        self.excluded.append("06_clips: no Clip Production Plan file found")
        return "missing"

    def _copy(
        self, source: Path, target: Path, category: str, identifier: str, version: str,
        basis: str = "",
    ) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not (target.exists() and sha256(target) == sha256(source)):
            shutil.copy2(source, target)
        self.records.append({
            "file": target.relative_to(self.package_root).as_posix(),
            "category": category,
            "identifier": identifier,
            "version": version,
            "basis": basis,
            "source": str(source),
            "bytes": str(target.stat().st_size),
            "sha256": sha256(target),
        })

    def _write_category_manifests(self, assets: list[Asset]) -> None:
        by_kind: dict[str, list[Asset]] = {}
        for asset in assets:
            admitted, _why = asset_is_confirmed(asset, asset.text)
            if admitted:
                by_kind.setdefault(asset.kind or "UNCLASSIFIED", []).append(asset)
        for kind, folder in (("CHAR", "02_assets/CHAR"), ("ENV", "02_assets/ENV"),
                             ("PROP", "02_assets/PROP"), ("FX", "02_assets/FX"),
                             ("SUPPORT", "02_assets/SUPPORT")):
            entries = by_kind.get(kind, [])
            lines = [
                f"# {kind} Manifest",
                "",
                "| 文件名 | Asset ID | Active Version | Status | Approval Basis |",
                "|---|---|---|---|---|",
            ]
            if not entries:
                lines.append(f"| Not Applicable | — | — | — | 本项目无{kind}类别已认可资产 |")
            for asset in sorted(entries, key=lambda item: item.asset_id):
                names = "、".join(asset.references) or "—"
                lines.append(
                    f"| {names} | {asset.asset_id} | {asset.active_version or '—'} | "
                    f"{asset.status or '—'} | {preferred_basis(asset.text)} |"
                )
            target = self.package_root / folder / "_MANIFEST.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    def write_index_and_manifest(self, assets: list[Asset], built_at: str) -> None:
        index = [
            f"# {self.package_name}",
            "",
            f"- Project ID: {self.project_id}",
            f"- Project Name: {self.project_name or '—'}",
            f"- Package Revision: {self.version}",
            f"- Built At: {built_at}",
            f"- Confirmed Assets: "
            f"{sum(1 for a in assets if asset_is_confirmed(a, a.text)[0])} / {len(assets)}",
            f"- Packaged Files: {len(self.records)}",
            f"- Not Packaged: {len(self.excluded)}",
            "",
            "只打包用户已认可的内容：每一项都有确认记录且真实文件存在。",
            "",
            "| 类别 | 目录 | 内容（均须已认可） |",
            "|---|---|---|",
            "| Script | `01_script/` | 用户确认过的剧本与剧本分析 |",
            "| Assets | `02_assets/` | 每条`Asset Confirmed`的图片（按CHAR / ENV / PROP / FX / SUPPORT） |",
            "| Visual Development | `03_visual_development/` | 用户确认过的Style Baseline / Aesthetic Decision Lock / Project Color Reference |",
            "| Scenes | `04_scenes/` | 用户确认过的Scene Breakdown与适用Sequence Plan |",
            "| Shots | `05_shots/` | 用户确认过的Detailed Shot Design与适用Storyboard |",
            "| Clips | `06_clips/` | 用户确认过的Clip Production Plan |",
            "",
        ]
        if self.excluded:
            index += ["## 未确认／未打包", ""] + [f"- {item}" for item in self.excluded] + [""]
        if self.warnings:
            index += ["## Warnings", ""] + [f"- {item}" for item in self.warnings] + [""]
        if self.errors:
            index += ["## Blocked Items", ""] + [f"- {item}" for item in self.errors] + [""]
        if not self.errors:
            index += ["## Status", "", "已认可项已全部打包，命名与对应性检查通过。"]
        (self.package_root / "00_INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8", newline="\n")

        manifest = [
            "# Package Manifest",
            "",
            "包在Clip表确认后、最终视频Prompt之前生成；包内不含最终视频Prompt。",
            "`Approval Basis`区分逐项确认、批次确认（未提异议）与FAST自动接受。",
            "",
            "| 文件 | 类别 | Asset ID / Artifact | 版本 | Approval Basis | 来源 | 字节 | SHA-256 |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for record in sorted(self.records, key=lambda item: item["file"]):
            manifest.append(
                f"| {record['file']} | {record['category']} | {record['identifier']} | "
                f"{record['version'] or '—'} | {record.get('basis') or '—'} | {record['source']} | "
                f"{record['bytes']} | {record['sha256']} |"
            )
        if self.excluded:
            manifest += ["", "## 未确认／未打包（未进入本包）", ""] + [
                f"- {item}" for item in self.excluded
            ]
        (self.package_root / "00_MANIFEST.md").write_text("\n".join(manifest) + "\n", encoding="utf-8", newline="\n")

    def check_correspondence(self) -> None:
        if not self.check_prompt:
            return
        if not self.check_prompt.is_file():
            self.error(f"prompt file to check is not readable: {self.check_prompt}")
            return
        text = self.check_prompt.read_text(encoding="utf-8-sig")
        packaged: dict[str, list[str]] = {}
        for record in self.records:
            if not record["file"].startswith("02_assets/"):
                continue
            name = Path(record["file"]).name
            match = re.match(r"((?:CHAR|ENV|PROP|FX|BOARD-[A-Za-z]+)-\d+)", name, re.I)
            if match:
                packaged.setdefault(match.group(1).upper(), []).append(name)
        packaged_files = {name for names in packaged.values() for name in names}

        # Full locked file names quoted anywhere in the prompt.
        referenced = {Path(name).name for name in LOCKED_FILENAME_RE.findall(text)}

        # Short reference names: `<Asset ID>｜<title>[_<View Code>]`.
        remainder = LOCKED_FILENAME_RE.sub(" ", text)
        for asset_id, tail in REFERENCE_NAME_RE.findall(remainder):
            key = asset_id.upper()
            files = packaged.get(key, [])
            if not files:
                self.error(
                    f"compiled prompt references an asset ID that is not in the package: {asset_id}"
                )
                continue
            if len(files) == 1:
                referenced.add(files[0])
                continue
            view_match = VIEW_CODE_TAIL_RE.search(tail)
            chosen = (
                [name for name in files if Path(name).stem.upper().endswith(view_match.group(0).upper())]
                if view_match
                else []
            )
            if len(chosen) == 1:
                referenced.add(chosen[0])
            else:
                self.error(
                    f"compiled prompt references {asset_id} without a View Code or Purpose, but the "
                    f"package holds several files for it ({', '.join(sorted(files))}); "
                    "the entry cannot be mapped to one file"
                )

        for name in sorted(referenced - packaged_files):
            self.error(f"compiled prompt references a file that is not in the package: {name}")
        for name in sorted(packaged_files - referenced):
            self.warn(f"packaged asset file is not referenced by this prompt: {name}")

    def make_archive(self) -> str | None:
        if not self.make_zip:
            return None
        archive = self.output_dir / f"{self.package_name}.zip"
        if archive.exists():
            archive.unlink()
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as handle:
            for path in sorted(self.package_root.rglob("*")):
                if path.is_file():
                    handle.write(path, path.relative_to(self.output_dir).as_posix())
        return str(archive)

    def run(self) -> dict[str, object]:
        if not self.project_root.is_dir():
            self.error(f"project root does not exist: {self.project_root}")
            return self._result(None)
        if not self.registry_path.is_file():
            self.error(f"asset registry is not readable: {self.registry_path}")
            return self._result(None)
        assets = parse_registry(self.registry_path)
        if not assets:
            self.error(f"no asset records found in {self.registry_path}")
            return self._result(None)
        seen_ids: dict[str, str] = {}
        for asset in assets:
            if asset.asset_id in seen_ids:
                self.error(f"duplicate asset ID in registry: {asset.asset_id}")
            seen_ids[asset.asset_id] = asset.title
        self.package_root.mkdir(parents=True, exist_ok=True)
        built_at = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
        self.stage_assets(assets)
        self.stage_category_files()
        clip_state = self.clip_table_state()
        if clip_state != "confirmed":
            self.error(
                f"package gate not met: Confirmed Clip Production Plan is {clip_state} "
                "(06_clips)"
            )
        self.check_correspondence()
        self.write_index_and_manifest(assets, built_at)
        archive = self.make_archive()
        if self.errors:
            # A partial package is misleading: keep it for diagnosis but say so loudly.
            self.warn("package is incomplete; see 00_INDEX.md Blocked Items")
        return self._result(archive)

    def _result(self, archive: str | None) -> dict[str, object]:
        return {
            "ok": not self.errors,
            "package_root": str(self.package_root),
            "archive": archive,
            "files": len(self.records),
            "errors": self.errors,
            "warnings": self.warnings,
            "excluded": self.excluded,
            "pending": self.excluded,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--registry")
    parser.add_argument("--project-id")
    parser.add_argument("--project-name", default="")
    parser.add_argument("--version", default="001")
    parser.add_argument("--output")
    parser.add_argument("--no-zip", action="store_true")
    parser.add_argument("--check-prompt")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = Builder(args).run()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        state = "OK" if result["ok"] else "BLOCKED"
        print(f"package: {result['package_root']}")
        print(f"archive: {result['archive'] or '—'}")
        print(f"files: {result['files']}  status: {state}")
        for item in result["warnings"]:
            print(f"WARN: {item}")
        for item in result["errors"]:
            print(f"ERROR: {item}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
