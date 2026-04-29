---
title: "Drift Investigation"
note_type: "evaluation"
status: "active"
tags:
  - "evals"
  - "drift"
  - "llm-wiki"
related:
  - "next-step-parallelism-test.md"
  - "next-step-parallelism-retest.md"
  - "../guidance/session-close.md"
  - "../progress/phase-log.md"
---

# Drift Investigation

## Finding

The drift was mostly coordination drift, not citation-check failure. The core validators caught missing citation keys, broken wiki links, and tracked TODO mismatches, but several wiki guidance notes described an earlier project state after parallel workers advanced the source and paper skeletons.

## Evidence

| Drift | Evidence | Consequence | Close control |
| --- | --- | --- | --- |
| Phase state lagged repo state. | The first parallelism test found Phase 1 still marked in progress after GitHub/CI/scaffold were complete. | Planning answer underweighted completed infrastructure. | Update plan and phase log during close. |
| Parallel write scopes were implicit. | The first test found no durable parallel work-plan note. | Workers needed ad hoc prompts for safe file ownership. | Maintain `wiki/progress/parallel-work-plan.md`. |
| Section guidance lagged tracked sections. | Section 06 entered the progress register before acceptance criteria included it. | Future agents could load current progress but stale acceptance rules. | Validator now checks tracked sections against section-acceptance coverage. |
| Source register lagged source-note files. | Source files moved from placeholder to working drafts in a parallel batch. | Planning could treat populated files as unavailable. | Session close requires source-register reconciliation. |
| Evaluation plan lagged implementation. | The retest found the parallel work-plan note still listed as a future check. | Wiki metrics understated implemented controls. | Session close includes evaluation-plan review. |
| Citation aliases appeared during worker handoff. | Workers proposed keys that differed from canonical BibTeX entries. | Integrator had to normalize references after worker completion. | Main integrator owns BibTeX and citation aliases during close; validator now checks source-note citation keys against BibTeX. |
| Generated state can become stale. | Wiki-state report and build artifacts depend on local file mtimes. | Validation can pass before final edits but not after them. | Run build and wiki-state report at the end, not mid-session only. |

## Root Cause

Parallel workers correctly respected disjoint write scopes, but the project had no explicit close contract for shared state. The wiki was useful for starting work, but did not yet force a final reconciliation of guidance, progress, source registers, and generated reports.

## Remediation

- Added [Session Close Procedure](../guidance/session-close.md).
- Added section-acceptance coverage validation to `scripts/validate_wiki_state.py`.
- Added source-note citation-key validation to `scripts/validate_wiki_state.py`.
- Keep parallel worker write scopes disjoint, but require a main integrator close before final response.
- Treat TODO closure count as a project metric, not just a citation-check side effect.
