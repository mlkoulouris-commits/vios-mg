---
name: "vios-training-programme"
description: "Turn a Vios F&B client's journey design into staff capability: the three-register translation into floor materials, the two-stack document architecture (workbooks per role, role cards, wall charts, floor playbook; facilitator guides, operating handbook, coaching guides, assessment instruments, cadence calendar), the pre-opening and post-opening cadence, the coaching infrastructure (manager as coach, pre-shift ritual, standing rotation, assessment loop), the three handoffs and the engagement retrospective. VIOS Practice Stage 4. Use when a client needs staff training, onboarding material, a floor playbook, pre-shift formats, a service manual, or 'how do we make the team do this'."
---

# Vios Training Programme

Stage 4. The design is true on paper and useless on the floor until the people can do it. This stage produces the documents and the cadence by which they do it, written for the conditions in which staff read: in fragments, between shifts, apron on. Hard lines: `vios-core:vios-guardrails` 6 (AI disclosure lines in any AI-carried moment), 9 (allergen and claim lines verified), 11 (escalation routes in every recovery card).

**Work in seven steps (the seven moves below, in their order). Stop after each and ask one question. Each step shows at most ten plain lines; the documents live in the files.** "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before the user has seen the step that writes it (`status.json` and `open-facts.md` bookkeeping excepted). Start by reading `clients/<slug>/status.json` and `open-facts.md`; never ask what they already answer.

## Steps

1. **Translation checklist** (Move 1). Show the counts (moments · recoveries · operational elements) and the case: venue open or opening, team size, minimum set or full stack. Writes the checklist as the opening section of `training/architecture.md`. Ask: *"Open venue with the minimum set, or the full architecture?"*
2. **Registers** (Move 2). Show three triples (concept → operational → floor), the HIGH moments first. Writes `training/registers.md`. Ask: *"Do the floor lines sound like the brand with a guest?"*
3. **Architecture** (Move 3). Show the document table: one line per document in, owner named; omissions with their reason. Writes `architecture.md` in full. Ask: *"Approve the architecture before writing starts?"* (founder and operations team; the task goes to Review).
4. **Cadence** (Move 4). Show onboarding / standard / compressed and why, the week or session sequence, the trainer and the dates. Writes `cadence-calendar.md`. Ask: *"Opening date and trainer right?"*
5. **Materials** (Move 5). Show the documents written in this pass with their length, and the allergen, alcohol, claim and AI-disclosure lines checked (count). Writes `staff/` and `management/`. Ask: *"Read-aloud drafts to the founder and the operations team?"*
6. **Coaching infrastructure** (Move 6). Show the four components with their owner and first date, and the register-audit date. Writes the coaching guides, the pre-shift facilitator guide and the calendar rows. Ask: *"Who is the manager-as-coach?"*
7. **Close** (Move 7). Show the six-question test as six rows, then the proof set as three lines: certification (people on the floor · role cards with their 10 checks · who signs), the behaviour KPIs (two per HIGH moment, the counting service), the thirty-day register audit (date, who visits), and the three handoff dates. Writes `handoffs.md`, `first-thirty-days.md`, `certification.csv` (header and the roster rows, uncertified), `behaviour-kpis.md`, the harvest and the retrospective; renders the PDF. Ask: *"Hand over to the founder, with the audit on this date?"*

**Ask only when necessary; never invent.** The trainer's name, the opening date, the team size and shift pattern, the manager who coaches, the rotating content (current menu or exhibition, prices) and the escalation person on every recovery card come from the client folder or the user; a missing one is written "to confirm", gets a row in `clients/<slug>/open-facts.md` and a blocker in `status.json`, and the step goes on. Allergen, alcohol and claim lines are checked against `fact-sheet.md` before they reach a card; an unverified line is CONFIRM, never a guess. Scripts are quoted from the design pages, never redrafted here. The founder's approval of the architecture and his sign-off at handoff are his, never recorded for him. One question per gap, asked once.

