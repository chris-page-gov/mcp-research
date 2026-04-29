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
- Avoid claims about resources, prompts, lifecycle, and versioning until source notes are added.

### `paper/04-technical-critiques-and-mitigations.md`

- Keep the criticism/evidence/mitigation/residual-risk matrix.
- Cover discovery, context bloat, security and identity, operational complexity, and positive technical assessments.
- Preserve caveats on vendor research, recent claims, and unpopulated discourse notes.

### `paper/06-mcp-vs-alternatives.md`

- Compare alternatives by decision criteria, not marketing labels.
- Preserve the distinction between facts, reported opinions, and analysis.
- Keep Semantic Kernel, OpenAI tools taxonomy, framework portability, and proprietary-connector procurement claims as TODO-grade until exact source evidence is accepted.
- Treat MCP, direct APIs/function calling, agent frameworks, Skills, proprietary app ecosystems, and hybrid models as layerable unless a source supports a mutually exclusive framing.

## Completion States

- `placeholder`: structure exists, evidence missing.
- `source-ready`: source notes accepted and citation keys exist.
- `draft-ready`: section can be written as prose.
- `review-ready`: prose drafted and citation/link checks pass.
