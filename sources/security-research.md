# Security Research

Date accessed for all sources: 2026-04-29.

This register separates normative MCP material, independent security research, vulnerability evidence, academic work, and public-sector governance sources. Source types use the project taxonomy: primary, secondary, forum, vendor, academic.

## MCP Specification and Official Guidance

### SR-001 - Authorization

- Title: Authorization
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- Source type: primary
- Key claims:
  - MCP authorization is optional, but HTTP transports should use the MCP OAuth-based authorization profile.
  - Protected MCP servers act as OAuth resource servers and must publish protected resource metadata.
  - Clients must use resource indicators; servers must validate token audience and must not accept or transit unrelated tokens.
  - STDIO transport should retrieve credentials from the environment rather than follow this HTTP authorization specification.
- Direct quotation under 25 words: "Authorization is OPTIONAL for MCP implementations."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Establishes that MCP is not itself a complete IAM control plane. A public-sector deployment needs a mandatory local profile for which servers require authorization, how scopes are assigned, how tokens are audience-bound, and where enterprise identity providers sit.
- Reliability assessment:
  - High. Normative primary specification, but it describes protocol requirements rather than proving that ecosystem implementations comply.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-002 - Transports

- Title: Transports
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- Source type: primary
- Key claims:
  - MCP defines STDIO and Streamable HTTP as core transports.
  - HTTP servers must validate `Origin` on incoming connections.
  - Locally bound HTTP servers should bind to localhost and authenticate connections to reduce DNS rebinding risk.
- Direct quotation under 25 words: "Servers MUST validate the `Origin` header on all incoming connections."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Helps distinguish local developer-style MCP from managed remote MCP. For a public-sector hub, remote HTTP deployments should be brokered, authenticated, logged, and network-controlled; local HTTP servers need hardening and inventory.
- Reliability assessment:
  - High. Normative primary specification; implementation quality must still be independently assessed.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-003 - Security Best Practices

- Title: Security Best Practices
- Author/organisation: Model Context Protocol project
- Publication/update date: Current documentation page; no stable publication date visible
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Source type: primary
- Key claims:
  - Identifies MCP-specific risks including confused deputy attacks, token passthrough, SSRF, session hijacking, and local server compromise.
  - Recommends token audience validation, scope minimization, secure sessions, hardened discovery flows, and avoiding token passthrough.
  - Places responsibility across clients, servers, authorization servers, and deployment architecture.
- Direct quotation under 25 words: "Token passthrough is explicitly forbidden."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Provides a checklist for acceptance criteria: no token passthrough, per-client consent, session integrity, explicit scopes, SSRF controls, gateway-level policy, and audit trails.
- Reliability assessment:
  - High for official guidance and terminology; less stable than a versioned spec page and should be rechecked before final publication.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-004 - Tools

- Title: Tools
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/server/tools
- Source type: primary
- Key claims:
  - Tools are intended to be model-controlled capabilities exposed by servers.
  - Clients should show available tools, surface tool invocations, and require user confirmation for operations.
  - Tool annotations can communicate properties such as read-only, destructive, idempotent, or open-world behavior, but the host still decides policy.
- Direct quotation under 25 words: "Tools in MCP are designed to be model-controlled."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Frames the core governance problem: models can select tools, so sensitive tools need approval workflows, data classification, least privilege, and non-model policy enforcement.
- Reliability assessment:
  - High. Normative primary specification for tool semantics; does not solve malicious metadata or indirect prompt-injection risk by itself.
- Sections where this source may be cited:
  - `02-mcp-in-a-nutshell.md`
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### SR-005 - Sampling

- Title: Sampling
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/client/sampling
- Source type: primary
- Key claims:
  - MCP servers can request LLM sampling through clients while clients retain model access, model selection, and permission control.
  - Tool-enabled sampling requires declared client capability.
  - Human review of sampling requests and outputs is recommended for trust and safety.
