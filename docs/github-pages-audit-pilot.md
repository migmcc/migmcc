# GitHub Profile & Pages — Audit and Pilot (draft)

Status: **Draft only — not published**. Branch: `feature/profile-portal-pilot`.

## Baseline
- Profile repository `migmcc/migmcc` contains a README describing quality engineering and AI workflows, with projects including SkillLab and an AI content pipeline. Some entries are private or planned; public visitors cannot necessarily inspect them.
- 22 public repositories identified under `migmcc`. Not all are original products; forks, learning exercises and collaborations must be labeled rather than presented as owned software.
- Reference `RBraga01/a-team` separates README pitch, operational docs and GitHub Pages visual presentation.
- Pilot `migmcc/quality-docs-validator` has an MIT license, Python 3.12+, CLI `qdv`, sample reports and technical docs. It compares PFMEA and Control Plan XLSX files, reports **potential** inconsistencies, and does not replace engineering review.

## Priority issues and actions
1. **Portfolio positioning:** distinguish personal engineering portfolio from CriaTek commercial site. Avoid suggesting all projects are CriaTek products.
2. **Profile accuracy:** verify ownership, status and public availability before featuring projects. Avoid advertising planned work as shipped.
3. **Discovery:** use one indexable portfolio hub with unique project pages; link directly to canonical repository documentation.
4. **SEO:** unique titles, descriptions, canonical URLs, sitemap, robots.txt, social cards, and relevant SoftwareSourceCode JSON-LD; verify generated HTML and mobile experience.
5. **Evidence:** only show screenshots, claims, metrics and supported features verified from repository files; never invent testimonials or results.
6. **Governance:** no GitHub Pages activation, DNS changes, merges or pushes to main without approval.

## Pilot: Quality Docs Validator
**Audience:** quality/process/manufacturing engineers, SQEs, APQP/PPAP teams.

**Problem:** gaps between PFMEA and Control Plan can be missed when documents are reviewed separately.

**Promise:** local-first CLI checks two XLSX workbooks against six explicit consistency rules and produces severity-classified *potential findings* in Markdown or JSON.

**CTA:** View repository / Read findings reference / Try synthetic examples.

**Constraints:** human engineering review remains mandatory; no regulatory certification claim, no cloud processing claim beyond documented local execution.

**Proposed URL:** `https://migmcc.github.io/projects/quality-docs-validator/` (not live).

## Acceptance gates
- Static HTML works without JavaScript; keyboard accessible and responsive.
- Content traceable to current README/docs; no stale version claims.
- Internal links, SEO metadata, canonical, schema and sitemap validated.
- No accidental private-repo exposure or credentials.
- Build and tests pass on isolated branch; human visual approval before publication.

## Next phase
Create a dedicated `migmcc.github.io` repository **only after approval**. Build the portfolio hub and this pilot page in a review branch; keep GitHub Pages disabled until explicit go-live authorization.
