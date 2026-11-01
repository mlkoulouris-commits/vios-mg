---
name: vios-ads-audit
description: Weekly health check of a Vios Marketing client's Meta Ads and Google Ads accounts — tracking and consent, structure, pacing, creative fatigue, wasted spend, audience overlap, policy and live-copy guardrails — using the connected Meta Ads / Google Ads / Windsor.ai data, ending in a short action list for human approval. Owns the minimum-sample, learning-phase, winner, fatigue and refresh rules every other Vios skill quotes. Use for "how are the ads doing", "audit the account", "what should we pause", or on the weekly schedule.
---

# Vios Ads Audit

Rising costs and fatigued creative don't announce themselves. A weekly 15-minute audit catches them before they cost a month's budget. This skill reads the accounts, applies thresholds, and proposes changes; a named human approves. Google Ads is read-only here; approved Google changes are applied by hand and confirmed. Hard lines: `vios-guardrails`.

## Load first (`vios-guardrails` › client file)

- `persona-bible.md` (the named approver), `accounts.md` (ad account, pixel, Google customer id), `ads-plan.md` (targets, budget plan, attribution method, test end dates, accepted Ad Strength notes). No `ads-plan.md`: report actuals only, Target = "not set", ask the account manager before proposing pauses.
- Data: Meta Ads connector (official MCP), Google Ads MCP (read-only), Windsor.ai or Supermetrics, Metricool ads reporting. Nothing connected: ask for a 14-day export by ad (spend, impressions, reach, frequency, CTR, CPC, CPM, results, cost per result).

Windows: last 7 days vs previous 7; last 28 for fatigue curves. Reach and frequency with the 7-day window as the reporting period, never summed from daily rows. Venue accounts are small, so daily numbers swing; compare 7-day blocks, not days.

## Rules this skill owns (everyone else quotes them)

- **Minimum sample**: don't flag an ad, placement or audience on a metric with < 1,000 impressions or < 30 clicks in either window. Mark "too thin to judge", keep on the Watch list.
- **Learning phase**: don't judge or edit ads < 7 days old or ad sets still in learning. Edits reset learning.
- **Planned tests**: don't pause a running test before its end date unless disapproved or overspending.
- **Winner** (for `vios-ad-factory`): the minimum-sample rule is met in both cells (≥ 1,000 impressions, ≥ 30 clicks) AND ≥ ~15 results of the pre-registered metric per cell AND ≥ 30 % gap; otherwise "inconclusive, keep running". Always an "early read" in reports (guardrails › Shared numbers).
- **Warm / guest campaigns** only with an audience ≥ 1,000. **Retargeting**: 7-day frequency ≤ 3 by audience size vs budget (caps exist only on reach buying); exclude 14-day visitors, converters, staff, and people who messaged a "no".
- Any cost-per-result built on < 30 results shows n and status "too small to call".
- **Fatigue**: flag when **two of three** turn together: 7-day frequency > 3 (> 4 urgent) · 7-day CTR down ≥ 20 % vs previous 7 · cost per result up > 30 % vs first full week (counts only with ≥ 30 results in both windows; otherwise that signal is "too thin" and both remaining signals are required). Also flag ads 3–4 weeks old without refresh, ads with < 5 % of spend, and Meta "Creative Limited / Creative Fatigue" labels.
- **Status key**: on track = within target · at risk = within 15 % of the limit · off = past it · too small to call = n < 30 or below minimum sample.

Why: without these, the audit kills ads that never got a fair test, which is the exact error it exists to prevent.

## The five areas (run all, in order)

### 1. Tracking, consent, policy
- Pixel + Conversions API active, deduplicated, Event Match Quality ≥ 6/10 ("Good" or better in Events Manager)
- Consent banner live and **Google Consent Mode v2** passing (EEA requirement; otherwise conversion data is silently thin)
- Google conversion actions firing; landing pages and booking links live
- Off-site bookings (phone, WhatsApp, TheFork) are invisible to the pixel: mark offline, use the offer-code / booking-source method; don't force a pixel event
- **Reconciliation**: ads-reported : system bookings, weekly. Not expected to be 1:1 either way (attribution windows over-count; phone and walk-in under-count). Stability is what matters; a > 25 % move with no campaign change = fix tracking first.
- **Close the loop with POS**: upload offer-code redemptions or booking lists to Meta as offline events weekly where the system allows; if not, compare offer-day covers with the same-weekday baseline.
- Policy: disapprovals, account-quality alerts, payment failures, alcohol age targeting. **Skim live ad text** for pressure devices, price-anchor claims and missing partnership labels (guardrails 1–3); flag to the approver.

