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
  - The launch post describes the registry as the official central registry and a primary source of truth for public-server metadata that sub-registries can build upon.
  - The post separates public subregistries and private enterprise subregistries, and says downstream consumers can augment registry data for their end users.
  - The post describes registry metadata as self-reported information that downstream consumers can massage and deliver.
  - The post says community members can flag servers that violate moderation guidelines, with registry maintainers able to denylist and remove entries from public access.
  - This source supports public discovery and registry intent; use OS-011, OS-022, and OS-023 for current limitation wording.
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
  - The registry page says the MCP Registry is currently in preview and that breaking changes or data resets may occur before general availability.
  - The registry is the official centralized metadata repository for publicly accessible MCP servers.
  - The registry provides publication metadata, namespace management through DNS verification, a REST API for clients and aggregators, and standardized installation/configuration information.
  - The registry hosts metadata pointing to code/binaries in package registries; it is not itself the package registry.
  - The registry supports open-source and closed-source servers only where installation or server access is public; it does not support private servers.
  - The registry recommends a private MCP registry for private servers.
  - The registry is intended primarily for downstream aggregators, and its metadata is deliberately unopinionated.
  - Host applications are not intended to consume the official registry directly; they should consume downstream registries conforming to the OpenAPI spec.
  - The registry delegates security scanning to underlying package registries and downstream aggregators, focusing on namespace authentication and metadata hosting.
  - The official registry codebase is not designed for self-hosting; forks must be maintained independently.
- Direct quotation under 25 words: "official centralized metadata repository"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of registry governance, discovery metadata, and the gap between public discovery and enterprise approval.
- Reliability assessment:
  - High for official registry description. Use OS-022 for moderation limits and OS-023 for durability/API-consumption limits.
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
  - The post says growing remote-server demand created practical challenges for enterprise-scale distributed deployments.
  - Listed challenges include load-balancer/API-gateway routing complexity, sticky routing from stateful connections, backend-storage burden for simple tools, and ambiguous session scope.
  - The post says MCP was originally designed as a stateful protocol with a capability/protocol-version handshake and fixed connection state.
  - The transport working group was exploring stateless protocol changes, capability discovery, explicit session semantics, optional notification/caching improvements, and server cards.
  - Server Cards are presented as a roadmap direction for structured metadata exposed at a well-known endpoint, not as already-stable protocol behavior in this source.
  - The post says MCP will continue to support STDIO and Streamable HTTP as the only official transports for the current cycle, while specialized teams may use custom transports.
  - The post says required SEPs were targeted for Q1 2026 and possible inclusion in the next specification release tentatively slated for June 2026.
- Direct quotation under 25 words: "enabling remote MCP deployments"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports transport and operational complexity analysis for enterprise-scale remote MCP.
- Reliability assessment:
  - High for official project direction and roadmap concerns; not a stable normative requirement source.
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
  - MCP provides a standardized way for clients to expose filesystem roots to servers.
  - Roots define filesystem boundaries for where servers can operate and what directories/files they can access.
  - Servers can request roots from supporting clients and receive notifications when the root list changes.
  - The protocol does not mandate a specific user interaction model for exposing roots.
  - Clients that support roots must declare the `roots` capability during initialization; `listChanged` indicates whether they emit root-list change notifications.
  - Servers retrieve roots with `roots/list`; clients that support `listChanged` send `notifications/roots/list_changed` when roots change.
  - A root has a URI and optional human-readable name; the URI must be a `file://` URI in the current specification.
  - Security considerations say clients must expose only roots with appropriate permissions, validate root URIs, implement access controls, and monitor accessibility.
  - Servers should respect root boundaries and validate paths against provided roots.
