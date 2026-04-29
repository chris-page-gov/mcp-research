# Source Register

Date accessed for current register review: 2026-04-29.

This is the project-level map of source-note files. Detailed source metadata lives inside each file.

| Source note file | Status | Primary use | Acceptance state |
| --- | --- | --- | --- |
| `sources/official-specs.md` | Started | Protocol facts and official MCP documentation | Contains accepted entries for authorization, transports, tools, sampling, elicitation, security best practices, intro, architecture, client guidance, registry, roadmap, transport future, roots, and tasks; records explicit TODO gaps. |
| `sources/security-research.md` | Started | Security evidence, advisories, academic/security-lab research, public-sector AI security guidance | Structured entries present; final weighting still needed for vendor claims and preprints. |
| `sources/discourse-and-criticism.md` | Placeholder | Reported opinions, public debate, community implementation criticism | Must be populated before drafting sections 03 and non-security reported opinions in section 04. |
| `sources/vendor-adoption.md` | Placeholder | Vendor implementation and adoption evidence | Must be populated before positive ecosystem claims. |
| `sources/fastmcp.md` | Placeholder | FastMCP history, role, and SDK relationship | Must be populated before framework/tooling claims. |
| `sources/alternatives-skills-agents.md` | Placeholder | Alternatives to MCP and layered architectures | Must be populated before section 06 drafting. |

## Source Rules

- A paper section may cite only keys represented in `latex/references.bib`.
- A fact may be drafted only when it is backed by a structured source note.
- A `TODO-...` citation key is a blocker, not permission to assert a fact.
- Source notes should include relevance and reliability assessment before being used for public-sector recommendations.
