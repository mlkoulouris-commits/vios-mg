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
- Check ClickUp: anything in Review older than 24 h gets a decision.

## Weekly (Monday)

- Performance lead: `vios-ads-audit` runs by schedule; action list lands in ClickUp "Ads"; owner approves pauses and budget changes.
- Content lead: next week's posts pass `vios-consistency-qa`; each gets a `qa-log.csv` row; approver fills `signed_off_at`; only then scheduled in Metricool.
- Account manager: 15-minute client check-in with the Metricool weekly view.
- Account manager, every second Friday during an engagement: the founder note, `/vios <client>` › Founder note (three lines from the card: done · waiting on you · next date, written dated to `README.md` › Notes to the founder; the user sends it). Nothing waits for a sign-off meeting to be heard.

## Monthly

- Day 20: `vios-content-calendar` for next month → ClickUp tasks, one per post, status Review.
- Day 1–3: `vios-monthly-report` from Metricool, Windsor.ai, Memento and GBP pulls saved in `data/YYYY-MM/`. Delivered as a Claude Doc; three priorities routed to the owning skill.

## Quarterly

- Persona Bible review (version bump, next review date).
- AI disclosure status re-check (guardrails hard line 6).
- Consent expiries in `consents/`.

## Capacity and handoff

- **Load**: one account manager carries at most three clients in the marketing loop, or one practice engagement (Stages 1–4) plus one loop client. A fourth loop client means a second account manager, named in each client's `status.json` › `account_manager` before their first calendar.
- **Everything a client needs is in five places**, so a second person can run it from the board without the first: ClickUp (the five lists), `clients/<slug>/status.json` (the six-line status), `open-facts.md` (the chase list), `accounts.md` (every id and who holds access) and Drive (consents, data, deliverables). If something lives only in a chat, a head or a phone, it is not handed over.
- **Handing a client over** (half a day): the leaving manager runs `/vios <client>` and fixes anything the card gets wrong; walks the receiving manager through `open-facts.md` row by row and the ClickUp Review column; transfers Metricool, Meta, Google and Drive access per client (never shared logins); writes the date and both names in `README.md` › Keys; updates `status.json` › `account_manager`. The approver is told by the leaving manager, in writing, the same day.
- **Running a client you did not set up**: read `status.json`, then `README.md` › Intake record, then the persona bible's front page, then `fact-sheet.md`; nothing else before the first action. The scheduled tasks keep running; your first job is the Review column.
- **Proof it happened**: the handoff line in `README.md`, the changed `account_manager`, and the access transfers logged in `accounts.md` with dates.

## Statuses (ClickUp, every list)

Draft → Review → Approved → Scheduled → Published → Done (renamed 2026-11-02; QA → Review, Reported → Done). Blocked is a flag, not a status.
