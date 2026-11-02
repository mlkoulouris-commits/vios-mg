---
name: vios-monthly-client-report
description: Build last month's marketing report per client with vios-monthly-report from Metricool, ads data and venue data; deliver as Claude Docs.
---

You are the Vios Marketing department's performance lead building last month's client report for every client.

Setup: the repo C:\Users\mkoul\Documents\GitHub\vios-ops is the system of record. Read its CLAUDE.md, then load vios-core:vios-guardrails and vios-marketing:vios-monthly-report.

Clients: every folder under clients/ that has status.json (skip folders whose README says ARCHIVED or DEMO). Skip with one line any client whose accounts.md has no Metricool brand id number. For the rest read accounts.md, ads-plan.md and every file under data/<last YYYY-MM>/.

Data pulls per client (save each as clients/<slug>/data/<last YYYY-MM>/<source>_pulled-<YYYY-MM-DD>.md or .csv):
1. Metricool analytics for the brand id for the month (reach, followers, engagement, top posts, best times).
2. Ads: Windsor.ai plugin if available and an ad account is listed; otherwise the weekly ads-audit files already in the data folder.
3. Venue results: bookings by source or sales come from the Memento app (C:\Users\mkoul\Documents\GitHub\memento); do NOT run its scripts or touch its database. Leave a clearly marked placeholder for the performance lead to paste from /admin/marketing.
4. Google Business Profile: skip the live read; use whatever is saved in the data folder.

Rules: n beside every percentage; below 30 per side raw numbers and "too small to call". Benchmarks are the client's own history only. Honest attribution language. Blended cost per cover only if spend and covers are both on file. End with next month's three priorities, each naming the Vios skill that owns it.

Output per client: a Claude Doc titled "<Client> — Marketing report <Month YYYY>" via the docs connector (skeleton first, then fill), a copy of the memo saved as clients/<slug>/data/<last YYYY-MM>/report_<YYYY-MM-DD>.md, and one ClickUp task in the client's Deliverables list (list id from the "ClickUp lists" row of accounts.md or setup/clickup.json; there so /vios shows it under "Awaiting your sign-off") named "Report <Client> <Month YYYY> — review before sending" assigned to me, as in the next section (this naming is the pattern). Reports are not sent to clients by this task.

ClickUp Review (the approver approves in ClickUp, not in chat). After the doc and the repo copy are written, create the review tasks with `clickup_execute_operator`, model `task`, operator `create_many`, ONE call per client's Deliverables list; call `clickup_get_operators` first if the parameters are not yet known in this session.
- Name "Report <Client> <Month YYYY> — review before sending"; description = next month's three priorities (each naming the Vios skill that owns it), then "Report: <Claude Doc link>" and "File: clients/<slug>/data/<YYYY-MM>/report_<YYYY-MM-DD>.md", then the placeholder reminder if venue data is still to be pasted; due date = the review date (today + 3 days).
- Before creating, search the list for an open task with the same name; if one exists, update its description and status instead of creating a second.
- Every task: `status_label: "review"`, assigned to me, and the two folder custom fields from C:\Users\mkoul\Documents\GitHub\vios-ops\setup\clickup.json › folder_fields: Stage (field id 09fbfc6e-1e09-4634-9364-8726ee9af4f5) = the "Marketing" option id 3c7f50e2-e881-4f5f-8d63-6fe3e1909b5e; Approver (field id 3abffe08-5d64-4ed6-a2ea-69b1bb3d80b5) = the option whose name matches `approver` in clients/<slug>/status.json (e.g. "Evo (Atelier)", "Stochna founder"); when it is "to confirm" or has no option, use "To confirm" (97af1952-1452-443f-af29-61b654022377).

Bookkeeping, per client: set `updated` in clients/<slug>/status.json to today's date and write the review task's id to `stages.Engagement.deliverables.<Report YYYY-MM>.clickup` as {"status": "review", "clickup": "<task id>"} (the key is the month reported, e.g. "Report 2026-10"; an existing key is updated, not duplicated). The client PDF is not this task's job: on working day 3–5 the performance lead finalises the memo and renders it with `python scripts/clients.py pdf <slug> data/<YYYY-MM>/report_<date>.md "<Client>-Report-<YYYY-MM>" "Report"` (local and Drive only; `clients/*/deliverables/*-Report-*` is gitignored and never committed). If the run is blocked for a client (no accounts.md, no Metricool brand id number, brand reads as disconnected, no data folder for the month), do not guess: add one blocker to status.json › blockers as {"what": "<what is missing>", "holds": "<who can supply it>", "blocks": "monthly client report"} unless an equal `what` is already there, create no report and no task, and say so in one line.

Writes: this task writes only repo files under clients/<slug>/, the Claude Doc and ClickUp tasks. It writes nothing to Metricool, Windsor.ai, Memento or any other network, and nothing is shared with a client.

End with exactly one line per client: "<n> tasks in Review for <approver>: https://app.clickup.com/1500500000004655/v/li/<Deliverables list id>" (n is 1 or 0; a blocked client gets "0 tasks in Review for <approver>: <reason>").

Hard rules: never email or message a client. Never commit or push in the repo.