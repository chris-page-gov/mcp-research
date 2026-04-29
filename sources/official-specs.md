# Official MCP Specifications

Date accessed for all accepted source notes in this file: 2026-04-29.

This file records only specification and official-documentation sources that may support protocol facts in the paper. It intentionally leaves gaps as TODOs where the current local notes are insufficient. Do not draft continuous prose from TODO entries.

## Source Notes

### OS-001 - Authorization

- Citation key: `mcp-authorization-2025-11-25`
- Title: Authorization
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- Source type: primary
- Key claims:
  - Authorization is optional for MCP implementations.
  - For HTTP transports, MCP defines an OAuth-oriented authorization profile.
  - Protected MCP servers act as OAuth resource servers.
  - Clients must use resource indicators and servers must validate token audience.
  - STDIO uses a different credential pattern and should retrieve credentials from the environment.
- Direct quotation under 25 words: "Authorization is OPTIONAL for MCP implementations."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the finding that MCP does not by itself provide a complete enterprise IAM control plane; deployment profiles must make authorization requirements explicit.
- Reliability assessment:
  - High. Normative primary specification.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-002 - Transports

- Citation key: `mcp-transports-2025-11-25`
- Title: Transports
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- Source type: primary
- Key claims:
  - MCP defines STDIO and Streamable HTTP as core transports in the current accepted notes.
  - HTTP servers must validate incoming `Origin` headers.
  - Local HTTP servers should bind to localhost and authenticate connections to reduce DNS rebinding risk.
- Direct quotation under 25 words: "Servers MUST validate the `Origin` header on all incoming connections."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports different control baselines for local developer servers, local HTTP servers, and centrally managed remote servers.
- Reliability assessment:
  - High. Normative primary specification.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-003 - Tools

- Citation key: `mcp-tools-2025-11-25`
- Title: Tools
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/server/tools
- Source type: primary
- Key claims:
  - Tools are model-controlled capabilities exposed by servers.
  - Clients should show available tools and surface invocations to users.
  - Human confirmation is expected for operations, especially where risk is material.
  - Tool annotations can communicate properties such as read-only, destructive, idempotent, or open-world behavior.
