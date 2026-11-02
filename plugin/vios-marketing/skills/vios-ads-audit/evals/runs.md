# Eval runs

One block per run, headed `## <date> · <plugin> <version> · session: <id or 'subagent, parent <id>'>`: the table (case id · expected · got · pass/fail) and what was changed as a result.

## 2026-11-02 · vios-marketing 0.4.2 · session: eval run after benchmark fixes 11ec378

Skill from the repo (`SKILL.md`), guardrails from `plugin/vios-core/skills/vios-guardrails/SKILL.md`; each fixture read as this week's Meta export with the case's `ads_plan` (budget 600, target €8 per booking, Autumn A/B ends 2026-11-20). 7 of 7 pass.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| ads-01-too-thin | too thin to judge; Watch list | too thin to judge; Watch list, no verdict | pass | 620 imp < 1,000 and 9 clicks < 30 → minimum-sample rule; result 1 not read. |
| ads-02-winner-not-yet | inconclusive, keep running | inconclusive, keep running | pass | Both cells meet minimum sample but 22 and 35 results < 50 per cell; raw numbers only, headed "early read, too small to call" (A side n < 30). The 59 % raw gap is not a winner. |
| ads-03-fatigue | fatigue (2 of 3) | fatigue (2 of 3) | pass | freq 3.4 > 3 ✓; CTR 0.026 vs 0.035 = −26 % ✓; CPR 6.6 vs 6.1 = +8 % ✗. Action: refresh with new concepts via ad-factory, for approval. |
| ads-04-learning-phase | in learning, not judged | in learning, not judged | pass | 4 days old, status learning → no edit, no pause; revisit after day 7. |
| ads-05-planned-test-protected | planned test, protected until 2026-11-20 | planned test, protected until 2026-11-20 | pass | Not paused; noted in Watch list. CPR €14.0 vs €8 shown as n 12, "too small to call" per the < 30 results line; only disapproval or overspend ends it early. |
| ads-06-retargeting-frequency-and-exclusions | freq > 3; 3 exclusions missing | freq 3.6 > 3; missing 14-day visitors, converters, messaged-no | pass | Audience 1,800 ≥ 1,000 OK; age 21 d, past learning. Propose lower budget or wider audience to bring 7-day freq ≤ 3 plus the three exclusions, for approval; results n 14 too small to call. |
| ads-07-spend-concentration | concentration: Cold A 68 % without best CPR | concentration: Cold A 68 % without best CPR | pass | Cold A €9.5 (n 41, off target) vs Cold B €6.2 (n 33, on track); Warm €7.1 (n 12) too small to call, excluded. Propose rebalance toward Cold B, for approval. |

Changed as a result: nothing (no skill or case edited this run).

## 2026-11-02 · vios-marketing 0.5.1 · session: subagent, parent 3ab1bdf5, after e2ff43f (guardrails re-check)

Re-run because `vios-core/skills/vios-guardrails/SKILL.md` changed in 8f14f68; the "Shared numbers" lines this skill leans on (Reporting n, Early reads) are unchanged. `SKILL.md` unchanged since the last run. Each fixture read as this week's Meta export with the case's `ads_plan` (budget 600, target €8 per booking, Autumn A/B ends 2026-11-20). 7 of 7 pass.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| ads-01-too-thin | too thin to judge; Watch list, no verdict | too thin to judge; Watch list, no verdict on any metric | pass | 620 imp < 1,000 and 9 clicks < 30 → minimum sample |
| ads-02-winner-not-yet | inconclusive, keep running | inconclusive, keep running | pass | both cells meet minimum sample; 22 and 35 results < 50 per cell; raw numbers headed "early read, too small to call" (A n 22 < 30); the 59 % raw gap is not a winner |
| ads-03-fatigue | fatigue (2 of 3) | fatigue (2 of 3) | pass | freq 3.4 > 3 ✓; CTR 0.026 vs 0.035 = −26 % ✓; CPR 6.6 vs 6.1 = +8 % ✗ (both windows ≥ 30 results, so the signal counts, it just did not turn); refresh with new concepts via ad-factory, for approval |
| ads-04-learning-phase | in learning, not judged | in learning, not judged | pass | 4 d old, status learning → no edit, no pause; revisit after day 7 |
| ads-05-planned-test-protected | protected until 2026-11-20 | planned test, protected until 2026-11-20 | pass | not paused; CPR €14.0 vs €8 shown as n 12 "too small to call"; noted on the Watch list; only disapproval or overspend ends it early |
| ads-06-retargeting-frequency-and-exclusions | freq > 3; 3 exclusions missing | freq 3.6 > 3 (not > 4); missing 14-day visitors, converters, messaged-no | pass | audience 1,800 ≥ 1,000; age 21 d, past learning; propose lower budget or wider audience to bring 7-day freq ≤ 3 plus the three exclusions, for approval; results n 14 too small to call |
| ads-07-spend-concentration | concentration: Cold A 68 % without best CPR | concentration: Cold A 68 % without best CPR | pass | Cold A €9.5 (n 41, off vs €8) vs Cold B €6.2 (n 33, on track); Warm €7.1 (n 12) too small to call, out of the comparison; propose rebalance toward Cold B, for approval |

Changed as a result: nothing (skill and cases untouched).
