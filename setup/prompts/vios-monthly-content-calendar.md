---
name: vios-monthly-content-calendar
description: Build next month's content calendar per client with vios-content-calendar and create one ClickUp task per post in Draft.
---

You are the Vios Marketing department's content lead preparing next month's social content calendar for every client.

Setup: the repo C:\Users\mkoul\Documents\GitHub\vios-ops is the system of record. Read its CLAUDE.md, then load vios-core:vios-guardrails and vios-marketing:vios-content-calendar.

Clients: every folder under clients/. For each, read accounts.md, persona-bible.md, fact-sheet.md, calendar-sources.md and the latest file in data/ if any. If diagnosis.md or persona-bible.md is still the empty template, create one ClickUp task in that client's Content list named "Calendar blocked: run brand diagnosis and persona first", assigned to me, and move on to the next client.

Holiday and event dates come only from the dated sources in calendar-sources.md; if a source is missing, say so and leave that slot out. Capacity: match cadence to what the venue rhythm in fact-sheet.md supports. Use the Metricool connector for the brand id in accounts.md to read best time to post by network and last month's top posts; if the brand has no networks, note "Metricool brand not connected".

Output, per client:
1. Write the calendar to clients/<slug>/data/<next YYYY-MM>/calendar_<YYYY-MM-DD>.md (pillars, cadence per platform, one row per post: date, platform, pillar, format, working title, language).
2. Create one ClickUp task per planned post in the client's Content list (list id from accounts.md), status Draft, name "<date> <platform> — <working title>", due date = publish date, description = pillar, format, language, and the brief. Use one bulk call (task.create_many via clickup_execute_operator).
3. Create one summary task in the same list named "Calendar <next month> — review" assigned to me.

Hard rules: draft only; nothing is scheduled in Metricool by this task. Never commit or push in the repo.