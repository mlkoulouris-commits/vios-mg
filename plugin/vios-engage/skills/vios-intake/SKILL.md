---
name: "vios-intake"
description: "Run the VIOS Practice intake protocol for a prospective F&B client: the initial conversation (four questions), scoping against the four stages, the pull from the pattern library, the engagement timeline, and the intake record that opens the project workspace. VIOS Practice section 5.3. Use for a first call, a discovery meeting, 'is this a client for us', or before any proposal is written."
---

# Vios Intake

The six moves at the start of an engagement, from the first conversation to the formal opening of the workspace. Half a day to two days of practitioner time. An engagement that skips this slides from conversation into work and drifts; the intake's small cost prevents the large one. Hard lines: `vios-core:vios-guardrails` 10 (named approver from day one), 12 (client data stays private).

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.2 (the three layers) and § 5.3 (the intake protocol), verbatim.
- `vios-core:vios-guardrails` › client file convention: the workspace this intake opens.
- `[client]/` if a folder already exists (a marketing-only client coming into a Practice engagement): read it before the call.

## Move 1 — The initial conversation

Four questions, asked and answered in the founder's own words, recorded verbatim: what are you trying to build · what stage are you at and what is the timeline · which partners are already engaged (architect, designer, chef, operator) · what outcome would make this worth the investment. Listen for whether the brief is one the method can serve. A brand-book-only brief is a partial brief the practice can take with the scope adjusted; a founder who wants the room designed around a concept that does not exist yet is not ready. Say which, plainly.

## Move 2 — Scope against the four stages

Three questions: which stages are in scope, in full or in part (1 brand strategy and book · 2 journey map · 3 journey design · 4 training) · which briefs will be generated (designer, architect, interior, operations) · which partners execute the work the practice does not. Output: a one-page scope summary, over-named rather than under-named, ratified by the founder before anything begins. The marketing loop (`vios-marketing`) is named as in or out of scope on the same page.

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
3. One line to the account manager: in scope / out of scope / not ready, and the next step (`vios-proposal`).

## Example (placeholders)

Brief: a second gelato atelier plus a B2B line. Scope: Stage 1 revision pass (book exists), Stages 2–3 for the new atelier, Stage 4 onboarding, marketing in scope. Briefs: interior designer, operations. Partners: the client's architect. Starting set: the counter-format variant (small-format page), the two-moment end, the by-weight onboarding plan, section 3.1 entries 1, 7, 10, 17. Timeline: eight weeks, retrospective in week 9, case window April. Not answered on the call: counter height, allergen policy, Ring Mall hours (three rows in `open-facts.md`).
