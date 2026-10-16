# MigMCC portal — prepublication review

This is an unpublished static site, stored under `site/` in the `feature/github-pages-portal-review` branch of `migmcc/migmcc`. The existing public profile README is unaffected.

## Preview locally

From the repository root: `python -m http.server 8000 --directory site`, then open `http://localhost:8000`. The HTML also supports file-based browsing from `site/index.html`.

## Scope

- Home page, searchable project catalog, about/contact page, five individual project landing pages.
- Responsive, keyboard-accessible static HTML/CSS and a minimal client-side search on the catalog.
- Draft SEO metadata: unique titles, descriptions, social title/description, semantic headings; `noindex,nofollow` intentionally applied.
- No canonical, sitemap or Schema.org domain URLs are invented before the deployment URL is approved.
- Project statements and commands are grounded in the GitHub repositories as inspected on 2026-10-17.

## Release gate — explicit approval required

1. Visually review all eight pages on desktop and mobile (including keyboard focus and small screens).
2. Confirm the five selected projects, descriptions, contact details, labels and links.
3. Validate all internal links and external documentation URLs, and rerun copy/paste quick starts where possible.
4. Decide publishing architecture: dedicated `migmcc.github.io` site repo vs folder deployment; profile repo itself is not a Pages site.
5. Set real public deployment base URL; then remove `noindex,nofollow`, add correct canonical URLs, OG URLs, JSON-LD `SoftwareSourceCode` and sitemap.xml / robots.txt.
6. Test Pages build and robots/search indexing before measuring organic traffic. Record baseline visits and referrals if available.
7. Separately authorize publication and any domain/DNS changes; no deployment is configured in this branch.

## Known constraints

No real GIF terminal recording is included; the flow diagram is explicitly illustrative. Search function is local-only and does not use a search API. The preview carries no cookies, analytics or externally hosted fonts.
