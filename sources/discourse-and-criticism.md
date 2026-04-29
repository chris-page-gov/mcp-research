# Discourse and Criticism

Status: working source notes from local security notes, official notes, and imported-report leads only. These notes are not yet a complete discourse sample.

## Purpose

Capture reported opinions, practitioner criticism, and discourse patterns separately from protocol facts.

## Acceptance Criteria

- Each source must record title, author/organisation, date accessed, URL, source type, key claims, short quote if useful, relevance, reliability, and sections where it may be cited.
- Reported opinions must be clearly attributed.
- Forum or issue evidence must not be generalized beyond its scope.

## Source Boundary

- Use only local source notes, imported materials under `import/`, `sources/security-research.md`, `sources/official-specs.md`, and named source URLs already present in those local/imported leads.
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

- Citation key: `julien-simon-rpc-best-practices-2025-07-29`
- Title: Why MCP's Disregard for 40 Years of RPC Best Practices Will Burn Enterprises
- Author/organisation: Julien Simon
- Publication/update date: 2025-07-29
- Date accessed: 2026-04-29
- URL: https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b
- Source type: secondary
- Key claims:
  - Facts:
    - Medium page title, author, and publication date were directly extracted.
    - The article says its analysis is based on the 2025-06-18 MCP specification, so it should not be treated as current-state protocol evidence without pairing it with later official roadmap/source notes.
  - Reported opinions:
    - Simon argues that MCP prioritizes adoption simplicity over operational robustness for enterprise use.
    - The critique compares MCP unfavourably with older RPC, REST, SOAP, and gRPC patterns on type contracts, stateless scaling, cache semantics, standardized faults, tracing, deadlines, cost attribution, schema versioning, and auditability.
    - Simon frames later MCP additions as evidence of retrofitted enterprise features.
  - Analysis:
    - Use as representative architectural criticism, not as a protocol fact.
    - Pair with official roadmap and transport-future facts before saying a criticism remains current or has been partly mitigated.
- Direct quotation under 25 words: "overlooks four decades of hard-won lessons"
- Relevance:
  - Supports a reported-opinion row on operational complexity and distributed-systems maturity.
  - Helps explain why section 04 should separate protocol-layer, implementation-layer, and enterprise-operations criticisms.
- Reliability assessment:
  - Medium for discourse mapping. Lower for current technical state because the article self-identifies the 2025-06-18 spec as its basis and later official roadmap material addresses some of the same themes.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-003 - ZenMCP GitHub issue on passive context use

- Citation key: `zenmcp-context-bloat-issue-255-2025-08-26`
- Title: ZenMCP uses about 20% (~40,000 tokens) of the Claude Opus 4.1's context window at all times, even when not in use
- Author/organisation: BeehiveInnovations/zen-mcp-server GitHub issue participants
- Publication/update date: opened 2025-08-26; closed 2025-10-01
- Date accessed: 2026-04-29
- URL: https://github.com/BeehiveInnovations/zen-mcp-server/issues/255
- Canonical URL returned by GitHub issue data: https://github.com/BeehiveInnovations/pal-mcp-server/issues/255
- Source type: forum
- Key claims:
  - Facts:
    - Reporter used project version 5.10.3 on macOS with Claude Code and multiple provider keys selected in the issue template.
    - The issue title reports about 20 percent, or about 40,000 tokens, of the Claude Opus 4.1 context window used by ZenMCP when not in use.
    - A maintainer comment says v5.11 reduced token usage by 60-80 percent in most cases and points users to `DISABLED_TOOLS`.
    - A later maintainer comment attributes excessive bloat to each tool advertising model lists for CLI auto-mode, multiplied by total tools, with an expected 60-70 percent cut once fixed.
    - The issue was closed on 2025-10-01.
  - Reported opinions:
    - Participants argue that loading many MCP tools at startup can waste context and increase compaction pressure.
    - One participant suggests fewer tools or subagent isolation as possible mitigation directions.
  - Analysis:
    - Scoped evidence for one ZenMCP/Claude Code configuration, not population-level evidence about all MCP hosts or servers.
    - Supports the narrower claim that eager tool definition loading can be materially expensive and that tool/server design can reduce the cost.
- Direct quotation under 25 words: "consumes about ~20% ... even when not in use"
- Relevance:
  - Supports section 04 reported-opinion language on context bloat and tool-surface cost.
  - Helps distinguish implementation-specific context loading from protocol-inherent overhead.
- Reliability assessment:
  - Low-medium. Practitioner issue evidence with useful configuration details; still not independently reproduced.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-004 - GitHub MCP Server issue on token scopes, verbose prompts, and project focus

