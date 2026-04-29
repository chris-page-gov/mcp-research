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
- Every citation key used in `paper/`, `sources/`, or `wiki/` must exist in `latex/references.bib`.

## TODO Keys

`TODO-...` keys are allowed only when:

- a needed source is known but not yet captured in a source note;
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
