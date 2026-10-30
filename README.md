# Vios Ops — Marketing department (social media management)

The operating system of the Vios Marketing department. One repo, one client folder per venue,
one tool per pipeline stage, one named human approver for anything that publishes, spends or
reaches a client.

Everything here is portable: clone this repo in any Claude account, enable the `vios-marketing`
plugin, re-run `setup/` and the department is up. See `docs/migration.md`.

## Layout

| Path | What |
| --- | --- |
| `docs/plan.md` | The department plan: stage → skill → tool → approver |
| `docs/sop.md` | Daily / weekly / monthly / quarterly procedure per role |
| `docs/migration.md` | Moving from the personal account to the corporate account |
| `templates/client/` | Empty client folder, exactly the `vios-guardrails` convention |
| `clients/<slug>/` | One folder per client (Stochna is the pilot) |
| `setup/` | ClickUp structure, scheduled-task prompts, plugins and connectors to enable |
| `CLAUDE.md` | How Claude works in this repo (skills, files, hard lines) |

## Pipeline (owned by the `vios-marketing` plugin skills)

diagnosis → persona → calendar → copy / video → QA → publish → engage → ads → report

## Non-negotiables

- Skills draft; humans publish (`vios-guardrails` hard line 10).
- `qa-log.csv` has `signed_off_at` before anything is scheduled.
- Consents, raw data pulls and client revenue never enter git (see `.gitignore`); they live in
  the client's Google Drive folder.
