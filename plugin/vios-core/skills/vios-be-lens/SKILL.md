---
name: vios-be-lens
description: Review any Vios Marketing post, video script, ad, booking flow or reply through the Vios behavioural economics library (Kahneman, Gladwell) before it ships. Use when asked to check, review or improve copy or a flow for persuasion, clarity or guest psychology, and as a pass inside the other Vios skills.
---

# Vios BE Lens

A review pass run on Vios Marketing output before it goes to QA. It applies the Vios behavioural economics library (grounded in Kahneman, *Thinking, Fast and Slow*, and Gladwell, *Blink*) to digital work: online content is the first touchpoints of the guest journey, so the same rules apply as in the venue. Hard lines: `vios-guardrails` 1–12.

Read first: `../../references/section-3-1-behavioural-economics.md`, the library verbatim (System 1 and System 2, the two selves, the principles with mechanism and failure mode per entry, the limits of asking customers). It overrides anything below; the checks here are the marketing-side application of it. When you flag something, cite the library principle given in brackets after the check (its section 3.1 name, e.g. "7. Peak-end"), so the fix traces to the library. Checks marked *Vios device* are the practice's own application with no library entry of their own: cite the check name and the hard line instead.

## Foundation: Two Selves

The experiencing self lives the moment; the remembering self decides whether to return and what to tell others. Marketing speaks to the remembering self. Every asset shows something worth remembering and promises only what the venue's journey really delivers.

## Checks (run all, in order)

1. **Thin-slice** [17. Thin-slicing] — the first 1–2 s (video) or first glance (static, profile grid) reads as this brand. If not, rewrite the hook.
2. **Peak and end** [7. Peak-end and duration neglect; 3.1.4 the two selves] — one clear peak; the last frame or line is deliberate and warm, not a fade or a hard sell.
3. **Cognitive ease** [1. Cognitive ease] — one message per asset, simple visual, persona consistent with the Persona Bible.
4. **Proper choices** [8. Choice architecture; 14. Decision fatigue] — one CTA per ad; booking and landing flows offer 2–3 clean paths, never a wall.
5. **Tone ladder** [Vios device; 9. Framing] — label the copy neutral (asks), suggestive (proposes) or directive (recommends). For tests, one of each.
6. **Plain voice** [1. Cognitive ease; 5. Affect heuristic] — no hype, no performed enthusiasm, no flattery. Plain respects the guest as a decision-maker.
7. **Commitment** [Vios device; 6. Defaults for the restated plan; 16. Hyperbolic discounting for the reminder] — booking confirmations restate the plan in persona voice; a reminder before the visit.
8. **Respect the no** [Vios device; guardrails 1 and 4] — retargeting and reply rules per `vios-ads-audit` and `vios-persona-voice`; never chase, never a second pitch after a decline.
9. **System output** [11. Social proof; 3.1.6 the limits of asking customers] — does it give guests a moment they'd want to share themselves? Organic shares and tags are the success signal.
10. **Pressure** [12. Prospect theory, the loss aversion a pressure device exploits; guardrails 1] — a true fact once is fine; pressure wording or invented scarcity fails.

## Accepted trade-off

Lower click-through from not using pressure is fine. Trust and return visits are the metric.

## Output

A short table: check → pass / fix → the fix in one line. Then the revised asset if fixes were needed. Brief and plain; the team reads this between shifts. Then hand to `vios-consistency-qa`.
