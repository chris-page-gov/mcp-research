---
title: "Parallel Work Plan"
note_type: "plan"
status: "active"
tags:
  - "progress"
  - "parallel-work"
  - "llm-wiki"
related:
  - "plan.md"
  - "phase-log.md"
  - "../data/progress-register.json"
  - "../../sources/source-register.md"
---

# Parallel Work Plan

Use this note when splitting paper work across agents. Keep each lane source-first and assign disjoint write sets.

## Current Parallel Lanes

| Lane | Write scope | Depends on | Can run in parallel? | Integration rule |
| --- | --- | --- | --- | --- |
| Official specs and section 02 | `sources/official-specs.md`, `paper/02-mcp-in-a-nutshell.md` | Local MCP specification notes and citation file | Yes | Main integrator updates shared citation/progress metadata after review. |
| Criticism and section 04 | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | Security notes, official notes, local discourse notes | Yes | Preserve the criticism/evidence/mitigation/residual-risk matrix. |
| Vendor and FastMCP notes | `sources/vendor-adoption.md`, `sources/fastmcp.md` | Local vendor and framework notes | Yes | Do not draft ecosystem claims until source notes are accepted. |
| Alternatives notes and section 06 | `sources/alternatives-skills-agents.md`, `paper/06-mcp-vs-alternatives.md` | Local alternatives notes and imported citation file | Yes | Keep section 06 as a skeleton until source notes are accepted. |
| Government/local authority analysis | `paper/09-government-local-authority-ai-hub.md` | Official, security, vendor, and alternatives notes | Partly | Risk-register structure can start; recommendations wait for accepted evidence. |
| Consolidation | `paper/00-executive-summary.md`, `paper/11-glossary.md`, `latex/references.bib` | Stable section drafts and source registers | No | Run after source-backed sections settle. |

## Shared Files

Only the main integrator should edit shared coordination files while worker lanes are running:

- `latex/references.bib`
- `sources/source-register.md`
- `wiki/data/progress-register.json`
- `wiki/progress/plan.md`
- `wiki/progress/phase-log.md`
- validation reports under `wiki/`

## Integration Checklist

- Review worker diffs before staging.
- Add missing BibTeX TODO keys only when cited in paper/source files.
- Update `sources/source-register.md` status after source-note files change.
- Update `wiki/data/progress-register.json` for section TODO blockers.
- Run `uv run python scripts/validate_wiki_state.py --write-report`.
- Run `make check`, `make lint`, and `make typecheck`.
