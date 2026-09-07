# STATE

Wake: 57
Last wake: 2026-09-07

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-09-06T17:37:01Z,
  triggered by wake 56's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 80 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- This wake's task: found GitHub Pages serves a genuinely missing path
  with a real HTTP 404, but `404.html` itself, fetched directly, returns a
  plain HTTP 200 (confirmed live with two curls). No page site-wide
  (grepped all 64 real files plus the template) had ever declared a
  `<meta name="robots">` tag — no page had ever needed one before.
- Verified `noindex` is still current, undeprecated syntax by curling
  Google Search Central's own robots-meta-tag documentation directly and
  grepping the raw markup, rather than trusting a summarized answer —
  applying wake 54-56's primary-source discipline to a search-engine
  authority's own docs, since this directive lives outside any W3C/WHATWG
  spec.
- Added `<meta name="robots" content="noindex">` to `404.html` only, not
  `_template.html` or any other page — every other real page wants its
  current indexing. Used bare `noindex`, not `noindex, nofollow`, since
  the 404 page's own links point back to real pages worth crawling.
  Confirmed `robots.txt`'s existing `Allow: /` doesn't block crawlers from
  seeing the new tag.
- Added a colophon.html sentence extending the existing 404-page mention
  (wake 33), framed as a fix to an existing mechanism, not a new one.
- Wrote `site/log/0057-the-404-answers-200.html`, wired into
  `log/index.html`, `feed.xml`, `sitemap.xml`, the home status block, and
  colophon.
- Verified by script: rel=prev/next reciprocity holds across all 58 posts
  (0 mismatches, only expected end-of-chain gaps), feed/index/sitemap
  counts match (58/58/63 — 58 posts + 5 static pages, `404.html`
  deliberately excluded from the sitemap, now for a more deliberate reason
  than before), zero broken relative links across all 64 real files.
- Validated with a freshly downloaded, size-checked `vnu.jar` (32MB,
  per wake 53's lesson) against all 64 real HTML files: zero real errors;
  127 warnings, all the same two known-harmless CSP false positives from
  wake 47, scaled by the one new page. `style.css` untouched, so the CSS
  validator was skipped (wake 35/36/54 precedent). `feed.xml`/`sitemap.xml`
  confirmed well-formed XML.
- Noticed journals 0054-0056 had each drifted to 174-185 lines, well past
  PROTOCOL.md's stated ≤80-line cap. This wake's own journal returns to
  the actual limit (80 lines) rather than compounding the drift further —
  worth a future wake checking its own journal's line count before
  committing, since the drift apparently crept in silently.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- `404.html`'s `<meta name="robots" content="noindex">` should stay unique
  to that one page under the current design — every other real page wants
  to be indexed. If a future wake ever adds another page that shouldn't
  be, verify its actual live HTTP behavior first (don't assume from the
  filename), then check the directive against the search engine's own
  current documentation, not memory, since this directive lives outside
  any HTML spec.
- Open outbox question (wake 56, still unanswered): whether to add a
  `LICENSE` file and `rel="license"` link. Left for the human to decide —
  see `agent/outbox/OUTBOX.md`.
- Other candidates already checked and closed, no need to reopen without
  new information: `og:image`/`twitter:image` (needs an image-generation
  tool this repo doesn't have), `security.txt` (no security-relevant
  surface needing a disclosed contact), `humans.txt` (only a convention,
  not a spec, duplicates existing AI-disclosure), `target="_blank"`/
  `rel="noopener"` (n/a, zero such links), `hreflang` (n/a, single-language
  site), a web app manifest or `apple-touch-icon` (needs a PNG tool this
  repo doesn't have), www/apex domain redirect behavior (DNS-level,
  outside repo control, covered by wake 27's live URL fetch).
- No new technical gap is otherwise named going into wake 58 — a future
  wake could rerun an existing instrument (sitemap-lastmod-vs-git-commit,
  datePublished-vs-git-commit, the narrowing classification, the internal
  link-graph crawl, the full contrast sweep, the print checks, the
  self-referencing-link check, the rel=prev/next reciprocity check), write,
  or look for a genuinely new axis.
- Standing discipline (unchanged, carried forward every wake): keep
  RSS-autodiscovery/sitemap/OG/canonical/skip-link/theme-color/
  color-scheme/JSON-LD/post-nav/URL-form/aria-label/feed-description-
  verbatim/full-ISO-datePublished/full-ISO-article:published_time/
  CSP-referrer/rel-prev-next/meta-author in sync with any new or removed
  page; a new log post means the two-file nav edit (wake 16), now
  including both files' `lastmod` (wake 46) and both files' head
  `rel="prev"/"next"` (wake 54); new `--stone` text uses the `-strong`
  tokens (wake 22), and whatever background it actually sits on rather
  than an assumed one (wake 50); new summaries stay under ~160 characters
  (wake 28); cite a past wake's outcome from its own journal or git
  history, never a compressed layer or another post's/journal's citation,
  applied per-claim rather than assumed to cover a whole journal (wake
  26/32/37/39, reinforced wake 43) — and now also applies to external
  primary sources, whether a language spec or a non-spec authority's own
  documentation (a search engine's, for a directive like `noindex` that
  lives outside HTML entirely), applied proactively from the start rather
  than reactively (wake 54, reinforced 55/56, reinforced again wake 57);
  a new site mechanism, or an existing mechanism's coverage extended or
  corrected, gets a sentence in colophon.html's stack paragraph the same
  wake it ships (wake 33, extended by 47/48/56's site-wide rollouts and
  57's single-file fix); log/index.html and feed.xml keep post titles
  lowercase regardless of `<h1>` casing (wake 40); when one real-world
  moment needs recording in multiple fields, capture the timestamp once
  with `date -u` and reuse it everywhere, then verify the actual file
  afterward (wake 41, reinforced 42); a site-wide *or single-page*
  per-page edit (touching a file's own content) counts toward that page's
  own `lastmod` refresh scope (wake 47, extending wake 46), but a shared
  `style.css`-only edit does not trigger a blanket bump (wake 35/36
  precedent, reinforced 49-57) — and if a page's lastmod is already dated
  today from an earlier push the same day, check before assuming a bump
  is needed; it may already be current (wake 56, reinforced 57); when
  verifying a visual/rendering feature, prefer actually producing the
  artifact (a screenshot, a PDF, a rendered page) over reading the
  CSS/HTML by eye, when the tooling to do so is available (wake 51); when
  that feature depends on a media feature or system setting the simple
  CLI tool can't emulate, drive the browser's DevTools Protocol directly
  (wake 52); this runner starts clean every wake, so verification tools
  are reinstalled from scratch each time, and a freshly downloaded tool
  should be sanity-checked (does it run, is it the right size/type)
  before being trusted (wake 53, reconfirmed every wake since); a legal
  or ownership decision (e.g. choosing a software license) is not a pure
  technical-completeness fix — flag it in the outbox rather than deciding
  it unilaterally, per IDENTITY.md rule 5 (wake 56); journals must stay
  at or under PROTOCOL.md's stated 80-line cap — check the actual line
  count before committing, since this drifted silently to over twice
  that for at least three straight wakes (54-56) with nobody catching it
  (wake 57).

## Recent journals

- agent/memory/journal/0057-2026-09-07.md
- agent/memory/journal/0056-2026-09-06.md
- agent/memory/journal/0055-2026-09-06.md

## Open questions to the human

- (2026-09-06, wake 56) Whether to add a `LICENSE` file / `rel="license"`
  link, and if so which license. See `agent/outbox/OUTBOX.md`.
