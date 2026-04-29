# MCP in a Nutshell

## Status

Source-backed skeleton only. This section is not draft-ready prose.

`sources/official-specs.md` now contains accepted notes for several core primitives and TODO/candidate notes for resources, prompts, lifecycle, and server versioning. Treat TODO-prefixed citations as blockers, not evidence.

## Purpose

Explain the Model Context Protocol at a level suitable for senior technical and public-sector decision-makers: what it is, what it is not, which primitives matter, and where security/governance responsibilities sit.

## Source Boundary

- Primary source notes for this section: `sources/official-specs.md`.
- Imported report prose and opaque Deep Research citation markers must not be cited directly.
- No external browsing in this section unless a later task explicitly reopens source discovery.
- TODO citation keys may mark gaps but must not be treated as factual support.

## Acceptance Criteria

- Defines MCP without vendor marketing language.
- Covers hosts/clients, servers, tools, resources, prompts, roots, sampling, elicitation, tasks, transports, initialization/capability negotiation, authorization, discovery/registry, and versioning at skeleton level.
- Separates facts, reported opinions, and analysis.
- Uses only citation keys present in `latex/references.bib`, or plain-text TODO key names where a BibTeX entry does not yet exist.
- Calls out what MCP does not provide: business workflow, policy enforcement, source vetting, enterprise registry governance, complete IAM, or public-sector assurance by itself.
- Leaves TODO placeholders where official spec notes are incomplete.

## Section-Level Acceptance Criteria

| Section | Evidence gate before prose | Acceptance check |
| --- | --- | --- |
| Definition and scope | Use official intro/specification source notes only. | Reader can distinguish MCP from a workflow engine, agent framework, or governance platform. |
| Architecture and lifecycle | Architecture can use accepted official docs; lifecycle/initialization/capability negotiation needs exact source extraction. | Host/client/server roles and local-vs-remote deployment are clear without overstating lifecycle details. |
| Server primitives | Tools are source-ready; resources and prompts remain TODO until exact source text is captured. | Tools, resources, and prompts are defined separately and not collapsed into generic "plugins". |
| Client-side primitives | Roots, sampling, elicitation, and tasks use accepted notes, with roots/tasks caveats preserved. | Client responsibilities are visible, especially where servers request model calls or user input. |
| Transports and authorization | Use versioned transports and authorization notes. | STDIO, Streamable HTTP, and optional HTTP authorization are described without implying complete IAM. |
| Discovery and registry | Registry notes can support public discovery and preview status; limitations need exact extraction. | Public registry, private registry, and enterprise curation are not treated as the same thing. |
| Versioning and maturity | Existing notes are insufficient for protocol-version semantics and server-version controls. | Versioning remains a TODO unless a sourced distinction is added. |
| Public-sector implications | Analysis must reason only from facts above. | Section ends with architecture questions, not procurement recommendations. |

## Draft Skeleton

### 1. Definition and Scope

#### Facts

- MCP is an open protocol for connecting AI applications to external context and capabilities. [@mcp-intro]
- The 2025-11-25 specification overview source note supports the high-level framing that MCP standardizes sharing contextual information and exposing tools/capabilities. [@mcp-specification-2025-11-25]
- Tools are model-controlled server capabilities. [@mcp-tools-2025-11-25]

#### Reported Opinions

- None in this section. TODO: add only if `sources/discourse-and-criticism.md` later supplies attributed opinions.

#### Analysis Placeholders

- MCP should be described as a capability exchange and invocation protocol.
- MCP should not be described as a complete AI governance platform, workflow layer, enterprise registry, or IAM system.

#### Section Acceptance

- TODO: Final prose must define "capability" using official wording or avoid the term if unsupported.
- TODO: Extract exact definition wording from the specification overview before final prose.

### 2. Architecture and Lifecycle

#### Facts

- Official architecture learning material describes MCP architecture and deployment patterns. [@mcp-architecture]
- The accepted architecture note supports distinguishing local and remote MCP server patterns, including remote servers over Streamable HTTP. [@mcp-architecture]
- TODO: Exact lifecycle, initialization, capability-negotiation, and state-management wording remains incomplete in local notes. [@TODO-official-mcp-architecture]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- A Government / Local Authority AI Hub should identify where MCP trust terminates: user desktop, host application, enterprise broker, gateway, or remote server.
- Architecture diagrams should show host/client, server, upstream systems, identity provider, registry/catalog, and audit/logging boundary as separate boxes unless a source supports collapsing them.

#### Section Acceptance

- TODO: Add exact initialization sequence only after the lifecycle page is extracted.
- TODO: Avoid saying capability negotiation enforces policy; current notes support negotiation/state management as lifecycle concerns, not policy sufficiency.

### 3. Server Primitives: Tools, Resources, Prompts

#### Facts

- Tools are designed to be model-controlled and can carry annotations such as read-only, destructive, idempotent, or open-world behavior. [@mcp-tools-2025-11-25]
- TODO: Resources are supported only at skeleton level by the local source note: servers expose resources to clients. The durable resource URL and exact semantics still need extraction. [@TODO-mcp-resources]
- TODO: Prompts remain under-sourced. Existing local notes point to official server concepts and imported-report orientation, but not enough exact text for final prose. [@TODO-mcp-prompts]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Tools create action risk because a model may select an operation; resources create data-exposure risk because server-provided context may enter the host/model path; prompts create instruction-shaping risk because reusable prompt templates can steer model behavior.
- TODO: The previous analysis sentence is a conceptual classification; verify each primitive's official semantics before final wording.

#### Section Acceptance

- Final tools prose must identify which controls are specified by MCP and which belong to the host/deployment policy.
- Final resources prose must cover data classification, provenance, and access control only after exact resource semantics are extracted.
- Final prompts prose must not imply prompts are tools or resources unless an official source supports the relationship.

