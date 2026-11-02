# Dry run — the 2026-11-02 steps on the DEMO client Gradina (2026-11-02)

Purpose: prove that the steps added on 2026-11-02 (intake's fourth question, the proposal's "What we aim to move" table, setup step 7 Baseline, `status.json` › `kpis` and `baseline`) hold together end to end, and list the friction. Method: the three `vios-engage` skills were run in order on `clients/demo-gradina/` (fictional venue, founder "Nadia Petrova (founder, DEMO)"). **The founder and the account manager were both played by the practice; every founder answer below is invented for the test and says so in the files.** No ClickUp task, Drive folder or calendar event was created (the DEMO has no lists); each is recorded as "would create". No number was pulled from a POS, Metricool or Google: the DEMO has no data, so the run tests the to-confirm paths, the file writes and the `status.json` / `open-facts.md` bookkeeping. Nothing committed; no plugin file touched.

## What was run and what it produced

| # | Step | Founder's (invented) input | Produced |
| --- | --- | --- | --- |
| 1 | `vios-intake` move 2, fourth question | three measures: "80 covers a Fri/Sat evening" (a number) · "tables that rebook before leaving" (to measure) · "half the tables by word of mouth" (no monthly source) | `clients/demo-gradina/README.md` › Move 2 (measure · today · wanted table, the dropped one named); `open-facts.md` rows 6–10 |
| 2 | `vios-proposal` steps 3–5 as v2 | scope, deliverables, timeline, price unchanged from v1 | `clients/demo-gradina/proposal-v2.md` (§ 4 KPI table, go-live = opening 15 Apr 2027, the fixed attribution sentence, "Not promised" paragraph; § 6 diagnostic sprint line "to confirm"); `proposal-v2-deliverables.md` from `templates/proposal/deliverables-sheet.md`; `deliverables/Gradina-DEMO-What-you-get-v2.pdf` (+ `.html`) via `clients.py pdf`; `status.json` › `proposal` v2 not sent, `kpis` (2 rows, attribution contribution, due 2027-07-14); README › Proposal table (v1 superseded) |
| 3 | `vios-engagement-setup` step 7 Baseline | nothing to pull: the venue opens 15 Apr 2027 | `clients/demo-gradina/data/baseline-2026-11.md` (every row "to confirm", holder and open-fact number per row in § 6, reading in § 7); `deliverables/Gradina-DEMO-Baseline-2026-11.pdf`; `status.json` › `baseline` partial, 4 missing groups; blockers 6, 7, 9; README › Setup line. `git check-ignore` confirms the page, its PDF and HTML are ignored |
| 4 | Check | — | `clients.py check demo-gradina` → ok; `clients.py facts demo-gradina` builds the ten-task payload (would create in "Gradina — Open facts") |

Would create in ClickUp (not done): "Proposal Gradina (DEMO) — awaiting signature" (Deliverables, Stage Engagement, Review); "Baseline Gradina (DEMO)" (Stage Engagement, Review, missing rows in the description); open-facts tasks #6–#10.

## The card after the run (`python scripts/clients.py status demo-gradina`)

```
**Gradina (DEMO)** — 0 intake · approver: Nadia Petrova (founder, DEMO) · updated 2026-11-02
Proposal: not sent (v2) · marketing loop: in · baseline: partial 2026-11-02, 4 to confirm
Stages: Brand in/not started · Map in/not started · Design in/not started · Training in/not started
KPIs: covers per Friday and Saturday evening, garden measured in week 1 after opening → 80 · tables that book their next visit before leaving measured in week 1 after opening → set at baseline (practice proposes one step after May 2027, labelled as ours)
Blocked by: Budget and target spend per head (founder); POS system and a covers-by-day export (founder); Booking system that records a rebooking made on site (founder) +1 more
Open facts: 10, 0 overdue
Next: Send the v2 PDF (with the KPI table) to Nadia; on signature run vios-engagement-setup steps 1-6, then re-measure the baseline in May 2027  →  vios-engage:vios-proposal
```

Verdict: the three steps hold together. The intake's three lines became two KPI rows and one "not promised" paragraph; the rows reached `status.json` in the shape the card and the report read; the baseline's to-confirm path wrote the page, the open facts, the blockers and the partial status without a single invented number. The friction is around the edges, mostly the pre-opening case.

## Friction points (ranked by impact, fix suggested)

