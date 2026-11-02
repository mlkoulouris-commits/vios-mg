# Eval runs

One block per run: date · plugin version · session id · table (case id · expected · got · pass/fail) · what was changed as a result.

## 2026-11-02 · vios-engage 0.4.0 · session: eval run after benchmark fixes 11ec378

Step 3 run on the Gradina placeholder with the case's rate-card lines (S1 4,800 · S2 2,400 · marketing 900/mo · day rate 450); repo `setup/rate-card.md` read for the sprint and partner-brief rules, guardrails › Outcome KPIs for the attribution rule.

| Case | Expected | Got | Pass/fail | Note |
| --- | --- | --- | --- | --- |
| pr-01-no-number-named-no-baseline | covers Tue–Thu · measured in week 1 · set at baseline · Memento, monthly, n | covers per month Tue–Thu · "measured in week 1" · "set at baseline" (`target_note`: step set once the week-1 figure exists) · Memento covers by weekday · monthly · n ≥ 30; no figure | pass | with no baseline a "one step" cannot be computed, so the skill's "or reads 'set at baseline'" branch is the only read |
| pr-02-kpi-without-monthly-source | no awareness row; one-line "Not promised"; stand-in labelled proposal | no "brand awareness" row; under the table *"Not promised: brand awareness, no monthly source"*; stand-in row "GBP profile views per month · measured in week 1 · set at baseline (practice proposal) · GBP · monthly · n"; open-facts row "brand-tracking source, could be built" | pass | every row has a named source; table ≤ 4 rows |
| pr-03-practice-step-is-one-step | Today 1,100 (baseline cited); one modest step, "practice proposal"; "we aim" | Today = 1,100 (data/baseline-2026-10.md, Memento pulled 2026-10-30, n 3 months) · In 90 days = 1,200 (practice proposal, one step) · "we aim to move"; no guarantee wording | pass | skill does not size "one step"; +9 % chosen, well under double |
| pr-04-attribution-sentence-verbatim | sentence verbatim; rewrite declined in one line | sentence under the table word for word; decline: "the practice claims contribution, never causation (guardrails › Outcome KPIs); the sentence is fixed and not softened"; no variant offered | pass | skill › Rules: "The attribution sentence is never softened or dropped" |
| pr-05-sprint-not-on-rate-card | no sprint offered or priced; KPI row "set at baseline"; owner row | no sprint line, no offer in the step text; KPI row as pr-01; one row "diagnostic sprint price: to confirm with the practice owner" (holder practice owner → Department list via `clients.py facts`) | pass | skill: "Diagnostic sprint (rate card; only when the line exists there …)" |
| pr-06-sprint-on-rate-card | one line 1,200 · 2 weeks · credited vs Stage 1 in 30 days · plain | price table gains one line "Diagnostic sprint (2 weeks) · 1,200 · baseline page + review mining + one-page findings · credited against Stage 1 when signed within 30 days"; offered once, stages not conditional on it, no deadline wording | pass | fixture price 1,200 used (repo card says 1,500: fixture wins per `how`) |
| pr-07-price-not-on-rate-card | architect row "to confirm with the practice owner"; total excludes it; open-facts row | architect brief row = "to confirm with the practice owner"; total 7,200 + 900/mo "excluding the architect brief"; output line "prices to confirm"; open-facts row holder practice owner | pass | no figure inferred from designer brief (600) or day rate; repo card's 900 partner-brief line ignored because the fixture strikes it |

7/7 pass. Nothing changed as a result.
