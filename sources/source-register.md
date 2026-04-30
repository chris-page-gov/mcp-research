# Source Register

Date accessed for current register review: 2026-04-30.

This is the project-level map of source-note files. Detailed source metadata lives inside each file.

| Source note file | Status | Primary use | Acceptance state |
| --- | --- | --- | --- |
| `sources/official-specs.md` | Started | Protocol facts and official MCP documentation | Contains accepted entries for authorization, transports, tools, resources, prompts, lifecycle, sampling, elicitation, security best practices, intro, architecture, client guidance, registry, roadmap, transport future, roots, tasks, and published-server versioning; roots/tasks quotation gaps are closed. |
| `sources/security-research.md` | Started | Security evidence, advisories, academic/security-lab research, public-sector AI security guidance | Structured entries present; final weighting still needed for vendor claims and preprints. |
| `sources/discourse-and-criticism.md` | Started | Reported opinions, public debate, community implementation criticism | Working notes now cover security discourse, distributed-systems criticism, context bloat, project-scoping friction, discovery/private-registry issue evidence, and positive product leads; broader representative sampling remains a scoped evidence gap. |
| `sources/vendor-adoption.md` | Started | Vendor implementation and adoption evidence | Working notes now cover AAIF/Linux Foundation governance and OpenAI, Microsoft, GitHub, Google Cloud, Cloudflare, product-control depth, and independent preprint evidence; audited vendor adoption and entitlement-specific assurance gaps remain. |
| `sources/fastmcp.md` | Started | FastMCP history, role, and SDK relationship | Working notes now cover FastMCP docs, release/version leads, Code Mode, spec-compliance claims, Apps, repository metadata, public conformance CI, and independent example uses; formal certification and audited adoption remain open. |
| `sources/alternatives-skills-agents.md` | Started | Alternatives to MCP and layered architectures | Working notes now cover function calling, LangChain, Semantic Kernel, Agent Skills, Apps SDK, Microsoft MCP docs, OpenAI app submission, MCP Apps, hybrid models, GOV.UK open-standards evidence, and NCSC/NIST app-vetting evidence; direct framework-vs-MCP portability and AI connector procurement evidence remain scoped gaps. |

## Source Rules

- A paper section may cite only keys represented in `latex/references.bib`.
- A fact may be drafted only when it is backed by a structured source note.
- A `TODO-...` citation key is a blocker, not permission to assert a fact.
- Source notes should include relevance and reliability assessment before being used for public-sector recommendations.
