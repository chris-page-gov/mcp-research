# MCP vs Alternatives

## Status

Rigorous skeleton. Semantic Kernel, OpenAI tools taxonomy, Copilot Studio, Dynamics 365, and OpenAI app-submission wording have been verified in source notes and backed by BibTeX entries. Public-sector portability and app-approval evidence has been added to source notes, but BibTeX is pending and the evidence remains indirect for AI connector procurement.

## Purpose

Compare MCP with direct APIs/function calling, agent frameworks, Skills, proprietary connectors/app ecosystems, and hybrid patterns. The section should support architecture choices for a Government or Local Authority AI Hub without implying that these patterns are mutually exclusive.

## Source Boundary

- Primary source notes:
  - `sources/alternatives-skills-agents.md`
  - `sources/official-specs.md`
  - `sources/security-research.md` where security tradeoffs affect alternatives
- Context-only source files:
  - `sources/vendor-adoption.md` is now a working source-note draft; use only entries with exact URLs/text for final positive ecosystem claims.
  - `sources/fastmcp.md` is now a working source-note draft; use only entries with exact URLs/text for final FastMCP claims.
- Imported report:
  - Use only as orientation. Do not cite Deep Research turn markers.

## Acceptance Criteria

- Compares alternatives by decision criteria, not by marketing labels.
- Separates interoperability, governance, latency, security, procurement, portability, lock-in, and maintainability.
- Separates facts, reported opinions, and analysis.
- Makes clear that direct APIs, frameworks, Skills, proprietary apps, and MCP can be layered.
- Treats Pandoc citations based on local snippets as skeleton citations until exact source wording is verified.
- Preserves TODO markers where exact source wording or independent evidence is missing.

## Evidence State

- Source notes now support a direct API/function-calling baseline from OpenAI Function Calling. See ASA-001.
- Source notes now support an agent-framework baseline from LangChain and Semantic Kernel. Semantic Kernel exact plugin/framework URLs and wording are verified, but BibTeX is pending. See ASA-002, ASA-003, and ASA-010.
- Source notes now support Skills as reusable procedural/domain packaging, using Anthropic Agent Skills. See ASA-004.
- Source notes now support proprietary app and connector ecosystems through OpenAI Apps SDK, OpenAI app-submission evidence, Microsoft Copilot Studio, and Microsoft Dynamics 365 MCP documentation. Exact Microsoft wording is verified. See ASA-005 through ASA-007 and ASA-012.
- Source notes now support hybrid models through MCP Apps and the official MCP roadmap. See ASA-008 and ASA-009.
- OpenAI tools taxonomy is verified for built-in tools, function calling, tool search, remote MCP, and the separate treatment of Skills/MCP in the OpenAI docs navigation and model tool matrix. See ASA-011.
- Framework portability is further narrowed: ASA-013 adds non-vendor public-sector evidence that open standards/open protocols, interoperability, exit planning, and migration-cost analysis reduce lock-in, but there is still no independent direct comparison of framework-only agent runtimes with MCP connectors.
- Proprietary-connector procurement is further narrowed: vendor review, publication, licensing, allowed-client, and connector-control facts exist; ASA-014 and ASA-015 add public-sector third-party app approval/vetting evidence. No accepted source is specific to procurement of proprietary AI app-store connectors, marketplace SLAs, data residency, audit retention, or connector licensing.

## Draft Skeleton

### Facts

