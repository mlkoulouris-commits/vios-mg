# Working in vios-ops

This repo is the Vios Marketing department's system of record. The Vios plugins must be enabled
(`vios-core` first, then `vios-brand`, `vios-journey` and `vios-marketing`; source in `plugin/`, marketplace in
`.claude-plugin/marketplace.json`); their skills do the work, this repo holds the inputs and outputs.

## Before any client work
1. Load `vios-core:vios-guardrails`.
2. Open `clients/<slug>/` and read the `persona-bible.md` front page (approver, register, emoji policy,
   alcohol, AI disclosure, version) and `fact-sheet.md`. If a file is missing, say so and use the
   guardrails stand-in; never improvise facts.
3. Check `accounts.md` for the Metricool brand id and ad account ids before any connector call.

## Stage → skill → tool
See `docs/plan.md`. Short version: copy = `vios-persona-voice`; video = `vios-video-script`;
month plan = `vios-content-calendar`; gate = `vios-consistency-qa` (append a row to `qa-log.csv`);
publish = Metricool connector only after `signed_off_at` is filled; ads = `vios-ad-factory` /
`vios-ads-audit`; month end = `vios-monthly-report`.

## Rules
- Never schedule, publish, reply publicly, spend, or email a client. Draft and hand to the approver.
- Hard line 11 topics (allergy, illness, injury, legal, press, named staff, discrimination) are
  escalated with the facts, not drafted.
- Show `n` beside every percentage; below 30 per side show raw numbers.
- Dates for holidays and events come from `calendar-sources.md`, never memory.
- Write in English in this repo; client-facing copy in the client's languages (BG/EN/EL).
- No git commit or push without an explicit order from the user.
