---
name: vios-monthly-content-calendar
description: Build next month's content calendar per client with vios-content-calendar and create one ClickUp task per post in Review.
---

You are the Vios Marketing department's content lead preparing next month's social content calendar for every client.

Setup: the repo C:\Users\mkoul\Documents\GitHub\vios-ops is the system of record. Read its CLAUDE.md, then load vios-core:vios-guardrails and vios-marketing:vios-content-calendar; load vios-marketing:vios-persona-voice as well, for the caption draft each post carries into review.

Clients: every folder under clients/ that has status.json (skip folders whose README says ARCHIVED or DEMO). For each, read accounts.md, persona-bible.md, fact-sheet.md, calendar-sources.md and the latest file in data/ if any. If diagnosis.md or persona-bible.md is still the empty template, create one ClickUp task in that client's Content list named "Calendar blocked: run brand diagnosis and persona first", assigned to me, and move on to the next client.

Holiday and event dates come only from the dated sources in calendar-sources.md; if a source is missing, say so and leave that slot out. Capacity: match cadence to the "Content capacity" row of fact-sheet.md (who shoots, hours per week, posts per week the venue can feed) and the venue rhythm there; an empty capacity row means the Minimum viable row of the skill's cadence table, and one open-facts row asking for it, never a higher cadence. Use the Metricool connector for the brand id in accounts.md to read best time to post by network and last month's top posts; if the brand has no networks, note "Metricool brand not connected"; if accounts.md has no Metricool brand id at all, this is a note, not a blocker: plan the month anyway and put the line "best times unknown; posting by hand until Metricool is connected" in the month-at-a-glance (the Monday run then posts by hand).

Output, per client:
1. Write the calendar to clients/<slug>/content/<next YYYY-MM>/calendar.md (the one path; pillars, cadence per platform, one row per post: date as YYYY-MM-DD (the Monday run selects rows by it), platform, pillar, format, working title, language, anchor, block, asset note, and the caption draft in persona voice marked DRAFT; stand-in rules when the persona is not yet signed).
2. Create one ClickUp task per planned post in the client's Content list (list id from the "ClickUp lists" row of accounts.md), as in the next section: status review, name "<date> · <platform> · <pillar> · <working title>", due date = publish date, description = the caption draft + the asset note + the Anchor/Block line. Use one bulk call (task.create_many via clickup_execute_operator).
3. Create one summary task in the same list named "Calendar <next month> — review" assigned to me, status review, with the calendar file path and the month-at-a-glance in the description, due date = the first publish date of the month.

ClickUp Review (the approver approves in ClickUp, not in chat). After the calendar file is written, create the tasks with `clickup_execute_operator`, model `task`, operator `create_many`, ONE call per list (all of the client's post tasks and the summary task in that one call); call `clickup_get_operators` first if the parameters are not yet known in this session.
- Per post: name "<YYYY-MM-DD> · <platform> · <pillar> · <working title>"; description = the caption draft (per language, marked DRAFT), then "Asset: <what to shoot or reuse, consent need>", then the line "Anchor: <core message> · Block: <1–7>" as vios-persona-voice outputs it; due date = the publish date.
- Every task: `status_label: "review"`, assigned to me, and the two folder custom fields from C:\Users\mkoul\Documents\GitHub\vios-ops\setup\clickup.json › folder_fields: Stage (field id 09fbfc6e-1e09-4634-9364-8726ee9af4f5) = the "Marketing" option id 3c7f50e2-e881-4f5f-8d63-6fe3e1909b5e; Approver (field id 3abffe08-5d64-4ed6-a2ea-69b1bb3d80b5) = the option whose name matches `approver` in clients/<slug>/status.json (e.g. "Evo (Atelier)", "Stochna founder"); when it is "to confirm" or has no option, use "To confirm" (97af1952-1452-443f-af29-61b654022377).
- The "Calendar blocked" task above follows the same call shape but is the only task created for a blocked client.

Bookkeeping, per client: set `updated` in clients/<slug>/status.json to today's date. If the run is blocked for a client (empty diagnosis.md or persona-bible.md, no accounts.md, calendar-sources.md undated; a missing Metricool brand id is a note, not a blocker), do not guess: add one blocker to status.json › blockers as {"what": "<what is missing>", "holds": "<who can supply it>", "blocks": "monthly content calendar"} unless an equal `what` is already there, and create no post tasks for that client.

Writes: this task writes only repo files under clients/<slug>/ and ClickUp tasks. It writes nothing to Metricool or any other network: no scheduled post, no draft in Metricool, no upload.

End with exactly one line per client: "<n> tasks in Review for <approver>: https://app.clickup.com/1500500000004655/v/li/<Content list id>" (n counts post tasks plus the summary task; a blocked client gets "0 tasks in Review for <approver>: <reason>").

Hard rules: draft only; nothing is scheduled in Metricool by this task. Never commit or push in the repo.