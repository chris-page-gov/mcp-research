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

Last reviewed: 2026-04-29.

Use this note for quick progress answers. It is a navigation and status dashboard, not a drafting surface.

## Summary

| Area | State | Completion signal | Next gate |
| --- | --- | --- | --- |
| Repository and method | Complete | CI, build, citation, link, wiki-state, and Node 24 workflow checks pass. | Keep validation green before each push. |
| Source-note base | Started | 6/6 source note files have structured entries. | Promote source files only after open evidence blockers are resolved or explicitly scoped out. |
| Priority sections | In progress | 1 source-ready, 3 started; 3 priority sections still have evidence or control-mapping blockers. | Move sections 04, 06, and 09 toward source-ready. |
| Citation mechanics | Green | 0 TODO citation keys in paper citations. | Keep source-note citation keys synchronized with BibTeX. |
| Final prose | Not started | Executive summary and consolidation remain pending. | Wait until source-ready sections are stable. |

## Paper Sections

| Section | File | Current state | Main blocker | Next action |
| --- | --- | --- | --- | --- |
| Executive summary | `paper/00-executive-summary.md` | Placeholder | Evidence sections incomplete | Draft last. |
| Introduction and methodology | `paper/01-introduction-methodology.md` | Skeleton | Scope/method prose not drafted | Draft after source discipline stabilizes. |
| MCP in a nutshell | `paper/02-mcp-in-a-nutshell.md` | Source-ready | Needs prose drafting, not more official-spec evidence | Convert to prose when drafting begins. |
| Perceptions and discourse | `paper/03-perceptions-and-discourse.md` | Placeholder | Representative discourse evidence incomplete | Use `sources/discourse-and-criticism.md` after sampling improves. |
| Technical critiques and mitigations | `paper/04-technical-critiques-and-mitigations.md` | Started | Broader discourse sampling and discovery-friction evidence | Close `TODO-discourse-criticism-source-notes` and `TODO-discourse-discovery-criticism`. |
| Timeline and evolution | `paper/05-timeline-and-evolution.md` | Placeholder | Timeline not synthesized | Use official/vendor/FastMCP dated source notes. |
| MCP vs alternatives | `paper/06-mcp-vs-alternatives.md` | Started | Portability and procurement evidence | Close or explicitly scope `TODO-framework-portability-evidence` and `TODO-proprietary-connector-procurement-evidence`. |
| Hype vs substance | `paper/07-hype-vs-substance.md` | Placeholder | Evidence sections incomplete | Draft after sections 03, 04, 05, and 06 stabilize. |
| Deeper analyses and case studies | `paper/08-deeper-analyses-and-case-studies.md` | Placeholder | Case-study selection incomplete | Select cases from accepted vendor/security/source notes. |
| Government and Local Authority AI Hub | `paper/09-government-local-authority-ai-hub.md` | Started | Control mapping, vendor-control evidence, and procurement evidence | Map controls; do not write recommendations yet. |
| Open questions and future directions | `paper/10-open-questions-and-future-directions.md` | Placeholder | Depends on unresolved evidence list | Draft after blocker closure decisions. |
| Glossary | `paper/11-glossary.md` | Partial | AI Hub definition incomplete | Update when section 09 terminology stabilizes. |

## Source Notes

| Source file | State | Open blocker summary | Primary next use |
| --- | --- | --- | --- |
| `sources/official-specs.md` | Started, section 02 source-ready | General official-spec notes still include some lower-priority TODOs, but section 02 roots/tasks blocker is closed. | Section 02 prose and section 09 control mapping. |
| `sources/security-research.md` | Started | Vendor/preprint weighting remains to be finalized. | Section 04 and section 09 risk controls. |
| `sources/discourse-and-criticism.md` | Started | Broader discourse sampling and correct discovery-friction evidence remain open. | Sections 03, 04, and 07. |
| `sources/vendor-adoption.md` | Started | Independent adoption, governance process, and product control-depth evidence remain open. | Sections 05, 07, and 09. |
| `sources/fastmcp.md` | Started | Official historical SDK confirmation, independent conformance, and adoption evidence remain open. | Sections 05, 06, and 07. |
| `sources/alternatives-skills-agents.md` | Started | Portability and public-sector procurement evidence remain open. | Section 06. |

## Active Evidence Blockers

| Blocker | Current owner file | Status | Decision rule |
| --- | --- | --- | --- |
| `TODO-discourse-criticism-source-notes` | `sources/discourse-and-criticism.md` | Narrowed | Add broader representative sampling or keep claims scoped to named examples. |
| `TODO-discourse-discovery-criticism` | `sources/discourse-and-criticism.md` | Open | Find correct evidence or remove the practitioner discovery/private-registry claim. |
| `TODO-framework-portability-evidence` | `sources/alternatives-skills-agents.md` | Open | Add non-vendor evidence or keep portability comparison analysis-grade. |
| `TODO-proprietary-connector-procurement-evidence` | `sources/alternatives-skills-agents.md` | Open | Add public-sector procurement evidence or keep recommendations out. |
| `TODO-vendor-adoption-independent-use` | `sources/vendor-adoption.md` | Open | Do not claim broad adoption without independent usage/deployment evidence. |
| `TODO-product-control-depth` | `sources/vendor-adoption.md` | Open | Do not rely on vendor product controls without audit, tenant, residency, SLA, and support evidence. |
| `TODO-fastmcp-conformance-evidence` | `sources/fastmcp.md` | Narrowed | Treat FastMCP conformance as project-reported unless independent tests/certification are found. |
| `TODO-fastmcp-adoption-evidence` | `sources/fastmcp.md` | Narrowed | Treat stars/downloads/maintainer claims as popularity signals, not production adoption. |

## Current Parallel Capacity

Run these in parallel with disjoint write scopes:

| Lane | Write scope | Priority |
| --- | --- | --- |
| Discovery-friction discourse | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | High |
| Portability/procurement evidence | `sources/alternatives-skills-agents.md`, `paper/06-mcp-vs-alternatives.md` | High |
| Vendor control-depth evidence | `sources/vendor-adoption.md`, `paper/09-government-local-authority-ai-hub.md` | High |
| FastMCP conformance/adoption evidence | `sources/fastmcp.md`, later `paper/06-mcp-vs-alternatives.md` or `paper/07-hype-vs-substance.md` | Medium |
| Section 09 control mapping | `paper/09-government-local-authority-ai-hub.md` | Medium, only from accepted notes |

The main integrator owns `latex/references.bib`, `sources/source-register.md`, `wiki/data/progress-register.json`, this dashboard, and generated reports.
