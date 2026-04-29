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
- Author/organisation: FastMCP project; TODO-local-import-maintainer-ownership-confirmation
- Publication/update date: Current documentation page; no stable publication date visible in local notes
- Date accessed: 2026-04-29
- URL: https://gofastmcp.com/getting-started/welcome
- Source type: primary
- Key claims:
  - Facts:
    - The imported synthesis says the current standalone FastMCP project describes itself as a framework for building MCP servers, clients, and applications.
    - The imported synthesis says FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024 and the standalone project later continued independently.
    - The imported synthesis says FastMCP documentation warns that parity with the official API cannot be assumed as the projects diverge.
  - Reported opinions:
    - Local citation snippets describe FastMCP as the standard framework for building MCP servers and clients.
  - Analysis:
    - This source supports treating FastMCP as an implementation and developer-experience layer above MCP, not as a competing protocol.
    - The official Python SDK relationship should be corroborated with an MCP Python SDK primary source before being used as a central timeline fact.
- Direct quotation under 25 words: "standard framework for building MCP servers and clients"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Helps decision-makers distinguish adoption of MCP itself from adoption of a higher-level framework that may add convenience, composition, proxying, testing, auth helpers, and application patterns.
- Reliability assessment:
  - Medium-high for FastMCP project self-description. Medium for SDK lineage until corroborated by an official MCP Python SDK source.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### FM-002 - FastMCP package release record

- Citation key: `fastmcp-pypi-2026-04-13`
- Title: FastMCP
- Author/organisation: FastMCP project / PyPI
- Publication/update date: 2026-04-13 for the latest PyPI release in the local citation snippet
- Date accessed: 2026-04-29
- URL: TODO-local-import-exact-url-missing; citation export includes PyPI title/snippets but not the full project URL.
- Source type: primary
- Key claims:
  - Facts:
    - The local citation export says the latest FastMCP package version was released on 2026-04-13.
    - The imported synthesis says the latest GitHub release was v3.2.4 on 2026-04-14; TODO-reconcile-date-source because this may reflect timezone or source differences.
    - The local citation export says the package provides a way to build MCP servers and clients.
  - Reported opinions:
    - The package tagline describes FastMCP as "fast" and "Pythonic."
  - Analysis:
    - Package-index evidence supports active maintenance and version tracking.
    - It does not establish public-sector readiness, production deployment, or API parity with official SDKs.
- Direct quotation under 25 words: "The fast, Pythonic way to build MCP servers and clients."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Useful for assessing release recency, dependency-management requirements, and whether a hub would be relying on an actively moving third-party framework.
- Reliability assessment:
  - Medium until exact URL and raw package metadata are recovered. High for package release facts once verified against PyPI.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-003 - Releases - PrefectHQ/fastmcp

- Citation key: `fastmcp-github-releases-2026-04`
- Title: Releases - PrefectHQ/fastmcp
- Author/organisation: FastMCP maintainers / GitHub
- Publication/update date: Local citation export shows GitHub release verification on 2026-04-13; imported synthesis reports v3.2.4 on 2026-04-14
- Date accessed: 2026-04-29
- URL: TODO-local-import-exact-url-missing; citation export includes title but not the full GitHub releases URL.
- Source type: primary
- Key claims:
  - Facts:
    - The imported synthesis says FastMCP reached v3.2.4 by end-April 2026.
    - The local citation export includes a GitHub releases result for `PrefectHQ/fastmcp`.
    - The local citation export includes release-note text about fixing suppression of server stderr in `fastmcp call`.
  - Reported opinions:
    - TODO-raw-source-needed for maintainer release positioning.
  - Analysis:
    - GitHub releases are suitable for version chronology and release-note facts, once the exact local source URL is recovered.
    - Do not use release cadence alone as evidence of governance maturity or support guarantees.
- Direct quotation under 25 words: "fix: stop suppressing server stderr"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports dependency-risk review, upgrade cadence assessment, and the need to pin framework versions before using FastMCP in a managed hub.
- Reliability assessment:
  - Medium until exact release URL is recovered; likely high for release chronology once verified against GitHub.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-004 - FastMCP 3.0 is GA

- Citation key: `fastmcp-3-0-ga-2026-02-18`
- Title: FastMCP 3.0 is GA
- Author/organisation: Mostly Harmless / FastMCP maintainer blog; TODO-local-import-maintainer-confirmation
- Publication/update date: 2026-02-18
- Date accessed: 2026-04-29
- URL: TODO-local-import-exact-url-missing; citation export includes title/date but not the full URL.
- Source type: primary / secondary; TODO-classify-after-raw-source
- Key claims:
  - Facts:
    - The local citation export says FastMCP 3.0 was stable and generally available on 2026-02-18.
    - The snippet includes an installation command, `pip install fastmcp -U`.
  - Reported opinions:
    - The release announcement presents 3.0 as a stability milestone.
  - Analysis:
    - This supports claims that FastMCP's standalone branch had reached a v3 stable release by early 2026.
    - It should not be used for protocol behaviour unless supported by MCP specifications or official SDK documentation.
- Direct quotation under 25 words: "FastMCP 3.0 is stable"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant for deciding whether FastMCP is merely experimental or has a separately maintained release line that may need supplier/dependency review.
- Reliability assessment:
  - Medium until source ownership and exact URL are recovered. Stronger for release-positioning facts if confirmed as a maintainer post.
