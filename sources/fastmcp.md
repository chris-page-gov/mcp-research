# FastMCP

Status: started.

Date accessed for all accepted source notes in this file: 2026-04-29.

This file records source notes on FastMCP's relationship to the MCP ecosystem. It is based only on the local import bundle:

- `import/MCP as an integration backbone for enterprise and government AI.md`
- `import/Citations from MCP as an integration backbone for enterprise and government AI`

Use notes with TODO markers only as research leads until the missing local evidence is supplied.

## Purpose

Capture source notes on FastMCP's relationship to MCP SDKs, server ergonomics, and adoption.

## Acceptance Criteria

- Distinguish FastMCP as an implementation/tooling layer from MCP as a protocol.
- Record version dates and official SDK relationship only from primary sources.
- Do not use this file to infer protocol behavior unless the official spec also supports it.
- Separate facts, reported opinions, and analysis.

## Source Notes

### FM-001 - Welcome to FastMCP

- Citation key: `fastmcp-welcome`
- Title: Welcome to FastMCP
- Author/organisation: FastMCP project / Prefect
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://gofastmcp.com/getting-started/welcome
- Source type: primary
- Key claims:
  - Facts:
    - The FastMCP welcome page describes FastMCP as a framework for building MCP servers, clients, and applications.
    - The page says FastMCP is made by Prefect.
    - The page says docs can be accessed as Markdown by appending `.md`; `https://gofastmcp.com/getting-started/welcome.md` was used for raw recovery.
    - The official MCP Python SDK repository is https://github.com/modelcontextprotocol/python-sdk and describes itself as the official Python SDK for MCP servers and clients.
    - The current official MCP Python SDK README includes `from mcp.server.fastmcp import FastMCP` in the quickstart and examples.
    - The FastMCP changelog entry for `v1.0` says that release is included in the official Model Context Protocol SDK.
    - The FastMCP `v0.4.0` changelog says relicensing to MIT was to facilitate inclusion in the official MCP SDK.
  - Reported opinions:
    - FastMCP describes itself as the standard framework for building MCP applications.
    - FastMCP's docs report one million downloads per day and 70% of MCP servers across all languages; this is project-reported adoption evidence, not independently audited here.
  - Analysis:
    - This source supports treating FastMCP as an implementation and developer-experience layer above MCP, not as a competing protocol.
    - The official Python SDK relationship is corroborated for current API presence, but the incorporation history still depends on FastMCP-maintainer/project statements.
- Direct quotation under 25 words: "The fast, Pythonic way"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Helps decision-makers distinguish adoption of MCP itself from adoption of a higher-level framework that may add convenience, composition, proxying, testing, auth helpers, and application patterns.
- Reliability assessment:
  - High for FastMCP project self-description and current official SDK API presence. Medium for incorporation history and adoption metrics because those remain FastMCP-reported.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### FM-002 - FastMCP package release record

- Citation key: `fastmcp-pypi-2026-04-13`
- Title: FastMCP
- Author/organisation: FastMCP project / PyPI
- Publication/update date: 2026-04-14T01:42:26.850408Z for PyPI upload of v3.2.4; local PyPI snippet displayed 2026-04-13
- Date accessed: 2026-04-29
- URL: https://pypi.org/project/fastmcp/
- Source type: primary
- Key claims:
  - Facts:
    - PyPI JSON reported latest package version `3.2.4` on 2026-04-29.
    - PyPI JSON reported upload time 2026-04-14T01:42:26.850408Z.
    - The PyPI summary says the package provides a way to build MCP servers and clients.
    - PyPI project URLs point to `https://gofastmcp.com` for documentation/homepage and `https://github.com/PrefectHQ/fastmcp` for the repository.
    - The local citation's 2026-04-13 date is consistent with a local-display or timezone rendering of the 2026-04-14 UTC upload.
  - Reported opinions:
    - The package tagline describes FastMCP as "fast" and "Pythonic."
  - Analysis:
    - Package-index evidence supports active maintenance and version tracking.
    - It does not establish public-sector readiness, production deployment, or API parity with official SDKs.
