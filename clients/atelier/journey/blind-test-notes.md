# Blind generation test — vios-journey on Atelier del Gelato (2026-11-01)

Run without opening anything about ONE Gallery: not the client folder, not the dry-run doc, not Drive. The only ONE Gallery facts in my context are the ones the skills themselves quote (the 6/12/10 split, "28 pages", "M13–M21 protects the peak at M18"). Inputs used: `vios-core:vios-guardrails`, `vios-journey:vios-journey-map`, `vios-journey:vios-journey-design`, `vios-core:vios-filter-test`, their references (stage 2, stage 3, §3.3, §3.4, and the §3.1 / §3.2 headings plus three entries), Brand Book v3 PDF from Drive (read in full), `brand-book.md`, `persona-bible.md`, `diagnosis.md`, `fact-sheet.md`, `calendar-sources.md`, and a skim of `content/` for operational facts. Nothing committed.

## Result in one line

8 phases, 31 moments: 6 HIGH, 12 MEDIUM, 10 LOW, 3 silent. Signature ★ M7 the question. Peak ◉ M15 the Note from the jar. End ⊐ M22 farewell + M23 attention held to the door. One design page (M07) and the filter test ("Is this processing the guest?").

## Tool calls per step (excluding task-list calls)

| Step | Calls | Of which |
| --- | --- | --- |
| 1 Load skills, read inputs | 11 | 2 skill loads, 1 Drive read, 1 tool load, 7 file reads (reference, three-registers, four client files, content skim, folder listings) |
| 2 Journey map set | 9 | 1 failed heredoc, 1 mkdir, 6 writes (map, intake, reasoning note, handoff, inventory, harvest), 1 brand-book edit |
| 3 Filter test and design page | 10 | 2 skill loads, 4 reference reads (§3.4, stage 3 twice because of output size, §3.1/§3.2 headings and entries), 1 brand-book edit, 2 writes |
| 4 Notes | 2 | this file, git status |

About 32 calls end to end. The reading dominated; writing the map was mostly thinking, not tool time.

## Where a skill was unclear

1. **`vios-journey-map` › Move 0.** "One page … Opens `[client]/journey/` as the Stage 2 file" names no file. I wrote `journey/intake-stage-2.md`. The reasoning note's prescribed order has no slot for the intake, so it could not go there.
2. **Shares of the inventory.** "State the distribution as counts and shares (ONE Gallery: 6 HIGH 21 %, 12 MEDIUM 43 %, 10 LOW 36 %)" sums to 100 % with no silences, yet the house form counts silences separately. I gave shares of all 31 with silences as their own row. The skill should say which denominator. (My honest weights landed on 6/12/10 as well, which looks copied and is not; the example numbers in the skill may be pulling the count toward them, and a reviewer cannot tell.)
3. **Owner column.** The bridge step needs "who owns it (marketing or floor)" per touchpoint, but the per-phase table in the house form has no owner column. I assigned owners by hand at the bridge. Either add the column or say the bridge derives it.
4. **Languages.** The skill says the map, note and handoff are delivered in EN and BG, "the BG version a redraft". `CLAUDE.md` says write in English in this repo, client-facing copy in the client's languages. I wrote EN only and left the BG redraft pending; the skill should say whether BG lives in the repo or only in the Claude Doc.
5. **Claude Doc.** "The Claude Doc version when the docs connector is present." The connector is present; I did not make one. Reason: the test is about the files, and a Doc is an outward artefact the owner has not asked for. The skill should make the Doc explicitly a step the account manager triggers, or explicitly automatic.
6. **"One or two pages when rendered."** With 31 moments in the house-form table and the Stage 3 summary, the map is about four rendered pages. Either the house form has grown past the manuscript's two-page rule, or the per-phase tables should drop the intention text for LOW moments to a few words. I kept full cells for traceability.
7. **Second audience.** The skill reads one persona; the guardrails say a B2B line "adds partner table and delivery as named touchpoints". Nothing says how to map a phase whose customer has no persona. I mapped phase 8 thin, all MEDIUM, with the owner's target states invented from the brand book's B2B tone row only, and flagged it. The skill should say: stop at the B2B line until a persona paragraph exists, or map it MEDIUM-only as I did.
8. **Silent moments and the four fields.** The manuscript says silent moments "are not given the four-field treatment". The house form table has the columns anyway; I left them empty with ○ in weight and marker. Fine, but the skill could say so.
9. **`vios-journey-design` › working order vs the task.** The skill orders peak and end first; the task asked for the signature. I wrote M07 out of order and said so on the page. The skill has no instruction for a partial set (one page written before the schedule exists); it assumes the whole set. A "single page" mode (what to reference when `choreography.md` and `recovery.md` do not exist yet) would help: I referenced them as "to be written".
10. **Design page file name.** "`pages/M01.md … Mnn.md`" implies two-digit codes; the map uses M7. I named the file `M07.md` and the header `M07`. The map and the pages should use one convention; I would change the map to M01–M31 on the next edition.
11. **BE and NV cross-references.** The design skill says "named from section 3.1" and the example cites "§3.1.17", "§3.1.1". The reference file numbers principles "### 17. Thin-slicing" under 3.1.5, so "§3.1.17" does not exist as a heading. I cited "BE 17" and "NV C.2". The skill should fix the citation form.
12. **`vios-filter-test` › output location.** "`[client]/brand-book.md` › Part 5 › Filter test". `brand-book.md` has no Part 5; its sections are the live summary's own. I added "## Filter test (Part 5; …)" at the end. The skill should say "a section named Filter test, under Messages and story if the file has no parts".
13. **Filter test scope.** The reference says the test applies to "any piece of content the brand produces". The tagline "Happiness is an attitude." fails the test as written (a slogan talks past the person), and so would Doppio's. I scoped the test to lines addressed to a guest, partner or team member and said taglines are judged by the brand book. The skill should say whether the tagline is inside or outside the test.

