#!/usr/bin/env python3
"""Check Pandoc citation keys against latex/references.bib."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "latex" / "references.bib"
SCAN_DIRS = [ROOT / "paper", ROOT / "sources", ROOT / "wiki"]
SCAN_FILES = [ROOT / "README.md"]

ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
FENCED_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
CITATION_RE = re.compile(r"(?<![\w@])@([A-Za-z0-9][A-Za-z0-9:_-]*)")


def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCED_RE.sub("", text))


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in SCAN_DIRS:
        if directory.exists():
            files.extend(sorted(directory.rglob("*.md")))
    files.extend(path for path in SCAN_FILES if path.exists())
    return files


def load_bib_keys() -> set[str]:
    if not BIB.exists():
        return set()
    return set(ENTRY_RE.findall(BIB.read_text(encoding="utf-8")))


def main() -> int:
    bib_keys = load_bib_keys()
    used: dict[str, list[str]] = {}
    for path in markdown_files():
        text = strip_code(path.read_text(encoding="utf-8"))
        for key in CITATION_RE.findall(text):
            used.setdefault(key, []).append(path.relative_to(ROOT).as_posix())

    missing = sorted(key for key in used if key not in bib_keys)
    todo = sorted(key for key in used if key.startswith("TODO-"))
    unused = sorted(key for key in bib_keys if key not in used and not key.startswith("TODO-"))

    print(f"Citation keys used: {len(used)}")
    print(f"BibTeX entries: {len(bib_keys)}")
    print(f"TODO citation keys still present: {len(todo)}")
    for key in todo:
        locations = ", ".join(sorted(set(used[key])))
        print(f"  TODO {key}: {locations}")

    if missing:
        print("Missing BibTeX entries:", file=sys.stderr)
        for key in missing:
            locations = ", ".join(sorted(set(used[key])))
            print(f"  {key}: {locations}", file=sys.stderr)
        return 1

    if unused:
        print(f"Unused non-TODO BibTeX entries: {len(unused)}")
        for key in unused:
            print(f"  {key}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
