---
name: vios-be-lens
description: Review any Vios Marketing post, video script, ad, booking flow or reply through the Vios behavioural economics library (Kahneman, Gladwell) before it ships. Use when asked to check, review or improve copy or a flow for persuasion, clarity or guest psychology, and as a pass inside the other Vios skills.
---

# Vios BE Lens

A review pass run on Vios Marketing output before it goes to QA. It applies the Vios behavioural economics library (grounded in Kahneman, *Thinking, Fast and Slow*, and Gladwell, *Blink*) to digital work: online content is the first touchpoints of the guest journey, so the same rules apply as in the venue. Hard lines: `vios-guardrails` 1–12.

Read first: `../../references/section-3-1-behavioural-economics.md`, the library verbatim (System 1 and System 2, the two selves, the principles with mechanism and failure mode per entry, the limits of asking customers). It overrides anything below; the checks here are the marketing-side application of it. Cite entries by their section-3.1 name when you flag something, so the fix traces to the library.

## Foundation: Two Selves

The experiencing self lives the moment; the remembering self decides whether to return and what to tell others. Marketing speaks to the remembering self. Every asset shows something worth remembering and promises only what the venue's journey really delivers.

## Checks (run all, in order)

1. **Thin-slice** — the first 1–2 s (video) or first glance (static, profile grid) reads as this brand. If not, rewrite the hook.
2. **Peak and end** — one clear peak; the last frame or line is deliberate and warm, not a fade or a hard sell.
3. **Cognitive ease** — one message per asset, simple visual, persona consistent with the Persona Bible.
4. **Proper choices** — one CTA per ad; booking and landing flows offer 2–3 clean paths, never a wall.
5. **Tone ladder** — label the copy neutral (asks), suggestive (proposes) or directive (recommends). For tests, one of each.
6. **Plain voice** — no hype, no performed enthusiasm, no flattery. Plain respects the guest as a decision-maker.
7. **Commitment** — booking confirmations restate the plan in persona voice; a reminder before the visit.
8. **Respect the no** — retargeting and reply rules per `vios-ads-audit` and `vios-persona-voice`; never chase, never a second pitch after a decline.
9. **System output** — does it give guests a moment they'd want to share themselves? Organic shares and tags are the success signal.
10. **Pressure** — guardrails 1: a true fact once is fine; pressure wording or invented scarcity fails.

## Accepted trade-off

Lower click-through from not using pressure is fine. Trust and return visits are the metric.

## Output

A short table: check → pass / fix → the fix in one line. Then the revised asset if fixes were needed. Brief and plain; the team reads this between shifts. Then hand to `vios-consistency-qa`.
