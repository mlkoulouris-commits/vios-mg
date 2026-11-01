---
name: "vios-guardrails"
description: "The shared hard lines, definitions, numbers and client-file convention every Vios Marketing skill relies on. Load whenever any Vios skill runs, when a question comes up about what's allowed in a post, ad, review, persona or offer, or when setting up a new client file."
---

# Vios Guardrails

One place for the lines we don't cross and the numbers we share, so every skill says the same thing. Other Vios skills link here by hard-line number (e.g. "guardrails 6") and keep one sentence each instead of restating.

## Hard lines (any breach = BLOCK in `vios-consistency-qa`, except a true fact worded as pressure, which is FIX per QA row 10)

1. **No invented scarcity or pressure.** *True, plain, once = allowed; false, unverifiable or pressure = never.* "Menu runs 14–20 Nov" is a fact stated once. "Last chance", "hurry", timers, "only 2 left" that isn't counted, are pressure. A corrected line must not be a softer nudge either.
2. **No fake proof.** Reviews, testimonials and UGC are real, verbatim, with written permission; never composited or incentivised without saying so. Review requests: ask every guest, never reward, never gate on satisfaction. Gifted or paid partnerships labelled on every post.
3. **No fake price anchors.** Only the actual current price. For a reduction, the reference is the lowest price charged in the previous 30 days (EU price-indication rule, transposed in BG/GR; the law covers goods, Vios applies it to menu and set-menu prices too). No other "was" price.
4. **No dark patterns** in booking, sign-up or unsubscribe flows.
5. **Food truth.** Dish, portion, plating, the room and the exterior are shown as they are. AI may enhance a real photo; it never generates food, the room or the street.
6. **AI disclosure.** Any synthetic face or voice: on-screen label from the persona's first frame, platform AI label on where one exists. EU AI Act Art. 50 transparency duties apply from 2 Aug 2026; check the current status of the Digital Omnibus deferral for machine-readable marking before relying on any grace period (status to be confirmed by the account manager before release and re-checked quarterly; until confirmed, treat as "no grace period"). Block when a label that exists is missing. If the scheduling or upload route can't set the platform AI label, the post goes native or is verified after publish; QA logs "label ✓ confirmed live". Full disclosure set for any AI or AI-scaled persona: (a) a permanent bio line on every account the persona appears on ("X is our AI host; the food/drinks/room are real"); (b) on-screen label from the first frame + platform AI label; (c) caption hashtag on every persona post (#AIcreated / #AIсъздадено / Greek equivalent); (d) paid partnerships carry dual disclosure, paid label + AI label; (e) every agency, freelancer or voice-actor contract states the disclosure duty and who is liable if it is missed. An AI persona never speaks or signs in a real person's name. When an AI post is wrong: approver pulls it within 2 hours, a named person signs the correction, log it, fix the Bible or prompt; two serious errors in a month pause persona content.
7. **Likeness and voice consent.** Any real person's face or voice (owner, staff, guests, a persona modelled on someone): written, paid where relevant, time-limited consent on file before cloning, filming for ads, or generation. The consent states whether the persona/voice is retired or continues when they leave, and who decides. No minors in frame without a guardian's release.
8. **Alcohol.** Where the venue sells alcohol: 18+ targeting (21+ where platform policy requires), no link to driving, sport, performance or youth, no health claims, per Meta/Google alcohol policy and BG/GR advertising law.
9. **Claims and rights.** Allergen, "organic", "vegan", "gluten-free", "local", "homemade" verified against the fact sheet. Music: licensed or commercial-library only (business accounts lose personal-library audio; unlicensed tracks get muted or removed).
10. **Human sign-off.** Nothing publishes, spends or is sent to a client without a named approver. Skills draft; they never publish.
11. **Escalate, don't draft.** Replies touching illness, allergy or food safety, injury, legal threats, press, a named staff member, discrimination or harassment go to the approver with the facts. A fluent draft here can create liability or read as dismissive.
12. **Data.** Customer lists in ads only with a documented GDPR basis. Client revenue and cover data stays private; sharing is the account manager's decision.

## Behavioural economics, the five-line version

one message · one CTA or none · no pressure device · no persuasion after a "no" · plain words, no superlatives. The full library (Two Selves, peak-end, thin-slicing, cognitive ease, proper choices, tone ladder neutral/suggestive/directive, commitment devices, system output not guest tendency, accepted trade-offs) is in the VIOS Practice manuscript, held by the account manager; the five lines above are enough to run any skill.

## Shared numbers (owned here)

- **Reporting n**: show *n* beside every percentage. If either side is < 30, show raw numbers and say "too small to call". An owner will act on "doubled" when it's 3 vs 6.
- **Early reads**: ad-cell decisions (the `vios-ads-audit` winner rule) are early reads that decide whether to keep spending, which is reversible. Reports and client messages still use n ≥ 30 per side; an early read with n < 30 per side is shown as raw numbers, headed "early read, too small to call", never as a percentage lift.
- **Benchmarks**: the client's own history. Industry numbers only when sourced and dated. Never invented, including posting times.
- Minimum sample, learning phase, planned-test protection and fatigue thresholds: `vios-ads-audit`.

## Client file convention

Every client has a folder (`[client]/`) with:

| File | Holds |
| --- | --- |
| `diagnosis.md` | Output of `vios-brand-diagnosis`: purpose, audience persona, positioning, archetype, Brand Role |
| `persona-bible.md` | From `vios-persona-builder`; front page names the **approver**, the **address register** (BG ти/Вие, GR εσύ/εσείς, per channel; default informal on social, formal in booking messages), **emoji policy**, **alcohol: yes/no**, **AI disclosure rule**, **version number and next review date**; sections include is/is-not pairs, tone by guest mood, objective and KPIs, error protocol and pilot |
| `brand-book.md` | Colours, type, logo rules, image style (or a link to the design system) |
| `fact-sheet.md` | Hours, address, prices, menu names, allergens, claims we may make, booking channels, venue rhythm (open days, slow days, peak days, events) |
| `accounts.md` | Meta ad account / page / pixel ids, Google Ads customer id, Metricool brand id, POS and booking system |
| `ads-plan.md` | Monthly budget by cold/warm/guest, target cost per booking, offline attribution method, planned test dates, accepted Ad Strength notes (e.g. venue-name pin) |
| `character-sheet/` | Locked reference stills, expression palette stills, voice spec |
| `consents/` | Persona-source, staff, guest and minor-guardian releases; UGC permissions; each with date and expiry |
| `calendar-sources.md` | Where holiday / name-day / event dates come from (dated sources, never memory) |
| `qa-log.csv` | `date, client, asset, platform, language, attempt, verdict, failed_checks (joined with ;), approver, signed_off_by, signed_off_at` — scheduling and upload require `signed_off_at` filled |
| `data/YYYY-MM/` | Raw pulls with source and pulled-at in the filename |

Skills' "Load first" sections point here. If a file is missing, say so and use the stand-in below; don't improvise.

## Not installed or not on file? Stand-ins

| Missing | Stand-in |
| --- | --- |
| `vios-be-lens` | The five-line BE version above |
| `vios-nonverbal-lens` | Smile reaches the eyes · face matches the words · lens on invitations · resting face between lines · warm last frame |
| `vios-persona-builder` / Persona Bible | Fact-only copy (hours, address, thank-you) in plain neutral register, marked "DRAFT, no persona"; then run `vios-brand-diagnosis`; if `vios-persona-builder` is not installed, the account manager writes `persona-bible.md` by hand with the front-page fields listed above |
| Character sheet or consent | Filmed-only work, no persona, no AI shots; say so |
| `ads-plan.md` | Report actuals only, mark targets "not set", ask the account manager before proposing pauses |
| POS / covers data | Marketing-only report headed "Venue link not measurable this month"; priority #1 becomes getting POS or booking access |