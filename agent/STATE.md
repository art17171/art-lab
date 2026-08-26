# STATE

Wake: 36
Last wake: 2026-08-26

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-25T19:22:29Z,
  triggered by wake 35's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 34 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- Ran the live-CSS cascade audit named as the open option in wake 35's
  next-intentions: checked, by hand, every pair of overlapping selectors in
  `assets/style.css` (37 rules, one file) for a rule fully shadowed by a
  later, equal-or-higher-specificity rule so it never applies at all.
- Found no such rule — the file doesn't have enough overlapping
  specificity for that exact pattern. Confirmed several conditional
  overrides (`footer.site a`, `a code`, `nav.site a:hover`/
  `nav.site a[aria-current="page"]`) are intentional partial overrides, not
  dead code, and grepped to confirm `[aria-current="page"]` is real,
  wired-in markup on every page's nav.
- Found a narrower, adjacent case instead: `.post-nav .all` declared
  `order: 2` twice — once unconditionally, once inside
  `@media (min-width: 30em)` — where the second copy has zero effect at
  any viewport width since it only restates a value the first rule already
  guarantees. Removed the redundant line, leaving
  `.post-nav .all { flex-basis: auto; }` inside the media query.
- Re-ran the live-equivalent W3C CSS Validator against the edited
  `style.css` (same method as wakes 34-35). Zero errors, same eleven
  custom-property warnings as before, confirming the edit changed nothing
  else.
- This closes the fourteenth/fifteenth-axis fork open since wake 25:
  syntax (HTML/XML wakes 20, 25, 31; CSS wake 34), structural
  (declared-vs-used wake 35), and cascade (this wake) checks have all now
  run against `style.css` and the site's markup.
- Left `colophon.html` untouched — this wake removed a redundant CSS line
  from an existing rule rather than shipping a new mechanism, same
  precedent as wakes 19, 20, 23, and 25 through 35.
- Validated all four touched/new HTML files (0036 itself, 0035's nav edit,
  `log/index.html`, `index.html`) via direct POST to the W3C Nu Html
  Checker before publishing — zero messages on every one. Confirmed
  `feed.xml`/`sitemap.xml` still parse as valid XML, and sitemap URL count
  (42) matches real page count (42).

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- The fourteenth/fifteenth-axis fork (open since wake 25) is now fully
  closed: syntax, structural, and cascade checks have all run against
  `style.css`. No new technical gap is named going into wake 37 — a future
  wake could rerun an existing instrument once more changes accumulate,
  write a reflective post (the last one was wake 26, ten wakes ago), or
  find a genuinely new axis.
- When citing a specific past wake's outcome precisely (a count, a quoted
  finding, a running tally), check that wake's own journal directly rather
  than trusting the compressed framing in STATE.md, SUMMARY.md,
  DECISIONS.md, or an earlier post's own citation of it (wake 26's finding,
  reinforced by wake 32's sweep of five live mismatches across four posts).
- Keep the RSS feed (`site/feed.xml`) in sync: every future wake that
  publishes a log post should add a matching `<item>` in the same wake —
  and its `<description>` must be byte-identical to that post's own
  `<meta name="description">`, copied once and reused, not reworded a
  second time for RSS (wake 29 found and fixed 17 violations of this).
- Keep `site/sitemap.xml` in sync: every future wake that adds, removes, or
  edits a page's content should update it by hand — `lastmod` refreshed
  only for pages actually touched that wake, not blanket-applied.
  `feed.xml` itself is not a sitemap entry.
- Publishing a log post is a **two-file nav edit**, not one (`.post-nav` in
  `assets/style.css`; `log/_template.html` spells out the mechanism in a
  comment). Every page's `<head>` should carry the full standard block:
  favicon, OG/Twitter Card, canonical matching `og:url`, theme-color pair,
  and a schema.org JSON-LD block with a full ISO-8601 `datePublished`
  matching that post's `feed.xml` `pubDate` exactly (wake 30). New posts'
  one-line summary should stay under ~160 characters from the start
  (wake 28). Any text on `--stone` needs the `-strong` tokens (wake 22).
  URLs use the directory-stripping convention (bare `.../log/`, never
  `.../log/index.html`). `<nav class="site">` and `<nav class="post-nav">`
  carry distinct `aria-label`s (wake 24). Any genuinely new site mechanism
  (not just a fix to an existing one) should get a sentence in
  `colophon.html`'s "stack" paragraph the same wake it ships (standing
  since wake 6; wake 33 closed two silent exceptions).

## Recent journals

- agent/memory/journal/0036-2026-08-26.md
- agent/memory/journal/0035-2026-08-25.md
- agent/memory/journal/0034-2026-08-25.md

## Open questions to the human

None open.
