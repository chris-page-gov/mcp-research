#!/usr/bin/env python3
"""Build private and public assistant postmortem wikis for this repository."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote

from codex_project_summary import (
    ROOT,
    _discover_session_files,
    _extract_user_text,
    _human_int,
    _is_bootstrap_message,
    _parse_session_file,
    build_summary,
)

CODEX_HOME = Path.home() / ".codex"
REPO_FILTER = "mcp-research"
PRIVATE_DIR = ROOT / "postmortem"
PUBLIC_DIR = ROOT / "postmortem-public"
PUBLIC_WIKI = PUBLIC_DIR / "wiki"


def _now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _git_output(args: list[str]) -> str:
    try:
        result = subprocess.run(["git", *args], cwd=ROOT, check=True, text=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def _github_base_url() -> str:
    remote = _git_output(["remote", "get-url", "origin"])
    if remote.startswith("https://github.com/"):
        return remote.removesuffix(".git")
    match = re.match(r"git@github\.com:(.+?)(?:\.git)?$", remote)
    if match:
        return f"https://github.com/{match.group(1)}"
    return "https://github.com/chris-page-gov/mcp-research"


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def _link(label: str, target: str) -> str:
    return f"[{label}]({target})"


def _table_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _blob_url(repo_url: str, commit: str, path: str) -> str:
    return f"{repo_url}/blob/{commit}/{quote(path)}"


def _artifact_inputs(repo_url: str, baseline_commit: str) -> list[dict[str, Any]]:
    raw = [
        ("README", "README.md", "Project setup and build entry point."),
        ("Changelog", "CHANGELOG.md", "Public change history and wiki tracking explanation."),
        ("Makefile", "Makefile", "Build, validation, and reporting commands."),
        ("Paper skeleton", "paper/02-mcp-in-a-nutshell.md", "First source-ready paper section."),
        ("Technical critiques skeleton", "paper/04-technical-critiques-and-mitigations.md", "Criticism/evidence/mitigation matrix."),
        ("Alternatives skeleton", "paper/06-mcp-vs-alternatives.md", "Alternatives comparison skeleton."),
        ("AI Hub skeleton", "paper/09-government-local-authority-ai-hub.md", "Government/local authority risk and control mapping."),
        ("Source register", "sources/source-register.md", "Source-note status map."),
        ("Official specs", "sources/official-specs.md", "Primary MCP source notes."),
        ("Security research", "sources/security-research.md", "Security source notes."),
        ("Vendor adoption", "sources/vendor-adoption.md", "Vendor and control-depth source notes."),
        ("Wiki index", "wiki/index.md", "LLM-Wiki entry point."),
        ("Completion dashboard", "wiki/progress/completion-dashboard.md", "Current progress dashboard."),
        ("Parallel work plan", "wiki/progress/parallel-work-plan.md", "Safe parallel write scopes."),
        ("Drift investigation", "wiki/evals/drift-investigation.md", "Coordination-drift analysis."),
        ("Post-integration evaluation", "wiki/evals/next-step-parallelism-post-integration-test.md", "Latest wiki-guidance evaluation."),
        ("Project summary report", "reports/mcp_research_codex_project_summary_2026-04-29.md", "Public aggregate Codex metrics."),
    ]
    artifacts: list[dict[str, Any]] = []
    for title, path, evidence in raw:
        artifacts.append(
            {
                "id": _slug(title),
                "title": title,
                "path": path,
                "public_url": _blob_url(repo_url, baseline_commit, path),
                "evidence": evidence,
                "publication_status": "public",
            }
        )
    return artifacts


def _decisions() -> list[dict[str, str]]:
    return [
        {
            "id": "private-public-split",
            "decision": "Keep raw assistant transcript evidence in ignored postmortem/ and publish only redacted registers and synthesis.",
            "reason": "The skill requires a full audit archive while keeping raw prompts, local paths, and transcript bodies out of GitHub.",
            "evidence": "skills/assistant-postmortem-wiki/SKILL.md",
        },
        {
            "id": "source-first-paper",
            "decision": "Delay full report prose until source notes and section-level acceptance criteria are stable.",
            "reason": "The project started from a failed deep-research report and needed citation discipline before prose.",
            "evidence": "wiki/guidance/source-discipline.md",
        },
        {
            "id": "llm-wiki",
            "decision": "Use a linked LLM-Wiki for guidance, progress, evaluation, and close procedures.",
            "reason": "Large agent files and session context were becoming too broad; small linked notes support targeted retrieval.",
            "evidence": "wiki/index.md",
        },
        {
            "id": "machine-readable-state",
            "decision": "Track paper progress and source TODOs in JSON registers.",
            "reason": "Prose-only progress tracking caused drift after parallel worker lanes.",
            "evidence": "wiki/data/progress-register.json and wiki/data/source-todo-register.json",
        },
        {
            "id": "parallel-workers",
            "decision": "Split source-note and section-skeleton work into disjoint worker lanes, then integrate centrally.",
            "reason": "Context limits made broad single-agent source extraction brittle.",
            "evidence": "wiki/progress/parallel-work-plan.md",
        },
    ]


def _phase_rows() -> list[dict[str, str]]:
    return [
        {"id": "scaffold", "title": "Repository and method scaffold", "status": "complete"},
        {"id": "official-specs", "title": "Primary-source MCP foundation", "status": "source-ready for section 02"},
        {"id": "parallel-source-lanes", "title": "Parallel source-note and section skeleton lanes", "status": "integrated"},
        {"id": "wiki-evaluation", "title": "LLM-Wiki guidance evaluation", "status": "active"},
        {"id": "postmortem", "title": "Assistant postmortem wiki", "status": "created"},
    ]


def _metrics_by_session_id() -> dict[str, Any]:
    return {
        parsed.session_id: parsed
        for path in _discover_session_files(CODEX_HOME)
        if (parsed := _parse_session_file(path, REPO_FILTER)) is not None
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def _session_title(session: dict[str, Any]) -> str:
    nickname = str(session.get("agent_nickname") or "").strip()
    role = str(session.get("agent_role") or "").strip()
    if nickname and role:
        return f"{nickname} {role} session"
    if nickname:
        return f"{nickname} session"
    if session.get("is_subagent"):
        return "Unnamed subagent session"
    return "Main Codex session"


def _session_page_name(session: dict[str, Any], index: int) -> str:
    session_id = str(session["session_id"])
    start = str(session.get("start_iso") or "")[:10].replace("-", "")
    return f"{index:04d}-{start}-{session_id[-8:]}.md"


def _copy_private_sources(summary: dict[str, Any], metrics_by_id: dict[str, Any]) -> list[dict[str, Any]]:
    source_dir = PRIVATE_DIR / "sources" / "conversations"
    source_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for index, public_session in enumerate(summary["sessions"], start=1):
        session_id = str(public_session["session_id"])
        metrics = metrics_by_id.get(session_id)
        if metrics is None:
            continue
        source = Path(metrics.file_path)
        target = source_dir / f"{index:04d}-{session_id}.jsonl"
        shutil.copy2(source, target)
        rows.append(
            {
                "session_id": session_id,
                "source_path": str(source),
                "private_copy": str(target.relative_to(PRIVATE_DIR)),
                "start_iso": metrics.start_iso,
                "end_iso": metrics.end_iso,
                "agent_nickname": metrics.agent_nickname,
                "agent_role": metrics.agent_role,
            }
        )
    return rows


def _build_private_archive(summary: dict[str, Any], metrics_by_id: dict[str, Any]) -> None:
    _reset_dir(PRIVATE_DIR)
    rows = _copy_private_sources(summary, metrics_by_id)
    _write_json(PRIVATE_DIR / "wiki" / "data" / "private_session_sources.json", rows)
    _write_text(
        PRIVATE_DIR / "README.md",
        "\n".join(
            [
                "# Private Assistant Postmortem Archive",
                "",
                "This directory is intentionally ignored by Git.",
                "",
                "It contains local-only Codex rollout JSONL copies and private source registers used to regenerate or audit the public postmortem derivative.",
                "",
                "- Public derivative: `../postmortem-public/wiki/index.md`",
                "- Private session source register: `wiki/data/private_session_sources.json`",
                "- Raw conversation copies: `sources/conversations/`",
            ]
        ),
    )


def _new_turn(
    *,
    turn_index: int,
    session_turn_index: int,
    session: dict[str, Any],
    timestamp: str,
    turn_position: str,
) -> dict[str, Any]:
    return {
        "id": f"turn-{turn_index:04d}",
        "turn_number": turn_index,
        "session_turn_number": session_turn_index,
        "turn_position": turn_position,
        "session_id": session["session_id"],
        "title": f"{_session_title(session)} turn {session_turn_index}",
        "public_page": f"turns/turn-{turn_index:04d}.md",
        "first_timestamp": timestamp,
        "last_timestamp": timestamp,
        "user_messages": 0,
        "assistant_messages": 0,
        "tool_calls": 0,
        "tool_outputs": 0,
        "context_events": 0,
        "tool_names": {},
    }


def _finish_exchange(turn: dict[str, Any], exchange_index: int) -> dict[str, Any]:
    exchange_id = f"exchange-{exchange_index:04d}"
    summary_parts = [
        f"{turn['user_messages']} user message(s)",
        f"{turn['assistant_messages']} assistant message(s)",
        f"{turn['tool_calls']} tool call(s)",
        f"{turn['tool_outputs']} tool output(s)",
    ]
    if turn["context_events"]:
        summary_parts.append(f"{turn['context_events']} context event(s)")
    return {
        "id": exchange_id,
        "turn_id": turn["id"],
        "session_id": turn["session_id"],
        "title": f"{turn['title']} exchange",
        "public_page": f"exchanges/{exchange_id}.md",
        "kind": "redacted-turn-summary",
        "publication_status": "public-redacted",
        "content_status": "raw content private; public page contains structural counts only",
        "first_timestamp": turn["first_timestamp"],
        "last_timestamp": turn["last_timestamp"],
        "summary": "; ".join(summary_parts),
        "user_messages": turn["user_messages"],
        "assistant_messages": turn["assistant_messages"],
        "tool_calls": turn["tool_calls"],
        "tool_outputs": turn["tool_outputs"],
        "context_events": turn["context_events"],
        "tool_names": sorted(turn["tool_names"]),
    }


def _extract_turns_and_exchanges(
    summary: dict[str, Any],
    metrics_by_id: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    turns: list[dict[str, Any]] = []
    exchanges: list[dict[str, Any]] = []
    turn_index = 0
    exchange_index = 0

    for session in summary["sessions"]:
        session_id = str(session["session_id"])
        metrics = metrics_by_id.get(session_id)
        current_turn: dict[str, Any] | None = None
        session_turn_index = 0

        def start_turn(timestamp: str, turn_position: str, session_for_turn: dict[str, Any]) -> dict[str, Any]:
            nonlocal turn_index, session_turn_index
            turn_index += 1
            session_turn_index += 1
            return _new_turn(
                turn_index=turn_index,
                session_turn_index=session_turn_index,
                session=session_for_turn,
                timestamp=timestamp,
                turn_position=turn_position,
            )

        def close_turn() -> None:
            nonlocal current_turn, exchange_index
            if current_turn is None:
                return
            exchange_index += 1
            exchange = _finish_exchange(current_turn, exchange_index)
            current_turn["exchange_id"] = exchange["id"]
            current_turn["exchange_page"] = exchange["public_page"]
            turns.append(current_turn)
            exchanges.append(exchange)
            current_turn = None

        if metrics is not None:
            for record in _read_jsonl(Path(metrics.file_path)):
                timestamp = str(record.get("timestamp") or "")
                record_type = record.get("type")
                raw_payload = record.get("payload")
                payload: dict[str, Any] = raw_payload if isinstance(raw_payload, dict) else {}

                if record_type == "response_item":
                    response_type = payload.get("type")
                    if response_type == "message":
                        role = str(payload.get("role") or "")
                        if role == "user":
                            text = _extract_user_text(payload)
                            if _is_bootstrap_message(text):
                                continue
                            close_turn()
                            current_turn = start_turn(timestamp, "user-prompt", session)
                            current_turn["user_messages"] += 1
                        elif role == "assistant":
                            if current_turn is None:
                                current_turn = start_turn(timestamp, "pre-user-context", session)
                            current_turn["assistant_messages"] += 1
                        else:
                            if current_turn is None:
                                current_turn = start_turn(timestamp, "pre-user-context", session)
                            current_turn["context_events"] += 1
                        current_turn["last_timestamp"] = timestamp
                        continue

                    if response_type in {"function_call", "custom_tool_call", "web_search_call"}:
                        if current_turn is None:
                            current_turn = start_turn(timestamp, "pre-user-context", session)
                        current_turn["tool_calls"] += 1
                        name = str(payload.get("name") or ("web_search" if response_type == "web_search_call" else "unknown"))
                        current_turn["tool_names"][name] = current_turn["tool_names"].get(name, 0) + 1
                        current_turn["last_timestamp"] = timestamp
                        continue

                    if response_type in {"function_call_output", "custom_tool_call_output"}:
                        if current_turn is None:
                            current_turn = start_turn(timestamp, "pre-user-context", session)
                        current_turn["tool_outputs"] += 1
                        current_turn["last_timestamp"] = timestamp
                        continue

                if record_type == "compacted" or (
                    record_type == "event_msg" and payload.get("type") == "context_compacted"
                ):
                    if current_turn is None:
                        current_turn = start_turn(timestamp, "pre-user-context", session)
                    current_turn["context_events"] += 1
                    current_turn["last_timestamp"] = timestamp

        close_turn()

        if session_turn_index == 0:
            current_turn = start_turn(str(session.get("start_iso") or ""), "session-summary", session)
            current_turn["context_events"] = 1
            close_turn()

    return turns, exchanges


def _public_lint(public_root: Path) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    md_files = sorted(public_root.rglob("*.md"))
    markdown_link_re = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")

    required_data = [
        "publication_lint.json",
        "graph_nodes.json",
        "graph_edges.json",
        "facets.json",
        "sources.json",
        "exchanges.json",
        "turns.json",
        "sessions.json",
        "artifacts.json",
        "decisions.json",
    ]
    for filename in required_data:
        path = public_root / "wiki" / "data" / filename
        if not path.exists():
            errors.append({"type": "missing_data_file", "file": str(path.relative_to(public_root))})

    for path in md_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(public_root).as_posix()
        errors.extend(
            {"type": "private_path_leak", "file": rel, "marker": marker}
            for marker in ("/Users/", ".codex/", "postmortem/sources/conversations")
            if marker in text
        )
        errors.extend(
            {"type": "raw_html_folding", "file": rel, "marker": marker}
            for marker in ("<details", "<summary")
            if marker in text.lower()
        )
        for line_number, line in enumerate(text.splitlines(), start=1):
            if "|" in line and "[[" in line:
                errors.append({"type": "wikilink_in_table", "file": rel, "line": str(line_number)})
        for match in markdown_link_re.finditer(text):
            target = match.group(1).strip()
            if not target or re.match(r"^[a-z]+:", target):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(public_root.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append({"type": "broken_markdown_link", "file": rel, "target": target})

    return {
        "generated": _now(),
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "markdown_files_checked": len(md_files),
            "errors": len(errors),
            "warnings": len(warnings),
        },
    }


def _build_public_wiki(
    summary: dict[str, Any],
    artifacts: list[dict[str, Any]],
    baseline_commit: str,
    metrics_by_id: dict[str, Any],
) -> None:
    _reset_dir(PUBLIC_DIR)
    generated = _now()
    stats = summary["summary"]
    repo_state = summary["repo_state"]
    decisions = _decisions()
    phases = _phase_rows()

    session_pages: list[dict[str, Any]] = []
    for index, session in enumerate(summary["sessions"], start=1):
        filename = _session_page_name(session, index)
        title = _session_title(session)
        session_pages.append({**session, "public_page": f"sessions/{filename}", "title": title, "turn_id": f"turn-{index:04d}"})

    turns, exchanges = _extract_turns_and_exchanges({"sessions": session_pages}, metrics_by_id)
    sources = [
        {
            "id": "local-codex-session-logs",
            "title": "Local Codex session logs",
            "public_page": "sources/local-codex-session-logs.md",
            "public_status": "sanitized metadata only",
            "private_status": "raw JSONL copies in ignored local archive",
        }
    ]

    artifact_pages = []
    for artifact in artifacts:
        filename = f"{artifact['id']}.md"
        artifact_pages.append({**artifact, "public_page": f"artifacts/{filename}"})

    graph_nodes: list[dict[str, str]] = [{"id": "index", "label": "Postmortem index", "kind": "index"}]
    graph_edges: list[dict[str, str]] = []
    for row in session_pages:
        graph_nodes.append({"id": f"session:{row['session_id']}", "label": row["title"], "kind": "session"})
        graph_edges.append({"source": "index", "target": f"session:{row['session_id']}", "kind": "contains"})
    for turn in turns:
        graph_nodes.append({"id": f"turn:{turn['id']}", "label": turn["title"], "kind": "turn"})
        graph_edges.append({"source": f"session:{turn['session_id']}", "target": f"turn:{turn['id']}", "kind": "contains"})
    for exchange in exchanges:
        graph_nodes.append({"id": f"exchange:{exchange['id']}", "label": exchange["title"], "kind": "exchange"})
        graph_edges.append({"source": f"turn:{exchange['turn_id']}", "target": f"exchange:{exchange['id']}", "kind": "summarizes"})
    for artifact in artifact_pages:
        graph_nodes.append({"id": f"artifact:{artifact['id']}", "label": artifact["title"], "kind": "artifact"})
        graph_edges.append({"source": "index", "target": f"artifact:{artifact['id']}", "kind": "evidences"})
    for source in sources:
        graph_nodes.append({"id": f"source:{source['id']}", "label": source["title"], "kind": "source"})
        graph_edges.append({"source": "index", "target": f"source:{source['id']}", "kind": "documents"})

    facets = {
        "phases": phases,
        "topics": [
            {"id": "source-discipline", "title": "Source discipline"},
            {"id": "parallel-work", "title": "Parallel work"},
            {"id": "semantic-drift", "title": "Semantic drift"},
            {"id": "public-private-split", "title": "Public/private split"},
        ],
        "kinds": [
            {"id": "session-summary", "title": "Session summary"},
            {"id": "turn-summary", "title": "Turn summary"},
            {"id": "redacted-turn-summary", "title": "Redacted turn summary"},
            {"id": "repository-artifact", "title": "Repository artifact"},
            {"id": "decision", "title": "Decision"},
        ],
    }
    roles = sorted({str(row.get("agent_role") or "main") for row in session_pages})
    entities = [
        {"id": "codex", "title": "Codex"},
        {"id": "mcp-research", "title": "mcp-research"},
        {"id": "llm-wiki", "title": "LLM-Wiki"},
    ]
    facets["roles"] = [{"id": _slug(role), "title": role} for role in roles]
    facets["entities"] = entities
    facets["turn_positions"] = [
        {"id": "user-prompt", "title": "User prompt"},
        {"id": "pre-user-context", "title": "Pre-user context"},
        {"id": "session-summary", "title": "Session summary"},
    ]

    _write_json(PUBLIC_WIKI / "data" / "sessions.json", session_pages)
    _write_json(PUBLIC_WIKI / "data" / "turns.json", turns)
    _write_json(PUBLIC_WIKI / "data" / "exchanges.json", exchanges)
    _write_json(PUBLIC_WIKI / "data" / "sources.json", sources)
    _write_json(PUBLIC_WIKI / "data" / "artifacts.json", artifact_pages)
    _write_json(PUBLIC_WIKI / "data" / "decisions.json", decisions)
    _write_json(PUBLIC_WIKI / "data" / "facets.json", facets)
    _write_json(PUBLIC_WIKI / "data" / "graph_nodes.json", graph_nodes)
    _write_json(PUBLIC_WIKI / "data" / "graph_edges.json", graph_edges)

    _write_text(
        PUBLIC_DIR / "AGENTS.md",
        "\n".join(
            [
                "# Public Postmortem Rules",
                "",
                "- Do not add raw Codex JSONL, local filesystem paths, or private transcript bodies to this public derivative.",
                "- Use standard Markdown links, not table-hostile aliased wikilinks.",
                "- Keep local-only evidence marked as private-only in the publication decision register.",
                "- Regenerate with `uv run python scripts/build_postmortem_wiki.py` rather than hand-editing registers.",
            ]
        ),
    )

    session_links = "\n".join(
        f"- {_link(row['title'], row['public_page'])}: `{row['session_id']}`" for row in session_pages[:10]
    )
    if len(session_pages) > 10:
        session_links += f"\n- ... {len(session_pages) - 10} more sessions in [sessions.json](data/sessions.json)."

    _write_text(
        PUBLIC_WIKI / "index.md",
        "\n".join(
            [
                "# MCP Research Assistant Postmortem",
                "",
                f"Generated: `{generated}`",
                f"Baseline commit for artifact permalinks: `{baseline_commit}`",
                "",
                "This is the public-safe derivative of the assistant collaboration postmortem. The full raw archive is local-only in ignored `postmortem/`.",
                "",
                "## Navigation",
                "",
                "- [Postmortem synthesis](postmortem.md)",
                "- [Conversation summary](conversation-summary.md)",
                "- [Repository evidence](repository-evidence.md)",
                "- [Decision register](decisions.md)",
                "- [Methodology](methodology.md)",
                "- [Publication decisions](publication.md)",
                "- [Timeline](timeline.md)",
                "- [Surrogate catalogue](surrogate-catalogue.md)",
                "- [Public source boundary](sources/local-codex-session-logs.md)",
                "- [Exchange register](data/exchanges.json)",
                "- [Publication lint](data/publication_lint.json)",
                "",
                "## Session Entry Points",
                "",
                session_links,
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "postmortem.md",
        "\n".join(
            [
                "# Postmortem Synthesis",
                "",
                "## What Happened",
                "",
                "The project converted a failed deep-research report into a controlled Markdown/LaTeX paper project with structured source notes, a build path, validation scripts, and an LLM-Wiki for guidance and progress tracking.",
                "",
                "The assistant workflow then moved from broad drafting toward source-first scaffolding, parallel evidence lanes, and repeated wiki-guidance evaluations.",
                "",
                "## What Worked",
                "",
                "- The LLM-Wiki reduced context load by separating source discipline, progress, acceptance criteria, and evaluation records.",
                "- Parallel worker lanes worked when write scopes were explicit and the main thread owned shared integration files.",
                "- Citation and wiki-state validation caught missing BibTeX entries, broken links, incomplete section tracking, and source TODO register gaps.",
                "",
                "## What Failed Or Drifted",
                "",
                "- Prose guidance drifted after parallel work, especially current-state statements in wiki guidance.",
                "- Source-note TODOs were initially prose-only, making blocker state hard to validate.",
                "- The full report remains intentionally undrafted; source readiness is still incomplete for sections 04, 06, and 09.",
                "",
                "## Current Risk",
                "",
                "Semantic drift remains the largest workflow risk. Structural validators now catch many file/register errors, but stale guidance prose still needs a dedicated alignment check.",
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "conversation-summary.md",
        "\n".join(
            [
                "# Conversation Summary",
                "",
                "This page uses aggregate telemetry and redacted session metadata only. Raw prompts and transcript bodies remain private.",
                "",
                "| Metric | Value |",
                "| --- | --- |",
                f"| Sessions included | `{stats['session_count']}` |",
                f"| Redacted turn summaries | `{len(turns)}` |",
                f"| Redacted exchange summaries | `{len(exchanges)}` |",
                f"| Subagent sessions | `{stats['subagent_sessions']}` |",
                f"| Active runtime | `{stats['active_runtime_hours']:.1f}h` |",
                f"| Wall-clock span | `{stats['wall_clock_span_hours']:.1f}h` |",
                f"| Token usage | `{_human_int(stats['total_tokens'])}` |",
                f"| Tool calls | `{_human_int(stats['tool_calls'])}` |",
                f"| Patch lines added | `{_human_int(stats['apply_patch_lines_added'])}` |",
                f"| Context compactions | `{stats['context_compactions']}` |",
                "",
                "## Repository State At Generation",
                "",
                "| Metric | Value |",
                "| --- | --- |",
                f"| Commits | `{repo_state['commit_count']}` |",
                f"| Tracked files | `{repo_state['tracked_files']}` |",
                f"| Paper sections | `{repo_state['paper_sections']}` |",
                f"| Source notes | `{repo_state['source_notes']}` |",
                f"| Wiki pages | `{repo_state['wiki_pages']}` |",
                f"| Wiki validation | `{repo_state['wiki_validation_status']}` |",
            ]
        ),
    )

    artifact_table = "\n".join(
        "| {} | {} | {} |".format(
            _table_cell(_link(artifact["title"], artifact["public_page"])),
            _table_cell(artifact["path"]),
            _table_cell(_link("GitHub permalink", artifact["public_url"])),
        )
        for artifact in artifact_pages
    )
    _write_text(
        PUBLIC_WIKI / "repository-evidence.md",
        "\n".join(
            [
                "# Repository Evidence",
                "",
                "| Artifact | Path | Public permalink |",
                "| --- | --- | --- |",
                artifact_table,
            ]
        ),
    )

    decision_table = "\n".join(
        f"| `{row['id']}` | {_table_cell(row['decision'])} | {_table_cell(row['reason'])} | {_table_cell(row['evidence'])} |"
        for row in decisions
    )
    _write_text(
        PUBLIC_WIKI / "decisions.md",
        "\n".join(
            [
                "# Decision Register",
                "",
                "| ID | Decision | Reason | Evidence |",
                "| --- | --- | --- | --- |",
                decision_table,
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "methodology.md",
        "\n".join(
            [
                "# Methodology",
                "",
                "The postmortem follows the local `assistant-postmortem-wiki` skill:",
                "",
                "- keep a full private archive out of Git;",
                "- publish a redacted derivative;",
                "- use commit-specific permalinks for repository artifacts;",
                "- validate public rendering and private-data leakage risks;",
                "- prefer regeneration from repository artifacts and local Codex session metadata.",
                "",
                "Raw conversation bodies are not published. Public session pages expose sanitized metrics and structural evidence only.",
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "publication.md",
        "\n".join(
            [
                "# Publication Decisions",
                "",
                "| Evidence class | Public status | Rationale |",
                "| --- | --- | --- |",
                "| Raw Codex rollout JSONL | Private only | Contains prompts, tool calls, local paths, and full transcript bodies. |",
                "| Session metrics | Public | Sanitized aggregate and per-session telemetry does not expose raw prompts. |",
                "| Repository artifacts | Public | Already tracked in the public repository and linked by commit-specific permalinks. |",
                "| Local filesystem paths | Redacted | Public derivative uses `<codex_home>` and repository-relative paths. |",
                "| Third-party source bodies | Excluded | Source-note citations are enough for this postmortem; full copied bodies are not republished. |",
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "timeline.md",
        "\n".join(
            [
                "# Timeline",
                "",
                "| Phase | Status |",
                "| --- | --- |",
                *[
                    "| {} | `{}` |".format(
                        _table_cell(_link(phase["title"], f"phases/{phase['id']}.md")),
                        _table_cell(phase["status"]),
                    )
                    for phase in phases
                ],
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "surrogate-catalogue.md",
        "\n".join(
            [
                "# Surrogate Catalogue",
                "",
                "Public session and turn pages are surrogates for private transcript evidence. They preserve order, metadata, and links without exposing raw prompts.",
                "",
                "| Turn | Exchange | Session | Role |",
                "| --- | --- | --- | --- |",
                *[
                    "| {} | {} | {} | `{}` |".format(
                        _table_cell(_link(str(turn["turn_number"]), turn["public_page"])),
                        _table_cell(_link(turn["exchange_id"], f"exchanges/{turn['exchange_id']}.md")),
                        _table_cell(
                            _link(
                                next(row["title"] for row in session_pages if row["session_id"] == turn["session_id"]),
                                next(row["public_page"] for row in session_pages if row["session_id"] == turn["session_id"]),
                            )
                        ),
                        _table_cell(next((row.get("agent_role") or "main") for row in session_pages if row["session_id"] == turn["session_id"])),
                    )
                    for turn in turns
                ],
            ]
        ),
    )

    _write_text(
        PUBLIC_WIKI / "sources" / "local-codex-session-logs.md",
        "\n".join(
            [
                "# Local Codex Session Logs",
                "",
                "The private archive contains local Codex rollout JSONL copies for audit. The public derivative publishes only sanitized metrics and session surrogates.",
                "",
                "- Private source location: ignored local postmortem archive",
                "- Private source register: `postmortem/wiki/data/private_session_sources.json`",
                "- Public session register: [sessions.json](../data/sessions.json)",
            ]
        ),
    )

    for row in session_pages:
        session_turns = [turn for turn in turns if turn["session_id"] == row["session_id"]]
        turn_links = "\n".join(
            f"- {_link(turn['title'], '../' + turn['public_page'])}: `{turn['exchange_id']}`"
            for turn in session_turns[:20]
        )
        if len(session_turns) > 20:
            turn_links += f"\n- ... {len(session_turns) - 20} more turns in [turns.json](../data/turns.json)."
        _write_text(
            PUBLIC_WIKI / row["public_page"],
            "\n".join(
                [
                    f"# {row['title']}",
                    "",
                    f"- Session id: `{row['session_id']}`",
                    f"- Source path: `{row['file_path']}`",
                    f"- Start: `{row['start_iso']}`",
                    f"- End: `{row['end_iso']}`",
                    f"- Role: `{row.get('agent_role') or 'main'}`",
                    f"- Tool calls: `{row['tool_calls']}`",
                    f"- Patch calls: `{row['patch_calls']}`",
                    f"- Tokens: `{_human_int(row['total_tokens'])}`",
                    f"- Turn register id: `{row['turn_id']}`",
                    "",
                    "Transcript detail is private-only. This public page preserves sanitized structure and telemetry.",
                    "",
                    "## Redacted Turns",
                    "",
                    turn_links or "- No public turn surrogates.",
                    "",
                    "[Back to index](../index.md)",
                ]
            ),
        )

    for turn in turns:
        session = next(row for row in session_pages if row["session_id"] == turn["session_id"])
        exchange = next(row for row in exchanges if row["id"] == turn["exchange_id"])
        _write_text(
            PUBLIC_WIKI / "turns" / f"{turn['id']}.md",
            "\n".join(
                [
                    f"# Turn {turn['turn_number']}: {turn['title']}",
                    "",
                    f"- Turn id: `{turn['id']}`",
                    f"- Turn position: `{turn['turn_position']}`",
                    f"- Session: {_link(session['title'], '../' + session['public_page'])}",
                    f"- Session id: `{turn['session_id']}`",
                    f"- Exchange: {_link(exchange['id'], '../' + exchange['public_page'])}",
                    f"- User messages: `{turn['user_messages']}`",
                    f"- Assistant messages: `{turn['assistant_messages']}`",
                    f"- Tool calls: `{turn['tool_calls']}`",
                    f"- Tool outputs: `{turn['tool_outputs']}`",
                    "",
                    "This public turn is a surrogate for the private user prompt, assistant response, and tool evidence sequence in the local archive.",
                    "",
                    "[Back to surrogate catalogue](../surrogate-catalogue.md)",
                ]
            ),
        )

    for exchange in exchanges:
        session = next(row for row in session_pages if row["session_id"] == exchange["session_id"])
        turn = next(row for row in turns if row["id"] == exchange["turn_id"])
        tool_names = ", ".join(exchange["tool_names"]) if exchange["tool_names"] else "none recorded"
        _write_text(
            PUBLIC_WIKI / exchange["public_page"],
            "\n".join(
                [
                    f"# {exchange['title']}",
                    "",
                    f"- Exchange id: `{exchange['id']}`",
                    f"- Kind: `{exchange['kind']}`",
                    f"- Publication status: `{exchange['publication_status']}`",
                    f"- Content status: {exchange['content_status']}",
                    f"- Turn: {_link(turn['title'], '../' + turn['public_page'])}",
                    f"- Session: {_link(session['title'], '../' + session['public_page'])}",
                    f"- First timestamp: `{exchange['first_timestamp']}`",
                    f"- Last timestamp: `{exchange['last_timestamp']}`",
                    f"- Summary: {exchange['summary']}",
                    f"- Tool names: `{tool_names}`",
                    "",
                    "Raw prompt, assistant response, and tool payload text are private-only in the local archive.",
                    "",
                    "[Back to surrogate catalogue](../surrogate-catalogue.md)",
                ]
            ),
        )

    for artifact in artifact_pages:
        _write_text(
            PUBLIC_WIKI / artifact["public_page"],
            "\n".join(
                [
                    f"# {artifact['title']}",
                    "",
                    f"- Repository path: `{artifact['path']}`",
                    f"- Evidence role: {artifact['evidence']}",
                    f"- Public permalink: {_link('GitHub', artifact['public_url'])}",
                    f"- Publication status: `{artifact['publication_status']}`",
                    "",
                    "[Back to repository evidence](../repository-evidence.md)",
                ]
            ),
        )

    for phase in phases:
        _write_text(
            PUBLIC_WIKI / "phases" / f"{phase['id']}.md",
            "\n".join(
                [
                    f"# {phase['title']}",
                    "",
                    f"- Status: `{phase['status']}`",
                    "",
                    "[Back to index](../index.md)",
                ]
            ),
        )

    for topic in facets["topics"]:
        _write_text(
            PUBLIC_WIKI / "topics" / f"{topic['id']}.md",
            f"# {topic['title']}\n\n[Back to index](../index.md)",
        )

    for role in facets["roles"]:
        role_sessions = [row for row in session_pages if _slug(str(row.get("agent_role") or "main")) == role["id"]]
        rows = "\n".join(f"- {_link(row['title'], '../' + row['public_page'])}" for row in role_sessions)
        _write_text(
            PUBLIC_WIKI / "roles" / f"{role['id']}.md",
            f"# {role['title']}\n\n{rows or '- No sessions.'}\n\n[Back to index](../index.md)",
        )

    for kind in facets["kinds"]:
        _write_text(
            PUBLIC_WIKI / "kinds" / f"{kind['id']}.md",
            f"# {kind['title']}\n\n[Back to index](../index.md)",
        )

    for entity in facets["entities"]:
        _write_text(
            PUBLIC_WIKI / "entities" / f"{entity['id']}.md",
            f"# {entity['title']}\n\n[Back to index](../index.md)",
        )

    for turn_position in facets["turn_positions"]:
        _write_text(
            PUBLIC_WIKI / "turn-positions" / f"{turn_position['id']}.md",
            f"# {turn_position['title']}\n\n[Back to surrogate catalogue](../surrogate-catalogue.md)",
        )

    _write_json(
        PUBLIC_WIKI / "data" / "publication_lint.json",
        {"generated": _now(), "status": "pending", "errors": [], "warnings": []},
    )
    lint = _public_lint(PUBLIC_DIR)
    _write_json(PUBLIC_WIKI / "data" / "publication_lint.json", lint)
    if lint["status"] != "pass":
        raise SystemExit("Public postmortem lint failed; see postmortem-public/wiki/data/publication_lint.json")


def main() -> int:
    baseline_commit = _git_output(["rev-parse", "HEAD"]) or "HEAD"
    repo_url = _github_base_url()
    summary = build_summary(CODEX_HOME, REPO_FILTER)
    metrics_by_id = _metrics_by_session_id()
    artifacts = _artifact_inputs(repo_url, baseline_commit)

    _build_private_archive(summary, metrics_by_id)
    _build_public_wiki(summary, artifacts, baseline_commit, metrics_by_id)

    print(f"Built private postmortem archive: {PRIVATE_DIR.relative_to(ROOT)}")
    print(f"Built public postmortem wiki: {PUBLIC_WIKI.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
