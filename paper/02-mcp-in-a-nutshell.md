# MCP in a Nutshell

## Status

Starter skeleton with source-backed notes only. Do not expand into full prose until `sources/official-specs.md` is accepted.

## Purpose

Explain the Model Context Protocol at a level suitable for senior technical and public-sector decision-makers: what it is, what it is not, which primitives matter, and where security/governance responsibilities sit.

## Source Boundary

- Primary source notes: `sources/official-specs.md`.
- Supporting security source notes where protocol security behavior is relevant: `sources/security-research.md`.
- No external browsing in this section unless a later task explicitly reopens source discovery.

## Acceptance Criteria

- Defines MCP without vendor marketing language.
- Covers hosts/clients, servers, tools, resources, prompts, roots, sampling, elicitation, transports, initialization/capability negotiation, and authorization at skeleton level.
- Separates facts, reported opinions, and analysis.
- Uses only citation keys present in `latex/references.bib`.
- Calls out what MCP does not provide: business workflow, policy enforcement, source vetting, enterprise registry governance, or complete IAM by itself.
- Leaves TODO placeholders where official spec notes are missing.

## Draft Skeleton

### Facts

- MCP is an open protocol for connecting AI applications to external context and capabilities. [@mcp-intro]
- The official learning material distinguishes MCP architecture and deployment patterns, including remote MCP servers using Streamable HTTP. TODO: verify exact host/client/server lifecycle wording before final prose. [@mcp-architecture]
- Tools are model-controlled server capabilities; this matters because model selection of actions must be governed by the host and deployment policy. [@mcp-tools-2025-11-25]
- Current source notes identify STDIO and Streamable HTTP as core transport areas requiring different security treatment. [@mcp-transports-2025-11-25]
- HTTP authorization is optional in the protocol but, when used, has an OAuth-oriented profile; STDIO is handled differently and should retrieve credentials from the environment. [@mcp-authorization-2025-11-25]
- Sampling allows servers to request model calls through clients, which makes host-side permissioning and human review important. [@mcp-sampling-2025-11-25]
- Elicitation allows servers to request user input through clients and carries explicit constraints around sensitive information. [@mcp-elicitation-2025-11-25]
- Roots are relevant to filesystem or workspace boundaries exposed by clients to servers; final prose should use exact wording from the roots specification. [@mcp-roots-2025-06-18]
- Tasks are part of the 2025-11-25 specification set for long-running or deferred work; final prose should verify exact status and semantics. [@mcp-tasks-2025-11-25]

### Reported Opinions

- TODO: Add only reported opinions that are already captured in `sources/discourse-and-criticism.md`.

### Analysis

- MCP should be described as a capability exchange and invocation protocol, not as a complete AI governance platform.
- For public-sector use, the deployment architecture decides where trust terminates: direct local servers and centrally brokered remote servers create materially different risk profiles.

## Evidence Gaps

- TODO: Add official source entries for resources, prompts, lifecycle/initialization, and versioning before drafting this as continuous prose.
