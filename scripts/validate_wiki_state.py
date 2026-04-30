#!/usr/bin/env python3
"""Validate that the LLM-Wiki matches the current repository state.

This complements the link and citation checks by validating the wiki as a
contract over the paper/source project: tracked paper sections must exist,
progress blockers must match current TODO citations, source-register entries
must point to real source files, and generated build artifacts must not be stale.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import TypedDict, cast
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PROGRESS_REGISTER = WIKI / "data" / "progress-register.json"
SOURCE_REGISTER = ROOT / "sources" / "source-register.md"
DASHBOARD = WIKI / "progress" / "completion-dashboard.md"
BIB = ROOT / "latex" / "references.bib"
CHANGELOG = ROOT / "CHANGELOG.md"
DIST_FILES = [
    ROOT / "dist" / "mcp-research-paper.md",
    ROOT / "dist" / "mcp-research-paper.tex",
    ROOT / "dist" / "mcp-research-paper.pdf",
]

REQUIRED_WIKI_FILES = [
    WIKI / "index.md",
    WIKI / "AGENTS.md",
    WIKI / "guidance" / "authoring-contract.md",
    WIKI / "guidance" / "citation-conventions.md",
    WIKI / "guidance" / "source-discipline.md",
    WIKI / "guidance" / "section-acceptance.md",
    WIKI / "guidance" / "session-close.md",
    WIKI / "progress" / "plan.md",
    WIKI / "progress" / "parallel-work-plan.md",
    DASHBOARD,
    WIKI / "progress" / "phase-log.md",
    WIKI / "evals" / "wiki-evaluation-plan.md",
    WIKI / "templates" / "source-note.md",
    WIKI / "templates" / "section-skeleton.md",
    PROGRESS_REGISTER,
]
REQUIRED_DOC_FILES = [
    ROOT / "README.md",
    CHANGELOG,
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^]\n|#]+)(?:#[^]\n|]+)?(?:\|[^]\n]+)?\]\]")
FENCED_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
CITATION_RE = re.compile(r"(?<![\w@])@([A-Za-z0-9][A-Za-z0-9:_-]*)")
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
SOURCE_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+)\|", re.MULTILINE)
SOURCE_NOTE_KEY_LINE_RE = re.compile(
    r"^\s*-\s*(?:Citation key|Proposed citation key|Proposed citation keys):\s*(.+)$",
    re.MULTILINE,
)
BACKTICK_KEY_RE = re.compile(r"`([^`]+)`")


class Issue(TypedDict):
    type: str
    file: str
    message: str
    target: str
    status: str
    blocker: str
    blockers: str


class Report(TypedDict):
    generated: str
    status: str
    summary: dict[str, int]
    errors: list[Issue]
    warnings: list[Issue]


def issue(
    kind: str,
    *,
    file: str = "",
    message: str = "",
    target: str = "",
    status: str = "",
    blocker: str = "",
    blockers: str = "",
) -> Issue:
    return {
        "type": kind,
        "file": file,
        "message": message,
        "target": target,
        "status": status,
        "blocker": blocker,
        "blockers": blockers,
    }


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCED_RE.sub("", text))


def is_external(target: str) -> bool:
    return urlparse(target).scheme in {"http", "https", "mailto"}


def normalize_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def resolve_link(source: Path, target: str) -> Path | None:
    target = normalize_target(target)
    if not target or target.startswith("#") or is_external(target):
        return None
    return (source.parent / target).resolve()


def markdown_files(base: Path) -> list[Path]:
    return sorted(path for path in base.rglob("*.md") if path.is_file())


def load_json(path: Path, errors: list[Issue]) -> object | None:
    try:
        return cast(object, json.loads(path.read_text(encoding="utf-8")))
    except Exception as exc:
        errors.append(issue("json_parse", file=rel(path), message=str(exc)))
        return None


def bib_keys() -> set[str]:
    if not BIB.exists():
        return set()
    return set(BIB_ENTRY_RE.findall(BIB.read_text(encoding="utf-8")))


def citations_in(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(CITATION_RE.findall(strip_code(path.read_text(encoding="utf-8"))))


def all_todo_markers(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = FENCED_RE.sub("", path.read_text(encoding="utf-8"))
    return set(re.findall(r"\bTODO-[A-Za-z0-9:_-]+\b", text))


def check_required_files(errors: list[Issue]) -> None:
    errors.extend(
        issue("missing_required_wiki_file", file=rel(path)) for path in REQUIRED_WIKI_FILES if not path.exists()
    )
    errors.extend(
        issue("missing_required_doc_file", file=rel(path)) for path in REQUIRED_DOC_FILES if not path.exists()
    )


def check_ds_store(warnings: list[Issue]) -> None:
    warnings.extend(issue("metadata_file_in_wiki", file=rel(path)) for path in WIKI.rglob(".DS_Store"))


def check_wiki_links(errors: list[Issue], summary: dict[str, int]) -> None:
    checked = 0
    for path in markdown_files(WIKI):
        text = strip_code(path.read_text(encoding="utf-8"))
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1)
            resolved = resolve_link(path, target)
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                errors.append(issue("broken_wiki_link", file=rel(path), target=target))
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1)
            if not target.endswith(".md"):
                target = f"{target}.md"
            resolved = resolve_link(path, target)
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                errors.append(issue("broken_wikilink", file=rel(path), target=match.group(1)))
    summary["wiki_internal_links_checked"] = checked


def check_source_register(errors: list[Issue], warnings: list[Issue], summary: dict[str, int]) -> None:
    if not SOURCE_REGISTER.exists():
        errors.append(issue("missing_source_register", file=rel(SOURCE_REGISTER)))
        return
    text = SOURCE_REGISTER.read_text(encoding="utf-8")
    rows = SOURCE_ROW_RE.findall(text)
    summary["source_register_rows"] = len(rows)
    for source_path, status in rows:
        path = ROOT / source_path
        normalized_status = status.strip().lower()
        if not path.exists():
            errors.append(issue("source_register_missing_file", file=source_path))
            continue
        body = path.read_text(encoding="utf-8")
        if "[To be added]" in body or "[To be written]" in body:
            errors.append(issue("legacy_placeholder", file=source_path))
        if normalized_status == "placeholder" and "Status: placeholder" not in body:
            warnings.append(issue("placeholder_status_without_marker", file=source_path))
        if normalized_status == "started" and "### " not in body:
            warnings.append(issue("started_source_without_entries", file=source_path))


def check_source_note_citation_keys(errors: list[Issue], summary: dict[str, int]) -> None:
    keys = bib_keys()
    checked = 0
    for path in sorted((ROOT / "sources").glob("*.md")):
        if path == SOURCE_REGISTER:
            continue
        text = path.read_text(encoding="utf-8")
        for line in SOURCE_NOTE_KEY_LINE_RE.findall(text):
            for key in BACKTICK_KEY_RE.findall(line):
                if key.startswith("TODO-"):
                    continue
                checked += 1
                if key not in keys:
                    errors.append(
                        issue(
                            "source_note_key_missing_bib",
                            file=rel(path),
                            blocker=key,
                        )
                    )
    summary["source_note_citation_keys_checked"] = checked


def check_progress_register(errors: list[Issue], warnings: list[Issue], summary: dict[str, int]) -> None:
    data = load_json(PROGRESS_REGISTER, errors)
    if not isinstance(data, dict):
        return
    sections = data.get("sections")
    if not isinstance(sections, list):
        errors.append(issue("progress_register_shape", file=rel(PROGRESS_REGISTER), message="sections must be a list"))
        return
    keys = bib_keys()
    summary["progress_sections"] = len(sections)
    summary["bib_entries"] = len(keys)

    paper_todo_citations: dict[str, set[str]] = {}
    for path in sorted((ROOT / "paper").glob("*.md")):
        paper_todo_citations[rel(path)] = {key for key in citations_in(path) if key.startswith("TODO-")}

    progress_paths: set[str] = set()
    for item in sections:
        if not isinstance(item, dict):
            errors.append(
                issue("progress_register_shape", file=rel(PROGRESS_REGISTER), message="section item must be object")
            )
            continue
        section_path = item.get("path")
        next_source_file = item.get("next_source_file")
        status = item.get("status")
        blockers = item.get("blocked_by", [])
        if not isinstance(section_path, str):
            errors.append(issue("progress_missing_path", file=rel(PROGRESS_REGISTER)))
            continue
        progress_paths.add(section_path)
        section = ROOT / section_path
        if not section.exists():
            errors.append(issue("progress_missing_section", file=section_path))
            continue
        if status not in {"placeholder", "started", "source-ready", "draft-ready", "review-ready"}:
            errors.append(issue("invalid_section_status", file=section_path, status=str(status)))
        if not isinstance(next_source_file, str) or not (ROOT / next_source_file).exists():
            errors.append(issue("progress_missing_next_source", file=section_path, target=str(next_source_file)))
        if not isinstance(blockers, list) or not all(isinstance(blocker, str) for blocker in blockers):
            errors.append(issue("progress_invalid_blockers", file=section_path))
            continue

        blocker_set = set(blockers)
        for blocker in sorted(blocker_set):
            if not blocker.startswith("TODO-"):
                errors.append(issue("progress_blocker_not_todo", file=section_path, blocker=blocker))
            if blocker not in keys:
                errors.append(issue("progress_blocker_missing_bib", file=section_path, blocker=blocker))

            search_paths = [section]
            if isinstance(next_source_file, str):
                search_paths.append(ROOT / next_source_file)
            if not any(blocker in all_todo_markers(path) for path in search_paths if path.exists()):
                warnings.append(
                    issue("progress_blocker_not_near_section_or_source", file=section_path, blocker=blocker)
                )

        section_todos = paper_todo_citations.get(section_path, set())
        missing_from_progress = sorted(section_todos - blocker_set)
        errors.extend(
            issue("section_todo_not_in_progress_register", file=section_path, blocker=blocker)
            for blocker in missing_from_progress
        )

    for section_path, todos in sorted(paper_todo_citations.items()):
        if todos and section_path not in progress_paths:
            errors.append(
                issue("paper_section_with_todos_not_tracked", file=section_path, blockers=", ".join(sorted(todos)))
            )


def check_section_acceptance_coverage(errors: list[Issue], summary: dict[str, int]) -> None:
    acceptance_path = WIKI / "guidance" / "section-acceptance.md"
    data = load_json(PROGRESS_REGISTER, errors)
    if not acceptance_path.exists() or not isinstance(data, dict):
        return
    sections = data.get("sections")
    if not isinstance(sections, list):
        return

    acceptance = acceptance_path.read_text(encoding="utf-8")
    tracked = 0
    for item in sections:
        if not isinstance(item, dict):
            continue
        section_path = item.get("path")
        if not isinstance(section_path, str):
            continue
        tracked += 1
        if f"`{section_path}`" not in acceptance:
            errors.append(
                issue(
                    "tracked_section_missing_acceptance_criteria",
                    file=section_path,
                    target=rel(acceptance_path),
                )
            )
    summary["acceptance_tracked_sections"] = tracked


def check_completion_dashboard_coverage(errors: list[Issue], summary: dict[str, int]) -> None:
    if not DASHBOARD.exists():
        return
    dashboard = DASHBOARD.read_text(encoding="utf-8")

    paper_paths = sorted(rel(path) for path in (ROOT / "paper").glob("*.md"))
    errors.extend(
        issue("completion_dashboard_missing_paper_section", file=paper_path, target=rel(DASHBOARD))
        for paper_path in paper_paths
        if f"`{paper_path}`" not in dashboard
    )
    summary["completion_dashboard_paper_sections"] = len(paper_paths)

    if SOURCE_REGISTER.exists():
        source_rows = SOURCE_ROW_RE.findall(SOURCE_REGISTER.read_text(encoding="utf-8"))
        for source_path, _status in source_rows:
            if f"`{source_path}`" not in dashboard:
                errors.append(
                    issue("completion_dashboard_missing_source_file", file=source_path, target=rel(DASHBOARD))
                )
        summary["completion_dashboard_source_files"] = len(source_rows)

    data = load_json(PROGRESS_REGISTER, errors)
    if not isinstance(data, dict):
        return
    sections = data.get("sections")
    if not isinstance(sections, list):
        return
    tracked = 0
    for item in sections:
        if not isinstance(item, dict):
            continue
        section_path = item.get("path")
        status = item.get("status")
        if not isinstance(section_path, str):
            continue
        tracked += 1
        if f"`{section_path}`" not in dashboard:
            errors.append(
                issue("completion_dashboard_missing_tracked_section", file=section_path, target=rel(DASHBOARD))
            )
        dashboard_lower = dashboard.lower()
        if (
            isinstance(status, str)
            and status.lower() not in dashboard_lower
            and status.replace("-", " ") not in dashboard_lower
        ):
            errors.append(
                issue(
                    "completion_dashboard_missing_tracked_status",
                    file=section_path,
                    target=rel(DASHBOARD),
                    status=status,
                )
            )
    summary["completion_dashboard_tracked_sections"] = tracked


def check_build_freshness(errors: list[Issue], warnings: list[Issue], summary: dict[str, int]) -> None:
    source_paths: list[Path] = []
    for dirname in ("paper", "sources", "latex"):
        source_paths.extend(path for path in (ROOT / dirname).rglob("*") if path.is_file())
    source_paths.extend([ROOT / "README.md", ROOT / "Makefile"])
    latest_source = max((path.stat().st_mtime for path in source_paths if path.exists()), default=0)
    summary["build_artifacts_expected"] = len(DIST_FILES)
    for artifact in DIST_FILES:
        if not artifact.exists():
            warnings.append(issue("missing_build_artifact", file=rel(artifact)))
            continue
        if artifact.stat().st_mtime < latest_source:
            warnings.append(issue("stale_build_artifact", file=rel(artifact)))


def write_reports(report: Report) -> None:
    data_dir = WIKI / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "wiki-state-report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    summary = report["summary"]
    errors = report["errors"]
    warnings = report["warnings"]
    lines = [
        "---",
        'title: "Wiki State Report"',
        'note_type: "validation-report"',
        'status: "{}"'.format(report["status"]),
        "tags:",
        '  - "wiki"',
        '  - "validation"',
        '  - "repo-state"',
        "related:",
        '  - "index.md"',
        '  - "progress/plan.md"',
        "---",
        "",
        "# Wiki State Report",
        "",
        f"- Generated: `{report['generated']}`",
        f"- Status: `{report['status']}`",
        f"- Errors: `{len(errors)}`",
        f"- Warnings: `{len(warnings)}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in sorted(summary.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Errors", ""])
    if errors:
        lines.extend(f"- `{error['type']}`: {error}" for error in errors)
    else:
        lines.append("- None.")
    lines.extend(["", "## Warnings", ""])
    if warnings:
        lines.extend(f"- `{warning['type']}`: {warning}" for warning in warnings)
    else:
        lines.append("- None.")
    lines.append("")
    (WIKI / "wiki-state-report.md").write_text("\n".join(lines), encoding="utf-8")


def build_report() -> Report:
    errors: list[Issue] = []
    warnings: list[Issue] = []
    summary: dict[str, int] = {}

    check_required_files(errors)
    check_ds_store(warnings)
    check_wiki_links(errors, summary)
    check_source_register(errors, warnings, summary)
    check_source_note_citation_keys(errors, summary)
    check_progress_register(errors, warnings, summary)
    check_section_acceptance_coverage(errors, summary)
    check_completion_dashboard_coverage(errors, summary)
    check_build_freshness(errors, warnings, summary)

    return {
        "generated": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "status": "pass" if not errors else "fail",
        "summary": summary,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="write wiki/data/wiki-state-report.json and wiki/wiki-state-report.md",
    )
    args = parser.parse_args()

    report = build_report()
    if args.write_report:
        write_reports(report)

    print(f"Wiki state validation: {report['status']}")
    print(f"Errors: {len(report['errors'])}")
    print(f"Warnings: {len(report['warnings'])}")
    for error in report["errors"]:
        print(f"ERROR {error['type']}: {error}", file=sys.stderr)
    for warning in report["warnings"]:
        print(f"WARN {warning['type']}: {warning}")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
