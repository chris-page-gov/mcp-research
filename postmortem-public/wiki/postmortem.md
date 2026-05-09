# Postmortem Synthesis

## What Happened

The project converted a failed deep-research report into a controlled Markdown/LaTeX paper project with structured source notes, a build path, validation scripts, and an LLM-Wiki for guidance and progress tracking.

The assistant workflow then moved from broad drafting toward source-first scaffolding, parallel evidence lanes, and repeated wiki-guidance evaluations.

## What Worked

- The LLM-Wiki reduced context load by separating source discipline, progress, acceptance criteria, and evaluation records.
- Parallel worker lanes worked when write scopes were explicit and the main thread owned shared integration files.
- Citation and wiki-state validation caught missing BibTeX entries, broken links, incomplete section tracking, and source TODO register gaps.

## What Failed Or Drifted

- Prose guidance drifted after parallel work, especially current-state statements in wiki guidance.
- Source-note TODOs were initially prose-only, making blocker state hard to validate.
- The full report remains intentionally undrafted; source readiness is still incomplete for sections 04, 06, and 09.

## Current Risk

Semantic drift remains the largest workflow risk. Structural validators now catch many file/register errors, but stale guidance prose still needs a dedicated alignment check.