- Direct quotation under 25 words: "Tools in MCP are designed to be model-controlled."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the need for non-model policy enforcement around model-selected actions.
- Reliability assessment:
  - High. Normative primary specification.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`

### OS-004 - Sampling

- Citation key: `mcp-sampling-2025-11-25`
- Title: Sampling
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/client/sampling
- Source type: primary
- Key claims:
  - Servers can request LLM sampling through clients.
  - Clients retain control over model access, model selection, and permissions.
  - Human review is recommended for sampling requests and outputs.
- Direct quotation under 25 words: "there SHOULD always be a human in the loop"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports deciding whether server-initiated model calls are allowed, disabled by default, or subject to special logging and approval.
- Reliability assessment:
  - High. Normative primary specification.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-005 - Elicitation

- Citation key: `mcp-elicitation-2025-11-25`
- Title: Elicitation
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation
- Source type: primary
- Key claims:
  - Servers can request structured user input through clients.
  - Form-mode elicitation must not be used for sensitive information.
  - Clients should guard against phishing-style flows and unsafe URL handling.
- Direct quotation under 25 words: "Servers MUST NOT use form mode elicitation to request sensitive information."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports procurement requirements around secret collection, user identity binding, anti-phishing UI, and auditability.
- Reliability assessment:
  - High. Normative primary specification.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-006 - Security Best Practices

- Citation key: `mcp-security-best-practices`
- Title: Security Best Practices
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Source type: primary
- Key claims:
  - Official guidance identifies confused deputy attacks, token passthrough, SSRF, session hijacking, and local server compromise.
  - It recommends audience validation, scope minimization, secure sessions, hardened discovery flows, and avoiding token passthrough.
- Direct quotation under 25 words: "Token passthrough is explicitly forbidden."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Provides official terminology and a minimum risk checklist for security-control mapping.
- Reliability assessment:
  - High for official guidance, but less stable than versioned specification pages.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-007 - Getting Started: Intro

- Citation key: `mcp-intro`
- Title: What is the Model Context Protocol (MCP)?
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/getting-started/intro
- Source type: primary
- Key claims:
  - MCP is presented as an open protocol for integration between LLM applications and external data sources and tools.
  - The official docs use the "USB-C" metaphor for standardized connection, but the paper should treat that as explanatory framing rather than analysis.
- Direct quotation under 25 words: "MCP is an open protocol"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Provides the neutral starting definition for section 02 before assessing whether the protocol is sufficient for public-sector deployment.
- Reliability assessment:
  - High for official positioning and introductory terminology; use versioned specification pages for normative requirements.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `03-perceptions-and-discourse.md`

### OS-008 - Architecture

- Citation key: `mcp-architecture`
- Title: Architecture
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/learn/architecture
- Source type: primary
- Key claims:
  - The official learning material describes MCP architecture and deployment patterns.
  - The saved citation snippets include remote MCP server examples using Streamable HTTP.
  - The imported citation scrape specifically records the Sentry hosted example as a "remote MCP server" using Streamable HTTP.
  - This source can orient the report's host/client/server diagram, but it is not enough on its own for normative lifecycle, initialization, capability-negotiation, or protocol-version claims.
  - This source should be used for architecture orientation, while versioned spec pages should support normative protocol claims.
- Direct quotation under 25 words: "commonly referred to as a remote MCP server"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports distinguishing local and remote MCP deployment patterns and where an enterprise broker or gateway might sit.
- Reliability assessment:
  - High for official explanatory documentation; current page should be rechecked before final publication if architecture details are central.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-009 - Client Best Practices

- Citation key: `mcp-client-best-practices`
- Title: Client Best Practices
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/develop/clients/client-best-practices
- Source type: primary
- Key claims:
  - Official client guidance is a source for host/client controls and implementation practices.
  - The imported report associates this source with progressive discovery, host-side caching, and code-mediated tool execution patterns; verify exact language before final prose.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating context management and host-side policy as implementation responsibilities, not purely protocol properties.
- Reliability assessment:
  - Medium-high. Official documentation, but exact claim extraction remains TODO before final drafting.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-010 - Introducing the MCP Registry

- Citation key: `mcp-registry-preview-2025-09-08`
- Title: Introducing the MCP Registry
- Author/organisation: Model Context Protocol project
- Publication/update date: 2025-09-08
- Date accessed: 2026-04-29
- URL: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- Source type: primary
- Key claims:
  - The MCP Registry launched in preview as an open catalog and API for discovering publicly available MCP servers.
  - The registry is relevant to discovery but should not be treated as a complete enterprise curation layer without further source support.
  - The imported report attributes preview limitations to this source family, including possible breaking changes and lack of durability guarantees; exact wording still needs extraction before final prose.
- Direct quotation under 25 words: "an open catalog and API"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports discovery and registry analysis, especially the need for private or curated registries in regulated environments.
- Reliability assessment:
  - High for launch status and official project intent; preview limitations need confirmation from registry documentation.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `09-government-local-authority-ai-hub.md`

### OS-011 - The MCP Registry

- Citation key: `mcp-registry-about`
- Title: The MCP Registry
- Author/organisation: Model Context Protocol project
- Publication/update date: Current registry documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/registry/about
- Source type: primary
- Key claims:
  - The registry is the official centralized metadata repository for publicly accessible MCP servers.
  - The saved citation snippets indicate the registry is backed by trusted contributors and intended for discovery metadata.
  - The imported report attributes additional constraints to this source family: public-server scope, light moderation, downstream aggregation or private registry expectations, and caution against direct host consumption; exact language remains TODO before final prose.
- Direct quotation under 25 words: "official centralized metadata repository"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of registry governance, discovery metadata, and the gap between public discovery and enterprise approval.
- Reliability assessment:
  - High for official registry description; final prose should verify current durability, moderation, and direct-consumption language.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-012 - Roadmap

- Citation key: `mcp-roadmap-2026-03-05`
- Title: Roadmap
- Author/organisation: Model Context Protocol project
- Publication/update date: 2026-03-05
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/development/roadmap
- Source type: primary
- Key claims:
  - The roadmap identifies enterprise-managed authorization, audit trails, gateway/proxy patterns, configuration portability, and other enterprise-readiness themes.
  - The imported report uses this source to support the claim that several enterprise concerns remain active work.
- Direct quotation under 25 words: "manage MCP access the same way they manage everything else"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Important evidence that public-sector deployment should track roadmap maturity and not assume all enterprise concerns are already solved.
- Reliability assessment:
  - High for official roadmap intent; roadmap items are not stable specification requirements.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### OS-013 - Exploring the Future of MCP Transports

- Citation key: `mcp-transport-future-2025-12-19`
- Title: Exploring the Future of MCP Transports
- Author/organisation: Model Context Protocol project
- Publication/update date: 2025-12-19
- Date accessed: 2026-04-29
- URL: https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/
- Source type: primary
- Key claims:
  - Streamable HTTP enabled remote MCP deployments.
  - The imported report associates this source with unresolved scale concerns including sticky sessions, stateful connections, ambiguous session scope, server discovery, server cards, and statelessness; verify exact wording before final prose.
- Direct quotation under 25 words: "enabling remote MCP deployments"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports transport and operational complexity analysis for enterprise-scale remote MCP.
- Reliability assessment:
  - High for official project direction; final claims about specific unresolved issues should be checked against the page text before publication.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `09-government-local-authority-ai-hub.md`

### OS-014 - Roots

- Citation key: `mcp-roots-2025-06-18`
- Title: Roots
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-06-18
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-06-18/client/roots
- Source type: primary
- Key claims:
  - Roots define filesystem or workspace boundaries exposed by the client to the server.
  - Roots are relevant to local server trust and workspace scoping.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of local filesystem boundaries and workspace trust for developer or back-office use cases.
- Reliability assessment:
  - High as versioned specification page, though the local citation file lists the 2025-06-18 version rather than the 2025-11-25 page.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`