**After every step**: write the files → update `clients/<slug>/status.json` (deliverable `status` draft / review / approved / done, `file`, blockers, `next_action`, `updated`) → move the ClickUp task (id in `status.json` › `clickup`; Draft while writing, Review when it waits for the approver, Approved on sign-off, Done when delivered) → at step 7, `python scripts/clients.py pdf <slug> training/journey-training-plan.md "<Client>-Journey-Training-Plan-vN"` (the Journey Training Plan of the house form for a running venue; for an opening, the floor playbook as `"<Client>-Floor-Playbook-vN"`) and send the PDF to the user. The user forwards it; the practice never emails a client.

## Read first

- `../../references/stage-4-training.md`, the chapter verbatim: seven moves, the document architecture, patterns S4-01 to S4-07, the handoffs, the engagement harvest.
- `../../references/section-3-3-three-registers.md`: the engine of this stage. Concept register for the founder and senior readers, operational for managers, floor for staff. Each is redrafted for its reader, never compressed from another.
- `vios-core:vios-filter-test`: built into the floor playbook, the wall chart and the operating handbook so staff who improvise can self-check.
- `[client]/journey/design/` in full: pages, choreography, recovery, briefs; plus the brand book and the journey map, so materials stay anchored to strategy, not only to pages; plus the operating concept (menu, beverage programme, systems), which staff must know at least as deeply as the brand.

## House form (from the ONE Gallery Journey Training Plan v2 and Operations Brief, Oct 2026)

For a venue that is already open, the practice ships one **Journey Training Plan**: an onboarding programme that takes one new team member at a time through the whole journey, trainer named on the cover, aligned to the brand-book edition. Its shape:

- **Five training principles**, stated first: foundations before moments · say it, then walk it (words first, then words + geometry + retreat in the real room) · the retreat is the lesson (as much time on what not to do) · drill the counter-intuitive (restraint is trained in, the instinct to help trained out) · floor-ready is a checklist, not a feeling.
- **Order by weight, not by sequence.** Session 1 foundations: the non-negotiables (three, from the handoff) and the continuities (from the choreography), learned once so they are not re-taught per moment. Session 2 the HIGH moments, each as what it is → the locked script → the geometry → the retreat; the end pair rehearsed together. Session 3 the MEDIUM moments as a table (moment · what the trainee does · target state). Session 4 the LOW moments as standards, then the full arc walked once in the room, narrated. Session 5 the silences and the three drills. Session 1 always first and alone; Session 5 always last and never skipped; shadow shifts only after Session 4.
- **The three drills**: the retreat drill (step back 2–3 m, no glance back; the glance is the tell) · the silent-moment drill (a seated stand-in and a clock; the 20-minute floor should feel uncomfortable before it feels normal) · the welcome-symmetry drill (greeting and farewell back to back).
- **Knowledge the trainee must hold**: the rotating content (current exhibition or menu, the signature drinks or dishes with their one-line cue, the three-noun positioning and the one-line differentiator), who holds deeper knowledge and the defer rule, where prices live. Refreshed on the rotation cycle.
- **Floor-ready sign-off**: a checklist grouped foundations · HIGH moments (every register) · service moments · silences (verified under a clock) · knowledge · shadow shifts, signed and dated by trainer and trainee. Sign-off is against the list.
- **Pre-shift briefing** as the ongoing carrier: 15–20 minutes (the cadence in Move 5 is the one source for the number), today's rotating content, reservations and events, notes from the last shift, then one role-play of a locked moment, rotating daily.
- Scripts are quoted from the design pages, in their **registers** (default · evening · private event), and the plan says to pull the final wording from the pages before each session.

The manuscript's full two-stack architecture and the four-to-six-week pre-opening cadence apply to an opening. For a running venue with a small team the minimum set is the Journey Training Plan, the floor playbook (the locked scripts in journey order) and the sign-off checklist; everything else in the architecture is added when the team size justifies it, and each omission is recorded.

## Move 1 — Intake and translation checklist

Every moment, recovery and operational element that must reach the floor, listed with its source page. The checklist is the stage's table of contents.

## Move 2 — Translate across registers

For each item: concept line exists (from the book or the page footer) → operational line (the page) → floor line, redrafted, read aloud, 60–80 % shorter, in the words the brand uses with guests. Then the three are read together: does the floor line, performed, deliver what the concept line says the brand believes? Capture the triple in `[client]/training/registers.md`.