### 2. Account structure
- Cold, warm, guest in separate campaigns; warm/guest only where the audience is ≥ 1,000
- Ad sets with no active ads, campaigns past end date, duplicates
- Radius correct; Google location on "presence", not "presence or interest"
- Exclusions: 14-day visitors, converters, staff, people who messaged a "no"
- Google: search terms reviewed, negatives added; Ad Strength "Good" or better, except "Average" from the venue-name pin (accepted, noted in `ads-plan.md`)

### 3. Pacing and spend
- Spend vs plan for week and month; projected over/underspend
- Cost per result vs target
- Concentration: one ad set over 60 % of spend without the best cost per result (that large, it starves the others of learning)

### 4. Creative fatigue (the main lever)
Apply the fatigue rule to the top 5 ads by spend; list others only if flagged or too thin.

### 5. Audience and placement
- Audience overlap between ad sets
- Placement gaps: a placement at half the CTR of the rest, **only with ≥ 1,000 impressions and ≥ 30 clicks per placement**, and only if bookings by code don't favour it (placement CTR gaps often reflect intent, not waste). Under Advantage+ placements the lever is excluding a placement, not moving budget.
- Retargeting 7-day frequency ≤ 3 via audience size vs budget (caps only exist on reach buying)

## Vios rules inside the audit

- Respect the no: an audit that recommends "increase frequency" is wrong by default.
- Judge on bookings, covers and return visits, not CTR or dashboard ROAS alone.
- Replace fatigued creative with new *concepts* from `vios-ad-factory`, not the same ad in a new colour.

## Output format

ALWAYS this shape, short enough to read on a phone:

```
## Ads audit — [client] — week of [date]

**Headline:** "Spend on plan (€412 of €420); 9 bookings by code vs 7 last week (too small to call); one ad fatigued; Reels placement too thin to judge."

| Metric | This week | Last week | Target | Status |
| --- | --- | --- | --- | --- |
| Spend | €412 | €398 | €420 | on track |
| Cost per booking (code) | €46 (n 9) | €57 (n 7) | ≤ €50 | too small to call |
| Ads : system bookings | 1.4 : 1 | 1.3 : 1 | stable | on track |
| Retargeting freq (7d) | 2.6 | 2.2 | ≤ 3 | at risk |

### Creative (top 5 by spend)
| Ad | Age (d) | Freq 7d | CTR 7d vs prev | CPR vs wk 1 | Flag |
| --- | --- | --- | --- | --- | --- |
| Moment-A | 19 | 3.4 | −24 % | +38 % (n 34) | fatigue (3 of 3) |
| Craft-A | 19 | 2.1 | +3 % | −5 % | — |
| Proof-A | 5 | 1.2 | — | — | learning, < 7 d |
| Offer-A | 19 | 1.8 | (640 imp) | — | too thin to judge |

### Actions (approver [name]: reply with the numbers to approve, e.g. "1, 3")
| # | Action | Why | Expected effect |
| --- | --- | --- | --- |
| 1 | Pause Moment-A | freq 3.4, CTR −24 %, CPR +38 % | stop ~€60/wk waste |
| 2 | Brief 2 new concepts to ad-factory | "moment" angle fatigued | refresh library |
| 3 | Reels placement: keep, re-check next week | 640 impressions, too thin | — |

### Watch list
Ads nearing thresholds; too thin to judge; learning; tests ending this week.

### Tracking notes
Broken, unverified, Consent Mode, live-copy flags.
```

Then stop. Apply only the numbers the named approver replies with (Meta via connector; Google by hand), and confirm each change in one line.

## Schedule

Weekly scheduled task, Tuesday morning (Monday's data is still attributing). Launch week: daily pacing, disapprovals, tracking and billing only; fatigue is read weekly.
