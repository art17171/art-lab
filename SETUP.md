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
