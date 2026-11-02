---
name: "vios-messages-and-story"
description: "Write the message architecture for a Vios F&B client from a finished diagnosis: the nine core message blocks (five primary, four secondary), the seven-block hero-led story framework, and the micro-message blocks per journey touchpoint, then verify them against the positioning. VIOS Practice Stage 1 steps 10–11. Use after vios-brand-diagnosis whenever a client needs core messages, a brand story, messaging architecture, 'what should we say', or before vios-persona-builder and vios-content-calendar can anchor copy."
---

# Vios Messages and Story

Steps 10 and 11 of the fourteen interrogations: the message architecture and the narrative. The diagnosis settled what the brand is; this skill settles what the audience should understand and the story it lives inside. Nothing here is copy. Hard lines: `vios-core:vios-guardrails` 1–12; the micro-story rule is in guardrails › Messages and micro-stories.

**Work in six steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before step 6 (status.json and open-facts.md bookkeeping aside). Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Primary core messages** (Step 1): the five blocks, one sentence each, with the diagnosis field each draws on. Ask: *"Does each sentence say what the guest should understand, in the diagnosis's own terms?"*
2. **Secondary core messages** (Step 2): purpose, vision, mission, one per value; the tone-by-moment rows. Ask: *"Are these the values as the owner holds them, one message each?"*
3. **Story framework** (Step 3): the seven blocks, hero to new world, in the client's languages. Ask: *"Does the hero recognise themselves, and does the brand stay the guide?"*
4. **Micro-message blocks** (Step 4): one per touchpoint, peak marked (provisional if the journey is not on file). Ask: *"Any touchpoint this venue does not have, or one missing?"*
5. **The closing test** (Step 5): six questions, yes/no, the fix for each no. Ask: *"Any no that should go back to the diagnosis rather than be fixed here?"*
6. **Write it** (Output): now write `[client]/brand-book.md` › Messages and story, the long-form doc and the PDF. Ask: *"Read it. Change anything before the PDF?"*

