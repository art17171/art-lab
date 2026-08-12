# STATE

Wake: 8
Last wake: 2026-08-12

## Site health

- Deploy: live and healthy. Last checked wake 8 via the public Actions API —
  latest completed `deploy-pages` run: success (from wake 7's push, on
  2026-08-12). No new deploy triggered by wake 8 yet at the time this file
  was written; this wake's own push will trigger the next one.
- Domain: demo-slayer.com — DNS setup pending on the human's side (see
  SETUP.md), site currently served via GitHub Pages.
- The wake-4 anomaly (a `slade-wake` run on 2026-08-10T10:02:51Z that failed
  with no trace) remains resolved as "noted, not investigable further" — see
  DECISIONS.md 0004 and OUTBOX.md. No further anomalies confirmed as of
  wake 8 — every run since wake 4 has completed successfully.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

1. **Reader tips (0001-A) — approved, link missing.**
   Done when: the human pastes a public tipping-platform URL into
   `INBOX.md` (suggested format `LINK: 0001-A <url>`), and a wake replaces
   the explanatory paragraph in `site/support.html` with the real link.
   Status: unchanged since wake 2. `site/support.html` is live, linked from
   every page's nav. Request for the URL is in `agent/outbox/OUTBOX.md`.
   Checked the inbox this wake — still nothing. Keep checking every wake;
   don't re-ask in the outbox until something changes.

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
  block (title/description copied verbatim from the page's own meta
  description, url matching sitemap.xml, type website/article), and for log
  posts an `article:published_time`. All of this is now baked into
  `log/_template.html`, including a `{{SLUG}}` placeholder for the post's
  own filename — fill it in alongside `{{TITLE}}` etc., or the smoke check
  will catch the leftover braces. This should stay true automatically for
  new log posts; only a concern if a wake ever adds a page outside the
  template pattern.
- If the inbox is empty and no commitment is actionable, and no next-
  intention above is unblocked, pick free exploration consistent with
  IDENTITY.md rather than inventing scope for its own sake. Wakes 5-8 did
  this (404.html, robots.txt/sitemap.xml, favicon.svg, OG/Twitter tags) —
  all four were "missing web-standard plumbing." Before reaching for a
  fifth one of these, actually check whether another genuine gap of this
  shape exists, rather than assuming it does.

## Recent journals

- agent/memory/journal/0008-2026-08-12.md
- agent/memory/journal/0007-2026-08-12.md
- agent/memory/journal/0006-2026-08-11.md

## Open questions to the human

- Needed: the tip-platform URL for option 0001-A. See
  `agent/outbox/OUTBOX.md` for the exact ask.
- FYI only, not blocking: a wake run failed silently on 2026-08-10 (see
  OUTBOX.md for the run id) — worth a look only if you have Actions log
  access and are curious. No further anomalies since, confirmed through
  wake 8.
