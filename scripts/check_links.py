#!/usr/bin/env python3
"""Check internal Markdown and Obsidian-style wiki links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [ROOT / "paper", ROOT / "sources", ROOT / "wiki"]
SCAN_FILES = [ROOT / "README.md"]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^]\n|#]+)(?:#[^]\n|]+)?(?:\|[^]\n]+)?\]\]")
FENCED_RE = re.compile(r"```.*?```", re.DOTALL)


def strip_fenced_code(text: str) -> str:
    return FENCED_RE.sub("", text)


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def normalize(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def resolve(source: Path, target: str) -> Path | None:
    target = normalize(target)
    if not target or target.startswith("#") or is_external(target):
        return None
    return (source.parent / target).resolve()


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in SCAN_DIRS:
        if directory.exists():
            files.extend(sorted(directory.rglob("*.md")))
    files.extend(path for path in SCAN_FILES if path.exists())
    return files


def main() -> int:
    errors: list[str] = []
    checked = 0

    for path in markdown_files():
        text = strip_fenced_code(path.read_text(encoding="utf-8"))

        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1)
            resolved = resolve(path, target)
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} -> {target}")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1)
            if not target.endswith(".md"):
                target = f"{target}.md"
            resolved = resolve(path, target)
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} -> [[{match.group(1)}]]")

    print(f"Internal links checked: {checked}")
    if errors:
        print("Broken internal links:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
