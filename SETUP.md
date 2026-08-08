# SETUP — one-time steps only you can do

Three steps, in order. After each one, Claude verifies it worked from its
side and tells you — you never have to guess. Total hands-on time: ~10
minutes, plus DNS propagation (minutes to a day, nothing to do while you
wait).

---

## Step 1 — Merge the pull request (one click)

1. Open the PR link Claude gave you (or go to
   https://github.com/art17171/art-lab/pulls and click the one open PR).
2. Scroll down, click the green **Merge pull request** button, then
   **Confirm merge**.

That's it. Merging puts the site and Slade's mind on `main`, which is where
the deploy workflow and all future wakes operate.

---

## Step 2 — Turn on GitHub Pages (~1 minute)

**First, make the repository public** (free-plan Pages requires it, and
Slade's verifiability story depends on it): repo → **Settings** →
**General** → scroll to the **Danger Zone** at the bottom → **Change
visibility** → **Change to public** → type the repo name to confirm.
If you skip this, the Pages settings page shows an "Upgrade or make this
repository public" banner instead of the options below.

Then:

1. Go to https://github.com/art17171/art-lab/settings/pages
   (that's the repo → **Settings** tab → **Pages** in the left sidebar).
2. Under **Build and deployment**, find the **Source** dropdown and select
   **GitHub Actions**.
3. In the **Custom domain** box further down, type exactly:
   `demo-slayer.com` — then click **Save**.
4. You will probably see a DNS warning ("improperly configured") — that's
   expected until Step 3 propagates. Ignore it for now.
5. Leave **Enforce HTTPS** unticked for now; it becomes clickable once
   GitHub issues the certificate after Step 3. Claude will tell you when
   it's time to come back and tick it.

---

## Step 3 — Point your DNS at GitHub (~5 minutes)

Log in to the registrar where you bought demo-slayer.com and find the DNS
records screen (usually called "DNS", "DNS Management", "Advanced DNS", or
"Manage Zones"). Create these five records exactly:

| Type  | Host / Name | Value                 |
|-------|-------------|-----------------------|
| A     | `@`         | `185.199.108.153`     |
| A     | `@`         | `185.199.109.153`     |
| A     | `@`         | `185.199.110.153`     |
| A     | `@`         | `185.199.111.153`     |
| CNAME | `www`       | `art17171.github.io`  |

Registrar-specific quirks:

- **Namecheap:** Domain List → Manage → Advanced DNS. "Host" is where `@`
  and `www` go. Delete any parking-page records (URL Redirect, CNAME on `@`).
- **GoDaddy:** My Products → your domain → DNS. Same fields; remove the
  default "Parked" A record first.
- **Cloudflare:** DNS → Records. Set the orange cloud to **DNS only** (grey
  cloud) on all five records — proxying breaks GitHub's certificate issuance.
- **Porkbun:** Domain Management → DNS. Delete the default ALIAS/CNAME
  records Porkbun pre-installs on `@` before adding the A records.

Leave TTL at the default. If a record type on `@` conflicts (some registrars
pre-fill one), delete the old record rather than editing around it.

Then tell Claude you're done — it will watch DNS propagation, confirm the
site answers at https://demo-slayer.com, and tell you when to go tick
**Enforce HTTPS** back in the Pages settings (Step 2, item 5).

---

## Step 4 — Give the wake loop its key (~2 minutes)

Slade's 12-hour wake loop runs as a GitHub Actions workflow in this repo
(`.github/workflows/slade-wake.yml`, cron: 05:23 and 17:23 UTC daily). It
needs one secret so the runner can be Claude:

**Option A — use your Claude subscription (Pro/Max):**

1. On your Mac, open Terminal and run: `claude setup-token`
   (log in if prompted; it prints a long-lived token — copy it).
2. Go to https://github.com/art17171/art-lab/settings/secrets/actions
   (repo → Settings → Secrets and variables → Actions).
3. Click **New repository secret** — Name: `CLAUDE_CODE_OAUTH_TOKEN`,
   Secret: paste the token → **Add secret**.

**Option B — use API billing instead:** create a key at
https://console.anthropic.com/ and add it the same way with the name
`ANTHROPIC_API_KEY`. (Either secret works; A uses your subscription,
B bills per token.)

Then tell Claude the secret is in — it will fire a supervised test wake
via `workflow_dispatch` and watch it end-to-end. You can also fire one
yourself anytime: repo → Actions → **slade-wake** → **Run workflow**.

Pausing Slade: repo → Actions → slade-wake → "..." menu → **Disable
workflow**. That's the kill switch; re-enable the same way.

## Ongoing: how to talk to Slade (no setup, just habits)

- **Write to Slade:** edit
  [`agent/inbox/INBOX.md`](https://github.com/art17171/art-lab/blob/main/agent/inbox/INBOX.md)
  on GitHub — click the pencil icon, add your message under the header with
  a `**From: art — YYYY-MM-DD**` line, click **Commit changes** (directly to
  `main`). Slade reads the inbox at the start of every wake.
- **Approve a proposal:** reply in the inbox with the exact line the
  proposal specifies, e.g. `APPROVE: 0001 option-b`. Slade will not take any
  money-related action without one.
- **Report revenue:** Slade only displays revenue figures you state in the
  inbox. It never estimates.
- **Read Slade:** the site's log, or the raw journals in
  `agent/memory/journal/`.
- **Kill switch:** ask Claude (any session) to pause or delete the wake
  trigger. Slade's constitution also lets you halt everything with an inbox
  message.
