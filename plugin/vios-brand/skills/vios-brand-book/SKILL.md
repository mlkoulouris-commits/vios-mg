---
name: "vios-brand-book"
description: "Assemble or revise the VIOS brand book for an F&B client from the Stage 1 outputs (diagnosis, messages and story, journey, persona bible, name and tagline, identity notes) into the house structure Why → Who → Soul → Story → Voice → Look → Use → Govern, with the Brand Wheel, the AI Persona Brief annex and the designer brief, then run the designer-selection checklist. VIOS Practice Stage 1 § 2.1.3, 2.1.2.14, 2.1.6. Use when a client needs a brand book, brand guidelines, a new edition of their book, a designer brief, or help choosing a designer."
---

# Vios Brand Book

The deliverable of Stage 1: the strategy organised for use, not a stack of worksheets. Read by the practice in later stages, by the designer, the architect, the floor and the founder. It governs the visual identity; it does not contain it until the designer delivers. Hard lines: `vios-core:vios-guardrails` 6 (disclosure set), 7 (consents), 10 (approver).

## Read first

- `../../references/brand-book-structure.md`: the two formats (A, interrogation order, the engagement deliverable; B, Why → Govern, the team edition derived from A), what each part holds and where it comes from. Follow it; Format A unless the brief asks for the team edition as well.
- `../../references/stage-1-brand-strategy.md` § 2.1.3 (deliverable rules), § 2.1.2.14 (designer selection), § 2.1.6 (briefs), § 2.1.7 (harvest).
- The client folder: `diagnosis.md`, `persona-bible.md`, `brand-book.md` (Messages and story, Journey), `fact-sheet.md`, `archive/` (naming, interrogation), `character-sheet/`. A previous edition of the book, if any: the new edition states what changed.

## Principles

- **Synthesis, not worksheets.** Worksheet form stays in `archive/`; the book carries the answers organised for use.
- **Nothing invented.** A section without a source is written as **to confirm** with the question the owner must answer. The book is finished when the fourteen interrogations resolve consistently, not when every box has text.
- **Guest is the hero, brand is the guide.** Part 0 states it; every part obeys it.
- **Direction, not identity.** Part 6 holds Brand Identity Notes and the reference set until the designer delivers; then the delivered system replaces it and the edition number moves.
- **Neutral register**, except the manifesto in the brand's voice.
- **One Brand Wheel** closes the book: essence, rational and emotional attributes, positioning, key messages, personality, on one page.

