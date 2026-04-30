# Alternatives: Skills and Agents

Date accessed for local imported source set and targeted official documentation checks: 2026-04-29 and 2026-04-30.

Status: source-note draft. This file converts locally imported research material into structured source notes and records targeted verification against official vendor documentation already present in, or directly implied by, the local imports. The exact Semantic Kernel, OpenAI tools, and OpenAI app-submission entries now have BibTeX records.

## Purpose

Capture sources on direct APIs/function calling, agent frameworks, skills, proprietary connectors, and hybrid architectures.

## Evidence Boundary

- Inputs inspected locally:
  - `import/MCP as an integration backbone for enterprise and government AI.md`
  - `import/Citations from MCP as an integration backbone for enterprise and government AI`
  - `sources/official-specs.md`
- Targeted official documentation checks, all accessed 2026-04-29:
  - OpenAI developer docs only for OpenAI taxonomy, Apps SDK, and app submission evidence.
  - Microsoft Learn pages already present in, or directly implied by, local Microsoft source leads.
- Targeted public-sector and non-vendor checks, all accessed 2026-04-30:
  - GOV.UK open standards guidance for interoperability, procurement, exit, and lock-in evidence.
  - NCSC and NIST application-vetting guidance for third-party app marketplace/catalogue approval evidence.
- The imported report is used only for orientation and gap-finding. Final paper prose should cite durable source notes and BibTeX keys, not Deep Research turn markers.
- Future entries marked "candidate" have enough local signal to preserve as source leads, but still need exact page verification before final prose.

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

### ASA-003 - Plugins in Semantic Kernel

- Proposed citation key: `semantic-kernel-plugins-2024-12-10`
- Title: Plugins in Semantic Kernel
- Author/organisation: Microsoft
- Publication/update date: 2024-12-10
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/
- Source type: primary
- Key claims:
  - Facts:
    - Microsoft describes plugins as a way to encapsulate existing APIs into a collection that an AI can use.
    - The page says Semantic Kernel uses function calling behind the scenes and marshals model requests to functions in the codebase.
    - It defines a plugin as a group of functions exposed to AI apps and services, and says those functions can be invoked automatically with function calling.
    - It says plugins can be imported from native code, OpenAPI specifications, or an MCP Server.
    - It verifies the local snippet's three-step process: define a plugin, add it to the kernel, then invoke plugin functions with function calling.
  - Reported opinions:
    - Microsoft says plugins are valuable in enterprise scenarios because they mirror how enterprise developers build services and APIs.
  - Analysis:
    - This closes the exact Semantic Kernel plugin URL and wording blocker for framework-plugin facts.
    - It does not provide independent evidence that Semantic Kernel is more portable, secure, or procurement-ready than MCP.
- Direct quotation under 25 words: "group of functions"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports comparing framework-native plugin/function abstractions with MCP tool publication. Treat Microsoft enterprise-value statements as vendor positioning.
- Reliability assessment:
  - High for Microsoft's Semantic Kernel product documentation. Low for independent comparison with MCP.
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
  - Facts:
    - Local snippets say the Apps SDK is a framework for building apps for ChatGPT.
    - Local snippets state that building an app for ChatGPT with the Apps SDK requires an MCP server that defines the app's tools and capabilities.
    - Local snippets state that, within the Apps SDK, MCP keeps the server, model, and UI in sync.
    - Targeted verification of the Apps SDK landing page says the current submission flow is the path to public distribution, and that an approved published app appears in the ChatGPT apps store while OpenAI creates a Codex plugin.
  - Reported opinions:
    - OpenAI presents the Apps SDK as a supported way to build and distribute ChatGPT apps.
  - Analysis:
    - Supports the proprietary app ecosystem comparison: vendor-hosted app layers can build on MCP while still creating host-specific packaging, review, UX, and distribution concerns.
- Direct quotation under 25 words: "MCP is the backbone"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports the proprietary app ecosystem comparison: vendor-hosted app layers can build on MCP while still creating host-specific packaging, review, UX, and distribution concerns.
- Reliability assessment:
  - High for OpenAI's current product model. Product availability, submission rules, and enterprise controls should be rechecked before procurement recommendations.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-006 - Extend Agent Actions with MCP in Copilot Studio

