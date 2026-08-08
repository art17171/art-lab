#!/usr/bin/env python3
"""Site smoke check. Stdlib only. Run from anywhere; exits nonzero on failure.

Gates every wake's commit (PROTOCOL.md phase 4) and every Pages deploy
(.github/workflows/pages.yml). If this fails in CI, the previous deploy
stays live.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
DOMAIN = "demo-slayer.com"
MAX_BYTES = 200 * 1024
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

errors = []


class Checker(HTMLParser):
    """Tracks tag balance and collects href/src references."""

    def __init__(self, name):
        super().__init__(convert_charrefs=True)
        self.name = name
        self.stack = []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.refs.append((v, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            errors.append(f"{self.name}:{self.getpos()[0]}: closing </{tag}> with nothing open")
            return
        open_tag, line = self.stack.pop()
        if open_tag != tag:
            errors.append(f"{self.name}:{self.getpos()[0]}: </{tag}> closes <{open_tag}> opened at line {line}")


def is_external(ref):
    return ref.startswith(("http://", "https://", "mailto:", "//", "#", "data:"))


def main():
    if not SITE.is_dir():
        errors.append(f"missing site directory: {SITE}")
        report()

    cname = SITE / "CNAME"
    if not cname.is_file() or cname.read_text().strip() != DOMAIN:
        errors.append(f"site/CNAME must contain exactly '{DOMAIN}'")

    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        errors.append("no HTML files under site/")

    for page in pages:
        rel = page.relative_to(SITE)
        raw = page.read_bytes()
        if len(raw) > MAX_BYTES:
            errors.append(f"{rel}: {len(raw)} bytes exceeds {MAX_BYTES}")
        text = raw.decode("utf-8", errors="replace")

        is_template = page.name == "_template.html"
        if not is_template and re.search(r"\{\{[A-Z_]+\}\}", text):
            errors.append(f"{rel}: leftover {{{{PLACEHOLDER}}}} in a live page")

        checker = Checker(str(rel))
        checker.feed(text)
        checker.close()
        for tag, line in checker.stack:
            errors.append(f"{rel}:{line}: <{tag}> never closed")

        # every relative href/src must resolve to a real file
        for ref, line in checker.refs:
            if is_external(ref) or is_template:
                continue
            target = ref.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (page.parent / target).resolve()
            if not resolved.is_file():
                errors.append(f"{rel}:{line}: broken link '{ref}'")

    # markers wakes depend on
    home = (SITE / "index.html").read_text(errors="replace") if (SITE / "index.html").is_file() else ""
    for marker in ("<!-- STATUS:BEGIN", "<!-- STATUS:END"):
        if marker not in home:
            errors.append(f"index.html: missing marker '{marker}'")

    log_index_path = SITE / "log" / "index.html"
    log_index = log_index_path.read_text(errors="replace") if log_index_path.is_file() else ""
    if "<!-- POSTS:NEWEST-FIRST" not in log_index:
        errors.append("log/index.html: missing POSTS:NEWEST-FIRST marker")

    # every post listed <-> every post file exists (both directions)
    post_files = {p.name for p in (SITE / "log").glob("*.html")
                  if p.name not in ("index.html", "_template.html")}
    listed = set(re.findall(r'href="([^"/]+\.html)"', log_index))
    listed.discard("index.html")
    listed = {l for l in listed if not l.startswith("../")}
    for missing in sorted(post_files - listed):
        errors.append(f"log/{missing} exists but is not listed in log/index.html")
    for ghost in sorted(listed - post_files):
        errors.append(f"log/index.html links to log/{ghost} which does not exist")

    report()


def report():
    if errors:
        print(f"SMOKE CHECK FAILED — {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("smoke check passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
