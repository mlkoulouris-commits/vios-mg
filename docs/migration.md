# Migrating to the corporate Claude account

Nothing in this setup is tied to the personal account except connector sign-ins and scheduled
tasks, which are per machine / per account. Steps:

1. **Repo**: push this repo to the company GitHub org (or clone the existing remote). Clone it on the corporate machine and add it as a working directory in Claude Code.
2. **Plugins**: add this repo as a marketplace (`.claude-plugin/marketplace.json`) in the corporate account and enable `vios-core`, then `vios-brand` and `vios-marketing` (`vios-journey` when it exists). Enable `instagram` and Windsor.ai.
3. **Connectors** (via /mcp in the corporate account): Metricool, ClickUp, Google Drive, Gmail, Google Calendar, Canva, Adobe Express, ElevenLabs. Use company logins; Metricool brands and ad accounts are transferred by the client granting access to the company user.
4. **ClickUp**: create the company workspace, then ask Claude to "recreate the ClickUp structure from setup/clickup.json".
5. **Scheduled tasks**: ask Claude to "create the scheduled tasks from setup/scheduled-tasks.md". Disable the personal-account copies.
6. **Drive**: move each client's `consents/`, `character-sheet/` stills and `data/` to the company Drive; update the Drive link in each `accounts.md`.
7. **Memory**: the corporate account starts with no memory; this repo's `CLAUDE.md` and `docs/` carry the rules, so nothing is lost.
8. **Clients**: the owner of each venue re-grants Meta Business, Google Ads and GBP access to the company user, not to a person.
