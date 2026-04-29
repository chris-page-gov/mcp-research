# Vendor Adoption

Status: started.

Date accessed for all accepted source notes in this file: 2026-04-29.

This file records vendor, ecosystem, and governance evidence for MCP adoption. It is based only on the local import bundle:

- `import/MCP as an integration backbone for enterprise and government AI.md`
- `import/Citations from MCP as an integration backbone for enterprise and government AI`

Use notes with TODO markers only as research leads until the missing local evidence is supplied.

## Purpose

Capture primary vendor documentation and adoption evidence for MCP implementations.

## Acceptance Criteria

- Prefer official vendor documentation, changelogs, or product announcements.
- Separate product availability from production maturity.
- Record whether claims are vendor-reported, independently verified, or only roadmap-level.
- Separate facts, reported opinions, and analysis.

## Source Notes

### VA-001 - MCP joins the Agentic AI Foundation

- Citation key: `mcp-aaif-2025-12-09`
- Title: MCP joins the Agentic AI Foundation
- Author/organisation: Model Context Protocol project / Anthropic
- Publication/update date: 2025-12-09
- Date accessed: 2026-04-29
- URL: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/
- Source type: primary
- Key claims:
  - Facts:
    - The local citation export says Anthropic is donating MCP to the newly formed Agentic AI Foundation under the Linux Foundation.
    - The imported synthesis treats this as a material governance milestone rather than a protocol feature change.
    - This source supports claims about stewardship, not claims about specific vendor deployments or production maturity.
  - Reported opinions:
    - The official project announcement frames the move as a major milestone for MCP.
  - Analysis:
    - This source can support ecosystem sustainability analysis, but should be paired with vendor/product sources before making adoption-strength claims.
- Direct quotation under 25 words: "ensuring vendor-neutral governance"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Helps assess whether MCP is controlled by one vendor or has an emerging neutral governance home, which affects procurement and long-term standards risk.
- Reliability assessment:
  - High for the governance event and official project framing. It is not independent evidence of implementation quality, operational security, or deployment scale.
- Sections where this source may be cited:
  - `01-introduction-methodology.md`
  - `05-timeline-and-evolution.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-002 - Linux Foundation Announces the Formation of the Agentic AI Foundation

- Citation key: `linux-foundation-aaif-2025-12-09`
- Title: Linux Foundation Announces the Formation of the Agentic AI Foundation
- Author/organisation: Linux Foundation
- Publication/update date: 2025-12-09; page metadata also shows date modified 2026-02-24
- Date accessed: 2026-04-29
- URL: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- Source type: primary
- Key claims:
  - Facts:
    - The Linux Foundation announcement says it formed the Agentic AI Foundation with founding project contributions from Anthropic's Model Context Protocol, Block's goose, and OpenAI's AGENTS.md.
    - The announcement lists Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI as platinum members.
    - The announcement links the AAIF to a neutral foundation role and to broader open-source governance; it also includes vendor statements from AWS, Bloomberg, Cloudflare, Google Cloud, Microsoft, and OpenAI.
    - The imported synthesis uses this source to support multi-vendor backing for the Agentic AI Foundation.
  - Reported opinions:
    - Linux Foundation positioning describes AAIF as a neutral, open foundation for transparent and collaborative evolution of agentic AI.
    - Vendor quotes in the announcement frame MCP as important infrastructure, but those are reported opinions from member representatives.
  - Analysis:
    - This is useful corroboration that MCP governance moved into a broader industry-backed foundation context.
    - It does not prove that each listed member has production MCP offerings.
- Direct quotation under 25 words: "Platinum members include Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft and OpenAI."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports assessment of ecosystem breadth and governance sustainability, but procurement decisions still need product-level evidence and support commitments.
- Reliability assessment:
  - High for foundation membership and launch details. It is still not enough for maintainer authority, technical steering, change-control, or product-maturity claims.
- Sections where this source may be cited:
  - `01-introduction-methodology.md`
  - `05-timeline-and-evolution.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-003 - Apps SDK

