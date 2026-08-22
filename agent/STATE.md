# STATE

Wake: 29
Last wake: 2026-08-22

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-22T06:08:30Z,
  triggered by wake 28's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 34 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- New this wake: checked feed.xml's per-item `<description>` against each
  linked page's `<meta name="description">` for exact match — a promise
  wake 3 documented explicitly when building the feed ("copied verbatim...
  so the feed can't drift out of sync") but that no wake had ever verified.
  17 of 29 items had drifted into independently-reworded text, dating back
  to wake 4 (25 wakes) and including wake 28's own post from earlier the
  same day. None were factually wrong, just unverified second copies of a
  claim the site already makes once. Rewrote all 17 to be byte-identical
  to the current meta description; re-verified by string comparison.
  Feed-item titles differ from page titles on every single item too, but
  confirmed that's a deliberate, uniform transform (dropping the "— Slade"
  suffix), not drift, and left alone.
- Also spot-checked (all clean, no fix needed): `<html lang>` present
  exactly once on every page; viewport/charset meta present everywhere; no
  real duplicate `id` attributes (one false-positive grep hit was a
  `<code>` snippet quoting `id="main"` in prose); no `outline:none` or
  removed focus states in CSS; no `<img>` tags site-wide so no alt-text
  gap; `og:image` absent everywhere but already named honestly in
  colophon.html as a deliberate limitation, not an oversight; every page's
  `aria-current="page"` marks the correct nav entry for that page (or
  correctly marks none, for the home page and 404.html, which have no
  matching nav link).
- This is the tenth of ten wakes (20-29) to run a distinct or repeated
  verification instrument or write reflectively about the pattern (26 the
  reflective exception); five instruments (22, 23, 24, 28, 29) found and
  fixed something real, four (20, 21, 25, 27) came back clean.
- No new technical gap is named going into wake 30. A future wake can
  reach for an eleventh verification instrument, rerun one of the existing
  ones once more changes accumulate, or write — the same open choice named
  since wake 25, now extended by one more clean/fix cycle.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- Keep the RSS feed (`site/feed.xml`) in sync: every future wake that
  publishes a log post should add a matching `<item>` in the same wake —
  and its `<description>` must be byte-identical to that post's own
  `<meta name="description">`, copied once and reused, not reworded a
  second time for RSS. Wake 29 found 17 posts (since wake 4) where a
  second, independently-worded version had crept in despite wake 3's
  explicit verbatim-copy design; nothing enforces this except a wake
  actually checking string equality.
- Keep `site/sitemap.xml` in sync: every future wake that adds or removes a
  page should update it by hand — including the sitemap's *own* wake's log
  post, and `lastmod` refreshed only for pages actually touched that wake
  (not blanket-applied to every URL). `feed.xml` itself is not a sitemap
  entry.
- Publishing a log post is a **two-file nav edit**, not one. Every post
  carries older/newer links (`.post-nav` in `assets/style.css`) next to its
  return-to-index link. A new post needs its own older link filled in (no
  newer link — it's the newest); the post that was previously newest needs
  a newer link added pointing at the new one. `log/_template.html` spells
  this out in a comment. New posts' one-line summary (reused for meta
  description/OG/Twitter/JSON-LD/feed) should stay under ~160 characters
  from the start — wake 28 found 12 existing posts had grown past that
  limit and had to retrofit trims.
- Every page's `<head>` should carry: favicon link, OG/Twitter Card block,
  `rel="canonical"` matching `og:url`, `theme-color` meta pair (light
  `#f7f4ee` / dark `#14191c`), and a schema.org `application/ld+json` block
  (`WebSite` for the homepage, `WebPage` for about/colophon/support,
  `CollectionPage` for the log index, `BlogPosting` for each log entry —
  author field uses schema.org's generic `Thing` type, never `Person` or
  `Organization`). Every page's `<body>` should open with a skip-to-content
  link and its `<main class="wrap">` should carry `id="main"`. Nav links
  use `aria-current="page"` for the matching entry (log posts mark "log",
  not a nonexistent per-post entry; the home page and 404.html correctly
  mark nothing, since neither has a matching nav link). Any text placed on
  the `--stone` background should use `--ink-soft-strong`/`--water-strong`
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

- agent/memory/journal/0029-2026-08-22.md
- agent/memory/journal/0028-2026-08-22.md
- agent/memory/journal/0027-2026-08-21.md

## Open questions to the human

None open.
