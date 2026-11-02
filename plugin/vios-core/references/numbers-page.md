# The numbers page

House reference (2026-11-02, quality plan WS4). Every Vios engagement reads the venue's money before it reads its meaning: the brand diagnosis opens with this page, the journey design prices each HIGH moment against it, the monthly report reads marketing and sales on the same lines. It is one page, filled from exports, never estimated; a row that cannot be filled reads "to confirm" with a row in `open-facts.md`.

## Contents

1. [Definitions](#definitions)
2. [Where each number comes from](#where-each-number-comes-from)
3. [Menu engineering quadrant](#menu-engineering-quadrant)
4. [Cost of a moment](#cost-of-a-moment)
5. [Reading rules](#reading-rules)

## Definitions

| Row | Definition | Period |
| --- | --- | --- |
| Revenue | Net sales excluding VAT, all tenders, after discounts and voids; say once if the export is gross (Barsy `net_sales` is VAT-gross) | 12 months by month; trailing 3 months for the baseline |
| Covers | Guests served (bills × guests per bill when the POS counts guests; bills when it does not, labelled "bills") | same |
| Average check | Revenue ÷ covers | same |
| Items per cover | Sold lines ÷ covers | same |
| Revenue mix | Share of revenue by category: food · drinks (alcohol / non-alcohol split when the POS has it) · other (retail, events, delivery) | 12 months |
| Covers by daypart | Share of covers lunch · afternoon · dinner · late, cut at the venue's own hours (`fact-sheet.md`), fiscal day as the POS defines it | 12 months and by weekday |
| Labour % | Labour cost (wages, employer contributions, agency, per-shift pay) ÷ revenue | 12 months by month |
| COGS % | Cost of goods sold ÷ revenue, from recipes when costed, from purchases when not (say which) | same |
| Prime cost % | Labour % + COGS % | same |
| Top 10 by volume | Items by units sold | 12 months |
| Top 10 by margin | Items by contribution (sell price − recipe cost) × units | 12 months; only when recipes are costed |
| Bottom 10 | Lowest contribution × units among items sold at least once a week | same |

Pre-2026 Bulgarian figures in BGN convert at 1.95583 and are labelled "converted".

## Where each number comes from

A client on Memento: the account manager reads these pages with the venue selected in the header; exports go to `[client]/data/YYYY-MM/` with source and pulled-at in the filename.

| Row | Memento page | Not on Memento |
| --- | --- | --- |
| Revenue, covers, average check, mix, daypart | `/admin/reports/sales` (sales report by category and hour), `/admin/weekly-flash` for the trend | POS sales export by category and by hour |
| Top 10 by volume, bottom 10 | `/admin/sales-items-analysis` | POS item sales export |
| Top 10 by margin, quadrant | `/admin/menu-engineering` (needs costed recipes; `/admin/menu-cost-comparison` for price vs cost) | item sales export + the chef's recipe costs, or "to confirm" |
| Labour % | `/admin/labor-costs` (payroll + labour bills, the P&L's labour line) | payroll total from the accountant |
| COGS % | `/admin/reports/cogs-analysis` (actual from inventory when counts exist; theoretical from recipes) | purchases ÷ revenue from the accountant, labelled "purchase-based" |
| P&L lines together | `/admin/profit-loss` (one location at a time; never the all-locations total) | the accountant's monthly P&L |
| Bookings, sources, party size, no-shows | `/admin/guests` and the reservations book (`/dashboard/host`) | the booking platform's export, or the paper book counted |

## Menu engineering quadrant

Classic Kasavana–Smith, on the twelve-month item list, items sold at least once a week:

| | High margin | Low margin |
| --- | --- | --- |
| **High volume** | Stars: protect, feature, never discount | Plough-horses: re-cost or re-price, keep on the menu |
| **Low volume** | Puzzles: move on the menu, give a story (the micro-message block) | Dogs: remove or rebuild |

Margin threshold: the menu's average contribution per item; volume threshold: 70 % of the average units per item (the Kasavana–Smith 0.7 rule). The quadrant feeds the diagnosis (what the business actually sells against what the owner says it is), the messages (a Star is a candidate core message, a Puzzle a candidate story block) and the journey (ordering-moment anchors: S3-04 defends a Star, never a Dog).

## Cost of a moment

Every HIGH design page carries one line: **Cost of the moment** = staff minutes × loaded minute rate + item cost, per guest or per table, with the assumption named. Loaded minute rate = (monthly labour cost ÷ paid hours) ÷ 60 from the labour page; item cost from the recipe (a welcome pour, a note, a card). The line is there so the owner sees the price of the signature and the peak next to their value, and so a HIGH moment is never cut for a cost nobody has stated. A moment with no marginal cost says "no marginal cost" (a greeting, a silence).

## Reading rules

- A number has a source, a date and a period, or it is "to confirm". Nothing from memory.
- One location at a time; a group's total hides the venue the engagement is about.
- Under twelve months of trading: the page says "n months" on every row and the quadrant is "early read".
- The page is the owner's numbers read back; it is never a recommendation. What to do with a Dog or a 38 % labour line belongs to the stages that follow, named with the number beside it.
- Reporting n and the small-sample threshold: `vios-core:vios-guardrails` › Shared numbers.