- Citation key: `openai-apps-sdk`
- Title: Apps SDK
- Author/organisation: OpenAI
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://developers.openai.com/apps-sdk/
- Source type: vendor
- Key claims:
  - Facts:
    - The Apps SDK landing page describes OpenAI's framework for building apps for ChatGPT.
    - Related official pages used for raw recovery: https://developers.openai.com/apps-sdk/quickstart and https://developers.openai.com/apps-sdk/build/mcp-server.
    - The Apps SDK quickstart says Apps SDK apps use MCP to connect to ChatGPT.
    - The quickstart says a Model Context Protocol server is required and defines the app's capabilities as tools exposed to ChatGPT.
    - The build guide says an MCP server defines tools, enforces auth, returns data, and points each tool to a UI bundle.
    - The build guide recommends starting with the MCP Apps bridge and treating `window.openai` as a compatibility layer for optional ChatGPT extensions.
  - Reported opinions:
    - OpenAI presents the Apps SDK as a supported way to build and distribute ChatGPT Apps.
  - Analysis:
    - This is strong evidence of OpenAI product-level MCP compatibility for ChatGPT app development.
    - It is not independent evidence that arbitrary MCP servers are approved, safe, or suitable for public-sector deployment.
- Direct quotation under 25 words: "A Model Context Protocol (MCP) server (required)"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Shows that one major AI platform expects MCP servers to participate in app and UI integration patterns, making MCP relevant to cross-client portability.
- Reliability assessment:
  - High for OpenAI product documentation and supported integration patterns. Vendor-reported and should be supplemented with security, submission, and data-handling documentation.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-004 - Extend agents with Model Context Protocol actions

- Citation key: `microsoft-copilot-studio-mcp`
- Title: Extend agents with Model Context Protocol actions
- Author/organisation: Microsoft
- Publication/update date: 2026-04-17
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
- Source type: vendor
- Key claims:
  - Facts:
    - The Microsoft Learn page is titled "Extend your agent with Model Context Protocol."
    - The page says Copilot Studio agents can be extended with tools by using MCP.
    - The page says connecting to an MCP server makes published tools and resources automatically available in Copilot Studio.
    - The page says Copilot Studio currently supports MCP tools and resources.
    - The page says generative orchestration must be enabled to use MCP.
    - The imported synthesis treats Copilot Studio as a concrete Microsoft MCP integration.
  - Reported opinions:
    - Microsoft describes MCP as a way to connect to existing knowledge servers and data sources directly within Copilot Studio.
  - Analysis:
    - This source supports Microsoft adoption at the product-documentation level.
    - It should not be used to infer deployment maturity, tenant controls, or audit behaviour beyond the documented Copilot Studio integration steps.
- Direct quotation under 25 words: "Copilot Studio currently supports MCP tools and resources."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant where public-sector users may adopt Microsoft agent tooling and need to know whether MCP connectors can be surfaced through Copilot Studio.
- Reliability assessment:
  - High for Microsoft product documentation and supported integration shape. Still insufficient for detailed product-control claims.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-005 - Use Model Context Protocol for finance and operations apps

- Citation key: `microsoft-dynamics365-mcp-2026-03-11`
- Title: Use Model Context Protocol for finance and operations apps
- Author/organisation: Microsoft
- Publication/update date: 2026-04-27; local import previously carried 2026-03-11
- Date accessed: 2026-04-29
- URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- Source type: vendor
- Key claims:
  - Facts:
    - The page explains how to use an MCP server to create and extend agents for Microsoft Dynamics 365 finance and operations apps.
    - Microsoft describes Dynamics 365 ERP MCP as a dynamic server for data operations and business logic in finance and operations apps.
    - The page lists prerequisites including finance and operations app version 10.0.47 or later, enabling the Dynamics 365 ERP MCP server feature, and configuring allowed MCP clients.
    - The page says returned menus, forms, entities, and APIs are limited by the authenticated user's security role.
    - The page records known limitations, including no support for attachments and unavailability during environment downtime.
    - The imported synthesis says the Dynamics 365 documentation emphasises consistent data access, permissions, and auditability across agent integrations.
    - The imported synthesis says this source supports reuse claims for agent integrations without custom connectors or APIs.
  - Reported opinions:
    - Microsoft's reuse and simplified-development claims are vendor-reported product positioning.
  - Analysis:
    - This is one of the more decision-relevant vendor sources because it links MCP to enterprise application data, permissions, and auditability concerns.
    - It should still be cited as Microsoft-reported capability, not as independent assurance that controls are sufficient for government use.
- Direct quotation under 25 words: "consistent data access, permissions, and auditability"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Directly relevant to line-of-business system integration, audit expectations, and whether MCP can reduce duplicate connectors in enterprise environments.
- Reliability assessment:
  - High for Microsoft product documentation. Medium for maturity and control adequacy because those claims remain vendor-reported in the local evidence.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-006 - GitHub MCP Server: new Projects tools, OAuth scope filtering, and new features

