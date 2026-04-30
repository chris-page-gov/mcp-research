---
title: "Completion Dashboard"
note_type: "dashboard"
status: "active"
tags:
  - "progress"
  - "completion"
  - "llm-wiki"
related:
  - "plan.md"
  - "parallel-work-plan.md"
  - "../data/progress-register.json"
  - "../../sources/source-register.md"
  - "../wiki-state-report.md"
---

# Completion Dashboard

Last reviewed: 2026-04-30.

Use this note for quick progress answers. It is a navigation and status dashboard, not a drafting surface.

## Summary

| Area | State | Completion signal | Next gate |
| --- | --- | --- | --- |
| Repository and method | Complete | CI, build, citation, link, wiki-state, and Node 24 workflow checks pass. | Keep validation green before each push. |
| Source-note base | Started | 6/6 source note files have structured entries; source TODOs are tracked in `wiki/data/source-todo-register.json`. | Promote source files only after open evidence blockers are resolved or explicitly scoped out. |
| Paper sections | In progress | 12/12 paper sections tracked: 1 source-ready, 5 started, 6 placeholders. | Move sections 04, 06, and 09 toward source-ready before consolidation. |
| Citation mechanics | Green | 0 TODO citation keys in paper citations. | Keep source-note citation keys synchronized with BibTeX. |
| Final prose | Not started | Executive summary and consolidation remain pending. | Wait until source-ready sections are stable. |

## Paper Sections

| Section | File | Current state | Main blocker | Next action |
| --- | --- | --- | --- | --- |
| Executive summary | `paper/00-executive-summary.md` | Placeholder | Evidence sections incomplete | Draft last. |
| Introduction and methodology | `paper/01-introduction-methodology.md` | Skeleton | Scope/method prose not drafted | Draft after source discipline stabilizes. |
| MCP in a nutshell | `paper/02-mcp-in-a-nutshell.md` | Source-ready | Needs prose drafting, not more official-spec evidence | Convert to prose when drafting begins. |
| Perceptions and discourse | `paper/03-perceptions-and-discourse.md` | Placeholder | Representative discourse evidence incomplete | Use `sources/discourse-and-criticism.md` after sampling improves. |
| Technical critiques and mitigations | `paper/04-technical-critiques-and-mitigations.md` | Started | Broader discourse sampling; discovery-friction evidence is narrowed to named issue-level evidence | Decide whether named examples are enough or add representative sampling before prose. |
| Timeline and evolution | `paper/05-timeline-and-evolution.md` | Placeholder | Timeline not synthesized | Use official/vendor/FastMCP dated source notes. |
| MCP vs alternatives | `paper/06-mcp-vs-alternatives.md` | Started | Portability and procurement evidence narrowed, not closed | Keep direct comparisons analysis-grade unless AI-specific public-sector evidence is added. |
| Hype vs substance | `paper/07-hype-vs-substance.md` | Placeholder | Evidence sections incomplete | Draft after sections 03, 04, 05, and 06 stabilize. |
| Deeper analyses and case studies | `paper/08-deeper-analyses-and-case-studies.md` | Placeholder | Case-study selection incomplete | Select cases from accepted vendor/security/source notes. |
| Government and Local Authority AI Hub | `paper/09-government-local-authority-ai-hub.md` | Started | Control mapping added; vendor-control, independent-adoption, and procurement evidence remain conditional | Hold final recommendations until residual evidence decisions are made. |
| Open questions and future directions | `paper/10-open-questions-and-future-directions.md` | Placeholder | Depends on unresolved evidence list | Draft after blocker closure decisions. |
| Glossary | `paper/11-glossary.md` | Partial | AI Hub definition incomplete | Update when section 09 terminology stabilizes. |

## Source Notes

| Source file | State | Open blocker summary | Primary next use |
| --- | --- | --- | --- |
| `sources/official-specs.md` | Started, section 02 source-ready | General official-spec notes still include some lower-priority TODOs, but section 02 roots/tasks blocker is closed. | Section 02 prose and section 09 control mapping. |
| `sources/security-research.md` | Started | Vendor/preprint weighting remains to be finalized. | Section 04 and section 09 risk controls. |
| `sources/discourse-and-criticism.md` | Started | Representative sampling remains open; discovery/private-registry criticism is narrowed to issue-level evidence. | Sections 03, 04, and 07. |
| `sources/vendor-adoption.md` | Started | Product-control and independent-adoption evidence are narrowed; SLA, incident, public-sector terms, retention, strict enforcement, and audited adoption gaps remain. | Sections 05, 07, and 09. |
| `sources/fastmcp.md` | Started | Public conformance CI and independent examples now exist; official historical SDK confirmation, formal certification, and audited adoption remain open. | Sections 05, 06, and 07. |
| `sources/alternatives-skills-agents.md` | Started | GOV.UK/NCSC/NIST evidence narrows portability/procurement blockers; direct framework-vs-MCP and AI connector procurement evidence remain absent. | Section 06. |

## Active Evidence Blockers

| Blocker | Current owner file | Status | Decision rule |
| --- | --- | --- | --- |
| `TODO-discourse-criticism-source-notes` | `sources/discourse-and-criticism.md` | Narrowed | Add broader representative sampling or keep claims scoped to named examples. |
| `TODO-discourse-discovery-criticism` | `sources/discourse-and-criticism.md` | Narrowed | Use only issue-level evidence; do not restore the rejected GitHub issue #1683 reading. |
| `TODO-framework-portability-evidence` | `sources/alternatives-skills-agents.md` | Narrowed | Use GOV.UK open-standards evidence as the public-sector baseline; keep framework-vs-MCP comparison analysis-grade. |
| `TODO-proprietary-connector-procurement-evidence` | `sources/alternatives-skills-agents.md` | Narrowed | Use NCSC/NIST evidence for local approval/vetting only; do not claim AI connector marketplace procurement readiness. |
| `TODO-vendor-adoption-independent-use` | `sources/vendor-adoption.md` | Narrowed | Use independent preprints for ecosystem evidence only; do not claim audited vendor product adoption. |
| `TODO-product-control-depth` | `sources/vendor-adoption.md` | Narrowed | Use vendor control evidence conditionally by product path; retain assurance, SLA, incident, retention, and public-sector-term gaps. |
| `TODO-fastmcp-conformance-evidence` | `sources/fastmcp.md` | Narrowed | Treat FastMCP conformance as project-reported unless independent tests/certification are found. |
| `TODO-fastmcp-adoption-evidence` | `sources/fastmcp.md` | Narrowed | Treat stars/downloads/maintainer claims as popularity signals, not production adoption. |

## Current Parallel Capacity

Run these in parallel with disjoint write scopes:

| Lane | Write scope | Priority |
| --- | --- | --- |
| Representative discourse sampling | `sources/discourse-and-criticism.md`, `paper/03-perceptions-and-discourse.md` or `paper/04-technical-critiques-and-mitigations.md` | High if section 03/04 prose starts. |
| Alternatives decision pass | `paper/06-mcp-vs-alternatives.md` | High, but no new source claims unless evidence is added first. |
| Vendor assurance residuals | `sources/vendor-adoption.md`, `paper/09-government-local-authority-ai-hub.md` | High for procurement/recommendation readiness. |
| FastMCP residuals | `sources/fastmcp.md`, later `paper/06-mcp-vs-alternatives.md` or `paper/07-hype-vs-substance.md` | Medium. |

The main integrator owns `latex/references.bib`, `sources/source-register.md`, `wiki/data/progress-register.json`, this dashboard, and generated reports.
