---
title: "Wiki Evaluation Plan"
note_type: "evaluation-plan"
status: "active"
tags:
  - "evals"
  - "llm-wiki"
  - "metrics"
related:
  - "../progress/plan.md"
  - "../guidance/section-acceptance.md"
---

# Wiki Evaluation Plan

## Goal

Measure whether the wiki helps agents retrieve the right guidance and avoid context bloat, unsupported claims, and repeated course corrections.

## Candidate Metrics

- Guidance precision: number of wiki notes needed for a task.
- Citation compliance: cited keys present in `latex/references.bib`.
- Source discipline: factual claims with supporting source-note entries.
- TODO closure: count of `TODO-...` citation keys over time.
- Link health: internal Markdown links resolve.
- Course correction count: number of later edits caused by source-boundary errors.
- Context efficiency: task can be completed from section file plus one or two wiki notes.

## Implemented Checks

- Structured progress register in `wiki/data/progress-register.json`.
- Wiki link validation through `scripts/check_links.py` and `scripts/validate_wiki_state.py`.
- TODO citation key reporting through `scripts/check_citations.py`.
- Wiki/repo alignment report through `scripts/validate_wiki_state.py`.
- Source-note citation-key coverage: non-TODO `Citation key` and `Proposed citation key` entries in `sources/*.md` must exist in `latex/references.bib`.
- Section-acceptance coverage: tracked paper sections in `wiki/data/progress-register.json` must appear in `wiki/guidance/section-acceptance.md`.
- Parallel work-plan note for safe write scopes in `wiki/progress/parallel-work-plan.md`.
- Completion dashboard for paper-section state, source-note state, active evidence blockers, and current parallel capacity.

## Recorded Runs

- [Next Step Parallelism Test](next-step-parallelism-test.md)
- [Next Step Parallelism Retest](next-step-parallelism-retest.md)
- [Next Step Parallelism Progress Test](next-step-parallelism-progress-test.md)
- [Drift Investigation](drift-investigation.md)

## Future Checks

- Add an evaluation prompt set once sections 02 and 04 have first drafts.
- Add raw-page recovery tracking if exact extraction becomes hard to coordinate through section blockers alone.
- Track close-procedure failures as course-correction evidence.
