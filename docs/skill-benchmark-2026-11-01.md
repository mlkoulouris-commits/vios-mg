# Vios skills benchmark against skill-authoring best practices

Date: 2026-11-01. Scope: the 19 skills in `plugin/vios-core`, `vios-brand`, `vios-journey`, `vios-marketing`, plus the 5 scheduled-task prompts. Rubric: Anthropic skill-creator guidance (description triggers, progressive disclosure, resolving paths, why-not-MUST style, defined outputs, workflow clarity, testability, redundancy, tool fallbacks). Static audit only; no eval runs were executed.

## Bottom line

Overall: **3.8 / 5**. Structure is sound (all plugins packaged, cache in sync, every `../../references/` path resolves, no CAPS-heavy prose, bodies 35–123 lines). The gaps are system-level, not per-skill: no evals anywhere, numbers copied between skills, two schedule contradictions, client-specific text in general skills, and 12 stale duplicate copies of the skills on claude.ai.

## Scorecard (1–5)

| Skill | Desc | Disclosure | Paths | Style | Output | Workflow | Tests | Drift | Avg |
|---|---|---|---|---|---|---|---|---|---|
| vios-guardrails | 4 | 4 | 3 | 4 | 3 | 4 | 2 | 3 | 3.4 |
| vios-be-lens | 4 | 4 | 5 | 4 | 3 | 4 | 2 | 2 | 3.5 |
| vios-nonverbal-lens | 4 | 3 | 5 | 4 | 3 | 4 | 2 | 3 | 3.5 |
| vios-filter-test | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 2 | 4.0 |
| vios-brand-diagnosis | 2 | 4 | 5 | 3 | 4 | 4 | 2 | 3 | 3.4 |
| vios-messages-and-story | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 3 | 4.3 |
| vios-persona-builder | 4 | 3 | 5 | 3 | 5 | 4 | 2 | 2 | 3.5 |
| vios-name-and-tagline | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 3 | 4.3 |
| vios-brand-book | 5 | 4 | 5 | 4 | 4 | 5 | 3 | 3 | 4.1 |
| vios-journey-map | 4 | 3 | 5 | 3 | 4 | 5 | 2 | 3 | 3.6 |
| vios-journey-design | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 3 | 3.5 |
| vios-training-programme | 4 | 3 | 5 | 3 | 4 | 5 | 2 | 3 | 3.6 |
| vios-content-calendar | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 3 | 4.1 |
| vios-persona-voice | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 3 | 4.1 |
| vios-video-script | 4 | 4 | 5 | 4 | 5 | 5 | 2 | 3 | 4.0 |
| vios-consistency-qa | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 4 | 4.3 |
| vios-ad-factory | 4 | 4 | 5 | 4 | 4 | 5 | 2 | 3 | 3.9 |
| vios-ads-audit | 5 | 4 | 5 | 5 | 5 | 5 | 2 | 2 | 4.1 |
| vios-monthly-report | 5 | 4 | 5 | 3 | 5 | 4 | 2 | 3 | 3.9 |

Best pattern to copy: the marketing descriptions (what + trigger phrasings + "Not for X (sibling)"). Weakest description: vios-brand-diagnosis (no trigger phrasings, no not-for).

## Findings ranked by impact

### 1. Contradictions (fix first)
- **Ads audit day**: skill says Tuesday morning (`vios-ads-audit/SKILL.md:109`); `setup/scheduled-tasks.md:8` runs it Mon 08:00.
- **Monthly report day**: skill says working day 3–5 (`vios-monthly-report/SKILL.md:12`); scheduled task runs on the 2nd.
- **Pre-shift length**: 10–15 min (`vios-training-programme/SKILL.md:26`) vs 15–20 min (line 62, matching the manuscript).
- **Library names that do not exist**: guardrails line 27 and be-lens checks 4, 5, 7, 9 cite "proper choices", "tone ladder", "commitment devices", "system output" as section 3.1 entries. The reference has 17 principles (cognitive ease … thin-slicing) and none of those names, so be-lens' rule "cite entries by their section-3.1 name" cannot be followed.
- **Persona gap across plugins**: brand-book Part 5 expects tone sliders, word rules, hard moments, ten-line checklist; vios-persona-builder produces none of those by name.

