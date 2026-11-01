---
name: "vios-video-script"
description: "Write hook-first short-form video scripts (Reels, TikTok, Shorts, paid video ads, persona talking-head clips) for a Vios Marketing F&B client, with word-for-word captions, shot list with safe zones, expression cues, consent and disclosure placement, and ready-to-paste prompts for AI tools (Veo, Runway, HeyGen, Seedance) used only for the persona. Use whenever a client needs a video, a Reel, a TikTok, a video ad or a persona clip, even if the user only says \"make a video about the new menu\"."
---

# Vios Video Script

A script is a sequence of moments, not a list of features. This skill writes the first two seconds first, protects the peak and the ending, and hands production an exact plan the persona can perform without drifting. Hard lines: `vios-guardrails` 1–12.

## Load first (`vios-guardrails` › client file)

- `persona-bible.md` (voice, traits, never-list, Expression palette, register, approver, alcohol yes/no)
- `character-sheet/` (locked stills, expression stills, voice spec) and `consents/` (releases, UGC permissions). No character sheet or consent on file: write the script **filmed-only**, no persona, no AI prompts, and say so.
- `fact-sheet.md` (hours, prices, dish names, location)
- `brand-book.md` › Messages and story: the anchor core message and the story block this video plays (guardrails › Messages and micro-stories); the calendar row usually names both
- The brief: goal, the one offer or moment, platform, language(s), length, organic or paid

## What we follow, and why

- Viewers decide in roughly 2 seconds. Spoken hook starts at 0.0 s and finishes by 3 s; frame 1 moves; the hook card is visible in frame 1.
- Hook rate (3 s plays ÷ impressions) is our early diagnostic; platforms reward watch time, completion and sends. Benchmark: the client's own last 10 videos (no invented baseline, guardrails › Shared numbers).
- Views from outside the venue's catchment rarely become covers: name the neighbourhood early, give a reason to come this week.
- 15–30 seconds: long enough for a peak and an end, short enough to finish.
- **This skill owns the caption rule:** word-for-word captions of every spoken line, plus at most 3 emphasis cards. Most watch muted; captions are the dialogue.

## Structure (every script)

| Beat | Time | Job | Vios rule |
| --- | --- | --- | --- |
| 1. Hook | 0–3 s | Motion in frame 1 + spoken line ≤ 10 words done by 3 s; hook card ≤ 6 words in frame 1 | Thin-slice: frame 1 must read as this brand; name the place |
| 2. Promise | 3–5 s | What this video gives (a moment, not a menu) | One message |
| 3. Proof | 25–75 % of runtime | 2–4 shots that deliver it | The moment people would want to remember (Two Selves) |
| 4. Peak | at ~80 % | The single best second | Designed on purpose; this is what gets remembered |
| 5. End | last 2–3 s | Settled warm frame + plain invitation | Peak-end; one CTA or none |

A video is a micro-story: one anchor message, one story block, the guest as hero. The beats map onto the frame: the hook shows the hero's world or obstacle (blocks 1–2), the promise is the call to action (3), the proof is the guide at work (4) or the challenge surfacing (5), the peak is the transformation (6), the end is the new world (7). The brand never narrates its own story; the persona is the guide in frame, not the subject.

## Hook types (write 3 options, pick one)

1. **Local landmark** — "Behind the door you've walked past a hundred times."
2. **Question** — "What does Tuesday night in [neighbourhood] sound like?" (one option to test; question openers often hold early attention)
3. **Reveal first** — start on the result, then rewind to how.
4. **POV** — "POV: the corner table is free tonight."
5. **Quiet contrast** — a calm, slow opening in a loud feed (Sage/Caregiver brands; the brand decides).

Never: "Hey guys", "Don't miss", "best in town", "limited time", timers, screaming text (guardrails 1). A real date once, as fact, is fine.

## How many scripts

- **Organic**: one script with 3 hook options. Film all 3 hooks in the same shoot (first 3 s only), post each as a Trial Reel (shown to non-followers first, so the hook is tested without spending), then post the winner normally. If the venue can't film 3, use one hook and say so.
- **Paid**: one script per concept. Three tone scripts (neutral / suggestive / directive) only for the round-1 winner, per `vios-ad-factory`, which owns the test design.

## Persona on camera

