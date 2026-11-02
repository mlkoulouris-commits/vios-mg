---
name: "vios-ad-factory"
description: "Produce paid ad concepts and variants for a Vios Marketing F&B client — Meta (Facebook/Instagram) and Google Ads — with a two-round test design sized to a venue budget (concepts first, then the Vios tone ladder on the winner), local targeting, offline booking attribution agreed up front, and upload-ready copy sheets. Use whenever a client needs ads, an ad campaign, ad copy, creative variants, responsive search ads, or \"let's promote this on Facebook\"."
---

# Vios Ad Factory

Creative is the targeting now. Meta's and Google's systems find the audience; what we control is a varied, on-brand creative library and a clean test a venue budget can afford. Hard lines: `vios-guardrails` 1–12, apply all. Minimum-sample and refresh rules: `vios-ads-audit`.

**Work in five steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Each step writes its file and `status.json` as it goes; the ClickUp task only at step 5. Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Brief recap** (Output format 1): goal, offer, one CTA, radius, budget and cells, structure, dates, languages, attribution method or proxy, alcohol yes/no, tracking check. Ask: *"Budget, dates, radius and attribution right?"*
2. **Concept board** (Output format 2): 3–5 concepts, one line each. Ask: *"Which 2–3 go to round 1?"*
3. **Variant sheet** (Output format 3): the round-1 ads, one per concept, passed through `vios-persona-voice` rules. Ask: *"Change a line?"*
4. **Test plan and checks** (Output format 5–6): cells, budget per cell, duration, delivery event, decision metric, winner rule; test or bet, said plainly. Ask: *"Anything to fix before the files are written?"*
5. **The files** (Output format 4): now write `clients/<slug>/ads-plan.md` (test plan, attribution, Ad Strength note), the upload sheets to `clients/<slug>/data/YYYY-MM/`, and the ClickUp task. Ask: *"Read it. Change anything before it goes to Review?"*

**Ask only when necessary; never invent.** Prices, dish names, hours, claims and the neighbourhood come only from `fact-sheet.md` or the user; budget, target cost per booking, attribution method and test dates only from `ads-plan.md` or the user; holiday and event dates only from `calendar-sources.md`; never from memory. A budget or offer date the test cannot be sized without, that the user can give now, is one question; otherwise "to confirm", a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and, when it blocks the next action or the stage from closing, a blocker in `status.json`, and the plan goes on with the cells the known budget supports.