## Where an input was missing (marked "to confirm" in the files)

- B2B venue owner persona (diagnosis §5 flags it; nobody has written it).
- How the ritual survives a Ring Mall queue (diagnosis contradiction 4; asked of Evo 2026-10-30, unanswered).
- Room facts: current counter height, whether the display is visible from the street, where the tables are, whether the celebration board exists, who draws the Note (guest or team member).
- Prices, allergen policy, the legal age line for the Aperitivo gelato, Ring Mall hours.
- The email capture route (the brand book lists four email pieces; nothing says how an address is collected).
- The core messages and story blocks are in the PDF and not in `brand-book.md` ("to transcribe" still stands). I read them from the PDF; a skill run without Drive access would have had to use the guardrails stand-in for the intention column.
- `brand-book-vN.md` does not exist (the skill reads it); the PDF stood in.

## Decisions taken without guidance

- **Eight phases, B2B as the eighth.** The skill allows 4–8; the Vision forces the partner table in. Alternative was a separate B2B map; rejected because the B2B customer has no persona to build it for.
- **Threshold split into M4 (the room) and M5 (the person), with HIGH on the person.** The manuscript's threshold is sensory-dominant and the brand book's differentiator "needs no theatre, only people". A restaurant would put HIGH on the room.
- **Signature before the peak.** The skill example and the practice's phrasing ("usually a different moment from the peak") allow it but do not say the signature can precede the peak. The brand's own three-step ritual decided it.
- **The end as two HIGH moments.** The house form allows end-1 and end-2. Spending two of six HIGH on a thirty-second phase is unusual; the counter format (next guest already present) justified it.
- **M8 as a silent moment inside the threshold phase.** Not in the manuscript's three locations for silence (between HIGHs, private activity, transitions). It is a fourth kind: the pause the brand's own tone rule ("asks before she tells") implies. Recorded in the harvest.
- **Weights for the B2B phase all MEDIUM.** No persona, so no HIGH; not LOW, because the Vision rests on it.
- **The filter test's trait.** Candidates were refusal of theatre ("Is this performed?"), refusal of urgency ("Is this rushed?") and refusal of the transaction. I chose the transaction because the positioning, the persona's fear and the owner's stated hates all name it, and because "performed" would not catch "Next!" while "rushed" would not catch "That's our bestseller". The markers (hurry · sell · talk past) are what make one trait cover both; a stricter reading of "one trait" might call that two.
- **Recovery lines on M07** ("Then let's just choose something good.", "Pistachio it is.") are new floor-register lines not in the brand book. The design skill allows locked lines to be written at Stage 3; I kept them to the brand's key-phrase vocabulary and filter-tested them. Menelaos should read them as new copy.
- **Shares stated of 31, not of 28.** See unclear item 2.
- **Harvest written** (`archive/harvest-stage-2.md`) although the task listed five files; the skill lists it as output 6 and it cost one write.

## What a reviewer should look at first

1. Is M5 (the person) rather than M4 (the room) the right HIGH threshold for a counter format? If the room should carry it, the HIGH count rises to 7 or M11 drops.
2. Is M7 the right signature, or is the signature the whole ritual (M7 + M15) with the peak inside it? The map keeps them separate because Stage 3 needs two pages, not one.
3. Phase 8: keep, or cut until the B2B persona exists?
4. The filter test: does "Is this processing the guest?" read naturally in BG for the wall chart? I did not draft the BG form; the Bible's vocabulary has „обработват" only by implication.

## Not done

- BG redrafts of the map, note and handoff.
- Claude Doc rendering.
- The rest of Stage 3: 30 pages, choreography, recovery, briefs, schedule.
- Transcription of core messages and story blocks into `brand-book.md`.
- Nothing committed; nothing scheduled, published or sent.