- Proposed citation key: `microsoft-copilot-studio-mcp`
- Title: Extend your agent with Model Context Protocol
- Author/organisation: Microsoft
- Publication/update date: 2026-04-17
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
- Source type: primary
- Key claims:
  - Facts:
    - Microsoft says Copilot Studio can extend an agent with tools by using MCP.
    - The page says MCP connects existing knowledge servers and data sources inside Copilot Studio.
    - It says Copilot Studio currently supports MCP tools and resources.
    - It says connected MCP server tools and resources are automatically available in Copilot Studio and dynamically reflect server-side updates or removal.
    - It includes an optional step to publish an MCP connector so it can be used across tenants.
  - Reported opinions:
    - Microsoft positions MCP as a way to connect existing knowledge servers and data sources directly within Copilot Studio.
  - Analysis:
    - This entry supports Microsoft proprietary-platform integration evidence.
    - It does not, by itself, prove tenant audit retention, public-sector procurement readiness, or control adequacy.
- Direct quotation under 25 words: "extend your agent with tools"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant to procurement where a Microsoft-controlled agent platform may expose MCP capabilities through existing enterprise administration, permission, and audit patterns.
- Reliability assessment:
  - High for Microsoft product documentation. Medium for governance and procurement claims unless paired with tenant-control, audit, support, and licensing evidence.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-007 - Use Model Context Protocol for Finance and Operations Apps

- Proposed citation key: `microsoft-dynamics365-mcp-2026-03-11`
- Title: Use Model Context Protocol for finance and operations apps
- Author/organisation: Microsoft
- Publication/update date: Local citation snippet captured 2026-03-11; targeted verification found Microsoft Learn last updated 2026-04-27.
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- Source type: primary
- Key claims:
  - Facts:
    - Microsoft says MCP defines a common language for agents and applications to interact with enterprise data and business logic.
    - The page says the common protocol enables agent access across multiple apps, agent reuse across ERP systems, access from any compatible agent platform, simplified development, and consistent data access, permissions, and auditability.
    - It says the Dynamics 365 ERP MCP server lets agents perform data operations and access business logic without custom code, connectors, or APIs.
    - It says dynamic context is based on the agent's security permissions, application configuration, extensions, and personalization.
    - It says customers choose which agent platforms can access the MCP server, with default access for Microsoft Copilot Studio and Visual Studio Code.
    - It records licensing and billing differences between Copilot Studio and other agent clients, plus known limitations.
  - Reported opinions:
    - Microsoft frames MCP standardization as producing consistency, context, control, and a simplified development experience.
  - Analysis:
    - This source supports the claim that MCP can appear inside proprietary enterprise application platforms, not only in standalone AI clients.
    - It supplies some procurement-relevant product evidence around allowed clients, billing, prerequisites, and limitations, but it is not public-sector procurement guidance.
- Direct quotation under 25 words: "any compatible agent platform"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for comparing direct API integration with vendor-platform MCP integration in an enterprise line-of-business system. Treat permission and auditability claims as Microsoft product documentation, not independent assurance.
- Reliability assessment:
  - High for Microsoft product documentation. Medium for comparative and procurement claims because the source is vendor-reported and product-specific.
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

### ASA-010 - Introduction to Semantic Kernel

- Proposed citation key: `semantic-kernel-overview-2024-06-24`
- Title: Introduction to Semantic Kernel
- Author/organisation: Microsoft
- Publication/update date: 2024-06-24
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/semantic-kernel/overview/
- Source type: primary
- Key claims:
  - Facts:
    - Microsoft describes Semantic Kernel as a lightweight, open-source development kit for building AI agents and integrating models into C#, Python, or Java codebases.
    - The page describes Semantic Kernel as middleware that translates a model's request into a function call and passes results back to the model.
    - It says Semantic Kernel combines prompts with existing APIs to perform actions.
    - It says adding existing code as a plugin lets developers integrate AI services through connectors and share extensions through OpenAPI specifications.
  - Reported opinions:
    - Microsoft calls Semantic Kernel enterprise-ready, modular, observable, and future proof.
  - Analysis:
    - This closes the exact Semantic Kernel framework URL and wording blocker for treating Semantic Kernel as an agent/application framework.
    - It does not provide independent evidence for portability, lock-in, or public-sector suitability.
- Direct quotation under 25 words: "lightweight, open-source development kit"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful as a primary-source baseline for comparing a framework/middleware approach with a neutral connector protocol.
- Reliability assessment:
  - High for Microsoft's own framework description. Vendor positioning claims require corroboration before final recommendations.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-011 - Using Tools | OpenAI API

