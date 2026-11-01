---
name: "vios-consistency-qa"
description: "Final pre-publish quality gate for any Vios Marketing asset (post, caption, story, video, ad, reply, Google post, landing page, client report) — checks it against the client's Persona Bible, brand book, visual lock, the behavioural-economics and non-verbal rules and the vios-guardrails hard lines, logs the verdict, and returns SHIP / FIX / HOLD / BLOCK with evidence. Use before anything is scheduled, published or sent to a client, and whenever someone asks \"is this on-brand?\"."
---

# Vios Consistency QA

Nothing goes out without a named human sign-off, and nothing reaches that human without this check. Drift is cumulative: one off-brand post is survivable, twenty teach the audience a different brand. The hard lines are defined in `vios-guardrails`; this skill enforces them.

## Load first (`vios-guardrails` › client file)

- `persona-bible.md` (traits, is/is-not pairs, never-list, tone by guest mood, signature phrases, Expression palette, register, emoji policy, disclosure set, **approver**, alcohol yes/no, **version and review date**). If the review date has passed, say so in the verdict header.
- `brand-book.md` (colours, type, logo rules, image style)
- `character-sheet/` (locked stills, expression stills, voice spec)
- `consents/` (releases, UGC permissions, expiry dates)
- `fact-sheet.md` (the only source for facts)
- The asset(s), platform, language, publish date; for video: script + cue sheet and, if available, stills or the cut

## Evidence rule

A pass has to be earned. Facts are checked against the fact sheet; no source → "needs human check". Video face checks need stills or the cut; script only → "unverified on final cut". Rows that don't apply are **N/A**, never pass.

## The checklist

| # | Check | Pass looks like | If failed |
| --- | --- | --- | --- |
| 1 | Meaning | Expresses the purpose or a pillar; not noise | fix |
| 2 | Persona voice | Traits present on the "is" side of every is/is-not pair, never-trait absent, plain words, right register; replies: tone matches the guest-mood row, no second pitch after a decline | fix |
| 3 | Signature | A signature phrase or habit appears naturally, or deliberately doesn't | fix |
| 4 | One message | Sayable in one sentence | fix |
| 5 | One CTA (or none) | No competing asks | fix |
| 6 | Locality | Neighbourhood or city named where it matters (ads, Reels, GBP) | fix |
| 7 | Visual identity | Per brand book | fix |
| 8 | Character lock | Face, wardrobe, anchor detail, setting match the character sheet | block (regenerate) |
| 9 | Face & voice (video) | `vios-nonverbal-lens` checks (or the 5-point stand-in in guardrails) pass on stills/cut | block |
| 10 | Pressure / scarcity | True, verified fact stated once, plainly (guardrails 1) | FIX: true and verified but pressure wording ("last chance", "hurry") → rewrite as the plain fact. BLOCK: false or unverifiable claim, timer, counted scarcity, or the same pressure in the corrected line |
| 11 | BE rules | Hook within 3 s (video), peak + end designed, tone labelled | fix |
| 12 | Food truth | Guardrails 5 | block |
| 13 | Facts | Verified against the fact sheet (reports: against the saved data files) | block |
| 14 | AI disclosure | Guardrails 6, full set: account bio line live, first-frame label, platform AI label (or "label ✓ confirmed live"), caption hashtag, dual paid + AI label on partnerships; persona does not speak or sign in a real person's name | block |
| 15 | Consent & rights | Guardrails 7; 2 (UGC permission in `consents/`, verbatim reviews, partnership labels); 9 (music); no minor in frame without a release | block |
| 16 | Alcohol, allergen, claims | Guardrails 8, 9 | block |
| 17 | Platform fit | Length, ratio, safe zones, caption limits, hashtags 3–5 specific | fix |
| 18 | Language | Right language and register; both versions in persona voice, not translated | fix |
| 19 | Accessibility | Captions on video, alt text on images, contrast on overlays | fix |
| 20 | Escalation | A reply on an escalation topic (guardrails 11) was drafted instead of handed to the approver | block |
| 21 | Other hard lines | Guardrails 3, 4, 12 | block |
| 22 | Persona error history | No open correction for this persona; fewer than two serious errors this month (guardrails 6 error rule) | hold |

## Verdicts

- Any **block** → BLOCK, with the reason and what must change.
- Any **unverified / needs human check** or **hold** row and no block → HOLD: name who checks and what they need.
- Only **fix** rows → FIX, with the corrected version supplied (rewrite the line, re-spec the shot).
- All pass or N/A → SHIP, addressed to the named approver.
- After a FIX: re-run the failed rows on the corrected asset, log attempt 2. Pass rate = first-attempt SHIP only.

## Log every verdict

Append a row per the guardrails `qa-log.csv` schema; `signed_off_by` and `signed_off_at` are filled by the approver's reply, and nothing schedules without them.

## Output format

```
## QA — [asset] — [platform] — [date] — attempt [n]
Verdict: SHIP / FIX / HOLD / BLOCK

| # | Check | Result | Evidence / fix |
(rows in number order; only fix, block, hold, unverified; then one line: "all other checks pass or N/A")

### Corrected asset (if FIX)

Approver: [name] — nothing publishes without this sign-off.
```

Keep it short. The team reads this between shifts.

## Example

```
## QA — "Strawberry is back" Reel — Instagram — 12 May — attempt 1
Verdict: BLOCK

| # | Check | Result | Evidence / fix |
| --- | --- | --- | --- |
| 6 | Locality | fix | No place named. → hook card "FIRST STRAWBERRIES · [NEIGHBOURHOOD]" |
| 9 | Face & voice | unverified | Script only; needs the cut or 3 stills |
| 10 | Pressure | block | "Get it before it's gone!!!" implies scarcity that is not on the fact sheet (unverifiable) → BLOCK. → "Strawberry is on the counter from today." |
all other checks pass or N/A

### Corrected asset
Hook card: "FIRST STRAWBERRIES · [NEIGHBOURHOOD]". Line 3: "Strawberry is on the counter from today."

Approver: [name] — nothing publishes without this sign-off.
```

## Batch and report modes

- **Batch** (a week's calendar): one summary table (asset, verdict, top issue), then details only for FIX, HOLD and BLOCK. Three assets failing the same check = a brief problem, say so.
- **Report** (a client memo or dashboard): row 13 against the saved data files (re-compute at least the 5 headline numbers), every percentage carries n, no estimates; rows 14–16 N/A; row 21: dashboard private, recipient named by the account manager. Log as asset "monthly report".