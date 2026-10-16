# GitHub discovery and showcase playbook

**Status:** proposal only; repository descriptions, topics, social-preview settings and GitHub Pages are NOT modified by this document.

## What we learned from Harvey
- Place a specific, audience-oriented one-sentence promise at the top of the README.
- Show a **real, labelled** command/output or screenshot before a long technical explanation.
- Follow with: why it matters → how it works → quick start → evidence and limitations → next action.
- Use images as evidence or clearly labelled diagrams; do not invent screenshots, performance figures or visitors.
- Maintain technical reference docs separately and link to them, rather than duplicating information.

## GitHub search discovery
GitHub repository search usually considers repository name, description and topics; searching README content requires an explicit `in:readme` qualifier (GitHub documentation). Therefore **description and topics require dedicated work beyond README changes**.

### Suggested repository metadata (review before applying)

| Repository | Suggested short description | Suggested topics |
| --- | --- | --- |
| `quality-docs-validator` | Local Python CLI to check potential PFMEA and Control Plan inconsistencies in Excel files. | `pfmea`, `control-plan`, `quality-engineering`, `apqp`, `python`, `cli`, `excel` |
| `public-repo-audit` | Deterministic local CLI for assessing GitHub repository publication readiness. | `github`, `repository-audit`, `python`, `cli`, `software-quality`, `developer-tools` |
| `agent-skill-quality-gate` | Deterministic quality checks and CI reporting for AI agent SKILL.md files. | `ai-agents`, `agent-skills`, `quality-gate`, `python`, `ci`, `developer-tools` |
| `project-pilot` | Local CLI to manage project lifecycle phases, required artefacts and human approval gates. | `project-management`, `workflow`, `cli`, `python`, `local-first` |
| `AgentDesk` | Local-first CLI coordinating prompts, handoffs and quality gates for AI-assisted projects. | `ai-agents`, `claude-code`, `codex`, `python`, `workflow`, `local-first` |

These are **proposals, not applied settings**. Verify keywords and project positioning before modifying topics via the GitHub About panel. GitHub topics must be lowercase and hyphenated.

## Showcase acceptance criteria
1. Clear target visitor and benefit within the first screen.
2. Demo is authentic: real recorded output, synthetic input clearly labelled, or truthful architectural diagram.
3. Quick-start copied from verified repository docs.
4. Human limits and unavailable features prominently disclosed.
5. Internal links resolve and rendered images work on GitHub.
6. README links from profile to each project and back; no duplicate promises.
7. Metadata (description/topics/social preview) reviewed and updated only after approval.
8. Record a baseline of GitHub repository traffic (views, clones, referrers) and search performance, where accessible, before measuring later changes. Do not attribute growth to README alone.
9. GitHub Pages requires separate publishing permission, live canonical URLs, sitemap, responsive/accessibility tests and a real preview.

## Proposed publishing order
1. Approve revised personal profile and quality-docs-validator README.
2. Approve metadata and optional social-preview image for quality-docs-validator.
3. Repeat README showcase on public-repo-audit and agent-skill-quality-gate.
4. Expand to ProjectPilot and AgentDesk based on verified releases.
5. Build Pages landing pages from the same factual source content, avoiding copy-paste duplication.

Sources: GitHub docs on READMEs, topics and repository search; Google Search Central on descriptive titles and snippets.
