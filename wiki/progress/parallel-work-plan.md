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

## Completed Integration Lanes

These lanes ran in parallel and have been integrated by the main thread. Their non-TODO citation keys have been normalized in `latex/references.bib`.

| Lane | Write scope | Depends on | Can run in parallel? | Integration rule |
| --- | --- | --- | --- | --- |
| Official exact extraction | `sources/official-specs.md`, `paper/02-mcp-in-a-nutshell.md` | Official MCP notes and named official MCP pages | Done | Closed resources, prompts, lifecycle, versioning, and registry limitation placeholders. |
| Criticism/discourse extraction | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | Security notes, official notes, named discourse leads | Done | Preserved the criticism/evidence/mitigation/residual-risk matrix. |
| Vendor and FastMCP raw-page recovery | `sources/vendor-adoption.md`, `sources/fastmcp.md` | Named vendor, governance, and FastMCP leads | Done | Recovered exact URLs/text for main vendor and FastMCP leads. |
| Alternatives verification | `sources/alternatives-skills-agents.md`, `paper/06-mcp-vs-alternatives.md` | Named alternatives notes and official vendor docs | Done | Verified Semantic Kernel, OpenAI tools taxonomy, and app-submission evidence; left portability/procurement blockers narrow. |
| Government/local authority risk skeleton | `paper/09-government-local-authority-ai-hub.md` | Official, security, vendor, and alternatives notes | Done | Added risk-register structure only; recommendations wait for accepted evidence. |
| Roots/tasks official extraction | `sources/official-specs.md`, `paper/02-mcp-in-a-nutshell.md` | Versioned official MCP roots/tasks pages | Done | Closed roots/tasks quotation gaps and promoted section 02 to source-ready. |
| Discovery-friction discourse | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | Registry, GitHub Docs, and project issue leads | Done | Replaced the failed GitHub issue #1683 reading with narrower issue-level discovery/private-registry evidence. |
| Portability/procurement evidence | `sources/alternatives-skills-agents.md`, `paper/06-mcp-vs-alternatives.md` | GOV.UK, NCSC, and NIST public-sector evidence | Done | Narrowed portability/procurement blockers; kept direct AI framework/connector claims analysis-grade. |
| Vendor control-depth evidence | `sources/vendor-adoption.md` | Vendor admin/audit/security/licensing docs and independent preprints | Done | Added product-control depth and independent ecosystem evidence while preserving residual assurance gaps. |
| Section 09 control mapping | `paper/09-government-local-authority-ai-hub.md` | Accepted official, security, vendor, and alternatives notes | Done | Added identity, registry, approval, audit, data, incident, supplier, and procurement control mappings without final recommendations. |
| FastMCP conformance/adoption evidence | `sources/fastmcp.md` | Official conformance framework, FastMCP CI, Cisco, and PNNL/OSTI leads | Done | Added public conformance CI and independent example evidence; formal certification and audited adoption remain open. |

## Next Parallel Lanes

| Lane | Write scope | Depends on | Can run in parallel? | Integration rule |
| --- | --- | --- | --- | --- |
| Representative discourse sampling | `sources/discourse-and-criticism.md`, `paper/03-perceptions-and-discourse.md` or `paper/04-technical-critiques-and-mitigations.md` | Broader public discourse sampling method | Yes | Keep existing discovery evidence scoped unless a representative sampling plan is added. |
| Alternatives decision pass | `paper/06-mcp-vs-alternatives.md` | Current accepted alternatives notes and residual blocker decisions | Yes | Convert narrowed evidence into source-ready analysis without adding unsupported claims. |
| Vendor assurance residuals | `sources/vendor-adoption.md`, `paper/09-government-local-authority-ai-hub.md` | Entitlement-specific SLA, incident, retention, UK/EU terms, and assurance evidence | Yes | Only close `TODO-product-control-depth` if evidence covers the residual assurance gaps. |
| Consolidation | `paper/00-executive-summary.md`, `paper/11-glossary.md`, `latex/references.bib` | Stable section drafts and source registers | No | Run only after source-backed sections settle. |

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
- Add missing non-TODO BibTeX keys recorded in source notes before replacing section placeholders.
- Update `sources/source-register.md` status after source-note files change.
- Update `wiki/data/progress-register.json` for section TODO blockers.
- Run `uv run python scripts/validate_wiki_state.py --write-report`.
- Run `make check`, `make lint`, and `make typecheck`.
- Follow [Session Close Procedure](../guidance/session-close.md) before final response.