- Direct quotation under 25 words: "there SHOULD always be a human in the loop"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Sampling expands the risk surface from tool calls to server-initiated model calls. A hub should decide whether sampling is allowed, logged, redacted, or disabled by default.
- Reliability assessment:
  - High. Normative primary specification; operational safety depends on host UX and policy enforcement.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-006 - Elicitation

- Title: Elicitation
- Author/organisation: Model Context Protocol project
- Publication/update date: Version 2025-11-25
- Date accessed: 2026-04-29
- URL: https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation
- Source type: primary
- Key claims:
  - MCP servers can request structured user input through clients.
  - Form-mode elicitation must not be used for sensitive information; sensitive data should use safer URL-mediated flows.
  - Clients should guard against phishing-style flows, URL prefetching, and user identity confusion.
- Direct quotation under 25 words: "Servers MUST NOT use form mode elicitation to request sensitive information."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Important for citizen data and staff credentials. Procurement should require controls around secret collection, identity binding, anti-phishing UX, and audit logs.
- Reliability assessment:
  - High. Normative primary specification; still requires host and server implementation review.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-007 - DNS Rebinding Protection Disabled by Default in Model Context Protocol Python SDK for Servers Running on Localhost

- Title: DNS Rebinding Protection Disabled by Default in Model Context Protocol Python SDK for Servers Running on Localhost
- Author/organisation: Model Context Protocol Python SDK maintainers / GitHub Security Advisory
- Publication/update date: Published 2025-12-02
- Date accessed: 2026-04-29
- URL: https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-9h52-p55h-vw2f
- Source type: primary
- Key claims:
  - Python SDK versions before 1.23.0 lacked default DNS rebinding protection for local HTTP FastMCP servers.
  - The issue affected localhost/127.0.0.1 HTTP servers and was patched by enabling protection by default.
  - STDIO transport was not affected.
- Direct quotation under 25 words: "This issue does not affect servers using stdio transport."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Shows that official SDK defaults can carry security defects. A public-sector hub needs pinned versions, advisory monitoring, SBOMs, and minimum SDK baselines.
- Reliability assessment:
  - High. Primary maintainer advisory, specific affected versions and remediation.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-008 - MCP SDK FastMCP Server Validation Error Leading to Denial of Service

- Title: MCP SDK FastMCP Server Validation Error Leading to Denial of Service
- Author/organisation: Model Context Protocol Python SDK maintainers / GitHub Security Advisory
- Publication/update date: Published 2025-07-04
- Date accessed: 2026-04-29
- URL: https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-3qhf-m339-9g5v
- Source type: primary
- Key claims:
  - Malformed requests could trigger unhandled validation errors in affected Python SDK versions.
  - The failure mode could make servers unavailable until restart.
  - Patched in Python SDK version 1.9.4.
- Direct quotation under 25 words: "A validation error in the MCP SDK can cause an unhandled exception."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Demonstrates the need for defensive validation, restart policies, rate limits, health checks, and patch governance even for framework-generated servers.
- Reliability assessment:
  - High. Primary maintainer advisory.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `08-deeper-analyses-and-case-studies.md`

### SR-009 - Model Context Protocol Servers Security Overview

- Title: Security: modelcontextprotocol/servers
- Author/organisation: Model Context Protocol project / GitHub
- Publication/update date: Current GitHub security overview; advisory list visible on 2026-04-29
- Date accessed: 2026-04-29
- URL: https://github.com/modelcontextprotocol/servers/security
- Source type: primary
- Key claims:
  - The reference server repository warns that its servers are educational examples, not production-ready solutions.
  - The security page lists multiple Git server advisories, including path validation bypasses and argument/path handling issues.
  - The repository directs SDK vulnerabilities to the relevant SDK advisory process.
- Direct quotation under 25 words: "not as production-ready solutions"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Prevents treating reference implementations as procurement-ready connectors. Public-sector use should require production support, security review, owner accountability, and maintained forks.
- Reliability assessment:
  - High for repository policy and advisory existence; individual advisories require separate technical review.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

## Independent Security Research and Vulnerability Evidence

