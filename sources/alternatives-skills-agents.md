# Alternatives: Skills and Agents

Date accessed for local imported source set: 2026-04-29.

Status: source-note draft. This file converts locally imported research material into structured source notes. It does not rely on live browsing. Several entries need BibTeX records before section 06 can cite them in Pandoc form.

## Purpose

Capture sources on direct APIs/function calling, agent frameworks, skills, proprietary connectors, and hybrid architectures.

## Evidence Boundary

- Inputs inspected locally:
  - `import/MCP as an integration backbone for enterprise and government AI.md`
  - `import/Citations from MCP as an integration backbone for enterprise and government AI`
  - `sources/official-specs.md`
- The imported report is used only for orientation and gap-finding. Final paper prose should cite durable source notes and BibTeX keys, not Deep Research turn markers.
- Entries marked "candidate" have enough local signal to preserve as source leads, but still need exact page verification before final prose.

## Acceptance Criteria

- Compare alternatives by control boundary, reuse, portability, security, latency, procurement, and maintainability.
- Avoid treating frameworks, skills, apps, proprietary connectors, and MCP as mutually exclusive unless a source supports that framing.
- Separate product facts from vendor positioning and from this paper's analysis.
- Do not cite new alternative-source keys in `paper/` until the corresponding BibTeX entries exist.

## Source Notes

### ASA-001 - Function Calling | OpenAI API

- Proposed citation key: `openai-function-calling-2025-08-07`
- Title: Function Calling | OpenAI API
- Author/organisation: OpenAI
- Publication/update date: 2025-08-07, according to local citation snippet
- Date accessed: 2026-04-29
- URL: https://developers.openai.com/api/docs/guides/function-calling
- Source type: primary
- Key claims:
  - OpenAI describes function calling, also called tool calling, as a way for models to interface with external systems.
  - The imported report records a five-step loop: send tool definitions, receive a tool call, execute code, send the result back, then receive the model's final answer.
  - This source supports direct API/function-calling as a baseline integration pattern that does not require MCP.
- Direct quotation under 25 words: "interface with external systems"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports a non-MCP baseline for tightly controlled automations where existing API gateway, IAM, audit, and service-management controls are already mature.
- Reliability assessment:
  - High for OpenAI API behavior and product positioning. It is vendor documentation, not comparative evidence about all AI providers or public-sector suitability.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-002 - LangChain Overview

- Proposed citation key: `langchain-overview`
- Title: LangChain overview
- Author/organisation: LangChain
- Publication/update date: Current documentation page; no stable publication date captured in local imports
- Date accessed: 2026-04-29
- URL: https://docs.langchain.com/oss/python/langchain/overview
- Source type: primary
- Key claims:
  - The local imported report records LangChain as an open-source framework with prebuilt agent architecture and integrations for models and tools.
  - The imported report also records LangChain tools as callable functions with structured inputs and outputs passed to a chat model.
  - This supports treating LangChain as an orchestration/framework alternative, not as a neutral connector publication protocol by itself.
- Direct quotation under 25 words, if useful: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for comparing a framework-owned agent loop against an MCP connector layer. A framework-only design can be simpler when one organisation controls the runtime, but it may reduce cross-client portability.
- Reliability assessment:
  - High for LangChain's self-description. Comparative claims about portability or governance are analysis and need to be argued from multiple sources.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-003 - Plugins in Semantic Kernel (candidate)

- Proposed citation key: `semantic-kernel-plugins-2024-12-10`
- Title: Plugins in Semantic Kernel
- Author/organisation: Microsoft
- Publication/update date: 2024-12-10, according to local citation snippet
- Date accessed: 2026-04-29
- URL: TODO: exact URL not captured in local imports; local snippets place this under `learn.microsoft.com`.
- Source type: primary (candidate source note)
- Key claims:
  - Local citation snippets say Semantic Kernel plugins are used through a three-step process: define a plugin, add the plugin to a kernel, and then use it.
  - Local citation snippets also identify Semantic Kernel as a development kit for building AI agents and integrating models.
  - The imported report records Semantic Kernel plugins as grouped functions invoked through model function calling.
- Direct quotation under 25 words: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Preserves a Microsoft framework source lead for comparing framework-native plugins with MCP. Do not rely on this entry in final prose until the exact URL and wording are verified.
- Reliability assessment:
  - Medium until URL and exact wording are verified. Likely high once matched to the official Microsoft documentation page.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-004 - Equipping Agents for the Real World with Agent Skills

- Proposed citation key: `anthropic-agent-skills-2025-10-16`
- Title: Equipping agents for the real world with Agent Skills
- Author/organisation: Anthropic
- Publication/update date: 2025-10-16
- Date accessed: 2026-04-29
- URL: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Source type: primary
- Key claims:
  - Local snippets describe Agent Skills as modular skills for complex real-world tasks.
  - The imported report records Agent Skills as directories of instructions, scripts, and resources loaded progressively.
  - The imported report records Anthropic's position that Skills can complement MCP servers.
- Direct quotation under 25 words: "Skills extend Claude's capabilities"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports separating capability access from reusable procedural/domain knowledge. Skills may be useful above a connector layer, but this source alone should not be used to claim that skills replace controlled remote integration.
- Reliability assessment:
  - High for Anthropic's product design and positioning. Treat complementarity claims as vendor positioning unless corroborated by independent implementation evidence.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### ASA-005 - Apps SDK

