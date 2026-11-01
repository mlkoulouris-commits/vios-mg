# Filter test — sharpening batches (Atelier del Gelato)

Test (brand-book.md › Filter test, 2026-11-01): **Is this processing the guest?** — does it hurry her, sell to her, or talk past her? Pass = no.

Regression set for the yearly review. Every line in batch A must pass; every line in batch B must fail. A line that moves batches means the test, or the brand, has changed; log it below.

## Batch A — lines the brand would say (all pass)

| # | Line | Hurry | Sell | Talk past | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | "What are we celebrating today?" / „Какво празнуваме днес?" | no | no | no: to her | pass |
| 2 | "Good to see you again." / „Радваме се да те видим пак." | no | no | no | pass |
| 3 | "Pistachio again, or something new today?" | no | no: a memory, not a push | no | pass |
| 4 | "Want to taste two together?" | no | no | no | pass |
| 5 | "Take your time." / „Не бързай." | no | no | no | pass |
| 6 | "Here's a little note for your moment." / „Ето една бележка за твоя момент." | no | no | no | pass |
| 7 | "Until the next celebration." / „До следващото празнуване." | no | no | no | pass |
| 8 | "Made this morning." | no | no | no: a fact to someone choosing | pass |
| 9 | "Today Nikolai celebrated finishing his thesis. What's yours?" (caption) | no | no | no: asks the reader | pass |
| 10 | "It's been a while. We'd love to hear what you're celebrating." (email) | no | no | no | pass |
| 11 | "Every delivery arrives with story cards for your tables." (B2B, Вие) | no | no | no: to the owner | pass |
| 12 | "I'm sorry. Menelaos will write to you today." (complaint) | no | no | no | pass |

Line 8 was the false-negative risk: a product fact says nothing about the person. The "talk past" marker was sharpened to *a line for the crowd rather than this person* so that a plain fact offered to someone choosing passes and hype fails.

## Batch B — lines the brand would not say (all fail)

| # | Line | Hurry | Sell | Talk past | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | "Next!" | yes | | | fail |
| 2 | "Anything else?" | yes | yes | | fail |
| 3 | "That's our bestseller." | | yes | yes | fail |
| 4 | "Last chance for the summer menu!" | yes | yes | | fail |
| 5 | "Treat yourself, you deserve it!" | | yes | yes: a billboard line | fail |
| 6 | "The best gelato in Sofia." | | | yes: self-praise | fail |
| 7 | "Welcome to our establishment, how may I help you today?" | | | yes: for the crowd | fail |
| 8 | "OMG this new flavour is AMAZING!!!" | | | yes: hype | fail |
| 9 | "Watch beauty being made at our marble station." (retired 2025 line) | | | yes: about the show, not her | fail |
| 10 | "Dear valued customer, thank you for your loyalty." | | | yes: form letter | fail |
| 11 | "We're SO excited to celebrate YOU today!!!" | | | yes: performed warmth | fail |
| 12 | "Would you like to add a tiramisu for only 2 leva more?" | | yes | | fail |

Line 11 was the false-positive risk: it says "you" and "celebrate". It fails on exclamation energy and performed warmth, which is the Innocent guardrail ("light, never cute") doing its work inside the test.

## Boundary cases noted

- "Happiness is an attitude." — the tagline. Not a line to a guest; judged by the brand book, not the test. If it ever appears as a reply to a person, it would fail "talk past".
- "Small wins count." — passes as a farewell (said to her, after her answer); would fail if used to push a guest who said "nothing" into finding something.

## Revision log

| Date | Change | Why |
| --- | --- | --- |
| 2026-11-01 | Derived; markers set to hurry · sell · talk past | First derivation, blind test of `vios-filter-test` |