- Proposed citation key: `openai-using-tools`
- Title: Using tools
- Author/organisation: OpenAI
- Publication/update date: Current documentation page; no stable publication date captured
- Date accessed: 2026-04-29
- URL: https://developers.openai.com/api/docs/guides/tools
- Related official OpenAI verification URL for tool support matrix: https://developers.openai.com/api/docs/models/gpt-5.5-pro
- Source type: primary
- Key claims:
  - Facts:
    - The Using tools page says model responses or agents can extend capabilities using built-in tools, function calling, tool search, and remote MCP servers.
    - The same page has separate examples or sections for web search, file search, tool search, function calling, and remote MCP.
    - The OpenAI API documentation navigation lists Tools entries for MCP and Connectors, Skills, Shell, Computer use, File search/retrieval, Tool search, and other tools.
    - The official OpenAI model page tool-support matrix lists Skills and MCP separately under tools.
  - Reported opinions:
    - OpenAI positions these as ways to extend model or agent capabilities inside the OpenAI API product surface.
  - Analysis:
    - This closes `TODO-openai-tools-taxonomy` for the claim that OpenAI distinguishes built-in tools, function calling, tool search, and remote MCP servers.
    - It supports saying OpenAI documentation treats Skills and MCP as separate tool categories, but final prose should not imply that the Using tools intro sentence itself lists Skills.
- Direct quotation under 25 words: "built-in tools, function calling, tool search, and remote MCP servers"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating OpenAI-hosted tool categories, Skills, remote MCP, and function calling as layerable product options rather than a single mutually exclusive architecture.
- Reliability assessment:
  - High for OpenAI API product taxonomy as of access date. Product taxonomy may change and should be rechecked before final publication.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-012 - OpenAI Apps SDK Submission and Review Evidence

- Proposed citation keys: `openai-app-submission-guidelines`; `openai-app-submission-flow`
- Titles: App submission guidelines; Submit and maintain your app
- Author/organisation: OpenAI
- Publication/update date: Current documentation pages; no stable publication date captured
- Date accessed: 2026-04-29
- URLs:
  - https://developers.openai.com/apps-sdk/app-submission-guidelines
  - https://developers.openai.com/apps-sdk/deploy/submission
- Source type: primary
- Key claims:
  - Facts:
    - The guidelines page sets minimum standards that developers must meet for a ChatGPT app to be considered for publication and remain available.
    - OpenAI says MCP tool definitions make an app safer and easier for the model and users to understand.
    - The guidelines say apps primarily functioning as unofficial connectors to third-party services, including pass-through middleware layers, cannot be approved.
    - The guidelines require a published privacy policy and data-collection minimization.
    - The submission flow says submitted apps enter a review queue and may receive automated scans or manual reviews.
    - The submission flow says approved apps can be published in the dashboard and listed in the App Directory and Codex Plugin Directory.
    - It says changes to published app information require a new draft and re-review, and that inactive, unstable, or non-compliant apps may be removed.
  - Reported opinions:
    - OpenAI frames the ChatGPT app ecosystem as built on trust and a fair, transparent process.
  - Analysis:
    - This narrows `TODO-proprietary-connector-procurement-evidence`: there is official vendor evidence for review, publication, directory, privacy, data-minimization, and connector restrictions.
    - It does not close the public-sector procurement blocker because it is not public-sector supplier-assurance guidance, pricing terms, SLA evidence, audit-retention evidence, or data-residency procurement evidence.
- Direct quotation under 25 words: "minimum standard"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for describing proprietary app-store style governance surfaces. Procurement recommendations still need public-sector and supplier-assurance sources.
- Reliability assessment:
  - High for OpenAI's current app submission and review process. Low for public-sector procurement sufficiency.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-013 - GOV.UK Open Standards Principles and Procurement Guidance

- Proposed citation keys: `govuk-open-standards-principles-2018-04-05`; `govuk-make-use-open-standards-2021-03-31`
- Titles: Open Standards principles; Make use of open standards
- Author/organisation: Cabinet Office / Government Digital Service / Central Digital and Data Office
- Publication/update dates:
  - Open Standards principles: published 2013-04-09; last updated 2018-04-05
  - Make use of open standards: published 2017-11-06; last updated 2021-03-31
- Date accessed: 2026-04-30
- URLs:
  - https://www.gov.uk/government/publications/open-standards-principles/open-standards-principles
  - https://www.gov.uk/guidance/make-use-of-open-standards
