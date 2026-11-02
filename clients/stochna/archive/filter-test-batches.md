# Filter-test batches — Stochna Kitchen Brewery

Test (derived at Stage 3, 2026-11-01; `vios-core:vios-filter-test` to sharpen): **"Would someone who never explains themselves say or do this at their own table?"**

## Batch 3 — Stage 3 NEW lines (draft pages, 2026-11-01)

| Line | Page | Verdict | Note |
| --- | --- | --- | --- |
| "There's a darker one that goes with what's coming next. Want to try it?" | M24 | pass | book § 5.5 block 4 |
| "Sure." / „Разбира се.“ after a no | M24 | pass | |
| "Of course." / "No rush." at the bill | M30 | pass | |
| "See you next time." / „До следващия път.“ | M31 | pass | book § 4.6 |
| "Bring them. There's room." | M31 | pass | book § 4.6 |
| "The [beer] goes well with the [plate]." | M15 | pass | names pending |
| "If you're not sure, I'll pour you something." | M15 | pass | book § 4.5 |
| "The beer's brewed here. The bread's baked here, with the grain from the brew." | M17 | pass, **claim blocked** (open fact 6) | |
| "Brewed here. Baked here. They go together." | M17 fallback | pass | |
| "We got that wrong. Here's the right one." | R-WRONG | pass | book § 4.7 |
| "We're full tonight. Thursday has room." | R-FULL | pass | weekday named must be true |
| "Let me get the kitchen to answer that." | R-ALLERGY | pass | escalation |
| "Thank you for choosing us." | rejected | **fail** | performs gratitude |
| "Same again?" | rejected | **fail** | sells volume, not the pairing |

## Batch 4 — Stage 3 MEDIUM pages (draft, 2026-11-01)

| Line | Page | Verdict | Note |
| --- | --- | --- | --- |
| "Hi. Sit anywhere." / „Здравейте. Седнете където искате.“ | M08 | pass | book § 4.5 |
| "Hi. Under what name?" | M08 | pass | after eye contact only |
| "That one's yours." | M09 | pass | |
| "Here you go. Back in a few minutes." | M12 | pass | |
| "We don't do that one. The [item] is close." | M14 | pass | |
| "We'd rather do a few things properly." | M14 | pass | book § 4.6 |
| "No Wi-Fi, honestly. We never set it up." | M14 | pass, **claim blocked** (open fact 29) | |
| "[Plate]. Goes with the [beer]." | M19 | pass | |
| "Want me to ask the brewer?" | M21 | pass | |
| "Stay as long as you like. We're not counting." | M25 | pass | book § 4.6 |
| "There's room." / "Same as them?" | M27 | pass | |
| "2 km from the centre, in Stochna Gara." | M03 | pass | |
| "Lovely photo. Can we share it? We'll credit you." | M33 | pass | |
| "Good to see you. The [beer] is back." | M36 | pass | only if true |
| "Welcome back!" (announced) | rejected | **fail** | performs preference (value 4) |

All BG lines need a native-speaker read before lock.
