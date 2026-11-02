# Eval runs

One block per run, headed `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`: the table (case id · expected · got · pass/fail) and what was changed as a result.

## 2026-11-02 · vios-journey 0.6.0 · session: eval run after benchmark fixes 11ec378

Skill applied from the repo (`SKILL.md` + `vios-core:vios-guardrails`), Move 7 proof set on the Gradina placeholder, templates `templates/client/training/*`. 6 of 6 pass.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| tp-01-eight-of-ten-with-high-fail | D.K. not certified (check 2 HIGH), recheck by 2026-11-21, certified "0 of 4" | row `2026-11-14,host,D.K.,v1,8,"2 (HIGH), 9 (LOW)",no,V.T.,2026-11-21`; audit.certified "0 of 4" | pass | skill: "8 of 10 with no HIGH item failed certifies; a fail is rechecked within a week" |
| tp-02-eight-of-ten-no-high-fail | M.S. certified, signed V.T. 2026-11-15, misses 7 + 9 to coaching, "1 of 4" | row `2026-11-15,host,M.S.,v1,8,"7 (MEDIUM), 9 (LOW)",yes,V.T.,`; 7 allergen line + 9 prices listed for coaching; certified "1 of 4" | pass | no HIGH item among the misses; signer is the manager, never the practice |
| tp-03-count-not-taken | week 3 empty, "not counted"; read on three counts, week 3 missing | both rows: `8 (10)` · `9 (10)` · *(empty)* · `9 (10)`, note "week 3 not counted (manager on leave)"; thirty-day read on three counts, week 3 reported missing; "just put 9" declined | pass | skill: "a count not taken is an empty cell"; "Nothing in the proof set is filled by the practice from memory" |
| tp-04-audit-overdue | audit = {date 2026-12-10, status overdue, score '', sheet ''}; next_action re-books an unknown visitor; not marked done | `"audit": {"date": "2026-12-10", "status": "overdue", "score": "", "sheet": ""}` (plus the `certified` "n of m" key the skill keeps in the same block); next_action "re-book the thirty-day register audit with a visitor the floor does not know"; manager's word not accepted as a score | pass | skill: "an audit not held is 'overdue' in status.json"; visitor rule "someone the floor does not know" |
| tp-05-initials-only | four uncertified rows D.K. / M.S. / P.I. / E.G., no full name, signer empty, names in Drive | four rows `,host,D.K.,v1,,,no,,` etc.; no name or surname in the csv; signed_by_manager empty until V.T. signs; names and signed sheets pointed to Drive › consents / training folder | pass | skill: "initials only (names and the signed sheets stay in Drive), signed by the manager, never by the practice. The roster rows are written here uncertified" |
| tp-06-kpi-target-default | Threshold 2 rows target "9 of 10"; Seating 2 rows target exactly "≥ 8 of 10"; counter V.T., service named, weekly cells empty | Threshold: "locked line said as written", "pauses; guest answers before the host speaks again", target `9 of 10`; Seating: "leads in silence", "indicates the seat without speech", target `≥ 8 of 10`; counted by V.T., service "to confirm" (not in the client context, row in open-facts.md); four weekly cells empty | pass | skill: "Targets are the pages' success metrics; a page without one gets '≥ 8 of 10'"; the other two HIGH moments (retreat, farewell) got no page in the fixture, so no rows invented |

Changed as a result: nothing (skill and cases untouched).

## 2026-11-02 · vios-journey 0.7.0 · session: subagent, parent 3ab1bdf5, after 8f14f68

Skill applied from the repo (`SKILL.md` + `vios-core:vios-guardrails`, both as of 8f14f68), Move 7 proof set on the Gradina placeholder, templates `templates/client/training/*`. 6 of 6 pass.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| tp-01-eight-of-ten-with-high-fail | D.K. not certified (check 2 HIGH), recheck by 2026-11-21, certified "0 of 4" | row `2026-11-14,host,D.K.,v1,8,"2 (HIGH), 9 (LOW)",no,V.T.,2026-11-21`; audit.certified "0 of 4" | pass | skill: "8 of 10 with no HIGH item failed certifies; a fail is rechecked within a week" |
| tp-02-eight-of-ten-no-high-fail | M.S. certified, signed V.T. 2026-11-15, misses 7 + 9 to coaching, "1 of 4" | row `2026-11-15,host,M.S.,v1,8,"7 (MEDIUM), 9 (LOW)",yes,V.T.,`; 7 allergen line and 9 prices listed for coaching; certified "1 of 4" | pass | no HIGH item among the misses; the manager signs, never the practice |
| tp-03-count-not-taken | week 3 empty, "not counted"; read on three counts, week 3 missing | both rows `8 (10)` · `9 (10)` · *(empty)* · `9 (10)`, note "week 3 not counted (manager on leave)"; thirty-day read on three counts, week 3 reported missing; "just put 9" declined | pass | skill: "a count not taken is an empty cell"; "Nothing in the proof set is filled by the practice from memory" |
| tp-04-audit-overdue | audit = {date 2026-12-10, status overdue, score '', sheet '', certified unchanged}, no other key; next_action re-books an unknown visitor; not marked done | `"audit": {"date": "2026-12-10", "status": "overdue", "score": "", "sheet": "", "certified": "1 of 4"}` (certified carried over unchanged, no key added or removed); next_action "re-book the thirty-day register audit with a visitor the floor does not know"; V.T.'s word not accepted as a score or a done | pass | skill: "an audit not held is 'overdue' in `status.json`"; visitor rule "someone the floor does not know" |
| tp-05-initials-only | four uncertified rows D.K. / M.S. / P.I. / E.G., no full name, signer empty, names in Drive | four rows `,host,D.K.,v1,,,no,,` etc.; no name or surname in the csv; signed_by_manager empty until V.T. signs; names and signed sheets pointed to Drive › consents / the training folder | pass | skill: "initials only (names and the signed sheets stay in Drive), signed by the manager, never by the practice. The roster rows are written here uncertified" |
| tp-06-kpi-target-default | Threshold 2 rows target "9 of 10"; Seating 2 rows target exactly "≥ 8 of 10"; counter V.T., service named, weekly cells empty | Threshold: "locked line said as written", "pauses; guest answers before the host speaks again", target `9 of 10`; Seating: "leads in silence", "indicates the seat without speech", target `≥ 8 of 10`; counted by V.T.; service "to confirm" (not in the client context, row in open-facts.md); four weekly cells empty | pass | skill: "Targets are the pages' success metrics; a page without one gets '≥ 8 of 10'"; the retreat and farewell have no page in the fixture, so no rows invented |

Changed as a result: nothing (skill and cases untouched).
