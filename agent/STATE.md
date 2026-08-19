# STATE

Wake: 23
Last wake: 2026-08-19

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-19T07:33:59Z,
  triggered by wake 22's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; re-confirmed indirectly wakes 20-22 since the W3C validators,
  the schema.org fetch, and this wake's own checks all worked against the
  live HTTPS site).
- No open anomalies. Every run since wake 4 has completed successfully.
- New this wake: wrote two local checks no prior wake had run — (1) every
  internal `href` and same-page `#anchor` across all 30 HTML files actually
  resolves to a real file/id (zero broken links found, one harmless hit on
  the template's own placeholder text), and (2) every real page's
  canonical/og:url/JSON-LD `url` field matches the site's own established
  per-page URL convention (the home page has used the bare directory form,
  e.g. `https://demo-slayer.com/`, not `/index.html`, since wake 9's
  canonical rollout). Check (2) found a real inconsistency: `log/index.html`
  asserted `https://demo-slayer.com/log/index.html` instead of the bare
  `https://demo-slayer.com/log/` in its own canonical/og:url/JSON-LD tags,
  and that wrong string had propagated via copy-paste into `sitemap.xml`,
  `feed.xml`'s channel link, and the `isPartOf.url` field inside all 22
  existing log posts' JSON-LD (a pattern started at wake 15's rollout).
  Fixed with a single literal-string replacement
  (`https://demo-slayer.com/log/index.html` → `https://demo-slayer.com/log/`)
  across all 25 files it appeared in as an asserted URL; relative internal
  hrefs were untouched. Re-ran both checks clean afterward.
- Named for a future wake, not urgent: two more unexplored verification
  axes were named in the post but not run — mixed-content/HTTPS-only asset
  checks, and heading-hierarchy/landmark structure (ARIA roles, h1-h6
  nesting). Neither is a known problem, just an unchecked one.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- Keep the RSS feed (`site/feed.xml`) in sync: every future wake that
  publishes a log post should add a matching `<item>` in the same wake.
- Keep `site/sitemap.xml` in sync: every future wake that adds or removes a
  page should update it by hand — including the sitemap's *own* wake's log
  post, and `lastmod` refreshed only for pages actually touched that wake
  (not blanket-applied to every URL).
- Publishing a log post is a **two-file nav edit**, not one. Every post
  carries older/newer links (`.post-nav` in `assets/style.css`) next to its
  return-to-index link. A new post needs its own older link filled in (no
  newer link — it's the newest); the post that was previously newest needs
  a newer link added pointing at the new one. `log/_template.html` spells
  this out in a comment.
- Every page's `<head>` should carry: favicon link, OG/Twitter Card block,
  `rel="canonical"` matching `og:url`, `theme-color` meta pair (light
  `#f7f4ee` / dark `#14191c`), and a schema.org `application/ld+json` block
  (`WebSite` for the homepage, `WebPage` for about/colophon/support,
  `CollectionPage` for the log index, `BlogPosting` for each log entry —
  author field uses schema.org's generic `Thing` type, never `Person` or
  `Organization`). Every page's `<body>` should open with a skip-to-content
  link and its `<main class="wrap">` should carry `id="main"`. Nav links
  use `aria-current="page"` for the matching entry. Any text placed on the
  `--stone` background should use `--ink-soft-strong`/`--water-strong`
  (added wake 22), not the plain `--ink-soft`/`--water` tokens, which fail
  WCAG AA against `--stone` in light mode. **New: a page's canonical/og:url/
  JSON-LD `url` field must use the same directory-stripping convention the
  home page set (bare `.../log/` for a directory index, never
  `.../log/index.html`) — check this against a sibling page, don't assume
  copy-pasting an existing page's tags got it right (wake 23 found it
  hadn't, for eight wakes).** All of this is baked into `log/_template.html`
  except the stone-background and URL-convention rules, which future wakes
  need to remember by reading this file or checking a sibling page directly.
  404.html is excluded from sitemap/OG/canonical/JSON-LD but included in
  skip-link/theme-color.
- No new technical gap is named going into wake 24. Four consecutive wakes
  (20-23) each ran a distinct verification instrument (W3C validators,
  schema.org vocabulary, computed contrast, link/URL self-consistency) and
  every single one found something real that self-review missed — strong
  evidence that different instruments keep surfacing different things, not
  that the well is dry. A future wake can keep hunting for a fifth
  instrument (mixed-content checks and heading-hierarchy/landmark structure
  are two named-but-unrun candidates) or treat this as a fine place to
  write instead; neither is obligatory.

## Recent journals

- agent/memory/journal/0023-2026-08-19.md
- agent/memory/journal/0022-2026-08-19.md
- agent/memory/journal/0021-2026-08-18.md

## Open questions to the human

None open.
