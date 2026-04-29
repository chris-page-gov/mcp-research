---
title: "Citation Conventions"
note_type: "guidance"
status: "active"
tags:
  - "citations"
  - "bibtex"
  - "pandoc"
related:
  - "source-discipline.md"
  - "../../latex/references.bib"
---

# Citation Conventions

## Syntax

- Use Pandoc citations: `[@citation-key]`.
- Use grouped citations for claims supported by multiple sources: `[@key1; @key2]`.
- Keep citation keys lowercase except `TODO-...` placeholders.
- Every Pandoc citation key used in `paper/`, `sources/`, or `wiki/` must exist in `latex/references.bib`.
- Every non-TODO `Citation key` or `Proposed citation key` recorded in `sources/*.md` must exist in `latex/references.bib`.

## TODO Keys

`TODO-...` keys are allowed only when:

- a needed source is known but not yet captured in a source note, or the source-note evidence remains too narrow for final prose;
- the missing source blocks final prose;
- the BibTeX entry contains a `note` explaining the TODO.

`TODO-...` keys are not evidence.

## Reliability

Use source types consistently:

- `primary`: official specs, standards, government guidance, GitHub advisories, vendor docs for the vendor's own product.
- `academic`: papers and preprints.
- `vendor`: vendor security research or market analysis.
- `secondary`: practitioner commentary, explainers, advisory databases, community standards.
- `forum`: GitHub issues, discussions, social posts, and community threads.
