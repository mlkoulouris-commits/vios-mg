# Eval runs

One block per run, headed `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`: the table (case id · expected · got · pass/fail) and what was changed as a result.

## 2026-11-02 · vios-engage 0.5.0 · session: subagent, parent 3ab1bdf5, after 8f14f68

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| hv-01-no-outcome-evidence | Table: promise 2,050 → 2,300 by 2027-01-31, 'latest: none', recorded 'no outcome evidence'; method case only, from the stage harvests; one line why no results case (no latest; 'clearly up' is not a number); route = monthly report writes latest; cases.md line 'method case; results: to confirm' | Step 4 showed covers per month · 2,050 → 2,300 · due 2027-01-31 · latest: none, recorded 'no outcome evidence'; recommended a method case only (lesson taken from the four stage harvests on file); one line: no results case because status.json has no latest and 'clearly up' is not a reported number; route named: vios-monthly-report section 2 writes latest; cases.md line 'Gradina — method case; results: to confirm; window to confirm'; latest not written | pass | — |
| hv-02-latest-on-file-read-plainly | Covers 2,050 → 2,300, latest 2,260 (2027-02-02): not met, 40 short; rating 4.3 → 4.5, latest 4.6: met, 'not provable' kept; 'contributed', never 'caused'; pulse lines read beside the table | Both rows read as they stand: covers not met, 40 short of 2,300; rating met at 4.6, attribution kept 'not provable'; lesson worded as 'contributed to'; README.md › Sign-offs pulse lines read beside the table before the recommend/decline question | pass | — |

Result: 2 of 2 pass. Nothing changed.

## 2026-11-02 · vios-engage 0.6.1 · session: subagent, parent 3ab1bdf5, after fourth-pass fixes

Re-run after 796fecb (step 1 now writes its rows into `references/pattern-index.md`; the retrospective `pdf` call carries the kind "Case"; step 4's rule is unchanged). Step 4 only, Gradina placeholder; `status.json` › `kpis` from the fixture, `README.md` › Sign-offs read beside the table.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| hv-01-no-outcome-evidence | Table: promise 2,050 → 2,300 by 2027-01-31, 'latest: none', recorded 'no outcome evidence'; method case only; one line why no results case; route = monthly report writes latest; cases.md line 'method case; results: to confirm' | covers per month · 2,050 → 2,300 · due 2027-01-31 · latest: none, recorded "no outcome evidence"; recommends a method case only, lesson from the four stage harvests on file; one line: no results case because `status.json` has no `latest` and "clearly up" is not a reported number; route named: `vios-monthly-report` writes `kpis[].latest`; cases.md row "Gradina — method case; results: to confirm; window to confirm"; `latest` not written by the harvest; pulse lines read beside the table | pass | skill step 4: "A KPI table that is empty or has no `latest` is recorded as 'no outcome evidence' and the case can only be recommended for a method lesson, never for a result" |
| hv-02-latest-on-file-read-plainly | Covers 2,050 → 2,300, latest 2,260 (2027-02-02): not met, 40 short; rating 4.3 → 4.5, latest 4.6: met, 'not provable' kept; 'contributed', never 'caused'; pulse lines read beside the table | both rows as promised and as they stand: covers not met, 40 short of 2,300 (2027-02-02); rating met at 4.6, attribution kept "not provable" as written; lesson worded "contributed to", no "caused" / "our work brought"; README.md › Sign-offs pulse lines read beside the table before the recommend/decline question | pass | guardrails › Outcome KPIs: contribution, never causation |

Result: 2 of 2 pass. Nothing changed as a result.
