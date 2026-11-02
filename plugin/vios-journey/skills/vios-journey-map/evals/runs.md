# Eval runs

One block per run, headed `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`: the table (case id · expected · got · pass/fail) and what was changed as a result.

## 2026-11-02 · vios-journey 0.7.0 · session: subagent, parent 3ab1bdf5, after 8f14f68

Step 3 (Moves 2, 2b) only, placeholder venue Gradina, fixture = whole client file. Skill unchanged.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| jm-01-weights-before-observation | no observation.md; provisional note, cover 'provisional, unobserved', every HIGH brand-led, re-weighting 'observation + 14 days'; open-facts rows: shadowed services (A.) first, mystery visit second; asks once, goes on | Step 3 showed the phase lines and "mystery visit: none · shadowed services: none · review read: none"; declined to weight from the book ("the brand book ... cannot say what guests do"); wrote the provisional note, not observation.md; cover line "provisional, unobserved · all HIGH brand-led · re-weighting: observation + 14 days"; open-facts row 1 two shadowed services, holder A., blocks final weights; row 2 mystery visit, holder A.; status.json blocker "observation outstanding, map provisional"; asked once "Observation on file, or do we issue provisional?" and went on | pass | Move 2b › Re-weighting date applied verbatim ("issued provisional, every HIGH marked brand-led ... 'observation + 14 days'") |
| jm-02-mystery-visit-first | observation.md opens with the visit as (0) mapped to M01–M28, then services (1), review read (2) re-tagged; no second visit; candidates HIGH/MEDIUM reported; no weights set | observation.md: (0) mystery visit 2026-10-20, timeline mapped to M01–M28 with scores; (1) Thursday dinner 2026-10-27, Sunday lunch 2026-11-01; (2) review-mining 2026-10-18 re-tagged to moment codes, not extended (15 days < 90); no second visit (13 days, same concept); reported candidate HIGH (unprompted mentions, hesitation) and candidate MEDIUM (book-important, unnoticed) for the Reasoning Note; weights left to step 4 | pass | — |
| jm-03-venue-not-yet-open | two services planned at the comparable venue, in observation.md named as comparable; cover 'provisional, unobserved' + comparable named; re-weighting 30–60 days after opening as a condition; visit and review read as open-facts rows dated after opening; never 'no observation possible' | observation.md plans two services (different dayparts) at the named Lozenets garden restaurant, each headed "comparable-venue observation, not Gradina"; cover: "provisional, unobserved · comparable venue: <Lozenets> · re-weighting 2027-06-14 to 2027-07-14, condition of the map, owner A."; open-facts: mystery visit due 2027-06-14, review read due at re-weighting, both holder A.; the remote clause was not invoked | pass | Move 2b (1) parenthetical applied; the after-opening dates follow "until the venue's own observation at the re-weighting date" |

Changed as a result: nothing.
