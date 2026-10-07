#!/usr/bin/env python3
"""Deterministic repository verifier for the Elevate curriculum workspace.

Verifies:
1. Balanced fenced code blocks across all Markdown files.
2. All relative Markdown links and image embeds (outside code blocks/inline code)
   resolve to existing files on disk.
3. All topic notes in Notes/Day_1..Day_5 are indexed in their Day_N/README.md.
4. All PNG assets in Notes/Day_N/assets/ have valid PNG headers, are non-empty,
   and are referenced by at least one Markdown file in Notes/Day_N/.
"""

from __future__ import annotations

import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def strip_code(markdown_text: str) -> tuple[str, int]:
    """Return markdown with fenced and inline code removed, plus fence count."""
    lines = markdown_text.splitlines()
    out_lines: list[str] = []
    in_fence = False
    fence_marker = ""
    fence_count = 0

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_count += 1
                continue
            if stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
                fence_count += 1
                continue
        if not in_fence:
            # Strip inline code spans (`...`)
            cleaned = re.sub(r"`[^`]*`", "", line)
            out_lines.append(cleaned)

    return "\n".join(out_lines), fence_count


def extract_relative_targets(markdown_text: str) -> list[str]:
    """Extract relative link/image targets outside code blocks."""
    cleaned, _ = strip_code(markdown_text)
    targets: list[str] = []
    for match in LINK_RE.finditer(cleaned):
        raw = match.group(1).strip()
        if not raw:
            continue
        # Strip optional title in link: (path "title")
        target = raw.split()[0].strip("<>")
        if (
            target.startswith(("http://", "https://", "mailto:", "#"))
            or "://" in target
        ):
            continue
        target_path = target.split("#", 1)[0]
        if target_path:
            targets.append(target_path)
    return targets


def main() -> int:
    errors: list[str] = []
    md_files = sorted(
        p for p in REPO_ROOT.rglob("*.md") if ".git" not in p.parts
    )

    total_links_checked = 0
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        _, fence_count = strip_code(text)
        if fence_count % 2 != 0:
            errors.append(
                f"Unclosed code fence in {md_file.relative_to(REPO_ROOT)}"
            )

        for target in extract_relative_targets(text):
            total_links_checked += 1
            if target.startswith("/"):
                resolved = (REPO_ROOT / target.lstrip("/")).resolve()
            else:
                resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"Broken link in {md_file.relative_to(REPO_ROOT)}: "
                    f"'{target}' -> {resolved} does not exist"
                )

    notes_root = REPO_ROOT / "Notes"
    total_topic_notes = 0
    total_png_assets = 0

    for day_num in range(1, 6):
        day_dir = notes_root / f"Day_{day_num}"
        readme_path = day_dir / "README.md"
        if not readme_path.exists():
            errors.append(f"Missing {readme_path.relative_to(REPO_ROOT)}")
            continue

        readme_targets = {
            (day_dir / t).resolve()
            for t in extract_relative_targets(
                readme_path.read_text(encoding="utf-8")
            )
        }

        topic_notes = sorted(
            p for p in day_dir.glob("*.md") if p.name != "README.md"
        )
        total_topic_notes += len(topic_notes)
        for note in topic_notes:
            if note.resolve() not in readme_targets:
                errors.append(
                    f"Unindexed note in Day_{day_num}/README.md: "
                    f"{note.relative_to(REPO_ROOT)}"
                )

        referenced_assets: set[pathlib.Path] = set()
        for md_in_day in day_dir.glob("*.md"):
            for t in extract_relative_targets(
                md_in_day.read_text(encoding="utf-8")
            ):
                referenced_assets.add((md_in_day.parent / t).resolve())

        assets_dir = day_dir / "assets"
        if assets_dir.exists():
            for png in sorted(assets_dir.glob("*.png")):
                total_png_assets += 1
                size = png.stat().st_size
                if size == 0:
                    errors.append(
                        f"Empty PNG asset: {png.relative_to(REPO_ROOT)}"
                    )
                else:
                    with png.open("rb") as f:
                        header = f.read(8)
                    if header != PNG_MAGIC:
                        errors.append(
                            f"Invalid PNG header: {png.relative_to(REPO_ROOT)}"
                        )
                if png.resolve() not in referenced_assets:
                    errors.append(
                        f"Orphaned PNG asset (unreferenced): "
                        f"{png.relative_to(REPO_ROOT)}"
                    )

    if errors:
        print(f"Verification FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        f"Verification PASSED: {len(md_files)} Markdown files, "
        f"{total_topic_notes} curriculum topic notes, "
        f"{total_png_assets} PNG slide assets, and "
        f"{total_links_checked} relative links verified with 0 errors."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
