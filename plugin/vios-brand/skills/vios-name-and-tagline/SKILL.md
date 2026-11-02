---
name: "vios-name-and-tagline"
description: "Run the deep brand interrogation, extract the keyword set, and develop and test brand name candidates and a tagline for a Vios F&B client, with a documented decision (including the decision not to adopt a tagline). VIOS Practice Stage 1 steps 12–13. Use when a client needs a name, a rename, a tagline, a sub-brand or offer-line name, or when the strategy feels thin and needs the eleven deep questions as a diagnostic."
---

# Vios Name and Tagline

Steps 12 and 13: the brand's surface, reached only after the strategy is settled. The name and the tagline are tested against the strategy, never chosen for their sound alone. Hard lines: `vios-core:vios-guardrails` (3 for price words in taglines, 9 for claims).

**Work in six steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before the user has seen the step that writes it (status.json and open-facts.md bookkeeping aside). Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **The deep interrogation** (Step 1): which of the eleven answers are on file, at length, in the owner's words; which are open. Writes the archive. Ask: *"Are the open answers coming from the owner now, or does the keyword set wait for them?"*
2. **Keyword set** (Step 2): the ranked keywords with their source. Ask: *"Any word the brand would miss that is not here?"*
3. **Long list** (Step 3): candidates per technique, local languages first. Ask: *"Any technique to push further before the short list?"*
4. **Short list** (Step 4): 3–5 names with the strategy tests, then the practical tests. Ask: *"Any name to add or strike before ownership is checked?"*
5. **Tagline** (Step 5): the concepts with their tests, or the no-tagline recommendation. Ask: *"Tagline, two-line system, or none?"*
6. **Decision record** (Step 6): the recommendation and the owner's decision, or *to confirm*. Writes the book's Part 5, the archive and the PDF. Ask: *"Read it. Change anything before the PDF?"*

**Ask only when necessary; never invent.** The owner's interrogation answers are never drafted by the practice: an open answer is a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and, when it blocks the next action or the stage from closing, a blocker in `status.json`, and the keyword set draws only on the answers that exist. The decision is the owner's: until it is given, the record says *to confirm* with the recommendation beside it. Ownership (domain, trademark, handles) is written only with the date it was checked; unchecked is *to confirm*, never assumed free. Competitor names come from the audit, place names and the venue's history from the files or the user. A gap that stops a step and that the user can answer now is one question; any other gap is a row and the step goes on.

**After every step:** write the file → update `clients/<slug>/status.json` (deliverable "Name and tagline": draft → review → approved → done, blockers added or removed, `next_action`, `updated`) → move the ClickUp task (id in `status.json` › `clickup`; draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 6: `python scripts/clients.py pdf <slug> archive/naming.md "<Client>-Name-and-Tagline-vN"` (the decision record on the first page, the long list and scores after it) and send the PDF to the user. The user forwards it; the practice never emails a client.

## Read first

- `../../references/stage-1-brand-strategy.md` § 2.1.2.12, 2.1.2.13 and pattern S1-05. The eleven questions, the five techniques and the tests are there verbatim.
- `../vios-brand-diagnosis/references/worksheets.md` › Expression worksheets 3 and 4 (keywords | ideas tables).
- `[client]/diagnosis.md` (archetype and Brand Role, positioning, audience, competitor names) and `[client]/brand-book.md` › Messages and story if written (the keyword set should echo the core messages).
- Not before the positioning reads as one claim. A name chosen on an unsettled strategy is renamed within two years.

## Step 1 — The deep interrogation (11 questions, at length)

Ask the owner the eleven questions from § 2.1.2.12, one at a time, in the owner's language. Answers are paragraphs, not phrases; "the language of marketing" is sent back (pattern S1-05: if an answer reads like an About page, the interrogation was performed, not conducted). Record verbatim in `[client]/archive/deep-interrogation.md`.

Diagnostic use: if the owner cannot answer at length, stop and say which earlier step is thin. That is a finding, not a failure of this skill.

## Step 2 — Keyword set

Mine the answers for words, phrases and ideas the owner keeps returning to. Add the experience keywords from the differentiator, the audience's own words from the persona, and the short names of the core messages. Rank by recurrence and by how well each survives the test "would the brand still recognise itself if this word were gone". Output: 15–30 keywords in the worksheet-3 table, each with where it came from.

## Step 3 — Long list (names)

Generate candidates per technique, at least three each, in the worksheet table:

| Technique | What it does |
| --- | --- |
| Literal | a keyword used directly |
| Morphology | a keyword modified: ending, prefix, local form |
| Combination | two keywords joined |
| Metaphor | a word that stands for the brand |
| Abstraction | a coined word with the keyword's sound or rhythm |

Local languages first (BG, GR), then EN. Place names and the venue's own history count as keywords (an old station name attached to the site is a keyword, not a coincidence; `plugin/vios-core/references/worked-examples.md` › E6).

## Step 4 — Short list, tested against strategy

Score each candidate yes/no on: archetype and Brand Role fit · positioning fit · personality expression fit (would the imagined person introduce themselves this way) · audience register. Only then the practical tests: pronounceable in every operating language · distinct from every competitor in the audit · ownership (domain, trademark class 43, social handles; checked only on the strategic short list, never on the long list) · **the repetition test**: say it fifty times in fifty operational contexts (phone booking, delivery bag, a review, a staff T-shirt, a 3 a.m. invoice) and it still holds. Short list: 3–5 names with the table.

## Step 5 — Tagline (optional by design)

Same keyword-driven process into the worksheet-4 table: keyword | tagline concept. Tests: everything in step 4, plus **one thing**: placed next to the name it reads as one idea, not two phrases. A tagline is a plain claim the brand can keep for years; no superlatives, no price, no pressure (guardrails 1, 3). Consider the **two-line system** (`plugin/vios-core/references/worked-examples.md` › E7): a lockup tagline for the identity, three nouns or fewer that categorise in two seconds, and an editorial tagline for story-facing use that carries the brand belief; both must pass the one-thing test next to the name, each in its own place. If no concept carries the conviction the rest of the strategy has, the recommendation is **no tagline**, documented. A weak tagline harms more than none.

## Step 6 — Decision record

Chosen name, the reasoning, the rejected short-list names with the test each failed, ownership status with the date it was checked, the tagline or the no-tagline decision. Written to `[client]/brand-book.md` › Part 5 (name and tagline) and `[client]/archive/naming.md` (long list, scores). The owner decides; this skill recommends.

## Output

1. Deep interrogation answers (archive).
2. Keyword set with sources.
3. Long list by technique.
4. Short list with the strategy and practical test table.
5. Tagline concepts with tests, or the no-tagline recommendation.
6. Decision record.

End with one line: the recommended name, the tagline or "no tagline", what is "to confirm" and who confirms it (the owner's decision above all), and the next step (`vios-brand-book` to assemble, or designer selection per § 2.1.2.14). Then stop.

## Example (placeholders)

Keyword set fragment: *together · made here · proper · the table · worth the trip · the old station*. Long list, combination: "Table & Tank"; metaphor: "Gara"; morphology (BG): a coined form of the station's old name. Short list test: "Table & Tank" fails distinctiveness (a taproom in the audit uses "Tank"); "Gara" passes strategy, fails ownership (handle taken, trademark in class 43 live). Tagline concepts: "We cook for beer. We brew for food." passes the one-thing test next to the name; "Sofia's best craft evening" fails guardrails 1 and the conviction test. Worked from a real naming: `plugin/vios-core/references/worked-examples.md` › E8.