1. **The installed plugin is not the repo plugin.** The Skill tool loaded `vios-engage` from the claude.ai cache: no fourth question, no KPI table, six setup steps. The new steps exist only in `plugin/vios-engage/` (0.4.0). A session that trusts the loaded skill runs the old method and never knows. Fix: upload engage 0.4.0 (hygiene list, quality plan WS6); until then the front door prints "installed vX / repo vY" from `plugin.json`, and `CLAUDE.md` says to read the repo `SKILL.md` when they differ.
2. **The baseline assumes a trading venue.** Template and step 7 measure "the trailing 3 full months"; for an opening every row is "to confirm" and `partial` misdescribes it (nothing is missing, nothing exists yet). Fix: a fourth status `not trading` in the schema and the card; a rule in step 7: for an opening, month 0 is one line and the baseline is the first full month of trading, written then (`baseline-2027-05.md` here) and dated then.
3. **Go-live is undefined for an opening.** The proposal counts the 90 days from "first published post, or the first stage sign-off"; here the loop starts in Feb 2027 and nothing can be counted before 15 Apr. The run chose opening day and said so. Fix: add "opening day for a venue not yet trading" as the third go-live definition in proposal step 3 and in the sheet template; "measured in week 1" becomes "measured in month 1 after opening" for that case.
4. **Proposal step 5 contradicts the contract.** It still says render with Adobe `markdown_to_pdf`, save as `[client]/proposal-v1-deliverables.pdf`, task "in the department's setup list"; the contract, the operating system and v1 use `clients.py pdf` → `deliverables/` and the client's Deliverables list. Fix: rewrite step 5 to the contract wording; name the files vN, not v1.
5. **A dropped KPI has no home.** The skill drops a measure without a monthly source, but neither `status.json` nor the doc structure has a line for it; the harvest and v3 would lose the founder's words. The run added a "Not promised" paragraph under the table and open-fact 8 by hand. Fix: make that paragraph part of step 3 / doc § 4 ("not promised · why · what would make it measurable"), and an open-facts row per dropped measure.
6. **The diagnostic sprint does not fit an opening.** Offered "when the founder cannot name a number", but its content (baseline page, review mining) has nothing to read before trading. Shown as "to confirm". Fix: step 3 says trading venues only; the pre-opening alternative, if any, is a competitor review read, named as such.
7. **One proposal object in `status.json`.** v1's "superseded" state has nowhere to live once v2 is written; the run put a Proposal table in README. Fix: either `proposal.history[]` in the schema or the skill names README › Proposal as the version record.
8. **"Today" means two things.** The intake writes "today's number as the founder says it"; the proposal says "today" never comes from memory. A founder-stated number would be memory. Fix: the intake line is the founder's claim, kept in the record only; the table's "Today" column reads only the baseline page or "measured in …".
9. **Every gap becomes a blocker.** The contract says a gap is a row in open facts and a blocker in `status.json`; after step 7 the DEMO has 4 blockers for 10 open facts and the card shows "+1 more". Fix: blocker only when it blocks `next_action` or the current stage; the rest stay open facts.
10. **`clients.py new` leaves `accounts.md` as "<Client>"** with empty rows; setup step 1 says "ids known so far" but nothing writes "to confirm" there. Fix: `new` substitutes the name; step 7 adds POS and booking rows as "to confirm" when the baseline cannot read them.
11. **A sentence as a KPI target.** KPI 2 has no number yet, so `target` is a sentence and the card's KPI line runs to three lines. Fix: `target: "set at baseline"` plus an optional `target_note`; the card cuts a target at ~40 characters.
12. **The client sheet is cover + 3 pages**, against the skill's "1–2 pages", after the KPI section and its two paragraphs. Fix: say "cover + up to 3" in the skill, or move the "not in the table" line to the doc only.
13. **A practice-side to-confirm lands in the client's chase list.** Open-fact 10 (sprint price, held by the practice owner) goes into "Gradina — Open facts" via `facts`. Fix: practice-held rows go to "Department — Setup & SOP"; `facts` skips holder = practice owner.

## Not run

Setup steps 1–6 (lists, Drive, calendar, keys): nothing to make for a DEMO. Intake steps 1, 3–6 and proposal steps 1–2 were read, not rerun; their v1 content stands. No ClickUp, Drive or calendar call; no `release.py`.

## Next

Fixes 1–6 are skill or schema edits (method unchanged except 2 and 3, which add a pre-opening case and need the owner's word). Delete `clients/demo-gradina/` when the walk-through is no longer needed; its `data/` page and Baseline render are already outside git.
