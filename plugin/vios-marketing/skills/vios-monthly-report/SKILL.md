---
name: "vios-monthly-report"
description: "Build the monthly (or quarterly) client report for a Vios Marketing F&B client — social, ads, Google Business and POS/booking data joined into one insight memo and a private dashboard — with n beside every percentage, seasonal comparison, blended cost per cover, honest attribution language, and next month's three priorities routed to the skill that owns each. Use at month end, for \"how did we do this month\", quarterly reviews, or when a client asks what the marketing is actually bringing in."
---

# Vios Monthly Report

Clients don't pay for reach. They pay for covers, bookings and guests who come back. This report puts the venue's own numbers next to the marketing numbers so the connection is visible, and it ends with decisions, not charts. Measurement rules: guardrails › Shared numbers.

**Work in five steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a scoreboard counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written to disk before step 5 except the raw pulls, which step 1 saves as the method says (and status.json and open-facts.md bookkeeping). Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Data** (D0–D7): the baseline on file (or not), what was pulled from where, what is missing, the benchmark available. Ask: *"Anything missing you can paste now?"*
2. **The scoreboards** (Structure 1–3): the one sentence, the venue scoreboard, the marketing scoreboard. Ask: *"Numbers right?"*
3. **The reading** (Structure 4–6): what else moved the month, the link, what worked and what didn't, persona and brand health. Ask: *"Agree with the reading?"*
4. **Three priorities** (Structure 7): what, why, owner, how we'll know, owning skill, plus one test. Ask: *"These three?"*
5. **The report** (Deliverables and sign-off): now write the memo, the dashboard, the WhatsApp summary, the file and the PDF, and the ClickUp task. Ask: *"Read it. Change anything before the reviewer re-computes?"*

