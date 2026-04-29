---
title: "Wiki Evaluation Plan"
note_type: "evaluation-plan"
status: "draft"
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

## Future Checks

- Add a structured progress register in `wiki/data/`.
- Extend `scripts/check_links.py` to report unresolved wiki links.
- Extend `scripts/check_citations.py` to classify TODO citation keys.
- Add an evaluation prompt set once sections 02 and 04 have first drafts.
