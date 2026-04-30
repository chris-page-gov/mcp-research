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
- Current MCP registry documentation says the official registry is for publicly accessible MCP servers, does not support private servers, is intended primarily for downstream aggregators, and delegates security scanning to package registries and downstream aggregators. [@mcp-registry-about]
- MCP registry moderation guidance says consumers should assume minimal-to-no moderation, and aggregator guidance says the registry does not provide uptime or data-durability guarantees. [@mcp-registry-moderation-policy] [@mcp-registry-aggregators]
- MCP resources expose data as context to clients and need access-control decisions before sensitive resources are incorporated into a Government / Local Authority AI Hub. [@mcp-resources-2025-11-25]
- Public-sector AI security and risk-management guidance supports lifecycle governance, supply-chain controls, monitoring, and risk management for operational AI systems. [@ncsc-secure-ai-development-2023-11-27] [@dsit-ai-cyber-security-code-2025-01-31] [@nist-genai-profile-2026-04-08]

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

### Control Mapping Skeleton

This mapping is analysis-stage. It converts accepted source notes into control questions for an AI Hub design review; it does not make final adoption recommendations.

| Control lane | Hub decision to make | Control candidates to map | Evidence state |
| --- | --- | --- | --- |
| Identity and authorization | Decide where enterprise identity is enforced: host, broker/gateway, MCP server, upstream system, or vendor platform. | Mandatory local authorization profile for any HTTP server; audience-bound tokens; least-privilege scopes; no token passthrough; server/tool identity inventory; short-lived credentials and vault-backed secrets where servers need non-human access. | Supported by MCP authorization/security notes and public-sector AI supply-chain guidance. [@mcp-authorization-2025-11-25] [@mcp-security-best-practices] [@dsit-ai-cyber-security-code-2025-01-31] Product-specific tenant, residency, and support evidence remains open: `TODO-product-control-depth`. |
| Registry and allowlist | Decide whether the hub consumes the public registry only as upstream metadata, operates a private/curated registry, or uses product-specific registry controls. | Private or curated registry; allowlist by server, tool, version, owner, data class, and environment; namespace/owner verification; metadata persistence; change review before new metadata reaches model context; emergency denylist. | Supported for public-registry limitations and product-level allowlist existence. [@mcp-registry-about] [@mcp-registry-moderation-policy] [@mcp-registry-aggregators] [@github-copilot-mcp-registry-allowlist-2025-11-18] Suitability of managed product controls remains open: `TODO-product-control-depth`. |
| Approval and human control | Decide which operations require user confirmation, business approval, or automated policy denial before execution. | Tool tiers for read-only, write, destructive, external communication, and citizen/service-record access; user-visible tool invocation; approval records tied to actual scopes; stricter handling of sampling and elicitation. | Supported by MCP tools, sampling, elicitation, and security notes. [@mcp-tools-2025-11-25] [@mcp-sampling-2025-11-25] [@mcp-elicitation-2025-11-25] Host UX and enforcement depth remain implementation-dependent. |
| Audit and accountability | Decide the minimum event model for audit across host, broker, server, upstream system, and vendor platform. | Logs tied to user, server, tool, resource/data class, prompt or task context, approval decision, token scope, upstream action, result status, version, and incident correlation ID. | Public-sector need is supported by AI governance/security notes and MCP task lifecycle audit semantics. [@nist-genai-profile-2026-04-08] [@mcp-tasks-2025-11-25] MCP-specific cross-product audit semantics and vendor retention depth remain evidence gaps: `TODO-product-control-depth`. |
| Data classification | Decide which data classes may be exposed as resources, tool inputs, tool outputs, prompts, elicitation flows, or sampling requests. | Data-class labels in registry entries; resource and tool review by data owner; prohibition on sensitive secrets through form-mode elicitation; redaction/minimisation before model context; provenance and monitoring for operational AI data flows. | Supported by MCP resources/elicitation notes and public-sector AI security guidance. [@mcp-resources-2025-11-25] [@mcp-elicitation-2025-11-25] [@ncsc-secure-ai-development-2023-11-27] Specific council data-taxonomy mapping is local design work, not source evidence. |
| Incident response | Decide how the hub revokes access, disables servers/tools, rotates credentials, preserves logs, and notifies owners during an MCP incident. | Kill switch by server/tool/version; credential rotation; package/advisory monitoring; rollback to pinned versions; log preservation; incident owner routing; supplier notification path; post-incident change review. | Supported by public advisories, malicious-package notes, and public-sector AI security guidance at control-theme level. [@mcp-python-sdk-dns-rebinding-2025-12-02] [@mcp-remote-cve-2025-6514] [@postmark-mcp-backdoor-2025-09-25] [@dsit-ai-cyber-security-code-2025-01-31] Product SLAs and supplier incident commitments remain open: `TODO-product-control-depth`. |
| Supplier ownership | Decide who owns each connector and who is accountable for source, build, support, security fixes, and operational changes. | Named service owner, security owner, data owner, and supplier owner; SBOM/dependency evidence; maintained fork or support route for open-source servers; change-control requirements for manifests, schemas, prompts, and tool descriptions. | Supported by reference-server and supply-chain notes at analysis level. [@mcp-servers-security-overview] [@dsit-ai-cyber-security-code-2025-01-31] Supplier assurance details remain procurement/product evidence gaps. |
| Procurement and exit | Decide what contract and operating evidence is required before relying on managed vendor MCP offerings or proprietary app ecosystems. | Contractual support model; data processing and residency terms; audit-log access and retention; vulnerability disclosure and patch SLAs; licensing/billing model; registry portability; export/exit path; restrictions on unofficial pass-through connectors where app-store governance applies. | Public-sector AI supply-chain baseline is available, and vendor app/process facts exist, but no accepted public-sector procurement-specific evidence closes the blocker. [@dsit-ai-cyber-security-code-2025-01-31] [@openai-app-submission-guidelines] [@openai-app-submission-flow] [@microsoft-dynamics365-mcp-2026-03-11] TODO: `TODO-proprietary-connector-procurement-evidence`. |

