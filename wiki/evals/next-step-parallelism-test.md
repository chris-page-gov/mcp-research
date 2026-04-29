---
title: "Next Step Parallelism Test"
note_type: "evaluation-run"
status: "complete"
tags:
  - "evals"
  - "llm-wiki"
  - "parallel-work"
related:
  - "../index.md"
  - "../progress/plan.md"
  - "../progress/phase-log.md"
  - "../data/progress-register.json"
  - "../../sources/source-register.md"
---

# Next Step Parallelism Test

## Question

What should we do next and how much can be run in parallel?

## Context Used

- [Wiki index](../index.md)
- [Authoring contract](../guidance/authoring-contract.md)
- [Section acceptance criteria](../guidance/section-acceptance.md)
- [Project plan](../progress/plan.md)
- [Progress register](../data/progress-register.json)
- [Source register](../../sources/source-register.md)

## Answer Produced

The next critical path is to close the primary-source blockers for [paper/02-mcp-in-a-nutshell.md](../../paper/02-mcp-in-a-nutshell.md) before writing full prose. That means strengthening [sources/official-specs.md](../../sources/official-specs.md) around resources, prompts, architecture wording, lifecycle/versioning, and related specification concepts, then updating section 02 within its source boundary.

In parallel, section 04 can keep moving if the work stays source-first. The immediate source task is to populate [sources/discourse-and-criticism.md](../../sources/discourse-and-criticism.md) for discovery and context-bloat criticism, then update [paper/04-technical-critiques-and-mitigations.md](../../paper/04-technical-critiques-and-mitigations.md) with a criticism, evidence, mitigation, and residual-risk matrix. Security claims should remain grounded in [sources/security-research.md](../../sources/security-research.md) and official claims in `sources/official-specs.md`.

Recommended parallel lanes now:

| Lane | Files | Can run now? | Notes |
| --- | --- | --- | --- |
| Primary-source foundation | `sources/official-specs.md`, `paper/02-mcp-in-a-nutshell.md` | Yes, critical path | Keep to official/spec notes only. |
| Criticism and defence | `sources/discourse-and-criticism.md`, `paper/04-technical-critiques-and-mitigations.md` | Yes | Avoid final non-security opinions until discourse notes are populated. |
| Vendor and ecosystem evidence | `sources/vendor-adoption.md`, `sources/fastmcp.md` | Yes | Unblocks positive technical assessments, timeline, and ecosystem claims. |
| Alternatives | `sources/alternatives-skills-agents.md`, later `paper/06-mcp-vs-alternatives.md` | Yes | Can proceed independently if citations stay isolated. |
| Government/local authority analysis | `paper/09-government-local-authority-ai-hub.md` | Partly | Risk-register scaffolding can start; recommendations should wait for official, security, and vendor evidence. |
| Consolidation | `paper/00-executive-summary.md`, glossary, references | Not yet | This should wait until source sections have stable claims. |

Practical limit: run three or four source-note workers in parallel, plus one integrator/validator. Do not allow parallel writes to the same files. The highest-value split is official specs, discourse/criticism, vendor/FastMCP, and alternatives.

## Evaluation

The wiki answered the question from six compact files. It correctly pointed to the current source boundaries, active blockers, and the rule against drafting unsupported prose.

| Criterion | Result | Evidence |
| --- | --- | --- |
| Guidance precision | Pass | The answer used index, two guidance notes, plan, progress register, and source register. |
| Context efficiency | Pass | No paper/source full-text load was needed to answer a planning question. |
| Source discipline | Pass | The answer distinguishes source-note work from later paper drafting. |
| Progress awareness | Partial | The wiki identified active section 02 and 04 blockers, but Phase 1 was stale. |
| Parallelism clarity | Partial | The guidance implied safe parallel lanes but did not contain an explicit parallel work plan. |

## Gaps Found

- [Project plan](../progress/plan.md) still marked Phase 1 as in progress after the repo scaffold, validation scripts, CI, and GitHub publication were complete.
- The wiki has no durable page that maps phases to safe parallel write sets.
- The evaluation plan had future checks that are now partly implemented.

## Follow-Up Changes

- Mark Phase 1 complete in the project plan.
- Add this evaluation run to the evaluation plan.
- Consider adding `wiki/progress/parallel-work-plan.md` once source-note production starts in earnest.
