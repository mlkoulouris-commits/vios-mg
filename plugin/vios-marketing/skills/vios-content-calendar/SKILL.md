---
name: "vios-content-calendar"
description: "Build the monthly social content calendar for a Vios Marketing F&B client — pillars, venue rhythm, sourced BG/GR/EN holidays, capacity-matched cadence per platform, persona video cadence — ready to schedule through Metricool. Use whenever a client needs a content plan, a posting schedule, \"what do we post this month\", or a calendar for Instagram, TikTok, Facebook or Google Business. Not for one post's copy (vios-persona-voice) or ad scheduling (vios-ad-factory)."
---

# Vios Content Calendar

A venue's calendar is a logistics tool, not a gallery. It respects the kitchen, the slow days, the perishable moments and the meaning the brand stands for. Hard lines: `vios-guardrails` 1–12.

## Load first (`vios-guardrails` › client file)

- `diagnosis.md` + `persona-bible.md`: purpose, pillars, audience, archetype, never-list, approver, alcohol yes/no
- `brand-book.md` › Messages and story: core messages, the seven story blocks, micro-message blocks (guardrails › Messages and micro-stories). Missing: anchor slots to purpose + pillar and flag "no message architecture on file"
- `fact-sheet.md`: venue rhythm (open days, slow days, peak days, events), seasonal menu changes
- `accounts.md`: Metricool brand id, platforms, languages
- `calendar-sources.md`: holidays, name days, school holidays, festivals, from dated sources, never memory (a wrong date in a public post is a block-level fact error)
- Last month's `vios-monthly-report` if it exists (new client: skip and say so)
- `character-sheet/`: none → persona-video cadence = 0, replaced by team-filmed Reels
- Team capacity: who can shoot, hours per week

## Principles

