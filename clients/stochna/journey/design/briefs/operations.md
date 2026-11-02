# Operations brief — Stochna Kitchen Brewery

Date 2026-11-02 · DRAFT · from `design/` (36 pages, choreography, recovery) · for the owner and the floor manager · operational register.

**Status.** No POS or booking data was pulled (Barsy export, open fact 21), so every number in § 2 and § 4 is an **assumption, to replace with data**. No observation yet (open fact 9). The behaviour is complete; the staffing numbers are not.

## 1. Team structure and the operating principle

**Principle: position assigns the role in the moment.** Whoever is nearest the door when it opens does M07–M08; whoever is nearest a table when it stands does M31. No one stops working to greet (book § 4.2).

| Role | On the floor | Owns |
| --- | --- | --- |
| Floor manager | yes | the room: sound (M26), the door cover, R-UPSET, R-OVER, R-ESC, any compensation decision (afterwards, privately) |
| Server (per station) | yes | M09–M25, M27–M30 for their tables; reading the table (M23) |
| Bar | yes, behind the bar | pours; the "land together" call with the pass (M16–M17); the paired beer for M24 |
| Kitchen lead | at the pass | M17 bread timing, M19 plates, R-ALLERGY answers from the allergen sheet |
| Brewer | when on site | in view (M20); answers M21 if free |
| Not on the floor | — | the AI ambassador (never in the venue); marketing; the approver |

Names per shift: open fact 27. Who covers the door 18:00–24:00: open fact 7.

## 2. Coverage by daypart (minimum on the floor)

| Daypart | Hours and mode | Minimum on floor | Composition |
| --- | --- | --- | --- |
| Weeknight early | 18:00–20:00, filling | 3 | manager · 1 server · bar |
| Weeknight peak | 20:00–22:30, full | 4 | manager · 2 servers · bar |
| Weeknight late | 22:30–24:00, staying | 3 | manager · 1 server · bar |
| Weekend day | from 13:00 (doors CONFIRM, open fact 2) | 3 | manager · 1 server · bar |
| Weekend evening | as weeknight peak | 4–5 | manager · 2–3 servers · bar |

Kitchen and brewery staffing is outside this table. **To replace with data:** tickets per hour and covers per band from Barsy, bookings per slot from Memento. Rule: a band that can't be staffed is raised with the owner, never silently run short. Short staffing breaks M23 first and M24 second.

## 3. Roles at each HIGH moment

| Moment | Primary actor | Coordination | Backstop | Knowledge needed |
| --- | --- | --- | --- | --- |
| M07 threshold | nearest to the door | manager watches the door | anyone who sees a guest waiting > 15 s (R-M07) | the eyes-first rule |
| M15 order | table server | bar for pours | manager | the menu anchor for this edition; the pour offer; never answers allergens |
| M17 signature ★ | server + runner | bar ↔ pass "land together" call | kitchen lead | the one sentence; the fallback if the bread claim isn't confirmed |
| M24 peak ◉ | table server | kitchen tells the server what's next | manager | the three signals; the paired beer per course |
| M30 bill ⊐ | table server | — | manager (card machine, wrong bill) | payment route (open fact 8); nothing on the tray |
| M31 farewell ⊐ | nearest person at work | — | manager | the line; the bookend posture |

## 4. Service-flow assumptions (each to be checked at observation)

> **A1. Tables per server: about 5 at a 90–120 minute stay.** Protects M23 and M24: a server with more can't read every table from their station.

> **A2. Beer and bread within one minute of each other.** Protects M17. Needs the call between bar and pass and bread kept warm and ready during service.

> **A3. The paired next beer arrives within 4 minutes of a yes.** Protects M24.

> **A4. Bill brought within 3 minutes of being asked; paid within 8.** Protects M30.

> **A5. One unprompted approach per table between M19 and M30 (the M24 offer).** Protects the peak cluster; needs the M23 station view.

## 5. Equipment and layout dependencies

| Item | Moments | Source |
| --- | --- | --- |
| Clear sightline from the door into the room and to the making; no host stand blocking it | M06, M07, M20 | book § 6.1; floor plan CONFIRM |
| Server stations with a view of their tables | M23, M24 | design |
| Bar ↔ pass signal (a word, a light or a ticket flag) for "land together" | M16, M17 | design |
| Bread warmer or oven timing that holds bread for service | M17 | open fact 6 |
| Sound level meter (a phone app is enough) and one owner per shift | M26 | open fact 11 |
| Two card machines | M30 | R-M30 |
| Spare chairs reachable without crossing the room | M27 | design |
| One-page menu, readable in dim light, BG/EN, pairings marked | M12, M15 | book § 6.3 |
| Allergen sheet at the pass | M15, R-ALLERGY | open fact 26 |
| No review or QR cards at the bill or the door | M30, M32 | open fact 23 |

No separate equipment and layout brief: the build is small enough to sit here.

## 6. Training assumptions

- **Locked lines everyone learns** (once locked): M08 greeting · M15 anchor and the pour offer · M17 sentence (or the fallback) · M24 offer and "Sure." · M25 "Stay as long as you like" · M31 "See you next time" · R-WRONG · R-FULL · R-ALLERGY handover. Batches 3–4 in `archive/filter-test-batches.md`.
- **Knowledge:** the menu edition's pairings; what is brewed and baked on site and how (only confirmed facts); the escalation topics.
- **Drills:** the threshold (eyes in 10 s); reading the table (three signals); the offer once and accepting a no; a wrong order fixed in one line.
- **Pre-shift (10 min):** tonight's anchor and paired beers; bookings and big tables; who covers the door; one moment to watch.
- Detail and materials: `vios-journey:vios-training-programme` (Stage 4).

## 7. Standards and observable metrics (sampled, diagnostic, not punitive)

| Standard | Observable behaviour | Target |
| --- | --- | --- |
| Eyes before words | eye contact within 10 s of the door opening | 9 in 10 arrivals |
| Land together | beer and bread within 1 min | 9 in 10 first rounds |
| Offer once | at most one unprompted offer per table after M19 | every table |
| Nothing asked | no review, card or survey at the bill or door | every table |
| Bill on request | bill only when asked; paid within 8 min | 9 in 10 |
| One farewell | one line per table, by someone at work | 8 in 10 |
| Escalation | allergen questions answered only by the kitchen lead or manager | every time |

Show n with any share; under 30 observations, raw numbers only.

## 8. Management review cadence

- **Daily:** the 10-minute pre-shift (§ 6).
- **Weekly:** team review, 30 minutes: one standard from § 7, what slipped, one fix.
- **Monthly:** design review with the founder, off the floor: the standards sample, reviews tagged to moment codes, open facts closed.
- **Re-weighting:** observation + 14 days for the map (open fact 10).

Small revisions over the first 6–12 months are expected; each changed page gets a date and a line in the schedule.
