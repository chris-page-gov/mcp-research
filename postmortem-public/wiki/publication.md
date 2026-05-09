# Publication Decisions

| Evidence class | Public status | Rationale |
| --- | --- | --- |
| Raw Codex rollout JSONL | Private only | Contains prompts, tool calls, local paths, and full transcript bodies. |
| Session metrics | Public | Sanitized aggregate and per-session telemetry does not expose raw prompts. |
| Repository artifacts | Public | Already tracked in the public repository and linked by commit-specific permalinks. |
| Local filesystem paths | Redacted | Public derivative uses `<codex_home>` and repository-relative paths. |
| Third-party source bodies | Excluded | Source-note citations are enough for this postmortem; full copied bodies are not republished. |
