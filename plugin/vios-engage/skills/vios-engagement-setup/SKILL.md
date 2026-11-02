---
name: "vios-engagement-setup"
description: "Open the project workspace for a signed Vios engagement: the client folder from the template, the ClickUp engagement lists per stage from the setup file, the Drive folders for consents, stills and data, the intake record, the chase list and the first scheduled reviews. VIOS Practice section 5.3 move 4. Use when a proposal is signed, when a marketing client becomes a Practice client, or when a workspace needs to be rebuilt in another account."
---

# Vios Engagement Setup

Move 4 of the intake protocol, done once per engagement so every workspace has the same shape and any practitioner can move between them. Layer 3 of the practice: the engagement's record, separate from the method (Layer 1) and the patterns (Layer 2). Hard lines: `vios-core:vios-guardrails` 12 (consents, data and revenue never in git; one workspace per client; access per client).

**Work in six steps, in the order below. Stop after each and ask one question.** Each step shows at most ten plain lines: what will be made, where, and for which stages; no ids, no file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is created, in the repo, ClickUp, Drive or the calendar, before the user has seen the step that creates it, except `status.json` and `open-facts.md` bookkeeping.

## Steps

1. **Folder**: the files to fill and the stages out of scope. Ask: *"Fill the folder like this?"*
2. **ClickUp**: lists, tasks, approvers and due dates as a short table. Ask: *"Create these lists and tasks?"*
3. **Drive**: the folder and its five subfolders. Ask: *"Make the Drive folder and link it?"*
4. **Reviews on the calendar**: the sign-off dates and who is invited, one line each. Ask: *"Book these reviews?"*
5. **Scheduled tasks**: whether the client is picked up by the department tasks. Ask: *"Marketing loop in scope, picked up as shown?"*
6. **Hand the keys**: owner, approver, where the signed proposal lives. Ask: *"Are these the names?"*

## Ask only when necessary; never invent

- **Ids are never invented.** Workspace, folder, list and field ids come from `setup/clickup.json`; task ids from the ClickUp response of step 2; Drive and calendar ids from the connector's response or the user. An id the files do not hold and the connector does not return is one question to the user, or "to confirm" in `accounts.md` plus a row in `[client]/open-facts.md` and a blocker in `status.json`.
- Approver, due dates, stages in scope and the account manager come from the intake record, the signed proposal and `status.json`; a gap is one question if the step cannot proceed, otherwise "to confirm" and a row. A question is asked once; never ask what `status.json`, `open-facts.md` or the folder already answers.
- One `<Client> — Deliverables` list with the Stage field (`setup/clickup.json`) is the house shape since 2026-11-02; `setup/clickup-engagement.json` is the seed list of tasks per stage, not a list-per-stage layout.

## After every step

Write what the step made: the folder files (step 1), `accounts.md` with the ids returned (steps 2–3), the calendar lines in `README.md` (step 4), the keys line in `README.md` (step 6). Then `status.json`: `current_stage`, `approver`, `account_manager`, each stage's scope and its `deliverables` map (`status` not started, `clickup` task id, `due`), blockers added or removed, `next_action`, `updated`. Then the ClickUp task "Setup <Client>" in the client's Deliverables list: **draft** while the steps run, **done** at step 6. No client PDF: nothing in setup is client-facing.

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.2 (Layer 3) and § 5.3 move 4.
- `vios-core:vios-guardrails` › client file convention (the folder), `templates/client/` (the files), `setup/clickup-engagement.json` (the lists and statuses per stage), `setup/clickup.json` (the account's ids), `setup/plugins-and-connectors.md` (which connectors this account has).
- `[client]/README.md` › Intake record, `[client]/status.json` (`python scripts/clients.py status <slug>`) and the signed proposal: which stages are in scope decides which lists and folders are made.

## The steps in full

1. **Folder**: copy `templates/client/` to `[client]/` (or `python scripts/clients.py new <slug> "<Name>"` when the intake has not made it); fill `README.md` with the intake record; `accounts.md` with the ids known so far; `open-facts.md` with the intake's open rows. Stages out of scope keep their folders, empty, with a line saying why.
2. **ClickUp**: the five `<Client>` lists from `setup/clickup.json` (Deliverables · Open facts · Content · Engagement · Ads); in Deliverables one task per in-scope deliverable seeded from `setup/clickup-engagement.json`, Stage and Approver fields set, due date from the timeline, statuses Draft → Review → Approved → Done; in Open facts one task per row of `open-facts.md` (`python scripts/clients.py facts <slug>` builds the payload). Use the bulk operation, one call per list; record the task ids in `status.json`.
3. **Drive**: the client's Drive folder with `consents/`, `character-sheet/`, `data/`, `deliverables/`, `briefs/`; link it from `accounts.md`. Nothing from these folders is committed.
4. **Reviews on the calendar**: each stage's sign-off meeting, the Stage 4 retrospective, the thirty-day review after go-live, the case-writing window; as calendar events with the approver invited, via the calendar connector when present.
5. **Scheduled tasks**: when the marketing loop is in scope, confirm the client is picked up by the five department tasks (they iterate `clients/*/accounts.md`); nothing new is scheduled per client.
6. **Hand the keys**: one line in `README.md` naming who in the practice owns the workspace (account manager), who approves (from the front page of the persona bible once it exists), and where the signed proposal lives.

## Output

The folder, the lists, the Drive links, the calendar events, `status.json`, and one line: client · stages · lists created · reviews booked · what is "to confirm" and who confirms it · next step, the first in-scope stage's skill. Then stop; the front door reruns the card.

## Rebuilding elsewhere

The same steps run in another account from the repo alone: clone, `templates/client/`, `setup/clickup-engagement.json`, the connectors listed in `setup/plugins-and-connectors.md`. That is the migration path in `docs/migration.md`.