## Move 3 — Document architecture (decide before writing)

Two stacks, never mixed; every document named with audience, register, length, and the manager who owns it; omissions recorded with the reason.

| Stack | Document | Audience | Register | Length | Holds |
| --- | --- | --- | --- | --- | --- |
| Staff | Workbook, one per role | that role | floor | 20–40 pp | the role's moments in journey order: script, NV frame, sensory frame, success metric, failure trigger; 1–2 page brand summary in front; glossary at the back |
| Staff | Role cards | that role | floor | 1–2 laminated panels | locked scripts, recovery triggers, peak and end; nothing else (S4-04) |
| Staff | Wall charts | all | floor | one sheet each | the arc with moments, locked scripts, the brand in two sentences, the filter test |
| Staff | Reader (optional) | senior staff | operational | 30–50 pp | the design behind the instructions, cross-referenced to the book |
| Staff | Floor playbook | all FOH | floor | 30–60 pp bound | locked scripts in journey order, recovery triggers and scripts, moments of truth; lives at the host stand |
| Management | Facilitator guides | trainers | operational, floor quotes | 15–30 pp per module | intent, activities, prompts, assessment criteria, time budget; one per module plus one for the pre-shift ritual |
| Management | Operating handbook | managers | operational | 80–150 pp | brand summary, map and reasoning, pages in summary, recoveries, standards, manager-as-coach standard, assessment philosophy, the filter test |
| Management | Coaching guides | managers | operational | 5–10 pp each | one per topic: language, observations, follow-up |
| Management | Assessment instruments | managers | operational, floor quotes | 1–5 pp each | criteria, observation method, rubric, actions per score band |
| Management | Cadence calendar | all managers | operational | one document | every module, pre-shift theme, coaching topic and refresher across a year |

Founder and operations team approve the architecture before writing starts.

## Move 4 — Cadence

**Onboarding** (running venue): the five-session plan above, one trainee at a time, then shadow shifts, then sign-off. **Pre-opening**, four to six weeks (S4-01), sequenced brand → arc → design → execution → integration: week 1 brand and audience · week 2 the arc and the moments, wall chart up · week 3 the moments of truth, pairs practice, role cards out · week 4 recovery and choreography, group practice · weeks 5–6 full rehearsals with friends-and-family service, certification; failed certification gets targeted coaching, not a pass. Ten to fourteen days available: the compressed sequence (S4-02), recoveries earlier, heavier self-study, and a written acknowledgement that choreography and recovery will be rough for the first four to six weeks.

**Post-opening**: pre-shift daily 15–20 min as a ritual, brand point first, operations after, readiness check last (S4-06) · weekly coaching 15–30 min per direct report on the standing rotation · monthly refresher 30–60 min, one module, accelerated where assessment shows gaps · the first-thirty-days plan with the practice still engaged (S4-03); Stage 4 closes thirty days after opening, not on opening night.

## Move 5 — Write the materials

Three disciplines: one document, one job · show the design, do not summarise it (the why lives in the reader and the facilitator guide, not the workbook) · test by reading aloud and rewrite where it breaks (S4-05); expect drafts to lose 40–60 %. Allergen, alcohol and claim lines are checked against `fact-sheet.md` before they reach a card. Where an AI persona carries a moment, the disclosure line is on the card (guardrails 6). Drafts go to the founder and the operations team before finalising.

## Move 6 — Coaching infrastructure

The four components, integrated into the cadence so the operation runs them without the practice: the manager-as-coach standard, written into evaluation (S4-07) · the pre-shift ritual with its own facilitator guide and the three standing formats (standing moment, standing scenario, standing customer) · the standing rotation across pre-shifts, coaching and refreshers · the assessment loop (floor audits, table audits, mystery guest where commissioned) feeding the rotation. Add an annual **register audit** so workbooks do not accrete operational prose and handbooks do not accrete scripts (section 3.3, failure 5).

## Move 7 — Close the programme

