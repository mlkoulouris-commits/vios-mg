---
name: "vios-engagement-setup"
description: "Open the project workspace for a signed Vios engagement: the client folder from the template, the ClickUp engagement lists per stage from the setup file, the Drive folders for consents, stills and data, the intake record, the chase list and the first scheduled reviews. VIOS Practice section 5.3 move 4. Use when a proposal is signed, when a marketing client becomes a Practice client, or when a workspace needs to be rebuilt in another account."
---

# Vios Engagement Setup

Move 4 of the intake protocol, done once per engagement so every workspace has the same shape and any practitioner can move between them. Layer 3 of the practice: the engagement's record, separate from the method (Layer 1) and the patterns (Layer 2). Hard lines: `vios-core:vios-guardrails` 12 (consents, data and revenue never in git; one workspace per client; access per client).

## Read first

- `../../references/parts-4-5-examples-and-production.md` § 5.2 (Layer 3) and § 5.3 move 4.
- `vios-core:vios-guardrails` › client file convention (the folder), `templates/client/` (the files), `setup/clickup-engagement.json` (the lists and statuses per stage), `setup/plugins-and-connectors.md` (which connectors this account has).
- `[client]/README.md` › Intake record and the signed proposal: which stages are in scope decides which lists and folders are made.

## Steps

1. **Folder**: copy `templates/client/` to `[client]/`; fill `README.md` with the intake record; `accounts.md` with the ids known so far; `open-facts.md` with the intake's open rows. Stages out of scope keep their folders, empty, with a line saying why.
2. **ClickUp**: from `setup/clickup-engagement.json`, one list per in-scope stage under the client's folder (Stage 1 Brand · Stage 2 Map · Stage 3 Design · Stage 4 Training · Marketing, when in scope), statuses Draft → Review → Signed → Done, one task per deliverable with its approver and due date from the timeline, and one "Engagement — chase list" task mirroring `open-facts.md`. Use the bulk operation, one call per list.
3. **Drive**: the client's Drive folder with `consents/`, `character-sheet/`, `data/`, `deliverables/`, `briefs/`; link it from `accounts.md`. Nothing from these folders is committed.
4. **Reviews on the calendar**: each stage's sign-off meeting, the Stage 4 retrospective, the thirty-day review after go-live, the case-writing window; as calendar events with the approver invited, via the calendar connector when present.
5. **Scheduled tasks**: when the marketing loop is in scope, confirm the client is picked up by the five department tasks (they iterate `clients/*/accounts.md`); nothing new is scheduled per client.
6. **Hand the keys**: one line in `README.md` naming who in the practice owns the workspace (account manager), who approves (from the front page of the persona bible once it exists), and where the signed proposal lives.

## Output

The folder, the lists, the Drive links, the calendar events, and a one-line summary: client · stages · lists created · reviews booked · open facts count. Next step: the first in-scope stage's skill.

## Rebuilding elsewhere

The same steps run in another account from the repo alone: clone, `templates/client/`, `setup/clickup-engagement.json`, the connectors listed in `setup/plugins-and-connectors.md`. That is the migration path in `docs/migration.md`.