Each spoken line gets an expression cue: emotion + intensity 1–5 + gaze (lens / away), e.g. `[Warmth 3, lens]`. Face lands a beat before the line; resting face between lines; last frame settled and warm, then cut. Final-cut check: `vios-nonverbal-lens`, or the guardrails stand-in.

## What AI may and may not generate

- **Generated**: the persona (from the locked character sheet) and VO from the locked voice. Nothing else.
- **Always filmed**: food, drinks, the room, the exterior, staff, guests (guardrails 5).
- **Consent** (guardrails 7) before generating or filming any real face or voice; write "consent: on file / needed" per shot in the shot list.

## Disclosure placement (guardrails 6)

"AI-generated" on-screen from the first frame in which the synthetic face **or voice** appears, voice-over included: a synthetic VO under shot 1 means the label starts at 0.0 s even if the persona enters later. Written into the cue column, plus the platform AI label at upload, noted under Checks.

## Output format

ALWAYS deliver, in this order:

```
# [Working title] — [platform] — [length]s — [language(s)]

Goal: … | Organic / Paid (concept: …) | One message: … | Anchor: [core message] | Block: [1–7]

## Hook options (3)

## Script
| # | Time | Shot | Spoken line (per language) | Caption (word-for-word) | Emphasis card (≤ 3) | Persona cue + AI label |

## Shot list
Shot, framing (CU/MS/WS), 9:16, location, props, what moves, light, audio, consent status.
Safe zones: keep text out of the top ~14 % and bottom ~35 % (covered by platform UI); keep the hook card and key subject inside the centre 3:4 crop so the profile-grid thumbnail still reads.
Audio: licensed or commercial-library only (guardrails 9).

## AI generation prompts (persona shots only)
- Veo / Runway / Seedance: one prompt per persona shot, character sheet attached, camera, motion, lighting, 9:16, duration, negative list.
- HeyGen: avatar id, voice id, line, emotion + intensity, gaze note.
- ElevenLabs: voice id, line, pace, warmth.

## Caption + cover text
Caption in persona voice (`vios-persona-voice`). Cover text ≤ 6 words.

## Checks
Hook: motion frame 1, ≤ 10 words by 3 s, card ≤ 6 words ✓ | locality ✓ | one message ✓ | anchor reinforced, no core message contradicted, guest is the hero ✓ | peak designed ✓ | end warm, one CTA or none ✓ | never-list ✓ | captions word-for-word ✓ | AI label from persona's first frame + platform toggle ✓ | consent per real face/voice ✓ | food/room/exterior filmed ✓ | alcohol rules if applicable ✓
```

## Workflow

1. Pin the one moment, its anchor message and its story block. Three moments = three videos.
2. Hook options first; choose one; everything else serves it.
3. Script, then shot list, then prompts. Lines short enough for captions.
4. Run Checks. Fix before delivering.
5. Say what to measure: hook rate, completion, sends per reach, saves, profile visits, bookings.

Before publish: `vios-consistency-qa` → named approver. This skill drafts; it never publishes.

## Example (taverna, Sunday lunch, 20 s Reel, organic, AI persona; GR with EN captions; placeholders; anchor "the table is the centre", block 6 transformation)

| # | Time | Shot | Spoken (GR) | Caption GR / EN | Emphasis card | Persona cue + AI label |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0–2 | CU ladle lifts from the pot, steam (filmed) | "Κυριακή στην [γειτονιά]." | Κυριακή στην [γειτονιά]. / Sunday in [neighbourhood]. | ΚΥΡΙΑΚΗ | VO: AI voice → label on from 0.0 s |
| 2 | 2–5 | MS persona at the long table, chairs empty, looks to lens (AI persona) | "Εδώ το τραπέζι γεμίζει στις δύο." | Εδώ το τραπέζι γεμίζει στις δύο. / Here the table fills by two. | — | [Warmth 3, lens], label already on |
| 3 | 5–14 | WS plates landing, bread passed, a laugh off-camera (filmed; consent: staff release on file in `consents/`) | "Κανείς δεν παραγγέλνει μόνος." | Κανείς δεν παραγγέλνει μόνος. / Nobody orders alone. | ΜΟΝΟΣ | — |
| 4 | 14–17 | Glasses raised, the laugh lands (peak) | — | — | — | — |
| 5 | 17–20 | Persona, settled smile, slight nod | "Έχει καρέκλα." | Έχει καρέκλα. / There's a chair. | [venue] | [Contentment 3, lens] |

Platform AI label: on at upload.