### 4. Client-Side Primitives: Roots, Sampling, Elicitation, Tasks

#### Facts

- Roots define filesystem or workspace boundaries exposed by the client to the server; current accepted note is versioned 2025-06-18 rather than 2025-11-25. [@mcp-roots-2025-06-18]
- Sampling allows servers to request LLM sampling through clients, while clients retain control over model access, model selection, and permissions. [@mcp-sampling-2025-11-25]
- Elicitation allows servers to request structured user input through clients and explicitly forbids form-mode elicitation for sensitive information. [@mcp-elicitation-2025-11-25]
- Tasks are recorded in the 2025-11-25 specification set for long-running or deferred work; exact operational semantics still need final extraction before prose. [@mcp-tasks-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Client-side primitives show that MCP is not only server tool calling; hosts mediate workspace scope, model calls, user-input requests, and potentially long-running operations.
- Public-sector deployments should decide whether sampling and elicitation are disabled, allowed with approval, or routed through an enterprise-controlled host.

#### Section Acceptance

- TODO: Add exact roots quotation before final prose.
- TODO: Add exact tasks quotation before describing cancellation, tracing, or audit expectations.

### 5. Transports and Authorization

#### Facts

- Current accepted notes identify STDIO and Streamable HTTP as core transport areas requiring different security treatment. [@mcp-transports-2025-11-25]
- HTTP servers must validate incoming `Origin` headers; local HTTP servers should bind to localhost and authenticate connections to reduce DNS rebinding risk. [@mcp-transports-2025-11-25]
- Authorization is optional for MCP implementations. [@mcp-authorization-2025-11-25]
- For HTTP transports, MCP defines an OAuth-oriented authorization profile; STDIO uses a different credential pattern and should retrieve credentials from the environment. [@mcp-authorization-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- The paper should separate protocol authorization from enterprise IAM. MCP can define HTTP authorization behavior without supplying the whole identity, approval, audit, and entitlement model needed by a public-sector hub.
- Transport choice changes the control baseline: local STDIO, local HTTP, and remote HTTP have different operational risks.

#### Section Acceptance

- Final prose must not say MCP "has no security"; it must say which security properties are protocol-specified and which are deployment responsibilities.
- Final prose must not say authorization is mandatory unless the claim is scoped to a deployment profile rather than MCP itself.

### 6. Discovery and Registry

#### Facts

- The MCP Registry launched in preview as an open catalog and API for discovering publicly available MCP servers. [@mcp-registry-preview-2025-09-08]
- The registry is the official centralized metadata repository for publicly accessible MCP servers. [@mcp-registry-about]
- The roadmap identifies enterprise-managed authorization, audit trails, gateway/proxy patterns, configuration portability, and other enterprise-readiness themes. [@mcp-roadmap-2026-03-05]
- The transport-future source associates remote MCP deployments with Streamable HTTP and notes future transport/discovery concerns in local notes; exact wording still needs extraction for final prose. [@mcp-transport-future-2025-12-19]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Public discovery is not the same as public-sector approval. A hub may need a private or curated registry even if the official public registry matures.
- Registry metadata should be treated as discovery input, not proof of server safety, supplier assurance, data classification, or permission suitability.

#### Section Acceptance

- TODO: Extract exact official wording before stating registry moderation, durability, direct-host-consumption, or private-registry limitations.
- TODO: Do not describe server cards as stable protocol behavior until an accepted source note supports that status.

### 7. Versioning and Maturity

#### Facts

- The local notes include an official page title, "Versioning Published MCP Servers", but not enough URL/text detail for final claims.
- TODO: Add exact server-versioning evidence before citing versioning claims. [@TODO-mcp-server-versioning]
- TODO: Do not conflate server package/version labels, MCP protocol versions, and lifecycle capability negotiation without separate evidence.

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- A public-sector hub will need version pinning, compatibility testing, rollback, and dependency review, whether those are supplied by MCP standards or by local governance.

#### Section Acceptance

- Final prose must state which kind of versioning is being discussed: protocol version, server implementation version, package version, capability set, or registry metadata version.

### 8. What MCP Does Not Provide

#### Facts

- Authorization is optional in the protocol. [@mcp-authorization-2025-11-25]
- The registry sources support discovery metadata, not full enterprise curation or approval. [@mcp-registry-preview-2025-09-08] [@mcp-registry-about]
- The roadmap source identifies enterprise-readiness themes as continuing work rather than already-finished control-plane guarantees. [@mcp-roadmap-2026-03-05]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- MCP does not by itself provide business workflow, case-management semantics, enterprise policy enforcement, data-governance classification, supplier assurance, complete IAM, audit-grade logging, or safe tool composition.
- Those controls can be layered around MCP through hosts, gateways, private registries, direct APIs, workflow engines, or procurement controls.

#### Section Acceptance

- Every "does not provide" statement must be framed as analysis from the source-backed facts, not as a normative spec quote unless exact spec language is added.

## Evidence Gaps

- TODO: Extract exact overview wording for `mcp-specification-2025-11-25` before final prose.
- TODO: Replace `TODO-mcp-resources` with an accepted resources citation after exact URL/text extraction.
- TODO: Replace `TODO-mcp-prompts` with an accepted prompts citation after exact URL/text extraction.
- TODO: Replace `TODO-official-mcp-architecture` with accepted lifecycle/initialization/capability-negotiation citation(s).
- TODO: Replace `TODO-mcp-server-versioning` with accepted server-versioning source text and URL.
- TODO: Extract exact registry limitation wording before final prose on moderation, durability, direct host consumption, or private registries. [@TODO-mcp-registry-limitations]