- MCP tools are model-controlled capabilities exposed by servers; clients should surface tools, invocations, and confirmation flows. [@mcp-tools-2025-11-25]
- MCP HTTP authorization is optional at the protocol level, but the HTTP authorization profile provides OAuth-oriented behavior for protected resources. [@mcp-authorization-2025-11-25]
- Direct API/function-calling source note: OpenAI describes function calling/tool calling as a way for models to interface with external systems; the imported report records a model-tool execution loop. [@openai-function-calling-2025-08-07]
- Agent-framework source note: LangChain is locally recorded as an agent/application framework with tool abstractions. [@langchain-overview]
- Semantic Kernel verified source notes: Microsoft describes Semantic Kernel as an open-source development kit/middleware for building AI agents, and describes plugins as function groups exposed to AI apps and invoked with function calling. [@semantic-kernel-plugins-2024-12-10] [@semantic-kernel-overview-2024-06-24]
- Skills source note: Anthropic Agent Skills are locally recorded as instruction/script/resource packages loaded progressively, and Anthropic positions them as complementary to MCP. [@anthropic-agent-skills-2025-10-16]
- Proprietary app ecosystem source note: OpenAI Apps SDK local snippets say an MCP server is required for ChatGPT apps and that MCP keeps server, model, and UI in sync. [@openai-apps-sdk]
- OpenAI app-submission source note: OpenAI's Apps SDK submission docs record app review, approval, directory publication, re-review for changes, privacy/data-minimization requirements, and restrictions on unofficial pass-through connectors. [@openai-app-submission-guidelines] [@openai-app-submission-flow]
- Public-sector supplier-assurance baseline: existing security source notes cover secure AI development and AI supply-chain requirements, but they are general AI guidance rather than proprietary app-store connector procurement evidence. [@ncsc-secure-ai-development-2023-11-27] [@dsit-ai-cyber-security-code-2025-01-31]
- Public-sector portability baseline: ASA-013 records GOV.UK guidance that open standards support software interoperability, data exchange, reuse, supplier neutrality, lock-in reduction, exit planning, and procurement requirements. BibTeX pending: `govuk-open-standards-principles-2018-04-05`; `govuk-make-use-open-standards-2021-03-31`.
- Public-sector third-party app baseline: ASA-014 and ASA-015 record NCSC/NIST guidance on application marketplaces, app catalogues, procurement/legal/security involvement, software asset management, updates, re-review, and app-vetting against organisational security requirements. BibTeX pending: `ncsc-third-party-applications-devices`; `nist-sp-800-163r1-app-vetting-2019-04`.
- Proprietary enterprise connector source note: Microsoft Dynamics 365 says MCP standardization supports access from compatible agent platforms, consistent data access/permissions/auditability, allowed-client configuration, licensing/billing distinctions, and known limitations. Current Microsoft page last updated 2026-04-27; existing BibTeX key date may need reconciliation. [@microsoft-dynamics365-mcp-2026-03-11]
- Proprietary platform source note: Microsoft Copilot Studio says connected MCP tools/resources become available to agents and update dynamically; the page also includes optional connector publication across tenants. [@microsoft-copilot-studio-mcp]
- Hybrid direction source note: the official MCP roadmap identifies enterprise-managed authorization, audit trails, gateway/proxy patterns, and configuration portability as active work. [@mcp-roadmap-2026-03-05]
- Hybrid UI/app source note: MCP Apps local snippets describe interactive UI components returned by tools, with support varying by host. [@mcp-apps-2026-01-26]

### Reported Opinions

- OpenAI positions built-in tools, function calling, tool search, and remote MCP servers as ways to extend model capabilities. OpenAI docs also list Skills and MCP separately in tool navigation/model tool-support context; avoid saying the Using tools intro sentence itself lists Skills. [@openai-using-tools]
- Anthropic positions Skills as complementary to MCP. Treat this as vendor positioning unless corroborated. [@anthropic-agent-skills-2025-10-16]
- Microsoft product documentation positions MCP around reuse across compatible agent platforms, consistent data access, permissions, auditability, dynamic tool/resource availability, allowed clients, and simplified development. Treat these as vendor/product claims, not independent assurance. [@microsoft-dynamics365-mcp-2026-03-11] [@microsoft-copilot-studio-mcp]
- OpenAI positions app submission as a trust, quality, safety, policy, and privacy review process for ChatGPT app distribution. Treat this as vendor process evidence, not public-sector procurement assurance. [@openai-app-submission-guidelines] [@openai-app-submission-flow]
- GOV.UK positions open standards as supporting affordable, secure, innovative, and better connected public technology. Treat this as public-sector policy rationale, not a measured comparison of MCP and AI agent frameworks. ASA-013; BibTeX pending.
- NCSC presents lightweight third-party app approval as a way to balance productivity and information risk. Treat this as app-governance guidance, not evidence that proprietary AI app stores meet procurement requirements. ASA-014; BibTeX pending.
- The MCP project roadmap positions gateway/proxy patterns and enterprise readiness as active project priorities rather than solved current-state guarantees. [@mcp-roadmap-2026-03-05]

### Analysis

- Direct APIs/function calling should be analyzed as the simplest control boundary when there are few clients, mature existing API gateways, strict latency needs, or high-risk operations that already have audited service interfaces.
- Agent frameworks should be analyzed as orchestration environments: strong when one team owns the agent loop and runtime. Any claim that they are weaker than MCP across unrelated clients must be framed as analysis from open-standards/exit-planning principles and product-boundary facts, not as independently demonstrated comparative evidence. `TODO-framework-portability-evidence` remains narrowed, not closed.
- Skills should be analyzed as procedural/domain packaging above the tool layer. They can replace some light local workflows, but they do not by themselves provide a shared remote transport, authorization profile, or cross-client connector schema.
- Proprietary connectors and app ecosystems should be analyzed as productivity, review, and distribution layers. Vendor docs show app review/publication and Microsoft allowed-client/licensing controls. Public-sector app guidance supports local catalogue approval, procurement/legal/security review, update handling, asset-management integration, and re-review; it does not support recommending a proprietary AI app ecosystem as procurement-ready by virtue of marketplace review alone. `TODO-proprietary-connector-procurement-evidence` remains narrowed, not closed.
- MCP should be analyzed as a connector/capability exchange layer, not a complete workflow engine, IAM control plane, procurement regime, or security boundary.
- The likely public-sector default should remain hybrid: direct APIs for sensitive or latency-critical paths, MCP for reusable bounded connectors, frameworks/Skills for orchestration and procedural knowledge, and enterprise broker/IAM/audit controls around all high-risk actions.