- Citation key: `github-mcp-server-changelog-2026-01-28`
- Title: GitHub MCP Server: new Projects tools, OAuth scope filtering, and new features
- Author/organisation: GitHub
- Publication/update date: 2026-01-28
- Date accessed: 2026-04-29
- URL: https://github.blog/changelog/2026-01-28-github-mcp-server-new-projects-tools-oauth-scope-filtering-and-new-features/
- Source type: vendor
- Key claims:
  - Facts:
    - The title records new GitHub MCP Server Projects tools and OAuth scope filtering.
    - GitHub page metadata records publication on 2026-01-28 and modification on 2026-01-29.
    - The local citation export describes GitHub's official MCP Server as connecting AI tools directly to GitHub so assistants can read repositories and code.
    - The imported synthesis says GitHub has an official MCP server and Copilot integration.
    - GitHub reports reducing Projects toolset token usage by about 23,000 tokens, or 50%, with a consolidated toolset.
    - GitHub says classic PAT usage now detects OAuth scopes and hides tools the token cannot use.
    - GitHub says enterprise users can run the GitHub MCP Server in HTTP mode with OAuth token support.
  - Reported opinions:
    - GitHub frames its MCP server and registry work as faster and safer AI-building infrastructure.
  - Analysis:
    - This source supports both adoption substance and implementation-maturity concerns: token reduction is evidence that naive tool exposure has real costs.
- Direct quotation under 25 words: "new Projects tools, OAuth scope filtering"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant for developer-platform integration, OAuth scoping, registry policy, and the need to manage tool-list size before exposing MCP servers broadly.
- Reliability assessment:
  - High for GitHub product changes and self-reported token-reduction figures. Not independent evidence of security effectiveness or end-user adoption.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-007 - MCP registry and allowlist controls for VS Code Stable in GitHub Copilot

- Citation key: `github-copilot-mcp-registry-allowlist-2025-11-18`
- Title: MCP registry and allowlist controls for VS Code Stable in GitHub Copilot
- Author/organisation: GitHub
- Publication/update date: 2025-11-18
- Date accessed: 2026-04-29
- URL: https://github.blog/changelog/2025-11-18-internal-mcp-registry-and-allowlist-controls-for-vs-code-stable-in-public-preview/
- Source type: vendor
- Key claims:
  - Facts:
    - The changelog says enterprise and organization administrators can configure MCP registries and enforce allowlist policies in VS Code Stable.
    - The changelog says Visual Studio supports registry discovery, with enforcement planned for a future release.
    - GitHub's linked docs page is https://docs.github.com/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access.
    - The docs page says the MCP registry URL and allowlist are in public preview and subject to change.
    - The docs page offers `Allow all` and `Registry only` policy choices for enterprise and organization configuration.
    - GitHub's linked registry-creation docs page is https://docs.github.com/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry.
    - The registry docs say a valid registry must support the v0.1 MCP registry endpoints and CORS requirements.
  - Reported opinions:
    - GitHub describes its MCP Registry as centralizing server discovery for easier integration and collaboration.
  - Analysis:
    - Registry and allowlist controls are directly relevant to making MCP usable in managed estates.
    - This source should not be treated as proof that open public registries are suitable for government production use.
- Direct quotation under 25 words: "configure MCP registries and enforce allowlist policies"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports a private or curated-registry requirement for any hub using GitHub Copilot or VS Code as an MCP client surface.
- Reliability assessment:
  - High for GitHub product status and documented policy options. Public-preview status and local-server enforcement limitations remain important caveats.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-008 - gRPC as a native transport for MCP

- Citation key: `google-cloud-grpc-mcp-transport`
- Title: gRPC as a native transport for MCP
- Author/organisation: Google Cloud
- Publication/update date: 2026-01-14
- Date accessed: 2026-04-29
- URL: https://cloud.google.com/blog/products/networking/grpc-as-a-native-transport-for-mcp
- Source type: vendor
- Key claims:
  - Facts:
    - The page metadata headline is "gRPC as a custom transport for MCP"; the local import title used "native transport."
    - Google Cloud says it is working with MCP maintainers to support pluggable transports in the MCP SDK and gRPC as a transport without transcoding.
    - The imported synthesis says Google Cloud is investing in gRPC transport support for MCP.
    - The imported synthesis distinguishes this from the official core transports, stating that gRPC was not an official core transport as of the research cut-off.
    - The page links to the MCP project post about official and custom transports and to a Python SDK pull request for pluggable transport interfaces.
  - Reported opinions:
    - Google Cloud positions gRPC as a better fit for some enterprise infrastructure patterns.
    - Google Cloud claims gRPC can improve performance, security, operations, and developer productivity for environments already using gRPC.
  - Analysis:
    - This source supports the claim that vendors are trying to adapt MCP to production infrastructure, but protocol-status claims still require official MCP specification support.
