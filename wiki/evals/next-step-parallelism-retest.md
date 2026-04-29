---
title: "Next Step Parallelism Retest"
note_type: "evaluation-run"
status: "complete"
tags:
  - "evals"
  - "llm-wiki"
  - "parallel-work"
  - "comparison"
related:
  - "next-step-parallelism-test.md"
  - "../index.md"
  - "../progress/plan.md"
  - "../progress/parallel-work-plan.md"
  - "../data/progress-register.json"
  - "../../sources/source-register.md"
---

# Next Step Parallelism Retest

## Question

What should we do next and how much can be run in parallel?

## Context Used

- [Wiki index](../index.md)
- [Previous next-step test](next-step-parallelism-test.md)
- [Authoring contract](../guidance/authoring-contract.md)
- [Section acceptance criteria](../guidance/section-acceptance.md)
- [Project plan](../progress/plan.md)
- [Parallel work plan](../progress/parallel-work-plan.md)
- [Progress register](../data/progress-register.json)
- [Source register](../../sources/source-register.md)
- `uv run python scripts/check_citations.py`
- `uv run python scripts/validate_wiki_state.py`

## Answer Produced

The next step is no longer broad source-note population. The four parallel lanes from the previous test have already produced working source notes and skeletons. The next step is targeted blocker closure: exact source extraction, raw-page recovery, and promotion of sections from `started` toward `source-ready`.

Recommended parallel lanes now:

| Lane | Write scope | Can run now? | Purpose |
| --- | --- | --- | --- |
| Official exact extraction | `sources/official-specs.md`, `paper/02-mcp-in-a-nutshell.md` | Yes, critical path | Close resources, prompts, lifecycle/initialization/capability negotiation, server versioning, and registry limitation blockers. |
| Criticism/discourse extraction | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | Yes | Replace umbrella TODOs with exact source notes for discovery friction, context bloat, token-reduction claims, and positive product leads. |
| Alternatives verification | `sources/alternatives-skills-agents.md`, `paper/06-mcp-vs-alternatives.md` | Yes | Verify Semantic Kernel, OpenAI tools taxonomy, portability evidence, and procurement evidence before final comparison prose. |
| Vendor and FastMCP raw-page recovery | `sources/vendor-adoption.md`, `sources/fastmcp.md` | Yes | Recover exact URLs/text for governance, vendor implementation, FastMCP release, conformance, and adoption leads. |
| Government/local authority risk skeleton | `paper/09-government-local-authority-ai-hub.md` | Partly | Build architecture-option and risk-register structure only; recommendations should wait for accepted evidence. |
| Consolidation | `paper/00-executive-summary.md`, glossary, final references | No | Wait until sections 02, 04, 06, and 09 are source-ready. |

Practical parallelism: run four blocker-closure workers plus one main integrator/validator. A fifth worker can safely start the section 09 risk-register skeleton if capacity exists, but it must not write recommendations or introduce new evidence. The main integrator should retain ownership of `latex/references.bib`, `sources/source-register.md`, `wiki/data/progress-register.json`, and validation reports.

## Comparison With Previous Session

| Dimension | Previous test | Current retest | Evidence |
| --- | --- | --- | --- |
| Next work | Broad source-note population, especially official specs, discourse, vendor/FastMCP, and alternatives. | Targeted exact extraction and blocker closure. | Previous answer in [next-step-parallelism-test.md](next-step-parallelism-test.md); current source register shows all six source files are now `Started`. |
| Parallelism | Three or four source-note workers plus one integrator. | Four blocker-closure workers plus one integrator; optional section 09 skeleton worker. | [Parallel work plan](../progress/parallel-work-plan.md) now defines disjoint write scopes. |
| Tracked sections | Sections 02 and 04 only. | Sections 02, 04, and 06. | [Progress register](../data/progress-register.json) now has three section entries. |
| Source state | Several source files were placeholders. | `discourse-and-criticism`, `vendor-adoption`, `fastmcp`, and `alternatives-skills-agents` are working drafts. | [Source register](../../sources/source-register.md). |
| TODO blockers | Seven TODO citation blockers in section 04. | Twelve TODO citation blockers across sections 02, 04, and 06. | `uv run python scripts/check_citations.py`. |
| Parallelism clarity | Partial, because the previous test found no durable parallel work-plan note. | Pass, because a parallel work-plan note now exists. | Previous evaluation gaps; [parallel-work-plan.md](../progress/parallel-work-plan.md). |
| Progress awareness | Partial, because Phase 1 was stale. | Pass, because Phase 1 is complete and phases 2-4 reflect current started work. | [Project plan](../progress/plan.md). |
| Wiki alignment | Pass with no current errors. | Pass with no current errors. | `uv run python scripts/validate_wiki_state.py`. |

## Evaluation

The wiki performed better than in the first run. It now answered not only "what next" but also "what can safely run in parallel" with explicit ownership boundaries.

| Criterion | Result | Evidence |
| --- | --- | --- |
| Guidance precision | Pass | The answer came from eight compact files plus two validation commands. |
| Context efficiency | Pass | No full paper/source scan was needed to answer the planning question. |
| Source discipline | Pass | The answer distinguishes exact extraction from final prose and keeps TODO keys as blockers. |
| Progress awareness | Pass | Phase status, source-register status, and tracked blockers were all current. |
| Parallelism clarity | Pass | `wiki/progress/parallel-work-plan.md` defines write scopes and shared-file ownership. |
| Evaluation comparability | Pass | The previous run is linked and used as an explicit baseline. |

## Gaps Found

- [Section acceptance criteria](../guidance/section-acceptance.md) still names sections 02 and 04 as priority sections but does not include section 06, even though section 06 is now tracked.
- [Wiki evaluation plan](wiki-evaluation-plan.md) still listed the parallel work-plan note as a future check, although it now exists.
- The progress register tracks paper sections but not source-note raw-page recovery tasks directly; that is acceptable for now, but may become limiting as exact extraction becomes the main work type.

## Follow-Up Changes

- Add this retest to the evaluation plan and wiki index.
- Add section 06 to the section acceptance criteria.
- Mark the parallel work-plan note as implemented in the evaluation plan.
