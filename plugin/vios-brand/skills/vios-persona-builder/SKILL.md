---
name: "vios-persona-builder"
description: "Build a Vios Marketing Brand Persona (Persona Bible, character sheet brief, voice spec, behaviour rules, expression palette, is/is-not pairs, tone by guest mood, objective and KPIs, full AI disclosure, error protocol, pilot and versioning) for an F&B client, EN/BG side by side, one question at a time. Use after vios-brand-diagnosis, whenever a client needs a brand persona, a brand character, a mascot or an AI ambassador defined."
---

# Vios Persona Builder

Turns a client's brand foundation into a Brand Persona: the brand as a character that can appear on camera, speak and post every day without drifting. Hard lines: `vios-guardrails` 1–12. Output lands in `[client]/persona-bible.md` per the guardrails client-file convention. The brand book's Part 5 (How we sound) is assembled from this file, so every Part 5 element is built here, not by the assembler.

**Work in seven steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no open-fact numbers, section references or file paths on screen. The method's own one-question-at-a-time inside a step stays as it is. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Each step writes its file and `status.json` as it goes; the client-facing render (the PDF) only at step 7. Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Inputs and archetype** (Steps 0–1): what the diagnosis and the messages give; 2–3 archetype pairs with one line each. Ask: *"Which pair?"*
2. **Format** (Step 2): the three formats, one recommended with its reason; the three AI rules if AI. Ask: *"Which format?"*
3. **Personality and tone by mood** (Steps 3–4): the seven personality questions one at a time, then the is/is-not pairs and the mood rows. Ask: *"Is this the person who walks into the room?"*
4. **Persona in practice, behaviour, journey** (Steps 4b–5): sliders, word rules, hard moments, the ten-line checklist; the matrix; speaks / present / silent per touchpoint. Ask: *"Any cell or touchpoint that feels off?"*
5. **Expression palette and the locks** (Steps 6–7): palette rows; character sheet brief, voice spec, consent plan. Ask: *"Who signs the consent, and what does it cover?"*
6. **Objective, KPIs, disclosure, error protocol, pilot** (Steps 8–11): the job sentence, 4–6 KPIs, who does what, the pilot. Ask: *"Which measures are yours, and who is the approver?"*
7. **The Persona Bible** (Output): now write `[client]/persona-bible.md` and the PDF. Ask: *"Read it. Change anything before the PDF?"*

**Ask only when necessary; never invent.** The client's choices (archetype pair, format, traits, never-list), the approver, the consent signatories and the KPI baselines are never drafted by the practice: when the client is not in the room the step records the recommendation and writes *to confirm* with the question, a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and, when it blocks the next action or the stage from closing, a blocker in `status.json`.

Alcohol yes/no, the address register, the name and the signature phrases come only from the files or the client; a baseline not on file is "open". No approver on file is a blocker on the front page, never a placeholder name. A gap that stops a step and that the user can answer now is one question; any other gap is a row and the step goes on.