- Direct quotation under 25 words: "gRPC as a custom transport for MCP"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant where an AI Hub must integrate with existing service meshes, gRPC estates, or high-throughput infrastructure rather than only local stdio or HTTP servers.
- Reliability assessment:
  - High for Google Cloud's stated work and motivation. Not authoritative for the official MCP specification status.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-009 - Use the Gemini Cloud Assist remote MCP server

- Citation key: `google-cloud-assist-remote-mcp-2026-04`
- Title: Integrate Gemini Cloud Assist with third-party tools using MCP
- Author/organisation: Google Cloud
- Publication/update date: 2026-04-23
- Date accessed: 2026-04-29
- URL: https://docs.cloud.google.com/cloud-assist/configure-mcp
- Source type: vendor
- Key claims:
  - Facts:
    - The exact local-import title was not recovered; the official Google Cloud page that matches the product and MCP lead is titled "Integrate Gemini Cloud Assist with third-party tools using MCP."
    - The page says integrating Gemini Cloud Assist with third-party tools using MCP is in private preview.
    - The page covers integration with third-party tools including Antigravity, Gemini CLI, and Cursor.
    - The page says Gemini Cloud Assist is exposed through MCP tools using an agents-as-tools pattern.
    - The page lists `ask_cloud_assist`, `design_infra`, and `optimize_costs` among the Gemini Cloud Assist MCP tools.
    - The page warns that these MCP tools should not be treated as stable APIs and may change over time.
    - The imported synthesis treats managed remote MCP servers as part of Google Cloud's MCP adoption evidence.
  - Reported opinions:
    - Google Cloud positions the integration as a way to access cloud-operations expertise in existing tools and workflows.
  - Analysis:
    - This source supports the existence of a managed remote MCP server use case, but it should be cited with the private-preview and unstable-tool caveats.
- Direct quotation under 25 words: "using MCP is in private preview"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant for evaluating managed cloud-provider MCP endpoints versus locally installed or self-hosted servers.
- Reliability assessment:
  - High for the recovered Google Cloud documentation page. Medium for maturity claims because the feature is private preview and the exact imported title was not recovered.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### VA-010 - MCP servers for Cloudflare

- Citation key: `cloudflare-mcp-servers`
- Title: MCP servers for Cloudflare
- Author/organisation: Cloudflare
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/
- Source type: vendor
- Key claims:
  - Facts:
    - Cloudflare says it runs a catalog of managed remote MCP servers that clients can connect to using OAuth.
    - Cloudflare says its API MCP server exposes more than 2,500 API endpoints through two tools, `search()` and `execute()`.
    - Cloudflare says its API MCP server uses Codemode, where the model writes JavaScript against a typed API representation instead of loading endpoint tool definitions.
    - Cloudflare estimates native full-schema MCP exposure at about 1,170,000 tokens and Codemode at about 1,000 tokens.
    - Cloudflare says OAuth authorization redirects the user to select permissions, while CI/CD can use Cloudflare API tokens.
    - The page was last updated on 2026-04-20.
  - Reported opinions:
    - Cloudflare frames codemode as a better way to expose broad API surfaces through MCP.
  - Analysis:
    - This source is strong evidence that major vendors are adapting MCP server design to context and token-cost constraints.
    - The token estimates are vendor-reported and should be cited as such.
- Direct quotation under 25 words: "managed remote MCP servers"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports evaluating whether a hub should expose many granular tools or use brokered/code-mediated access patterns for large API estates.
- Reliability assessment:
  - High for Cloudflare product documentation. Medium for quantitative token claims because they are vendor-reported and depend on implementation assumptions.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

## Required Source Gaps

- `TODO-vendor-adoption-independent-use`: local materials do not provide independently audited adoption numbers, production-deployment counts, or usage metrics for vendor MCP products.
- `TODO-vendor-adoption-raw-pages`: narrowed. Exact URLs recovered for Linux Foundation AAIF announcement and GitHub Copilot registry/allowlist changelog/docs. The Google Cloud Assist lead maps to `https://docs.cloud.google.com/cloud-assist/configure-mcp`, but the exact imported title "Use the Gemini Cloud Assist remote MCP server" was not recovered.
- `TODO-governance-source-notes`: narrowed by VA-001 and VA-002 for donation, foundation launch, membership, and vendor-neutral positioning; still needs source text for foundation governance process, maintainer authority, technical steering, and change-control rules.
- `TODO-product-control-depth`: vendor docs show product support, but local materials are insufficient for detailed claims about audit log retention, tenant isolation, data residency, SLAs, incident response, and procurement terms.
