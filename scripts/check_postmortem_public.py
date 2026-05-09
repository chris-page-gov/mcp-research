#!/usr/bin/env python3
"""Validate the generated public assistant postmortem derivative."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINT = ROOT / "postmortem-public" / "wiki" / "data" / "publication_lint.json"


def main() -> int:
    if not LINT.exists():
        print("Public postmortem not present; skipping postmortem publication check.")
        return 0

    try:
        payload = json.loads(LINT.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Could not parse {LINT.relative_to(ROOT)}: {exc}", file=sys.stderr)
        return 1

    status = payload.get("status")
    errors = payload.get("errors") or []
    warnings = payload.get("warnings") or []
    print(f"Postmortem publication lint: {status}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if status != "pass":
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