- Source type: public-sector policy/guidance; non-vendor
- Key claims:
  - Facts:
    - GOV.UK says the Open Standards Principles apply to software interoperability, data, and document formats in government IT.
    - The principles apply to UK central government departments and agencies, and GOV.UK encourages local government, the wider public sector, and devolved administrations to adopt them.
    - GOV.UK says selected open standards should enable software interoperability through open protocols and data exchange between software and data stores.
    - GOV.UK says open standards must be well documented, publicly available, free to use, mature unless used for innovation, market-supported, royalty-free, and compatible with open source and proprietary licensed solutions.
    - GOV.UK says open standards can help avoid vendor lock-in, support interoperability, support component reuse, support sharing of data, and reduce overall programme cost.
    - GOV.UK says open standards help suppliers by being neutral and flexible, reducing unintentional contract lock-ins, and helping break large IT contracts into smaller components.
    - GOV.UK says organisations specifying IT requirements should specify open standards unless there is a clear reason why this is not possible.
    - GOV.UK says open-standards selection considers interoperability needs, market support, potential vendor lock-in, maturity, security/legal requirements, operational needs, and economic efficiency.
    - GOV.UK says teams should estimate exit and migration costs at the start of a new IT project or programme.
    - The Technology Code guidance says using open standards increases interoperability, can save time and money through reuse, increases compatibility with stakeholders, and helps avoid vendor lock-in.
  - Reported opinions:
    - GOV.UK presents openness as supporting affordable, secure, innovative, better connected public technology.
  - Analysis:
    - This narrows `TODO-framework-portability-evidence`: there is now non-vendor public-sector evidence that open standards and open protocols are procurement-relevant mechanisms for portability, interoperability, reuse, exit planning, and lock-in reduction.
    - It does not close the narrower comparison between framework-only agent runtimes and MCP-based connectors because it does not mention MCP, LangChain, Semantic Kernel, Skills, or current AI agent frameworks.
    - Final section 06 can use this as a policy baseline: any portability recommendation should be framed as an open-standards/exit-planning requirement, not as proof that MCP is automatically portable in deployment.
- Direct quotation under 25 words: "avoid vendor lock-in"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Strong baseline for procurement criteria: prefer open, documented, market-supported interface standards where they meet user needs; document exemptions, interoperability constraints, and exit/migration costs.
- Reliability assessment:
  - High for UK public-sector policy/guidance on open standards and procurement. Low for direct technical comparison among AI agent frameworks and MCP.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-014 - NCSC Guidance on Third-Party Applications and App Catalogues

- Proposed citation key: `ncsc-third-party-applications-devices`
- Title: Using third-party applications on devices
- Author/organisation: National Cyber Security Centre
- Publication/update date: NCSC page reviewed/published as part of device security guidance; exact visible date not captured in page text
- Date accessed: 2026-04-30
- URL: https://www.ncsc.gov.uk/collection/device-security-guidance/policies-and-settings/using-third-party-applications-on-devices
- Source type: public-sector cyber guidance
- Key claims:
  - Facts:
    - NCSC says modern devices often support third-party applications and many platforms offer online marketplaces for installation.
    - NCSC says third-party applications may access user and organisational data, and once an app has accessed data it can be difficult to know what was done with that data.
    - NCSC recommends organisational policies for third-party applications that balance productivity and information risk.
    - NCSC says application allow lists can be joined up with software licensing and procurement activities in a lightweight approvals process.
    - NCSC says application approval should include procurement, legal, security, IT administration, and user representatives as required.
    - NCSC says approval should be integrated with software asset management, handle software updates, and regularly re-review approved apps.
    - NCSC says application-store checks can reduce malicious-app risk but are not a guarantee and may permit behaviour that conflicts with enterprise policy.
    - NCSC says most regular business apps can be approved into an app catalogue, while risky apps may be limited to users with a strong business need.
  - Reported opinions:
    - NCSC presents a fast, lightweight, responsive app-approval process as a way to balance user productivity and risk.
  - Analysis:
    - This narrows `TODO-proprietary-connector-procurement-evidence`: there is public-sector evidence for marketplace/app catalogue approval, procurement involvement, re-review, update handling, and limits of app-store checks.
    - It does not close the blocker for AI-specific proprietary connector ecosystems because the guidance is about device applications, not ChatGPT apps, Copilot connectors, MCP servers, SaaS connectors, SLAs, data residency, audit retention, or public-sector framework terms.
    - Section 06 should avoid procurement recommendations that treat vendor app-store approval as sufficient assurance. Use this source only to require local approval/catalogue, asset-management, update, and re-review controls around any proprietary app or connector ecosystem.