- Direct quotation under 25 words: "The fast, Pythonic way to build MCP servers and clients."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for assessing release recency, dependency-management requirements, and whether a hub would be relying on an actively moving third-party framework.
- Reliability assessment:
  - High for package metadata and version chronology. It does not validate production deployments or public-sector suitability.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-003 - Releases - PrefectHQ/fastmcp

- Citation key: `fastmcp-github-releases-2026-04`
- Title: Releases - PrefectHQ/fastmcp
- Author/organisation: FastMCP maintainers / GitHub
- Publication/update date: 2026-04-14T01:42:08Z for latest v3.2.4 GitHub release
- Date accessed: 2026-04-29
- URL: https://github.com/PrefectHQ/fastmcp/releases/tag/v3.2.4
- Source type: primary
- Key claims:
  - Facts:
    - GitHub API reported latest release tag `v3.2.4`, release title `v3.2.4: Patch Me If You Can`, and publication timestamp 2026-04-14T01:42:08Z.
    - The release notes describe fixes, hardening, and polish.
    - The release notes say background tasks are now scoped to the authorization context rather than the MCP session.
    - Security-related notes include decoded-base64 size validation for `FileUpload`, stopping proxy forwarding of inbound HTTP headers to unrelated remote servers, and AuthKit audience binding per RFC 8707.
  - Reported opinions:
    - The maintainers frame the release as patch hardening and polish.
  - Analysis:
    - GitHub releases are suitable for version chronology and release-note facts.
    - Do not use release cadence alone as evidence of governance maturity or support guarantees.
- Direct quotation under 25 words: "Patch Me If You Can"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports dependency-risk review, upgrade cadence assessment, and the need to pin framework versions before using FastMCP in a managed hub.
- Reliability assessment:
  - High for GitHub release chronology and release-note facts. It does not establish governance maturity or support guarantees.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-004 - FastMCP 3.0 is GA

- Citation key: `fastmcp-3-0-ga-2026-02-18`
- Title: FastMCP 3.0 is GA
- Author/organisation: Jonathan Lowin / FastMCP maintainer blog; FastMCP maintainers / GitHub release
- Publication/update date: 2026-02-18
- Date accessed: 2026-04-29
- URL: https://jlowin.dev/blog/fastmcp-3-launch/
- Source type: primary maintainer post
- Key claims:
  - Facts:
    - The maintainer post metadata title is "FastMCP 3.0 is GA" and datePublished is 2026-02-18T12:00:00Z.
    - The post says FastMCP 3.0 was stable and generally available.
    - The post includes an installation command, `pip install fastmcp -U`.
    - The GitHub release URL for the same milestone is https://github.com/PrefectHQ/fastmcp/releases/tag/v3.0.0, published 2026-02-18T21:25:15Z.
    - The GitHub release notes say this is when FastMCP moved from `jlowin/fastmcp` to `PrefectHQ/fastmcp`.
  - Reported opinions:
    - The release announcement presents 3.0 as a stability milestone.
  - Analysis:
    - This supports claims that FastMCP's standalone branch had reached a v3 stable release by early 2026.
    - It should not be used for protocol behaviour unless supported by MCP specifications or official SDK documentation.
- Direct quotation under 25 words: "FastMCP 3.0 is stable"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant for deciding whether FastMCP is merely experimental or has a separately maintained release line that may need supplier/dependency review.
- Reliability assessment:
  - High for maintainer and GitHub release chronology. Medium for maturity claims because stability is project-reported.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-005 - Stop Calling Tools, Start Writing Code (Mode)

