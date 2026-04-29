# MCP in a Nutshell

## Status

Source-ready skeleton for official protocol basics. This section is not draft-ready prose.

`sources/official-specs.md` now contains accepted exact-extraction notes for resources, prompts, lifecycle/initialization/capability negotiation, published-server versioning, registry limitation wording, and the specification overview. The temporary TODO citation placeholders from the extraction lane have been replaced with BibTeX-backed keys.

## Purpose

Explain the Model Context Protocol at a level suitable for senior technical and public-sector decision-makers: what it is, what it is not, which primitives matter, and where security/governance responsibilities sit.

## Source Boundary

- Primary source notes for this section: `sources/official-specs.md`.
- Imported report prose and opaque Deep Research citation markers must not be cited directly.
- This retest used only official MCP pages directly implied by local notes/imports; all fetched pages are recorded in `sources/official-specs.md` with Date accessed 2026-04-29.
- TODO marker names may mark evidence gaps. Where exact extraction is complete, use the non-TODO BibTeX key recorded in `sources/official-specs.md`.

## Acceptance Criteria

- Defines MCP without vendor marketing language.
- Covers hosts/clients, servers, tools, resources, prompts, roots, sampling, elicitation, tasks, transports, initialization/capability negotiation, authorization, discovery/registry, and versioning at skeleton level.
- Separates facts, reported opinions, and analysis.
- Uses only citation keys present in `latex/references.bib`, or plain-text TODO marker names where evidence extraction is still incomplete.
- Calls out what MCP does not provide: business workflow, policy enforcement, source vetting, enterprise registry governance, complete IAM, or public-sector assurance by itself.
- Leaves TODO placeholders only where non-official or non-protocol evidence remains incomplete.

## Section-Level Acceptance Criteria

| Section | Evidence gate before prose | Acceptance check |
| --- | --- | --- |
| Definition and scope | Use official intro/specification source notes only; exact overview wording is now extracted. | Reader can distinguish MCP from a workflow engine, agent framework, or governance platform. |
| Architecture and lifecycle | Architecture can use accepted official docs; exact lifecycle/initialization/capability-negotiation source text is now extracted and backed by `mcp-lifecycle-2025-11-25`. | Host/client/server roles and local-vs-remote deployment are clear without overstating lifecycle or policy semantics. |
| Server primitives | Tools, resources, and prompts now have exact official source notes and BibTeX-backed citation keys. | Tools, resources, and prompts are defined separately and not collapsed into generic "plugins". |
| Client-side primitives | Roots, sampling, elicitation, and tasks use accepted notes; roots/tasks exact quotation gaps are closed. | Client responsibilities are visible, especially where servers request model calls, user input, workspace access, or long-running operations. |
| Transports and authorization | Use versioned transports and authorization notes. | STDIO, Streamable HTTP, and optional HTTP authorization are described without implying complete IAM. |
| Discovery and registry | Registry notes now support public discovery, preview status, private-server limits, downstream aggregation, direct-host-consumption limits, moderation limits, and durability limits; some exact limitation pages need BibTeX. | Public registry, private registry, and enterprise curation are not treated as the same thing. |
| Versioning and maturity | Published-server registry versioning is now extracted; protocol-version negotiation is separately sourced by lifecycle. | Versioning claims specify whether they mean protocol version, server metadata version, package/API version, capability set, or registry metadata. |
| Public-sector implications | Analysis must reason only from facts above. | Section ends with architecture questions, not procurement recommendations. |

## Draft Skeleton

### 1. Definition and Scope

#### Facts

- MCP is an open protocol for connecting AI applications to external context and capabilities. [@mcp-intro]
- The 2025-11-25 specification says MCP integrates LLM applications with external data sources and tools, and standardizes sharing contextual information, exposing tools/capabilities, and building composable integrations/workflows. [@mcp-specification-2025-11-25]
- The specification describes MCP communication between hosts, clients, and servers using JSON-RPC 2.0. [@mcp-specification-2025-11-25]
- The specification separates server features (resources, prompts, tools) from client features (sampling, roots, elicitation). [@mcp-specification-2025-11-25]
- Tools are model-controlled server capabilities. [@mcp-tools-2025-11-25]

