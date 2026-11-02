---
name: "vios-engagement-setup"
description: "Open the project workspace for a signed Vios engagement: the client folder from the template, the client's five ClickUp lists and the Deliverables tasks from the setup file, the Drive folders for consents, stills and data, the intake record, the chase list, the first scheduled reviews and the month-0 baseline measured before any deliverable. VIOS Practice section 5.3 move 4. Use when a proposal is signed, when a marketing client becomes a Practice client, or when a workspace needs to be rebuilt in another account."
---

# Vios Engagement Setup

Move 4 of the intake protocol, done once per engagement so every workspace has the same shape and any practitioner can move between them. Layer 3 of the practice: the engagement's record, separate from the method (Layer 1) and the patterns (Layer 2). Hard lines: `vios-core:vios-guardrails` 12 (consents, data and revenue never in git; one workspace per client; access per client).

**Work in seven steps, in the order below. Stop after each and ask one question.** Each step shows at most ten plain lines: what will be made, where, and for which stages; no ids, no file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is created, in the repo, ClickUp, Drive or the calendar, before the user has seen the step that creates it, except `status.json` and `open-facts.md` bookkeeping.

## Steps

1. **Folder**: the files to fill and the stages out of scope. Ask: *"Fill the folder like this?"*
2. **ClickUp**: lists, tasks, approvers and due dates as a short table. Ask: *"Create these lists and tasks?"*
3. **Drive**: the folder and its five subfolders. Ask: *"Make the Drive folder and link it?"*
4. **Reviews on the calendar**: the sign-off dates and who is invited, one line each. Ask: *"Book these reviews?"*
5. **Scheduled tasks**: whether the client is picked up by the department tasks. Ask: *"Marketing loop in scope, picked up as shown?"*
6. **Hand the keys**: owner, approver, where the signed proposal lives. Ask: *"Are these the names?"*
7. **Baseline**: the month-0 numbers, one line per measure with its source and n; the rows that cannot be filled, and who holds them. Ask: *"Measure the baseline like this, or can you paste what is missing now?"*

## Ask only when necessary; never invent

- **Ids are never invented.** Workspace, folder, list and field ids come from `setup/clickup.json`; task ids from the ClickUp response of step 2; Drive and calendar ids from the connector's response or the user. An id the files do not hold and the connector does not return is one question to the user, or "to confirm" in `accounts.md` plus a row in `[client]/open-facts.md` and, when it blocks the next action or the stage from closing, a blocker in `status.json`.
- Approver, due dates, stages in scope and the account manager come from the intake record, the signed proposal and `status.json`; a gap is one question if the step cannot proceed, otherwise "to confirm" and a row. A question is asked once; never ask what `status.json`, `open-facts.md` or the folder already answers.
- **Baseline numbers are never estimated.** Each comes from a pull saved in `[client]/data/YYYY-MM/` (Memento export, POS export, Metricool, GBP, ads account) or from a paste by the user, with source and date. No pull and no paste → the row reads "to confirm", goes to `open-facts.md`, and the baseline is **partial** in `status.json`; the engagement goes on. Under three months of trading history → the baseline says so and measures what exists.
- One `<Client> — Deliverables` list with the Stage field (`setup/clickup.json`) is the house shape since 2026-11-02; `setup/clickup-engagement.json` is the seed list of tasks per stage, not a list-per-stage layout.

## After every step

Write what the step made: the folder files (step 1), `accounts.md` with the ids returned (steps 2–3), the calendar lines in `README.md` (step 4), the keys line in `README.md` (step 6), `data/baseline-YYYY-MM.md` (step 7). Then `status.json`: `current_stage`, `approver`, `account_manager`, each stage's scope and its `deliverables` map (`status` not started, `clickup` task id, `due`), `baseline` (`status`, `date`, `file`, `missing`), blockers added or removed, `next_action`, `updated`.

Then the ClickUp task "Setup <Client>" in the client's Deliverables list (id at `stages.Engagement.deliverables.Setup.clickup`): **draft** while the steps run, **done** at step 7; the baseline gets its own task "Baseline <Client>" (Stage = Engagement; id under `Baseline`), **done** when measured, **review** while partial with the missing rows in the description, **review** with "not trading: first full month after opening <date>" in the description for a venue not yet open.

