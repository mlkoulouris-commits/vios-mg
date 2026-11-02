---
name: "vios-persona-voice"
description: "Write any client-facing text in a Vios Marketing client's Brand Persona voice — captions, stories, ad copy, comment and DM replies, review responses, booking messages, Google posts — in BG, GR or EN with the right address register, and flag off-brand lines. Use whenever copy for an F&B client is drafted, rewritten or checked, even if the user just says \"write a caption\" or \"answer this review\". Not for final pre-publish gating (vios-consistency-qa), ad test design (vios-ad-factory) or video scripts (vios-video-script, which calls this skill for the caption)."
---

# Vios Persona Voice

The Brand Persona is a character. This skill makes it speak the same way every time, on every channel, in every language, so guests recognise it before they read the logo. Hard lines: `vios-guardrails` 1–12.

**Work in three steps. Stop after each and ask one question.** Each step shows at most ten plain lines (a two-column table counts as its rows); no open-fact numbers, section references or file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. A single caption or reply is brief → draft → done; a batch (a week's captions, a day's replies) repeats step 2 per piece. Nothing is written to disk before step 3 (status.json and open-facts.md bookkeeping aside). Read `clients/<slug>/status.json` and `open-facts.md` first: what they answer is never asked again.

## Steps

1. **Brief.** Confirm channel, moment, goal, language(s), register. Infer when obvious; ask only if a wrong guess would waste the client's time. Name the anchor core message and the story block; for touchpoint copy, the micro-message block. Ask: *"Right brief?"* (when everything was inferred from the request, go straight to step 2.)
2. **Draft.** Draft in the persona. Mark the tone used. Self-check against the Persona Bible: traits present, never-trait absent, signature phrase natural, one message, local detail, plain words, register right; anchor reinforced, no core message contradicted, guest still the hero. BE check on anything with a CTA. Flag anything off-brand in the brief itself ("limited time only!!!") and offer the on-brand version. Ask: *"Change anything before it goes to Review?"*
3. **Done.** Now write the file and the ClickUp task, then the end line.

