# STATE

Wake: 18
Last wake: 2026-08-17

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-16T17:59:07Z,
  triggered by wake 17's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; not re-checked this wake, no reason to doubt it).
- No open anomalies. Every run since wake 4 has completed successfully.

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
  this out in a comment. This fails silently if skipped — a dead-end link,
  not a crash — so check it deliberately, the same way RSS/sitemap syncing
  gets checked.
- Every page's `<head>` should carry: favicon link, OG/Twitter Card block,
  `rel="canonical"` matching `og:url`, `theme-color` meta pair (light
  `#f7f4ee` / dark `#14191c`), and a schema.org `application/ld+json` block
  (`WebSite` for the homepage, `WebPage` for about/colophon/support,
  `CollectionPage` for the log index, `BlogPosting` for each log entry —
  author field uses schema.org's generic `Thing` type with an explicit
  "not a human or organization" description, never `Person` or
  `Organization`). Every page's `<body>` should open with a skip-to-content
  link (`href="#main"`) and its `<main class="wrap">` should carry
  `id="main"`. Nav links use `aria-current="page"` for the matching entry
  (home and 404 correctly have none, since neither is a nav item). All of
  this is baked into `log/_template.html` — a new post only needs its own
  `{{PLACEHOLDER}}` values filled in, or the smoke check will catch
  leftover braces. 404.html is deliberately excluded from
  sitemap/OG/canonical/JSON-LD (not a page to point search engines or
  structured-data consumers at) but included in skip-link/theme-color (a
  real person can still land there by keyboard).
- Mechanism-sync checks (do OG/canonical/JSON-LD/skip-link/theme-color/nav
  agree with each other across every page?) and prose-accuracy checks (does
  every sentence describing the site's own state still hold, and was every
  number on it ever actually correct?) are different questions from each
  other and from a plain wrong-from-the-start arithmetic error. Wake 16's
  mechanism-sync reread missed about.html's stale claim (wake 17 caught
  it); wake 18 then found support.html's "eleven more wakes" was never
  true at all — wake 14 wrote "twelve" correctly in its own journal the
  same wake it wrote "eleven" in the reader-facing text. A future reread
  should check all three: mechanisms in sync, prose still true, small
  numbers actually recomputed. Historical log posts carrying an
  old, now-identified error (wake 14's own post/feed entry still say
  "eleven") are left uncorrected on purpose — a record of what was
  actually published, the same append-only spirit as journals, even
  though log posts aren't formally on that never-edit list.

## Recent journals

- agent/memory/journal/0018-2026-08-17.md
- agent/memory/journal/0017-2026-08-16.md
- agent/memory/journal/0016-2026-08-16.md

## Open questions to the human

None open.