- Sections where this source may be cited:
  - `05-timeline-and-evolution.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`

### FM-005 - Stop Calling Tools, Start Writing Code (Mode)

- Citation key: `fastmcp-code-mode-2026-03-03`
- Title: Stop Calling Tools, Start Writing Code (Mode)
- Author/organisation: Mostly Harmless / FastMCP maintainer blog; TODO-local-import-maintainer-confirmation
- Publication/update date: 2026-03-03
- Date accessed: 2026-04-29
- URL: TODO-local-import-exact-url-missing; citation export includes title/date but not the full URL.
- Source type: primary / secondary; TODO-classify-after-raw-source
- Key claims:
  - Facts:
    - The local citation export says the post discusses a server with two hundred tools putting two hundred schemas into the context window.
    - The imported synthesis says FastMCP 3.1 added a Code Mode capability.
  - Reported opinions:
    - The post argues for code-mediated execution instead of exposing large tool catalogs directly to the model.
  - Analysis:
    - This is useful evidence for FastMCP's implementation philosophy: it tries to reduce context overhead by layering developer tooling over MCP.
    - It is not neutral evidence of the general cost of MCP; use independent or official client-guidance sources for broader performance claims.
- Direct quotation under 25 words: "two hundred schemas into the context window"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Supports evaluating whether a hub should permit large direct tool catalogs or require brokered/code-mediated patterns for broad API surfaces.
- Reliability assessment:
  - Medium. Useful maintainer/practitioner evidence, but advocacy-heavy and not independent benchmarking.
- Sections where this source may be cited:
  - `04-technical-critiques-and-mitigations.md`
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

### FM-006 - FastMCP 2.10 compliance with the 2025-06-18 MCP specification update

- Citation key: `fastmcp-2-10-spec-compliance`
- Title: FastMCP 2.10 achieves full compliance with the 6/18/2025 MCP specification update
- Author/organisation: FastMCP project
- Publication/update date: TODO-local-import-date-missing
- Date accessed: 2026-04-29
- URL: TODO-local-import-exact-url-missing; citation export includes title/snippet but not the full URL.
- Source type: primary
- Key claims:
  - Facts:
    - The local citation export says FastMCP 2.10 achieved full compliance with the 2025-06-18 MCP specification update.
    - The local citation export says the release introduced elicitation support and new communication patterns.
  - Reported opinions:
    - "Full compliance" is a project-reported claim and should be treated as such unless corroborated by tests or official conformance criteria.
  - Analysis:
    - This source can support FastMCP's claim to track MCP spec evolution, but not independent conformance.
    - Any protocol-level claims must still cite the official 2025-06-18 MCP specification notes.
- Direct quotation under 25 words: "full compliance with the 6/18/2025 MCP specification update"
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant to dependency selection: a hub adopting FastMCP needs to know which MCP spec versions are implemented and how conformance is tested.
- Reliability assessment:
  - Medium. Primary project claim but exact URL, date, and conformance methodology are missing from local evidence.
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
- URL: TODO-local-import-exact-url-missing; citation export includes FastMCP Apps snippets but not the page URL.
- Source type: primary
- Key claims:
  - Facts:
    - The local citation export says FastMCP Apps were new in version 3.0.0.
    - The local citation export says MCP tools normally return text, while apps support data users want to explore.
    - The imported synthesis says recent releases added interactive application support via `FastMCPApp` in 3.2.
  - Reported opinions:
    - FastMCP frames apps as a better fit for interactive outputs such as dashboards, forms, and visualizations.
  - Analysis:
    - This source supports the view that FastMCP is building an application framework layer above MCP's core protocol.
    - It should not be cited as evidence that MCP core itself specifies these app behaviours unless official MCP Apps sources also support the claim.
- Direct quotation under 25 words: "MCP tools normally return text."
- Relevance to Government / Local Authority AI Hub decision-making:
  - Relevant if a public-sector hub needs interactive forms, dashboards, or case-management views rather than text-only tool results.
- Reliability assessment:
  - Medium until exact page URL and release/version details are recovered. High for FastMCP project self-description once verified.
- Sections where this source may be cited:
  - `06-mcp-vs-alternatives.md`
  - `07-hype-vs-substance.md`
  - `09-government-local-authority-ai-hub.md`

## Required Source Gaps

- `TODO-fastmcp-official-sdk-confirmation`: recover an official MCP Python SDK source for the claim that FastMCP 1.0 was incorporated into the official SDK in 2024.
- `TODO-fastmcp-release-url-recovery`: recover exact local URLs for PyPI, GitHub releases, FastMCP 3.0 GA, Code Mode, 2.10 compliance, and Apps documentation.
- `TODO-fastmcp-version-date-reconcile`: reconcile PyPI release date 2026-04-13 with imported synthesis saying GitHub v3.2.4 on 2026-04-14.
- `TODO-fastmcp-conformance-evidence`: local evidence records project-reported spec compliance, but not independent conformance tests or official certification.
- `TODO-fastmcp-adoption-evidence`: local snippets mention GitHub stars and project popularity, but no independently audited production adoption data.