- Citation key: `fastmcp-code-mode-2026-03-03`
- Title: Stop Calling Tools, Start Writing Code (Mode)
- Author/organisation: Jonathan Lowin / FastMCP maintainer blog; FastMCP maintainers / GitHub release
- Publication/update date: 2026-03-03
- Date accessed: 2026-04-29
- URL: https://jlowin.dev/blog/fastmcp-3-1-code-mode/
- Source type: primary maintainer post
- Key claims:
  - Facts:
    - The maintainer post metadata title is "Stop Calling Tools, Start Writing Code (Mode)" and datePublished is 2026-03-03T00:00:00Z.
    - The post discusses a server with two hundred tools putting two hundred schemas into the context window.
    - The post says FastMCP 3.1 ships server-side Code Mode with configurable discovery.
    - The GitHub release URL for the same feature is https://github.com/PrefectHQ/fastmcp/releases/tag/v3.1.0, published 2026-03-03T02:42:42Z.
    - The GitHub release describes CodeMode as an experimental transform where the LLM searches for relevant tools, inspects schemas, and writes sandboxed Python that chains `call_tool()` calls.
  - Reported opinions:
    - The post argues for code-mediated execution instead of exposing large tool catalogs directly to the model.
  - Analysis:
    - This is useful evidence for FastMCP's implementation philosophy: it tries to reduce context overhead by layering developer tooling over MCP.
    - It is not neutral evidence of the general cost of MCP; use independent or official client-guidance sources for broader performance claims.
- Direct quotation under 25 words: "two hundred schemas into the context window"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports evaluating whether a hub should permit large direct tool catalogs or require brokered/code-mediated patterns for broad API surfaces.
- Reliability assessment:
  - Medium-high for release chronology and feature description. Useful maintainer/practitioner evidence, but advocacy-heavy and not independent benchmarking.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### FM-006 - FastMCP 2.10 compliance with the 2025-06-18 MCP specification update

- Citation key: `fastmcp-2-10-spec-compliance`
- Title: FastMCP 2.10 achieves full compliance with the 6/18/2025 MCP specification update
- Author/organisation: FastMCP project
- Publication/update date: 2025-07-01T23:24:43Z for GitHub release; updates page displays 2025-07-02
- Date accessed: 2026-04-29
- URL: https://github.com/PrefectHQ/fastmcp/releases/tag/v2.10.0
- Source type: primary
- Key claims:
  - Facts:
    - The FastMCP updates page maps the local snippet to release `FastMCP 2.10: Great Spec-tations`.
    - The GitHub release tag is `v2.10.0`, title `v2.10.0: Great Spec-tations`, and published timestamp 2025-07-01T23:24:43Z.
    - The release notes say FastMCP 2.10.0 delivers full compliance with the 2025-06-18 MCP spec update.
    - The release notes identify elicitation support, output schemas, and structured outputs as headline protocol features.
    - The changelog Markdown contains a conflicting `2024-07-01` description for `v2.10.0`; the GitHub API timestamp and updates page make 2025-07-01/02 the usable date.
  - Reported opinions:
    - "Full compliance" is a project-reported claim and should be treated as such unless corroborated by tests or official conformance criteria.
  - Analysis:
    - This source can support FastMCP's claim to track MCP spec evolution, but not independent conformance.
    - Any protocol-level claims must still cite the official 2025-06-18 MCP specification notes.
- Direct quotation under 25 words: "full compliance with the 6/18/2025 MCP specification update"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant to dependency selection: a hub adopting FastMCP needs to know which MCP spec versions are implemented and how conformance is tested.
- Reliability assessment:
  - Medium. Primary project claim; exact URL and date are recovered, but conformance methodology and independent certification are not.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-007 - FastMCP Apps