**Ask only when necessary; never invent.** A value, a brand belief, a purpose line or a peak that `diagnosis.md` and the journey do not hold is not written as if known: the block says *to confirm* with the question, a row goes to `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker to `status.json`. The owner's words (the belief, a value's name, the sentence the hero says to a friend when the owner has one) are never drafted by the practice. Names of competitors, venues and dishes come only from the files or the user. A gap that stops a step and that the user can answer now is one question; any other gap is a row and the step goes on.

**After every step:** write the file → update `clients/<slug>/status.json` (deliverable "Messages and story": draft → review → approved → done, blockers added or removed, `next_action`, `updated`) → move the ClickUp task (id in `status.json` › `clickup`; draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 6: `python scripts/clients.py pdf <slug> brand-book.md "<Client>-Messages-and-Story-vN"` and send the PDF to the user. The user forwards it; the practice never emails a client.

## Read first

- `../../references/stage-1-brand-strategy.md` § 2.1.2.10, 2.1.2.11, pattern S1-04 and the closing test under "Closing the sequence". The method is there verbatim; this skill applies it.
- `[client]/diagnosis.md`: purpose, vision, mission, values, audience persona (archetypal mix, before/after emotions, situational and personality desires), competitor audit, differentiator, positioning formula, archetype and Brand Role, Connection statement. No diagnosis, or a positioning that does not read as one claim: stop and run `vios-brand-diagnosis`; message blocks written on a loose positioning collapse within a month.
- `[client]/brand-book.md` › Journey if filled (touchpoints, guest state, peak); else the canonical touchpoint list in guardrails › Journey.
- An existing brand book, if the client has one: transcribe its messages first, then run the checks below on them before proposing changes.

## Principles

- **Strategy, not copy** (pattern S1-04). Each block is a single-sentence statement of what the audience should understand. If a line could appear in an ad, rewrite it as strategy.
- **Pull, don't invent.** Every block traces to a diagnosis field: audience from the persona, pain from the emotional insights, benefit from stated wants, alternative from the competitor audit, differentiator from step 7. Nothing enters a block that the diagnosis does not support.
- **Hero-led.** The audience is the hero in every block; the brand is the guide, whatever its Brand Role. A story in which the brand is the hero is returned.
- **Short and specific.** Story blocks are short stories in specific terms: a Tuesday, a street, a name for the feeling. Abstractions ("quality", "experience") are returned.
- **One arc.** The seven blocks read as one story from world to new world; each block is then a stand-alone foundation for micro-stories (guardrails › Messages and micro-stories).

## Step 1 — Primary core messages (5)

One sentence each, in this order, as "what the guest should understand":

| Block | Draws on | The sentence answers |
| --- | --- | --- |
| Audience | persona | who they are, in words that make them recognise themselves |
| Pain-points | emotional insights | the pain they feel around this category and what it does to their evenings |
| Key benefit | wants + offer | what they experience with this brand and what it changes |
| Alternative | competitor audit | the closest competitive group and where it falls short, the mirror of the differentiator |
| Differentiator | step 7 | the one difference and how it changes the guest's experience |

Then write each as the house format the practice's books use: **For** (who) · **Pain** · **Understanding we want to create** · **Emotional value** · **Competitors say / we say** · **Where this message lives** (the touchpoints and proofs). A message with no "where it lives" is not yet a message.

## Step 2 — Secondary core messages (4)

Purpose, vision, mission, and **one message per value** (ONE Gallery: Welcome, Ritual, Discovery, Quality each as a single line), each rewritten as a takeaway for the audience, not a fact about the brand ("We believe…" becomes "You should understand that here…"). Format: **Underlying belief** · **Understanding we want to create** · **Reinforces** (the behaviours, choices and refusals that prove it).

Then a **tone-by-moment** table: the voice stays one, the tone is calibrated to the moment (morning, afternoon, golden hour, evening for a day-long venue; arrival, the evening, departure for a dinner venue), one line of direction and one example each.

**Integrity rule**, written into the output: before communicating anything, does it reinforce at least one primary or secondary message without contradicting another? If not, it does not belong. The `vios-consistency-qa` check "Message anchor" enforces it.

## Step 3 — Story framework (7 blocks)

Each block a short story, three to six sentences, specific, present tense where it helps:

1. **The existing world** — who the hero is and what their life looks like before the story; they must recognise themselves.
2. **The obstacle** — the want or need that causes conflict; the category as it is.
3. **The call to action** — what sparks them to act, with the cost of not acting made vivid.
4. **Meeting the guide** — the brand appears, calms, shows credibility, points the way; it does not boast.
5. **The challenge** — the emotional consequence under the practical problem; the hero's vulnerability.
6. **The transformation** — the payoff; before against after.
7. **The new world** — life with the resolution in place; the sentence the hero says to a friend.

Write the arc in the client's languages when the audience persona is local-language; EN alongside for the team. Rewrite, never translate tone. Where the diagnosis holds a **brand belief** (one sentence the brand uses when the moment calls for narrative rather than category), place it under the story as "the belief, deployed" with where it lives (the peak, the email, long-form copy), not at the front of the differentiator.

## Step 4 — Micro-message blocks (per touchpoint)

One block per journey touchpoint, using the canonical touchpoint names in guardrails › Journey (drop what the venue does not have; never invent a new name without saying so). For each: **Anchors** (which core messages and story block) · **Touchpoint** · **Customer state** · **Tension to resolve** · **Understanding we must create** · **Non-verbal expression** · **Verbal expression** · **Success signal** · **Failure modes**. The verbal line is a register and an example, still not copy. Mark the peak touchpoint; if the journey is not on file, mark it provisional (Stage 2 sets it).

## Step 5 — The closing test (from the manuscript)

Read the whole output in sequence and answer each, yes or no, with the fix if no:

- Does the differentiator block solve the pain-point block for that audience?
- Does the positioning statement use the differentiator as its solution, and do the five primary blocks say the same thing as the formula?
- Does each secondary message trace to one of purpose, vision, mission, values without adding a new belief?
- Does the story cast the audience as a hero this brand can credibly guide, given its Brand Role?
- Does any block read as copy? Rewrite as strategy.
- Does any micro-message block contradict a core message?

A no that cannot be fixed here goes back to the diagnosis step it came from; say which.

## Output

`[client]/brand-book.md` › Messages and story, in the template's tables (core messages with short names and tier; story framework; journey if known; micro-message blocks), plus the long-form versions as a Claude Doc deliverable "<Client> — Messages and story v1" when the docs connector is present. Header names the source: diagnosis version and date. Every unsupported field is marked **to confirm**, never filled.

End with one line: the closing test results, the short names the other skills will use as anchors, what is "to confirm" and who confirms it, and the next step (`vios-persona-builder` if the persona is not built; otherwise `vios-name-and-tagline` or `vios-brand-book`). Then stop. This skill writes strategy; `vios-persona-voice` writes the copy.

## Example (brewery; placeholders; one primary message in house format)

**Message 1 — Made together.** For: people who want to know where things come from. Pain: breweries don't cook seriously, restaurants don't brew; the two worlds are kept apart. Understanding we want to create: here the food is designed for the beer and the beer for the food, both made in this building. Emotional value: trust; the feeling that someone thought about this. Competitors say "great beer, we have food too"; we say "we cook for beer, we brew for food". Where it lives: visible production, menu pairings, the host's first pairing suggestion, the tagline.

Not a message: "Great beer, great food, made with love." (copy, and a slogan)