- Proposed citation key: `openai-apps-sdk`
- Title: Apps SDK
- Author/organisation: OpenAI
- Publication/update date: Current documentation page; no stable publication date captured in local imports
- Date accessed: 2026-04-29
- URL: https://developers.openai.com/apps-sdk/
- Source type: primary
- Key claims:
  - Local snippets say the Apps SDK is a framework for building apps for ChatGPT.
  - Local snippets state that building an app for ChatGPT with the Apps SDK requires an MCP server that defines the app's tools and capabilities.
  - Local snippets state that, within the Apps SDK, MCP keeps the server, model, and UI in sync.
  - Local OpenAI API snippets list built-in tools, function calling, tool search, and remote MCP servers as different ways to extend model capabilities.
- Direct quotation under 25 words: "MCP is the backbone"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the proprietary app ecosystem comparison: vendor-hosted app layers can build on MCP while still creating host-specific packaging, review, UX, and distribution concerns.
- Reliability assessment:
  - High for OpenAI's current product model. Product availability, submission rules, and enterprise controls should be rechecked before procurement recommendations.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-006 - Extend Agent Actions with MCP in Copilot Studio (candidate)

- Proposed citation key: `microsoft-copilot-studio-mcp`
- Title: Microsoft Copilot Studio MCP action documentation; exact page title TODO
- Author/organisation: Microsoft
- Publication/update date: Current documentation page; no stable publication date captured in local imports
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
- Source type: primary (candidate source note)
- Key claims:
  - The imported report records Microsoft Copilot Studio as having MCP integration.
  - The imported report records Microsoft product positioning around reuse across agent platforms, consistent permissions, auditability, and simplified development.
  - This entry supports proprietary-platform comparison, but exact page wording remains TODO.
- Direct quotation under 25 words: TODO: extract exact quotation before final prose.
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant to procurement where a Microsoft-controlled agent platform may expose MCP capabilities through existing enterprise administration, permission, and audit patterns.
- Reliability assessment:
  - Medium-high. Official Microsoft URL is captured locally, but exact title and claim text need verification before final prose.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-007 - Use Model Context Protocol for Finance and Operations Apps

- Proposed citation key: `microsoft-dynamics365-mcp-2026-03-11`
- Title: Use Model Context Protocol for finance and operations apps
- Author/organisation: Microsoft
- Publication/update date: 2026-03-11, according to local citation snippet
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- Source type: primary
- Key claims:
  - Local snippets describe using an MCP server to create and extend agents for Microsoft Dynamics 365 finance and operations apps.
  - The imported report records Microsoft Dynamics 365 as evidence for reuse, consistent permissions, auditability, and avoiding bespoke custom connectors or APIs for every integration.
  - This source supports the claim that MCP can appear inside proprietary enterprise application platforms, not only in standalone AI clients.
- Direct quotation under 25 words: "create and extend agents"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for comparing direct API integration with vendor-platform MCP integration in an enterprise line-of-business system. Exact permission and audit behavior must be verified before final public-sector recommendations.
- Reliability assessment:
  - High for Microsoft product documentation. Medium for comparative claims until exact wording on permissions, auditability, and custom connectors is extracted.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-008 - MCP Apps - Bringing UI Capabilities to MCP Clients

- Proposed citation key: `mcp-apps-2026-01-26`
- Title: MCP Apps - Bringing UI Capabilities To MCP Clients
- Author/organisation: Model Context Protocol project
- Publication/update date: 2026-01-26
- Date accessed: 2026-04-29
- URL: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
- Source type: primary
- Key claims:
  - Local snippets describe MCP Apps as an official extension that lets tools return interactive UI components in the conversation.
  - Local snippets say host support varies by client.
  - The imported report records MCP Apps as evidence for convergence around UI/app layers above MCP rather than a pure protocol-vs-apps choice.
- Direct quotation under 25 words: "interactive UI components"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports hybrid-architecture analysis: MCP may provide capability access while UI/app layers handle human interaction, forms, dashboards, and multi-step workflows.
- Reliability assessment:
  - High for official MCP extension status and project positioning. Final procurement analysis should verify current host support.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-009 - Roadmap

- Citation key: `mcp-roadmap-2026-03-05`
- Title: Roadmap
- Author/organisation: Model Context Protocol project
- Publication/update date: 2026-03-05
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/development/roadmap
- Source type: primary
- Key claims:
  - The accepted official-spec source note records enterprise-managed authorization, audit trails, gateway/proxy patterns, configuration portability, and enterprise-readiness themes.
  - The imported report records roadmap material on server cards, better discovery, gateway/proxy semantics, and skills-over-MCP as evidence that future designs are likely layered.
  - This source supports treating hybrid models as a live roadmap direction, not merely this paper's preference.
- Direct quotation under 25 words: "manage MCP access the same way they manage everything else"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Important for distinguishing current production-ready evidence from project roadmap work. Roadmap items should not be treated as delivered controls.
- Reliability assessment:
  - High for official project intent; roadmap items are not normative requirements or implementation proof.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

## Known Alternatives Evidence Gaps

These gaps should be filled before converting section 06 into final report prose.

| Needed source or verification | Working TODO key | Blocks |
| --- | --- | --- |
| BibTeX entries for accepted alternative notes above | `TODO-alternatives-source-bibtex` | Any Pandoc citation to ASA-001 through ASA-008 |
| Exact Semantic Kernel plugin and agent-framework URLs/wording | `TODO-semantic-kernel-source-note` | Final claims about Semantic Kernel as an alternative framework |
| Exact OpenAI "Using tools" page key for remote MCP servers and Skills as separate tool categories | `TODO-openai-tools-taxonomy` | Claims that OpenAI separates remote MCP, Skills, built-in tools, and function calling |
| Independent or non-vendor evidence comparing framework-only and MCP-based portability | `TODO-framework-portability-evidence` | Strong claims about portability, lock-in, or maintainability |
| Public-sector procurement evidence for proprietary app-store style connectors | `TODO-proprietary-connector-procurement-evidence` | Procurement recommendations about app ecosystems |
