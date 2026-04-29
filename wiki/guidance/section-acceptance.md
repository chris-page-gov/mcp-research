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
  - "../../paper/02-mcp-in-a-nutshell.md"
  - "../../paper/04-technical-critiques-and-mitigations.md"
---

# Section Acceptance Criteria

## Global Criteria

- Contains `Purpose`, `Source Boundary`, and `Acceptance Criteria`.
- Separates `Facts`, `Reported opinions`, and `Analysis`.
- Has no opaque Deep Research citation markers.
- Has no uncited factual claims in draft prose.
- Uses only citation keys in `latex/references.bib`.
- Flags source gaps with `TODO-...` keys and does not treat them as evidence.

## Current Priority Sections

### `paper/02-mcp-in-a-nutshell.md`

- Define MCP from official source notes only.
- Cover host/client/server, tools, resources, prompts, roots, sampling, elicitation, transports, lifecycle, versioning, discovery, and authorization at skeleton level.
- Resources, prompts, lifecycle, published-server versioning, registry moderation, and registry aggregator claims are now source-backed; roots and tasks still need exact quotation before final prose.

### `paper/04-technical-critiques-and-mitigations.md`

- Keep the criticism/evidence/mitigation/residual-risk matrix.
- Cover discovery, context bloat, security and identity, operational complexity, and positive technical assessments.
- Preserve caveats on vendor research, recent claims, and unpopulated discourse notes.

### `paper/06-mcp-vs-alternatives.md`

- Compare alternatives by decision criteria, not marketing labels.
- Preserve the distinction between facts, reported opinions, and analysis.
- Semantic Kernel and OpenAI tools taxonomy claims are now source-backed; framework portability and proprietary-connector procurement claims remain TODO-grade unless kept explicitly analysis/provisional.
- Treat MCP, direct APIs/function calling, agent frameworks, Skills, proprietary app ecosystems, and hybrid models as layerable unless a source supports a mutually exclusive framing.

### `paper/09-government-local-authority-ai-hub.md`

- Build architecture options and a risk-register skeleton before writing recommendations.
- Use public-sector security guidance, official MCP notes, and accepted section 04 risk evidence.
- Keep procurement and vendor-platform claims provisional until vendor-control and procurement evidence is accepted.
- Do not recommend production adoption unless controls are mapped to identity, registry, approval, audit, data classification, incident response, and supplier ownership.

## Completion States

- `placeholder`: structure exists, evidence missing.
- `source-ready`: source notes accepted and citation keys exist.
- `draft-ready`: section can be written as prose.
- `review-ready`: prose drafted and citation/link checks pass.
