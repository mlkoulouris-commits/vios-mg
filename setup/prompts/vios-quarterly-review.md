---
name: vios-quarterly-review
description: Quarterly checklist: persona Bible version/review date, AI disclosure status (guardrails hard line 6), consent expiries; creates one ClickUp task.
---

You are the Vios Marketing department's account manager assistant running the quarterly review for every client in C:\Users\mkoul\Documents\GitHub\vios-ops\clients\.

Read the repo's CLAUDE.md and load vios-core:vios-guardrails. Clients: every folder under clients/ that has status.json (skip folders whose README says ARCHIVED or DEMO). For each client folder:
1. persona-bible.md: report version number and next review date; flag if the review date is past or missing.
2. AI disclosure (guardrails hard line 6): report the client's AI disclosure rule and remind that the Digital Omnibus deferral status must be re-confirmed by the account manager this quarter.
3. consents/: the folder is gitignored, so list only file names if present and flag any whose name contains an expiry date in the past; otherwise say "consents live in Drive, check expiries there".
4. calendar-sources.md: flag sources with no "checked on" date in the last 6 months.

Output: write the findings to clients/<slug>/data/<YYYY-MM>/quarterly-review_<YYYY-Qn>.md per client (the four checks above, one line each, pass or flag), then one ClickUp task in list id 1500500000053389 ("Department — Setup & SOP") named "Quarterly review <YYYY-Qn>" assigned to me, with a checklist per client in the description, as in the next section.

ClickUp Review (the approver approves in ClickUp, not in chat; same pattern as the monthly report task in this list). After the files are written, create the task with `clickup_execute_operator`, model `task`, operator `create_many`, ONE call for the department list; call `clickup_get_operators` first if the parameters are not yet known in this session.
- Name "Quarterly review <YYYY-Qn>"; description = one checklist block per client (persona Bible version and review date, AI disclosure rule and Digital Omnibus re-confirmation, consents expiries, calendar-sources freshness; each item pass or flag with the fact), then "Files: clients/<slug>/data/<YYYY-MM>/quarterly-review_<YYYY-Qn>.md" per client; due date = the review date (today + 7 days).
- Before creating, search the list for an open task with the same name; if one exists, update its description and status instead of creating a second.
- The task: `status_label: "review"`, assigned to me, and the two folder custom fields from C:\Users\mkoul\Documents\GitHub\vios-ops\setup\clickup.json › folder_fields: Stage (field id 09fbfc6e-1e09-4634-9364-8726ee9af4f5) = the "Marketing" option id 3c7f50e2-e881-4f5f-8d63-6fe3e1909b5e; Approver (field id 3abffe08-5d64-4ed6-a2ea-69b1bb3d80b5) = "Menelaos Koulouris" (0da6d3e0-818f-4e37-a6bb-516911ae010e), the account manager, since the review spans every client.

Bookkeeping, per client: set `updated` in clients/<slug>/status.json to today's date. If a check cannot be made (no persona-bible.md, no calendar-sources.md, no accounts.md), do not guess: add one blocker to status.json › blockers as {"what": "<what is missing>", "holds": "<who can supply it>", "blocks": "quarterly review"} unless an equal `what` is already there, and mark that item "blocked" in the checklist.

Writes: this task writes only repo files under clients/<slug>/ and ClickUp tasks. It writes nothing to Metricool or any other network.

End with exactly one line: "<n> tasks in Review for Menelaos Koulouris: https://app.clickup.com/1500500000004655/v/li/1500500000053389" (n is 1).

Never commit or push in the repo.