- Citation key: `github-mcp-project-focus-issue-1683-2025-12-24`
- Title: Addressing GitHub MCP's Key Issues: Token Scopes, Verbose Prompts, and Lack of Project Context
- Author/organisation: github/github-mcp-server GitHub issue participants
- Publication/update date: opened 2025-12-24; still open as of 2026-04-29 source extraction
- Date accessed: 2026-04-29
- URL: https://github.com/github/github-mcp-server/issues/1683
- Source type: forum
- Key claims:
  - Facts:
    - The exact issue is open and is not a private-registry or package-registry request.
    - The original report covers restricted token scope in private repositories, verbose or repetitive prompts, and lack of current-project focus.
    - The reporter later says a Classic PAT resolves the private repository access issue, while a fine-grained PAT still appears limited in cross-user private-repository scenarios.
    - A GitHub collaborator says a repo-specific version was considered, lists possible options, and says the server lacks local folder access unlike `gh`.
    - A later collaborator comment says a remote server cannot read local files and Docker stdio would require a volume mount, so host-side roots-like support may be needed.
  - Reported opinions:
    - The reporter argues that a project-focused mode would reduce cognitive load and ineffective interaction in single-repository workflows.
    - Commenters describe verbose prompts/tool catalogs as workflow friction and suggest filtering or gateway patterns.
  - Analysis:
    - This issue supports client/server UX and tool-surface criticism, not public/private registry maturity.
    - The imported "closed as not planned" and "private registry" descriptions are not supported by the extracted issue state or title.
- Direct quotation under 25 words: "lacks awareness of the most natural context"
- Relevance:
  - Supports context/tool-surface and project-scoping criticism as practitioner evidence.
  - Does not support section 04 discovery/private-registry criticism except indirectly through the need for host-side scoping and roots-like context.
- Reliability assessment:
  - Low-medium. GitHub issue evidence is valuable for practitioner friction but must be scoped narrowly.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`

### DC-005 - GitHub MCP Server changelog on token reduction

- Citation key: `github-mcp-server-changelog-2026-01-28`
- Title: GitHub MCP Server: New Projects tools, OAuth scope filtering, and new features
- Author/organisation: GitHub
- Publication/update date: 2026-01-28
- Date accessed: 2026-04-29
- URL: https://github.blog/changelog/2026-01-28-github-mcp-server-new-projects-tools-oauth-scope-filtering-and-new-features/
- Source type: primary for GitHub's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Facts:
    - GitHub says the Projects toolset previously used a significant portion of the context window for the tools list.
    - GitHub reports reducing token usage by around 23,000 tokens, or 50 percent, through a consolidated Projects toolset.
    - GitHub says classic PAT scope filtering hides tools the token lacks permission to use, reducing clutter and preventing permission errors.
    - GitHub says enterprise users can run the MCP Server in HTTP mode with OAuth token support.
  - Reported opinions:
    - GitHub positions these changes as improved capability and more efficient context-window use.
  - Analysis:
    - Product-specific evidence that toolset consolidation and permission-aware filtering can reduce context/tool-surface cost.
    - Vendor-reported number; not independent ecosystem measurement.
- Direct quotation under 25 words: "reduced token usage by around 23,000 tokens (50%)"
- Relevance:
  - Supports section 04 context-bloat mitigation and positive technical assessment.
  - Helps avoid overclaiming that context bloat is unavoidable.
- Reliability assessment:
  - Medium-high for GitHub's product change; limited as ecosystem-wide evidence.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`

### DC-006 - Cloudflare codemode and managed remote MCP docs

- Citation key: `cloudflare-mcp-servers`
- Title: Cloudflare's own MCP servers
- Author/organisation: Cloudflare
- Publication/update date: current documentation page; no stable publication date visible in extracted page
- Date accessed: 2026-04-29
- URL: https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/
- Source type: primary for Cloudflare's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Facts:
    - Cloudflare says it runs managed remote MCP servers connectable with OAuth from clients that support MCP.
    - The Cloudflare API MCP server exposes over 2,500 endpoints through two tools, `search()` and `execute()`.
    - Cloudflare says Codemode has the model write JavaScript against a typed OpenAPI/API-client representation inside an isolated Dynamic Worker sandbox.
    - Cloudflare's token table reports 2,594 native full-schema tools at about 1,170,000 tokens, required-params-only native MCP at about 244,000 tokens, and Codemode at two tools and about 1,000 tokens.
  - Reported opinions:
    - Cloudflare frames Codemode as a better way to expose broad API surfaces through MCP.
  - Analysis:
    - Strong product-specific evidence that large API surfaces can be exposed in very different token-cost shapes depending on server design.
    - Token figures are Cloudflare-reported and should not be generalized beyond this design.
