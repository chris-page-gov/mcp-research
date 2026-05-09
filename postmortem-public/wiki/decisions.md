# Decision Register

| ID | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| `private-public-split` | Keep raw assistant transcript evidence in ignored postmortem/ and publish only redacted registers and synthesis. | The skill requires a full audit archive while keeping raw prompts, local paths, and transcript bodies out of GitHub. | skills/assistant-postmortem-wiki/SKILL.md |
| `source-first-paper` | Delay full report prose until source notes and section-level acceptance criteria are stable. | The project started from a failed deep-research report and needed citation discipline before prose. | wiki/guidance/source-discipline.md |
| `llm-wiki` | Use a linked LLM-Wiki for guidance, progress, evaluation, and close procedures. | Large agent files and session context were becoming too broad; small linked notes support targeted retrieval. | wiki/index.md |
| `machine-readable-state` | Track paper progress and source TODOs in JSON registers. | Prose-only progress tracking caused drift after parallel worker lanes. | wiki/data/progress-register.json and wiki/data/source-todo-register.json |
| `parallel-workers` | Split source-note and section-skeleton work into disjoint worker lanes, then integrate centrally. | Context limits made broad single-agent source extraction brittle. | wiki/progress/parallel-work-plan.md |
