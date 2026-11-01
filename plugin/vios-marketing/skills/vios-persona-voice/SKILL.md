---
name: "vios-persona-voice"
description: "Write any client-facing text in a Vios Marketing client's Brand Persona voice — captions, stories, ad copy, comment and DM replies, review responses, booking messages, Google posts — in BG, GR or EN with the right address register, and flag off-brand lines. Use whenever copy for an F&B client is drafted, rewritten or checked, even if the user just says \"write a caption\" or \"answer this review\". Not for final pre-publish gating (vios-consistency-qa), ad test design (vios-ad-factory) or video scripts (vios-video-script, which calls this skill for the caption)."
---

# Vios Persona Voice

The Brand Persona is a character. This skill makes it speak the same way every time, on every channel, in every language, so guests recognise it before they read the logo. Hard lines: `vios-guardrails` 1–12.

## Load first (`vios-guardrails` › client file)

1. `persona-bible.md`: traits, never-trait, point of view, signature phrases, humour level, do/don't lines, behaviour matrix, address register, emoji policy, approver.
2. `fact-sheet.md`: hours, prices, dish names, claims we may make.
3. The channel, the moment (launch, slow Tuesday, event, complaint, holiday), the language(s).

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

## Per channel

| Channel | Shape | Length | CTA |
| --- | --- | --- | --- |
| Instagram / Facebook caption | Place + moment in the first line, one idea, sign-off in persona | 1–3 short paragraphs | One, soft, or none |
| Story text | One line, present tense, now (read in under 5 s) | ≤ 12 words | Sticker or none |
| Reel / TikTok on-screen text | Word-for-word captions + ≤ 3 emphasis cards (rule owned by `vios-video-script`) | — | Last card only |
| Paid ad primary text | Offer and place in the first line, reason to come this week | 1–2 lines + optional 2nd paragraph | Exactly one |
| Comment / DM reply | Answer first, warmth second, persona phrase last | 1–3 sentences | Only if they asked |
| Review reply (positive) | Thank by the specific detail they named, no template | 2–3 sentences | None |
| Review reply (negative) | Unless it touches illness, allergy, injury, a legal threat or a named staff member (guardrails 11: no draft, hand the facts to the approver). Otherwise one apology, one fact, one direct line. Never argue in public, never offer a discount in public (it teaches guests to complain for rewards), never ask for the review to be changed | 3–4 sentences | Invite to continue privately |
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

## Workflow

1. Confirm channel, moment, goal, language(s), register. Infer when obvious; ask only if a wrong guess would waste the client's time.
2. Draft in the persona. Mark the tone used.
3. Self-check against the Persona Bible: traits present, never-trait absent, signature phrase natural, one message, local detail, plain words, register right.
4. BE check on anything with a CTA.
5. Flag anything off-brand in the brief itself ("limited time only!!!") and offer the on-brand version.

## Output

The copy, per language (two columns when side by side), marked DRAFT. Below it, one line: tone used + register used + anything flagged. No preamble.

Before publish: `vios-consistency-qa` → named approver. This skill drafts; it never publishes.

**Example (bad → good, gelato shop, first strawberry batch, Instagram; facts and place are placeholders, never reuse):**

- Bad: "Our AMAZING strawberry gelato is BACK! 🍓🔥 Limited batch — get it before it's gone! Tag a friend who needs this!!!"
- Good: "Strawberry is on the counter in [Neighbourhood] from today. First of the season, from the Thursday market, churned by eleven." (neutral; informal register; a fact stated once; locality in the first line)