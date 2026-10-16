#!/usr/bin/env python3
"""Check unpublished portal structure without external dependencies.

Run: python site/tests/validate_portal.py
This checks structure, not live browser rendering, content truth or external links.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path(__file__).resolve().parents[1]
EXPECTED = [
    "index.html",
    "404.html",
    "about/index.html",
    "projects/index.html",
    "projects/quality-docs-validator/index.html",
    "projects/public-repo-audit/index.html",
    "projects/agent-skill-quality-gate/index.html",
    "projects/project-pilot/index.html",
    "projects/AgentDesk/index.html",
]
ASSETS = ["assets/site.css", "assets/catalog.js"]


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.description = False
        self.noindex = False
        self.viewport = False
        self.title = False
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title = True
        if tag == "meta" and a.get("name") == "description" and a.get("content"):
            self.description = True
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        if tag == "meta" and a.get("name") == "robots" and "noindex" in (a.get("content") or ""):
            self.noindex = True
        if a.get("id"):
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])


def validate() -> list[str]:
    errors: list[str] = []
    for name in EXPECTED + ASSETS:
        if not (SITE / name).is_file():
            errors.append(f"Missing file: {name}")
    for name in EXPECTED:
        html = SITE / name
        if not html.is_file():
            continue
        parser = Page()
        parser.feed(html.read_text(encoding="utf-8"))
        if parser.h1 != 1:
            errors.append(f"{name}: expected 1 h1, got {parser.h1}")
        for field in ("description", "title", "viewport", "noindex"):
            if not getattr(parser, field):
                errors.append(f"{name}: missing {field}")
        if "main" not in parser.ids:
            errors.append(f"{name}: missing main landmark id")
        for url in parser.links:
            parsed = urlsplit(url)
            if parsed.scheme or url.startswith("//"):
                continue
            if parsed.path:
                target = (html.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(SITE.resolve()):
                    errors.append(f"{name}: link escapes site: {url}")
                elif not target.is_file():
                    errors.append(f"{name}: broken internal link: {url}")
            elif url.startswith("#") and parsed.fragment and parsed.fragment not in parser.ids:
                errors.append(f"{name}: missing anchor: {url}")
    return errors


if __name__ == "__main__":
    problems = validate()
    for issue in problems:
        print(f"FAIL: {issue}")
    if problems:
        raise SystemExit(1)
    print(f"PASS: {len(EXPECTED)} HTML pages, assets, metadata and local paths checked.")
