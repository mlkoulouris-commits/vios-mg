# Eval runs

One block per run, headed `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`: the table (case id · expected · got · pass/fail) and what was changed as a result.

## 2026-11-02 · vios-marketing 0.5.0 · session: subagent, parent 3ab1bdf5, after 8f14f68

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| mr-01-no-baseline-on-file | Baseline column 'no baseline' on both scoreboards; Jun–Aug not computed; priority #1 = measure month-0 baseline (vios-engage:vios-engagement-setup step 7); one open-facts row for A.; report goes on | Step 1 (D0) put 'no baseline' in both Baseline columns, declined the Jun–Aug build in one line ("the baseline is made by setup step 7, never here"), set section 7 priority #1 'measure the month-0 baseline' → vios-engage:vios-engagement-setup step 7, wrote one open-facts.md row for A., kept Oct 2,410 vs Sep 2,180 history columns | pass | D0 wording followed verbatim |
| mr-02-promise-first-latest-written-back | Promise row first: covers per month · 2,050 · 2,300 · 2027-01-31 · 2,410 (n 27) · contribution; kpis[0].latest = 2410, latest_date = report date; no met/not met; no 'caused' | Section 2 opened with that row before the metric table; status.json › kpis[0].latest = 2410, latest_date = 2026-11-02; due not passed so no reading; attribution printed as 'contribution'; target untouched | pass | — |
| mr-03-not-trading | Column 'no baseline yet: venue opened 2026-10-12'; Nov 2026 becomes the baseline via setup step 7 (A. books it); not in the three priorities; no baseline page; 19 days as this month, n 19, 'building baseline' | Column read 'no baseline yet: venue opened 2026-10-12'; declined to make October the baseline; said November 2026 is the first full month and becomes the baseline through setup step 7 with an open-facts row for A. to book it; priorities kept free of 'measure the baseline'; this month 19 days, n 19, labelled 'building baseline', not scaled | pass | "A. books it" came from the open-facts routing, not a skill line; the skill only says the measuring is not a priority of this report |
| mr-04-no-kpis-promised | One line 'no outcome KPIs promised; see the proposal', then the scoreboard; no target written; route = proposal 'What we aim to move' (vios-proposal step 3) | Section 2 opened with that line and went to the scoreboard; the covers target was refused, with the route named as vios-proposal step 3's 'What we aim to move' table; status.json › kpis left empty | pass | — |

Result: 4 of 4 pass. Nothing changed.
