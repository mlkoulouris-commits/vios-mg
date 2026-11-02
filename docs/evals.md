# Evals for the Vios skills

Eleven skills carry eval cases. Three are verdict skills, the ones whose output is a verdict and can be checked: `vios-consistency-qa`, `vios-ads-audit`, `vios-filter-test`. Each has `evals/cases.json` (the cases, inputs and expected results) and `evals/runs.md` (the log). `cases.json` is the only source `release.py check` reads and a session runs: a `cases` array, one object per case with an `id` and an expectation. The skill-creator folders beside three of them (`<case>/case.yaml`, `prompt.md`, `graders/`, `files/`) are an early subset and are not maintained; a case exists only when it is in `cases.json`.

Four more sets, added 2026-11-02 with the quality plan (WS1–WS5), guard the "never invent" rules of the stage skills on a placeholder venue (Gradina): `vios-brand-diagnosis` (step 1 numbers page without a POS export or costed recipes, the step 4 guest-evidence gate, the real attributed persona quote, a venue not yet open), `vios-proposal` (the "What we aim to move" table: founder's number or "set at baseline", one labelled step, no KPI without a monthly source, the attribution sentence verbatim, prices and the diagnostic sprint only from the rate card), `vios-engagement-setup` (step 7 baseline: measured vs partial, never estimated, under three months of trading, the page and PDF never committed, a loop client keeps its loop-start baseline) and `vios-training-programme` (Move 7 proof set: 8 of 10 with no HIGH fail, empty cells for counts not taken, audit "overdue", initials only, the "≥ 8 of 10" default target). Four more, added 2026-11-02 after the second benchmark, cover the gates that had none: `vios-journey-map` (Move 2b: observe before weighing, provisional weights, the mystery visit first, the comparable venue for a venue not yet open), `vios-journey-design` (the "Cost of the moment" line: no marginal cost, rate to confirm, never the reason to drop a HIGH), `vios-monthly-report` (D0 no baseline / partial / not trading, the promise printed first, `kpis[].latest` written back) and `vios-harvest` (step 4: no outcome evidence → a method case only). Same shape, same run procedure, placeholder venue Gradina.

Count on 2026-11-02: **69 cases** across the eleven sets, counted as the length of each `cases` array: brand-diagnosis 7 · filter-test 12 · engagement-setup 6 · harvest 2 · proposal 7 · journey-design 3 · journey-map 3 · training-programme 6 · ads-audit 7 · consistency-qa 12 · monthly-report 4. A run log or commit that states a total states it this way.

## When

Before every `release.py package` of the plugin that holds the skill, and after any edit to the skill or to the guardrails it quotes. `release.py check` verifies the structure (frontmatter, reference paths, eval files present and parseable); it cannot run the skill. The run itself is done by a session.

## How to run

1. Start a fresh session in this repo (no client context beyond what the case carries).
2. Ask it: "Run the evals in `plugin/<plugin>/skills/<skill>/evals/cases.json`: load the skill, apply it to each case exactly as `how` says, and return a table case id · expected · got · pass/fail. Do not edit the skill."
3. Paste the table into `evals/runs.md` under a heading `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`; the session id shows the run was not the session that edited the skill.
4. A failed case is either a skill regression (fix the skill) or a wrong expectation (fix the case, with the reason in the run log). Never both in silence.

## Pass bar

All cases pass before a package. A case that fails twice in a row on an unchanged skill is a flaky expectation: rewrite the case.

## Adding cases

One case per rule the skill owns. A case names the rule it tests. Client-specific fixtures are placeholders, never a real client's data.
