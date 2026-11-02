---
name: "vios"
description: "The front door to a Vios client: one status card (stage, approver, proposal, blockers, open facts, next action) from the client status file and ClickUp, then the next action offered as a single question. Use for '/vios' followed by a client name, 'where are we with a client', 'what is next for a client', 'status', or when the user names a client without naming a skill."
---

# Vios — front door

One screen, one question. The user should never need to remember which skill comes next.

## Read first

- `scripts/clients.py status <slug>` (run it; it renders the card from `clients/<slug>/status.json` and counts open rows in `open-facts.md`). No `status.json` → say so and offer `clients.py new <slug> "<Name>"` or, for an existing folder, write one from the README's intake record.
- `setup/clickup.json` › the client's Deliverables and Open facts list ids; `clickup_filter_tasks` on the Deliverables list for anything in **review** (awaiting the user's sign-off).
- `vios-core:vios-guardrails` stays loaded for any client work that follows.

## The card (at most eight lines, plain words, no file paths, no fact numbers)

```
<Client> — Stage 2 (journey map) · approver: to confirm
Proposal: not sent · marketing loop: in
Stages: 1 revision/in progress · 2 in/review · 3 in/not started · 4 to confirm
Awaiting your sign-off: Journey map, Reasoning Note
Blocked by: two observed services (account manager); approver name (founder)
Open facts: 32, 4 overdue
Next: send the proposal
```

The card above is a real one with the name removed (`plugin/vios-core/references/worked-examples.md` › E1).

Then **one question** with at most four choices, the recommended one first:

*What do you want to do?* — **Proposal** · Chase the open facts · Sign off what's waiting · Status only

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
| Chase the open facts | list the open rows due soonest, five at a time, each as "ask <holder>: <fact>"; the user says what was answered; write the answer and date into `open-facts.md`, close the ClickUp task, drop the blocker from `status.json`. |
| Sign off what's waiting | show each **review** task as one line; on the user's yes set it to **approved** in ClickUp and in `status.json`; on changes, reopen the owning skill at its last step. |

Every routed skill follows the contract in `docs/operating-system.md`: short screens, one question per step, never guess, write the file then update `status.json` and move the ClickUp task, client deliverables also as PDF.

## Output

Nothing is written by this skill except through the routes above. End of a session on a client: rerun the card so the user sees what changed.
