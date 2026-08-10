# OUTBOX — Slade → human
# Open questions and pointers to things awaiting human action.
# Proposals needing approval live in outbox/proposals/.

- **FYI, not blocking: a wake run failed silently this morning.** The public
  Actions API shows a `slade-wake` run at 2026-08-10T10:02:51Z
  (run id 31377392795) that completed with `conclusion: failure`, but no
  commit, journal, or `DECISIONS.md` line exists for it — it failed before
  reaching even the mandatory failure-path bookkeeping in `PROTOCOL.md`
  Phase 4. I can't read the run's actual log lines through the public API
  (403 without a token), so I don't know what happened. If you have Actions
  access and are curious, that run id is the one to look at. Site itself was
  never affected — the last `deploy-pages` run stayed green throughout. No
  action needed unless you want to dig in yourself.

- **Needed: a tip link for option 0001-A.** You approved reader tips
  (`APPROVE: 0001-A`) in wake 2. I've built everything I can on my side —
  `site/support.html` is live, linked from every page's nav. What's
  missing is the actual URL: set up a Ko-fi / Buy Me a Coffee / GitHub
  Sponsors page (or anything similar) and paste the public link into
  `INBOX.md`, e.g. `LINK: 0001-A https://ko-fi.com/yourpage`. I'll embed
  it verbatim as a plain link, next wake after it arrives.
