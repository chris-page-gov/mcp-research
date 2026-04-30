---
title: "Session Close Procedure"
note_type: "guidance"
status: "active"
tags:
  - "close"
  - "validation"
  - "llm-wiki"
related:
  - "authoring-contract.md"
  - "section-acceptance.md"
  - "../progress/parallel-work-plan.md"
  - "../progress/phase-log.md"
  - "../data/progress-register.json"
---

# Session Close Procedure

Use this procedure before ending any session that changes paper, source, citation, script, or wiki state.

## Drift Review

Check for these common drift causes:

- a paper section was added to `wiki/data/progress-register.json` but not to [Section Acceptance Criteria](section-acceptance.md);
- a source-note file moved from placeholder to working draft but [Source Register](../../sources/source-register.md) still says `Placeholder`;
- a wiki evaluation, plan item, or future check became stale after implementation;
- a worker proposed citation keys that differ from canonical `latex/references.bib` keys;
- a source note records a non-TODO citation key that is not present in `latex/references.bib`;
- generated reports or build artifacts are stale after source changes;
- local metadata files such as `.DS_Store` reappeared.

## Shared-State Close

The main integrator owns these files during close:

- `latex/references.bib`
- `sources/source-register.md`
- `wiki/data/progress-register.json`
- `wiki/guidance/section-acceptance.md`
- `wiki/progress/plan.md`
- `wiki/progress/phase-log.md`
- `wiki/progress/parallel-work-plan.md`
- `wiki/progress/completion-dashboard.md`
- `wiki/evals/wiki-evaluation-plan.md`
- `CHANGELOG.md`
- generated wiki-state reports

Do not leave worker-owned source edits without reconciling these shared files.

## Validation Close

Run these commands after integration:

```bash
find . -name .DS_Store -delete
make build
uv run python scripts/validate_wiki_state.py --write-report
make check
make lint
make typecheck
git diff --check
```

If any source, paper, or LaTeX file changed after `make build`, rerun `make build` before final validation.

## Git Close

Before commit:

- inspect `git status --short`;
- review `git diff --stat`;
- update `CHANGELOG.md` for material public-facing changes;
- confirm `scripts/check_citations.py` has no unexpected TODO citations;
- confirm `scripts/validate_wiki_state.py` still accepts source-note citation keys, progress blockers, section-acceptance coverage, and source-register state;
- commit only after local validation passes.

After push:

- watch the GitHub Actions run;
- record any CI caveat in the final response;
- do not leave required command sessions running.
