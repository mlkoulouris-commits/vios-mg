# Vios Ops — Marketing department (social media management)

The operating system of the Vios Marketing department. One repo, one client folder per venue,
one tool per pipeline stage, one named human approver for anything that publishes, spends or
reaches a client.

Everything here is portable: clone this repo in any Claude account, enable the Vios plugins
(`vios-core`, `vios-brand`, `vios-marketing`), re-run `setup/` and the department is up. See `docs/migration.md`.

## Layout

| Path | What |
| --- | --- |
| `docs/plan.md` | The department plan: stage → skill → tool → approver |
| `docs/sop.md` | Daily / weekly / monthly / quarterly procedure per role |
| `docs/method.md` | The pinned reference set: manuscript, framework master, guidelines structure, plugin, worked examples |
| `docs/workflow.md` | Workflow chart with stage, skill, tool and human per step |
| `docs/migration.md` | Moving from the personal account to the corporate account |
| `templates/client/` | Empty client folder, exactly the `vios-guardrails` convention |
| `clients/<slug>/` | One folder per client (Stochna is the pilot) |
| `setup/` | ClickUp structure, scheduled-task prompts, plugins and connectors to enable |
| `CLAUDE.md` | How Claude works in this repo (skills, files, hard lines) |

## Pipeline (owned by the Vios plugin skills: `vios-brand` for stages 1–3, `vios-journey` for the map, design and training, `vios-marketing` from stage 4, `vios-core` throughout)

diagnosis → persona → calendar → copy / video → QA → publish → engage → ads → report

## Releasing a skill change

Edit under `plugin/<plugin>/skills/`, then `python scripts/release.py`:

- `package <plugin> <x.y.z>` bumps the version, rebuilds `plugin/<plugin>-<x.y.z>.plugin`; upload it in Settings › Plugins, commit.
- `sync [plugin]` copies the repo skills into the installed plugin cache for a quick fix (live next session, replaced by the next upload).
- `tasks` copies `setup/prompts/*.md` over the live scheduled-task prompts.
- `status` shows repo, packaged and installed versions.

## Non-negotiables

- Skills draft; humans publish (`vios-guardrails` hard line 10).
- `qa-log.csv` has `signed_off_at` before anything is scheduled.
- Consents, raw data pulls and client revenue never enter git (see `.gitignore`); they live in
  the client's Google Drive folder.