### OS-015 - Tasks

- Citation key: `mcp-tasks-2025-11-25`
- Title: Tasks
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks
- Source type: primary
- Key claims:
  - Tasks are an MCP utility for long-running or deferred work in the 2025-11-25 specification set.
  - Tasks matter for operational design because long-running work requires state, tracing, cancellation, and audit decisions.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of operational complexity where MCP-backed actions outlive a single interaction.
- Reliability assessment:
  - High. Versioned primary specification page.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-016 - Specification Overview

- Citation key: `mcp-specification-2025-11-25`
- Title: Specification
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25
- Source type: primary
- Key claims:
  - The imported citation scrape records the 2025-11-25 specification as saying MCP provides a standardized way for applications to share contextual information with language models and expose tools/capabilities to AI applications.
  - Use this source only for high-level protocol scope unless the final drafting pass extracts exact text from the relevant primitive-specific pages.
  - The imported report treats 2025-11-25 as the current stable spec at the April 2026 cut-off; verify against a current local source before final publication.
- Direct quotation under 25 words: "Share contextual information with language models"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the neutral opening definition that MCP is an integration protocol for context and capabilities, not a complete governance or workflow layer.
- Reliability assessment:
  - High as a primary specification page, but local notes contain only a short scrape snippet.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `05-timeline-and-evolution.md`

### OS-017 - Resources

- Working placeholder citation key: `TODO-mcp-resources`
- Future citation key after exact extraction: `mcp-resources-2025-06-18`
- Title: Resources
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-06-18
- Date accessed: 2026-04-29
- URL: TODO: exact resource page URL is not present in the imported citation list; local scrape identifies an official Resources page dated 2025-06-18.
- Source type: primary
- Key claims:
  - The imported citation scrape records an official Resources page saying MCP provides a standardized way for servers to expose resources to clients.
  - The scrape snippet says resources allow servers to share something with clients, but the snippet is truncated; do not draft final prose about resource contents, URI templates, subscriptions, or listing semantics until exact text is extracted.
