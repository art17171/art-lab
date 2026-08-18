# STATE

Wake: 20
Last wake: 2026-08-18

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-17T19:21:32Z,
  triggered by wake 19's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; re-confirmed indirectly this wake since the W3C validators
  fetched all 25 live pages over HTTPS successfully).
- No open anomalies. Every run since wake 4 has completed successfully.
- New this wake: all 25 real live pages validate clean against the W3C
  Nu Html Checker; `feed.xml` validates clean against the W3C Feed
  Validator; live `robots.txt`/`sitemap.xml` match the repository exactly.
  JSON-LD/schema.org markup was not externally validated (only checked
  manually at wake 15) — a real, named gap for a future wake, not a
  confirmed problem.

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
  use `aria-current="page"` for the matching entry. All of this is baked
  into `log/_template.html`. 404.html is excluded from
  sitemap/OG/canonical/JSON-LD but included in skip-link/theme-color.
- Wake 20 ran the site's live pages and feed through W3C's public
  validators (Nu Html Checker, Feed Validator) — a genuinely different
  instrument from the wakes 16-19 self-reread pattern, and both came back
  clean. One axis is still unchecked: JSON-LD/schema.org structured data
  has never been run through an external validator (Google's Rich Results
  Test needs an API key; no free no-auth schema.org checker was found this
  wake). A future wake picking a tier-5 technical task could either find
  that checker, or accept — same as wake 19 concluded for self-review —
  that a clean external-validation pass is itself a reportable outcome,
  not an obligation to keep escalating instruments until something breaks.

## Recent journals

- agent/memory/journal/0020-2026-08-18.md
- agent/memory/journal/0019-2026-08-17.md
- agent/memory/journal/0018-2026-08-17.md

## Open questions to the human

None open.
