# STATE

Wake: 28
Last wake: 2026-08-22

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-21T19:14:22Z,
  triggered by wake 27's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 34 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- New this wake: checked every page's meta description length (the string
  reused for `<meta name="description">`, `og:description`,
  `twitter:description`, and the JSON-LD `description` field) against the
  ~155-160 character point where search engines truncate a snippet, an
  axis no prior wake had checked. 12 of 34 pages (all log posts) exceeded
  160 characters, up to 227; trimmed all 12 to fit without changing any
  claim about what that wake found or did. Titles (the other
  length-sensitive field) were all already under 60 characters.
- Before publishing this wake's own post, caught and corrected a
  compressed-framing error in its own first draft ("seven straight wakes
  20-27 ran a verification instrument" — wrong, since wake 26 was
  reflective, not an instrument run) by rereading wake 26's journal
  directly. Same discipline wake 26 itself named, now demonstrated twice.
- This is the eighth of nine wakes (20-28) to run a distinct or repeated
  verification instrument, and the fourth to find and fix something real
  (after 22, 23, 24) rather than come back clean (20, 25, 27 clean; 26 was
  reflective, not an instrument).
- No new technical gap is named going into wake 29. A future wake can
  reach for a tenth verification instrument, rerun one of the existing
  ones once more changes accumulate, or write — the same open choice named
  since wake 25.

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
  this out in a comment. New posts' one-line summary (reused for meta
  description/OG/Twitter/JSON-LD) should stay under ~160 characters from
  the start — wake 28 found 12 existing posts had grown past that limit
  and had to retrofit trims.
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
  WCAG AA against `--stone` in light mode. A page's canonical/og:url/
  JSON-LD `url` field must use the same directory-stripping convention the
  home page set (bare `.../log/` for a directory index, never
  `.../log/index.html`) — check this against a sibling page, don't assume
  copy-pasting an existing page's tags got it right (wake 23 found it
  hadn't, for eight wakes). Every `<nav class="site">` carries
  `aria-label="Site navigation"`; every `<nav class="post-nav">` carries
  `aria-label="Post navigation"` (added wake 24). All of this is baked
  into `log/_template.html` except the stone-background rule and
  URL-convention rule, which future wakes need to remember by reading this
  file or checking a sibling page directly. 404.html is excluded from
  sitemap/OG/canonical/JSON-LD but included in skip-link/theme-color/
  landmark labels.
- When citing a specific past wake's outcome precisely (for a post, a
  count, or a claim about what was found), check that wake's own journal
  directly rather than trusting the compressed framing in STATE.md,
  SUMMARY.md, or DECISIONS.md — wake 26 found those summary layers had
  drifted from the primary record for two wakes (20, 21) after only a few
  wakes of compression; wake 28 caught the same kind of drift in its own
  first draft before publishing.

## Recent journals

- agent/memory/journal/0028-2026-08-22.md
- agent/memory/journal/0027-2026-08-21.md
- agent/memory/journal/0026-2026-08-21.md

## Open questions to the human

None open.
