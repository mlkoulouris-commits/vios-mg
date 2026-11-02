---
name: "vios-brand-diagnosis"
description: "Run the Vios Marketing brand diagnosis on a new F&B client: the real business, its authentic meaning, its audience and competitors. The entry gate before any persona or content work."
---

# Vios Brand Diagnosis

The first step of every Vios Marketing engagement. Understand before acting: we sell clarity, then strategy, then execution. Nothing gets produced before this is done and signed off.

Built on the Vios Branding Tool Box (Worksheets 1–8 and 10, Brand Personality Questionnaire). The worksheets are in this skill: read `references/worksheets.md` for the exact questions in order, `references/archetypes.md` for the twelve archetypes (drive, fear, strategy, voice, message) before Step 4 and Step 7, and copy `references/competitor-audit-template.md` into the client folder for Step 5. Ask the worksheet questions in their own words; the steps below are the order and the tests.

**Work in seven steps. Stop after each and ask one question.** Each step shows at most ten plain lines; no open-fact numbers, section references or file paths on screen (those go in the file). "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before the user has seen the step that writes it (status.json and open-facts.md bookkeeping aside). Start by reading `clients/<slug>/status.json` and `open-facts.md`: what they already answer is never asked again.

## Steps

1. **Inputs and the real business** (Inputs, Step 1): what is on file of the five inputs, and the numbers page as its eight rows (size, mix, daypart, cost lines, quadrant, bookings, to confirm, reading), with the rows that read "to confirm" and who holds them. Ask: *"Anything to add to the inputs, or a number you can paste now, before I read them as the real business?"*
2. **Owner interview** (Step 2): the eleven questions, answered by the owner only. Show which answers are on file and which are open. Ask: *"Can you answer the open ones now, or do they go to the owner?"*
3. **Meaning check** (Step 3): purpose, vision, mission, values as drafted or confirmed; the gate verdict. Ask: *"Does the purpose read as the owner's own, or does it need building?"*
4. **Audience** (Step 4): first the guest evidence on file (review themes with counts, interview themes, the mystery visit's three things; what is missing), then the persona, archetype mix, the Brand Affinity Audit patterns, a second audience where one exists. **Gate:** no review mining on file → the step stops here with a blocker; the persona is not drafted from the owner's picture alone. Ask: *"Is this the guest the reviews and the room show?"*
5. **Competitors** (Step 5): the scored table, IDEAS and OPPORTUNITIES. Ask: *"Any competitor missing or misjudged?"*
6. **Differentiator, positioning, archetype and role** (Steps 6–7). Ask: *"Does the positioning read as one claim?"*
7. **The Diagnosis doc** (Output): now write `[client]/diagnosis.md` and the PDF. Ask: *"Read the doc. Change anything before the PDF?"*

**Ask only when necessary; never invent.** The owner's interview answers (step 2), the purpose in the owner's words and the verdict's sign-off are never drafted by the practice: an open one is written *to confirm* with the question, a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and, when it blocks the next action or the stage from closing, a blocker in `status.json`. POS numbers, covers, spend, review counts and competitor names come only from the files or the user; no POS export means the numbers page says so, not an estimate. A gap that stops a step and that the user can answer now is one question; any other gap is a row and the step goes on.

**After every step:** write the file → update `clients/<slug>/status.json` (deliverable "Diagnosis": draft → review → approved → done, blockers added or removed, `next_action`, `updated`) → move the ClickUp task (id at `stages.<stage>.deliverables.<name>.clickup` in `status.json`; draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 7: `python scripts/clients.py pdf <slug> diagnosis.md "<Client>-Diagnosis-vN"` and send the PDF to the user. The user forwards it; the practice never emails a client.

## Principles

- **Meaning first.** If the business has no authentic meaning (purpose) and the owner won't build one, say so plainly and stop. That is the Vios client filter.
- **Strategy before marketing.** Marketing cannot fix a weak concept. If the diagnosis finds an upstream contradiction (what they say vs what they do), name it before building anything.
- **Structural over cosmetic.** A brand element only counts if it governs an operational decision.
- **Offline metrics over vanity metrics.** Success is return visits, covers and spend per guest, not followers.
- **Archetype-driven, not character-driven.**
- Work one step at a time. Short questions, casual language. Give structured options (1/2/3) over open prompts. Final client-facing output in the client's language (BG, GR or EN; side by side on request).

## Inputs to gather first

1. Existing brand materials (brand book, menu, website, socials)
2. 12 months of POS data if available (Memento, otherwise the POS export): covers, average spend, peak days, top sellers
3. Guest evidence, three pieces (templates in `templates/client/data/`, filled files in `[client]/data/`): **review mining** (`review-mining.md`, the last 200 reviews coded into praise and complaint themes with counts; required), **guest interviews** (`guest-interviews.md`, 8–10 fixed-question conversations, anonymised summary; consents in Drive), **mystery visit** (`mystery-visit-YYYY-MM-DD.md`, one unannounced scored visit). A venue not yet open: review mining of the two closest comparable venues, named as such, and no interviews or visit; say so.
4. An owner interview (the eleven questions below)
5. Competitor list: 10 minimum, 20 ideal, found by searching the client's own description + location

## Step 1 — The real business (facts before feelings)

From POS and observation: what sells, when, to whom, at what spend. Where the money and the empty seats are. One page, numbers only: **the numbers page**, `[client]/data/numbers-page.md` from `templates/client/data/numbers-page.md`, definitions and the Memento page (or export) for each row in `plugin/vios-core/references/numbers-page.md`. Fixed rows, in this order: size and shape (revenue, covers, average check, items per cover: 12-month total or average, best and worst month) · revenue mix by category · covers by daypart and weekday · cost lines (labour %, COGS %, prime cost %, loaded labour minute rate) · menu engineering (top 10 by volume, top 10 by margin, the quadrant with the three Stars and three Dogs named) · bookings · to confirm · what the numbers say (five lines, read back, never recommended).

A client on Memento: fill from the pages the reference names, one location, exports saved to `data/YYYY-MM/`; otherwise from the POS export and the accountant, each row labelled with its basis.

Recipes not costed → the margin rows and the quadrant read "to confirm" and a row goes to `open-facts.md`; the page still ships. The page's last section is the first finding of the diagnosis: what the venue actually sells, when and at what margin, set beside what the owner says it is in step 2.

## Step 2 — Owner interview: brand voice excavation

Ask one at a time, numbered as the worksheet (Brand Personality Questionnaire, `references/worksheets.md`):
1. What do you love about this business, and why?
2. What do you dislike or hate, and why?
3. Where do you bring the most value to your guests, beyond the plate?
4. If you could change one thing about this industry, what?
5. Why is this market great?
6. What has social media brought, good and bad?
7. Aside from money, why do you do this? (seeds W1 Purpose)
8. How do you do business, in a sentence?
9. What do your guests need protecting from?
10. What matters to you in the world right now?
11. What are you passionate about?

## Step 3 — Meaning check (W1–W4)

- Purpose: "Aside from commercial intent, why do we do what we do?" Who/what commitment → what we do → resources and frequency. Purpose without action has no substance.
- Vision: big, bold, slightly scary, believable; 5–10 years; transformational verbs.
- Mission: the everyday commitment; present tense; action-based.
- Values: each one must carry a verb or a behaviour. Single-word values are weak.

Gate: if purpose is empty or performed, stop here and report it.

## Step 4 — Audience (W5)

**Guest evidence first.** Before any persona line is written, show what the guests themselves put on file: the top five praise and top five complaint themes with counts and n (`data/review-mining.md`); the top answers per interview question with counts (`data/guest-interviews.md`); the mystery visit's three things (`data/mystery-visit-*.md`); and the three strongest guest quotes, one sentence each, platform or initials and month, no names. Mark where the guests contradict the owner's picture from step 2; the contradiction goes into the diagnosis as a finding, not smoothed over.

**Gate:** no review mining on file → stop at this step: a blocker in `status.json` ("review mining not done", holder the account manager), a row in `open-facts.md`, the ClickUp task stays draft, and the persona is not written; a persona built from the owner alone is the thing this gate exists to prevent. Interviews or the visit missing → the persona is marked **"review-based; interviews / visit pending"** and the two go to `open-facts.md`. The limits of asking (section 3.1) apply: what guests remember is evidence, what they say they would do is not.

Build the primary persona from 10–20 competitor profiles, the guest evidence above and the owner interview: demographics, psychographics, emotional before/after, pain, needs, beliefs, a quote (a real one from the evidence, attributed as above, never composed). Assign archetype(s), 70/30 rule, max two.

Then the **Brand Affinity Audit** (Reference Tool; the house worked instance is `plugin/vios-core/references/worked-examples.md` › E4): five or six brands the persona already loves, as a table brand · years · alternatives · why they stay beyond features, in the persona's own words; then the patterns across the affinities (restraint as a signal, an ambient cultural reference, belonging without performing, curated over comprehensive …). The patterns govern the positioning, the messages and the operating foundations: the brand must sit naturally next to those brands in the persona's life. Mark the audit **speculative until ground-truthed** in real audience conversations (pilot or post-opening) and say so in the output; interview question 1 ("why here rather than somewhere else") is the first ground truth, cite it when it is on file.

Where the business serves a **second audience** (collectors and the art community for a gallery, B2B partners for a producer, event hosts for a venue), name it as its own short section: who · what they need · where they are served (channels, programme, direct relationship) · what does not change (one welcome on the floor; the second audience is served through channels, not through a different door). The primary persona stays the calibration point for the room.

## Step 5 — Competitors (W6)

Score each on Brand Message, Positioning, Personality, Identity, Web/UX, Reviews: 1–10; 8+ green, 7 yellow, under 7 red. Output two lists: IDEAS (their strengths worth adopting) and OPPORTUNITIES (their gaps).

## Step 6 — Differentiator and positioning (W7–W8)

- The ONE thing done differently that adds value to the guest. Read reviews for "the story within the story".
- Positioning: WE HELP [audience] WHO [qualifier + pain] TO EXPERIENCE [benefit] UNLIKE [alternative] OUR SOLUTION [differentiator].

## Step 7 — Brand archetype and role (W10)

Three steps, in order: audience archetype → what they want in the context of their situation → brand archetype that serves that need. Then Brand Role: Guide, Inspiration, Defender, Peer or Leader.

## Output — the Diagnosis doc (`[client]/diagnosis.md`)

1. One-line verdict: meaning present / meaning to build / no meaning (decline)
2. The real business in numbers
3. Purpose, vision, mission, values (draft or confirmed)
4. Primary audience persona + archetype, the Brand Affinity Audit with its patterns, a second audience where one exists
5. Competitor map: ideas and opportunities
6. Differentiator and positioning statement
7. Brand archetype (core + influencer) and Brand Role
8. Contradictions found and what must change upstream
9. Recommended next step: `vios-messages-and-story` (steps 10–11) when the positioning reads as one claim; then `vios-persona-builder`, `vios-name-and-tagline`, `vios-brand-book`; or branding work upstream first

End with one line: the verdict, what is "to confirm" and who confirms it, and the next step and its skill. Then stop.