- **80/20.** Roughly 80 % community, story and moment content; 20 % direct offers. Feeds that only sell empty out.
- **Sell the visit, not the menu.** Every post answers "why come this week?".
- **Pillars are the brand.** 4–5 from the purpose and persona. Default set, adapted per client: the place and its people · the moment (the persona's territory) · the craft · the neighbourhood · guest moments and proof (UGC with permission, reviews, regulars; the highest-trust content). Persona video and offers are formats and CTAs, not pillars.
- **Perishable vs evergreen.** Evergreen scheduled weeks out; perishable posted same-day from the floor. 15–20 % of slots open for it.
- **Consistency beats volume.** A sustained 2 a week beats 5 then silence; consistency is what guests thin-slice when they check the profile before choosing.
- **Rotate pillars** so no two consecutive weeks lead with the same one: a profile check should show range.
- **The month tells the story, the post tells a moment.** Every slot is a micro-story: one anchor core message and one story block (guardrails › Messages and micro-stories). Across the month the seven blocks are all played at least once, led by blocks 1–4 and 6; block 7 (the new world) belongs to proof and regulars content, block 5 (the challenge) to the persona's quieter pieces. Never two consecutive posts in the same block, never a post that narrates the whole arc.
- **System output, not guest tendency.** "Guests share us themselves" is built by giving them a moment worth posting.
- **Offline metrics.** Judged on bookings, covers, repeat visits and organic tags.

## Cadence (pick the row that matches capacity; never plan above it)

| Capacity | Instagram feed | TikTok | Facebook | Google Business | of which persona video |
| --- | --- | --- | --- | --- | --- |
| Minimum viable (owner-run) | 2 (1 Reel) | optional | cross-post | 1 / week | 1 every 2 weeks |
| Standard | 3–4 (≥ 2 Reels) | 2–3 | 2–3, local angle | 1 / week + photos | 1 / week |
| Signature | 5 (3 Reels) | 4–5 | 3 | 2 / week + offer/event | 2 / week |

Persona videos count inside the Reel/TikTok numbers; they are the costliest asset. Stories: a weekly template, not a row per story. Rough effort: Reel 2–3 h, carousel 1 h, photo 30 min, persona clip 3–4 h; check the month's total against hours available.

Posting times: Metricool best-time data when connected. Until it exists, schedule around the venue's own decision moments (guests choose dinner at lunchtime, the weekend on Thursday); treat as a hypothesis, test in month one. No invented benchmarks (guardrails › Shared numbers).

## Workflow

1. **Map the month.** Days open, slow days, events, sourced holidays, menu changes. Mark the 2–3 moments the month is built around.
2. **Assign pillars by week**, rotating.
3. **Fill slots.** Date, platform, language, pillar, anchor message, story block, format, the one idea, hook, CTA or none, owner, asset, status. Touchpoint-shaped slots (booking reminders, GBP posts about arrival or parking, after-visit thank-yous) name their micro-message block in the brief.
4. **Offers on slow days**, where the venue needs covers. A real date once; no pressure devices.
5. **Persona cadence.** Scripts from `vios-video-script`.
6. **Community block.** Daily on the calendar: comments, DMs, tags, reviews (`vios-persona-voice`).
7. **Perishable slots** with "from the floor" briefs the staff can shoot on a phone.
8. **Feed the loop.** Top organic posts (saves, sends, shares) go to `vios-ad-factory` as existing-post ad concepts.
9. **Check** every slot: BE five-line · locality · never-list · alcohol rules if applicable · anchor message named and not contradicted · story blocks covered across the month, none repeated back to back.

## Output format

ALWAYS deliver:

1. **Month at a glance** — moments, pillar rotation by week, offer days, capacity row, estimated hours vs available.
2. **Calendar table** (one row per post; a row per language when posts go out separately; "BG+EN" in one row when both share a caption):

| Date | Day | Platform | Lang | Pillar | Anchor | Block | Format | Idea | Hook | CTA | Owner | Asset | Status |

Anchor = the core message by short name; Block = story block 1–7 (or the micro-message block name for touchpoint copy).

Status: idea → drafted → QA (SHIP) → approved → scheduled → label ✓ (persona posts). "Posted" is the platform's job, not ours.

3. **Stories template** for the week: one line per day with its block, so the week's stories read as a sequence (e.g. Mon existing world · Wed obstacle · Thu call to action · Fri meeting the guide · Sat transformation · Sun new world), each story still one moment.
4. **Production list** grouped by shoot day (batch recording saves the team), with consent needs.
5. **Scheduling** — either the current Metricool bulk-upload CSV template (download it first; it moves and its columns change), or schedule through the Metricool connector at best time per network. Only posts whose QA-log row shows SHIP with `signed_off_at` filled get scheduled. Persona or synthetic posts: confirm the scheduler can set the platform AI label; if it can't, publish natively, tick the label by hand and verify after publish (guardrails 6), status "label ✓".
6. **Open slots** — the "from the floor" briefs.
7. **What we'll measure** — sends per reach, saves, tags, profile visits, bookings, covers on offer days vs the same-weekday baseline.

Before scheduling: `vios-consistency-qa` → named approver. This skill plans; it never publishes.

## Example week (events café, October; pillars place & people / moment / neighbourhood / proof; dates shown as week labels because real dates come from the sourced calendar; capacity row: Standard; TikTok shown 1 of 2–3, Facebook 1 of 2–3)

| Date | Day | Platform | Lang | Pillar | Anchor | Block | Format | Idea | Hook | CTA | Owner | Asset | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wk 2 | Mon | IG | BG+EN | Place & people | Made here | 4 guide | Reel | The room being set for Thursday's vinyl night | "Четвъртък се подготвя от понеделник." / "Thursday starts on Monday." | none | M. | Reel 20 s | drafted |
| Wk 2 | Wed | IG + FB | BG | Neighbourhood | Place matters | 1 existing world | Carousel | The three shops on our street we buy from | "Нашата улица." | none | M. | 5 photos | idea |
| Wk 2 | Thu | TikTok | EN | Moment | Human, not performed | 5 challenge | Talking-head (persona) | Why the lights go down at nine | "At nine we turn the lights down. Here's why." | none | persona | clip 25 s | QA |
| Wk 2 | Fri | GBP | BG | Moment | Worth the trip | 3 call to action | Post | Friday 21:00 live set, table for the late show | — | "Book" | M. | 1 photo | scheduled |
| Wk 2 | Sat | IG story | BG | Proof | Table is the centre | 6 transformation | UGC repost (permission on file) | Guest's photo from Thursday | — | none | M. | — | idea |
| Wk 2 | Sun | IG | BG+EN | Moment | Worth the trip | 7 new world | Reel | Sunday morning, first coffee, empty gallery | "Преди да отворим." / "Before we open." | none | M. | Reel 15 s | idea |