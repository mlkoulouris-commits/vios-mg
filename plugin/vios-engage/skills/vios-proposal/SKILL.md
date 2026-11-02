---
name: "vios-proposal"
description: "Write the engagement proposal for a Vios F&B client from the intake record, in five short steps with a check-in after each: scope, deliverables, timeline and price, the proposal doc the founder signs, and a one-page client PDF listing what they get. Use after vios-intake whenever a client needs a proposal, a quote, a scope letter, or 'what would this cost and when'."
---

# Vios Proposal

The scope summary from the intake, turned into the document the founder signs and a one-page PDF the founder reads. One proposal per engagement; a change of scope is a new version, never a silent extension. Hard lines: `vios-core:vios-guardrails` 1 and 3 (no pressure, no fake anchors, in our own selling too), 10, 12.

**Work in five steps. Stop after each and ask one question. Write nothing to disk before step 4.** "All good" or "skip" moves to the next step; "all good to the end" runs the rest without stopping.

## Read first

- `[client]/README.md` › Intake record: brief, scope, starting set, timeline, approver. `[client]/open-facts.md` for what the founder could not answer.
- `setup/rate-card.md`: the practice's prices per stage and per brief, the day rate, the travel rule, the payment terms. **No rate card on file: every price reads "to confirm" and the output line says so; never invent a price.**
- `[client]/data/baseline-*.md` and `status.json` › `baseline` when they exist (a client already in the marketing loop, or a diagnostic sprint done first): today's numbers for the KPI table. Not on file: the table's baseline column reads "measured in week 1".
- `vios-core:vios-guardrails` › Shared numbers: *n*, early reads, and the outcome-KPI attribution rule the table must follow.
- `../../references/parts-4-5-examples-and-production.md` § 5.3 move 2 (scoping) and the stage chapters' deliverable sections (what each stage actually hands over).
- `templates/proposal/deliverables-sheet.md`: the client PDF layout.

## Step 1 — Confirm scope

Show the intake's scope summary as a checklist, one line per item, in / out:

- Stage 1 brand strategy and book (full · revision pass) · Stage 2 journey map · Stage 3 journey design · Stage 4 training (onboarding plan · full programme)
- Partner briefs: designer · architect · interior · operations
- Marketing loop (`vios-marketing`)

Ask: *"Is this the scope? Tick or strike."* Out-of-scope items stay on the list marked **out**; the proposal names them as plainly as what is in.

## Step 2 — Deliverables

One table, one row per in-scope stage, deliverables named exactly as the practice ships them:

| Stage | Deliverables | Approver | Client supplies |
| --- | --- | --- | --- |
| 1 | brand book Format A, Persona Bible, designer brief | | founder's time, menus, prices, existing material |
| 2 | journey map, Reasoning Note, handoff | | the room (plan or visit), partner contacts |
| 3 | design pages, choreography, recovery document, operations brief | | POS data, allergens, service hours |
| 4 | training plan or programme, handoffs, retrospective | | staff list, shift pattern |
| marketing | calendar, copy, QA, ads, monthly report | | consents, accounts, ad budget |

Approver from the intake record (hard line 10). "Client supplies" from the intake's open facts, the facts and access without which a stage cannot close.

Ask: *"Rename, add or drop any deliverable?"*

## Step 3 — Timeline and price

Timeline from the intake (move 5): stage start dates, partner briefs, reviews, close, the retrospective, the case window.

Price per stage and per brief from `setup/rate-card.md`; day rate for anything outside scope; travel; payment terms (deposit, per stage on sign-off). One total. No discounts invented to close; a price reduction is a scope reduction, named in step 1.

**What we aim to move.** A third table, from the intake's 90-day numbers (move 2, fourth question): at most four rows.

| KPI | Today | In 90 days | How we measure it |
| --- | --- | --- | --- |
| covers per month | baseline figure, or "measured in week 1" | the founder's wanted number, or a step the practice can stand behind | source · monthly · n rule |

