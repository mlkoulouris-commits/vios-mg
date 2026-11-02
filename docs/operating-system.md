# The Vios operating system

Bottom line: no new app. Three pieces you already have, glued together, with one front door.

| Layer | Tool | What it holds |
| --- | --- | --- |
| Board (what you look at) | ClickUp folder "Vios Marketing" | one task per deliverable, per missing fact, per post; statuses and sign-offs |
| Vault (where the work lives) | this repo, `clients/<slug>/` + Google Drive | every file; `status.json` per client; final PDFs in `deliverables/` |
| Worker (who does the work) | the Vios plugins | skills that write the files, move the tasks, make the PDFs |

## ClickUp (instance personal_2026-11-02, see `setup/clickup.json`)

- One status set for the whole space: **Draft → Review → Approved → Scheduled → Published → Done**. Engagement deliverables use Draft → Review → Approved (= signed) → Done (= delivered as PDF). Marketing posts use all six.
- Per client, five lists: **Deliverables** (Stages 1–4, briefs, proposal, harvest), **Open facts** (mirror of `open-facts.md`, one task per row), Content, Engagement, Ads (the marketing loop, unchanged).
- Two folder-level fields on every task: **Stage** (1 Brand · 2 Map · 3 Design · 4 Training · Marketing · Engagement) and **Approver**.
- Ids live in `setup/clickup.json` and each client's `accounts.md`.

## status.json (schema `setup/status.schema.json`, template `templates/client/status.json`)

Six things at a glance: approver, proposal status, current stage, each stage's scope and status, blockers, next action. Every skill updates it at the end of a step. `/vios <client>` reads it.

## The skill contract (every Vios skill, from `vios-proposal` onward)

1. Short screens: at most ten plain lines and one question per step. No open-fact numbers, no section refs in chat; those go in the file.
2. Ask, never guess: a missing fact is one question to the user, or a row in `open-facts.md` and a blocker in `status.json`.
3. Every step writes its file, then updates `status.json` and moves the ClickUp task.
4. Every client-facing deliverable also ships as a PDF in `clients/<slug>/deliverables/` (Adobe `markdown_to_pdf`); the user forwards it, the practice never emails a client.
5. Writes nothing to disk before the user has seen the plan of the step.

## Daily use

ClickUp → what is awaiting your sign-off → approve or comment. Claude → `/vios <client>` → the status card and the next action. Forward PDFs.

## Build order

| # | Step | State |
| --- | --- | --- |
| 1 | ClickUp statuses, fields, Deliverables + Open facts lists; status.json schema; `scripts/clients.py`; Stochna + Atelier seeded | done 2026-11-02 |
| 2 | Front door `/vios <client>` (plugin `vios-engage`) | done 2026-11-02 |
| 3 | Engage skills (intake, proposal, setup, harvest) to the contract | proposal done; rest open |
| 4 | Brand + journey skills to the contract, each with a client PDF | open |
| 5 | Marketing loop: scheduled tasks drop drafts as ClickUp tasks in Review | open |
| 6 | Migrate ONE Gallery; retire `atelier-2026-10` | open |

## Not in scope

A web dashboard. ClickUp is the dashboard; a second app would be a second Memento to maintain.
