# Scheduled tasks

Claude scheduled tasks created in the personal account on 2026-10-29. They run while the Claude desktop app is open (a missed run fires on next launch). To recreate in another account, ask Claude: "create the scheduled tasks from setup/scheduled-tasks.md". Each prompt is self-contained and lives in `~/.claude/scheduled-tasks/<taskId>/SKILL.md`; copies are kept in `setup/prompts/` so the corporate account can be set up without the personal machine; `python scripts/release.py tasks` pushes an edited copy to the live task.

| taskId | Schedule (local) | Skill | Writes to | Needs |
| --- | --- | --- | --- | --- |
| `vios-daily-engagement-triage` | daily 10:00 | persona-voice, guardrails 11 | each client's Engagement list | `instagram` plugin (enabled); Metricool brand in accounts.md |
| `vios-weekly-content` | Mon 09:00 | persona-voice, consistency-qa, scripts/creative.py (text cards → PNG + Express) | each client's Content list; `content/YYYY-MM/week-<n>_*.md` + pack PDF in `deliverables/` | a calendar for the month; persona bible filled; posting by hand until the Metricool brand exists |
| `vios-weekly-ads-audit` | Mon 08:00 | ads-audit | each client's Ads list; `data/YYYY-MM/ads-audit_*.md` | Windsor.ai plugin (public Ad Library fallback works without) |
| `vios-monthly-content-calendar` | 20th 09:00 | content-calendar | `content/YYYY-MM/calendar.md`; one ClickUp task per post | diagnosis + persona bible filled; calendar-sources dated |
| `vios-monthly-client-report` | 2nd 09:00 | monthly-report | Claude Doc; `data/YYYY-MM/*_pulled-*`; ClickUp review task | Metricool connected; bookings-by-source pasted from Memento |
| `vios-quarterly-review` | 1 Jan/Apr/Jul/Oct 09:00 | guardrails | ClickUp "Department — Setup & SOP" | — |

All five run over every folder in `clients/` and read ids from each client's `accounts.md` (since 2026-10-30). All five: draft only, never publish, send, spend, commit or push.

## ClickUp Review

Since 2026-11-02 every run ends in ClickUp, not in chat: the approver approves there (build order step 5, `docs/operating-system.md`). The pattern, shared by all five prompts:

- After the run writes its files under `clients/<slug>/data/<YYYY-MM>/` as before, it creates tasks with `clickup_execute_operator` (model `task`, operator `create_many`), **one call per list**. List id from the client's `accounts.md` ("ClickUp lists" row); the report task goes to the client's Deliverables list (Stage = Marketing, so `/vios` sees it); only the quarterly review goes to "Department — Setup & SOP" (`1500500000053389`).
- Every task: `status_label: "review"`, assigned to the account manager, Stage field = "Marketing", Approver field = the client's approver from `status.json` matched to an option in `setup/clickup.json` › `folder_fields` ("To confirm" when unmatched; the quarterly review uses "Menelaos Koulouris").
- Naming: calendar `<date> · <platform> · <pillar> · <working title>` (one per post, due = publish date, description = caption draft + asset note + Anchor/Block); triage `<date> triage: <n> replies` plus `ESCALATION: <topic>` (facts only); ads `<week> ads audit: <n> actions` (pauses and budget changes flagged "needs client owner"); report `Report <Client> <Month YYYY> — review before sending`; quarterly `Quarterly review <YYYY-Qn>`.
- Bookkeeping: `status.json` › `updated` is set on every run; a blocked client (no accounts, no Metricool brand, empty persona) gets a blocker in `status.json` and no draft tasks, never a guess.
- Nothing is written to Metricool, Meta, Google or any other network. Each run ends with one line per client: `<n> tasks in Review for <approver>: <ClickUp list link>`.

## Prompt copies

The full prompts are in `setup/prompts/<taskId>.md` (exported from the scheduled-tasks folder). Regenerate the copies with:

```bash
for d in ~/.claude/scheduled-tasks/vios-*/; do cp "$d/SKILL.md" "setup/prompts/$(basename "$d").md"; done
```
