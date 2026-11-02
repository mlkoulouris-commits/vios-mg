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
4. Every client-facing deliverable also ships as a PDF in `clients/<slug>/deliverables/` (`scripts/clients.py pdf <slug> <file.md> <Title>`; headless Edge); the user forwards it, the practice never emails a client.
5. Writes nothing to disk before the user has seen the plan of the step.

## Daily use

ClickUp → what is awaiting your sign-off → approve or comment. Claude → `/vios <client>` → the status card and the next action. Forward PDFs.

## Build order

| # | Step | State |
| --- | --- | --- |
| 1 | ClickUp statuses, fields, Deliverables + Open facts lists; status.json schema; `scripts/clients.py`; Stochna + Atelier seeded | done 2026-11-02 |
| 2 | Front door `/vios <client>` (plugin `vios-engage`) | done 2026-11-02 |
| 3 | Engage skills (intake, proposal, setup, harvest) to the contract (`docs/skill-contract.md`) | 2026-11-02 |
| 4 | Brand (5) + journey (3) skills to the contract, each with a client PDF | 2026-11-02 |
| 5 | Marketing loop: the five scheduled tasks drop drafts as ClickUp tasks in Review | 2026-11-02 |
| 6 | ONE Gallery on the system; `atelier-2026-10` archived | 2026-11-02 |
| 7 | Marketing skills (calendar, voice, video, ads, report) to the contract; QA + ads-audit stay verdict skills | 2026-11-02 |
| 8 | Core lenses stay as review passes (no steps); guardrails unchanged | n/a |
| 9 | Month-0 baseline: setup step 7, `data/baseline-YYYY-MM.md`, "Baseline" column in the monthly report, `status.json` › `baseline` (`docs/quality-plan-2026-11-02.md` WS1) | 2026-11-02 |
| 10 | Outcome KPIs: intake's 90-day question, proposal's "What we aim to move" table (doc + client sheet), `status.json` › `kpis`, report prints the promise first, harvest reads it; diagnostic sprint on the rate card to confirm (quality plan WS3) | 2026-11-02 |
| 11 | Guest research: review mining, interview guide (EN/BG) and mystery visit templates in `templates/client/data/`; diagnosis step 4 opens with Guest evidence and cannot pass without review mining; the map's Move 2b takes the mystery visit as its first observation; guest research pack on the rate card to confirm (quality plan WS2) | 2026-11-02 |
| 12 | Financial lens: `vios-core/references/numbers-page.md` (definitions, Memento page per number, quadrant, cost of a moment) + `templates/client/data/numbers-page.md`; diagnosis step 1 fills it; HIGH design pages carry "Cost of the moment"; report section 4 reads marketing on its lines (quality plan WS4) | 2026-11-02 |
| 13 | Training proof: `training/certification.csv` (10-check role cards, manager signs), `training/behaviour-kpis.md` (two counts per HIGH moment, four weeks), the thirty-day register audit on the mystery-visit sheet with its score in `status.json` › stages › 4 Training › `audit`; quarterly service audit on the rate card to confirm (quality plan WS5) | 2026-11-02 |
| 14 | Proof and capacity: first case draft in the Part IV form (ONE Gallery v0.1, method case, results "to confirm"); `docs/sop.md` › Capacity and handoff; hygiene list in the quality plan (quality plan WS6) | 2026-11-02 |

## Not in scope

A web dashboard. ClickUp is the dashboard; a second app would be a second Memento to maintain.
