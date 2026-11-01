---
name: "vios-monthly-report"
description: "Build the monthly (or quarterly) client report for a Vios Marketing F&B client — social, ads, Google Business and POS/booking data joined into one insight memo and a private dashboard — with n beside every percentage, seasonal comparison, blended cost per cover, honest attribution language, and next month's three priorities routed to the skill that owns each. Use at month end, for \"how did we do this month\", quarterly reviews, or when a client asks what the marketing is actually bringing in."
---

# Vios Monthly Report

Clients don't pay for reach. They pay for covers, bookings and guests who come back. This report puts the venue's own numbers next to the marketing numbers so the connection is visible, and it ends with decisions, not charts. Measurement rules: guardrails › Shared numbers.

## When

Working day 3–5 (attribution windows are still filling on day 1). Quarterly: same structure, three monthly columns; Structure section 7 becomes 90-day priorities.

## Data (`vios-guardrails` › client file)

Save raw pulls to `[client]/data/YYYY-MM/` with source and pulled-at in the filename; compute in code; note what's missing rather than estimating. Use the metric names the current exports show (GBP renames them).

D1. **Venue truth** — Barsy POS export: covers, revenue, average spend, by day; bookings; offer-day covers vs same-weekday baseline; same month last year. Bulgarian clients: convert pre-2026 BGN figures at the fixed 1.95583 and label "converted" (the euro replaced the lev on 1 Jan 2026). State revenue and spend once as net or gross of VAT in the appendix, same basis both sides. No POS data: guardrails stand-in (marketing-only report, priority #1 = get access).
D2. **Paid** — Meta Ads connector, Google Ads MCP (or Windsor.ai): spend, results, cost per result, frequency, top ads; the reconciliation ratio from `vios-ads-audit`.
D3. **Organic** — Metricool: reach, saves, sends/DM shares, tags, profile visits, link clicks, follower change, best posts, best times, competitor benchmarks.
D4. **Local** — Google Business Profile: views, direction requests, calls, menu clicks, new reviews, rating.
D5. **Community** — reviews answered and response time (Metricool inbox or GBP export), UGC reposted, DMs handled.
D6. **QA log** — first-attempt pass rate, drift caught.
D7. Last month's three priorities and what happened.

## Benchmarks

The client's own history: trailing 3-month median, and same month last year when it exists. Seasonal venues: weight same-month-last-year over the median (three quiet months make a normal peak look like a win). Under 3 months: no benchmark, column "building baseline". Industry numbers only when sourced and dated.

## Numbers and attribution language

- *n* beside every percentage; under 30 per side → raw numbers and "too small to call" (guardrails › Shared numbers). An owner will act on "doubled" when it's 3 vs 6.
- Ad results are "bookings that used the code", not "bookings the ads brought", unless an offer-day lift against baseline supports causation. Early reads are labelled.
- Cost per cover is **blended** (marketing spend ÷ all covers, not incremental). Spend = ad spend + paid tools + production; agency fee excluded and stated.

## Structure

ALWAYS use this exact structure. Numbers first, interpretation second, decisions last.

### 1. The one sentence
"Covers 2,910 (+9 % vs Sep, n 2,670; +4 % vs Oct last year, n 2,800); Tuesday bookings 11 vs 6 (too small to call); organic sends at a 6-month high."

### 2. Venue scoreboard
| Metric | This month | Last month | Same month last year | 3-mo median | Note |
Covers · revenue · avg spend · bookings · repeat-guest share (if trackable) · offer-day covers vs baseline · blended cost per cover · marketing spend as % of revenue

### 3. Marketing scoreboard
| Channel | Key metric | This month | Last month | 3-mo median | Cost |
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
Full tables, post list, ad list, sources, as-of date. Followers live here.

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