### SR-010 - MCP Security Notification: Tool Poisoning Attacks

- Title: MCP Security Notification: Tool Poisoning Attacks
- Author/organisation: Invariant Labs; Luca Beurer-Kellner and Marc Fischer
- Publication/update date: 2025-04-01
- Date accessed: 2026-04-29
- URL: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
- Source type: vendor
- Key claims:
  - Malicious instructions can be embedded in MCP tool descriptions that are visible to the model but not necessarily to the user.
  - Demonstrates data exfiltration, behavior hijacking, cross-server shadowing, and rug-pull risk where tool descriptions change after approval.
  - Recommends clearer UI, tool/package pinning, and cross-server dataflow protection.
- Direct quotation under 25 words: "malicious instructions are embedded within MCP tool descriptions"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Strong evidence that server approval is not enough if tool metadata can change or influence other servers. Supports allowlists, signed manifests, broker mediation, and cross-server isolation.
- Reliability assessment:
  - Medium-high. Original security-lab disclosure with concrete examples; vendor has an interest in security tooling.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-011 - Jumping the line: How MCP servers can attack you before you ever use them

- Title: Jumping the line: How MCP servers can attack you before you ever use them
- Author/organisation: Trail of Bits
- Publication/update date: 2025-04-21
- Date accessed: 2026-04-29
- URL: https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/
- Source type: vendor
- Key claims:
  - Tool descriptions enter model context during `tools/list`, before any tool invocation.
  - This can bypass human approval models because malicious instructions may operate before explicit tool use.
  - Recommends source vetting, guardrails, trust-on-first-use validation, and alerts on changed tool descriptions.
- Direct quotation under 25 words: "MCP servers can manipulate model behavior without ever being invoked."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Shows that "approve each tool call" is insufficient as the only control. A hub needs pre-ingestion scanning of metadata and administrative review before tools reach model context.
- Reliability assessment:
  - High for threat-modeling value. Trail of Bits is a respected security firm; claims should still be mapped to specific client behavior.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-012 - Poison everywhere: No output from your MCP server is safe

- Title: Poison everywhere: No output from your MCP server is safe
- Author/organisation: CyberArk Labs
- Publication/update date: 2025-05-30
- Date accessed: 2026-04-29
- URL: https://www.cyberark.com/resources/all-blog-posts/poison-everywhere-no-output-from-your-mcp-server-is-safe
- Source type: vendor
- Key claims:
  - Tool poisoning risk is not limited to tool descriptions; schemas and tool outputs can also carry malicious instructions.
  - Static scanning of descriptions alone is incomplete.
  - Runtime monitoring and output handling are needed in addition to metadata controls.
- Direct quotation under 25 words: "the true attack surface extends across the entire tool schema"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports layered controls: metadata review, schema validation, output filtering, dataflow tracking, and runtime anomaly detection.
- Reliability assessment:
  - Medium-high. Credible vendor security-lab analysis; useful for broadening the attack surface beyond initial tool descriptions.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-013 - Critical RCE Vulnerability in mcp-remote: CVE-2025-6514

- Title: Critical RCE Vulnerability in mcp-remote: CVE-2025-6514
- Author/organisation: JFrog Security Research
- Publication/update date: 2025-07-09
- Date accessed: 2026-04-29
- URL: https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/
- Source type: vendor
- Key claims:
  - `mcp-remote` versions before 0.1.16 were exposed to OS command injection when connecting to untrusted MCP servers.
  - The attack abused OAuth authorization endpoint handling and could lead to client-side remote code execution.
  - CVE-2025-6514 was scored critical.
- Direct quotation under 25 words: "full remote code execution is achieved in a real-world scenario"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Demonstrates that remote MCP trust failures can compromise clients, not only servers. Supports central brokers, deny-by-default remote server policies, and emergency revocation.
- Reliability assessment:
  - High for the vulnerability evidence. Vendor disclosure is backed by CVE/advisory data and patched version information.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-014 - mcp-remote exposed to OS command injection via untrusted MCP server connections

