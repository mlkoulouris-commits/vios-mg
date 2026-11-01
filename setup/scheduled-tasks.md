# Scheduled tasks

Claude scheduled tasks created in the personal account on 2026-10-29. They run while the Claude desktop app is open (a missed run fires on next launch). To recreate in another account, ask Claude: "create the scheduled tasks from setup/scheduled-tasks.md". Each prompt is self-contained and lives in `~/.claude/scheduled-tasks/<taskId>/SKILL.md`; copies are kept in `setup/prompts/` so the corporate account can be set up without the personal machine; `python scripts/release.py tasks` pushes an edited copy to the live task.

| taskId | Schedule (local) | Skill | Writes to | Needs |
| --- | --- | --- | --- | --- |
| `vios-daily-engagement-triage` | daily 10:00 | persona-voice, guardrails 11 | each client's Engagement list | `instagram` plugin (enabled); Metricool brand in accounts.md |
| `vios-weekly-ads-audit` | Mon 08:00 | ads-audit | each client's Ads list; `data/YYYY-MM/ads-audit_*.md` | Windsor.ai plugin (public Ad Library fallback works without) |
| `vios-monthly-content-calendar` | 20th 09:00 | content-calendar | `data/YYYY-MM/calendar_*.md`; one ClickUp task per post | diagnosis + persona bible filled; calendar-sources dated |
| `vios-monthly-client-report` | 2nd 09:00 | monthly-report | Claude Doc; `data/YYYY-MM/*_pulled-*`; ClickUp review task | Metricool connected; bookings-by-source pasted from Memento |
| `vios-quarterly-review` | 1 Jan/Apr/Jul/Oct 09:00 | guardrails | ClickUp "Department — Setup & SOP" | — |

All five run over every folder in `clients/` and read ids from each client's `accounts.md` (since 2026-10-30). All five: draft only, never publish, send, spend, commit or push.

## Prompt copies

The full prompts are in `setup/prompts/<taskId>.md` (exported from the scheduled-tasks folder). Regenerate the copies with:

```bash
for d in ~/.claude/scheduled-tasks/vios-*/; do cp "$d/SKILL.md" "setup/prompts/$(basename "$d").md"; done
```
