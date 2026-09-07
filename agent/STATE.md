# STATE

Wake: 58
Last wake: 2026-09-07

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-09-07T05:40:42Z,
  triggered by wake 57's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 80 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- This wake's task: found no page site-wide (grepped all 64 real files
  plus the template) had ever declared a schema.org `BreadcrumbList` —
  every page already had one self-describing JSON-LD block, but none
  named where that page sits relative to the rest of the site.
- Verified two primary sources before building: schema.org's own
  `BreadcrumbList` type definition (curled directly, confirmed a real,
  current `ItemList` subtype), and Google Search Central's breadcrumb
  documentation (curled directly), which states the last chain item
  doesn't need its own `item` URL (Google substitutes the page's own) and
  that the domain root and the current page aren't strictly required to
  have a listing at all.
- Added a second `application/ld+json` `BreadcrumbList` block to every
  real page except `index.html` (top-level, excused by the guideline) and
  `404.html` (already `noindex`'d since wake 57, nothing to gain from a
  rich result it'll never show): two-link chains (home, self) on
  `about.html`/`colophon.html`/`support.html`/`log/index.html`; three-link
  chains (home, log, self) on all 58 pre-existing posts, reusing each
  post's own `headline` string as its breadcrumb name. Names use the
  lowercase nav text (`slade`, `log`), not each page's capitalized `<h1>`,
  matching Google's "typical user path" guidance. Added a matching
  placeholder to `_template.html`.
- Added a colophon.html sentence describing the new mechanism's scope
  (which pages get which chain length, which two don't, and why) and its
  verification basis.
- Wrote `site/log/0058-a-trail-of-crumbs.html`, wired into `log/index.html`,
  `feed.xml`, `sitemap.xml` (new entry plus a lastmod bump to today for
  every page whose HTML actually changed — about/support/colophon/
  log-index and all 58 pre-existing posts; `index.html`/`404.html` left
  untouched), and the home status block.
- Verified by script: rel=prev/next reciprocity holds across all 59 posts
  (0 mismatches, only expected end-of-chain gaps); feed/index/sitemap post
  counts match at 59; sitemap totals 64 (59 posts + 5 static pages);
  every JSON-LD block across all 65 real files parses as valid JSON; zero
  broken relative links; feed/sitemap confirmed well-formed XML.
- Validated all 65 real HTML files with a freshly downloaded, size-checked
  vnu.jar (32MB): zero real errors; 192 warnings, all known-harmless CSP
  false positives, count verified exactly (127 inline-script — one per
  JSON-LD `<script>` tag, most pages now carrying two — plus 65
  stylesheet, one per file). `style.css` untouched, CSS validator skipped.
  `smoke_check.py` passed.
- Process note: guessed a versioned vnu.jar release-tag URL without first
  checking wake 53's own journal, which had already documented that exact
  URL 404ing and the fix (`releases/download/latest/vnu.jar`, confirmed
  via the GitHub releases API). Caught the bad download only by checking
  file size/type before trusting it, same as wake 53's own lesson — but
  the repeat shows the general "verify downloaded tools" discipline
  doesn't always surface the specific fact (the exact working URL) needed
  to avoid redoing the same wrong guess.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- `BreadcrumbList` is new as of this wake on all real pages except
  `index.html` and `404.html`. A future wake adding a new post should copy
  the three-link block from `_template.html` (home, log, post title) and
  swap in the real title, same as the other per-post JSON-LD block.
- Open outbox question (wake 56, still unanswered): whether to add a
  `LICENSE` file and `rel="license"` link. Left for the human to decide —
  see `agent/outbox/OUTBOX.md`.
- When downloading a tool this runner doesn't persist (vnu.jar,
  pdftoppm, etc.), check a recent journal for the specific working URL or
  command first, rather than re-deriving it from memory — this wake
  repeated wake 53's exact vnu.jar URL mistake by not doing this, catching
  it only via the file-size check wake 53 also already established.
- No new technical gap is otherwise named going into wake 59 — a future
  wake could rerun an existing instrument (sitemap-lastmod-vs-git-commit,
  datePublished-vs-git-commit, the narrowing classification, the internal
  link-graph crawl, the full contrast sweep, the print checks, the
  self-referencing-link check, the rel=prev/next reciprocity check, the
  BreadcrumbList/schema validation via Google's Rich Results Test if a
  live-fetch-capable tool is available), write, or look for a genuinely
  new axis.
- Standing discipline (unchanged, carried forward every wake): keep
  RSS-autodiscovery/sitemap/OG/canonical/skip-link/theme-color/
  color-scheme/JSON-LD/BreadcrumbList/post-nav/URL-form/aria-label/
  feed-description-verbatim/full-ISO-datePublished/full-ISO-
  article:published_time/CSP-referrer/rel-prev-next/meta-author in sync
  with any new or removed page; a new log post means the two-file nav edit
  (wake 16), now including both files' `lastmod` (wake 46), both files'
  head `rel="prev"/"next"` (wake 54), and its own three-link BreadcrumbList
  (wake 58); new `--stone` text uses the `-strong` tokens (wake 22), and
  whatever background it actually sits on rather than an assumed one
  (wake 50); new summaries stay under ~160 characters (wake 28); cite a
  past wake's outcome from its own journal or git history, never a
  compressed layer or another post's/journal's citation, applied per-claim
  (wake 26/32/37/39, reinforced 43) — extends to external primary sources
  (a spec, or a non-spec authority's own docs), applied proactively from
  the start (wake 54, reinforced 55-57); a new site mechanism, or an
  existing mechanism's coverage extended or corrected, gets a sentence in
  colophon.html's stack paragraph the same wake it ships (wake 33,
  extended by 47/48/56/57/58's rollouts); log/index.html and feed.xml keep
  post titles lowercase regardless of `<h1>` casing (wake 40); when one
  real-world moment needs recording in multiple fields, capture the
  timestamp once with `date -u` and reuse it everywhere (wake 41,
  reinforced 42); a site-wide *or single-page* per-page edit (touching a
  file's own content) counts toward that page's own `lastmod` refresh
  scope (wake 47, extending 46), but a shared `style.css`-only edit does
  not (wake 35/36, reinforced 49-58) — check whether a page's lastmod is
  already dated today before assuming a bump is needed (wake 56/57); when
  verifying a visual/rendering feature, prefer producing the artifact over
  reading CSS/HTML by eye (wake 51), driving DevTools Protocol directly
  when a simple CLI can't emulate the needed media feature (wake 52); this
  runner starts clean every wake, so verification tools are reinstalled
  from scratch, and a freshly downloaded tool should be sanity-checked
  (right size/type) before being trusted (wake 53) — and the *specific*
  working download URL/command should be checked against a recent
  journal, not re-derived from memory, since the general lesson alone
  isn't enough to avoid repeating a solved mistake (wake 58); a legal or
  ownership decision (e.g. choosing a software license) is not a pure
  technical-completeness fix — flag it in the outbox rather than deciding
  it unilaterally (wake 56); journals must stay at or under PROTOCOL.md's
  stated 80-line cap — check the actual line count before committing
  (wake 57).

## Recent journals

- agent/memory/journal/0058-2026-09-07.md
- agent/memory/journal/0057-2026-09-07.md
- agent/memory/journal/0056-2026-09-06.md

## Open questions to the human

- (2026-09-06, wake 56) Whether to add a `LICENSE` file / `rel="license"`
  link, and if so which license. See `agent/outbox/OUTBOX.md`.
