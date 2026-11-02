# Quality plan — closing the gap to the best F&B consultancies

Status: DRAFT for the owner's edits, 2026-11-02. Nothing here is built yet.

Bottom line: the method (Stages 1–4, QA, governance) already scores 4/5. The gaps are around it: no baseline before we start, thin guest research, no outcome promise in the proposal, no financial lens, no proof after training, no case with numbers. Six workstreams, ordered by value. Each one names the skill it changes, the files it adds, and what "done" looks like.

Benchmark (from public method descriptions, not audits): Aaron Allen, Horwath HTL (F&B strategy); Pentagram, Lippincott (brand); Disney Institute, Ritz-Carlton, Hospitality Quotient (service, training); top restaurant marketing agencies (reporting).

## Scorecard today

| Area | Score | Why |
| --- | --- | --- |
| Brand strategy (Stage 1) | 4 | 14 interrogations, message architecture, filter test = agency depth |
| Journey and service design (Stages 2–3) | 4 | weighted moments, signature, peak, end, recovery; ONE Gallery delivered |
| QA and governance | 4.5 | evals, versioned method, hard pre-publish gate, audit trail |
| Reporting honesty | 4 | n beside every %, attribution language |
| Month-0 baseline | 2 | nothing measured before work starts |
| Guest research | 3 | owner interview + desk work; no guests, no mystery visit |
| Intake and proposal | 3 | free four-question intake, fixed fees, no outcome KPIs |
| Financial lens | 2.5 | Memento data exists, the process never uses it |
| Training proof | 3 | no certification, no post-training audit |
| Proof and scale | 2.5 | no case with numbers; one person; uploads pending |

Target after this plan: every row at 4 or above.

## Workstream 1 — Month-0 baseline (highest value)

What: a one-page baseline per client, measured before any deliverable, so the 30-day and 90-day reports show change, not just activity.

