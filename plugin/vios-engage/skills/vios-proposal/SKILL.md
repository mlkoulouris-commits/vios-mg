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

Show both as two short tables. Ask: *"Dates and prices right? Set any 'to confirm' now, or leave for the owner."* A price the user sets here goes into the proposal, not into the rate card; say so.

## Step 4 — The proposal doc

Now write the Claude Doc "<Client> — Proposal v1 (date)" via the docs connector (or `[client]/proposal-v1.md`), 4–8 pages:

1. **What you told us** (one paragraph in the founder's words, from move 1 of the intake).
2. **What we propose**: the stages from step 1, deliverables from step 2, approver per stage. Out of scope named.
3. **What you supply**: the "client supplies" column, by stage.
4. **Timeline**: from step 3, with the retrospective and the case window shown.
5. **Price**: from step 3, one total, terms.
6. **How we work**: one writer per deliverable, named sign-off at each stage, drafts never published, the client's data stays in the client's workspace, the harvest at close and what the practice keeps (patterns, never the client's material).
7. **Signature block**: founder, practice, date; the signed proposal is the confirmation of move 6 of the intake.

Ask: *"Read the doc. Change anything before the client PDF?"*

## Step 5 — The client PDF

"<Client> — What you get" (1–2 pages), from `templates/proposal/deliverables-sheet.md` filled with steps 1–3: deliverables table, what the client supplies, timeline, total, signature line. No method prose, no practice history. Render with the Adobe `markdown_to_pdf` tool (fallback: hand the filled markdown to the user to print) and save as `[client]/proposal-v1-deliverables.pdf` beside the markdown.

Then: a line in `[client]/README.md` › Intake record pointing at the doc and the PDF with status (sent · signed · declined · superseded), and the ClickUp task "Proposal <Client> — awaiting signature" in the department's setup list. The user sends the PDF; the practice never emails a client.

## Rules

- Prices come only from `setup/rate-card.md` or the user's word in step 3. A stage on neither is "to confirm with the practice owner".
- Language: the founder's working language; BG and EN both when the founder asks. The PDF is in the founder's language only.
- The filter test applies to our own copy: no superlatives about the practice, no urgency.
- A new version (v2, v3) restarts at step 1 with the previous answers pre-filled.

## Output

End with one line: stages, total price or "prices to confirm", where the doc and PDF are, and the next step (`vios-engagement-setup` on signature).
