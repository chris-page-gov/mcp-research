# Source Register

Date accessed for current register review: 2026-04-29.

This is the project-level map of source-note files. Detailed source metadata lives inside each file.

| Source note file | Status | Primary use | Acceptance state |
| --- | --- | --- | --- |
| `sources/official-specs.md` | Started | Protocol facts and official MCP documentation | Contains accepted entries for authorization, transports, tools, sampling, elicitation, security best practices, intro, architecture, client guidance, registry, roadmap, transport future, roots, and tasks; records explicit TODO gaps. |
| `sources/security-research.md` | Started | Security evidence, advisories, academic/security-lab research, public-sector AI security guidance | Structured entries present; final weighting still needed for vendor claims and preprints. |
| `sources/discourse-and-criticism.md` | Started | Reported opinions, public debate, community implementation criticism | Working notes now cover security discourse, distributed-systems criticism, context bloat, discovery friction, and positive product leads; several entries remain TODO-grade pending exact source extraction. |
| `sources/vendor-adoption.md` | Started | Vendor implementation and adoption evidence | Working notes now cover AAIF/Linux Foundation governance and OpenAI, Microsoft, GitHub, Google Cloud, and Cloudflare evidence; raw-page and independent-adoption gaps remain. |
| `sources/fastmcp.md` | Started | FastMCP history, role, and SDK relationship | Working notes now cover FastMCP docs, release/version leads, Code Mode, spec-compliance claims, and Apps; exact URLs and independent conformance/adoption evidence remain TODO. |
| `sources/alternatives-skills-agents.md` | Started | Alternatives to MCP and layered architectures | Working notes now cover function calling, LangChain, Semantic Kernel candidate evidence, Agent Skills, Apps SDK, Microsoft MCP docs, MCP Apps, and hybrid models; some candidate entries remain TODO-grade. |

## Source Rules

- A paper section may cite only keys represented in `latex/references.bib`.
- A fact may be drafted only when it is backed by a structured source note.
- A `TODO-...` citation key is a blocker, not permission to assert a fact.
- Source notes should include relevance and reliability assessment before being used for public-sector recommendations.