**Ask only when necessary; never invent.** Every number comes from the saved pulls in `data/YYYY-MM/` or from the user (bookings by source pasted from Memento); covers and revenue from the POS export; holiday and closure dates from `calendar-sources.md` and `fact-sheet.md`; never from memory, never estimated. A missing pull the user can paste now is one question; otherwise the cell reads "to confirm" or "missing" with a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker in `status.json`, and the report goes on with what is on file. No POS data: the guardrails stand-in (marketing-only report, priority #1 = get access). Under 3 months of history: "building baseline", not a benchmark. No approver on file: a blocker, never a placeholder name. Hard-line 11 topics in reviews (allergy, illness, injury, legal, press, named staff, discrimination) are reported as facts to the approver, never quoted or interpreted in the memo.

**After every step:** write the file → update `clients/<slug>/status.json` (`updated`, blockers added or removed, `next_action` = the first priority's skill) → at step 5: the memo copy to `clients/<slug>/data/<YYYY-MM>/report_<date>.md`; the ClickUp task `Report <Client> <Month YYYY> — review before sending` in "Department — Setup & SOP" (id in `setup/clickup.json`), status **review**, the three priorities and the memo link in the description, Stage = Marketing, Approver = the approver in `status.json` matched to `setup/clickup.json` ("To confirm" when unmatched), one `create_many` call per list (the pattern in `setup/scheduled-tasks.md` › ClickUp Review); then `python scripts/clients.py pdf <slug> data/<YYYY-MM>/report_<date>.md "<Client>-Report-<YYYY-MM>"` → `clients/<slug>/deliverables/`, sent to the user. The user forwards it; the practice never emails a client. A blocked client (no accounts, no Metricool brand) gets the blocker in `status.json` and no task. The QA gate stays: nothing moves past Review without the reviewer's re-computation, `vios-consistency-qa` (report mode) and a `qa-log.csv` row with `signed_off_at`.

## When

The scheduled task `vios-monthly-client-report` pulls the data and builds the draft early in the month (the 2nd); the report is finalised and sent on working day 3–5, once attribution windows have filled. A draft sent before then is labelled "draft, attribution still filling". Quarterly: same structure, three monthly columns; Structure section 7 becomes 90-day priorities.

## Data (`vios-guardrails` › client file)

Save raw pulls to `[client]/data/YYYY-MM/` with source and pulled-at in the filename; compute in code; note what's missing rather than estimating. Use the metric names the current exports show (GBP renames them).

D0. **Baseline** — `[client]/data/baseline-YYYY-MM.md` (made by `vios-engage:vios-engagement-setup` step 7; `status.json` › `baseline`). Its rows become the "Baseline" column of both scoreboards. No baseline on file: the column reads "no baseline" and priority #1 of section 7 is to measure one (owning skill `vios-engage:vios-engagement-setup`, step 7); **partial**: the missing rows read "to confirm" and are listed in the appendix with who holds them. The baseline is never recomputed by this skill; a wrong baseline is a row in `open-facts.md` for the account manager.
D1. **Venue truth** — Barsy POS export: covers, revenue, average spend, by day; bookings; offer-day covers vs same-weekday baseline; same month last year. Bulgarian clients: convert pre-2026 BGN figures at the fixed 1.95583 and label "converted" (the euro replaced the lev on 1 Jan 2026). State revenue and spend once as net or gross of VAT in the appendix, same basis both sides. No POS data: guardrails stand-in (marketing-only report, priority #1 = get access).
D2. **Paid** — Meta Ads connector, Google Ads MCP (or Windsor.ai): spend, results, cost per result, frequency, top ads; the reconciliation ratio from `vios-ads-audit`.
D3. **Organic** — Metricool: reach, saves, sends/DM shares, tags, profile visits, link clicks, follower change, best posts, best times, competitor benchmarks.
D4. **Local** — Google Business Profile: views, direction requests, calls, menu clicks, new reviews, rating.
D5. **Community** — reviews answered and response time (Metricool inbox or GBP export), UGC reposted, DMs handled.
D6. **QA log** — first-attempt pass rate, drift caught.
D7. Last month's three priorities and what happened.

## Benchmarks

Two fixed reference points, always both: the **baseline** (D0: the three months before the practice started, the "before") and the client's own history (trailing 3-month median, and same month last year when it exists, the "normal"). Seasonal venues: weight same-month-last-year over the median (three quiet months make a normal peak look like a win); a baseline measured in a quiet season is compared to the same season, never to the peak. Under 3 months of history after the baseline: the median column reads "building history". Industry numbers only when sourced and dated.

## Numbers and attribution language

- Reporting *n*, the small-sample threshold and early-read labelling: guardrails › Shared numbers, applied to every percentage in this report.
- Ad results are "bookings that used the code", not "bookings the ads brought", unless an offer-day lift against baseline supports causation. Early reads are labelled.
- Cost per cover is **blended** (marketing spend ÷ all covers, not incremental). Spend = ad spend + paid tools + production; agency fee excluded and stated.

## Structure

ALWAYS use this exact structure. Numbers first, interpretation second, decisions last.

### 1. The one sentence
"Covers 2,910 (+9 % vs Sep, n 2,670; +4 % vs Oct last year, n 2,800; +12 % vs baseline Jun–Aug avg 2,600); Tuesday bookings 11 vs 6 (too small to call); organic sends at a 6-month high."

### 2. Venue scoreboard
| Metric | Baseline | This month | Last month | Same month last year | 3-mo median | Note |
Covers · revenue · avg spend · bookings · repeat-guest share (if trackable) · offer-day covers vs baseline · blended cost per cover · marketing spend as % of revenue. "Baseline" = the D0 page's 3-month monthly average; "vs baseline" is stated once per row, with the baseline's season named when it differs from this month's.

### 3. Marketing scoreboard
| Channel | Key metric | Baseline | This month | Last month | 3-mo median | Cost |
Paid (cost per code booking, spend) · Organic (reach, saves, sends, tags) · GBP (directions, calls) · Community (reviews answered, response time)

### 4. The link between the two
First name what *else* moved the month: weather, holidays, closures, seasonality. Then where marketing moved the venue numbers and where it didn't: offer days vs baseline; code bookings vs total bookings; reconciliation ratio stability; organic spikes vs footfall. Say plainly when the link isn't provable and how to make it provable next month (booking-source field, "how did you hear about us" at the till).

### 5. What worked (top 3) and what didn't (top 3)
Number + n, the hypothesis, what we do with it. Winners by concept and angle.

### 6. Persona and brand health
Persona video count, best persona clip, QA first-attempt pass rate, drift caught, review sentiment themes (what guests remember: the remembering self speaking).

### 7. Next month: three priorities
Exactly three. What, why (tied to a number above), owner, how we'll know, **owning skill** (content → `vios-content-calendar`, ads → `vios-ad-factory`, tracking → `vios-ads-audit`, voice/replies → `vios-persona-voice`, video → `vios-video-script`, missing client files → `vios-brand-diagnosis` for `diagnosis.md` / `vios-persona-builder` for `persona-bible.md`, gate failures → `vios-consistency-qa`). Plus one test.

### 8. Appendix
Full tables, post list, ad list, sources, as-of date, the baseline's measurement date and period, its rows still "to confirm" and who holds them. Followers live here.

## Vios rules

- Don't dress up a flat month. Say it was flat and why, then what changes.
- Accept the trade-offs the brand chose: lower CTR from plain copy is not a problem to fix.
- Every number has a source and a date. Nothing from memory.

## Deliverables and sign-off

1. **Insight memo** — a Docs artifact in the client's language; EN/BG side by side on request.
2. **Dashboard** — a Dashboard artifact, published **private**, with the two scoreboards and the offer-day chart, updated monthly from the saved files. Pinned for the account manager so it's one click at every client call.
3. **Three-line WhatsApp summary** the owner can forward:
   "October: 2,910 covers (September 2,670; last October 2,800).
   41 bookings used the ad code at about €46 each; we can't yet say how many came only because of the ads.
   November: the Sunday-lunch concept goes to round 2, and we start the booking-source field."

Before anything is shared: a named Vios reviewer re-computes every figure from the saved data files (at least the 5 headline numbers), checks n beside each percentage, and signs (`vios-consistency-qa`, report mode; logged as asset "monthly report"). The account manager decides who gets the dashboard link: this is the client's revenue data.

End with one line: the month in a sentence (the one sentence from the memo), what is "to confirm" and who confirms it, and the next step (the reviewer's sign-off, then the first priority's skill). Then stop.