- Title: mcp-remote exposed to OS command injection via untrusted MCP server connections
- Author/organisation: GitHub Advisory Database / National Vulnerability Database
- Publication/update date: Published 2025-07-09; updated 2025-07-09
- Date accessed: 2026-04-29
- URL: https://github.com/advisories/GHSA-6xpm-ggf7-wc3p
- Source type: secondary
- Key claims:
  - Tracks the same CVE-2025-6514 vulnerability in `mcp-remote`.
  - Affected versions are >= 0.0.5 and < 0.1.16; patched version is 0.1.16.
  - CVSS 3.1 score shown as 9.7 critical.
- Direct quotation under 25 words: "Critical severity"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for formal risk registers because it provides advisory identifiers, severity, affected versions, and patched versions for dependency management.
- Reliability assessment:
  - High as an advisory database record; less explanatory than the JFrog write-up.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `09-government-local-authority-ai-hub.md`

### SR-015 - The Mother of All AI Supply Chains: Critical, Systemic Vulnerability at the Core of Anthropic's MCP

- Title: The Mother of All AI Supply Chains: Critical, Systemic Vulnerability at the Core of Anthropic's MCP
- Author/organisation: OX Security Research; Moshe Siman Tov Bustan, Mustafa Naamnih, Nir Zadok, Roni Bar
- Publication/update date: 2026-04-15
- Date accessed: 2026-04-29
- URL: https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/
- Source type: vendor
- Key claims:
  - Claims a systemic STDIO-related arbitrary command execution pattern across MCP SDK usage and downstream products.
  - Reports 30+ responsible disclosures, 10+ high/critical CVEs, marketplace poisoning, and live production command execution.
  - Recommends blocking public exposure, treating external MCP configuration as untrusted, using verified directories, sandboxing, monitoring tool invocations, and upgrading affected products.
- Direct quotation under 25 words: "This is not a traditional coding error."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Important late-April 2026 evidence for supply-chain and configuration risk. Should push any adoption plan toward sandboxed execution, manifest allowlists, private registries, and conservative handling of STDIO server definitions.
- Reliability assessment:
  - Medium. The disclosure is recent, detailed, and linked to CVEs, but the protocol-level framing is strong and may be contested. Treat as significant risk signal pending independent postmortems.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `05-timeline-and-evolution.md`
  - `07-hype-vs-substance.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `10-open-questions-and-future-directions.md`

### SR-016 - State of MCP Server Security 2025: 5,200 Servers, Credential Risks, and an Open-Source Fix

- Title: State of MCP Server Security 2025: 5,200 Servers, Credential Risks, and an Open-Source Fix
- Author/organisation: Astrix Security; Tal Skverer
- Publication/update date: 2025-10-15
- Date accessed: 2026-04-29
- URL: https://astrix.security/learn/blog/state-of-mcp-server-security-2025/
- Source type: vendor
- Key claims:
  - Reports analysis of more than 5,200 open-source MCP server implementations.
  - Claims 88% require credentials, 53% rely on static secrets or PATs, and OAuth adoption is only 8.5%.
  - Proposes vault-backed secret wrapping as one mitigation.
- Direct quotation under 25 words: "analyzed over 5,200 unique, open-source Model Context Protocol (MCP) server implementations"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports treating non-human identity and secrets management as a core MCP adoption risk. A hub should require short-lived credentials, vault integration, rotation, and inventory of server identities.
- Reliability assessment:
  - Medium. Useful quantitative vendor research; methodology and dataset should be reviewed before relying on exact percentages in final prose.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-017 - First Malicious MCP in the Wild: The Postmark Backdoor That's Stealing Your Emails

- Title: First Malicious MCP in the Wild: The Postmark Backdoor That's Stealing Your Emails
- Author/organisation: Koi Security; Idan Dardikman
- Publication/update date: 2025-09-25
- Date accessed: 2026-04-29
- URL: https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft
- Source type: vendor
- Key claims:
  - Reports a malicious npm package, `postmark-mcp`, that impersonated a legitimate Postmark integration and BCCed outbound email to an external address from version 1.0.16.
  - Shows MCP server supply-chain risk where a connector receives highly sensitive operational permissions.
  - Provides indicators of compromise and mitigation steps including uninstall, credential rotation, and email log audit.
- Direct quotation under 25 words: "first sighting of a real world malicious MCP server"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Concrete example for procurement and operational governance: public packages should not be installed directly into a council AI estate without provenance, scanning, approval, and continuous monitoring.
- Reliability assessment:
  - Medium-high. Detailed incident write-up with IOCs, but vendor framing is adversarial and should be corroborated if used as a central case study.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-018 - Prompt injection security problems in LLMs and AI agents

- Title: Prompt injection security problems in LLMs and AI agents
- Author/organisation: Simon Willison
- Publication/update date: 2025-04-11
- Date accessed: 2026-04-29
- URL: https://simonwillison.net/2025/Apr/11/prompt-injection-security-problems/
- Source type: secondary
- Key claims:
  - Argues that combining private data, untrusted content, and external communication creates severe AI-agent risk.
  - Uses MCP and agent tooling as practical examples of prompt-injection and confused-deputy problems.
  - Emphasizes that model-level instruction following cannot be treated as a security boundary.
- Direct quotation under 25 words: "prompt injection security problems"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for explaining the high-level threat model to non-specialist decision-makers. Supports architectural controls rather than relying on prompts or model alignment alone.
- Reliability assessment:
  - Medium-high. Practitioner analysis from a well-regarded commentator; not a formal vulnerability disclosure.
- Sections where this source may be cited:
  - `03-perceptions-and-discourse.md`
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`