- Citation key: `fastmcp-apps-docs`
- Title: Apps
- Author/organisation: FastMCP project
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://gofastmcp.com/apps/overview
- Source type: primary
- Key claims:
  - Facts:
    - The Apps overview page is available as Markdown at https://gofastmcp.com/apps/overview.md.
    - The page marks Apps as new in version 3.0.0.
    - The page says MCP tools normally return text, while MCP Apps let tools return interactive UIs rendered in the conversation.
    - The page says FastMCP builds on the MCP Apps extension with Prefab.
    - The page marks Prefab Apps as new in version 3.1.0.
    - The page marks `FastMCPApp` as new in version 3.2.0.
    - The page warns production users to pin `prefab-ui` because FastMCP only pins a minimum version and Prefab can have breaking changes.
  - Reported opinions:
    - FastMCP frames apps as a better fit for interactive outputs such as dashboards, forms, and visualizations.
  - Analysis:
    - This source supports the view that FastMCP is building an application framework layer above MCP's core protocol.
    - It should not be cited as evidence that MCP core itself specifies these app behaviours unless official MCP Apps sources also support the claim.
- Direct quotation under 25 words: "MCP tools normally return text."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant if a public-sector hub needs interactive forms, dashboards, or case-management views rather than text-only tool results.
- Reliability assessment:
  - High for FastMCP project self-description and version-badge details. Medium for production-readiness because the page itself warns about dependency pinning.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### FM-008 - FastMCP repository and adoption signals

- Citation key: `fastmcp-github-repo-2026-04-29`
- Title: PrefectHQ/fastmcp
- Author/organisation: FastMCP maintainers / GitHub; Jonathan Lowin maintainer blog
- Publication/update date: Repository metadata observed 2026-04-29; maintainer post published 2025-05-16
- Date accessed: 2026-04-29
- URL: https://github.com/PrefectHQ/fastmcp
- Source type: primary repository metadata plus maintainer-reported adoption commentary
- Key claims:
  - Facts:
    - GitHub API observed repository `PrefectHQ/fastmcp`, description "The fast, Pythonic way to build MCP servers and clients.", license `Apache-2.0`, 24,910 stars, 1,972 forks, and pushed timestamp 2026-04-26T17:49:34Z.
    - The maintainer adoption post URL is https://jlowin.dev/blog/fastmcp-2-10k-stars/.
    - The maintainer post metadata title is "Reflecting on FastMCP at 10k stars" and datePublished is 2025-05-16T00:00:00Z.
  - Reported opinions:
    - The maintainer post says FastMCP reached 10,000 GitHub stars in about six weeks.
    - The maintainer post says Anthropic adopted FastMCP as the reference implementation for the official MCP SDK.
    - The maintainer post says FastMCP is at the heart of almost every Python MCP server.
  - Analysis:
    - GitHub stars and forks are useful popularity and maintenance signals, but volatile and not equivalent to production adoption.
    - The adoption and reference-implementation statements remain maintainer-reported unless corroborated by independent deployment or official governance evidence.
- Direct quotation under 25 words: "about 6 weeks"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Helps identify dependency popularity and project activity, while preserving the distinction between open-source attention and deployed assurance.
- Reliability assessment:
  - High for observed GitHub repository metadata at access time. Medium for adoption claims because they are maintainer-reported and not independently audited here.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

## Required Source Gaps

- `TODO-fastmcp-official-sdk-confirmation`: narrowed. The official MCP Python SDK README currently imports `mcp.server.fastmcp.FastMCP`, while FastMCP project/changelog sources report the 2024 incorporation history. No separate official historical incorporation statement was recovered in this lane.
- `TODO-fastmcp-release-url-recovery`: closed for PyPI, GitHub v3.2.4, FastMCP 3.0 GA, Code Mode, 2.10 compliance, Apps overview, and repository/adoption leads.
- `TODO-fastmcp-version-date-reconcile`: closed. PyPI upload is 2026-04-14T01:42:26Z and GitHub v3.2.4 is 2026-04-14T01:42:08Z; the local 2026-04-13 snippet is a display/timezone artifact.
- `TODO-fastmcp-conformance-evidence`: narrowed. Exact 2.10 release URL and date recovered; evidence remains project-reported compliance without independent conformance tests or official certification.
- `TODO-fastmcp-adoption-evidence`: narrowed. GitHub metadata and maintainer adoption posts recovered; no independently audited production adoption data.