- Direct quotation under 25 words: "define the boundaries of where servers can operate"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of local filesystem boundaries and workspace trust for developer or back-office use cases.
- Reliability assessment:
  - High as versioned specification page, though this note uses the 2025-06-18 page because that is the version recorded in the local citation set.
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
  - Tasks were introduced in MCP version 2025-11-25 and are described as experimental.
  - Tasks let requestors augment requests with durable state machines for polling and deferred result retrieval.
  - A requestor can be either client or server; the receiver executes the task and generates a unique task ID.
  - Servers and clients supporting task-augmented requests must declare a `tasks` capability during initialization, structured by supported request category.
  - Requestors should create tasks only when the receiver has declared support for the relevant task-augmented request type.
  - Tool calls add finer-grained `execution.taskSupport` values of `required`, `optional`, or `forbidden`.
  - Task-augmented requests use a two-phase response pattern: an initial `CreateTaskResult` with task data, then the actual result through `tasks/result` after completion.
  - Requestors poll task state with `tasks/get`; task status notifications are optional and requestors must not rely on them.
  - `tasks/list` supports pagination, and `tasks/cancel` is the explicit cancellation operation.
  - Valid task states include `working`, `input_required`, `completed`, `failed`, and `cancelled`; completed, failed, and cancelled states are terminal.
  - Receivers must include creation/update timestamps and TTL behavior in task responses; task results may be deleted after TTL expiry.
  - Task-related requests, responses, and notifications must include related-task metadata except where the task ID is already the RPC parameter/source of truth.
  - Security considerations say receivers must bind tasks to the authorization context when available, reject access from other contexts, use high-entropy task IDs when context-binding is unavailable, limit task listing, rate-limit task operations, and log task lifecycle events for audit.
- Direct quotation under 25 words: "durable state machines"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports analysis of operational complexity where MCP-backed actions outlive a single interaction.
- Reliability assessment:
  - High as a versioned primary specification page. Task design is explicitly experimental in this version.
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
  - The 2025-11-25 specification defines MCP as an open protocol integrating LLM applications with external data sources and tools.
  - The specification says it defines authoritative protocol requirements based on the TypeScript schema.
  - MCP standardizes sharing contextual information with language models, exposing tools/capabilities to AI systems, and building composable integrations/workflows.
  - The specification describes communication between hosts, clients, and servers using JSON-RPC 2.0.
  - The server feature list separates resources, prompts, and tools; the client feature list separates sampling, roots, and elicitation.
  - Security principles include user consent/control, data privacy, tool safety, and LLM sampling controls; the spec says MCP cannot enforce those principles at protocol level.
- Direct quotation under 25 words: "Share contextual information with language models"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the neutral opening definition that MCP is an integration protocol for context and capabilities, not a complete governance or workflow layer.
- Reliability assessment:
  - High as a primary specification page, but local notes contain only a short scrape snippet.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `05-timeline-and-evolution.md`

### OS-017 - Resources

- Citation key: `mcp-resources-2025-11-25`
- Title: Resources
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/server/resources
- Source type: primary
- Key claims:
  - MCP provides a standardized way for servers to expose resources to clients.
  - Resources let servers share data that provides context to language models, such as files, database schemas, or application-specific information.
  - Each resource is identified by a URI.
  - Resources are application-driven; host applications decide how to incorporate context, and the protocol does not mandate a specific UI pattern.
  - Servers supporting resources must declare the `resources` capability during initialization.
  - Resource capability sub-features are optional: `subscribe` for individual resource-change subscriptions and `listChanged` for available-resource list notifications.
  - Clients discover available resources with `resources/list`, read content with `resources/read`, and discover parameterized resources with `resources/templates/list`.
  - Resources can contain text or binary data and can carry annotations for intended audience, priority, and last-modified time.
  - Security considerations include validating resource URIs, access controls for sensitive resources, proper binary encoding, and permission checks before operations.
- Direct quotation under 25 words: "servers to expose resources to clients"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating resources as a context-exposure primitive that needs data classification, provenance, access control, and audit decisions before government deployment.
- Reliability assessment:
  - High. Versioned primary specification page. Does not by itself classify data sensitivity or prove access-control sufficiency.
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
  - This source supports the broad server-feature taxonomy, but use OS-017 and OS-019 for exact versioned resources and prompts semantics.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the basic capability taxonomy for server review checklists, but should not be used alone for normative prompt semantics.
