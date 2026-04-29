# Government and Local-Authority AI Hub

## Status

Started skeleton. This section is not draft-ready and must not make final recommendations until sections 02, 04, 06, and the relevant source notes are source-ready.

## Purpose

Translate the technical assessment into architecture options, governance controls, procurement implications, and recommendation conditions for a Government / Local Authority AI Hub.

## Source Boundary

- Public-sector guidance: `sources/security-research.md`.
- Protocol and ecosystem notes: `sources/official-specs.md`, `sources/vendor-adoption.md`, `sources/alternatives-skills-agents.md`.
- Risk and mitigation context: `paper/04-technical-critiques-and-mitigations.md` and its source boundary.
- Do not cite the imported Deep Research report directly.
- Do not turn vendor product positioning into public-sector recommendations without accepted controls evidence.

## Acceptance Criteria

- Provides at least three architecture options with trade-offs.
- Includes a risk register with owners and controls.
- States mandatory controls for any MCP pilot.
- Separates procurement requirements from engineering implementation details.
- Separates facts, reported opinions, and analysis.
- Marks recommendation conditions as provisional until source sections are source-ready.

## Draft Skeleton

### Facts

- Public-sector AI security guidance requires security to be considered across design, development, deployment, and operation. [@ncsc-secure-ai-development-2023-11-27]
- UK AI cyber-security guidance treats AI systems as distinct from conventional software and includes supply-chain, monitoring, and governance expectations. [@dsit-ai-cyber-security-code-2025-01-31]
- NIST's generative AI profile provides a risk-management frame for governance, mapping, measurement, and management of generative AI risks. [@nist-genai-profile-2026-04-08]
- MCP authorization is optional at protocol level, while HTTP deployments can use the MCP authorization profile with audience-bound resource indicators. [@mcp-authorization-2025-11-25]
- MCP security guidance identifies confused deputy, token passthrough, SSRF, session hijacking, and local server compromise as MCP-specific risks. [@mcp-security-best-practices]
- MCP tools are model-controlled capabilities, which makes host-side tool visibility, approval, and policy important for high-risk operations. [@mcp-tools-2025-11-25]

### Reported Opinions

- Reported vendor positions and positive adoption claims should be drawn from `sources/vendor-adoption.md` only after exact source text is accepted.
- Reported criticism should be drawn from `sources/discourse-and-criticism.md` only with narrow attribution and scope.

### Analysis

- Treat MCP as a connector layer, not the trust boundary. The AI Hub should decide where identity, approval, audit, data classification, registry curation, and incident response are enforced.
- Compare at least four architecture options before recommending a pattern:

| Option | Pattern | Likely fit | Primary trade-off |
| --- | --- | --- | --- |
| Direct APIs/function calling only | Existing API gateways and service IAM expose narrowly scoped functions to one or more AI clients. | Sensitive, latency-critical, or low-integration-count workflows. | Less MCP portability; more bespoke wrappers per client. |
| MCP through enterprise broker | MCP servers terminate behind a hub-owned gateway/broker with central IAM, policy, logging, allowlists, and server inventory. | Reusable cross-client connectors where controls can be centralized. | Higher initial operating complexity. |
| Managed vendor platform | Vendor-hosted agent/app environment exposes MCP-compatible connectors under tenant controls. | Existing Microsoft/OpenAI/GitHub/Cloudflare estates where platform administration is already mature. | Platform dependency and evidence gaps around audit depth, data handling, and exit path. |
| Developer sandbox only | Local or constrained MCP use for engineering productivity, with no production data or destructive operations. | Low-risk experimentation and connector evaluation. | Benefits do not automatically transfer to public-service workflows. |
| Hybrid tiered model | Direct APIs for high-risk paths, MCP broker for reusable bounded connectors, and Skills/frameworks for orchestration or procedural knowledge. | Most likely candidate for a Government / Local Authority AI Hub if evidence supports controls. | Requires clear ownership boundaries and procurement discipline. |

### Risk Register Skeleton

| Risk | Likely owner | Control candidates | Evidence state |
| --- | --- | --- | --- |
| Unclear trust boundary | AI Hub architecture owner | Define broker, host, registry, IdP, server, and upstream-system responsibilities. | Supported by protocol/security facts; final design needs source-ready section 02 and 04. |
| Weak identity and authorization | IAM owner and service owner | Mandatory local auth profile; audience-bound tokens; least-privilege scopes; no token passthrough. | Supported by MCP authorization/security guidance. |
| Unsafe tool invocation | Product owner and host/client owner | Read/write/destructive tool tiers; approvals; user-visible tool invocation; policy checks before execution. | Supported by tools spec and security notes. |
| Discovery and registry trust | Platform owner | Private registry or allowlist; owner verification; change review; server inventory. | Still depends on exact registry limitation extraction. |
| Prompt/tool poisoning | Security owner | Metadata review; signing/provenance; red-team tests; cross-server dataflow restrictions. | Supported by security notes; mitigation strength remains implementation-dependent. |
| Context bloat and cost | Platform owner | Progressive discovery; toolset consolidation; context budgets; code-mediated access where justified. | Product-specific token-saving evidence exists; independent/cross-vendor corroboration remains open. |
| Supply chain and local servers | Security and endpoint owners | Dependency pinning; SBOMs; sandboxing; endpoint policy; kill switches. | Supported by advisories and public-sector secure-development guidance. |
| Audit and accountability gaps | SIRO / information governance owner | Logs tied to user, tool, server, data class, approval, and upstream action. | Public-sector control need is clear; MCP-specific audit semantics remain a source gap. |
| Procurement lock-in | Commercial owner | Exit path, data processing terms, support model, registry portability, and contract controls. | Requires procurement-specific evidence before final recommendations. |

### Provisional Adoption Gates

- No production pilot without a named service owner, security owner, and data owner.
- No unmanaged public registry consumption in production.
- No destructive or externally communicating tools without explicit approval, logging, and rollback or compensating controls.
- No sensitive data access through local unmanaged servers.
- No final recommendation until exact source extraction closes the section 02, 04, 06, and vendor-control gaps.

## Evidence Gaps

- Exact registry limitation wording is needed before specifying private-registry requirements as more than an analysis condition.
- Product-control evidence is needed before relying on managed vendor MCP offerings for audit, data residency, incident response, or procurement claims.
- Procurement-specific evidence is needed before making recommendations about proprietary app ecosystems.
- Section 09 should become source-ready only after the main technical and alternatives sections have stabilized.
