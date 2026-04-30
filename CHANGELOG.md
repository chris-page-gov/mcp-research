# CHANGELOG

This repository uses a two-layer change log:

- This top-level file gives a concise, public, reverse-chronological summary.
- The LLM-Wiki carries operational detail: [Phase Log](wiki/progress/phase-log.md), [Completion Dashboard](wiki/progress/completion-dashboard.md), [Parallel Work Plan](wiki/progress/parallel-work-plan.md), [Wiki Evaluation Plan](wiki/evals/wiki-evaluation-plan.md), and [Wiki State Report](wiki/wiki-state-report.md).

The intent is to keep public readers oriented without duplicating every source-note or evaluation detail. Material research or workflow changes should update this file and the relevant wiki tracking note in the same change.

## Unreleased

### Added

- Added this top-level changelog as the public entry point for repository history.
- Added tracked VSCode workspace settings that disable the isort language server and use Ruff for Python formatting/import organization.

### Changed

- Expanded documentation lockstep checks so the changelog participates in internal link validation and wiki-state validation.

## 2026-04-29

### Added

- Created the Markdown/LaTeX paper skeleton under `paper/` and `latex/`.
- Created structured source-note files and the source register under `sources/`.
- Created the LLM-Wiki under `wiki/` for guidance, progress, source discipline, evaluation, and close procedures.
- Added citation, link, wiki-state, lint, type-check, build, and CI workflows.
- Added the public GitHub repository setup and Node 24-compatible CI.
- Added the imported Deep Research report activity and citations under `import/`.
- Added Codex project summary reporting under `reports/` and `scripts/codex_project_summary.py`.

### Changed

- Promoted `paper/02-mcp-in-a-nutshell.md` to source-ready after closing official MCP resources, prompts, lifecycle, versioning, registry, roots, and tasks evidence gaps.
- Started source-first skeletons for technical critiques, alternatives, and Government / Local Authority AI Hub analysis.
- Added the completion dashboard and parallel work plan so future agents can see progress and safe write scopes without loading the whole repo.

### Validation

- CI passed after each pushed stage through `4ead873`.