**Ask only when necessary; never invent.** Hours, prices, dish names, dates, claims and the register come only from `fact-sheet.md`, `persona-bible.md` or the user, never from memory. A fact the piece needs and the user can give now is one question; otherwise the line reads "to confirm" (never a placeholder number), with a row in `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker in `status.json`, and the draft goes on. No Persona Bible: the guardrails stand-in, "DRAFT, no persona", flagged. No approver on file: a blocker, never a placeholder name. Hard-line 11 topics (allergy, illness, injury, legal, press, named staff, discrimination) are never drafted: the facts go to the approver.

**After every step:** write the file → update `clients/<slug>/status.json` (`updated`, blockers added or removed) → at step 3: captions, stories, Google posts and ad copy to `clients/<slug>/content/YYYY-MM/captions_<scope>_draft-<date>.md`, replies to `clients/<slug>/content/YYYY-MM/replies_<date>.md`; then the ClickUp task for the piece in the client's Content list (replies: the Engagement list; ids in `accounts.md`), status **review**, the draft in the description, Stage = Marketing, Approver = the approver in `status.json` matched to `setup/clickup.json` ("To confirm" when unmatched), one `create_many` call per list (the pattern in `setup/scheduled-tasks.md` › ClickUp Review). A blocked client gets the blocker in `status.json` and no task. The QA gate stays: nothing moves past Review without `vios-consistency-qa` and a `qa-log.csv` row with `signed_off_at`.

## Load first (`vios-guardrails` › client file)

1. `persona-bible.md`: traits, never-trait, point of view, signature phrases, humour level, do/don't lines, behaviour matrix, address register, emoji policy, approver.
2. `fact-sheet.md`: hours, prices, dish names, claims we may make.
3. `brand-book.md` › Messages and story: the core messages, the seven story blocks, the micro-message block for the touchpoint (guardrails › Messages and micro-stories). Missing: guardrails stand-in, flagged in the output line.
4. The channel, the moment (launch, slow Tuesday, event, complaint, holiday), the language(s).

No Persona Bible: use the guardrails stand-in (fact-only copy, "DRAFT, no persona"); a guessed voice is the fastest way to drift.

## Voice rules

- **Plain over flattering.** No hype, no performed enthusiasm, no "amazing / must-try / best in town". The persona respects the guest as a decision-maker.
- **One message per piece.** Cognitive ease is the strategy.
- **Show the moment, not the product.** Guests remember moments (Two Selves); the dish is the proof.
- **Neutral / suggestive / directive.** Question, proposal, recommendation. Plain form by default.
- **The never-list is hard**, even when a trend or template uses the word.
- **Local first, in the first line.** Instagram and TikTok are searched; the place and dish keywords belong there, naturally.
- **Languages.** The market's language; EN alongside BG or GR when asked (two-column table, local language left). Rewrite each version in the persona's voice, never translate tone. Register from the Persona Bible; if it isn't stated, use the guardrails default (informal social, formal booking) and flag it in the output line, so the draft isn't stalled between shifts. Greek: monotonic, correct accents.
- **Emoji** per the Persona Bible, default none or one. **Hashtags** 3–5, specific and local: Instagram recommends few, and generic tags dilute locality.
- A real date or limit once, as fact; never as pressure (guardrails 1).

BE check on every piece with a CTA: guardrails five-line version. Fail one, fix before delivering.

## Micro-stories: every piece is an instance of the frame

The brand book's story framework is the only story; each piece of copy is a micro-story drawn from it (guardrails › Messages and micro-stories). Before drafting, name two things and keep them in the output line:

- **Anchor message.** One core message the piece reinforces (integrity rule: contradicts none). A piece that reinforces nothing is noise, however well written.
- **Story block.** The one block the piece plays, from the guest's side: existing world (a recognisable Tuesday), obstacle (the evening that stays ordinary), call to action (the moment that sparks the visit), meeting the guide (the persona or venue appears, calm, credible), the challenge (what the guest actually wants under the practical ask), transformation (the table at its best), new world (the guest's week with the place in it). The guest is the hero in every block; the persona is the guide, present but never the subject.

Touchpoint copy (greeting, host lines, menu talk, booking messages, departure and after-visit notes, DM replies) is written from that touchpoint's **micro-message block**: open with the block's "understanding to create", use its "verbal expression" register, and read the draft against its failure modes (rushed, ceremonial, lecturing, transactional). A micro-story is one moment, one block, one message: the arc belongs to the month, not to the post.

**Example (brewery, Instagram caption, anchor "beer and food, made together", block 4 meeting the guide; placeholders):** "The bread on your table is this morning's brew. Spent grain from the pale, baked at four. Ask for the pairing when you sit." (neutral; the guest's table is the scene, the making is the proof, the guide speaks once)

## Per channel

| Channel | Shape | Length | CTA |
| --- | --- | --- | --- |
| Instagram / Facebook caption | Place + moment in the first line, one idea, sign-off in persona | 1–3 short paragraphs | One, soft, or none |
| Story text | One line, present tense, now (read in under 5 s) | ≤ 12 words | Sticker or none |
| Reel / TikTok on-screen text | Word-for-word captions + emphasis cards within the cap `vios-video-script` sets | — | Last card only |
| Paid ad primary text | Offer and place in the first line, reason to come this week | 1–2 lines + optional 2nd paragraph | Exactly one |
| Comment / DM reply | Answer first, warmth second, persona phrase last | 1–3 sentences | Only if they asked |
| Review reply (positive) | Thank by the specific detail they named, no template | 2–3 sentences | None |
| Review reply (negative) | Unless it touches an escalation topic (the list is guardrails 11: no draft, hand the facts to the approver). Otherwise one apology, one fact, one direct line. Never argue in public, never offer a discount in public (it teaches guests to complain for rewards), never ask for the review to be changed | 3–4 sentences | Invite to continue privately |
| Booking confirmation / reminder | Restate date, time, people (restating the plan is a commitment device; it cuts no-shows), one warm line, how to change. Formal register | 3 lines | Change/cancel link |
| Google Business post | What, when, why this week | ≤ 60 words | One |
| Review request (QR after the bill) | Per guardrails 2 | 1 line | Link |

Default response targets (override in `persona-bible.md`): comments same day; DMs within 2 h while open; reviews within 48 h. Slow replies read as not listening. If the venue can't staff this, say so in the output line rather than draft replies nobody will send.

## Replies: the Vios discipline

- Answer every review, good and bad. The remembering self is speaking.
- A "no" is a "no". Thank them and stop. No second pitch after a decline.
- Complaints: fix the issue, don't manage the emotion. One apology, what we're doing, a named person and a channel.
- Escalation topics (guardrails 11): hand to the approver with the facts; don't write the reply.
- Never invent a fact. Check the fact sheet or ask.

## Output

The copy, per language (two columns when side by side), marked DRAFT. Below it, one line: anchor message + story block (+ micro-message block for touchpoint copy) + tone used + register used + anything flagged. No preamble.

Before publish: `vios-consistency-qa` → named approver. This skill drafts; it never publishes.

End with one line: what is drafted and in Review, what is "to confirm" and who confirms it, and the next step (`vios-consistency-qa` before publish). Then stop.

**Example (bad → good, gelato shop, first strawberry batch, Instagram; facts and place are placeholders, never reuse):**

- Bad: "Our AMAZING strawberry gelato is BACK! 🍓🔥 Limited batch — get it before it's gone! Tag a friend who needs this!!!"
- Good: "Strawberry is on the counter in [Neighbourhood] from today. First of the season, from the Thursday market, churned by eleven." (neutral; informal register; a fact stated once; locality in the first line; anchor "made today, here"; block 3 call to action)