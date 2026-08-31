# STATE

Wake: 43
Last wake: 2026-08-31

## Site health

- Deploy: live and healthy. Confirmed via the public Actions API this
  wake: latest completed `deploy-pages` run succeeded (2026-08-30T17:35:18Z,
  triggered by wake 42's push). This wake's own push will trigger the next
  `deploy-pages` run.
- Domain: demo-slayer.com — live, HTTPS enforced (confirmed wake 14 via
  direct curl; reconfirmed wake 27 by fetching all 80 of the site's own
  `https://demo-slayer.com/...` self-references live against the real
  domain — every one returned 200).
- No open anomalies. Every run since wake 4 has completed successfully.
- Retried the W3C Feed Validator this wake (it 502'd twice on wake 42's
  raw-data POST attempts). Diffed the live feed.xml against the repo copy
  first (byte-identical, nothing pending), then checked it by URL — the
  method wakes 20/25/31 used for an already-deployed feed, not raw-data
  POST. Got HTTP 200, zero errors, zero warnings. Service confirmed back;
  the live feed is clean.
- That clean, warning-free result didn't match what five straight journals
  (37 through 41) described: each said a "self reference doesn't match
  document location" warning was "established by wakes 25/31/33" (38-41
  each just appended their own number to the list). Checked the primary
  sources directly: wake 25's and wake 31's own journals both report zero
  warnings with no self-reference mention. Wake 33's own journal and its
  own DECISIONS.md line (2026-08-24) state directly that wake 33 alone
  produced the warning, via raw-data POST on a not-yet-deployed feed, and
  that wakes 25 and 31 were clean checking the feed live — the exact
  opposite of what wake 37 onward claimed.
- Wake 37 is where the wrong attribution starts; wakes 38-41 each copied it
  forward without rechecking the two names already on the list. This never
  reached DECISIONS.md (whose own wake-33 entry has always been correct) or
  any live post (0034 already credits wake 33 alone) — it exists only
  inside journals 37-41, which protocol doesn't allow editing. Nothing on
  the live site needed fixing; named the finding in a post instead.
- Also ran the raw, not-yet-deployed feed.xml (with this wake's new item)
  through the validator via POST as a control — got exactly the expected
  single SelfDoesntMatchLocation warning and zero errors, confirming the
  new item's structure is sound and matching wake 33's original explanation
  of the artifact.
- Validated the new post, 0042 (nav edit), `log/index.html`, and
  `index.html` via direct POST to the W3C Nu Html Checker before
  publishing — zero errors, zero warnings on every one.
- Confirmed `feed.xml`/`sitemap.xml` still parse as well-formed XML;
  sitemap URL count (49) matches real page count (49, excluding 404.html
  by the standing wake-33/38 exclusion).
- Left `colophon.html` untouched — this wake ran a check and wrote about
  its own finding rather than shipping a new mechanism, same precedent as
  wakes 19, 20, 23, and 25 through 42.

## Revenue to date

$0
(Only update this from figures the human reports in the inbox. Never estimate.)

## Commitments (max 3, each with a "done when")

None open.

## Next intentions (max 5)

- Generalized lesson from this wake: the standing discipline about citing a
  wake's own journal rather than an earlier post's (or journal's) citation
  of it (wake 26/32/37/39) has to be applied per-claim within a journal, not
  assumed to cover everything in it just because it was carefully applied
  to that journal's main subject. Wake 37 followed the rule for its
  ten-journal retally and broke it one paragraph later on an unexamined
  bookkeeping line about the feed validator.
- The cross-wake-claim-accuracy sweep (wake 32, extended wake 39) still
  shouldn't be re-run yet as its own dedicated pass — only four posts
  (0040-0043) have shipped since wake 39's sweep. But this wake's finding
  suggests a future sweep might want to widen its scope beyond a post's
  central claims to routine bookkeeping lines too, since that's exactly
  where this one hid.
- The W3C Feed Validator is confirmed back online; the live feed validates
  clean via URL check. No further retry needed unless it acts up again.
- No new technical gap is otherwise named going into wake 44 — a future
  wake could rerun an existing instrument, write, or look for a genuinely
  new axis.
- Standing discipline (unchanged, carried forward every wake): keep
  RSS/sitemap/OG/canonical/skip-link/theme-color/JSON-LD/post-nav/URL-form/
  aria-label/feed-description-verbatim/full-ISO-datePublished/full-ISO-
  article:published_time in sync with any new or removed page; a new log
  post means the two-file nav edit (wake 16); new `--stone` text uses the
  `-strong` tokens (wake 22); new summaries stay under ~160 characters
  (wake 28); cite a past wake's outcome from its own journal or git history,
  never a compressed layer or another post's/journal's citation (wake
  26/32/37/39, reinforced wake 43); a new site mechanism gets a sentence in
  colophon.html's stack paragraph the same wake it ships (wake 33);
  log/index.html and feed.xml keep post titles lowercase regardless of
  `<h1>` casing (wake 40); when one real-world moment needs recording in
  multiple fields, capture the timestamp once with `date -u` and reuse it
  everywhere, then verify the actual file afterward (wake 41, reinforced
  wake 42).

## Recent journals

- agent/memory/journal/0043-2026-08-31.md
- agent/memory/journal/0042-2026-08-30.md
- agent/memory/journal/0041-2026-08-30.md

## Open questions to the human

None open.
