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

Lines added at Stage 3 (design pages M07, M15, M22, M23; new floor-register copy, for Menelaos to read as new lines):

| # | Line | Hurry | Sell | Talk past | Verdict |
| --- | --- | --- | --- | --- | --- |
| 13 | "Then let's just choose something good." (M07, after "nothing") | no | no | no | pass |
| 14 | "Pistachio it is." (M07, irritated guest) | no | no | no | pass |
| 15 | "I'm sorry. Let's choose something good for today." (M07, painful answer) | no | no | no | pass |
| 16 | "The note's inside, for whoever opens it." (M15, box to give away) | no | no | no | pass |
| 17 | "A note for today. It goes with every order." (M15, first-timer) | no | no | no | pass |
| 18 | "They're drawn by chance. This one's yours." (M15, asks to pick) | no | no | no | pass |
| 19 | "Thanks for waiting." (M05, wait past five minutes; a fact, not an apology) | no | no | no | pass |
| 20 | "Taste the new one?" (M11, regular wavering) | no | no | no | pass |
| 21 | "If you're not sure, the [flavour]. It's the one for a day like that." (M11, anchor after a shared moment) | no | no: one named flavour, once | no | pass |
| 22 | "If you're not sure, the [flavour]. Made this morning." (M11, anchor, no moment shared; only when true) | no | no | no | pass |
| 23 | "No hurry." (M11, anchor declined) | no | no | no | pass |
| 24 | "The gelato and the tiramisu are gluten-free; the Lab checks cross-contact." (M11, allergen fact from the fact sheet) | no | no | no | pass |
| 25 | "No added sugar in the Mindful line." (M11, fact only) | no | no | no | pass |
| 26 | "Then let's just choose something good." / „Тогава просто да изберем нещо хубаво." (M09, BG form) | no | no | no | pass |
| 27 | "I'm sorry. Let's choose something good for today." / „Съжалявам. Да изберем нещо хубаво за днес." (M09, BG form) | no | no | no | pass |
| 28 | "Good to see your note made it home, [name]." (M25, reply) | no | no | no | pass |
| 29 | "May we share your photo on our page, in your words? A yes here is enough; we keep it on file." (M25, permission ask; one ask, no reward) | no | no | no | pass |
| 30 | "We only supply venues that serve the story with it. If that changes, write to us." (M29, declining a venue) | no | no | no: a fact to the owner | pass |
| 31 | "Fresh this morning. The cards are on top." (M30, at the door; only when true) | no | no | no | pass |
| 32 | "The tiramisu collection is here too: L'Originale, pistachio, hazelnut, blueberry, mango." (M12, one offer as a fact) | no | no: what is there, not a question | no | pass |
| 33 | "That one has limoncello in it." / „В този има лимончело." (M13) | no | no | no | pass |
| 34 | "That line is 18 and over." (M13, if asked) | no | no | no | pass |
| 35 | "If you'd like to tell others about today, our Google page is here." (M26, review ask, no reward) | no | no | no | pass |
| 36 | "That's not yours. One moment." / „Това не е твоето. Един момент." (R-WRONG-ORDER) | no | no | no | pass |
| 37 | "That's the price on the list." / „Това е цената от листата." (R-BILL) | no | no | no | pass |
| 38 | "The till was wrong. It's [price]." (R-BILL) | no | no | no | pass |
| 39 | "The cards are part of the delivery; that's what we agreed. Can they be on the tables by [date]?" (R-PARTNER, to the owner, Вие) | no | no | no | pass |

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

- "Happiness is an attitude." — the lock-up tagline. Not a line to a guest; judged by the brand book, not the test. If it ever appears as a reply to a person, it would fail "talk past".
- "Italian joy crafted daily." — the editorial, story-facing tagline (owner decision 2026-11-01, recorded in `brand-book.md`). Same status: outside the test, judged by the brand book. Two things the brand book will judge it on: v3 §2.2 says "joy every day" is Doppio's and joy alone is not ownable; and "crafted daily" is a claim, true per the fact sheet (made fresh daily in the Lab) and to be kept true. As a reply to a person it would fail "talk past", like the other.
- "Small wins count." — passes as a farewell (said to her, after her answer); would fail if used to push a guest who said "nothing" into finding something.

## Revision log

| Date | Change | Why |
| --- | --- | --- |
| 2026-11-01 | Derived; markers set to hurry · sell · talk past | First derivation, blind test of `vios-filter-test` |