- Reliability assessment:
  - Medium-high. Official learning material; prefer versioned specification pages for normative primitive semantics.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `09-government-local-authority-ai-hub.md`

### OS-019 - Prompts

- Citation key: `mcp-prompts-2025-11-25`
- Title: Prompts
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/server/prompts
- Source type: primary
- Key claims:
  - MCP provides a standardized way for servers to expose prompt templates to clients.
  - Prompts provide structured messages and instructions for interacting with language models.
  - Clients can discover available prompts, retrieve their contents, and provide arguments to customize them.
  - Prompts are user-controlled and intended for explicit user selection; the protocol does not mandate a specific UI pattern.
  - Servers supporting prompts must declare the `prompts` capability during initialization; `listChanged` indicates prompt-list change notifications.
  - Clients retrieve available prompts with `prompts/list` and retrieve a specific prompt with `prompts/get`.
  - Prompt definitions include name, optional title/description/icons, and optional arguments for customization.
  - Prompt messages contain a role and content; supported content includes text, image, audio, and embedded resource content.
  - Implementations must validate prompt inputs and outputs to prevent injection attacks or unauthorized resource access.
- Direct quotation under 25 words: "servers to expose prompt templates to clients"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating prompts as user-selected instruction templates that require review for instruction integrity, input validation, and access to embedded resources.
- Reliability assessment:
  - High. Versioned primary specification page.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-020 - Lifecycle

- Citation key: `mcp-lifecycle-2025-11-25`
- Title: Lifecycle
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle
- Source type: primary
- Key claims:
  - MCP defines a lifecycle for client-server connections that includes initialization, operation, and shutdown.
  - Initialization covers capability negotiation and protocol-version agreement; operation covers normal protocol communication; shutdown covers graceful termination.
  - The initialization phase must be the first client-server interaction.
  - During initialization, the parties establish protocol-version compatibility, exchange/negotiate capabilities, and share implementation details.
  - The client initiates with an `initialize` request containing supported protocol version, client capabilities, and client implementation information.
  - The server responds with its protocol version, server capabilities, server implementation information, and optional instructions.
  - After successful initialization, the client sends a `notifications/initialized` notification before normal operation.
  - If the server responds with a protocol version the client does not support, the client should disconnect.
  - Client and server capabilities establish which optional protocol features are available during the session.
  - During operation, both parties must respect the negotiated protocol version and only use successfully negotiated capabilities.
  - Error cases include protocol-version mismatch, failure to negotiate required capabilities, and request timeouts.