## Decision Matrix Skeleton

| Approach | Control boundary | Reuse and portability | Security and governance | Latency and operations | Procurement/lock-in | Evidence status |
| --- | --- | --- | --- | --- | --- | --- |
| Direct APIs + function calling | Existing API gateway, service IAM, application code | Low to medium across AI clients; high within one estate | Strong where existing controls are mature | Lowest extra protocol overhead | Can lock each client to bespoke wrappers | Source note present; BibTeX TODO |
| Agent framework only | Framework runtime and deployment stack | High inside chosen framework; weaker across unrelated clients as analysis only | Depends on framework controls and app architecture | Framework overhead, but no MCP layer | Framework/runtime lock-in risk; evaluate against open-standards and exit-planning guidance | LangChain/Semantic Kernel notes plus ASA-013 policy baseline; no direct comparative evidence |
| Skills-only or Skills-heavy | Host-managed skill packaging and agent behavior | Portable only where skill format and host support align | Varies by host; not a transport or IAM layer | Can reduce repeated prompting/context if loaded progressively | Host and skill ecosystem dependency | Anthropic note present; BibTeX TODO |
| Proprietary app/connectors | Vendor app host, marketplace, connector policy | Strong inside one platform; weaker outside it as analysis only | Can inherit enterprise admin controls, but platform-specific; local app approval/re-review still needed | UX can be strong; operational behavior varies | Higher platform dependency; marketplace approval is not procurement assurance | OpenAI/Microsoft wording verified; ASA-014/ASA-015 app-vetting baseline; AI connector procurement evidence absent |
| MCP core | MCP host/client/server boundary plus deployment policy | Strong where multiple clients consume shared connectors | Requires host, broker, IAM, registry, audit, and supply-chain controls | Adds protocol/server lifecycle overhead | Lower connector lock-in, but ecosystem maturity risk | Existing MCP citations plus ASA notes |
| Hybrid MCP + direct APIs + framework/Skills | Enterprise broker plus selected integration layer per risk tier | Highest if governed well | Strongest only if responsibilities are explicit | Highest initial complexity; potentially lower long-run duplication | Mixed, can reduce single-vendor dependency | Best-supported skeleton; final prose still needs BibTeX |

## Acceptance Tests Before Final Prose

- Every factual row in the matrix has at least one accepted source note and a BibTeX key.
- Semantic Kernel is verified as an accepted source note with BibTeX-backed keys.
- OpenAI tools taxonomy is verified with nuance: remote MCP/function/tool-search wording comes from Using tools; Skills/MCP separation comes from docs navigation/model tool-support context.
- Microsoft Copilot Studio and Dynamics claims now quote or paraphrase exact source text, not imported-report analysis.
- Framework portability claims remain analysis-only except for the general public-sector open-standards/exit-planning baseline in ASA-013.
- Proprietary app/connectors procurement claims remain limited to vendor-process facts plus third-party app approval/vetting controls in ASA-014 and ASA-015; do not infer AI connector procurement readiness.
- Any recommendation for Government or Local Authority use maps to a control boundary: identity, approval, audit, registry, data classification, latency, support owner, and exit path.
- No full-report prose is added until this section is promoted from skeleton to draft-ready.

## Evidence Gaps

- CLOSED: Replaced `TODO-semantic-kernel-source-note` with `semantic-kernel-plugins-2024-12-10` and `semantic-kernel-overview-2024-06-24`.
- CLOSED: Replaced `TODO-openai-tools-taxonomy` with `openai-using-tools`.
- TODO narrowed: Added non-vendor public-sector open-standards/lock-in/exit evidence in ASA-013; direct framework-vs-MCP portability evidence still absent, so strong comparative claims stay analysis-grade: `TODO-framework-portability-evidence`.
- TODO narrowed: Added public-sector third-party app approval/vetting evidence in ASA-014 and ASA-015; AI connector marketplace procurement evidence still absent, so recommendations must be limited to local approval, vetting, re-review, and exit controls: `TODO-proprietary-connector-procurement-evidence`.
- CLOSED: Added BibTeX for ASA-013 through ASA-015; `TODO-alternatives-public-sector-bibtex` remains only as a closed source-tracking marker.
- CLOSED: Added BibTeX for OpenAI app-submission evidence: `openai-app-submission-guidelines` and `openai-app-submission-flow`.
- TODO: Revisit `sources/vendor-adoption.md` before making broad ecosystem claims.
- TODO: Revisit `sources/fastmcp.md` before comparing FastMCP as a framework/tooling layer.