### 2. No evals anywhere
Zero `evals/` folders across 19 skills. Cheapest seeds, in order: vios-consistency-qa (deterministic SHIP/FIX/HOLD/BLOCK fixtures), vios-ads-audit (two fixture exports → expected flags), vios-filter-test (its own 10-pass/10-fail batches already exist as a method).

### 3. Numbers and rules copied instead of pointed
Same value today, will drift:
- winner rule (≥1,000 imp, ~15 results, ≥30 % gap) and audience ≥1,000: ads-audit ↔ ad-factory lines 33–34
- n≥30 and the "3 vs 6" sentence: guardrails ↔ monthly-report
- 2-hour pull / two errors per month and the disclosure set: guardrails 6 ↔ persona-builder steps 9–10 (verbatim)
- touchpoint list: guardrails ↔ messages-and-story line 63
- hashtags 3–5: persona-voice ↔ QA row 17; ≤3 emphasis cards: video-script ↔ persona-voice
- 20–50 moments: guardrails ↔ journey-map
- guardrails cites QA by row number ("FIX per QA row 10", row 22); renumbering QA silently breaks guardrails. Give rows stable ids.

### 4. Progressive disclosure is nominal in core and journey
Six references over 300 lines (3.1: 577, 3.2: 663, stage-1: 530, stage-2: 328, stage-3: 415, stage-4: 466) have no table of contents, and the skills that use them say "read first, verbatim". Every journey run loads ~1,000 lines. messages-and-story and name-and-tagline do it right (point to sections). nonverbal-lens sends the reader through a 663-line floor library for a camera check; name the three sections that matter.

### 5. Client-specific text in general skills
ONE Gallery (all three journey skills, with "Oct 2026 revision" dates; brand-book; messages-and-story; name-and-tagline), Stochna, Atelier, Barsy (brand-diagnosis line 24, monthly-report line 18; Barsy is being dropped), "Module 1 Brand Persona Studio" and a version-history paragraph in persona-builder. Move house examples to one `references/house-form-example.md` or a README line.

### 6. Duplicate skill copies on claude.ai
12 standalone copies under the claude.ai skills folder (installed 24–26 Oct) sit beside the plugin versions and trigger alongside them in every session. They are stale: persona-builder differs by 242 lines, brand-diagnosis by 172, content-calendar 29, persona-voice 27, guardrails 21. Remove the standalone copies and keep the plugins as the only source.

### 7. Smaller consistency items
- Skill names sometimes prefixed (`vios-core:vios-guardrails`) and sometimes bare; bare names are ambiguous while the duplicates above exist.
- Guardrails line 27 uses a plugin-rooted path (`vios-core/references/…`); every other skill uses `../../references/…`.
- Guardrails archive table omits `deep-interrogation.md` (name-and-tagline) and `filter-test-batches.md` (filter-test).
- Frontmatter quoting mixed (be-lens, nonverbal-lens, ads-audit unquoted).
- Descriptions of journey-design (660 chars) and training-programme (703 chars) are inventories; move the inventory into the body.
- vios-marketing README points at `setup/scheduled-tasks.md`, which is outside the packaged plugin. Scheduled task expects "one ClickUp task per post" from the calendar; the skill never mentions ClickUp.
- Tool fallbacks missing: calendar-sources.md absent (content-calendar), Metricool/GBP not connected (monthly-report D2–D5), Meta Ad Library route (ad-factory).
- Brand-diagnosis lists 10 interview questions in the body while `references/worksheets.md` has 11 and says it wins.
- `*.plugin` zip artifacts sit beside the sources in `plugin/`; gitignore or move to `dist/`.

## Suggested order of work
1. Fix the five contradictions (section 1). One commit, no behaviour change beyond correctness.
2. De-duplicate numbers: one owner per number, siblings point (section 3). Give QA rows stable ids.
3. Delete the 12 claude.ai standalone copies.
4. Add TOCs to the six big references and replace "verbatim" with section pointers.
5. Strip client names into an examples reference.
6. Seed evals for consistency-qa, ads-audit, filter-test; then run the skill-creator eval loop and description optimiser on brand-diagnosis.
