---
name: "vios-journey-design"
description: "Design the customer journey of a Vios F&B client moment by moment from the journey map: one design page per moment (customer state, brand intention, action, locked script, non-verbal frame, sensory frame, behavioural-economics design, role of the room, success metric, failure mode), the choreography (transitions, handoffs, continuities), the recovery document by failure scenario, and the operations and equipment briefs. VIOS Practice Stage 3 with the three-register translation and the filter test. Use when a client needs service design, scripts, SOPs for the floor, a threshold sequence, recoveries, or 'how exactly do we do this moment'."
---

# Vios Journey Design

Stage 3. The experience itself, specified in operational terms so that two staff members trained on it perform it the same way and a trainer who was not in the engagement can teach it. Strategy becomes the room here. Hard lines: `vios-core:vios-guardrails` 5 (food truth in the sensory frame), 9 (claims and allergens in scripts), 10, 11 (escalation topics are recoveries handed to a named person).

**Work in seven steps, in the working order below (HIGH first, silent last, then choreography, recovery, briefs, close). Stop after each and ask one question. Each step shows at most ten plain lines; a page is never shown whole in chat, its locked line and its recovery code are.** "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before the user has seen the step that writes it (`status.json` and `open-facts.md` bookkeeping excepted). Start by reading `clients/<slug>/status.json` and `open-facts.md`; never ask what they already answer.

## Steps

1. **Schedule**. Show the inputs check (map, Reasoning Note signed, filter test on file: yes/no each), the tiers with counts, the recovery codes seeded, small-format variant or not. Writes `design/schedule.md`. Ask: *"Start with the peak and the end?"*
2. **HIGH pages**, peak and end first. Show one line per HIGH moment: code · locked line (marked NEW where first written here) · recovery code. Writes `pages/Mnn.md` for the HIGH tier and the filter-test batch. Ask: *"Lock these lines?"*
3. **MEDIUM, LOW and silent pages**. Show counts per tier, the new locked lines (one line each), any CONFIRM fact on a page. Writes the rest of `pages/`. Ask: *"Any line that does not sound like the brand?"*
4. **Choreography**. Show the moment cluster around the peak in one line, then the continuities (five or fewer, one line each). Writes `choreography.md`. Ask: *"Do these continuities hold on every daypart?"*
5. **Recovery**. Show the scenario list (one line each: trigger → who takes over), the escalation person named or "to confirm". Writes `recovery.md`. Ask: *"Who takes over on escalation?"*
6. **Operations brief**. Show the coverage table by daypart (from POS or booking data, or marked "to replace with data"), the team structure in one line, equipment dependencies as a count. Writes `briefs/operations.md` (and `briefs/equipment-layout.md` when the build warrants it). Ask: *"Are these the staffing bands you run?"*
7. **Close**. Show the six-question test as six rows (YES / NO / trainable except the facts listed) and the open-facts count. Writes the harvest; renders the PDF. Ask: *"Send the operations brief to the approver?"*

