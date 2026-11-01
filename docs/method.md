# Method — the Vios reference set

Every client diagnosis, persona and brand book cites these files and no others. When a source changes version, update this page in the same commit as the first client file that uses the new version. Pinned 2026-10-31.

## Primary sources

| # | Source | Version / date | Where | What it governs |
| --- | --- | --- | --- | --- |
| M1 | VIOS The Practice — Part II, Chapter 2.1, Stage 1 Brand Strategy & Brand Book | v1.3 "Persona in Practice (Instrument 6)", file dated 2026-10-23 | OneDrive › projects › Vios-MG › `02_VIOS_Practice_Stage_1_Brand_Strategy_v1.3.docx` | The method: fourteen interrogations in order (2.1.2.1–2.1.2.14), deliverable, toolkit, patterns, briefs, harvest. The manuscript the skills quote. |
| M2 | Branding Framework Master (process order) | 2026-10-27 | Drive › Projects › Estem › `00_Branding_Framework_Master.md` (id 1ZAHkQZbGIftpL8cqLS3clyekMNHi0LIq) | One-page checklist of the same sequence mapped to Worksheets 1–8, 10 and Expression Worksheets 1–5. Its source set is **M2a** below; the single "Branding framework total" document it names was not found in this Drive on 2026-11-01 and may live in another account. |
| M2a | Branding toolbox (course materials, UDMCC1) | files dated 2026-10-07 (uploaded), originals 2025 | Drive folder **BRANDING RESOURCES** (id 1xw0j1xtyANGz129vCOcTDy8yWjQA-P-c, renamed 2026-11-01, under the same parent as the Stochna brand book) | Worksheets 1 Purpose, 2 Vision, 3 Mission, 4 Core Values, 5 Audience Persona, 6 Competitor Audit (xlsx), 7 Differentiator, 8 Positioning Statement, 10 Brand Personality Workbook; Brand Personality Questionnaire; Characteristics and Traits; Archetypes Reference Tool; Personal Brand Workbook; Expression worksheets 3 Brand Name and 4 Tagline; UDMCC1 audio transcripts 1.2–7.2 (txt). Local copies of worksheets 1 and 10 and the Brand Builder Pro guidelines template (pptx) sit in OneDrive › Menelaos - vioscollective.com › Pure Burger. The 2025 HTML export "Vios Gastronomy Branding Toolbox — Audience Persona Development" (id 1eUrHFc6UMbkWiKzUbSzQOcG1dPODLMhS) and a 2025 copy of worksheet 10 were moved into the folder on 2026-11-01 as the earliest version of the persona instrument. |
| M3 | Brand Guidelines Book — Structure Reference | 2026-10-27 | Drive › Projects › Estem › `01_Brand_Guidelines_Structure_Reference.md` (id 1sIp94CUBF5xuVM14Dw-WR_nU-_AZafgL) | Shape of the final brand book: Brand Wheel, tiered themes, tone-of-voice lexicon, logo, type, colour, brand in action, summary. Structure only, never wording. |
| M4 | vios-marketing plugin | plugin_01MreUJhqNX9z9FTjGpDDZZc, authored 2026-10; packaged copy `vios-marketing.plugin` in Drive › Projects › Estem (2026-10-27) | installed in Claude; skills on disk under `%APPDATA%\Claude\rpm\...\plugin_01MreUJhqNX9z9FTjGpDDZZc\skills` | The 12 operating skills. `vios-guardrails` is the binding file for hard lines, numbers and the client-folder convention. |
| M5 | vios-brand-book skill | 2026-10-27 | OneDrive › projects › Vios-MG › `vios-brand-book.skill` | Earlier standalone brand-book skill; superseded by M4 for operations, kept for the book format. |
| M6 | Behavioural economics library | Kahneman, *Thinking, Fast and Slow*; Gladwell, *Blink* | OneDrive › projects › Vios-MG (epub, pdf) | Source of the BE lens (`vios-be-lens`) and the five-line BE rule in guardrails. |

## Worked examples (what a finished Stage 1 looks like)

| Client | File | Version | Where |
| --- | --- | --- | --- |
| Atelier del Gelato | Brand Book v3 | 7 Oct 2026, replaces update 6/11 and v2 | Drive › Projects › atelier del gelato › `Atelier_del_Gelato_Brand_Book_v3.pdf` (id 1nniF9M7I00pXE61qFlupiGilWy6gmsd5); working record `OneDrive › Atelier del Gelato 2026 › Atelier_del_Gelato_Stage1_Decisions.md` |
| ONE Gallery | Brand Book v2.2 EN + BG; Instagram Framework | 22 Oct 2026 (v2.2); 3 Oct 2026 (IG framework) | Drive: `01a_Brand_Book_v2_2_EN.pdf`, `01b_Brand_Book_v2_2_BG.pdf`, `ONE_Gallery_Instagram_Framework_VIOS.pdf` (+BG) |
| Stochna Kitchen Brewery | Brand Book V2 | 23 Feb 2026 | Drive › `Stochna_Brand_Book_V2_23_2_2026.docx` (id 1kNiXMhTJxOKgbbFiSQaOueKK2X3BR15k) |

## How the skills map to the fourteen interrogations (M1 §2.1.2)

| Interrogation | Skill | Output file in the client folder |
| --- | --- | --- |
| 1 Purpose · 2 Vision · 3 Mission · 4 Values | `vios-brand-diagnosis` step 3 | `diagnosis.md` §4 |
| 5 Audience Persona | `vios-brand-diagnosis` step 4 | `diagnosis.md` §5 |
| 6 Competitor Audit | `vios-brand-diagnosis` step 5 (spreadsheet) | `diagnosis.md` §6 + audit xlsx in Drive |
| 7 Differentiator · 9 Positioning Statement | `vios-brand-diagnosis` step 6 | `diagnosis.md` §7 |
| 8 Brand Personality (archetype, role) | `vios-brand-diagnosis` step 7, then `vios-persona-builder` | `diagnosis.md` §8, `persona-bible.md` |
| 10 Core Message Blocks · 11 Story Framework | brand book (M3 structure); `vios-persona-voice` reads them | `brand-book.md` link to the PDF |
| 12 Brand Name · 13 Tagline · 14 Designer Selection | brand book; designer brief | `brand-book.md` |
| Expression in daily use | `vios-content-calendar`, `vios-persona-voice`, `vios-video-script`, `vios-consistency-qa`, `vios-ad-factory`, `vios-ads-audit`, `vios-monthly-report` | `content/`, `qa-log.csv`, `ads-plan.md` |

## Rules

- A client file that cites "the brand book" names the version and date from the tables above.
- When M1 moves to v1.4, re-read §2.1.2 and check each skill's steps against it before the next diagnosis.
- M2a holds the worksheets and transcripts M2 was built from; the single "Branding framework total" document is still unlocated. M1 is authoritative where any of them differ.
- Nothing from M3's source (Marketing Lancashire) is reused for clients; it is a structure model only.