- Direct quotation under 25 words: "not a guarantee"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for modelling proprietary AI app/connectors as third-party application approvals: marketplace review is a signal, not a replacement for local risk assessment, app catalogue control, and re-review.
- Reliability assessment:
  - High for UK public-sector cyber guidance on third-party applications. Medium for analogy to AI connector/app ecosystems; the analogy must be stated as analysis.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### ASA-015 - NIST SP 800-163 Rev. 1 App Vetting

- Proposed citation key: `nist-sp-800-163r1-app-vetting-2019-04`
- Title: Vetting the Security of Mobile Applications
- Author/organisation: National Institute of Standards and Technology
- Publication/update date: 2019-04
- Date accessed: 2026-04-30
- URL: https://csrc.nist.gov/pubs/sp/800/163/r1/final
- Source type: public-sector technical guidance
- Key claims:
  - Facts:
    - NIST says public and private organisations increasingly rely on mobile applications, making security of those applications more important.
    - NIST says SP 800-163 Rev. 1 outlines and details a mobile application vetting process.
    - NIST says the process can ensure mobile applications conform to an organisation's security requirements and are reasonably free from vulnerabilities.
    - NIST identifies app vetting, app vetting systems, malware, security requirements, software assurance, software vulnerabilities, and software testing as keywords/topics for the publication.
  - Reported opinions:
    - None needed for section 06.
  - Analysis:
    - This further narrows `TODO-proprietary-connector-procurement-evidence` by adding a public-sector vetting-process baseline for third-party applications.
    - It remains mobile-application-specific and should not be cited as direct evidence for AI connector procurement, marketplace SLAs, licensing, data residency, or audit retention.
- Direct quotation under 25 words: "conform to an organization's security requirements"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful as a supporting assurance baseline when treating proprietary apps/connectors as third-party software that needs local security requirements and vetting, rather than vendor-store approval alone.
- Reliability assessment:
  - High for NIST app-vetting guidance. Low for direct proprietary AI connector procurement evidence.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

## Known Alternatives Evidence Gaps

These gaps should be filled before converting section 06 into final report prose.

| Needed source or verification | Working TODO key | Blocks |
| --- | --- | --- |
| BibTeX entries for accepted alternative notes above, especially newly verified ASA-003 and ASA-010 through ASA-012 | `TODO-alternatives-source-bibtex` | Closed for current accepted notes; `semantic-kernel-plugins-2024-12-10`, `semantic-kernel-overview-2024-06-24`, `openai-using-tools`, `openai-app-submission-guidelines`, and `openai-app-submission-flow` now exist |
| Exact Semantic Kernel plugin and agent-framework URLs/wording | `TODO-semantic-kernel-source-note` | Closed for source-note evidence and BibTeX-backed section 06 citation |
| Exact OpenAI "Using tools" page key for remote MCP servers and Skills as separate tool categories | `TODO-openai-tools-taxonomy` | Closed/narrowed: Using tools verifies built-in tools, function calling, tool search, and remote MCP; Skills/MCP separation is verified via OpenAI docs navigation and model tool matrix |
| Independent or non-vendor evidence comparing framework-only and MCP-based portability | `TODO-framework-portability-evidence` | Further narrowed: ASA-013 adds public-sector open-standards/lock-in/exit evidence, but no independent direct comparison of framework-only AI agent runtimes with MCP connectors was found; blocks strong MCP-over-framework portability claims |
| Public-sector procurement evidence for proprietary app-store style connectors | `TODO-proprietary-connector-procurement-evidence` | Further narrowed: ASA-014 and ASA-015 add public-sector third-party application approval/vetting evidence, but no public-sector procurement-specific source for proprietary AI app/connectors, marketplace SLAs, data residency, audit retention, or connector licensing was found; blocks app-ecosystem procurement recommendations beyond local approval/re-review controls |
| BibTeX entries for newly added public-sector evidence | `TODO-alternatives-public-sector-bibtex` | Closed; BibTeX records now exist for `govuk-open-standards-principles-2018-04-05`, `govuk-make-use-open-standards-2021-03-31`, `ncsc-third-party-applications-devices`, and `nist-sp-800-163r1-app-vetting-2019-04` |