Measures (one row each, with source and n):
- Covers, revenue, average check, items per cover — Memento POS / Barsy export (or the client's POS export when not on Memento)
- Labour cost % — Memento labor module
- Reviews: count, average rating, last-90-day velocity — Google Business, TripAdvisor
- Social: followers, reach, engagement rate — Metricool / Windsor
- Bookings by source — Memento reservations, or the client's book
- Guest sentiment: top 5 praise themes, top 5 complaint themes — review mining (workstream 2)

Changes:
- `vios-engagement-setup` gets step 7 **Baseline**: pulls what is reachable, writes `clients/<slug>/data/baseline-YYYY-MM.md`, rows it cannot fill go to `open-facts.md`.
- `vios-monthly-report` D1 reads the baseline and shows "vs baseline" beside every venue number.
- `templates/client/data/baseline.md` template; `status.json` gains `baseline: { date, status }`.
- Rate card: baseline included in every engagement (no new line).

Done when: Stochna and Atelier each have a baseline file dated before 2026-12-01, and the December report compares against it.

State 2026-11-02: skills, template, schema, card and guardrails built (engage 0.3.0, marketing 0.4.0, core 0.6.0); Stochna and Atelier baselines not yet measured.

## Workstream 2 — Guest research in the diagnosis

What: the diagnosis hears guests, not only the owner.

Three inputs, all cheap:
1. **Review mining** — last 200 reviews (Google, TripAdvisor, Facebook) coded into themes with counts. Skill does this from a paste or export.
2. **Guest interviews** — 8–10, 15 minutes each, five fixed questions, held by the account manager or the owner on the floor; transcribed into `data/guest-interviews.md`. Consent line per interview (Drive, never git).
3. **Mystery visit** — one visit by someone outside the venue, scored on the house journey template (threshold, first contact, peak, end, recovery); `data/mystery-visit-YYYY-MM-DD.md`.

Changes:
- `vios-brand-diagnosis` step 4 Audience reads all three before drafting the persona; a new sub-step **Guest evidence** shows theme counts and the three strongest quotes.
- `vios-journey-map` Move 2b (observe before weighing) takes the mystery visit as its first observation.
- Templates: `templates/client/data/interview-guide.md` (the five questions, EN/BG), `review-mining.md`, `mystery-visit.md`.
- Rate card: "Guest research pack" 900 (review mining + 10 interviews + 1 mystery visit), inside Stage 1 by default, sold alone for marketing-only clients.

Done when: a diagnosis cannot pass step 4 without at least review mining on file (blocker in `status.json` otherwise).

## Workstream 3 — Outcome KPIs in the proposal

What: every proposal names what should move, by how much, by when — and the report tracks it.

Changes:
- `vios-intake` move 2 Scope adds the question "What should be different in 90 days, in numbers?" (covers, check, rating, reach, labour %). Owner's answer or "to set at baseline".
- `vios-proposal` step 3 gains a **What we aim to move** table: KPI · baseline (from WS1, or "measured in week 1") · 90-day target · how measured. Attribution language from guardrails (we claim contribution, not causation).
- `status.json` gains `kpis: [{ name, baseline, target, due, latest }]`; `vios-monthly-report` section 2 prints them first.
- `vios-harvest` move 4 Case recommendation requires the KPI table filled — the case lesson is the KPI story.
- Paid diagnostic option: rate card line "Diagnostic sprint" 1,500, two weeks, deliverable = baseline + review mining + one-page findings; credited against Stage 1 if signed within 30 days. Moves the intake from free to paid for serious prospects.

Done when: the next proposal (ONE Gallery revision or the next new client) carries the KPI table.

## Workstream 4 — Financial lens

What: the brand and journey work uses the venue's money numbers, the way F&B strategy firms lead with them.

Changes:
- `vios-brand-diagnosis` step 1 "The real business" gets a fixed **numbers page**: revenue mix by category, top 10 items by margin and by volume (menu engineering quadrant), labour %, COGS %, covers by daypart. From Memento when the client is on it; from a POS export otherwise; "to confirm" rows go to open facts.
- `vios-journey-design` each HIGH page gets one line **Cost of the moment**: staff minutes and any item cost, so the owner sees the price of the signature and the peak.
- `vios-monthly-report` section 4 "The link" uses the numbers page categories, so marketing push and sales move are read on the same lines.
- New reference: `plugin/vios-core/references/section-x-numbers-page.md` — definitions and the Memento report each number comes from (P&L, COGS analysis, labor cost, reservations).

Done when: Stochna diagnosis has a filled numbers page and one HIGH design page shows its cost.

## Workstream 5 — Training proof

What: training ends with a measurement, not a handover.

Changes:
- `vios-training-programme` move 7 Close adds: **certification** (each role card has a 10-line check; manager signs per person; `training/certification.csv`), **30-day register audit** (already a date — make it a scored visit on the mystery-visit template, same scorer as WS2), **behaviour KPIs** (two per HIGH moment, e.g. "greeting within 30 s", counted on one shift a week for four weeks).
- Rate card: Stage 4 includes the 30-day audit; "Quarterly service audit" 600 as a standing option after.
- `status.json` stage 4 gains `audit: { date, score }`.

Done when: the ONE Gallery or Stochna training close has a certification file and an audit date on the calendar.

## Workstream 6 — Proof and capacity

What: one case with numbers, and the operation able to serve more than one client at a time.

- **Case**: write the ONE Gallery case (Stages 1–4 delivered) in the house case form from `docs/cases.md`, with whatever numbers exist now and the KPI table from WS3 for the next quarter. Atelier case in April 2027 as already logged.
- **Baseline for the existing clients** now (WS1), so the first case has a before/after by Q1 2027.
- **Hygiene** (user-only, blocking): upload pending plugins (brand 0.3.5, journey 0.4.9, engage 0.2.1, marketing 0.3.3); delete the 12 stale claude.ai skill copies; fix the Instagram connector; confirm the rate card.
- **Capacity**: one account manager per three clients in the loop; the scheduled tasks already iterate clients; document the handoff in `docs/sop.md` so a second person can run a client from the board.

Done when: one case PDF exists in `clients/one-gallery/deliverables/` and the hygiene list is empty.

## Order and effort

| # | Workstream | Build effort | Touches | Blocks |
| --- | --- | --- | --- | --- |
| 1 | Baseline | 1 day | engagement-setup, monthly-report, templates, status schema | WS3, WS6 |
| 3 | Outcome KPIs | 1 day | intake, proposal, monthly-report, harvest, rate card | — |
| 2 | Guest research | 1.5 days | brand-diagnosis, journey-map, templates, rate card | — |
| 4 | Financial lens | 1.5 days | brand-diagnosis, journey-design, monthly-report, core reference | needs Memento read access per client |
| 5 | Training proof | 1 day | training-programme, status schema, rate card | — |
| 6 | Proof and capacity | 0.5 day + user hygiene | cases.md, sop.md | WS1 |

Release path per workstream: edit skill in repo → `release.py check` → package → sync cache → one blind test on Stochna or Atelier → commit → the user uploads. One writer at a time (CLAUDE.md rule).

Plugin versions after the plan: engage 0.3.0, brand 0.4.0, journey 0.5.0, marketing 0.4.0, core 0.6.0.

## Open questions for the owner

1. Diagnostic sprint at 1,500 — sell it, or keep the intake free?
2. Who holds the guest interviews: account manager, or the owner with our guide?
3. Mystery visit: Vios staff, or a paid outsider?
4. Which KPIs do we promise by default: covers, average check, rating, reach — or client's pick of three?
5. Financial numbers page for clients not on Memento: ask for a POS export, or skip the page?
6. Start order: 1 → 3 → 2 → 4 → 5 → 6 as above, or baseline + KPIs only first?
