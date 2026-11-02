# Eval runs

One block per run: date · plugin version · session id · table (case id · expected · got · pass/fail) · what was changed as a result.

No run yet.

## 2026-11-02 · vios-core 0.7.1 · session: eval run after benchmark fixes 11ec378

Skill applied from the repo (`SKILL.md` + `references/section-3-4-filter-test.md` + `vios-guardrails`). Test under review: "Is this effusive?" (markers: exclamation marks, self-praise of the venue, performed warmth). 12 of 12 pass.

| id | expected | got | pass/fail | note |
| --- | --- | --- | --- | --- |
| ft-00-derive | trait: refusal of effusion; "Is this effusive?" | trait: refusal of effusion (the category default the character refuses); question "Is this effusive?", negative form, markers: exclamation marks, self-praise of the venue, performed warmth | pass | derived by moves 1–2 from the character given; coincides with the skill's example by design of the case |
| ft-01 | pass | pass: no marker present | pass | |
| ft-02 | fail | fail: "!" ×3, "wonderful restaurant" (self-praise), "so excited" (performed warmth) | pass | |
| ft-03 | pass | pass: three facts, no marker | pass | |
| ft-04 | fail | fail: "master chef's signature" (self-praise), "lovingly" (performed warmth); no exclamation mark needed | pass | shows the test works at trait level, not lexical |
| ft-05 | pass | pass: facts, no apology, no marker | pass | |
| ft-06 | fail | fail: "!!", "sorry to bother you" (performed, apologetic warmth) | pass | the line is mainly anxious; it still fails on the exclamation-mark marker |
| ft-07 | pass | pass: plain, no marker | pass | |
| ft-08 | fail | fail: "Oh my goodness", "SO sorry", "!", "anything you need" (performed warmth) | pass | |
| ft-09-scope | out of scope; the skill says so, does not fail it | not judged: "The name, the tagline and the lockup are judged by the vios-name-and-tagline tests … not by the filter test"; routed to vios-name-and-tagline | pass | the skill's "say so … when a tagline would fail it" is conditional; the scope sentence before it already excludes taglines, and this one would not fail anyway |
| ft-10-too-lenient | rejected, too lenient, failure mode named, back to refusal of effusion | rejected: "friendly" is a trait the whole category shares, so competitor copy (ft-02, ft-04) passes; failure mode "Too lenient (names a trait the category shares)"; fix per 3.4.5 Failure 1: phrase against the trait the brand does not share → "Is this effusive?" | pass | |
| ft-11-too-strict | rejected, too strict, ft-04 would pass under it, exclamation mark kept as a marker | rejected: tests a mark, not the trait; under it ft-04 ("master chef's signature lamb, lovingly hand-prepared") passes with no exclamation mark; failure mode "Too strict (tests a word, not the trait)"; fix per 3.4.5 Failure 2: raise to the character level, keep the exclamation mark as one marker under "Is this effusive?" | pass | |

Changed as a result: nothing (skill and cases untouched).