- Direct quotation under 25 words: "approximately 1,000 tokens regardless of how many API endpoints exist"
- Relevance:
  - Supports context-bloat mitigation, code-mediated tool use, and positive technical assessment.
  - Should not be generalized beyond Cloudflare's product without additional evidence.
- Reliability assessment:
  - Medium-high for Cloudflare's own documentation; quantitative estimates remain vendor-reported.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### DC-007 - Microsoft Dynamics 365 MCP reuse and auditability claim

- Citation key: `microsoft-dynamics365-mcp-2026-03-11` (existing BibTeX key; metadata now appears stale)
- Proposed future key if BibTeX is updated: `microsoft-dynamics365-mcp-2026-04-27`
- Title: Use Model Context Protocol for finance and operations apps
- Author/organisation: Microsoft
- Publication/update date: 2026-04-27 page `ms.date`; page metadata updated_at 2026-04-29T01:03:00Z
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- Source type: primary for Microsoft's own product; vendor evidence for the wider MCP ecosystem.
- Key claims:
  - Facts:
    - Microsoft describes MCP as a common language for how agents and applications interact with enterprise data and business logic.
    - Microsoft says standardization enables agent access to data/business logic in multiple apps, reuse across ERP systems, access from compatible agent platforms, simplified development, and consistent data access, permissions, and auditability.
    - Microsoft says the Dynamics 365 ERP MCP server lets developers build agents that work with data and nearly any user-available application function without custom code, connectors, or APIs.
    - The page states product version 10.0.47 or later is required and that default allowed MCP clients are Microsoft Copilot Studio and Visual Studio Code.
    - Microsoft says the server dynamically updates context based on security permissions and application configuration, and rejects explicit calls to unauthorized actions or objects.
    - Microsoft lists current implementation limitations, including unsupported controls, some system admin forms, advanced grid filters, attachments, environment downtime, and unsupported sidecar Copilot usage.
  - Reported opinions:
    - Microsoft's reuse, consistency, control, and simplified-development claims are vendor-reported product positioning.
  - Analysis:
    - Useful positive product evidence for reuse/auditability claims, but not independent assurance that the controls are sufficient for government deployment.
- Direct quotation under 25 words: "consistent data access, permissions, and auditability"
- Relevance:
  - Supports the positive technical assessment that MCP can reduce repeated connector work and improve portability where enterprise controls exist.
  - Should be paired with official protocol facts and public-sector governance controls before recommendations.
- Reliability assessment:
  - Medium-high for Microsoft product documentation; limited for general MCP claims and control sufficiency.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

## Official Mitigation / Context Extracts Used In Section 04

These are not discourse sources. They are exact extractions from official pages already named in local notes, recorded here because this lane cannot edit `sources/official-specs.md`.

### DCO-001 - Official registry preview and registry documentation

- Citation keys: `mcp-registry-preview-2025-09-08`; `mcp-registry-about`
- Titles: Introducing the MCP Registry; The MCP Registry
- Author/organisation: Model Context Protocol project
- Publication/update dates:
  - Registry preview blog: published 2025-09-08; HTML metadata modified 2026-03-12.
  - Registry about page: current documentation page; no stable publication date visible in extracted page.
- Date accessed: 2026-04-29
- URLs:
  - https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
  - https://modelcontextprotocol.io/registry/about
- Source type: primary
- Key claims:
  - Facts:
    - Preview blog describes the registry as an open catalog and API for publicly available MCP servers.
    - Preview blog says public marketplaces can augment upstream registry data, and private subregistries can exist inside enterprises with strict privacy and security requirements.
    - Preview blog says registry information is self-reported by server maintainers and downstream consumers will massage/deliver it to end users.
    - Preview blog says the preview does not provide data durability guarantees or other warranties and breaking changes may occur before general availability.
    - Registry docs say the registry is the official centralized metadata repository for publicly accessible MCP servers.
    - Registry docs say it does not support private servers, recommends private MCP registries for private servers, is primarily consumed by downstream aggregators, is not intended for direct host-application consumption, and delegates security scanning to package registries and downstream aggregators.
    - Registry docs say namespace authentication ties reverse-DNS server names to verified GitHub accounts or domains.
  - Reported opinions:
    - None; use as official project positioning and current documentation.
  - Analysis:
    - Supports discovery/registry maturity facts without relying on the misidentified GitHub issue #1683.
- Direct quotation under 25 words: "does not support private servers"

### DCO-002 - Official client best practices