No attribution method: the stated proxy, every result "unjudged on bookings" (the method's rule), plus the row. No approver on file: a blocker, never a placeholder name. Hard-line 11 topics (allergy, illness, injury, legal, press, named staff, discrimination) are never put in an ad: the facts go to the approver.

**After every step:** write the file → update `clients/<slug>/status.json` (`updated`, blockers added or removed) → at step 5 the ClickUp task in the client's Ads list (id in `accounts.md`), status **review**, named `<dates> ads: <concept(s)> — round 1`, the variant sheet and test plan in the description (budget changes and anything live flagged "needs client owner"), Stage = Marketing, Approver = the approver in `status.json` matched to `setup/clickup.json` ("To confirm" when unmatched), one `create_many` call per list (the pattern in `setup/scheduled-tasks.md` › ClickUp Review).

A blocked client (no accounts, no ad account, empty persona) gets the blocker in `status.json` and no task. The QA gate stays: nothing moves past Review without `vios-consistency-qa` and a `qa-log.csv` row with `signed_off_at`; nothing is uploaded or spent by this skill.

## Load first (`vios-guardrails` › client file)

- `persona-bible.md` (voice, never-list, register, approver, alcohol yes/no), `diagnosis.md` (positioning, audience)
- `fact-sheet.md` (prices, dish names, hours, claims we may make)
- `accounts.md`, `ads-plan.md` (budget by cold/warm/guest, target cost per booking, **offline attribution method**, test dates). No attribution method: run with link clicks or directions as the stated proxy and label every result "unjudged on bookings".
- The brief: goal, offer, dates, radius, platforms, landing, languages
- Past ad results (`vios-ads-audit` / `vios-monthly-report`); competitor ads from Meta Ad Library (what's saturated, what nobody says)

## Ads-specific principles

- **One CTA per ad.** Proper choices, not more choices.
- **Plain over flattering.** A real date once, as fact; never pressure. We accept lower CTR from not using pressure; the metric is bookings and return visits.
- **Local first.** Name the neighbourhood; give a reason to come this week.
- **Peak-end.** Video ads end warm, not on a hard sell.
- **Respect the no.** Retargeting frequency and exclusion rules are owned by `vios-ads-audit` (Rules block, areas 2 and 5); apply them when building.
- **Pre-launch**: run `vios-ads-audit` area 1 (pixel/CAPI, Consent Mode v2) before any budget is live; otherwise results can't be read.

## Test design: two rounds

- **Round 1, concepts.** 2–3 concepts (daily budget ÷ ~€8 = number of cells), each a different *angle* (the moment, the craft, the neighbourhood, the proof, the offer). Pitch 3–5 on the concept board; test what the budget covers. One ad per concept, default tone neutral, each concept its own ad set with an equal, fixed ad-set budget (no campaign budget optimisation in a test, or Meta starves one cell and the test is void). ≥ 7 days.
- **Round 2, tone.** The winning concept as three ads on the Vios tone ladder (A neutral: asks or states · B suggestive: proposes · C directive: recommends), separate ad sets. Round 2 needs 3 cells (≈ €24/day); under that, test only neutral vs suggestive, or run the same two cells for 14 days. Never split a cell below ~€8/day.
- **Delivery event**: the highest-volume event the budget can feed (landing-page view or link click; a booking event on €8/day never leaves learning).
- **Decision metric, round 1**: cost per landing-page view / link click, pre-registered in the test plan; bookings by code as a sanity check, not the winner call. Trade-off, stated plainly: a click winner can lose on covers, so a click winner is confirmed against offer-day covers before scaling.
- **Calling a winner**: the `vios-ads-audit` › Rules › Winner rule, as written there (minimum sample, 50 results per cell, gap); otherwise "inconclusive, keep running". Labelled "early read" in any report. Before round 1 starts, the test plan states whether the budget can reach 50 results per cell within 14 days; if it cannot, the plan says so and round 1 is a **bet** (the recap names what would have been needed), not a test.
- **Warm and guest campaigns**: only with the minimum audience in `vios-ads-audit` › Rules and only when ≥ €5/day is left over; otherwise cold only, noted in the recap. Never one budget across cold, warm and guests.

## Meta build

- **Formats**: 9:16 video (Reels), 1:1 or 4:5 static, carousel for menus/events. Test static against video; don't assume either.
- **Copy**: primary text 1–2 lines (offer + reason + place), optional 2nd paragraph; headline ≤ 40 chars; one CTA button matching the landing.
- **Multiple texts per ad**: up to 5 primary texts and 5 headlines so Advantage+ can mix, all the same tone. Never load A/B/C into one ad: tone is the test, Meta will blend it.
- **Targeting**: radius around the venue (3–5 km city, 10–15 km destination), otherwise broad. Customer lists only with a documented GDPR basis. Alcohol venues: age-restricted.
- **Advantage+ creative**: text generation/improvements OFF (tone is the test; it rewrites wording and can reintroduce pressure words); generative visuals OFF (they invent food); music enhancements OFF (rights, guardrails 9). Crop, brightness and placement adaptations may stay on. Design with safe zones.
- **Existing-post ads**: top organic posts (from `vios-content-calendar`) run first; they come with proof.

## Google build

- **Search**: RSAs with 15 headlines ≤ 30 chars and 4 descriptions ≤ 90 chars. Pin headline 1 = venue + neighbourhood; drops Ad Strength to "Average", accepted and noted in `ads-plan.md` so `vios-ads-audit` doesn't re-flag it. Keyword themes: "[dish/category] [neighbourhood/city]", "[category] near me", "[venue name]". Negatives: jobs, recipes, wholesale, franchise.
- **Location**: "presence" only, never "presence or interest".
- **Consent Mode v2** live before any EEA conversion tracking.
- **Performance Max for store goals**: only with a linked Google Business Profile and ≥ ~€15/day; add brand exclusions so it doesn't cannibalise venue-name search. Otherwise Search only.
- **Landing**: GBP, booking page or menu, whichever matches the one CTA.

## Output format

ALWAYS deliver, in this order:

1. **Brief recap** — goal, offer, one CTA, radius, budget and cells, campaign structure (cold only / +warm / +guests), dates, languages, attribution method or proxy, alcohol yes/no, Ad Strength note if pinned, pre-launch tracking check done.
2. **Concept board** — 3–5 concepts: angle, one-line idea, visual, why it fits the persona; which 2–3 go to round 1.
3. **Variant sheet** — concept, round, variant (A/B/C), platform, language, format, primary text, headline, description, CTA, visual brief, persona cue if a face appears, consent status.
4. **Upload sheets** — `meta_ads.csv` and `google_rsa.csv`, matching the current bulk templates (check the export first), or handed to the buyer as a sheet.
5. **Test plan** — cells, daily budget per cell, duration, delivery event, pre-registered decision metric, sanity check, winner rule and refresh triggers quoted from `vios-ads-audit`.
6. **Checks** — one CTA ✓ · locality ✓ · never-list ✓ · guardrails 1–12 ✓ (10 approver named, 11 no escalation topics, 12 audience basis) · landing matches CTA ✓ · attribution set or proxy labelled ✓ · tracking checked ✓ · AI label route confirmed if persona appears ✓.

Pass every variant through `vios-persona-voice` rules. Hand video concepts to `vios-video-script`.

Before upload: `vios-consistency-qa` → named approver. This skill drafts; it never publishes or spends.

End with one line: the test in a sentence (concepts, cells, budget per cell, test or bet), what is "to confirm" and who confirms it, and the next step (`vios-video-script` for video concepts, `vios-consistency-qa` before upload, `vios-ads-audit` once live). Then stop.

## Example (taverna, goal: Sunday-lunch bookings, €16/day → 2 cells, cold 4 km; placeholders)

- **Concept 1, the moment**: the long table at 13:45, twelve chairs, bread on the table. Round 1 (neutral): "Sunday lunch in [neighbourhood]. The long table seats twelve." CTA: Book now
- **Concept 2, the craft**: the pot on the stove at 11:00. Round 1 (neutral): "Sunday's lamb goes in at eleven. [Neighbourhood]." CTA: Book now
- Round 2 on the winner (needs ≈ €24/day for three cells; at €16/day: neutral vs suggestive only): B "Bring the cousins you only see at weddings." · C "Book the long table for Sunday. Lunch is at two."