# Miguel Alexandre Vieira Santos

### Quality Engineering × Open-Source Software × AI Workflows

I build **practical, explainable tools** for engineers and developers — from cross-checking quality documents to auditing repositories and coordinating AI-assisted projects.

My background is in automotive supplier quality, root cause investigation and corrective actions. I apply the same discipline to software: **explicit rules, traceable findings, local-first workflows and human approval gates**.

[Explore my projects](#featured-open-source-projects) · [How I work](#engineering-approach) · [Get in touch](#contact)

---

## Featured open-source projects

### [Quality Docs Validator](https://github.com/migmcc/quality-docs-validator) — spot potential PFMEA ↔ Control Plan gaps

**For quality, process and manufacturing engineers.** Check two Excel workbooks for missing controls, unmatched process steps and other potential inconsistencies **before technical review**.

| Example run on bundled synthetic files | Result |
| --- | --- |
| Potential findings | 3 critical · 3 warnings |
| Severity-weighted score | **43/100 — FAIL** |
| Outputs | Terminal, Markdown, JSON |

> The example is deliberately seeded with inconsistencies. The tool highlights **potential** issues for engineering judgement; it does **not** certify compliance or replace review.

```bash
git clone https://github.com/migmcc/quality-docs-validator.git
cd quality-docs-validator
pip install -e .
qdv pfmea-control-plan --pfmea examples/pfmea.xlsx --control-plan examples/control-plan.xlsx --out report.md
```

[See the full example report](https://github.com/migmcc/quality-docs-validator/blob/main/examples/report.md) · [Read the six checks](https://github.com/migmcc/quality-docs-validator/blob/main/docs/FINDINGS.md) · [View source](https://github.com/migmcc/quality-docs-validator)

### More tools

| Project | What problem it solves | Start here |
| --- | --- | --- |
| **[Public Repo Audit](https://github.com/migmcc/public-repo-audit)** | Checks whether a local repository has the documentation, tests, CI and packaging signals needed for public release. | [README](https://github.com/migmcc/public-repo-audit#readme) |
| **[Agent Skill Quality Gate](https://github.com/migmcc/agent-skill-quality-gate)** | Deterministic quality checks for `SKILL.md` files, including basic safety *heuristics* and CI-friendly output. | [README](https://github.com/migmcc/agent-skill-quality-gate#readme) |
| **[ProjectPilot](https://github.com/migmcc/project-pilot)** | Keeps track of the project lifecycle, required artefacts and human approval gates, without executing agents. | [README](https://github.com/migmcc/project-pilot#readme) |
| **[Agent Desk](https://github.com/migmcc/AgentDesk)** | Structures and coordinates manual AI-assisted work across Codex, Claude Code and local models. | [README](https://github.com/migmcc/AgentDesk#readme) |

**[Browse all public repositories →](https://github.com/migmcc?tab=repositories)**

## Engineering approach

- **Useful before flashy:** start with a concrete problem and a runnable example.
- **Evidence over claims:** link to documentation, real outputs and tests.
- **Human in control:** software assists decisions rather than hiding them.
- **Transparent scope:** state what each project does *not* support.
- **Local-first when practical:** prioritise data control and understandable execution.

My professional work includes supplier claims and warranty analysis, 8D / SCAR, IATF 16949, ISO 9001, AIAG Core Tools and VDA methods.

## Collaboration

I also contribute to work on reusable AI skills and agent workflows. Collaborative projects are distinguished from the tools I maintain in this portfolio.

## Contact

Based in Braga, Portugal.

[Email](mailto:migmcc@gmail.com) · [LinkedIn](https://www.linkedin.com/in/miguelavs) · [GitHub](https://github.com/migmcc)

---

<sub>Project capabilities and example outputs are drawn from their linked repositories. No traffic or conversion claims are implied.</sub>