**After every step:** write the file → update `clients/<slug>/status.json` (deliverable "Persona Bible": draft → review → approved → done, blockers added or removed, `next_action`, `updated`) → move the ClickUp task (id at `stages.<stage>.deliverables.<name>.clickup` in `status.json`; draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 7: `python scripts/clients.py pdf <slug> persona-bible.md "<Client>-Persona-Bible-vN"` and send the PDF to the user. The user forwards it; the practice never emails a client.

## Principles

- Meaning first. If the client has no authentic purpose or won't build one, stop and say so (the Vios client filter).
- Understand before acting: build only on what `diagnosis.md` and the client state. Never invent.
- One question at a time. Short, casual language. Options to pick from, not open prompts. When the client says "decide", pick and give the reason in one line.
- Every final statement in English and Bulgarian side by side (Greek for Greek markets).
- Propose options, record the client's choice.
- A persona is a living document: versioned, reviewed, retirable.
- No fake biography for an AI persona. A drive and a point of view, never an invented human life story (it reads as deception).

## Step 0 — Inputs

From `[client]/diagnosis.md` (or ask): purpose, vision, mission, values; audience persona (demographics, psychographics, emotional before/after, core trigger); positioning; archetype and Brand Role; identity (name, logo, colours, type, existing tone); the place (concept, menu highlights, the room, the team, the neighbourhood); alcohol yes/no; existing measures (e.g. brand book KPIs).

From `[client]/brand-book.md` › Messages and story (written by `vios-messages-and-story`): the core messages, the story framework and the **journey** (touchpoints, guest state, peak). The persona is the guide in that story; it is built knowing where in the journey it appears. No journey on file: use the canonical touchpoint list in `vios-guardrails` › Journey and say the placement is provisional.

No diagnosis: run `vios-brand-diagnosis` first. Don't continue without purpose and audience. If the brand book already fixes the archetype, carry it over and say so instead of re-asking.

## Step 1 — Archetype

Propose 2–3 archetype pairs (core + influencer, 70/30) that fit the purpose and the audience's situational need, taken from the twelve in `../vios-brand-diagnosis/references/archetypes.md` (drive, fear, strategy, voice, message per archetype), never from memory. One line each on why, plus the guardrail for the secondary. Client picks.

## Step 2 — Persona format

| Format | Best for | Watch out |
| --- | --- | --- |
| Real person (owner, chef, bartender) + AI scaled | Family places, chef-led concepts | Written likeness/voice consent (guardrails 7); depends on one person |
| AI digital ambassador | Chains, delivery, multi-language | Must be disclosed (guardrails 6); risk of feeling generic |
| Illustrated / mascot character | Gelato, kids, playful brands | Less "human" for trust-based ads |

Recommend one with a reason. Client decides. If AI is chosen, state the three rules at once: labelled from the first frame; real backgrounds only (guardrails 5); the AI never speaks in a real person's name (e.g. a founder-curator's signed voice stays human).

## Step 3 — Personality (one question at a time, confirm each)

1. If the place were a person walking into the room, who are they? Age range, energy, dress.
2. Three traits, and the one trait they must never show.
3. **Is / is-not pairs** (default): turn each trait into "X but not Y" (warm but not gushing, curious but not nosy, knowledgeable but not lecturing). 4–6 rows. Goes at the front of the traits section.
4. Their point of view on food/drink, people, the art or concept, and this neighbourhood.
5. How they talk: formal/informal address (BG ти/Вие, GR εσύ/εσείς, per channel), short/long, humour 1–5, slang yes/no, emoji policy.
6. Signature phrases or habits (a greeting, a sign-off, a gesture).
7. What they would never say or do (the never-list: "never says" and "never does").

## Step 4 — Tone by guest mood (default)

Voice stays fixed; tone follows the person addressed. One row each, with an example line EN | BG: unsure first-timer, regular, VIP/collector/high-spender (same welcome, different route), excited group, upset guest (calm, short, hands over to a named person). Add client-specific rows if the diagnosis names other audiences.

## Step 4b — Persona in Practice: sliders, word rules, hard moments, checklist

These are what the brand book's Part 5 carries and what a writer reaches for at speed, so they are built here with the client, not improvised by the assembler:

- **Tone sliders**: the five scales of `../../references/stage-1-brand-strategy.md` › Instrument 6, Layer 3 (home position and permitted range on each), with one line on what a notch lower and higher would sound like. Voice stays fixed; the eight expression dimensions belong to the map's Move 4, not here.
- **Word rules (lexicon)**: "it is" adjectives, "it has" nouns, the verbs the brand uses; house terms (what we call the room, the dish, the guest); never-words. 5–10 entries per list, EN | BG.
- **Hard moments**: the 4–6 situations where the voice is most likely to slip (full house, a no-show, a price question, a bad review, an allergy question, closing time), each with the line the persona says and the line it never says. Escalation topics (guardrails 11) are handed over, not scripted.
- **The ten-line checklist**: ten yes/no lines a writer runs on any draft in under a minute, drawn from the is/is-not pairs, the never-list and the word rules. `vios-persona-voice` and `vios-consistency-qa` use it as the fast pre-check.

## Step 5 — Behaviour matrix and journey placement

Channels (Reel/TikTok, story, feed post, paid ad, comment reply, bad-review reply, Google Business post) × moments (launch, slow weekday, event night, holiday, complaint). One line per cell. Client corrects what feels off. Default for AI personas: bad reviews are never answered by the AI; a named person signs.

