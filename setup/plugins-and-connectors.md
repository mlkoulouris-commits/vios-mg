# Plugins and connectors

What the department needs enabled in a Claude account, and why. Status column is the personal account on 2026-10-29.

## Plugins (Anthropic Directory)

| Plugin | Why | Status |
| --- | --- | --- |
| `vios-core` | guardrails, BE lens, non-verbal lens, filter test; every other Vios plugin loads it | **upload 0.2.0** |
| `vios-brand` | Stage 1: brand diagnosis, persona builder | **upload 0.1.0** |
| `vios-marketing` | operations: calendar, voice, video, QA, ads, audit, report | enabled 0.2.0; **upload 0.3.0** |
| `vios-journey` | Stages 2–4: journey map, journey design, training programme | **upload 0.1.0** |
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
