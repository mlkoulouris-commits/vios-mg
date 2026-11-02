---
name: "vios-intake"
description: "Run the VIOS Practice intake protocol for a prospective F&B client: the initial conversation (four questions), scoping against the four stages, the pull from the pattern library, the engagement timeline, and the intake record that opens the project workspace. VIOS Practice section 5.3. Use for a first call, a discovery meeting, 'is this a client for us', or before any proposal is written."
---

# Vios Intake

The six moves at the start of an engagement, from the first conversation to the formal opening of the workspace. Half a day to two days of practitioner time. An engagement that skips this slides from conversation into work and drifts; the intake's small cost prevents the large one. Hard lines: `vios-core:vios-guardrails` 10 (named approver from day one), 12 (client data stays private).

**Work in six steps, one per move. Stop after each and ask one question.** Each step shows at most ten plain lines; no fact numbers, no section references, no file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written before the user has seen the step that writes it, except `status.json` and `open-facts.md` bookkeeping.

## Steps

1. **The conversation** (move 1): the four answers in the founder's words, whether the method can serve the brief, and the client's folder name (new or existing). Ask: *"Are these the founder's words as given?"*
2. **Scope** (move 2): stages in / out / part, briefs, partners, marketing loop, as a checklist; under it the founder's answer to *"what should be different in 90 days, in numbers?"* as up to four lines (measure · today's number or "to measure" · wanted). Ask: *"Is this the scope, and are these the numbers the founder named?"*
3. **Starting set** (move 3): patterns, library entries, templates, closest prior case. Ask: *"Keep, add or drop any?"*
4. **The intake record** (move 4): the record's lines and the open-facts rows as they will be written, approver named. Ask: *"Is this the record, with this approver?"*
5. **Timeline** (move 5): the dates as one short table. Ask: *"Dates right? Set any 'to confirm' now, or leave for the founder."*
6. **Confirm and begin** (move 6): what the founder has confirmed in writing, and where. Ask: *"Confirmed on the record, or does it wait for the proposal?"*

## Ask only when necessary; never invent

- The founder's four answers, the scope ratification and the move 6 confirmation are the founder's words, never drafted by the practice. Founder absent → the step records **"not held"**, a row in `[client]/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker in `status.json`; the record says *to confirm* with the question.
- Approver (hard line 10), dates, partners, prices: only from the call, the files or the user. A missing one is one question if the step cannot proceed, otherwise "to confirm" and a row. A question is asked once; never ask what `status.json`, `open-facts.md` or an existing `[client]/` already answers.

## After every step

Write the step's lines into `[client]/README.md` › Intake record (new client: `python scripts/clients.py new <slug> "<Name>"` once, after step 1, which creates the folder, `status.json` and `open-facts.md`; an existing folder is updated). Then `status.json`: `current_stage` "0 intake", approver, `marketing_loop`, each stage's scope, blockers, `next_action`, `updated`. Then the ClickUp task "Intake <Client>" in the client's Deliverables list (ids in `setup/clickup.json`): **draft** while writing, **review** at step 6, **approved** on the founder's confirmation. No client PDF by default; when the founder confirms from the record itself rather than the proposal, `python scripts/clients.py pdf <slug> README.md "<Client>-Intake-v1"` at step 6 and hand the PDF to the user.

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.2 (the three layers) and § 5.3 (the intake protocol), verbatim.
- `vios-core:vios-guardrails` › client file convention: the workspace this intake opens.
- `[client]/` if a folder already exists (a marketing-only client coming into a Practice engagement): read it before the call, and `python scripts/clients.py status <slug>`.

## Move 1 — The initial conversation

Four questions, asked and answered in the founder's own words, recorded verbatim: what are you trying to build · what stage are you at and what is the timeline · which partners are already engaged (architect, designer, chef, operator) · what outcome would make this worth the investment. Listen for whether the brief is one the method can serve. A brand-book-only brief is a partial brief the practice can take with the scope adjusted; a founder who wants the room designed around a concept that does not exist yet is not ready. Say which, plainly.

## Move 2 — Scope against the four stages

Three questions: which stages are in scope, in full or in part (1 brand strategy and book · 2 journey map · 3 journey design · 4 training) · which briefs will be generated (designer, architect, interior, operations) · which partners execute the work the practice does not. Output: a one-page scope summary, over-named rather than under-named, ratified by the founder before anything begins. The marketing loop (`vios-marketing`) is named as in or out of scope on the same page.

A fourth question closes the move: **"What should be different in 90 days, in numbers?"** The founder names up to four measures in their own words (covers, average check, Google rating, bookings through our own channel, reach, labour %, a wait time, a review theme that must disappear). Each is written as measure · today's number as the founder says it, or "to measure" · what they want. Nothing is promised here: the baseline (`vios-engagement-setup` step 7) sets today's number, `vios-proposal` step 3 turns the wanted numbers into the KPI table the proposal carries. A founder who cannot name a number is recorded as such ("outcome: not named") and the proposal's KPI table says "set at baseline"; never invent a target for them.

## Move 3 — Pull from Layer 2

Consult what the practice already holds: the Patterns sections of each stage chapter, the candidate patterns in `docs/dry-run-*.md` harvest entries, the two libraries, the templates, the worked examples. Record a **starting set** for this engagement: the patterns likely to apply, the library entries that match the concept, the templates to reuse, the closest prior case. Not binding; the engagement may deviate and say why.

## Move 4 — Open the project workspace

Create `[client]/` from `templates/client/` (`vios-engagement-setup` does the folders, ClickUp and Drive). Write the **intake record** as `[client]/README.md`'s first section: brief summary, scope summary, starting set, timeline, named approver, working rhythm. It is the workspace's table of contents and is updated as the engagement moves.

## Move 5 — The engagement timeline

When Stage 1 begins, when each stage's working sessions fall, when partner briefs issue, when reviews happen, when the engagement closes, plus two dates most practices forget: the engagement-level retrospective at the end of Stage 4, and the case-writing window three to six months after close. Approximate, but firm enough that founder, partners and practice work at the same pace.

## Move 6 — Confirm and begin

The founder confirms scope, timeline, starting set and rhythm in writing (a dated line in the intake record, or the signed proposal from `vios-proposal`). Then the engagement begins with `vios-brand:vios-brand-diagnosis`, or at the first in-scope stage.

## Output

1. `[client]/README.md` › Intake record (the six moves, dated).
2. `[client]/open-facts.md` opened with the first rows: what the founder could not answer on the call.
3. `[client]/status.json` created or updated, the ClickUp intake task moved.
4. One line to the account manager: in scope / out of scope / not ready, what is "to confirm" and who confirms it, and the next step (`vios-proposal`). Then stop; the front door reruns the card.

## Example (placeholders)

Brief: a second counter-format gelato shop plus a B2B line. Scope: Stage 1 revision pass (book exists), Stages 2–3 for the new shop, Stage 4 onboarding, marketing in scope. Briefs: interior designer, operations. Partners: the client's architect. Starting set: the counter-format variant (small-format page), the two-moment end, the by-weight onboarding plan, section 3.1 entries 1, 7, 10, 17. Timeline: eight weeks, retrospective in week 9, case window April. Not answered on the call: counter height, allergen policy, Ring Mall hours (three rows in `open-facts.md`). Worked from a real intake: `plugin/vios-core/references/worked-examples.md` › E2.