#### Reported Opinions

- None in this section. TODO: add only if `sources/discourse-and-criticism.md` later supplies attributed opinions.

#### Analysis Placeholders

- MCP should be described as a capability exchange and invocation protocol.
- MCP should not be described as a complete AI governance platform, workflow layer, enterprise registry, or IAM system.

#### Section Acceptance

- CLOSED: Exact overview wording extracted in `sources/official-specs.md` OS-016.
- Final prose may use "capabilities" as an official term, but should not invent a broader governance meaning for it.

### 2. Architecture and Lifecycle

#### Facts

- Official architecture learning material describes MCP architecture and deployment patterns. [@mcp-architecture]
- The accepted architecture note supports distinguishing local and remote MCP server patterns, including remote servers over Streamable HTTP. [@mcp-architecture]
- Exact lifecycle extraction records initialization, operation, and shutdown as the lifecycle phases. [@mcp-lifecycle-2025-11-25]
- Initialization is the first client-server interaction. The client sends `initialize` with protocol version, capabilities, and client implementation information; the server responds with protocol version, capabilities, server information, and optional instructions; the client then sends `notifications/initialized`. [@mcp-lifecycle-2025-11-25]
- Lifecycle version negotiation and capability negotiation establish protocol-version compatibility and which optional features are available during the session. [@mcp-lifecycle-2025-11-25]
- During operation, both parties must respect the negotiated protocol version and only use successfully negotiated capabilities. [@mcp-lifecycle-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- A Government / Local Authority AI Hub should identify where MCP trust terminates: user desktop, host application, enterprise broker, gateway, or remote server.
- Architecture diagrams should show host/client, server, upstream systems, identity provider, registry/catalog, and audit/logging boundary as separate boxes unless a source supports collapsing them.

#### Section Acceptance

- CLOSED: Exact initialization sequence and capability-negotiation wording extracted in `sources/official-specs.md` OS-020.
- CLOSED: lifecycle facts now cite `mcp-lifecycle-2025-11-25`.
- Keep caveat: capability negotiation does not equal policy enforcement, authorization sufficiency, or enterprise approval.

### 3. Server Primitives: Tools, Resources, Prompts

#### Facts

- Tools are designed to be model-controlled and can carry annotations such as read-only, destructive, idempotent, or open-world behavior. [@mcp-tools-2025-11-25]
- Server-feature overview separates prompts, resources, and tools, and describes their control hierarchy as user-controlled, application-controlled, and model-controlled respectively. [@mcp-specification-2025-11-25]
- Exact resources extraction records resources as server-exposed data for model context, identified by URI, application-driven by the host, and discoverable/readable through `resources/list`, `resources/read`, and `resources/templates/list`. [@mcp-resources-2025-11-25]
- Resources capability sub-features `subscribe` and `listChanged` are optional; the resources page also records URI validation, access controls for sensitive resources, binary encoding, and permission checks as security considerations. [@mcp-resources-2025-11-25]
- Exact prompts extraction records prompts as server-exposed prompt templates, user-controlled by explicit selection, discoverable with `prompts/list`, retrievable with `prompts/get`, and customizable with arguments. [@mcp-prompts-2025-11-25]
- Prompt messages can contain text, image, audio, or embedded resource content; implementations must validate prompt inputs and outputs against injection and unauthorized resource access. [@mcp-prompts-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Tools create action risk because a model may select an operation; resources create data-exposure risk because server-provided context may enter the host/model path; prompts create instruction-shaping risk because reusable prompt templates can steer model behavior.
- The preceding classification is analysis from the official control hierarchy and exact primitive semantics, not a quoted MCP taxonomy.

#### Section Acceptance

- Final tools prose must identify which controls are specified by MCP and which belong to the host/deployment policy.
- CLOSED: Exact resources and prompts semantics extracted in `sources/official-specs.md` OS-017 and OS-019.
- CLOSED: resources facts now cite `mcp-resources-2025-11-25`.
- CLOSED: prompts facts now cite `mcp-prompts-2025-11-25`.
- Final resources prose may discuss data classification, provenance, and access control as deployment analysis, grounded in the resource-content and resource-security facts.
- Final prompts prose must not imply prompts are tools or resources; embedded resources in prompts should be described only as prompt-message content.

### 4. Client-Side Primitives: Roots, Sampling, Elicitation, Tasks

#### Facts

- Roots define filesystem boundaries exposed by the client to the server; the current accepted note is versioned 2025-06-18 rather than 2025-11-25. [@mcp-roots-2025-06-18]
- Clients that support roots declare the `roots` capability during initialization, and servers can request root lists with `roots/list`. [@mcp-roots-2025-06-18]
- Root URIs must be `file://` URIs in the accepted specification page; clients must expose only roots with appropriate permissions and servers should respect root boundaries. [@mcp-roots-2025-06-18]
- Sampling allows servers to request LLM sampling through clients, while clients retain control over model access, model selection, and permissions. [@mcp-sampling-2025-11-25]
- Elicitation allows servers to request structured user input through clients and explicitly forbids form-mode elicitation for sensitive information. [@mcp-elicitation-2025-11-25]
- Tasks were introduced in MCP version 2025-11-25 and are described as experimental. [@mcp-tasks-2025-11-25]
- Tasks support durable state for polling and deferred result retrieval, with a two-phase pattern: initial task data followed by the actual result through `tasks/result` after completion. [@mcp-tasks-2025-11-25]
- Task operations include `tasks/get`, `tasks/list`, and `tasks/cancel`; terminal task states include completed, failed, and cancelled. [@mcp-tasks-2025-11-25]
- Task security guidance includes binding tasks to the authorization context where available, using high-entropy task IDs where context binding is unavailable, rate limiting, and lifecycle audit logging. [@mcp-tasks-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Client-side primitives show that MCP is not only server tool calling; hosts mediate workspace scope, model calls, user-input requests, and potentially long-running operations.
- Public-sector deployments should decide whether sampling and elicitation are disabled, allowed with approval, or routed through an enterprise-controlled host.
- Public-sector deployments should decide whether roots are limited to managed workspaces and whether tasks require explicit audit, timeout, cancellation, and ownership controls.

#### Section Acceptance

- CLOSED: Exact roots quotation and operational semantics extracted in `sources/official-specs.md` OS-014.
- CLOSED: Exact tasks quotation and operational semantics extracted in `sources/official-specs.md` OS-015.

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
- Current registry documentation says the registry is in preview and may have breaking changes or data resets before general availability. [@mcp-registry-about]
- Registry metadata points to code/binaries in package registries or remote server URLs; the registry hosts metadata, not the server packages themselves. [@mcp-registry-about]
- The registry does not support private servers; it recommends hosting a private MCP registry for servers on private networks or private package registries. [@mcp-registry-about]
- The registry is intended primarily for downstream aggregators, its metadata is deliberately unopinionated, and host applications are not intended to consume it directly. [@mcp-registry-about]
- Registry security scanning is delegated to underlying package registries and downstream aggregators; the registry focuses on namespace authentication and metadata hosting. [@mcp-registry-about]
- Exact moderation-policy extraction says consumers should assume minimal-to-no moderation and that the official registry generally will not remove low-quality, buggy, vulnerable, duplicate-function, or adult-content servers. [@mcp-registry-moderation-policy]
- Exact aggregator extraction says aggregators should persist their own copy and that the official registry does not provide uptime or data-durability guarantees. [@mcp-registry-aggregators]
- The roadmap identifies enterprise-managed authorization, audit trails, gateway/proxy patterns, configuration portability, and other enterprise-readiness themes. [@mcp-roadmap-2026-03-05]
- The transport-future source identifies remote-scale challenges including sticky routing, stateful connections, routing complexity, backend-storage burden, ambiguous session scope, and server-card exploration; server cards remain roadmap direction, not stable protocol behavior in this source. [@mcp-transport-future-2025-12-19]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- Public discovery is not the same as public-sector approval. A hub may need a private or curated registry even if the official public registry matures.
- Registry metadata should be treated as discovery input, not proof of server safety, supplier assurance, data classification, or permission suitability.

#### Section Acceptance

- CLOSED: Exact official wording extracted for private-server limits, direct-host-consumption limits, moderation limits, data-durability limits, downstream aggregation, and security-scanning delegation.
- CLOSED: moderation and aggregator facts now cite `mcp-registry-moderation-policy` and `mcp-registry-aggregators`.
- Do not describe server cards as stable protocol behavior; current accepted notes support only roadmap/exploration wording.

### 7. Versioning and Maturity

#### Facts

- Exact published-server versioning extraction records registry-publication guidance, not protocol-version negotiation. [@mcp-server-versioning]
- Published MCP servers must define a version string in `server.json`; the version string must be unique for each publication, and once published the version string and other metadata cannot be changed. [@mcp-server-versioning]
- The registry recommends semantic versioning, supports other version-string formats, parses semantic versions for sorting/latest marking where possible, and prohibits version strings that appear to be version ranges. [@mcp-server-versioning]
- Best-practice guidance says local-server versions should align with underlying package versions, remote-server versions should align with remote API versions, and registry-only metadata updates should use prerelease versions. [@mcp-server-versioning]
- Protocol-version negotiation is separately sourced in the lifecycle page: the client sends a supported protocol version in `initialize`; the server either replies with that version or another supported version; unsupported server replies should lead the client to disconnect. [@mcp-lifecycle-2025-11-25]

#### Reported Opinions

- None in this section.

#### Analysis Placeholders

- A public-sector hub will need version pinning, compatibility testing, rollback, and dependency review, whether those are supplied by MCP standards or by local governance.
- Treat registry metadata immutability as useful for inventory and rollback review, but not as proof that an implementation is secure, compatible, or approved.

#### Section Acceptance

- CLOSED: Exact published-server versioning URL/text extracted in `sources/official-specs.md` OS-021.
- CLOSED: published-server versioning facts now cite `mcp-server-versioning`.
- CLOSED: protocol-version lifecycle facts now cite `mcp-lifecycle-2025-11-25`.
- Final prose must state which kind of versioning is being discussed: protocol version, server implementation version, package version, capability set, or registry metadata version.

### 8. What MCP Does Not Provide

#### Facts

- Authorization is optional in the protocol. [@mcp-authorization-2025-11-25]
- The specification overview says MCP itself cannot enforce its security principles at protocol level; implementors should build consent, authorization, access-control, and data-protection flows around it. [@mcp-specification-2025-11-25]
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

- CLOSED: Exact overview wording for `mcp-specification-2025-11-25` extracted.
- CLOSED: Exact Resources URL/text extracted and cited as `mcp-resources-2025-11-25`.
- CLOSED: Exact Prompts URL/text extracted and cited as `mcp-prompts-2025-11-25`.
- CLOSED: Exact lifecycle/initialization/capability-negotiation URL/text extracted and cited as `mcp-lifecycle-2025-11-25`.
- CLOSED: Exact published-server versioning URL/text extracted and cited as `mcp-server-versioning`.
- CLOSED: Exact registry limitation wording extracted for moderation, durability, direct host consumption, private registries, and downstream aggregation; moderation and durability now use `mcp-registry-moderation-policy` and `mcp-registry-aggregators`.
- CLOSED: Exact roots quotation and operational semantics extracted in `sources/official-specs.md` OS-014.
- CLOSED: Exact tasks quotation and operational semantics extracted in `sources/official-specs.md` OS-015.
