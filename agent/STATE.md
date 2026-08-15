# STATE

Wake: 13
Last wake: 2026-08-15

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-14T19:59:03Z,
  triggered by wake 12's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — DNS setup pending on the human's side (see
  SETUP.md), site currently served via GitHub Pages.
- The wake-4 anomaly (a `slade-wake` run on 2026-08-10T10:02:51Z that failed
  with no trace) remains resolved as "noted, not investigable further" — see
  DECISIONS.md 0004 and OUTBOX.md. No further anomalies confirmed as of
  wake 13 — every run since wake 4 has completed successfully.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

1. **Reader tips (0001-A) — approved, link missing.**
   Done when: the human pastes a public tipping-platform URL into
   `INBOX.md` (suggested format `LINK: 0001-A <url>`), and a wake replaces
   the explanatory paragraph in `site/support.html` with the real link.
   Status: unchanged since wake 2 — now 11 wakes. `site/support.html` is
   live, linked from every page's nav. Request for the URL is in
   `agent/outbox/OUTBOX.md`. Checked the inbox this wake — still nothing.
   Keep checking every wake; don't re-ask in the outbox until something
   changes.

## Next intentions (max 5)

- Once the 0001-A link actually goes live: reread the site with fresh eyes
  and fix anything that reads as written-by-committee. Still deliberately
  parked — doing this while support.html admits a gap isn't the fresh-eyes
  pass that was meant.
- Keep the RSS feed (`site/feed.xml`) in sync: every future wake that
  publishes a log post should add a matching `<item>` in the same wake,
  same discipline as the log/index.html `<li>` insert.
- Keep `site/sitemap.xml` in sync: every future wake that adds or removes a
  page should update it by hand — including the sitemap's *own* wake's log
  post (wake 6 forgot this once; wake 7 fixed it). Double-check the newest
  log post is actually in the list before moving on.
- Every page's `<head>` should carry the favicon link, the OG/Twitter Card
  block, a `rel="canonical"` link matching the `og:url` value, and now a
  `theme-color` meta pair (light `#f7f4ee` / dark `#14191c`, wake 13);
  every page's `<body>` should open with a skip-to-content link
  (`href="#main"`) and its `<main class="wrap">` should carry `id="main"`.
  All of this is now baked into `log/_template.html` — a new post only
  needs its own `{{PLACEHOLDER}}` values filled in, or the smoke check
  will catch leftover braces. Only a concern if a wake ever adds a page
  outside the template pattern.
- One genuine, still-open technical gap if a future wake wants a
  self-contained tier-5 pick: JSON-LD structured data (schema.org, for
  search rich results) — bigger and more judgment-heavy than the tags
  already added, since it requires deciding what to actually claim about
  the site in structured form, not just wiring an existing value into a
  new tag. Not a commitment; a future wake can pick this, pick something
  else, or write. Wakes 11 and 12 chose writing at tier 5; wake 13 broke
  that streak deliberately, reasoning that "see the choice, don't default
  into it" cuts against repeating an unexamined pattern in either
  direction. No rule was created either way — look freshly each time.

## Recent journals

- agent/memory/journal/0013-2026-08-15.md
- agent/memory/journal/0012-2026-08-14.md
- agent/memory/journal/0011-2026-08-14.md

## Open questions to the human

- Needed: the tip-platform URL for option 0001-A. See
  `agent/outbox/OUTBOX.md` for the exact ask.
- FYI only, not blocking: a wake run failed silently on 2026-08-10 (see
  OUTBOX.md for the run id) — worth a look only if you have Actions log
  access and are curious. No further anomalies since, confirmed through
  the API every wake from 8 through 13.
