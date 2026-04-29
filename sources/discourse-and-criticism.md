# Discourse and Criticism

Status: working source notes from local security notes, official notes, and imported-report leads only. These notes are not yet a complete discourse sample.

## Purpose

Capture reported opinions, practitioner criticism, and discourse patterns separately from protocol facts.

## Acceptance Criteria

- Each source must record title, author/organisation, date accessed, URL, source type, key claims, short quote if useful, relevance, reliability, and sections where it may be cited.
- Reported opinions must be clearly attributed.
- Forum or issue evidence must not be generalized beyond its scope.

## Source Boundary

- Use only local source notes, imported materials under `import/`, `sources/security-research.md`, and `sources/official-specs.md`.
- Do not treat imported Deep Research citation markers as final citations. Convert useful leads into source notes and keep TODO markers where exact extraction is incomplete.
- Forum and issue evidence is evidence of a reported problem in that thread only, not population-level evidence.

## Source Notes

### DC-001 - Simon Willison on prompt injection and agent tooling

- Citation key: `simon-willison-prompt-injection-2025-04-11`
- Title: Prompt injection security problems in LLMs and AI agents
- Author/organisation: Simon Willison
- Publication/update date: 2025-04-11
- Date accessed: 2026-04-29
- URL: https://simonwillison.net/2025/Apr/11/prompt-injection-security-problems/
- Source type: secondary
- Key claims:
  - Argues that combining private data, untrusted content, and external communication creates severe AI-agent risk.
  - Uses MCP and agent tooling as examples of prompt-injection and confused-deputy problems.
  - Emphasizes that model-level instruction following should not be treated as a security boundary.
- Direct quotation under 25 words: "prompt injection security problems"
- Relevance:
  - Supports section 04 reported-opinion language on the limits of approval-only or prompt-only safety models.
  - Useful for explaining why MCP security analysis must cover composed tool access, not only the protocol wire format.
- Reliability assessment:
  - Medium-high. Practitioner analysis by a well-regarded commentator; not a formal advisory.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`

### DC-002 - Julien Simon distributed-systems critique

- Citation key: `TODO-discourse-criticism-source-notes` (working placeholder)
- Proposed future key: `TODO-discourse-julien-simon-rpc-best-practices`
- Title: Why MCP's Disregard for 40 Years of RPC Best Practices Will Burn Enterprises
- Author/organisation: Julien Simon
- Publication/update date: TODO: exact publication/update date not extracted locally.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b
- Source type: secondary
- Key claims:
  - Imported report records this as a representative architectural critique, not a protocol fact.
  - Reported criticism: MCP is said to overlook long-established RPC and distributed-systems lessons.
  - Imported report analysis links this critique to official roadmap/transport work on sticky sessions, statefulness, discovery, server cards, and gateway/proxy semantics.
- Direct quotation under 25 words: "overlooks four decades of hard-won lessons"
- Relevance:
  - Supports a reported-opinion row on operational complexity and distributed-systems maturity.
  - Should be paired with official roadmap and transport-future source notes before any final claim that the critique is vindicated.
- Reliability assessment:
  - Medium for discourse mapping; lower for factual findings until the post is directly extracted into a complete source note.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-003 - ZenMCP GitHub issue on passive context use

- Citation key: `TODO-discourse-context-bloat` (working placeholder)
- Proposed future key: `TODO-discourse-zenmcp-context-bloat-issue-255`
- Title: GitHub issue #255 on ZenMCP passive context use
- Author/organisation: BeehiveInnovations/zen-mcp-server GitHub issue participants
- Publication/update date: TODO: exact issue title and dates not extracted locally.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://github.com/BeehiveInnovations/zen-mcp-server/issues/255
- Source type: forum
- Key claims:
  - Imported report records a practitioner issue reporting that MCP tools consumed about one fifth of a context window even when not actively used.
  - Imported report also summarizes the issue as roughly 40,000 passive tokens in Claude Code.
  - This is scoped evidence of one tool/client configuration and should not be generalized to MCP implementations as a whole.
- Direct quotation under 25 words: "consumes about ~20% ... even when not in use"
- Relevance:
  - Supports section 04 reported-opinion/TODO language on context bloat and tool-surface cost.
  - Helps distinguish implementation-specific context loading from protocol-inherent overhead.
- Reliability assessment:
  - Low-medium. Practitioner issue evidence can be useful, but exact configuration, versions, and reproducibility require verification.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-004 - GitHub MCP Server issue on private registry friction

- Citation key: `TODO-discourse-discovery-criticism` (working placeholder)
- Proposed future key: `TODO-discourse-github-mcp-private-registry-issue-1683`
- Title: GitHub MCP Server issue #1683 on private registry/package-registry support
- Author/organisation: github/github-mcp-server GitHub issue participants
- Publication/update date: TODO: exact issue title, opening date, and close rationale not extracted locally.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://github.com/github/github-mcp-server/issues/1683
- Source type: forum
- Key claims:
  - Imported report describes this as enterprise friction around private registries or private package registries.
  - Imported report says the issue was closed as not planned; exact local extraction is still required before final prose.
  - This is issue-level evidence, not proof of general registry immaturity.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance:
  - Supports discovery and registry criticism as a reported enterprise concern.
  - Should be paired with official registry and roadmap notes for facts about public registry scope and future discovery work.
- Reliability assessment:
  - Low-medium. GitHub issue evidence is valuable for practitioner friction but must be scoped narrowly.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-005 - GitHub MCP Server changelog on token reduction

- Citation key: `TODO-context-bloat-token-reduction` (working placeholder)
- Proposed future key: `TODO-discourse-github-mcp-token-reduction-2026-01-28`
- Title: GitHub MCP Server - new Projects tools, OAuth scope filtering, and new features
- Author/organisation: GitHub
- Publication/update date: 2026-01-28 according to imported citation list.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://github.blog/changelog/2026-01-28-github-mcp-server-new-projects-tools-oauth-scope-filtering-and-new-features/
- Source type: primary for GitHub's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Imported report states that GitHub reduced one toolset by about 23,000 tokens, roughly 50 percent for that area.
  - Supports the claim that context overhead is partly controllable by toolset consolidation and implementation design.
  - Exact local source extraction is required before treating the number as a final factual claim.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance:
  - Supports section 04 context-bloat mitigation and positive technical assessment.
  - Helps avoid overclaiming that context bloat is unavoidable.
- Reliability assessment:
  - Medium-high for GitHub's product change; limited as ecosystem-wide evidence.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`

