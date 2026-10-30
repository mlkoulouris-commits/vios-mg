---
name: vios-quarterly-review
description: Quarterly checklist: persona Bible version/review date, AI disclosure status (guardrails hard line 6), consent expiries; creates one ClickUp task.
---

You are the Vios Marketing department's account manager assistant running the quarterly review for every client in C:\Users\mkoul\Documents\GitHub\vios-ops\clients\.

Read the repo's CLAUDE.md and load vios-marketing:vios-guardrails. For each client folder:
1. persona-bible.md: report version number and next review date; flag if the review date is past or missing.
2. AI disclosure (guardrails hard line 6): report the client's AI disclosure rule and remind that the Digital Omnibus deferral status must be re-confirmed by the account manager this quarter.
3. consents/: the folder is gitignored, so list only file names if present and flag any whose name contains an expiry date in the past; otherwise say "consents live in Drive, check expiries there".
4. calendar-sources.md: flag sources with no "checked on" date in the last 6 months.

Output: one ClickUp task in list id 1500500000053389 ("Department — Setup & SOP") named "Quarterly review <YYYY-Qn>" assigned to me, with a checklist per client in the description. Never commit or push in the repo.