---
name: "vios-brand-book"
description: "Assemble or revise the VIOS brand book for an F&B client from the Stage 1 outputs (diagnosis, messages and story, journey, persona bible, name and tagline, identity notes) into the house structure Why → Who → Soul → Story → Voice → Look → Use → Govern, with the Brand Wheel, the AI Persona Brief annex and the designer brief, then run the designer-selection checklist. VIOS Practice Stage 1 § 2.1.3, 2.1.2.14, 2.1.6. Use when a client needs a brand book, brand guidelines, a new edition of their book, a designer brief, or help choosing a designer."
---

# Vios Brand Book

The deliverable of Stage 1: the strategy organised for use, not a stack of worksheets. Read by the practice in later stages, by the designer, the architect, the floor and the founder. It governs the visual identity; it does not contain it until the designer delivers. Hard lines: `vios-core:vios-guardrails` 6 (disclosure set), 7 (consents), 10 (approver).

## Read first

- `../../references/brand-book-structure.md`: the part order, what each part holds and where it comes from. Follow it.
- `../../references/stage-1-brand-strategy.md` § 2.1.3 (deliverable rules), § 2.1.2.14 (designer selection), § 2.1.6 (briefs), § 2.1.7 (harvest).
- The client folder: `diagnosis.md`, `persona-bible.md`, `brand-book.md` (Messages and story, Journey), `fact-sheet.md`, `archive/` (naming, interrogation), `character-sheet/`. A previous edition of the book, if any: the new edition states what changed.

## Principles

- **Synthesis, not worksheets.** Worksheet form stays in `archive/`; the book carries the answers organised for use.
- **Nothing invented.** A section without a source is written as **to confirm** with the question the owner must answer. The book is finished when the fourteen interrogations resolve consistently, not when every box has text.
- **Guest is the hero, brand is the guide.** Part 0 states it; every part obeys it.
- **Direction, not identity.** Part 6 holds Brand Identity Notes and the reference set until the designer delivers; then the delivered system replaces it and the edition number moves.
- **Neutral register**, except the manifesto in the brand's voice.
- **One Brand Wheel** closes the book: essence, rational and emotional attributes, positioning, key messages, personality, on one page.

## Workflow

1. **Inventory.** List every source file with its version and date; mark what is missing. Missing diagnosis → stop, `vios-brand-diagnosis`. Missing messages → `vios-messages-and-story`. Missing persona → `vios-persona-builder` (the book can be issued as "Part 5 to confirm", say so). Name undecided → `vios-name-and-tagline`, or the book uses the working name and flags it.
2. **Run the closing test** from § 2.1.2 "Closing the sequence" across the inventory: differentiator solves the pain; Role answers the audience's personality desires; archetypal mixes produce a relationship the audience accepts; positioning uses the differentiator; story casts a hero this brand can guide. A failed check names the step to revisit before assembly.
3. **Assemble** Parts 0–8 and Annex A per the structure reference. Each section carries its source step in a footnote line. Where the practice's house examples (Stochna V2, Atelier v3) show a better section shape, use it and keep the wording the client's.
4. **Brand Wheel** on one page, last.
5. **Designer selection** (if a visual identity is in scope): apply the six criteria from § 2.1.2.14 (processes, language, variation, style guide, interview, the brief) to each candidate, as a table; recommend; the owner chooses.
6. **Designer brief** (Annex B): one-paragraph brand summary · what the identity must achieve · what the brand refuses · what the brand is indifferent to (name it; it gives the designer the field) · applications (signage, menu, digital, print, packaging, staff) · constraints from the room · the Brand Identity Notes reproduced · review and revision protocol with versioning. Four to eight pages plus the book as appendix. Architect and interior-designer briefs follow the same six-section structure when the engagement has a room; see § 2.1.6.
7. **Govern.** Part 8 names the approver, the AI disclosure set, the consent rule, the edition, date and next review. Version the file: `[client]/brand-book-vN.md` for the book, `brand-book.md` stays the live summary the operating skills read (identity table, Messages and story, Journey).
8. **Harvest** (§ 2.1.7): one hour at close. New patterns in the standard form (when to use, what it produces, what it asks, failure mode), framework revisions suggested, which Persona in Practice layers held or were thin. Written to `[client]/archive/harvest-stage-1.md` and proposed for the manuscript's next version.

## Output

- The book as a Claude Doc deliverable "<Client> — Brand Book vN (date)" when the docs connector is present, otherwise `[client]/brand-book-vN.md`; the live `brand-book.md` updated to point at it and carry the summary tables.
- Annex A (AI Persona Brief) and Annex B (designer brief) as separate docs, since they go to different readers.
- The designer selection table, if in scope.
- The harvest note.

End with: edition, what changed, what is "to confirm" and who confirms it, and the next stage (`vios-journey` when it exists; until then the journey table is completed by the account manager by hand).

## Checks before issue

Hero/Guide rule stated and obeyed · every section sourced or marked to confirm · no worksheet wording · no finished copy inside message blocks · Part 6 marked direction unless the designer delivered · disclosure set present where an AI persona exists (guardrails 6) · approver named (guardrails 10) · Brand Wheel present · edition and date on the cover · previous edition's changes listed in Part 0.