Rules of the table: every KPI has a source the practice can read every month (Memento, POS export, GBP, Metricool, the booking book); "today" comes from the baseline page or reads "measured in week 1" ("measured in month 1 after opening" for a venue not yet trading); the number the founder claimed at intake stays in the intake record and never fills "today"; "in 90 days" is the founder's own number when they named one, otherwise the practice proposes one step (never a multiple) and says it is a proposal, or reads "set at baseline" with the reasoning in `kpis[].target_note`; a KPI nobody can measure monthly is dropped from the table and named under it in one line, *"Not promised: <KPI>, no monthly source"*, with an open-facts row when a source could be built. Under the table one sentence, fixed: *"We report these every month against the baseline, with the sample size beside each figure; we say where we contributed and we do not claim to have caused a number on our own."* The 90 days run from go-live, the date written in the table's heading: the first published post for a marketing client, the first stage sign-off for a practice-only engagement, or opening day for a venue not yet trading.

**Diagnostic sprint** (rate card; only when the line exists there, and only for a venue that trades, since it reads a baseline and reviews): offered when the founder is not ready to sign the stages, or cannot name a number. Two weeks, the baseline page plus review mining plus a one-page findings note, credited against Stage 1 when signed within 30 days. Shown as one extra line in the price table, never pushed (hard line 1).

Show the three tables. Ask: *"Dates, prices and the four KPIs right? Set any 'to confirm' now, or leave for the owner."* A price the user sets here goes into the proposal, not into the rate card; say so.

## Step 4 — The proposal doc

Now write the Claude Doc "<Client> — Proposal v1 (date)" via the docs connector (or `[client]/proposal-v1.md`), 4–8 pages:

1. **What you told us** (one paragraph in the founder's words, from move 1 of the intake).
2. **What we propose**: the stages from step 1, deliverables from step 2, approver per stage. Out of scope named.
3. **What you supply**: the "client supplies" column, by stage.
4. **What we aim to move**: the KPI table from step 3, the go-live date, the fixed attribution sentence, the "Not promised" line when a KPI was dropped.
5. **Timeline**: from step 3, with the retrospective and the case window shown.
6. **Price**: from step 3, one total, terms; the diagnostic sprint line when offered.
7. **How we work**: one writer per deliverable, named sign-off at each stage, drafts never published, the client's data stays in the client's workspace, the harvest at close and what the practice keeps (patterns, never the client's material).
8. **Signature block**: founder, practice, date; the signed proposal is the confirmation of move 6 of the intake.

Ask: *"Read the doc. Change anything before the client PDF?"*

## Step 5 — The client PDF

"<Client> — What you get" (a cover and up to three pages), from `templates/proposal/deliverables-sheet.md` filled with steps 1–3: deliverables table, what the client supplies, the KPI table with its sentence, timeline, total, signature line. No method prose, no practice history. Write `[client]/proposal-vN-deliverables.md` and render it with `python scripts/clients.py pdf <slug> proposal-vN-deliverables.md "<Client>-What-you-get-vN"` → `[client]/deliverables/`.

Then: `status.json` › `proposal` (`version` N, `status` sent, `doc`, `pdf`; the previous version moves into `proposal.history[]` as superseded) and `kpis` written from the table (name, baseline, target, target_note where used, due, how_measured, attribution "contribution") so the monthly report and the harvest read the same promise; a line in `[client]/README.md` › Intake record pointing at the doc and the PDF; and the ClickUp task "Proposal <Client> vN — awaiting signature" in the client's Deliverables list (Stage = Engagement, Approver = the founder), **review** until signed. The user sends the PDF; the practice never emails a client.

## Rules

- Prices come only from `setup/rate-card.md` or the user's word in step 3. A stage on neither is "to confirm with the practice owner".
- Language: the founder's working language; BG and EN both when the founder asks. The PDF is in the founder's language only.
- The filter test applies to our own copy: no superlatives about the practice, no urgency.
- A KPI target is a number the founder named or one step the practice proposed and labelled as such; never a guarantee, never a multiple, never a number with no monthly source. The attribution sentence is never softened or dropped.
- A new version (v2, v3) restarts at step 1 with the previous answers pre-filled.

## Output

End with one line: stages, total price or "prices to confirm", where the doc and PDF are, and the next step (`vios-engagement-setup` on signature).
