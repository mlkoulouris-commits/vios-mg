# Plugins and connectors

What the department needs enabled in a Claude account, and why. Status column is the personal account on 2026-10-29.

## Plugins (Anthropic Directory)

| Plugin | Why | Status |
| --- | --- | --- |
| `vios-marketing` | the method: all 12 skills | enabled |
| `instagram` | comments + DMs through the official Graph API, tokens stay with us | **enable** |
| Windsor.ai Ads and Marketing Data | Meta + Google Ads data for `vios-ads-audit` and the monthly report | **enable** |

Evaluated and not adopted: Buzzfy (hosted middleman for client tokens), Posty / So-me Studio (duplicate Metricool), Social Media Skills and marketingskills (generic skills that conflict with the persona and guardrails; mine for ideas only), Postiz (AGPL self-hosted scheduler, 30 req/h API cap; only if Metricool is dropped).

## Connectors (/mcp)

| Connector | Used for | Status |
| --- | --- | --- |
| Metricool | scheduling, best time to post, analytics, inbox | connected; brand 7633845 has no network |
| ClickUp | tasks, approvals, statuses | connected; structure in `clickup.json` |
| Claude Docs | client deliverables (diagnosis, reports) | connected |
| Google Drive | consents, stills, raw data per client | connected |
| Gmail | escalations to the approver, client mail | connected |
| Google Calendar | review dates, client check-ins | connected |
| Canva | brand kits, stills | **authorise** |
| Adobe Express | stills, quick video resize | connected |
| ElevenLabs creative | persona video, voice, image edits (persona only, never food or room) | connected |
| HubSpot | not needed now | not authorised, leave |
| Memento (own app) | bookings by source, covers, marketing spine | live, read via the app UI |
