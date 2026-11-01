---
name: "vios-proposal"
description: "Write the engagement proposal for a Vios F&B client from the intake record: stages in scope with their deliverables, what the client supplies, the timeline, pricing per stage from the practice's rate card, the approver and the working rhythm, as a Claude Doc the founder signs. Use after vios-intake whenever a client needs a proposal, a quote, a scope letter, or 'what would this cost and when'."
---

# Vios Proposal

The scope summary from the intake, turned into the document the founder signs. One proposal per engagement; a change of scope is a new version, never a silent extension. Hard lines: `vios-core:vios-guardrails` 1 and 3 (no pressure, no fake anchors, in our own selling too), 10, 12.

## Read first

- `[client]/README.md` › Intake record: brief, scope, starting set, timeline, approver.
- `setup/rate-card.md`: the practice's prices per stage and per brief, the day rate, the travel rule, the payment terms. **No rate card on file: write the proposal with every price as "to confirm" and say so in the output line; never invent a price.**
- `../../references/parts-4-5-examples-and-production.md` § 5.3 move 2 (scoping) and the stage chapters' deliverable sections (what each stage actually hands over).

## Structure (one Claude Doc, 4–8 pages)

1. **What you told us** (one paragraph in the founder's words, from move 1 of the intake).
2. **What we propose**: the stages in scope, each with its deliverables named exactly as the practice ships them (Stage 1: brand book Format A, Persona Bible, designer brief · Stage 2: journey map, Reasoning Note, handoff · Stage 3: design pages, choreography, recovery, operations brief · Stage 4: training plan or programme, handoffs, retrospective · marketing loop: calendar, copy, QA, ads, monthly report), with the approver named for each.
3. **What you supply**: the facts and access without which a stage cannot close (POS data, menus, prices, allergens, consents, the room, partner contacts, the founder's time per stage). Taken from the intake's open facts.
4. **Timeline**: from the intake, with the retrospective and the case window shown.
5. **Price**: per stage and per brief from the rate card, the day rate for anything outside scope, travel, payment terms (deposit, per stage on sign-off). One total. No discounts invented to close; a price reduction is a scope reduction, named.
6. **How we work**: one writer per deliverable, named sign-off at each stage, drafts never published, the client's data stays in the client's workspace, the harvest at close and what the practice keeps (patterns, never the client's material).
7. **Signature block**: founder, practice, date; the signed proposal is the confirmation of move 6 of the intake.

## Rules

- Prices come only from `setup/rate-card.md`. A stage not on the card is "to confirm with the practice owner".
- The proposal names what is **out** of scope as plainly as what is in.
- Language: the founder's working language; BG and EN both when the founder asks.
- The filter test applies to our own copy: no superlatives about the practice, no urgency.

## Output

The Claude Doc "<Client> — Proposal v1 (date)" via the docs connector (or `[client]/proposal-v1.md`), a line in `[client]/README.md` › Intake record pointing at it with its status (sent · signed · declined · superseded), and the ClickUp task "Proposal <Client> — awaiting signature" in the department's setup list. End with one line: stages, total price or "prices to confirm", and the next step (`vios-engagement-setup` on signature).
