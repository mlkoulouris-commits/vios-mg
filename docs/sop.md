# SOP — Vios Marketing, social media management

Every item names the role, the skill, the tool and the proof that it happened.

## Onboarding a client (once)

1. Account manager copies `templates/client/` to `clients/<slug>/` and fills `accounts.md` and `fact-sheet.md` from the client, never from memory.
2. Run `vios-brand-diagnosis` → `diagnosis.md`. Client owner signs the positioning.
3. Run `vios-persona-builder` → `persona-bible.md` with front page complete (approver, register, emoji, alcohol, AI disclosure, version, next review). Consents filed in Drive before any likeness or voice is used.
4. Brand book and Canva brand kit. Metricool brand connected (Instagram, Facebook, TikTok, Google Business). ClickUp list created from `setup/clickup.json`.
5. `calendar-sources.md` filled with dated holiday and event sources for BG/GR/EN as relevant.

## Daily (content lead, 20 min)

- Engagement triage runs by schedule (see `setup/scheduled-tasks.md`): drafts replies in persona voice, escalates hard-line 11 cases. Content lead reviews the batch, approver signs, replies go out from the platform.
- Check ClickUp: anything in QA older than 24 h gets a decision.

## Weekly (Monday)

- Performance lead: `vios-ads-audit` runs by schedule; action list lands in ClickUp "Ads"; owner approves pauses and budget changes.
- Content lead: next week's posts pass `vios-consistency-qa`; each gets a `qa-log.csv` row; approver fills `signed_off_at`; only then scheduled in Metricool.
- Account manager: 15-minute client check-in with the Metricool weekly view.

## Monthly

- Day 20: `vios-content-calendar` for next month → ClickUp tasks, one per post, status Draft.
- Day 1–3: `vios-monthly-report` from Metricool, Windsor.ai, Memento and GBP pulls saved in `data/YYYY-MM/`. Delivered as a Claude Doc; three priorities routed to the owning skill.

## Quarterly

- Persona Bible review (version bump, next review date).
- AI disclosure status re-check (guardrails hard line 6).
- Consent expiries in `consents/`.

## Statuses (ClickUp, every list)

Draft → QA → Approved → Scheduled → Published → Reported. Blocked is a flag, not a status.
