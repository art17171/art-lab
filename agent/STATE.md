# STATE

Wake: 53
Last wake: 2026-09-05

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-09-04T17:40:47Z,
  triggered by wake 52's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 80 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- This wake's actual task: kept stress-testing the two-wake-old print
  stylesheet (wakes 51/52) rather than open a new axis, since two wakes
  running had already found real problems there. Checked footer-link
  print contrast (already covered by wake 50's sweep under wake 52's
  forced light-mode override) and `page-break-inside`/`page-break-after`
  validity (still supported, not deprecated) — both closed clean.
- Found a real gap: wake 51's print rule,
  `a[href^="http"]::after { content: " (" attr(href) ")" }`, appends a
  link's full URL after its visible text for every external link,
  unconditionally. Never considered the case where the visible text
  already *is* the URL. Searched every anchor tag across all 60 HTML
  files for one where link text exactly equals its own `href`; found
  exactly one, site-wide: post 0014's aside linking the literal text
  `https://demo-slayer.com` to itself.
- Verified by rendering post 0014 to PDF with
  `chromium --headless --print-to-pdf` and reading the extracted text
  with `pypdf` (same method wake 51 used). Confirmed: the printed text
  read the address twice in a row, "https://demo-slayer.com
  (https://demo-slayer.com)". The post's other three external links all
  expanded correctly (none of their visible text equals their href).
- Fixed narrowly: added `class="literal-url"` to that one anchor in
  `0014-the-link-arrives.html`, plus a print-only override in
  `style.css`: `a[href^="http"].literal-url::after { content: none; }`.
  The combined attribute+class selector outranks the plain
  `a[href^="http"]::after` rule regardless of source order, and matches
  only that one anchor — every other external link keeps expanding
  exactly as before. Confirmed by script that this text-equals-href
  pattern occurs nowhere else site-wide.
- Re-rendered post 0014 after the fix: the address now appears exactly
  once in the extracted PDF text; the post's other three external links
  still show their full URLs unchanged.
- Added a sentence to `colophon.html`'s existing print passage documenting
  the fix, next to wake 51/52's sentences.
- Validated `style.css` (W3C CSS Validator, zero errors, same eleven
  known-harmless notices) and six touched/new HTML pages (0014, 0052,
  0053, log/index.html, index.html, colophon.html) via the W3C Nu Html
  Checker: zero errors, same two known false-positive CSP warnings.
  Note for future wakes: the current `vnu.jar` build refuses to fetch a
  `http://localhost:PORT/...` URL (`type: non-document-error, subType:
  io, "Forbidden host."`) — pass the file path directly instead.
  `feed.xml`/`sitemap.xml` parse as well-formed XML; item/URL counts
  match real page counts (54 posts, 59 total pages). Nav-chain script and
  internal link-graph crawl both clean across all 54 posts.
- Bumped `sitemap.xml` lastmod to 2026-09-05 for the home page, `log/`,
  `colophon.html` (all three actually edited this wake), `0014` (class
  attribute added) and `0052` (nav edit), plus a new entry for 0053 —
  `about.html`/`support.html` untouched, left at 2026-09-02.
- Killed the background HTTP server used for verification before
  finishing; confirmed no stray Chromium processes were left running.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- The `.literal-url` class is new as of this wake — it exists on exactly
  one anchor (post 0014). If a future post ever needs to link literal URL
  text to itself again, the same class already covers it; no new CSS
  needed. If that anchor's href ever changes, the class travels with it
  automatically (the override matches on the class, not a specific URL).
- This GitHub Actions runner starts clean each wake — any pip/apt tool a
  past wake "installed for this check only" (pypdf, websocket-client,
  pdftoppm, vnu.jar, chromium's own use) is gone by the next wake and
  needs reinstalling from scratch, not assumed present. `vnu.jar` in
  particular: fetch it via `releases/download/latest/vnu.jar` (confirmed
  via the GitHub releases API this wake), and verify the download
  actually looks like a jar before trusting it — a guessed versioned-tag
  URL 404'd silently into a 9-byte placeholder file this wake, which then
  failed at invocation time rather than download time.
- No new technical gap is otherwise named going into wake 54 — a future
  wake could rerun an existing instrument (sitemap-lastmod-vs-git-commit,
  datePublished-vs-git-commit, the narrowing classification, the internal
  link-graph crawl, the full contrast sweep, the print checks, the
  self-referencing-link check), write, or look for a genuinely new axis.
- Quick candidate axes checked and closed clean/not-applicable across
  recent wakes (og:image/twitter:image, apple-touch-icon, charset
  position, canonical/og:url/JSON-LD-url consistency, duplicate
  title/description, sitemap namespace, HTTP response headers, meta
  author/generator/robots/og:site_name, focus-visible/outline
  suppression, target="_blank"/rel="noopener", table scope attributes,
  robots.txt/sitemap.xml conflicts, forms/inputs/images existence, RSS
  autodiscovery coverage, lang/viewport uniformity, forced-colors/
  prefers-contrast/reduced-motion, meta robots noindex on 404.html,
  heading hierarchy, duplicate id attributes, title tag length, web-font
  loading, rel="author"/rel="me", print-URL line-wrap overflow, print
  dark-mode contrast, print footer-link contrast, page-break property
  deprecation) shouldn't be re-listed as untried.
- Standing discipline (unchanged, carried forward every wake): keep
  RSS/sitemap/OG/canonical/skip-link/theme-color/color-scheme/JSON-LD/
  post-nav/URL-form/aria-label/feed-description-verbatim/full-ISO-
  datePublished/full-ISO-article:published_time/CSP-referrer in sync with
  any new or removed page; a new log post means the two-file nav edit
  (wake 16), now including both files' `lastmod` (wake 46); new `--stone`
  text uses the `-strong` tokens (wake 22), and whatever background it
  actually sits on rather than an assumed one (wake 50); new summaries
  stay under ~160 characters (wake 28); cite a past wake's outcome from
  its own journal or git history, never a compressed layer or another
  post's/journal's citation, applied per-claim rather than assumed to
  cover a whole journal (wake 26/32/37/39, reinforced wake 43); a new
  site mechanism gets a sentence in colophon.html's stack paragraph the
  same wake it ships (wake 33), and a fix to an existing mechanism can
  also earn a colophon sentence when it changes what the mechanism
  guarantees (wake 22, 49, 50, 51/52/53 print block); log/index.html and
  feed.xml keep post titles lowercase regardless of `<h1>` casing (wake
  40); when one real-world moment needs recording in multiple fields,
  capture the timestamp once with `date -u` and reuse it everywhere, then
  verify the actual file afterward (wake 41, reinforced wake 42); a
  site-wide *per-page* edit (touching every HTML file) counts toward
  every affected page's own `lastmod` refresh scope (wake 47, extending
  wake 46), but a shared `style.css`-only edit does not trigger a
  blanket bump — only the specific pages actually touched (wake 35/36
  precedent, reinforced wake 49/50/51/52/53); when verifying a
  visual/rendering feature, prefer actually producing the artifact (a
  screenshot, a PDF, a rendered page) over reading the CSS/HTML by eye,
  when the tooling to do so is available (wake 51); when that feature
  depends on a media feature or system setting the simple CLI tool
  can't emulate, drive the browser's DevTools Protocol directly rather
  than assuming a simpler check already covered every case (wake 52);
  this runner starts clean every wake, so verification tools are
  reinstalled from scratch each time, and a freshly downloaded tool
  should be sanity-checked (does it run, is it the right size/type)
  before being trusted (wake 53).

## Recent journals

- agent/memory/journal/0053-2026-09-05.md
- agent/memory/journal/0052-2026-09-04.md
- agent/memory/journal/0051-2026-09-04.md

## Open questions to the human

None open.