- Direct quotation under 25 words: "servers to expose resources to clients"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating resources as a context-exposure primitive that needs data classification, provenance, access control, and audit decisions before government deployment.
- Reliability assessment:
  - Potentially high because it is an official specification page; current local note is incomplete because the durable URL and exact text were not captured.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-018 - Server Concepts

- Citation key: `mcp-server-concepts`
- Title: Server Concepts
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/learn/server-concepts
- Source type: primary
- Key claims:
  - The imported citation list includes this official learning page.
  - The imported report uses official docs/spec sources to define MCP servers as exposing capabilities such as tools, resources, and prompts.
  - The local scrape does not contain exact prompt-specific wording from this page; use this source only as orientation until direct text is extracted.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the basic capability taxonomy for server review checklists, but should not be used alone for normative prompt semantics.
- Reliability assessment:
  - Medium-high. Official learning material, but exact local claim extraction remains incomplete.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `09-government-local-authority-ai-hub.md`

### OS-019 - Lifecycle

- Working placeholder citation key: `TODO-official-mcp-architecture`
- Future citation key after exact extraction: `mcp-lifecycle-2025-03-26`
- Title: Lifecycle
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-03-26
- Date accessed: 2026-04-29
- URL: TODO: exact lifecycle page URL is not present in the imported citation list; local scrape identifies an official Lifecycle page dated 2025-03-26.
- Source type: primary
- Key claims:
  - The imported citation scrape records an official Lifecycle page saying MCP defines a lifecycle for client-server connections.
  - The same snippet associates the lifecycle with capability negotiation and state management.
  - This source is enough to keep lifecycle/capability negotiation in the skeleton, but not enough for final initialization sequence, message ordering, error handling, or protocol-version semantics.
- Direct quotation under 25 words: "capability negotiation and state management"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating connection setup, capability declaration, and state boundaries as architecture-review items rather than invisible implementation details.
- Reliability assessment:
  - Potentially high because it is an official specification page; current local note is incomplete because the durable URL and exact text were not captured.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`

### OS-020 - Versioning Published MCP Servers

- Working placeholder citation key: `TODO-mcp-server-versioning`
- Future citation key after exact extraction: `mcp-server-versioning`
- Title: Versioning Published MCP Servers
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page or specification-adjacent guidance; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: TODO: exact versioning page URL is not present in the imported citation list.
- Source type: primary
- Key claims:
  - The imported citation scrape records an official page titled "Versioning Published MCP Servers".
  - The snippet appears to discuss acceptable and recommended version-label formats for published MCP servers.
  - This should not be used as evidence for protocol-version negotiation until exact page text and scope are extracted.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Points to a future source for server inventory, version pinning, rollback, and supplier-change controls.
- Reliability assessment:
  - Unknown until exact URL and page scope are captured.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `09-government-local-authority-ai-hub.md`

## Known Official-Spec Gaps

These gaps must be filled before final drafting. The placeholder keys exist in `latex/references.bib` only to keep citation checks honest. Source notes above marked with TODO URLs are not final evidence for prose until exact page text is extracted.

| Needed source | Placeholder citation key | Required before |
| --- | --- | --- |
| Exact normative architecture / lifecycle / initialization wording | `TODO-official-mcp-architecture` | Describing lifecycle, initialization sequence, capability negotiation, state management, or protocol-version negotiation in final prose |
| Durable Resources specification URL and exact text | `TODO-mcp-resources` | Drafting resources subsection beyond the minimal "servers expose resources to clients" skeleton |
| Prompts specification or exact server-concepts wording | `TODO-mcp-prompts` | Drafting prompts subsection beyond "servers may expose prompts" |
| Published-server versioning guidance | TODO: add `TODO-mcp-server-versioning` to `latex/references.bib` | Drafting version-pinning or server-version-control claims |
| Registry limitations exact text | TODO: add `TODO-mcp-registry-limitations` to `latex/references.bib` if separate from current registry keys | Drafting claims about moderation, durability, private registries, or direct host consumption |
| Evidence for token-reduction or context-bloat claims | `TODO-context-bloat-token-reduction` | Drafting context-bloat evidence |
