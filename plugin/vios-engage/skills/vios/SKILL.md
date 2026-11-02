---
name: "vios"
description: "The front door to a Vios client: one status card (stage, approver, proposal, blockers, open facts, next action) from the client status file and ClickUp, then the next action offered as a single question. Use for '/vios' followed by a client name, 'where are we with a client', 'what is next for a client', 'status', or when the user names a client without naming a skill."
---

# Vios — front door

One screen, one question. The user should never need to remember which skill comes next.

## Read first

- `python scripts/release.py status` once per session: when an installed plugin is behind the repo version, say so in one line before the card ("engage installed 0.2.3, repo 0.4.0: the new steps load after the upload") and go on; for the steps the install lacks, follow the repo's `SKILL.md` text read from disk.
- `scripts/clients.py status <slug>` (run it; it renders the card from `clients/<slug>/status.json` and counts open rows in `open-facts.md`). No `status.json` → say so and offer `clients.py new <slug> "<Name>"` or, for an existing folder, write one from the README's intake record.
- `setup/clickup.json` › the client's Deliverables and Open facts list ids; `clickup_filter_tasks` on the Deliverables list for anything in **review** (awaiting the user's sign-off) and, while `stages.Engagement.deliverables` holds an id for a task not yet moved by setup step 2 (the intake or the proposal awaiting signature), "Department — Setup & SOP" filtered by the client's name.
- `vios-core:vios-guardrails` stays loaded for any client work that follows.

## The card (at most nine lines, plain words, no file paths, no fact numbers)

```
**Gradina (DEMO)** — 0 intake · approver: Nadia Petrova (founder, DEMO) · updated 2026-11-02
Proposal: not sent (v2) · marketing loop: in · baseline: not trading
Stages: Brand in/not started · Map in/not started · Design in/not started · Training in/not started
Engagement: no tasks yet
KPIs: covers per Friday and Saturday evening, garden measured in month 1 after opening → 80 · tables that book their next visit before leaving measured in month 1 after opening → set at baseline
Blocked by: Budget and target spend per head (founder)
Open facts: 10, 0 overdue
Next: Send the v2 PDF (with the KPI table) to Nadia; on signature run vios-engagement-setup steps 1-6; the venue is not trading, so the first full month of trading (May 2027, opening 15 April 2027) becomes the baseline  →  vios-engage:vios-proposal
```

The card above is `python scripts/clients.py status demo-gradina` as run on 2026-11-02 (the DEMO client; `plugin/vios-core/references/worked-examples.md` › E1). "Engagement" lists the tasks no stage owns (intake, proposal, setup, baseline, harvest, reports) with their status; a "Training proof" line appears when Stage 4 has an audit block; "Awaiting your sign-off" comes from the ClickUp review filter. A target longer than the card allows is cut at a word and the sentence lives in `target_note`.

Then **one question** with at most four choices, the recommended one first:

*What do you want to do?* — **Proposal** · Chase the open facts · Sign off what's waiting · Founder note

## Routing

| Choice | Skill |
| --- | --- |
| Proposal / quote / scope | `vios-engage:vios-proposal` |
| Intake, first call, is this a client | `vios-engage:vios-intake` |
| Open the workspace after signature | `vios-engage:vios-engagement-setup` |
| Stage 1 work | `vios-brand:vios-brand-diagnosis` → `vios-messages-and-story` → `vios-persona-builder` → `vios-name-and-tagline` → `vios-brand-book` |
| Stage 2 / 3 / 4 | `vios-journey:vios-journey-map` / `vios-journey-design` / `vios-training-programme` |
| Marketing loop | `vios-marketing:*` by task (calendar, voice, QA, ads, report) |
| Close | `vios-engage:vios-harvest` |
| Chase the open facts | list the open rows due soonest, five at a time, each as "ask <holder>: <fact>"; the user says what was answered; write the answer and date into `open-facts.md`, close the ClickUp task (found by its "#n" prefix in the client's Open facts list; `clients.py facts` names tasks "#n [holder] fact" and writes no ids back), drop the blocker from `status.json`. |
| Sign off what's waiting | show each **review** task as one line; on the user's yes set the deliverable to **approved** in ClickUp and in `status.json` (a stage closes as **signed** in `stages.<stage>.status`, and this route, not the stage skill, then moves the stage's seeded "Stage N sign-off" task in the Deliverables list to **approved**), and for a stage or proposal sign-off write the approver's pulse line (one sentence: what worked, what to change) dated into `README.md` › Sign-offs (create the heading when missing); on changes, reopen the owning skill at its last step. |
| Founder note (every second Friday during an engagement) | three lines from the card, in prose: done since the last note · waiting on you (the open facts the founder holds) · next date (the next review or sign-off). Written dated into `README.md` › Notes to the founder (create the heading when missing) and shown to the user, who sends it; the practice never emails a client. |

Every routed skill follows the contract in `docs/skill-contract.md`: short screens, one question per step, never guess, write the file then update `status.json` and move the ClickUp task, client deliverables also as PDF, the pulse line at a sign-off.

## Output

Nothing is written by this skill except through the routes above. End of a session on a client: rerun the card so the user sees what changed.
