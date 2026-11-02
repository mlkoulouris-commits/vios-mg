---
name: "vios-harvest"
description: "Close a Vios engagement with the harvest protocol: review the four stage harvests, consolidate library contributions and template refinements, recommend or decline a Part IV case, write the engagement retrospective, archive the workspace, and log the manuscript change-log entry with the version increment it justifies. VIOS Practice sections 5.4 to 5.5. Use at engagement close, after a dry run, or when the owner asks 'what did this engagement teach the practice'."
---

# Vios Harvest

The five moves at the close of an engagement, one to three days of practitioner time, that move what is universal from the project workspace (Layer 3) into the pattern library (Layer 2) and, when justified, into the manuscript (Layer 1). Without it each engagement is a fresh start. Hard lines: `vios-core:vios-guardrails` 12 (client material never travels; only the pattern does) and › Changing the method (doctrine changes on the owner's word, logged).

**Work in seven steps, in the method's order. Stop after each and ask one question.** Each step shows at most ten plain lines (a short table counts as its rows); no fact numbers, no section references, no file paths on screen. "All good" moves to the next step; "all good to the end" runs the rest without stopping. Nothing is written before the user has seen the step that writes it, except `status.json` and `open-facts.md` bookkeeping.

## Steps

1. **Stage-harvest review** (move 1): each candidate as a row, candidate · promoted · dropped, with the second engagement when promoted. Ask: *"Agree with each status?"*
2. **Library contributions** (move 2): the proposed sub-entries, one line each, under the principle they join. Ask: *"Keep, add or drop any?"*
3. **Template refinements** (move 3): held or made, with the engagements behind each. Ask: *"Make these and hold those?"*
4. **Case recommendation** (move 4): the KPI table as promised (proposal) and as it stands (baseline · target · latest · date, from `status.json` › `kpis`), then recommend or decline, the lesson, the window. A KPI table that is empty or has no `latest` is recorded as "no outcome evidence" and the case can only be recommended for a method lesson, never for a result. Ask: *"Recommend, or decline?"*
5. **Archive** (move 5): what becomes read-only, one line per group. Ask: *"Archive as listed?"*
6. **Retrospective**: what worked, what did not, what changes next time. Ask: *"Is this the practitioner's view as given?"*
7. **Version control**: the increment proposed and the change-log entry. Ask: *"Propose this increment to the owner?"*

## Ask only when necessary; never invent

- A missing stage harvest or retrospective is not reconstructed: the step records **"not held"**, a row in `[client]/open-facts.md` (fact · what it blocks · who holds it · asked on · due) and a blocker in `status.json`, and goes on with the harvests that exist.
- The second engagement that promotes a pattern, a refinement's second engagement, a case lesson, a version number: only from `docs/dry-run-*.md`, `docs/method.md`, `docs/cases.md`, the stage harvests or the user. None on file → the row stays *candidate* / *held* / *to confirm*; never promoted on a guess.
- The retrospective and the increment are the practitioner's and the owner's words: the practitioner's view is taken as given at step 6, the increment is proposed at step 7 and never made. A question is asked once; never ask what `status.json`, `open-facts.md` or the archive already answers.

## After every step

Write the step's table into `[client]/archive/harvest-engagement.md` (steps 1–5), `[client]/archive/retrospective.md` (step 6), `docs/cases.md` (step 4), `docs/changelog-proposals.md` (step 7). Then `status.json`: the harvest deliverable's `status` (draft → review → approved → done) and `file`, `current_stage` "closed" at step 5, blockers added or removed, `next_action`, `updated`. Then the ClickUp task "Harvest <Client>" in the client's Deliverables list (ids in `setup/clickup.json`): **draft** while writing, **review** at step 7 when it waits for the owner, **approved** on the owner's word, **done** when the increment is logged. No client PDF by default, the harvest is the practice's; when the user wants the retrospective to go to the founder, `python scripts/clients.py pdf <slug> archive/retrospective.md "<Client>-Retrospective-v1"` at step 6 and hand the PDF to the user.

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.4 (harvest protocol), § 5.5 (version control: major.minor, the three triggers, who may revise, the change log, the second-instance rule), § 4.3 (the criterion for a case).
- `[client]/archive/harvest-stage-*.md` (the four stage harvests), `retrospective.md` if Stage 4 wrote one, `docs/dry-run-*.md` harvest entries, and the manuscript's current version from `docs/method.md` (M1). `python scripts/clients.py status <slug>` for what is still open.

## The five moves

1. **Stage-harvest review.** Read the four stage harvests together. Consolidate: which candidate patterns recur across stages (a cross-stage discipline such as the locked greeting, which is a voice decision, then a moment, then a script), which template refinements hold in more than one stage, which library entries add up. Candidates used once stay candidates; a pattern used in two engagements is promoted. Say for each: candidate, promoted, or dropped, with the second engagement named when promoted.
2. **Library contribution review.** The engagement's BE and NV applications, written in the five-field form (definition, mechanism, hospitality application, worked illustration, failure mode) as sub-entries under existing principles. A wholly new principle needs two engagements.
3. **Template refinement review.** Refinements proposed by one engagement are held; by two or more, made. Each made refinement is logged: what changed, why, which engagements.
4. **Case recommendation.** Does the engagement teach the practice something specific (§ 4.3)? Recommend or decline now; write later, in the case window three to six months out. Add to the case-recommendation log in `docs/cases.md`: engagement, proposed lesson, window.
5. **Archive.** The workspace becomes read-only: worksheets, map and Reasoning Note, design document, training materials, briefs and revisions, intake record, harvest record, correspondence within the confidentiality terms. Nothing is deleted; nothing is reused except through Layer 2.

Then the **engagement-level retrospective**: what worked, what did not, what the practice does differently next time. Short, by the practitioner, the highest-altitude part of the harvest.

## Version control (§ 5.5)

Propose the manuscript increment the harvest justifies: minor for patterns, entries and refinements; a substantial minor for a retrospective learning; major only for structural change after accumulated pressure. Write the **change-log entry**: version, date, summary, the engagement(s) that informed it. The owner makes the increment; this skill proposes it and never edits the manuscript. A change log that grows fast means revisions come too easily; one that does not grow means the practice is not learning. Note which.

## Output

1. `[client]/archive/harvest-engagement.md`: the five moves, each with its table (candidate · status · evidence).
2. `[client]/archive/retrospective.md`.
3. `docs/cases.md` updated (recommend or decline, with the lesson and the window).
4. `docs/changelog-proposals.md`: the proposed version increment and change-log entry for the owner.
5. `[client]/status.json` closed, the ClickUp harvest task moved.
6. One line: patterns promoted / held / dropped, library entries, refinements made, case yes or no, version proposed, what is "to confirm" and who confirms it. Then stop; the front door reruns the card.

## Example (placeholders)

Engagement: a counter-format gelato shop. Promoted: none yet (first use of the small-format page; second engagement needed). Held: the counter collision pattern, the end on two pages. Library: one NV sub-entry under D.3 (the hand-over of a small object), one BE illustration under 7 (peak-end at a fifteen-second peak). Case: recommend, lesson "the signature can precede the peak", window April. Version proposed: 1.3 → 1.4, minor. Worked from a real harvest: `plugin/vios-core/references/worked-examples.md` › E3.
