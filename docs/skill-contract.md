# The skill contract

Every Vios skill that talks to the user follows this. It changes how a skill *talks*, never what the method *does*: the method sections of a skill stay as they are; the contract is a wrapper around them. Reference implementation: `plugin/vios-engage/skills/vios-proposal/SKILL.md`.

## 1. Steps, one screen, one question

- The skill declares its steps at the top (`## Steps`), 3–7 of them, in the order the method already works.
- Each step shows **at most ten plain lines** (a short table counts as its rows) and ends with **one question**. No open-fact numbers, no section references, no file paths in the screen; those go in the file.
- The user answers, or says "all good" (next step) or "all good to the end" (run the rest without stopping).
- **Nothing is written to disk before the user has seen the step that writes it**, except `status.json` and `open-facts.md` bookkeeping.

## 2. Ask only when necessary; never invent

- A fact the client folder does not hold is **not written as if known**. Three outcomes, in this order:
  1. The step cannot proceed without it and the user can answer now → **one question** to the user.
  2. The step can proceed with a gap → write **"to confirm"** in the deliverable, add a row to `clients/<slug>/open-facts.md` (fact · what it blocks · who holds it · asked on · due), and go on. A **blocker** in `status.json` only when the gap blocks the next action or the stage from closing: the card shows at most three, so a blocker is the thing the account manager must chase today, not every open row. A row the practice itself holds (price, access, a decision of the owner) goes to the Department list, not the client's Open facts (`clients.py facts` routes it).
  3. The method itself needs the founder's words (interview answers, signatures, decisions) → never drafted by the practice; a row in `open-facts.md` and the deliverable says *to confirm* with the question.
- A question is asked **once**. The skill never asks what `status.json`, `open-facts.md` or the client folder already answers.
- Dates, prices, names, numbers: only from the files or the user. A missing timeline is a question, not a guess (the proposal skill, step 3, is the pattern).

## 3. After every step

1. Write the deliverable file where the method says.
2. Update `clients/<slug>/status.json`: the deliverable's `status` (`not started` → `draft` → `review` → `approved` → `done`), `file`, blockers added or removed, `next_action`, `updated`. A deliverable is **approved**; a stage (`stages.<stage>.status`) is **signed** at its sign-off meeting (the schema's enums are the truth).
3. Move the ClickUp task (id at `stages.<stage>.deliverables.<name>.clickup` in `status.json`; lists and field ids in `setup/clickup.json`): draft while writing, **review** when it waits for the approver, **approved** on sign-off, **done** when delivered. Tasks no stage owns live under `stages.Engagement.deliverables`, keyed **Intake · Proposal vN · Setup · Baseline · Harvest · Report YYYY-MM**. Until setup step 2 has made the client's lists, the intake and proposal tasks sit in "Department — Setup & SOP" (id in `setup/clickup.json`), the client named in the task; step 2 moves them to the client's Deliverables list.
4. At the step that finishes a client-facing deliverable: `python scripts/clients.py pdf <slug> <file.md> "<Client>-<Deliverable>-vN" "<Kind>"` → `clients/<slug>/deliverables/`; `<Kind>` is the cover label, the deliverable's house name (Proposal · Baseline · Diagnosis · Brand book · Journey map · Design · Training plan · Report · Case, or the deliverable's own name), and every skill passes it, since the cover otherwise reads "Deliverable", and send the PDF to the user. The user forwards it; the practice never emails a client.
5. **Pulse line.** At a sign-off (the proposal's signature, each stage's close) the skill that takes it asks the approver for one sentence, what worked and what to change, and writes it dated to `clients/<slug>/README.md` › Sign-offs (create the heading when the README lacks it); the harvest reads those lines beside the KPIs. Never drafted for the approver; not given is "not given".

## 4. The end line

One line: what is now true · what is "to confirm" and who confirms it · the next step and its skill. Then stop. The front door (`vios-engage:vios`) reruns the card.

## 5. What the contract does not change

Hard lines, the method's moves, the deliverable structures, the house forms, the evidence tiers. A skill that needs a method change to fit the contract says so in its output line and leaves the method as is (`CLAUDE.md` › Rules: method changes only on the user's word).