Six questions, yes/no with the fix: every designed moment reaches the floor in floor register · each document has one job · floor material passed the read-aloud test · pre-opening cadence sequenced with real practice time, even if opening moves · the four coaching components in place · the operation can run it without the practice.

Then the **proof set**, because a programme is finished when the floor changed, not when the documents were handed over (quality plan WS5). Three instruments, all from templates in `templates/client/training/`:

1. **Certification** (`training/certification.csv`): every role card ends with ten observable checks drawn from its HIGH and MEDIUM moments (the locked line said as written, the threshold behaviour, the recovery code known, the allergen line correct …). The manager-as-coach watches each person on one service and ticks the ten; 8 of 10 with no HIGH item failed certifies; a fail is rechecked within a week. One row per person per role card, initials only (names and the signed sheets stay in Drive), signed by the manager, never by the practice. The roster rows are written here uncertified; the manager fills them in the first two weeks; `status.json` › `audit.certified` reads "n of m".
2. **Behaviour KPIs** (`training/behaviour-kpis.md`): two observable behaviours per HIGH moment, taken from the design page's DO line and success metric, counted by the manager-as-coach on the same service once a week for four weeks after go-live, with n. Targets are the pages' success metrics; a page without one gets "≥ 8 of 10". The four weekly counts are the thirty-day read.
3. **Thirty-day register audit**: the review date the cadence already carries becomes a scored visit on the house frame, `templates/client/data/mystery-visit.md`, by someone the floor does not know (the same visitor rule as the diagnosis); its score (HIGH moments at 3 / 2 / 1) and sheet path go to `status.json` › stages › 4 Training › `audit`, and the account manager books the date on the calendar at handoff. The audit, the counts and the certification roster are read together at the thirty-day review; what drifted becomes next month's standing pre-shift format (Move 6), and the quarterly service audit on the rate card is offered as the standing follow-up, never pushed.

Nothing in the proof set is filled by the practice from memory: a count not taken is an empty cell, an audit not held is "overdue" in `status.json`, a person not watched is uncertified.

## Handoffs (§ 2.4.6)

Three, documented (who received what, when, first scheduled use): the management team (the management stack, a structured session with Q&A) · the operations team (kitchen and bar: the small set they will use) · the founder (the full stack, with the brand book, the map and the handbook, and the first-thirty-days plan as the closing document).

## Harvest and retrospective (§ 2.4.7)

New Stage 4 patterns, template refinements, library entries (coaching-ready treatments of NV and BE), the engagement-level retrospective across all four stages (what worked, what did not, what changes next time), and the Part IV worked-example recommendation. A full day. `[client]/archive/harvest-stage-4.md` and `retrospective.md`.

## Output

`[client]/training/` with `architecture.md`, `registers.md`, `cadence-calendar.md`, `staff/` (workbooks by role, role-cards, wall-charts, floor-playbook, reader if any), `management/` (facilitator-guides by module, operating-handbook, coaching-guides, assessment), `handoffs.md`, `first-thirty-days.md`, `certification.csv`, `behaviour-kpis.md`; `status.json` › stages › 4 Training › `audit` with the planned date. Claude Docs for anything the founder reviews.

End with one line: documents produced per stack (or the minimum set, with omissions recorded), cadence chosen (onboarding, standard or compressed) and why, the sign-off criteria, the three handoff dates, the thirty-day audit date and who visits, people to certify, what is "to confirm" and who confirms it, and the next step (the engagement harvest, `vios-engage:vios-harvest`). Then stop.
- **Chase list**: `[client]/open-facts.md`, one table for the whole engagement, appended at every stage: fact needed · which moment, page or section it blocks · who holds it · asked on · due. Every "to confirm" in the deliverable points at a row here; the account manager works the list, nobody else. Say in the final line how many rows are open and which one blocks the stage from closing.


## Example (one idea in three registers; brewery; placeholders)

Concept: the brand refuses to narrate the room; the walk from the door is the room's first chance to work on the guest. Operational: after the locked greeting, lead slightly ahead in silence at a moderate pace; indicate the seat without speech; begin the seating sequence once the guest settles. Floor (role card, host): "Lead. Don't talk. The room does the work."
