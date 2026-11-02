# Migrating to the vios-mg Claude account

Nothing in this setup is tied to the personal account except connector sign-ins, scheduled
tasks and claude.ai skill uploads, which are per machine / per account. Steps:

1. **Sign in**: open the Claude desktop app as the vios-mg user.
2. **Repo**: clone `github.com/mlkoulouris-commits/vios-mg` (or transfer it to the company GitHub org first: GitHub › Settings › Transfer). Open the folder in the Code tab.
3. **Plugins**: upload the packaged files in `plugin/` in this order: `vios-core`, `vios-brand`, `vios-journey`, `vios-engage`, `vios-marketing` (latest `.plugin` of each; versions in `.claude-plugin/marketplace.json`). Or add this repo as a marketplace and enable the same five. Then enable `instagram` and Windsor.ai. On a Team account the org admin does this step.
4. **Connectors** (Settings › Connectors): Metricool, ClickUp, Google Drive, Gmail, Google Calendar, Canva, Adobe Express, ElevenLabs. Use company logins.
5. **ClickUp**: create the company workspace, then ask Claude to "recreate the ClickUp structure from setup/clickup.json and setup/clickup-engagement.json".
6. **Scheduled tasks**: ask Claude to "create the scheduled tasks from setup/scheduled-tasks.md" (six tasks: daily triage, weekly content, weekly ads audit, monthly calendar, monthly report, quarterly review). Then delete the six personal-account copies, or they run twice.
7. **Drive**: move each client's `consents/`, `character-sheet/` stills and `data/` to the company Drive; update the Drive link in each `clients/*/accounts.md`.
8. **Clients**: the owner of each venue re-grants Meta Business, Google Ads, GBP and the Metricool brand to the company user, not to a person (Atelier = Metricool brand 7633845).

After it works:

- Delete the 12 stale stand-alone Vios skill copies on claude.ai in the personal account.
- **Memory**: the new account starts with no memory; this repo's `CLAUDE.md` and `docs/` carry the rules, so nothing is lost.
