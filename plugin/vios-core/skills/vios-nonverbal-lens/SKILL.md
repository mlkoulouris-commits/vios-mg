---
name: vios-nonverbal-lens
description: Review a Vios Marketing persona video or avatar clip for facial expression, gaze, face-voice-word congruence, pacing and the closing frame before it ships. Use when asked to check a video, a talking-head clip, an avatar's performance, or whether a persona 'looks right'.
---

# Vios Non-verbal Lens

The Vios Non-verbal Communication library, moved from the venue floor to the camera. Run it on every persona video, avatar clip or talking-head ad, after the script passes `vios-be-lens` and before `vios-consistency-qa`. Hard lines: `vios-guardrails` 6 and 7.

Read first: `../../references/section-3-2-non-verbal-communication.md`, the library verbatim (thin-slicing and the threshold, the six categories: proxemics, paralanguage, kinesics, haptics, chronemics, environmental cues, each with mechanism and failure mode). It overrides anything below; the checks here are the camera-side application of it. Then load the client's Persona Bible, especially the Expression palette, and the character sheet. On the floor the same library is applied by `vios-journey:vios-journey-design` and `vios-journey:vios-training-programme`.

## Why the face matters

Viewers read emotion from the face in a fraction of a second, before the words (thin-slicing; Gladwell's *Blink*, drawing on Ekman's facial-expression research). If the face is wrong, the script doesn't matter.

## Evidence

This check needs stills or the cut. Script only → "unverified on final cut", never pass.

## Checks (run all; for video, note timestamps)

1. **Genuine smile** — reaches the eyes (cheeks lift, eye corners crease). Mouth-only smile = fail.
2. **Congruence** — face, voice tone and words say the same thing on every line. Flag any mismatch.
3. **Palette match** — each moment uses the emotion and intensity from the Expression palette. Flag improvised expressions.
4. **Gaze** — direct to lens on invitation and CTA moments; natural look-away when thinking or showing food. No unbroken stare.
5. **Pacing** — the expression lands a beat before the words. Natural blinks and breaths. No rushed delivery.
6. **Resting face** — relaxed and open between lines. No frozen grin, no blank mask.
7. **Intensity vs moment** — energy matches the content (event night higher; story or complaint reply softer).
8. **Closing frame** — ends on a settled, warm expression, then cut (peak-end).
9. **Uncanny check** — stiff jaw, lip-sync drift, too-perfect symmetry, dead eyes. Fail rather than ship.
10. **Disclosure and consent** — AI label on from the first synthetic frame or voice (guardrails 6); consent on file for any real face or voice (guardrails 7).

## Output

A short table: check, pass / fix / unverified, timestamp, fix in one line (for AI clips: the prompt change, emotion + intensity per line). Then a verdict: ship to QA / regenerate / reshoot.