**Work in seven steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before the user has seen the step that writes it (status.json and open-facts.md bookkeeping aside). Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Inventory.** List every source file with its version and date; mark what is missing. Missing diagnosis → stop, `vios-brand-diagnosis`. Missing messages → `vios-messages-and-story`. Missing persona → `vios-persona-builder` (the book can be issued as "Part 5 to confirm", say so). Name undecided → `vios-name-and-tagline`, or the book uses the working name and flags it. Show the inventory as one line per source. Ask: *"Assemble on this inventory, or fill a gap first?"*
2. **Run the closing test** from § 2.1.2 "Closing the sequence" across the inventory: differentiator solves the pain; Role answers the audience's personality desires; archetypal mixes produce a relationship the audience accepts; positioning uses the differentiator; story casts a hero this brand can guide. A failed check names the step to revisit before assembly. Show the five verdicts. Ask: *"Any failed check to send back before assembly?"*
3. **Assemble** per the structure reference: Format A sections 1–13 with the foreword (version history, what changed since the last edition, what did not), the positioning as a working tool with three or four proposals it rejects, tone-by-moment under the messages, the brand belief deployed under the story, the two-line tagline system under the name, the coherence test as a question/verdict table, the engagement notes with closed / still open / provisional. Then Format B if asked. Annex A in both. Each section carries its source step in a footnote line. Where the practice's house examples (Stochna V2, Atelier v3) show a better section shape, use it and keep the wording the client's. **Brand Wheel** on one page, last. Show the table of contents with each section's state (sourced · to confirm) and the Wheel in brief; this step writes the draft book. Ask: *"Format A only, or B as well, and anything to change before Govern?"*
4. **Designer selection** (if a visual identity is in scope): apply the six criteria from § 2.1.2.14 (processes, language, variation, style guide, interview, the brief) to each candidate, as a table; recommend; the owner chooses. Show the table. Ask: *"Which designer, or does the owner choose?"*
5. **Designer brief** (Annex B): one-paragraph brand summary · what the identity must achieve · what the brand refuses · what the brand is indifferent to (name it; it gives the designer the field) · applications (signage, menu, digital, print, packaging, staff) · constraints from the room · the Brand Identity Notes reproduced · review and revision protocol with versioning. Four to eight pages plus the book as appendix. Architect and interior-designer briefs follow the same six-section structure when the engagement has a room; see § 2.1.6. Show the eight headings with one line each; this step writes the brief. Ask: *"Read the brief. Change anything before its PDF?"*
6. **Govern** and issue. Part 8 names the approver, the AI disclosure set, the consent rule, the edition, date and next review. Version the file: `[client]/brand-book-vN.md` for the book, `brand-book.md` stays the live summary the operating skills read (identity table, Messages and story, Journey). **Revision pass** (v2.1 pattern): when Stage 3, Stage 4 or a marketing review surfaces operating facts, write them into section 11, add one coherence row per addition, update the engagement notes and move the edition number; the strategy sections stay unless a coherence row fails. Show Part 8 and the checks before issue; this step issues the book. Ask: *"Read the book. Change anything before the PDF?"*
7. **Harvest** (§ 2.1.7): one hour at close. New patterns in the standard form (when to use, what it produces, what it asks, failure mode), framework revisions suggested, which Persona in Practice layers held or were thin. Written to `[client]/archive/harvest-stage-1.md` and proposed for the manuscript's next version. Show the patterns, one line each. Ask: *"Anything to add to the harvest?"*

**Ask only when necessary; never invent.** The approver, the designer the owner chooses, the consent signatories and any section whose source file is missing are never drafted by the practice: the section says *to confirm* with the question the owner must answer, a row goes to `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker to `status.json`. Edition numbers, dates, the working name and the room's constraints come only from the files or the user. A gap that stops a step and that the user can answer now is one question; any other gap is a row and the step goes on.

**After every step:** write the file → update `clients/<slug>/status.json` (deliverables "Brand book" and "Designer brief": draft → review → approved → done, blockers added or removed, `next_action`, `updated`) → move the ClickUp task (id in `status.json` › `clickup`; draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 5: `python scripts/clients.py pdf <slug> <designer-brief.md> "<Client>-Designer-Brief-vN"`; at step 6: `python scripts/clients.py pdf <slug> brand-book-vN.md "<Client>-Brand-Book-vN"`; send each PDF to the user. The user forwards it; the practice never emails a client.

## Output

- The book as a Claude Doc deliverable "<Client> — Brand Book vN (date)" when the docs connector is present, otherwise `[client]/brand-book-vN.md`; the live `brand-book.md` updated to point at it and carry the summary tables.
- Annex A (AI Persona Brief) and Annex B (designer brief) as separate docs, since they go to different readers.
- The designer selection table, if in scope.
- The harvest note.

End with one line: edition, what changed, what is "to confirm" and who confirms it (every one a row in `[client]/open-facts.md`, the engagement's chase list: fact · what it blocks · who holds it · asked on · due), and the next stage (`vios-journey:vios-journey-map`). Then stop.

## Checks before issue

Hero/Guide rule stated and obeyed · every section sourced or marked to confirm · no worksheet wording · no finished copy inside message blocks · Part 6 marked direction unless the designer delivered · disclosure set present where an AI persona exists (guardrails 6) · approver named (guardrails 10) · Brand Wheel present · edition and date on the cover · previous edition's changes listed in Part 0.
