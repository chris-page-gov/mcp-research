---
title: "Section Acceptance Criteria"
note_type: "guidance"
status: "active"
tags:
  - "acceptance"
  - "sections"
  - "quality-gate"
related:
  - "authoring-contract.md"
  - "../../paper/00-executive-summary.md"
  - "../../paper/01-introduction-methodology.md"
  - "../../paper/02-mcp-in-a-nutshell.md"
  - "../../paper/03-perceptions-and-discourse.md"
  - "../../paper/04-technical-critiques-and-mitigations.md"
  - "../../paper/05-timeline-and-evolution.md"
  - "../../paper/06-mcp-vs-alternatives.md"
  - "../../paper/07-hype-vs-substance.md"
  - "../../paper/08-deeper-analyses-and-case-studies.md"
  - "../../paper/09-government-local-authority-ai-hub.md"
  - "../../paper/10-open-questions-and-future-directions.md"
  - "../../paper/11-glossary.md"
---

# Section Acceptance Criteria

## Global Criteria

- Contains `Purpose`, `Source Boundary`, and `Acceptance Criteria`.
- Separates `Facts`, `Reported opinions`, and `Analysis`.
- Has no opaque Deep Research citation markers.
- Has no uncited factual claims in draft prose.
- Uses only citation keys in `latex/references.bib`.
- Flags source gaps with `TODO-...` keys and does not treat them as evidence.

## Section-Specific Criteria

### `paper/00-executive-summary.md`

- Draft last from body-section findings only.
- Introduce no first-use sources.
- State recommendation conditions and caveats in no more than two pages.

### `paper/01-introduction-methodology.md`

- Define the research question, audience, evidence hierarchy, source cut-off, and drafting discipline.
- Explain how facts, reported opinions, and analysis are separated.
- Do not assert the paper's conclusions before evidence sections are stable.

### `paper/02-mcp-in-a-nutshell.md`

- Define MCP from official source notes only.
- Cover host/client/server, tools, resources, prompts, roots, sampling, elicitation, transports, lifecycle, versioning, discovery, and authorization at skeleton level.
- Resources, prompts, lifecycle, published-server versioning, registry moderation, registry aggregator, roots, and tasks claims are now source-backed.

### `paper/03-perceptions-and-discourse.md`

- Map official, vendor, practitioner, critic, and security-research framings without treating commentary as fact.
- Mark whether each criticism is representative, anecdotal, or source-limited.
- Reuse accepted discourse/security/vendor notes rather than importing opaque Deep Research claims.

### `paper/04-technical-critiques-and-mitigations.md`

- Keep the criticism/evidence/mitigation/residual-risk matrix.
- Cover discovery, context bloat, security and identity, operational complexity, and positive technical assessments.
- Preserve caveats on vendor research, recent claims, and unpopulated discourse notes.

### `paper/05-timeline-and-evolution.md`

- Every timeline event must have a date and citation.
- Distinguish specification evolution, governance events, vendor releases, adoption claims, and security incidents.
- Mark vendor-reported timing and adoption claims separately from independent evidence.

### `paper/06-mcp-vs-alternatives.md`

- Compare alternatives by decision criteria, not marketing labels.
- Preserve the distinction between facts, reported opinions, and analysis.
- Semantic Kernel and OpenAI tools taxonomy claims are now source-backed; framework portability and proprietary-connector procurement claims remain TODO-grade unless kept explicitly analysis/provisional.
- Treat MCP, direct APIs/function calling, agent frameworks, Skills, proprietary app ecosystems, and hybrid models as layerable unless a source supports a mutually exclusive framing.

### `paper/07-hype-vs-substance.md`

- Use a claim/evidence/status table.
- Separate popularity, vendor support, production adoption, maturity, and security assurance.
- Do not treat vendor adoption or open-source popularity as proof of public-sector readiness.

### `paper/08-deeper-analyses-and-case-studies.md`

- Select cases from accepted source notes only.
- Include at least one security/advisory case and one positive implementation case before final prose.
- State why each case was selected, what it evidences, and what it cannot evidence.

### `paper/09-government-local-authority-ai-hub.md`

- Build architecture options and a risk-register skeleton before writing recommendations.
- Use public-sector security guidance, official MCP notes, and accepted section 04 risk evidence.
- Keep procurement and vendor-platform claims provisional until vendor-control and procurement evidence is accepted.
- Do not recommend production adoption unless controls are mapped to identity, registry, approval, audit, data classification, incident response, and supplier ownership.

### `paper/10-open-questions-and-future-directions.md`

- Each open question needs an owner, evidence needed, refresh trigger, and decision impact.
- Include standards/spec evolution, registry governance, operational tooling, security research maturity, and public-sector procurement.
- Do not introduce speculative claims as facts.

### `paper/11-glossary.md`

- Define terms only after the relevant body section has stabilized.
- Keep definitions concise and citation-compatible.
- Resolve the AI Hub definition once section 09 terminology is stable.

## Completion States

- `placeholder`: structure exists, evidence missing.
- `source-ready`: source notes accepted and citation keys exist.
- `draft-ready`: section can be written as prose.
- `review-ready`: prose drafted and citation/link checks pass.
