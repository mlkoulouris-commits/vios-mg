# Baseline — <Client> — measured <YYYY-MM-DD>

One page, measured before any deliverable is made, so every later report shows change against it. Written by `vios-engage:vios-engagement-setup` step 7; read by `vios-marketing:vios-monthly-report` (column "Baseline") and by the KPI table of the proposal. Period: the trailing 3 full months before the measurement date, plus the same 3 months a year earlier when they exist. Every row names its source and its n; a row that cannot be filled reads "to confirm" and has a row in `open-facts.md`. Nothing is estimated.

Period measured: <YYYY-MM-DD> to <YYYY-MM-DD> (3 months) · same period last year: <yes / no history>
Revenue basis: <net / gross> of VAT · currency EUR (pre-2026 BGN converted at 1.95583, labelled)

## 1. Venue (POS)

Source: <Memento P&L / POS export>, pulled <date>, file `data/<YYYY-MM>/<file>`. When `data/numbers-page.md` exists, these rows are its trailing 3 months and the numbers page wins on a disagreement.

| Measure | 3-mo total or avg | Same period last year | n | Note |
| --- | --- | --- | --- | --- |
| Covers per month | | | | |
| Revenue per month | | | | |
| Average check | | | | |
| Items per cover | | | | |
| Covers by daypart (lunch / dinner / late) | | | | |
| Revenue mix by category (food / drinks / other) | | | | |
| Labour cost % of revenue | | | | Memento labor module; "to confirm" when the client is not on Memento |
| COGS % of revenue | | | | |

## 2. Bookings

Source: <Memento reservations / client's book / none>, pulled <date>.

| Measure | 3-mo avg per month | n | Note |
| --- | --- | --- | --- |
| Bookings per month | | | |
| Bookings by source (own site / Google / phone / walk-in / partners) | | | |
| No-show rate | | | |
| Average party size | | | |

## 3. Reviews

Source: Google Business Profile, TripAdvisor, Facebook; pulled <date>.

| Measure | Value | n | Note |
| --- | --- | --- | --- |
| Google rating · review count | | | |
| TripAdvisor rating · review count | | | |
| Reviews in the last 90 days (velocity) | | | |
| Share answered · median response time | | | |
| Top 5 praise themes (count each) | | | from review mining when on file; otherwise count and rating only (filled at diagnosis step 4; does not make the baseline partial) |
| Top 5 complaint themes (count each) | | | same |

## 4. Social and local

Source: Metricool / Windsor / GBP exports, pulled <date>.

| Channel | Followers | Reach per month | Engagement rate | Posts per month | n | Note |
| --- | --- | --- | --- | --- | --- | --- |
| Instagram | | | | | | |
| Facebook | | | | | | |
| TikTok | | | | | | |
| Google Business (views · directions · calls) | | | | | | |

## 5. Paid

Source: Meta Ads / Google Ads, pulled <date>. "none" when the client has never run ads.

| Measure | 3-mo total | n | Note |
| --- | --- | --- | --- |
| Spend per month | | | |
| Cost per result · result type | | | |

## 6. Not measured and why

One line per row above that reads "to confirm": what is missing, who holds it, open-facts row.

## 7. Reading (five lines at most)

What the numbers say before any work starts, in plain words. No targets here; targets live in the proposal's KPI table and `status.json` › `kpis`.

Measured by: <name> · reviewed by: <name> · date: <YYYY-MM-DD>