Then place the persona on the journey, one line per touchpoint (guardrails › Journey): **speaks** (the persona carries this moment), **present** (in frame or in copy, a human carries it), **silent** (humans only). Defaults: online touchpoints (discovery, profile check, booking, reminder, after-visit) speak; arrival and departure are human in the venue and the persona only echoes them online; ordering and making are present (the persona points at the people who make); review replies and escalation topics silent (guardrails 11). The peak is shown by the persona, never performed by it.

## Step 6 — Expression palette

For each moment: target emotion, face cues, intensity 1–5, gaze. Default rows: welcome (warmth 3), showing a dish/work (pride or curiosity 2–3), event (joy 3–4; cap at 3 if party energy is on the never-list), story (sincerity 2), complaint reply (empathy 2), sign-off (contentment 3). Becomes the reference stills brief.

## Step 7 — Visual & voice lock (briefs only)

- Character sheet brief: face, wardrobe in brand colours, hair, one unique anchor detail, settings, 7 fixed shots (front, 3/4 L, 3/4 R, profile, smiling, serious, with product) + one still per palette row. Negative list: what the character must never become.
- Voice spec per language: gender, age feel, pace, warmth, accent, example line.
- Consent plan (guardrails 7): who signs, what it covers, what happens when they leave. Goes to `consents/`.

## Step 8 — Objective and KPIs (default)

One sentence: the persona's job for the brand. Then 4–6 KPIs tied to the client's own measures (brand book or diagnosis), favouring offline and depth signals (saves, messages, return visits, sign-ups, enquiries, reviews mentioning the concept) over likes and views. Baseline column; "open" until the first month sets it. Review cadence named. Show n beside every percentage (guardrails shared numbers).

## Step 9 — Disclosure, full set (default for AI or AI-scaled personas)

Copy the disclosure set (a) to (e) from `vios-guardrails` hard line 6 into the Bible as a table with EN | BG lines, naming the account, platform or contract each item applies to for this client. Guardrails 6 is the only source for the wording, the label rule and the fallback when a scheduler cannot set the platform label; the Bible instances it, it does not restate it.

## Step 10 — Error protocol and retirement (default)

The error protocol (pull, correct, log, fix the source, pause) and its timings live in guardrails 6. In the Bible, name who does each step for this client: the approver who pulls, the person who signs corrections, where the log lives (`qa-log.csv`), who edits the Bible or the prompt.

Retirement rule: no KPI movement after two content cycles, a bad guest reaction to the format, or a rule change. The approver decides; old content stays labelled.

## Step 11 — Pilot before scaling (default)

3–5 clips tested with 3–5 real guests matching the audience persona before paid ads or daily posting. Three questions: does it feel like the brand? does the AI label (if any) bother you? did you notice the core offer/concept? Fail on the label question means rethink the format, not just the script.

## Output — the Persona Bible

One doc (Docs artifact when available), saved as `[client]/persona-bible.md`. Front page: **approver**, **address register per channel**, **emoji policy**, **alcohol yes/no**, **AI disclosure rule**, **version number and next review date** (quarterly and at each content-cycle close). Then:

1. Persona at a glance (name, archetype, format, one-line essence, speaks for / never speaks for) — EN | BG
2. Story & point of view — EN | BG (no invented biography for AI)
3. Objective and KPIs
4. Traits: is / is-not table, never-trait, never-list
5. Voice & tone rules: tone sliders on the five scales, 5 do/don't lines, word rules (lexicon, house terms, never-words), hard moments, the ten-line checklist — EN | BG
6. Tone by guest mood — EN | BG
7. Signature phrases and on-camera habits — EN | BG
8. Behaviour matrix and journey placement (speaks / present / silent per touchpoint)
9. Expression palette
10. Character sheet brief + negative list
11. Voice spec per language + consent
12. Content pillars (3–5) tied to the purpose, with who speaks for each
13. Disclosure, full set (instanced from guardrails 6)
14. Error protocol (names per guardrails 6) and retirement
15. Pilot before scaling
16. Guardrails that apply (link `vios-guardrails` 1–12)

End with one line: the persona in a sentence, what is "to confirm" and who confirms it, and the next step: pilot clips, character sheet production with the creative operator, then `vios-content-calendar`. If no approver is named, say so: nothing ships until one is. Then stop.