- Citation key: `mcp-client-best-practices`
- Title: Client Best Practices
- Author/organisation: Model Context Protocol project
- Publication/update date: current documentation page; no stable publication date visible in extracted page
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/develop/clients/client-best-practices
- Source type: primary
- Key claims:
  - Facts:
    - The page says naive tool management breaks down as hosts connect to more servers and accumulate hundreds or thousands of tools.
    - It says loading every tool definition upfront wastes tokens, increases latency, and degrades model performance.
    - It identifies progressive discovery and programmatic tool calling/code mode as mitigation patterns.
    - Progressive discovery defers injecting full tool definitions into model context, uses a lightweight `search_tools` meta-tool, and loads full definitions only as needed.
    - The page recommends thresholds, for example 1-5 percent of the context window, for switching to progressive discovery.
    - Implementation guidelines include multiple detail levels, host-side caching of tool definitions, refreshing on `notifications/tools/list_changed`, and grouping tools by server.
    - The page warns that adding or removing tool definitions mid-conversation can invalidate prompt caches.
    - Code mode has the model write code that calls tools in a sandbox, with only the final result returned to the model.
    - The page's figure contrasts direct tool calling at about 100K+ tokens with code mode using an about 200-token script and about 15-token summary.
  - Reported opinions:
    - None; use as official implementation guidance.
  - Analysis:
    - Supports the finding that context bloat is a host/client/server design problem with official mitigation patterns, not an unavoidable protocol property.
- Direct quotation under 25 words: "wastes tokens, increases latency, and degrades model performance"

### DCO-003 - Official transport roadmap and project roadmap

- Citation keys: `mcp-transport-future-2025-12-19`; `mcp-roadmap-2026-03-05`
- Titles: Exploring the Future of MCP Transports; Roadmap
- Author/organisation: Model Context Protocol project
- Publication/update dates:
  - Transport post: published 2025-12-19; HTML metadata modified 2026-03-12.
  - Roadmap page: last updated 2026-03-05.
- Date accessed: 2026-04-29
- URLs:
  - https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/
  - https://modelcontextprotocol.io/development/roadmap
- Source type: primary
- Key claims:
  - Facts:
    - Transport post says enterprise-scale remote deployments have practical challenges around existing infrastructure patterns, stateful connections, managed services, and load balancing.
    - Listed challenges include API gateways/load balancers parsing JSON-RPC payloads, sticky routing from stateful connections, backend storage for simple tools, and ambiguous session scope.
    - Transport post says MCP was originally designed as stateful and that scaling requires sticky sessions or distributed session storage.
    - Transport post says the working group is exploring stateless MCP, explicit sessions, optional notification mechanisms, routing-critical data in HTTP paths/headers, and Server Cards.
    - Server Cards are described as structured metadata documents at `/.well-known/mcp.json` for discovering capabilities, auth requirements, and primitives before connection.
    - Transport post says MCP will continue to support only STDIO and Streamable HTTP as official transports while custom transports remain possible.
    - Roadmap says Streamable HTTP at scale has gaps around horizontal scaling, stateless operation, and middleware patterns.
    - Roadmap enterprise-readiness priorities include audit trails and observability, enterprise-managed auth, gateway/proxy patterns, and configuration portability.
    - Roadmap notes its ideas are not commitments and may not materialize.
  - Reported opinions:
    - None; use as official roadmap intent, not normative requirements.
  - Analysis:
    - Supports pairing dated distributed-systems criticism with official acknowledgements of active transport and enterprise-readiness work.
- Direct quotation under 25 words: "gaps around horizontal scaling, stateless operation, and middleware patterns"

## Discourse Pattern Summary

- Reported criticism clusters around three themes: distributed-systems maturity, prompt-injection/security boundaries, and context/tool-surface bloat.
- Positive technical assessments cluster around interoperability, reusable connector surfaces, and the possibility of centralizing permissions and audit in managed products.
- The strongest local evidence remains security-oriented, but exact extraction now exists for the named non-security leads except the imported private-registry reading of GitHub issue #1683, which failed source verification.

## Required Source Gaps

- `TODO-discourse-criticism-source-notes`: narrowed. Exact source notes and BibTeX now exist for Julien Simon, ZenMCP issue #255, and GitHub MCP Server issue #1683, but this file is still not a representative discourse sample.
- `TODO-discourse-discovery-criticism`: narrowed/blocked. GitHub issue #1683 does not support the imported private-registry claim. Use DCO-001 for official registry limits; find a correct named practitioner source before retaining issue-level private-registry friction.
- `TODO-discourse-context-bloat`: narrowed. DC-003 has exact issue title, dates, configuration, and maintainer mitigation comments; remaining gap is independent reproduction or broader context-bloat evidence, not BibTeX.
- `TODO-context-bloat-token-reduction`: narrowed. DC-005 and DC-006 have exact vendor token figures and BibTeX keys; remaining gap is independent/cross-vendor corroboration.
- `TODO-vendor-adoption-source-notes`: closed for the Microsoft Dynamics note used in section 04; broad adoption claims remain out of scope for this discourse file.