### DC-006 - Cloudflare codemode and managed remote MCP docs

- Citation key: `TODO-context-bloat-token-reduction` (working placeholder)
- Proposed future key: `TODO-discourse-cloudflare-codemode-token-efficiency`
- Title: MCP servers for Cloudflare
- Author/organisation: Cloudflare
- Publication/update date: TODO: exact page date not extracted locally.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/
- Source type: primary for Cloudflare's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Imported report states that exposing Cloudflare's full API as thousands of native tools would cost about 1.17 million tokens.
  - Imported report states that Cloudflare's codemode approach uses about 1,000 tokens.
  - Also supports a positive assessment that managed, OAuth-protected remote MCP servers can reduce client-side integration work when carefully designed.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance:
  - Supports context-bloat mitigation, code-mediated tool use, and positive technical assessment.
  - Should not be generalized beyond Cloudflare's product without additional evidence.
- Reliability assessment:
  - Medium-high for Cloudflare's own documentation; exact token figures need direct extraction before final prose.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### DC-007 - Microsoft Dynamics 365 MCP reuse and auditability claim

- Citation key: `TODO-vendor-adoption-source-notes` (working placeholder)
- Proposed future key: `TODO-positive-microsoft-dynamics-mcp-reuse-auditability`
- Title: Use a Model Context Protocol server to create and extend agents for Microsoft Dynamics 365 finance and operations apps
- Author/organisation: Microsoft
- Publication/update date: 2026-03-11 according to imported citation list.
- Date accessed: 2026-04-29 in imported materials.
- URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- Source type: primary for Microsoft's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Imported report summarizes Microsoft as presenting MCP as reusable access to tools from compatible agent platforms.
  - Imported report links the source to consistent data access, permissions, auditability, and reduced need for custom connectors or APIs.
  - This is positive vendor product evidence, not independent proof of ecosystem maturity.
- Direct quotation under 25 words: "access to tools ... from any compatible agent platform"
- Relevance:
  - Supports the positive technical assessment that MCP can reduce repeated connector work and improve portability where enterprise controls exist.
  - Should be paired with official protocol facts and public-sector governance controls before recommendations.
- Reliability assessment:
  - Medium-high for Microsoft product positioning; limited for general MCP claims.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

## Discourse Pattern Summary

- Reported criticism clusters around three themes: distributed-systems maturity, prompt-injection/security boundaries, and context/tool-surface bloat.
- Positive technical assessments cluster around interoperability, reusable connector surfaces, and the possibility of centralizing permissions and audit in managed products.
- The strongest local evidence remains security-oriented. Non-security discourse notes are still imported-report conversions and should stay TODO-grade until exact source text is extracted.

## Required Source Gaps

- `TODO-discourse-criticism-source-notes`: still needed for a broader representative criticism sample beyond Simon Willison, Julien Simon, and a small number of GitHub issues.
- `TODO-discourse-discovery-criticism`: partially populated by DC-004, but exact issue details and additional enterprise-discovery evidence remain TODO.
- `TODO-discourse-context-bloat`: partially populated by DC-003, but exact issue details, configuration, and corroborating measurements remain TODO.
- `TODO-context-bloat-token-reduction`: partially populated by DC-005 and DC-006, but exact text and numbers need direct extraction before final prose.
- `TODO-vendor-adoption-source-notes`: partially populated for positive technical assessment by DC-007, but broad adoption claims remain out of scope until source notes are accepted.