## Academic and Benchmark Sources

### SR-019 - Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers

- Title: Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers
- Author/organisation: Mohammed Mehedi Hasan, Hao Li, Emad Fallahzadeh, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan
- Publication/update date: Submitted 2025-06-16; last revised 2026-04-13
- Date accessed: 2026-04-29
- URL: https://arxiv.org/abs/2506.13538
- Source type: academic
- Key claims:
  - Presents a large-scale empirical study of 1,899 open-source MCP servers.
  - Identifies eight distinct vulnerability classes, with only three overlapping traditional software vulnerabilities.
  - Reports 7.2% of servers contain general vulnerabilities and 5.5% exhibit MCP-specific tool poisoning.
  - Advocates MCP-specific vulnerability databases, automated registry scanning, and stronger governance.
- Direct quotation under 25 words: "7.2% of servers contain general vulnerabilities"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Provides empirical backing for requiring MCP-specific security scanning and not relying solely on traditional SAST or dependency checks.
- Reliability assessment:
  - Medium-high. Academic preprint with clear methodology claims; peer-review status should be checked before final publication.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `07-hype-vs-substance.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-020 - MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

- Title: MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols
- Author/organisation: Yixuan Yang, Cuifeng Gao, Daoyuan Wu, Yufan Chen, Yingjiu Li, Shuai Wang
- Publication/update date: Submitted 2025-08-17; last revised 2026-02-12
- Date accessed: 2026-04-29
- URL: https://arxiv.org/abs/2508.13220
- Source type: academic
- Key claims:
  - Formalizes secure MCP behavior and introduces a security taxonomy.
  - Identifies 17 attack types across client, protocol, server, and host surfaces.
  - Finds successful compromises across evaluated MCP platforms and reports low effectiveness for current protections.
- Direct quotation under 25 words: "17 distinct attack types across four primary attack surfaces"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for designing red-team exercises and acceptance tests before exposing MCP tools to staff or citizen-service workflows.
- Reliability assessment:
  - Medium-high. Academic preprint and benchmark; platform versions and current mitigations should be revalidated.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-021 - MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers

- Title: MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers
- Author/organisation: Zhiqiang Wang, Yichao Gao, Yanting Wang, Suyuan Liu, Haifeng Sun, Haoran Cheng, Guanquan Shi, Haohua Du, Xiangyang Li
- Publication/update date: Submitted 2025-08-19
- Date accessed: 2026-04-29
- URL: https://arxiv.org/abs/2508.14925
- Source type: academic
- Key claims:
  - Builds a benchmark from 45 live MCP servers and 353 authentic tools.
  - Generates 1,312 malicious test cases across 10 categories of potential risk.
  - Reports widespread susceptibility to tool poisoning and low refusal rates by agents.
- Direct quotation under 25 words: "agents rarely refuse these attacks"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports using live-server-style adversarial testing, not only generic prompt-injection test suites, before allowing high-risk tools.
- Reliability assessment:
  - Medium. Academic preprint; dataset and model versions need review before relying on exact success rates.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

## Public-Sector and General AI Security Guidance

### SR-022 - Guidelines for secure AI system development

- Title: Guidelines for secure AI system development
- Author/organisation: UK National Cyber Security Centre with international partners
- Publication/update date: 2023-11-27; version 1.0
- Date accessed: 2026-04-29
- URL: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
- Source type: primary
- Key claims:
  - Security should be addressed across secure design, secure development, secure deployment, and secure operation and maintenance.
  - AI systems have novel security vulnerabilities in addition to standard cyber risks.
  - Guidance is written for large organisations, SMEs, cyber professionals, and the public sector.
- Direct quotation under 25 words: "Security must be a core requirement"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Provides public-sector baseline language for secure-by-design lifecycle governance. MCP adoption should be assessed against design, development, deployment, and operational controls.
- Reliability assessment:
  - High. Official UK NCSC guidance endorsed by international cyber agencies.
- Sections where this source may be cited:
  - `01-introduction-methodology.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-023 - Code of Practice for the Cyber Security of AI

