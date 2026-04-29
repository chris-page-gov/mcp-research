# MCP vs Alternatives

## Status

Rigorous skeleton. Source notes exist for the main alternatives lane, but this section is not draft-ready until new alternative-source BibTeX entries are added and candidate entries are verified.

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
- Source notes now support an agent-framework baseline from LangChain, with Semantic Kernel retained as a candidate pending exact URL verification. See ASA-002 and ASA-003.
- Source notes now support Skills as reusable procedural/domain packaging, using Anthropic Agent Skills. See ASA-004.
- Source notes now support proprietary app and connector ecosystems through OpenAI Apps SDK, Microsoft Copilot Studio candidate evidence, and Microsoft Dynamics 365 MCP documentation. See ASA-005 through ASA-007.
- Source notes now support hybrid models through MCP Apps and the official MCP roadmap. See ASA-008 and ASA-009.

## Draft Skeleton

### Facts

- MCP tools are model-controlled capabilities exposed by servers; clients should surface tools, invocations, and confirmation flows. [@mcp-tools-2025-11-25]
- MCP HTTP authorization is optional at the protocol level, but the HTTP authorization profile provides OAuth-oriented behavior for protected resources. [@mcp-authorization-2025-11-25]
- Direct API/function-calling source note: OpenAI describes function calling/tool calling as a way for models to interface with external systems; the imported report records a model-tool execution loop. [@openai-function-calling-2025-08-07]
- Agent-framework source note: LangChain is locally recorded as an agent/application framework with tool abstractions. [@langchain-overview]
- Semantic Kernel remains a candidate framework source because the local imports capture snippets but not the exact URL. TODO: resolve source evidence before final claims. [@TODO-semantic-kernel-source-note]
- Skills source note: Anthropic Agent Skills are locally recorded as instruction/script/resource packages loaded progressively, and Anthropic positions them as complementary to MCP. [@anthropic-agent-skills-2025-10-16]
- Proprietary app ecosystem source note: OpenAI Apps SDK local snippets say an MCP server is required for ChatGPT apps and that MCP keeps server, model, and UI in sync. [@openai-apps-sdk]
- Proprietary enterprise connector source note: Microsoft Dynamics 365 local snippets describe MCP use for creating and extending agents for finance and operations apps. [@microsoft-dynamics365-mcp-2026-03-11]
- Hybrid direction source note: the official MCP roadmap identifies enterprise-managed authorization, audit trails, gateway/proxy patterns, and configuration portability as active work. [@mcp-roadmap-2026-03-05]
- Hybrid UI/app source note: MCP Apps local snippets describe interactive UI components returned by tools, with support varying by host. [@mcp-apps-2026-01-26]

### Reported Opinions

- OpenAI positions function calling, built-in tools, tool search, and remote MCP servers as separate ways to extend model capabilities. TODO: verify exact wording before final prose. [@TODO-openai-tools-taxonomy]
- Anthropic positions Skills as complementary to MCP. Treat this as vendor positioning unless corroborated. [@anthropic-agent-skills-2025-10-16]
- Microsoft product documentation is locally reported as positioning MCP around reuse across agent platforms, permissions, auditability, and simplified development. TODO: verify exact Microsoft wording before final prose.
- The MCP project roadmap positions gateway/proxy patterns and enterprise readiness as active project priorities rather than solved current-state guarantees. [@mcp-roadmap-2026-03-05]

### Analysis

- Direct APIs/function calling should be analyzed as the simplest control boundary when there are few clients, mature existing API gateways, strict latency needs, or high-risk operations that already have audited service interfaces.
- Agent frameworks should be analyzed as orchestration environments: strong when one team owns the agent loop and runtime, weaker when many clients need the same neutral connector surface.
- Skills should be analyzed as procedural/domain packaging above the tool layer. They can replace some light local workflows, but they do not by themselves provide a shared remote transport, authorization profile, or cross-client connector schema.
- Proprietary connectors and app ecosystems should be analyzed as productivity and distribution layers. They may improve UX and administration inside one platform while increasing host-specific dependency.
- MCP should be analyzed as a connector/capability exchange layer, not a complete workflow engine, IAM control plane, procurement regime, or security boundary.
- The likely public-sector default should remain hybrid: direct APIs for sensitive or latency-critical paths, MCP for reusable bounded connectors, frameworks/Skills for orchestration and procedural knowledge, and enterprise broker/IAM/audit controls around all high-risk actions.

## Decision Matrix Skeleton

| Approach | Control boundary | Reuse and portability | Security and governance | Latency and operations | Procurement/lock-in | Evidence status |
| --- | --- | --- | --- | --- | --- | --- |
| Direct APIs + function calling | Existing API gateway, service IAM, application code | Low to medium across AI clients; high within one estate | Strong where existing controls are mature | Lowest extra protocol overhead | Can lock each client to bespoke wrappers | Source note present; BibTeX TODO |
| Agent framework only | Framework runtime and deployment stack | High inside chosen framework; weaker across unrelated clients | Depends on framework controls and app architecture | Framework overhead, but no MCP layer | Framework/runtime lock-in risk | LangChain note present; Semantic Kernel candidate TODO |
| Skills-only or Skills-heavy | Host-managed skill packaging and agent behavior | Portable only where skill format and host support align | Varies by host; not a transport or IAM layer | Can reduce repeated prompting/context if loaded progressively | Host and skill ecosystem dependency | Anthropic note present; BibTeX TODO |
| Proprietary app/connectors | Vendor app host, marketplace, connector policy | Strong inside one platform; weaker outside it | Can inherit enterprise admin controls, but platform-specific | UX can be strong; operational behavior varies | Higher platform dependency | OpenAI/Microsoft notes present; verification TODO |
| MCP core | MCP host/client/server boundary plus deployment policy | Strong where multiple clients consume shared connectors | Requires host, broker, IAM, registry, audit, and supply-chain controls | Adds protocol/server lifecycle overhead | Lower connector lock-in, but ecosystem maturity risk | Existing MCP citations plus ASA notes |
| Hybrid MCP + direct APIs + framework/Skills | Enterprise broker plus selected integration layer per risk tier | Highest if governed well | Strongest only if responsibilities are explicit | Highest initial complexity; potentially lower long-run duplication | Mixed, can reduce single-vendor dependency | Best-supported skeleton; final prose still needs BibTeX |

## Acceptance Tests Before Final Prose

- Every factual row in the matrix has at least one accepted source note and a BibTeX key.
- Semantic Kernel is either verified as an accepted source note or removed from final prose.
- OpenAI tools taxonomy is verified before saying OpenAI separates remote MCP, Skills, built-in tools, and function calling.
- Microsoft Copilot Studio and Dynamics claims quote or paraphrase exact local source text, not imported-report analysis.
- Any recommendation for Government or Local Authority use maps to a control boundary: identity, approval, audit, registry, data classification, latency, support owner, and exit path.
- No full-report prose is added until this section is promoted from skeleton to draft-ready.

## Evidence Gaps

- TODO: Resolve `TODO-semantic-kernel-source-note`.
- TODO: Resolve `TODO-openai-tools-taxonomy`.
- TODO: Add non-vendor evidence for portability/lock-in claims: `TODO-framework-portability-evidence`.
- TODO: Add procurement-specific evidence for proprietary app or connector ecosystems: `TODO-proprietary-connector-procurement-evidence`.
- TODO: Revisit `sources/vendor-adoption.md` before making broad ecosystem claims.
- TODO: Revisit `sources/fastmcp.md` before comparing FastMCP as a framework/tooling layer.
