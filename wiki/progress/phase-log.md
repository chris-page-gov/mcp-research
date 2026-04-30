---
title: "Phase Log"
note_type: "log"
status: "active"
tags:
  - "progress"
  - "phase-log"
related:
  - "plan.md"
  - "parallel-work-plan.md"
  - "../index.md"
---

# Phase Log

## 2026-04-29

| Change | Reason | Follow-up |
| --- | --- | --- |
| Created section skeletons with acceptance criteria. | Avoid drafting before sources are accepted. | Populate source gaps before prose. |
| Created `sources/security-research.md` with structured security source entries. | Give section 04 a citation base. | Review vendor/preprint weighting during final drafting. |
| Started `sources/official-specs.md`. | Begin primary-source foundation for section 02. | Fill resources, prompts, roots, lifecycle, registry, roadmap, and context-management source notes. |
| Added LLM-Wiki guidance structure. | Keep agent context small and relevant. | Extend linting and metrics after first drafting pass. |
| Parallelized section 04 skeleton. | Reduce context pressure and keep technical critique separate. | Reconcile TODO citations and source gaps. |
| Imported citations file became available and was reconciled into official source notes. | Close official-source blockers without browsing. | Extract exact quotations for architecture, client best practices, roots, tasks, registry, and roadmap before final prose. |
| Published the public GitHub repository and confirmed CI. | Make the project shareable and repeatable. | Keep local wiki and validation reports current before each push. |
| Ran the next-step parallelism wiki evaluation. | Test whether the wiki can guide planning without loading broad context. | Consider adding a durable parallel work-plan note before starting multiple source-note workers. |
| Added a parallel work-plan note. | Make source-note worker scopes explicit before running multiple agents. | Update after integration if safe write sets change. |
| Ran four parallel source-note lanes. | Advance official specs, criticism, vendor/FastMCP, and alternatives without overlapping write scopes. | Integrate citation keys, source register status, and progress blockers before final prose. |
| Ran the next-step parallelism retest. | Compare wiki guidance after the parallel source-note batch against the previous evaluation run. | Use targeted blocker-closure lanes before drafting final prose. |
| Added drift investigation and session close procedure. | Prevent guidance, progress, source-register, and generated-report drift after parallel work. | Use the close procedure before every commit or final response. |
| Started section 09 risk-register skeleton. | Implement the optional Government / Local Authority lane without drafting recommendations. | Promote only after section 02, 04, 06, and vendor-control evidence stabilize. |
| Integrated parallel worker lanes and normalized BibTeX keys. | Workers closed exact extraction but left shared citation/register state to the integrator. | Keep `latex/references.bib`, source notes, and progress blockers synchronized during every close. |
| Extended wiki-state validation for source-note citation keys. | Citation-key drift was a repeated handoff risk. | Non-TODO citation keys in `sources/*.md` now fail validation if missing from BibTeX. |
| Ran next-step parallelism progress test. | Check whether the wiki can answer planning plus progress-to-completion questions after the close procedure. | Added completion dashboard after finding completion visibility was partial. |
| Closed roots/tasks official extraction and promoted section 02. | Complete the next official-spec blocker from the progress test. | Use section 02 as the first source-ready section when drafting begins. |
| Added completion dashboard. | Make progress-to-completion visible without ad hoc synthesis across several wiki notes. | Keep it synchronized during session close. |

## 2026-04-30

| Change | Reason | Follow-up |
| --- | --- | --- |
| Added top-level `CHANGELOG.md`. | Give public readers a conventional change history while keeping detailed operational tracking in the wiki. | Keep changelog, phase log, completion dashboard, and validation report synchronized before commits. |
| Added tracked VSCode Python workspace settings. | Avoid the isort language-server `EPIPE` failure and keep import organization under Ruff, matching repo checks. | Reload VSCode window if the old isort server keeps running. |
| Expanded progress tracking to every paper section. | The latest wiki evaluation showed the register only tracked priority sections. | Keep `wiki/data/progress-register.json`, acceptance criteria, and dashboard synchronized for all 12 sections. |
| Added machine-readable source TODO register. | Source-note TODO markers were partly prose-only and hard to validate. | Keep `wiki/data/source-todo-register.json` synchronized whenever source TODO markers are added, narrowed, closed, or removed. |
| Ran five targeted blocker-closure lanes. | Implement the wiki answer without starting full report prose. | Treat discourse, alternatives, vendor-control, section 09, and FastMCP blockers as narrowed unless residual evidence is explicitly found. |
| Added BibTeX records for 2026-04-30 evidence lanes. | Workers added new source-note citation keys that needed normalized citation records. | Keep source-note citation keys validation green before each close. |
| Ran post-integration next-step parallelism test. | Check whether the wiki answer changed after the five blocker lanes were integrated. | Add semantic guidance-alignment validation; structural validation does not catch stale current-bias prose. |
