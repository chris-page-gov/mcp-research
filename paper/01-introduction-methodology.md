# Introduction and Methodology

## Status

Skeleton only.

## Purpose

Define the research question, intended audience, evidence hierarchy, source cut-off, and drafting discipline.

## Source Boundary

- Use source registers in `sources/` as the paper evidence base.
- Prefer primary sources for protocol claims.
- Use secondary, vendor, forum, and academic sources to evidence perceptions, risks, and adoption claims.
- Do not reuse opaque Deep Research citation markers in final prose.

## Evidence Hierarchy

1. Primary: official specifications, standards, government guidance, GitHub advisories, vendor product documentation for that vendor's own product.
2. Academic: peer-reviewed work first, then clearly labelled preprints.
3. Vendor security research: useful for threat evidence, but avoid relying on one vendor claim for final recommendations.
4. Secondary/practitioner commentary: useful for discourse, implementation experience, and reported opinions.
5. Forum/community material: cite only for community perception or reproducible implementation issues.

## Citation Convention

- Use Pandoc citations: `[@citation-key]`.
- Use grouped citations for claims supported by multiple sources: `[@key1; @key2]`.
- Use `@TODO-...` keys only when a source gap blocks final prose; do not use TODO keys for facts whose non-TODO BibTeX entry already exists.
- Every citation key must appear in `latex/references.bib`.
- Do not invent citations or cite sources not represented in `sources/`.

## Acceptance Criteria

- States the research question and decision context.
- Defines `Fact`, `Reported opinion`, and `Analysis`.
- Explains source selection, reliability assessment, and update policy.
- Explains why the LLM-Wiki exists and how it constrains context selection.

## Draft Outline

### Facts

- TODO: State project scope, source cut-off, and evidence hierarchy.

### Reported Opinions

- TODO: Describe how discourse sources are handled without treating commentary as fact.

### Analysis

- TODO: Explain why a wiki-based guidance layer reduces context bloat and improves auditability.
