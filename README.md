# MCP Research

This repository is a Markdown/LaTeX paper project and LLM-Wiki for assessing the Model Context Protocol (MCP) as an integration backbone for enterprise and government AI, with particular attention to a Government / Local Authority AI Hub.

The current state is a rigorous skeleton, not the full report. Source notes, citation conventions, acceptance criteria, and wiki guidance are in place so prose can be drafted later without inventing citations.

## Layout

- `paper/`: section files for the paper.
- `sources/`: structured source notes and source registers.
- `latex/`: BibTeX and LaTeX support files.
- `scripts/`: build and validation scripts.
- `wiki/`: Obsidian-friendly LLM-Wiki for guidance, progress, and evaluation planning.
- `import/`: imported Deep Research artefacts for orientation only.
- `dist/`: generated build artefacts.

## Authoring Rules

- Do not write the full report until the relevant source notes are accepted.
- Separate `Facts`, `Reported opinions`, and `Analysis`.
- Use Pandoc citations such as `[@mcp-authorization-2025-11-25]`.
- Treat `TODO-...` citation keys as blockers, not evidence.
- Do not cite the imported Deep Research report directly in final prose; convert claims into source notes first.

See [the authoring contract](wiki/guidance/authoring-contract.md), [citation conventions](wiki/guidance/citation-conventions.md), and [source discipline](wiki/guidance/source-discipline.md).

## Current Priority

The next drafting phase should start with:

1. `sources/official-specs.md`
2. `paper/02-mcp-in-a-nutshell.md`
3. `paper/04-technical-critiques-and-mitigations.md`

Section 04 already has a criticism/evidence/mitigation/residual-risk skeleton. Discovery and context-bloat claims remain blocked on source-note gaps.

## Build

Python tooling uses `uv` by default. Install dependencies with:

```bash
uv sync
```

The build script always creates combined Markdown:

```bash
./scripts/build.sh
```

Output:

- `dist/mcp-research-paper.md`
- `dist/mcp-research-paper.tex` if Pandoc is installed
- `dist/mcp-research-paper.pdf` if Pandoc and XeLaTeX are installed

Recommended local toolchain:

- Pandoc 3.x
- TeX Live or MacTeX with `xelatex`

## Checks

Run all local checks:

```bash
make check
```

Or run checks individually:

```bash
./scripts/check_citations.py
./scripts/check_links.py
./scripts/validate_wiki_state.py
```

The Makefile runs these through `uv run python` by default.

The citation checker verifies that every used citation key exists in `latex/references.bib` and reports remaining `TODO-...` keys. The link checker validates internal Markdown and wiki links and ignores external URLs. The wiki-state validator checks that the wiki's progress register, source register, TODO blockers, required guidance files, and build artefacts match the current repository state.

Developer quality checks:

```bash
make lint
make typecheck
```

To write a browsable validation report:

```bash
./scripts/validate_wiki_state.py --write-report
```

Output:

- `wiki/wiki-state-report.md`
- `wiki/data/wiki-state-report.json`

## LLM-Wiki Workflow

The wiki is designed to keep context small:

1. Start at [wiki/index.md](wiki/index.md).
2. Read only the guidance note relevant to the task.
3. Read the target paper section.
4. Read only the source-note files listed in that section's `Source Boundary`.
5. Update [the phase log](wiki/progress/phase-log.md) when progress materially changes.

This mirrors the earlier AI Engineering Lab pattern: small linked notes, source boundaries, progress registers, and validation scripts rather than one oversized agent file.