- Title: Code of Practice for the Cyber Security of AI
- Author/organisation: UK Department for Science, Innovation and Technology
- Publication/update date: 2025-01-31
- Date accessed: 2026-04-29
- URL: https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai
- Source type: primary
- Key claims:
  - Sets out baseline cyber security requirements for AI systems and the AI supply chain.
  - Explicitly identifies AI-specific risks including data poisoning, model obfuscation, indirect prompt injection, and operational data-management differences.
  - Intended to inform a future ETSI standard and builds on NCSC secure AI guidance.
- Direct quotation under 25 words: "AI has distinct differences to software."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Directly applicable to UK public-sector procurement and supplier assurance. MCP vendors should evidence alignment with AI supply-chain, logging, least-privilege, vulnerability management, and incident response requirements.
- Reliability assessment:
  - High. Official UK government guidance; voluntary but policy-relevant.
- Sections where this source may be cited:
  - `01-introduction-methodology.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-024 - AI Data Security: Best Practices for Securing Data Used to Train and Operate AI Systems

- Title: AI Data Security: Best Practices for Securing Data Used to Train and Operate AI Systems
- Author/organisation: CISA, NSA, FBI, NCSC-UK, and international partners
- Publication/update date: 2025-05-22
- Date accessed: 2026-04-29
- URL: https://www.cisa.gov/resources-tools/resources/ai-data-security-best-practices-securing-data-used-train-operate-ai-systems
- Source type: primary
- Key claims:
  - Data security is critical to AI accuracy, integrity, and trustworthiness.
  - Covers risks across AI lifecycle phases and recommends data-protection, provenance, monitoring, threat detection, and network-defense measures.
  - Addresses sensitive, proprietary, and mission-critical data in operational AI systems.
- Direct quotation under 25 words: "an attacker who can manipulate the data can also manipulate the logic"
- Relevance to Government / Local Authority AI Hub decision-making:
  - MCP increases the volume and velocity of data movement between systems. This guidance supports data classification, provenance, encryption, access control, monitoring, and audit requirements.
- Reliability assessment:
  - High. Joint official cybersecurity guidance from national agencies; not MCP-specific but highly relevant to AI data governance.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

### SR-025 - Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

- Title: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile
- Author/organisation: NIST; Chloe Autio, Reva Schwartz, Jesse Dunietz, Shomik Jain, Martin Stanley, Elham Tabassi, Patrick Hall, Kamie Roberts
- Publication/update date: Published 2024-07-26; updated 2026-04-08
- Date accessed: 2026-04-29
- URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Source type: primary
- Key claims:
  - Provides a cross-sectoral profile and companion resource for applying the NIST AI RMF to generative AI.
  - Intended to help organisations incorporate trustworthiness considerations into design, development, use, and evaluation.
  - Useful for mapping governance, risk measurement, evaluation, and management controls.
- Direct quotation under 25 words: "incorporate trustworthiness considerations into the design, development, use, and evaluation"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supplies a risk-management frame for MCP-enabled AI services: map use cases, measure risk, manage mitigations, and document governance evidence.
- Reliability assessment:
  - High. Official NIST publication; broad AI governance source rather than MCP-specific security evidence.
- Sections where this source may be cited:
  - `01-introduction-methodology.md`
  - `04-technical-critiques-and-mitigations.md`
  - `09-government-local-authority-ai-hub.md`
  - `10-open-questions-and-future-directions.md`

### SR-026 - OWASP Top 10 for Large Language Model Applications

- Title: OWASP Top 10 for Large Language Model Applications
- Author/organisation: OWASP GenAI Security Project
- Publication/update date: 2025 project materials visible on current site
- Date accessed: 2026-04-29
- URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Source type: secondary
- Key claims:
  - Identifies common LLM application risks such as prompt injection, sensitive information disclosure, supply-chain risks, excessive agency, and overreliance.
  - Provides practitioner vocabulary for mapping MCP risks into wider LLM security controls.
  - Frames agentic AI as part of the generative AI application security problem, not only a protocol issue.
- Direct quotation under 25 words: "identifying, mitigating, and documenting security and safety risks"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for assurance checklists, red-team scope, control mapping, and communicating risks to suppliers and internal security teams.
- Reliability assessment:
  - Medium-high. Widely used community security framework; not a regulator or formal standard.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `09-government-local-authority-ai-hub.md`

### SR-027 - MCP03:2025 - Tool Poisoning

- Title: MCP03:2025 - Tool Poisoning
- Author/organisation: OWASP MCP Top 10 project
- Publication/update date: 2025
- Date accessed: 2026-04-29
- URL: https://owasp.org/www-project-mcp-top-10/2025/MCP03-2025%E2%80%93Tool-Poisoning
- Source type: secondary
- Key claims:
  - Treats tool metadata, schemas, and manifests as high-value attack surfaces.
  - Recommends provenance, signing, approval workflows, change detection, RBAC, and runtime policy checks.
  - Helps translate tool poisoning research into enterprise control requirements.
- Direct quotation under 25 words: "treat them as a high-value attack vector"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Directly supports private registry controls, signed server manifests, version pinning, and security review for every MCP tool exposed to an AI Hub.
- Reliability assessment:
  - Medium-high. MCP-specific community guidance; useful for control mapping but should be paired with primary specs and empirical research.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `08-deeper-analyses-and-case-studies.md`
  - `09-government-local-authority-ai-hub.md`

## Decision-Making Themes

- Identity and authorization: cite SR-001, SR-003, SR-013, SR-014, SR-016, SR-023.
- Local server and transport hardening: cite SR-002, SR-007, SR-008, SR-015.
- Tool poisoning and prompt injection: cite SR-004, SR-010, SR-011, SR-012, SR-018, SR-020, SR-021, SR-026, SR-027.
- Supply chain and malicious servers: cite SR-009, SR-015, SR-016, SR-017, SR-019, SR-023.
- Public-sector governance and assurance: cite SR-022, SR-023, SR-024, SR-025.
- Government / Local Authority AI Hub recommendation basis: combine primary MCP controls with independent vulnerability evidence and public-sector AI-security guidance; avoid citing vendor claims alone for final recommendations unless corroborated.