No client PDF for the setup; the baseline ships as `clients.py pdf <slug> data/baseline-YYYY-MM.md "<Client>-Baseline-<YYYY-MM>"` because the owner sees it again in the first report. The page and its render carry revenue, so neither is committed (hard line 12): `clients/*/data/*`, `clients/*/deliverables/*-Baseline-*` and `clients/*/deliverables/*-Report-*` (the monthly report's render) are gitignored; the account manager copies the PDF to Drive › deliverables, and `status.json` › `baseline.file` is the local path.

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.2 (Layer 3) and § 5.3 move 4.
- `vios-core:vios-guardrails` › client file convention (the folder), `templates/client/` (the files), `setup/clickup-engagement.json` (the seed tasks per stage), `setup/clickup.json` (the account's ids), `setup/plugins-and-connectors.md` (which connectors this account has).
- `[client]/README.md` › Intake record, `[client]/status.json` (`python scripts/clients.py status <slug>`) and the signed proposal: which stages are in scope decides which lists and folders are made.

## The steps in full

1. **Folder**: copy `templates/client/` to `[client]/` (or `python scripts/clients.py new <slug> "<Name>"` when the intake has not made it); fill `README.md` with the intake record; `accounts.md` with the ids known so far; `open-facts.md` with the intake's open rows. Stages out of scope keep their folders, empty, with a line saying why.
2. **ClickUp**: the five `<Client>` lists from `setup/clickup.json` (Deliverables · Open facts · Content · Engagement · Ads); in Deliverables one task per in-scope deliverable seeded from `setup/clickup-engagement.json`, Stage and Approver fields set, due date from the timeline, statuses Draft → Review → Approved → Done; in Open facts one task per row of `open-facts.md` (`python scripts/clients.py facts <slug>` builds the payload). Use the bulk operation, one call per list; record the task ids in `status.json` (stage deliverables under their stage, Setup and Baseline under `stages.Engagement.deliverables`).

   The intake and proposal tasks waiting in "Department — Setup & SOP" are moved into the new Deliverables list (`clickup_move_task`), ids unchanged.

   When `setup/clickup.json` › Approver has no option for this client's approver, add one with the field API (`clickup_execute_operator`, model `field_option`, operator `update_many`, the Approver field id, the approver's name as in `status.json`) and write the returned option id into `setup/clickup.json`. Until that option exists the tasks carry "To confirm"; the option list in `setup/clickup.json` is the record.
3. **Drive**: the client's Drive folder with `consents/`, `character-sheet/`, `data/`, `deliverables/`, `briefs/`; link it from `accounts.md`. Nothing from these folders is committed.
4. **Reviews on the calendar**: each stage's sign-off meeting, the Stage 4 retrospective, the thirty-day review after go-live, the case-writing window, and one recurring row for the account manager alone: the founder note every second Friday (`vios` › Founder note); as calendar events with the approver invited (not to the note), via the calendar connector when present.
5. **Scheduled tasks**: when the marketing loop is in scope, confirm the client is picked up by the five department tasks (they iterate `clients/*/accounts.md`); nothing new is scheduled per client.
6. **Hand the keys**: one line in `README.md` naming who in the practice owns the workspace (account manager), who approves (from the front page of the persona bible once it exists), and where the signed proposal lives.
7. **Baseline**: copy `templates/client/data/baseline.md` to `[client]/data/baseline-YYYY-MM.md` (the measurement month) and fill it from pulls saved to `[client]/data/YYYY-MM/`: venue (covers, revenue, average check, items per cover, daypart and category mix, labour % and COGS % — Memento P&L, labor and COGS reports when the client is on Memento, otherwise the POS export), bookings by source (Memento reservations or the client's book), reviews (rating, count, 90-day velocity, share answered; praise and complaint themes from the review mining when it is on file, otherwise count and rating only: the full mining is pulled at diagnosis step 4), social and local (Metricool / Windsor / GBP), paid (ads accounts). 

   Period: the three full months before the measurement date plus the same three a year earlier. Every row carries source, pulled-at and n; section 6 lists what is "to confirm" and who holds it; section 7 reads the numbers in five lines, with no targets (targets belong to the proposal's KPI table). The measurement date goes to `status.json` › `baseline.date`; **measured** when every other row is filled (the two theme rows wait for the mining and do not make it partial), **partial** otherwise. The baseline is made once, before the first deliverable; a client already in the marketing loop when the practice engagement starts keeps the baseline from the month the loop began.

   **A venue not yet trading** has no baseline to measure: `baseline.status` is **not trading**, the page is not written, and the first full month of trading becomes the baseline (the account manager books the measurement date at handoff; the proposal's KPI table says "measured in month 1 after opening"). Step 7 also adds to `accounts.md` the POS and booking-system rows as "to confirm" when they are missing, since the baseline cannot be measured without them.

## Output

The folder, the lists, the Drive links, the calendar events, the baseline page and its PDF, `status.json`, and one line: client · stages · lists created · reviews booked · baseline measured or partial (rows to confirm) · what is "to confirm" and who confirms it · next step, the first in-scope stage's skill. Then stop; the front door reruns the card.

## Rebuilding elsewhere

The same steps run in another account from the repo alone: clone, `templates/client/`, `setup/clickup-engagement.json`, the connectors listed in `setup/plugins-and-connectors.md`. That is the migration path in `docs/migration.md`.
