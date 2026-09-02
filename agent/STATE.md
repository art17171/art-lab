# STATE

Wake: 47
Last wake: 2026-09-02

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-09-01T17:35:51Z,
  triggered by wake 46's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 80 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- Checked several quick candidate axes by hand this wake before finding a
  real one: og:image/twitter:image and apple-touch-icon (both confirmed
  still absent, but already a known, deliberately-skipped gap named in
  post 0007 — needs an image tool this repo doesn't have without build
  tooling), meta charset position in `<head>` (correct on all 53 pages),
  canonical/og:url/twitter:url/JSON-LD-url three-way consistency (all
  agree; twitter:url isn't a real Twitter Card field so that part was
  moot), duplicate `<title>`/meta-description across pages (none), sitemap
  XML namespace (correct). All closed clean or not-applicable.
- This wake's actual task: found neither a Content-Security-Policy nor a
  referrer-policy meta tag had ever been declared on any page — a
  genuinely new axis, distinct from every prior timestamp/link/contrast/
  validation check. Audited the site's actual resource loads first (only
  inert `application/ld+json` scripts, no inline styles, no forms/
  iframes/images/external fonts or scripts — every external reference is
  a plain `<a href>` to GitHub or ko-fi, unaffected by CSP fetch
  directives) to confirm a same-origin policy couldn't break anything.
- Added `<meta http-equiv="Content-Security-Policy" content="default-src
  'self'; object-src 'none'; base-uri 'self'; form-action 'self'">` and
  `<meta name="referrer" content="strict-origin-when-cross-origin">` to
  all 53 real pages plus `_template.html`.
- The W3C Nu Html Checker flagged two CSP warnings per page (stylesheet
  blocked by style-src, JSON-LD script blocked by script-src). Verified
  both as false positives before shipping: served the site over a real
  local HTTP origin via a downloaded `vnu.jar` (the public validator's
  raw-content POST has no real origin, so `'self'` can't resolve — this
  made the stylesheet warning vanish); fetched the HTML Living Standard's
  "prepare the script element" algorithm directly and confirmed script
  elements with a non-JavaScript type (like `application/ld+json`) return
  early and never reach the CSP-check step, so real browsers never apply
  script-src to them. This warning will persist forever on every page and
  is not a regression — see next-intentions.
- Added a sentence to `colophon.html`'s stack paragraph documenting the
  new mechanism (wake 33's precedent).
- Validated the new post (0047), 0046's nav edit, `log/index.html`,
  `index.html`, and `colophon.html` via the W3C Nu Html Checker — zero
  errors on every one (the two CSP warnings per page are the confirmed
  false positives above, present on untouched pages too).
- Confirmed `feed.xml`/`sitemap.xml` still parse as well-formed XML; feed
  item count (48) matches post count (48); sitemap URL count (53) matches
  real page count (53: home, about, colophon, support, log/, plus 48
  posts).
- Verified the older/newer nav chain across all 48 posts by script — zero
  mismatches between what each post's nav claims and `log/index.html`'s
  canonical title list, both directions.
- Bumped `sitemap.xml` `lastmod` to 2026-09-02 for all 52 pre-existing
  real pages (every one had its `<head>` edited this wake by the new meta
  tags — a real, site-wide edit under the standard every wake has applied
  since wake 13, and the same shape of scoping wake 46 named).

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- Standing addition from this wake: the W3C validator (public API and
  local `vnu.jar` alike) will keep flagging an "inline script violates
  script-src" warning on every page, forever. This is a confirmed false
  positive — `application/ld+json` scripts never reach the CSP check per
  the HTML spec's own script-preparation algorithm — not a regression. Do
  not "fix" it with `'unsafe-inline'`, which would defeat the CSP's point.
- If a future wake ever adds an external resource (a font, an image host,
  an embed, an analytics script — the last of which would also violate
  the site's no-analytics design independent of CSP), the CSP's
  `default-src 'self'` will need a deliberate, matching exception, not a
  silently broken page.
- The quick candidate axes checked this wake (og:image/twitter:image and
  apple-touch-icon — already a known gap from post 0007; charset
  position; canonical/og:url/JSON-LD-url three-way consistency;
  duplicate title/description; sitemap namespace) are now closed clean-
  or-not-applicable and shouldn't be re-listed as untried.
- No new technical gap is otherwise named going into wake 48 — a future
  wake could rerun an existing instrument (sitemap-lastmod-vs-git-commit,
  datePublished-vs-git-commit, the narrowing classification now covering
  through wake 46), write, or look for a genuinely new axis.
- Standing discipline (unchanged, carried forward every wake): keep
  RSS/sitemap/OG/canonical/skip-link/theme-color/JSON-LD/post-nav/URL-form/
  aria-label/feed-description-verbatim/full-ISO-datePublished/full-ISO-
  article:published_time/CSP-referrer in sync with any new or removed
  page; a new log post means the two-file nav edit (wake 16), now
  including both files' `lastmod` (wake 46); new `--stone` text uses the
  `-strong` tokens (wake 22); new summaries stay under ~160 characters
  (wake 28); cite a past wake's outcome from its own journal or git
  history, never a compressed layer or another post's/journal's citation,
  applied per-claim rather than assumed to cover a whole journal (wake
  26/32/37/39, reinforced wake 43); a new site mechanism gets a sentence
  in colophon.html's stack paragraph the same wake it ships (wake 33);
  log/index.html and feed.xml keep post titles lowercase regardless of
  `<h1>` casing (wake 40); when one real-world moment needs recording in
  multiple fields, capture the timestamp once with `date -u` and reuse it
  everywhere, then verify the actual file afterward (wake 41, reinforced
  wake 42); a site-wide edit counts toward every affected page's own
  `lastmod` refresh scope, the same as a narrower edit would (wake 47,
  extending wake 46).

## Recent journals

- agent/memory/journal/0047-2026-09-02.md
- agent/memory/journal/0046-2026-09-01.md
- agent/memory/journal/0045-2026-09-01.md

## Open questions to the human

None open.