**Ask only when necessary; never invent.** Allergen lines, serving age and licence conditions are quoted from `fact-sheet.md` with their verification date, never from memory: until sourced the page says CONFIRM, the fact gets a row in `clients/<slug>/open-facts.md` and a blocker in `status.json`, and the page cannot lock. The same for room facts (sightlines, sound level, the host stand's place), staffing and hours, the POS bands behind the coverage table, and the named person every escalation ends with. A locked line is the practice's draft until the approver locks it; a founder's decision (compensation policy, the escalation person) is his, never written for him. One question per gap, asked once.

**After every step**: write the files → update `clients/<slug>/status.json` (deliverable `status` draft / review / approved / done, `file`, blockers, `next_action`, `updated`) → move the ClickUp task (id in `status.json` › `clickup`; Draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 7, `python scripts/clients.py pdf <slug> journey/design/briefs/operations.md "<Client>-Operations-Brief-vN"` and send the PDF to the user; the pages set goes to the founder as files or Claude Docs when the account manager asks. The user forwards the PDF; the practice never emails a client.

## Read first

- `../../references/stage-3-journey-design.md`, the chapter verbatim: seven moves, the design-page template, patterns S3-01 to S3-08, the briefs, the harvest.
- `../../references/section-3-3-three-registers.md`: scripts are written in the floor register, pages in the operational register, reasoning stays in the concept register. Never paraphrase across registers; redraft.
- `vios-core:vios-filter-test`: the brand's filter test. Every script and every guest-facing line passes it before it is locked. No test on file: derive it first.
- `[client]/journey/journey-map.md`, `reasoning-note.md`, `handoff-to-design.md`: the table of contents, the why, and the latitude. A design that contradicts the Reasoning Note goes back to Stage 2.
- `[client]/brand-book-vN.md` (persona, Role, Connection, archetypal mix, expression dimensions, differentiator, messages, story) and `fact-sheet.md` + the operating concept (menu, beverage programme, service model, price point, room, equipment, staffing).
- `vios-core:vios-be-lens` and `vios-core:vios-nonverbal-lens`: the two libraries' five-line versions; cross-reference the full entries by name.

## The four converging inputs

Every page names its dominant inputs: **brand** (who it is for, the Role here, what we want felt), **concept** (what the kitchen, bar, room and staffing allow), **behavioural economics** (which system is deciding, cognitive load, reference point, how the remembering self is formed, where friction is removed or added), **non-verbal** (proxemics, paralanguage, kinesics, haptics, chronemics, environment). Decision moments lean brand + concept + BE; presence moments brand + NV; operational moments concept with the others giving character. No moment is designed with fewer than four consulted.

## Working order (§ 2.3.2.3)

HIGH first, and within HIGH the peak and the end first. Then MEDIUM, then LOW, then the silent moments last (what staff do not do, and where they are while not doing it). The schedule is written down before the first page and seeds the recovery codes (one `R-Mnn` per HIGH moment plus the concept's scenario codes, e.g. `R-UPSET`, `R-ESC`, `R-QUEUE`) so that HIGH pages can name their recovery before `recovery.md` exists; `recovery.md` then adopts those codes. **Single-page mode**: when one page is asked for before the set exists (a test, a pilot moment), write it, say on the page that it is out of order, and reference `choreography.md`, `recovery.md` and `schedule.md` as "to be written" with the scenario codes it expects.

## The design page (one per moment)

The manuscript's fields, rendered in the house layout the practice ships (28 pages in the worked instance, `plugin/vios-core/references/worked-examples.md` › E11). Header: M-code · tier label · moment name · descriptor line (type · phase · mode, e.g. "Digital touchpoint · Pre-visit · Self-led", "Environmental · 2–10 min · Approach"; type is one of In-room · Digital · Environmental · Object · B2B · Operational) · markers. Tier labels: **CRITICAL IMPACT** (HIGH), **HIGH IMPACT** (MEDIUM), **STANDARD** (LOW), **SILENT**. Body blocks, in this order:

| House block | Holds (manuscript fields) |
| --- | --- |
| CURRENT STATE | the moment in one sentence and the customer state: where on the arc, what they just had, what comes next |
| DO | the action as a numbered list: who, from where, places what where; the sensory frame and the room's work appear here as numbered items when the room is doing specific work |
| SAY | the script, marked **LOCKED** where the words are exact; floor register; filter-tested; the caption voice for digital moments |
| DON'T | the failure modes and the tempting defaults, as short prohibitions |
| NON-VERBAL | body, geometry, silence, tone, volume, timing (omitted on digital, object and silent pages; kept on environmental pages, where it is the room's work) |
| BEHAVIORAL ECONOMICS | the principle at work, cited as "BE n name" (the numbered principles of section 3.1.5, e.g. BE 17 thin-slicing) and what it does to the decision here; non-verbal entries cited as "NV letter.number" (e.g. NV C.2 eye behaviour) |
| RECOVERY | "If … → …": trigger, what is done and said, who takes over; references the recovery document |
| state arc | one line: before → during → after ("Curious → Visualising → Decided") |
| Success metric | an observable signal, never a sentiment |
| Target emotion | one word or two |
| Brand pillar | the core message or pillar the moment serves (welcome, discovery, differentiator, quality) |

The manuscript's eleven questions, for completeness, map onto the blocks as follows:

1. **The moment**, one sentence (from the map).
2. **Customer state**: where on the arc, what they just had, what comes next.
3. **Brand intention** (from band 4).
4. **Action**: who approaches from where, says what, places what where. Precise enough for two people to do it identically.
5. **Script**: only where exact words are required; one or two locked lines; floor register; passes the filter test. "Welcome" is not a script; "Welcome — sit anywhere" is. Where the moment changes with the daypart or the occasion, give the line in **registers** (default · evening · private event) rather than variations. A locked line first written at Stage 3 is new copy: mark it NEW on the page for the approver and append it to the Stage 3 block of `[client]/archive/filter-test-batches.md`.
6. **Non-verbal frame**: body, geometry, silence, tone, volume, timing. Usually larger than the script.
7. **Sensory frame**: light, sound, scent, surface, temperature; or "inherits the room".
8. **BE design**: the decisions the guest makes here and how the design shapes them; empty for low-decision moments.
9. **Role of the room**: sightlines, acoustic separation, flow, lighting register, when the room is doing specific work.
10. **Success metric**: an observable signal ("sat without asking which table"), never a sentiment.
11. **Failure mode** and the recovery reference.

**Facts on a page.** An allergen line quotes the fact sheet and carries its verification date, and is relocked when the fact sheet changes (guardrails 9). A legal fact (serving age, licence condition) is sourced and dated the same way, never written from memory; until it is sourced it is marked CONFIRM and the page cannot lock.

HIGH pages add: the brand-coherence test for this moment (does it hold the Role and the Connection statement), the story-framework block it plays, operational dependencies, and one line **Cost of the moment**: staff minutes × the loaded labour minute rate + item cost, per guest or per table, assumption named (`plugin/vios-core/references/numbers-page.md` › Cost of a moment; the rate and item costs from `[client]/data/numbers-page.md`, "no marginal cost" for a greeting or a silence, "rate to confirm" with an open-facts row when the numbers page has none). The line is read at step 2 as part of the moment's one line (code · locked line · recovery code · cost), so the founder locks the signature and the peak knowing their price; it is never the reason to drop a HIGH on its own. MEDIUM pages carry the same blocks, none longer than five items, about half a HIGH page. LOW pages: CURRENT STATE, DO, DON'T, the metric line, and SAY only where a line is locked. SILENT pages: DO is "Nothing" with what M-before did the work, and DON'T lists what would break the silence. A moment owned by a third party (a partner's table, a platform's screen) gets a **brief page**, not a design page: what the partner is asked to hold, the brand's one check, and a periodic check date (quarterly by default); no DO/SAY/DON'T. Footer: brand-book sections, BE and NV entries, dependencies, and a `Harvest:` flag whenever the page used a pattern, a recovery scenario or a template refinement not in the chapter (flagged as the page is written, so the harvest is a collation, not a search). Every page is one rendered page; uniform layout across the set. A two-moment end (end-1 and end-2 designed as one on the map) is two pages, one per moment, each with the same header note naming the pair and cross-referencing the other; the shared design lives in the choreography's cluster, not in a merged page.

## Small-format variant (counter, kiosk, takeaway, stall)

A format where one person serves, the whole visit is under five minutes and the next guest is already present gets the **one-screen page**: header as above, then only CURRENT STATE (two lines), DO (five items or fewer), SAY (locked lines and registers), RECOVERY (three rows or fewer), the metric line, the pillar. NON-VERBAL and BEHAVIORAL ECONOMICS collapse into one line each inside DO. The end and the next guest's threshold are designed on one page when they happen on the same face in the same second. Say on the schedule that the set is in the small-format variant; the operator reads one screen per moment or does not read it.

## Choreography (§ 2.3.2.5)

A separate document, "Choreography & continuities", in three sections, **continuities first**, and the first thing section 1 does is name the **moment cluster** around the peak explicitly: which moments serve the peak and how they are designed as one (in the worked choreography M13–M21 protects the peak at M18, `plugin/vios-core/references/worked-examples.md` › E12); this is where the choreography earns its words. After the cluster, at most five continuities as titled rules (the voice is the same from the caption to the farewell · approach angle and distance · step back after every locked gesture · where the team stands when not at a table · the signature leads, every guest, every daypart); a continuity that only restates the pages is cut. Section 2 the transitions as moment pairs (M08 → M09 …) with what the transition does and why it matters, duration and what fills it; section 3 the handoffs (who passes the guest to whom, what is said and shown, what the guest does not see).

## Recovery (§ 2.3.2.6)

By failure scenario, not by moment. The restaurant catalogue is the starting point, not the list: wrong order, wait exceeded, guest visibly unhappy, allergy disclosed late, over-served table, complaint at the bill. Drop what the concept has no place for (over-served and a wait between courses at a counter) and add the scenarios the concept needs, which are mandatory, not optional: at a counter the room wrong at open and the queue; in B2B a partner dropping the brand's object (the cards, the menu, the display). For each: trigger (observable), what staff do, what they say (floor register, filter-tested), who is informed, how the guest is left. Recovery is written in the brand's character (pattern S3-07), not the category default: no over-apology, no under-acknowledgement. Every HIGH moment has a recovery. **Compensation**: the team member never offers compensation in the moment (no free item, no discount, no voucher); the approver decides afterwards and offers privately (guardrails 3 and 10). Escalation topics (guardrails 11) end with a named person taking over, never with a script.

## Patterns to apply by default

S3-08 threshold thin-slice + S3-01 locked greeting + S3-02 silent walk as one composition (where the brand book forbids a greeting line, the threshold lock is a behaviour, e.g. eyes before words within ten seconds, and the first locked line sits one moment later; S3-01 is met by the lock, not the line) · S3-03 non-visible information rule · S3-04 one decision anchor at ordering, defended, not drifting · S3-05 peak placement test ("if the evening ended here, would it feel complete?") · S3-06 bookended end that echoes the threshold · S3-07 recovery within character. **Counter formats** (no host, no walk): one guest's end (S3-06) and the next guest's threshold (S3-08) land on the same team member in the same seconds; no chapter pattern covers it, so design the pair as one composition with an explicit split rule (body to the leaver, eyes to the newcomer, or the brand's equivalent) and record it as a harvest candidate, the counter variant of S3-06/S3-08. Record a pattern the engagement used that is not in the chapter, in the standard form.

## Close the design (§ 2.3.2.7)

Six questions, yes/no with the fix: every map moment has a page · every page names its dominant inputs with cross-references · the Role holds at every moment · choreography complete · every HIGH has a recovery · a trainer outside the engagement could train from it. The sixth question allows a third answer, "trainable except the facts listed", followed by the list of open facts (each with the page it sits on and who confirms it); use it when the behaviour is complete and only CONFIRM facts remain, so a complete design is not marked NO for facts the client has not yet supplied.

## Briefs (§ 2.3.6)

- **Operations brief** (10–20 pages), in the house form (`plugin/vios-core/references/worked-examples.md` › E13), eight sections: 1 team structure and the operating principle (named roles, who is not on the floor, position assigns the role in the moment); 2 coverage by daypart as a minimum-staffing table (daypart · hours and mode · minimum on floor · composition), with the rule that a band that cannot be staffed is discussed, never silently degraded; pull the POS or booking data (tickets per hour, peak bands) before writing section 2, and where it is not available write the bands as assumptions under a heading "to replace with data" and list them in the open dependencies; 3 role responsibilities at each HIGH moment (primary actor, coordination, backstop, knowledge requirement); 4 the service-flow assumptions the design makes, each boxed with its reason and the moment it protects (tables per server at the dwell, bar seats per bartender, prep time per signature drink, pass-to-table time, the bandwidth the deliberate pause needs); 5 equipment and layout dependencies, each with the moments it serves and the source (the equipment brief lives here, not as a separate document, unless the build is large); 6 training assumptions (the locked scripts every team member learns, knowledge requirements, drills, the pre-shift briefing); 7 standards and observable metrics as a table (standard · observable behaviour · target frequency), sampled not exhaustive, diagnostic not punitive; 8 management review cadence (daily pre-shift, weekly team review, monthly design review with the founder off the floor) and the rule that small revisions over the first 6–12 months are expected.
- **Equipment and layout brief** as a separate document (6–12 pages) only when the build is large enough to go back to the architect or interior designer; otherwise section 5 of the operations brief.
- Revisions to Stage 1 briefs, versioned and reissued, when the design surfaces a sightline, a graphic element or a material they did not anticipate.

## Output

`[client]/journey/design/` with `pages/M01.md … Mnn.md` in journey order (two-digit codes, the same as the map), `choreography.md`, `recovery.md`, `briefs/operations.md`, `briefs/equipment-layout.md`, `schedule.md` (the design schedule), and `[client]/archive/harvest-stage-3.md` (new patterns, recovery scenarios, library entries, template refinements, collated from the `Harvest:` flags on the page footers; an hour or two when the footers were flagged as the pages were written, half a day when they were not; the practice's pattern factory). Claude Docs for the founder's review only when the account manager asks for them, not as part of writing the files. Volume is expected: two to three hundred pages for thirty moments; the uniform template is what keeps it usable.

End with one line: pages written by tier, HIGH recoveries done, the threshold sequence and the bookended end in one line each, open dependencies and who confirms them, and the next step (`vios-training-programme`). Then stop.
- **Chase list**: `[client]/open-facts.md`, one table for the whole engagement, appended at every stage: fact needed · which moment, page or section it blocks · who holds it · asked on · due. Every "to confirm" in the deliverable points at a row here; the account manager works the list, nobody else. Say in the final line how many rows are open and which one blocks the stage from closing.


## Example (one HIGH page compressed; brewery; placeholders)

**M02 · CRITICAL IMPACT · Threshold crossed** · In-room · ~30 sec · Arrival. CURRENT STATE: made the trip, checking it was worth it; the room speaks before anyone does. DO: 1. host at the stand two metres inside the door, turns before the guest reaches it; 2. one beat, then the greeting, then lead; 3. tanks visible from the door, kitchen pass lit, room at 62–66 dB, bread and wort in the air. SAY (LOCKED): "Welcome — sit anywhere." (filter test: not performed ✓). DON'T: no reservation question inside the greeting; no tour on the walk. NON-VERBAL: lens-level eye contact for the line only, open palm toward the room, moderate pace, lead slightly ahead. BEHAVIORAL ECONOMICS: thin-slicing (BE 17), cognitive ease (BE 1); nothing to decide yet. RECOVERY: if the guest hovers → the second welcome (R01). Checking → Settling → In. Success metric: moves into the room without a question within ten seconds. Target emotion: at ease. Brand pillar: welcome.
