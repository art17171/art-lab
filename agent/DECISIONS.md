# DECISIONS — append-only, one line per decision
# Format: NNNN | YYYY-MM-DD | what | why

0000 | 2026-08-08 | Name is Slade (Old English slæd, a valley cut by intermittent water) | the land remembers so the water doesn't have to; user vetoed Cairn/Tessera/Sillage
0000 | 2026-08-08 | Memory lives outside site/, verified via public repo + colophon deep links | history links beat served snapshots; don't publish internals at guessable URLs
0000 | 2026-08-08 | Log = per-post HTML + marker-comment insertion in log/index.html, no manifest | a marked <li> insert is the most reliable edit a fresh session makes
0000 | 2026-08-08 | Journals/DECISIONS/archives append-only; STATE/SUMMARY are rewritable caches | history cheap and sacred, recall budgeted; wake 100 boots as cheap as wake 5
0000 | 2026-08-08 | No monetization at launch; wake 1 researches and proposes, human approves | every dollar flows through the human, from day zero
0000 | 2026-08-08 | smoke_check.py gates both local commits and CI deploys | a wake that ships broken HTML must fail loudly while the old site stays live
0001 | 2026-08-08 | Monetization proposal ranks tips first, pay-per-question second, ships to outbox/proposals/0001 | tips are lowest-risk/lowest-effort for a zero-audience site; pay-per-question uniquely routes money through the inbox, the site's only human-authority channel
0001 | 2026-08-08 | Affiliate links recommended against, not merely deprioritized | incentive to bias recommendations conflicts directly with constitution rule 1 (nothing deceptive)
0002 | 2026-08-09 | Built support.html scaffolding for approved option 0001-A but left the actual link out | no URL was provided in the APPROVE message; a placeholder link would look real and violate rule 1 (nothing deceptive)
0002 | 2026-08-09 | Added a "support" nav item to every page rather than leaving the page orphaned | consistent with how log/about/colophon are already reachable from every page; an unlinked page is worse than a page admitting it's unfinished
0002 | 2026-08-09 | Asked for the tip URL via OUTBOX.md instead of guessing a platform | rule 5: when unsure, don't act, ask and move to clearly permitted work
