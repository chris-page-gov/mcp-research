---
title: "Next Step Parallelism Post-Integration Test"
note_type: "evaluation-run"
status: "complete"
tags:
  - "evals"
  - "llm-wiki"
  - "parallel-work"
  - "completion"
related:
  - "next-step-parallelism-completion-retest.md"
  - "../index.md"
  - "../AGENTS.md"
  - "../progress/completion-dashboard.md"
  - "../progress/parallel-work-plan.md"
  - "../data/progress-register.json"
  - "../data/source-todo-register.json"
---

# Next Step Parallelism Post-Integration Test

## Question

What should we do next and how much can be run in parallel? Show the progress towards completion.

## Context Used

- [Wiki index](../index.md)
- [Wiki operating rules](../AGENTS.md)
- [Project plan](../progress/plan.md)
- [Parallel work plan](../progress/parallel-work-plan.md)
- [Completion dashboard](../progress/completion-dashboard.md)
- [Progress register](../data/progress-register.json)
- [Source TODO register](../data/source-todo-register.json)
- [Section acceptance criteria](../guidance/section-acceptance.md)
- [Source register](../../sources/source-register.md)
- [Previous completion retest](next-step-parallelism-completion-retest.md)
- `uv run python scripts/check_citations.py`
- `uv run python scripts/validate_wiki_state.py`
- `jq` summaries of section and source TODO status counts
- `rg -n 'TODO-[A-Za-z0-9:_-]+' paper sources wiki`

## Answer Produced

Next work: advance source-ready decisions, not consolidation.

The five-lane blocker pass from the previous test has been implemented. Section 09 control mapping exists; discovery, portability/procurement, vendor-control, adoption, and FastMCP blockers are narrowed rather than fully closed. The next useful step is to decide which narrowed blockers need more evidence and which should remain explicitly caveated in draft prose.

Recommended parallel lanes:

| Lane | Write scope | Can run now? | Purpose | Notes |
| --- | --- | --- | --- | --- |
| Representative discourse sampling | `sources/discourse-and-criticism.md`, then `paper/03-perceptions-and-discourse.md` or `paper/04-technical-critiques-and-mitigations.md` | Yes | Decide whether named discourse examples are enough, or add a light sampling method before sections 03/04. | Do not broaden issue-level discovery evidence beyond what the source notes support. |
| Alternatives decision pass | `paper/06-mcp-vs-alternatives.md` | Yes | Convert the narrowed GOV.UK/NCSC/NIST evidence into a source-ready comparison, keeping framework-vs-MCP and proprietary connector claims analysis-grade. | No new source claims unless `sources/alternatives-skills-agents.md` changes first. |
| Vendor assurance residuals | `sources/vendor-adoption.md`, `paper/09-government-local-authority-ai-hub.md` | Yes | Decide whether to seek entitlement-specific SLA, incident, retention, UK/EU terms, and assurance evidence, or keep product-control claims conditional. | This is the main blocker for final recommendations. |
| FastMCP residuals | `sources/fastmcp.md`, later sections 05/06/07 | Yes, lower priority | Decide whether formal certification/audited adoption evidence is necessary, or keep FastMCP conformance/adoption as project-run and example-based. | Can run independently. |
| Section 02 prose draft | `paper/02-mcp-in-a-nutshell.md` | Optional | Section 02 is source-ready and can be converted into prose without waiting for sections 04/06/09. | Keep it bounded; do not start executive summary or consolidation. |

Practical parallelism: four independent worker lanes plus one optional section 02 prose lane can run without overlapping write scopes. The main integrator should keep ownership of `latex/references.bib`, source/progress registers, dashboard, changelog, and validation reports.

Do not start full report consolidation or the executive summary yet.

## Progress Toward Completion

| Area | Current state | Evidence | Completion implication |
| --- | --- | --- | --- |
| Repository/method | Complete | Public repo, CI, build, citation, link, wiki-state, Node 24 workflow, and close procedure are in place. | Infrastructure is not blocking research progress. |
| Citation mechanics | Green | `check_citations.py`: 64 used keys, 138 BibTeX entries, 0 TODO citation keys. | Citation mechanics are not blocking. |
| Wiki/repo alignment | Green after cleanup | Initial validation found `wiki/.DS_Store`; after removal, validation passes with 0 errors and 0 warnings. | Guidance is usable; metadata-file drift still recurs on macOS. |
| Source TODO tracking | Implemented | `source-todo-register.json`: 25 records, 12 closed and 13 narrowed. | Source gaps are visible and machine-readable. |
| Paper sections | In progress | `progress-register.json`: 12 tracked sections: 1 source-ready, 5 started, 6 placeholders. | The project is still before final prose/consolidation. |
| Source-note base | Started | Source register shows 6/6 planned source-note files started. | Enough source base exists for targeted section work; residual assurance gaps remain. |
| Final prose | Not started | Dashboard and plan keep executive summary and consolidation pending. | Draft section 02 only if a bounded prose lane is desired. |

## Evaluation

The wiki answered the question better than the previous run because the dashboard, progress register, and source TODO register now agree on the shape of the project. The answer was recoverable from compact wiki notes plus validation output.

| Criterion | Result | Evidence |
| --- | --- | --- |
| Guidance precision | Pass | The next lanes came directly from the dashboard and parallel work plan. |
| Completion visibility | Pass | Section counts and source TODO counts are machine-readable. |
| Parallelism clarity | Pass | Four current lanes have mostly disjoint write scopes; section 02 prose is optional and isolated. |
| Source discipline | Pass | The answer keeps narrowed blockers caveated and prevents recommendations from outrunning evidence. |
| Context efficiency | Pass | Full source files were not needed to answer; compact wiki files plus `rg`/validation were enough. |
| Drift detection | Partial | Validation caught `.DS_Store`, but not stale prose in `wiki/AGENTS.md` saying section 09 control mapping was still a blocker. |

## Comparison With Previous Completion Retest

| Dimension | Previous completion retest | Current post-integration test |
| --- | --- | --- |
| Main next step | Run five blocker-closure lanes. | Decide residual blockers and move sections 04/06/09 toward source-ready; optional section 02 prose. |
| Section 09 | Control mapping still needed. | Control mapping exists; recommendations remain gated. |
| Progress register | Newly expanded to all sections. | Still tracks all 12 paper sections. |
| Source TODO register | Newly added. | Stable and validates 25 source TODO markers. |
| Citation state | 64 used keys, 138 BibTeX entries, 0 TODO citation keys. | Same. |
| Wiki validation | Pass after integration. | Pass after `.DS_Store` cleanup. |

## Drift Found And Fixed

- Removed macOS `.DS_Store` files before final validation.
- Updated [Wiki operating rules](../AGENTS.md) so the current-bias line no longer names section 09 control mapping as an active blocker.
- Updated [Project plan](../progress/plan.md) so section 09 control mapping is recorded as present and discovery/private-registry evidence is described as narrowed rather than missing.

## Remaining Gaps

- `scripts/validate_wiki_state.py` catches structural drift, but not semantic stale-guidance statements such as obsolete "current blocker" prose.
- The next improvement should be a lightweight guidance-alignment check that compares active blockers in `source-todo-register.json` and `progress-register.json` against `wiki/AGENTS.md`, the dashboard, and the parallel plan.
- Consolidation and executive-summary drafting remain out of scope until sections 04, 06, and 09 are source-ready or deliberately caveated.