- Direct quotation under 25 words: "first interaction between client and server"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating connection setup, capability declaration, and state boundaries as architecture-review items rather than invisible implementation details.
- Reliability assessment:
  - High. Versioned primary specification page. Does not by itself prove policy enforcement, authorization sufficiency, or enterprise approval semantics.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`

### OS-021 - Versioning Published MCP Servers

- Citation key: `mcp-server-versioning`
- Title: Versioning Published MCP Servers
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page or specification-adjacent guidance; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/registry/versioning
- Source type: primary
- Key claims:
  - The MCP Registry versioning page is registry-publication guidance, not protocol-version negotiation.
  - The page repeats that the MCP Registry is in preview and may have breaking changes or data resets before general availability.
  - Published MCP servers must define a version string in `server.json`.
  - The version string must be unique for each publication; once published, the version string and other metadata cannot be changed.
  - The registry recommends semantic versioning but supports any version string format.
  - When a server is published, the registry tries to parse its version as semantic versioning for sorting and latest-version marking.
  - Version strings that appear to be version ranges are prohibited.
  - Best-practice guidance says local-server versions should align with package versions, remote-server versions should align with remote API versions, and registry-only metadata updates should use prerelease versions.
- Direct quotation under 25 words: "MCP servers MUST define a version string"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports inventory, immutable metadata, version-pinning, rollback, and supplier-change review for published MCP server metadata.
- Reliability assessment:
  - High for official registry publication guidance. Scope is published-server metadata/version strings, not MCP wire-protocol version negotiation.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `09-government-local-authority-ai-hub.md`

### OS-022 - MCP Registry Moderation Policy

- Citation key: `mcp-registry-moderation-policy`
- Title: The MCP Registry Moderation Policy
- Author/organisation: Model Context Protocol project
- Publication/update date: Current registry documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/registry/moderation-policy
- Source type: primary
- Key claims:
  - The policy applies to the official registry at `registry.modelcontextprotocol.io`; subregistries may have their own moderation policies.
  - The policy describes the registry as permissive and says it only removes illegal content, malware, spam, and completely broken servers.
  - The registry does not make moderation guarantees, and consumers should assume minimal-to-no moderation.
  - The project says it has limited active moderation capacity and relies largely on upstream package registries or downstream subregistries for deeper moderation.
  - The policy says the registry generally will not remove low-quality or buggy servers, servers with security vulnerabilities, duplicate-function servers, or adult-content servers.
  - When the registry removes a server, it usually sets status to `deleted` while metadata remains available via the API; extreme cases may overwrite or erase metadata.
- Direct quotation under 25 words: "consumers should assume minimal-to-no moderation"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the conclusion that a public-sector hub needs its own curation, risk review, and approval layer rather than relying on public-registry moderation.
- Reliability assessment:
  - High for official registry policy; current page should be rechecked before final publication because moderation policy may change.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

### OS-023 - MCP Registry Aggregators

- Citation key: `mcp-registry-aggregators`
- Title: MCP Registry Aggregators
- Author/organisation: Model Context Protocol project
- Publication/update date: Current registry documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/registry/registry-aggregators
- Source type: primary
- Key claims:
  - Aggregators are downstream consumers that add value, such as ratings or security scanning.
  - The official registry exposes an unauthenticated read-only REST API for aggregators to populate their own data stores.
  - Aggregators are expected to scrape registry data on a regular but infrequent basis and persist the data in their own store.
  - The MCP Registry does not provide uptime or data-durability guarantees.
  - Server metadata is generally immutable except for the `status` field.
  - A `deleted` status typically indicates violation of the permissive moderation policy, such as spam, malware, or illegal content.
  - A subregistry can implement the registry OpenAPI spec and inject custom metadata, including user ratings, download counts, and security-scan results.
- Direct quotation under 25 words: "does not provide uptime or data durability guarantees"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports designing private or curated registry layers that persist, enrich, and risk-score upstream public-registry metadata.
- Reliability assessment:
  - High for official registry guidance; current page should be rechecked before final publication because registry API behavior may change during preview.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`

## Known Official-Spec Gaps

These gaps must be filled before final drafting. Exact-extraction blockers for lifecycle, resources, prompts, published-server versioning, and registry moderation/aggregator limits are now closed and backed by BibTeX entries.

| Needed source or cleanup | Placeholder citation key | Current status |
| --- | --- | --- |
| Add BibTeX for exact lifecycle page | `TODO-official-mcp-architecture` | Closed; use `mcp-lifecycle-2025-11-25`. |
| Add BibTeX for exact Resources page | `TODO-mcp-resources` | Closed; use `mcp-resources-2025-11-25`. |
| Add BibTeX for exact Prompts page | `TODO-mcp-prompts` | Closed; use `mcp-prompts-2025-11-25`. |
| Add BibTeX for published-server versioning guidance | `TODO-mcp-server-versioning` | Closed; use `mcp-server-versioning`. Scope is registry server-version metadata, not protocol-version negotiation. |
| Add BibTeX for registry limitations | `TODO-mcp-registry-limitations` | Closed; use `mcp-registry-about`, `mcp-registry-moderation-policy`, and `mcp-registry-aggregators` depending on the claim. |
| Evidence for token-reduction or context-bloat claims | `TODO-context-bloat-token-reduction` | Out of scope for official specs; use `sources/discourse-and-criticism.md` and `sources/vendor-adoption.md` for product or practitioner evidence. |
| Add exact roots quotation | plain-text section TODO | Closed; use OS-014. |
| Add exact tasks quotation | plain-text section TODO | Closed; use OS-015. |
