# Worked examples

House reference (2026-11-02, quality plan item 5). The general skills describe house forms and show examples that came from real engagements; the client behind each one is named here and nowhere else, so a skill reads as the practice's method, not one client's file. A skill points at an entry as `plugin/vios-core/references/worked-examples.md` › E<n>. Add an entry when a new skill example is taken from a client; never put the name back in the skill.

## Contents

1. [Engagement (intake, status, harvest)](#engagement-intake-status-harvest)
2. [Stage 1 — brand](#stage-1--brand)
3. [Stage 2 — journey map](#stage-2--journey-map)
4. [Stage 3 — journey design](#stage-3--journey-design)
5. [Stage 4 — training](#stage-4--training)

## Engagement (intake, status, harvest)

**E1 — The status card.** The `vios` front-door card example is the Gradina (DEMO) card as `python scripts/clients.py status demo-gradina` printed it on 2026-11-02: intake done, proposal v2 not sent, baseline partial, two KPIs promised, three blockers. The point: at most nine plain lines, no file paths, no fact numbers; a demo client, so nothing in the example is a real venue's number. Source: `clients/demo-gradina/status.json`, `clients/demo-gradina/open-facts.md`.

**E2 — The intake record.** The `vios-intake` example (a second counter-format gelato shop plus a B2B line; Stage 1 revision, Stages 2–3 for the new shop, Stage 4 onboarding; three unanswered rows) is the Atelier del Gelato intake of 2026-11-01. The point: scope against the four stages, pull the starting set from the pattern library, log what the founder could not answer. Source: `clients/atelier/README.md` › Intake record, `clients/atelier/open-facts.md`.

**E3 — The harvest line.** The `vios-harvest` example (first use of the small-format page, counter collision held, "the signature can precede the peak", 1.3 → 1.4 minor) is the Atelier del Gelato blind test of 2026-11-01. The point: one engagement promotes nothing on its own; it holds, and the second engagement decides. Source: `docs/changelog-proposals.md` (1.3 → 1.4), `docs/dry-run-2026-11-01-one-gallery.md` § blind test, `clients/atelier-2026-10/journey/blind-test-notes.md` (archived folder).

## Stage 1 — brand

**E4 — Brand Affinity Audit.** The Reference Tool in `vios-brand-diagnosis` follows ONE Gallery Brand Book v2.2 § 2.4: five or six brands the persona already loves, why they stay beyond features, then the patterns (restraint as a signal, belonging without performing, curated over comprehensive). The point: the audit is speculative until ground-truthed; the book's own diagnosis still carries that gap. Source: Drive `01a_Brand_Book_v2_2_EN.pdf` (22 Oct 2026); lookup `clients/one-gallery/brand-book.md`; gap noted in `clients/one-gallery/diagnosis.md`.

**E5 — One message per value.** The `vios-messages-and-story` rule that each value carries a single line comes from ONE Gallery Brand Book v2.2, whose four values (Welcome, Ritual, Discovery, Quality) each read as one takeaway for the guest. The point: a value message is what the guest should understand here, not a fact about the brand. Source: Drive `01a_Brand_Book_v2_2_EN.pdf`; `clients/one-gallery/brand-book.md`.

**E6 — Place names as keywords.** The `vios-name-and-tagline` keyword rule (a place name attached to the site is a keyword, not a coincidence) comes from Stochna, whose name is a coined form of "Stochna Gara", the old station the venue sits by. The point: the venue's own history belongs in the keyword set before any invented word. Source: `clients/stochna/brand-book.md` (Stochna Brand Book V2, 23 Feb 2026).

**E7 — The two-line tagline system.** The lockup line (three nouns or fewer, categorises in two seconds) and the editorial line (carries the brand belief) are ONE Gallery's: lockup "Art Coffee Aperitivo", editorial "Where the art continues into your glass". The point: each line passes the one-thing test next to the name in its own place; neither replaces the other. Source: `clients/one-gallery/brand-book.md` § 9.3 and the tagline row; Brand Book v2.2.

**E8 — The name run.** The `vios-name-and-tagline` worked example (keyword fragment "together · made here · proper · the table · worth the trip · the old station"; "Table & Tank" failing distinctiveness, "Gara" failing ownership, the BG morphology candidate carrying the strategy; "We cook for beer. We brew for food.") is the Stochna naming, reconstructed from its book. The point: the short-list tests are run per candidate and the losing reasons are written down. Source: `clients/stochna/brand-book.md`; `Stochna_Brand_Book_V2_23_2_2026.docx` (Desktop; Drive link to add).

**E9 — House example books.** The two books `vios-brand-book` may borrow a section shape from are Stochna Brand Book V2 (23 Feb 2026) and Atelier del Gelato Brand Book v3 (7 Oct 2026, the founder's signed prior statement). The point: borrow the shape, keep the wording the client's. Source: `Stochna_Brand_Book_V2_23_2_2026.docx` (Desktop; Drive link to add); Atelier v3 on Drive, link in `clients/atelier/accounts.md`.

## Stage 2 — journey map

**E10 — The house map.** The `vios-journey-map` house form (markers ★ ◉ ⊐ ○ on the cover legend, one table per phase with the bands as columns, two-digit codes, the "what passes to Stage 3" summary) is the ONE Gallery Journey Map v2.2 (Oct 2026): 28 moments in 8 phases, ★ M13, ◉ M18, ⊐ M24+M25, ○ ×6, rendered in four pages. The point: the manuscript's one or two pages is the target, not the rule; the columns are the bands. Source: Drive › one gallery new › 01 Brand, `ONE_Gallery_Journey_Map_v2_2.pdf` / `_BG.pdf`; `clients/one-gallery/README.md` deliverables table.

## Stage 3 — journey design

**E11 — The design pages.** The house layout `vios-journey-design` ships (header with M-code, tier label, descriptor line and markers; the body blocks in order) is the ONE Gallery Journey Design v2, 28 pages, one per moment. The point: a page per moment, the same blocks every time, so the floor playbook can be cut from it. Source: Drive › one gallery new › 02 Operations (Journey Design v2 EN/BG).

**E12 — The peak cluster.** The choreography rule that section 1 names the cluster around the peak comes from ONE Gallery, where M13–M21 are designed as one to protect the peak at M18. The point: the choreography earns its words at the cluster; continuities that only restate the pages are cut. Source: Drive › one gallery new › 02 Operations (Choreography); `clients/one-gallery/README.md`.

**E13 — The operations brief.** The eight-section operations brief (team and operating principle, coverage by daypart, roles at each HIGH moment, service-flow assumptions, equipment and layout, training assumptions, standards and metrics, review cadence) is the ONE Gallery Operations Brief, Oct 2026 revision. The point: a band that cannot be staffed is discussed, never silently degraded; unavailable data is written as assumptions "to replace with data". Source: Drive › one gallery new › 02 Operations (Operations Brief, Oct 2026).

## Stage 4 — training

**E14 — The training plan.** The `vios-training-programme` house form for an open venue (five training principles, sessions ordered by weight, the three drills, the knowledge the trainee must hold) is the ONE Gallery Journey Training Plan v2, read with its Operations Brief, Oct 2026. The point: foundations first and alone, silences last and never skipped, shadow shifts only after the LOW moments. Source: Drive › one gallery new › 02 Operations, `ONE_Gallery_Journey_Training_Plan_v2`; `clients/one-gallery/README.md`.