### Risk Register Skeleton

| Risk | Likely owner | Control candidates | Evidence state |
| --- | --- | --- | --- |
| Unclear trust boundary | AI Hub architecture owner | Define broker, host, registry, IdP, server, and upstream-system responsibilities. | Supported by protocol/security facts; final design needs source-ready section 02 and 04. |
| Weak identity and authorization | IAM owner and service owner | Mandatory local auth profile; audience-bound tokens; least-privilege scopes; no token passthrough. | Supported by MCP authorization/security guidance. |
| Unsafe tool invocation | Product owner and host/client owner | Read/write/destructive tool tiers; approvals; user-visible tool invocation; policy checks before execution. | Supported by tools spec and security notes. |
| Discovery and registry trust | Platform owner | Private registry or allowlist; owner verification; change review; server inventory. | Official public-registry limitations are now source-backed; AI Hub control mapping remains analysis-stage. |
| Prompt/tool poisoning | Security owner | Metadata review; signing/provenance; red-team tests; cross-server dataflow restrictions. | Supported by security notes; mitigation strength remains implementation-dependent. |
| Context bloat and cost | Platform owner | Progressive discovery; toolset consolidation; context budgets; code-mediated access where justified. | Product-specific token-saving evidence exists; independent/cross-vendor corroboration remains open. |
| Supply chain and local servers | Security and endpoint owners | Dependency pinning; SBOMs; sandboxing; endpoint policy; kill switches. | Supported by advisories and public-sector secure-development guidance. |
| Audit and accountability gaps | SIRO / information governance owner | Logs tied to user, tool, server, resource/data class, approval, token scope, version, and upstream action. | Public-sector control need is clear; MCP-specific cross-product audit semantics and vendor retention depth remain source gaps: `TODO-product-control-depth`. |
| Data classification drift | Data owner and information governance owner | Data-class labels for resources/tools; owner review; redaction/minimisation; prohibit sensitive secrets in unsafe elicitation flows. | Supported by MCP resource/elicitation notes and public-sector data-security guidance; local data taxonomy remains design work. |
| Incident response gaps | Security operations owner | Server/tool kill switch; credential rotation; advisory monitoring; pinned-version rollback; log preservation; supplier notification path. | Control themes are source-backed; vendor SLA/support evidence remains open: `TODO-product-control-depth`. |
| Supplier ownership ambiguity | Commercial owner and service owner | Named supplier/service owner; support route; SBOM/dependency evidence; maintained fork strategy; manifest/schema/prompt change-control. | Supported as analysis from supply-chain and reference-server notes; detailed supplier assurance remains evidence-gated. |
| Procurement lock-in | Commercial owner | Exit path, data processing terms, support model, audit-log access, registry portability, licensing/billing clarity, and contract controls. | Requires procurement-specific evidence before final recommendations: `TODO-proprietary-connector-procurement-evidence`. |

### Provisional Adoption Gates

- No production pilot without a named service owner, security owner, and data owner.
- No unmanaged public registry consumption in production.
- No destructive or externally communicating tools without explicit approval, logging, and rollback or compensating controls.
- No sensitive data access through local unmanaged servers.
- No supplier-managed MCP service reliance without evidence for audit access, incident response, data handling, support route, and exit path.
- No final recommendation until exact source extraction closes the section 02, 04, 06, and vendor-control gaps.

## Evidence Gaps

- Control mapping for identity, registry/allowlist, approval, audit, data classification, incident response, supplier ownership, and procurement is now analysis-stage and source-note bounded; it still needs final integration after sections 04 and 06 stabilize.
- Product-control evidence is needed before relying on managed vendor MCP offerings for audit, data residency, incident response, or procurement claims: `TODO-product-control-depth`.
- Independent adoption evidence is needed before relying on broad vendor-adoption claims for public-sector decisions: `TODO-vendor-adoption-independent-use`.
- Procurement-specific evidence is needed before making recommendations about proprietary app ecosystems: `TODO-proprietary-connector-procurement-evidence`.
- Section 09 should become source-ready only after the main technical and alternatives sections have stabilized.
