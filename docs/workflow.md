# Workflow — Vios social media management

```mermaid
flowchart TD
  A[1 Brand diagnosis<br/>vios-brand-diagnosis · Claude Doc] --> B[2 Persona Bible<br/>vios-persona-builder · ElevenLabs face + voice]
  B --> C[3 Monthly calendar<br/>vios-content-calendar · ClickUp task per post]
  C --> D[4 Draft copy and video<br/>vios-persona-voice · vios-video-script · real plates]
  D --> E{5 QA gate<br/>vios-consistency-qa · 22 checks · 12 hard lines}
  E -- FIX --> D
  E -- HOLD / BLOCK --> H[Approver clears or kills]
  E -- SHIP --> F[6 Human sign-off<br/>named approver · qa-log signed_off_at]
  H --> F
  F --> G[7 Schedule and publish<br/>Metricool 18:00 / 20:00 · AI clips native with label]
  G --> I[8 Engage daily<br/>triage task drafts · human sends · hard line 11 escalates]
  G --> J[9 Ads and report<br/>Monday audit · monthly report · n on every number]
  J -. priorities .-> C
  I -. guest moments .-> D
```

## Who does what

| Stage | Skill | Tool | Human |
| --- | --- | --- | --- |
| 1 Diagnosis | vios-brand-diagnosis | Claude Doc → `diagnosis.md` | account manager + owner signs |
| 2 Persona | vios-persona-builder | `persona-bible.md`, ElevenLabs flow + voice | account manager; owner informed |
| 3 Calendar | vios-content-calendar | ClickUp list per client, `content/YYYY-MM/calendar.md` | content lead |
| 4 Drafts | vios-persona-voice, vios-video-script | `content/YYYY-MM/*.md`, plates in `character-sheet/plates/` | content lead |
| 5 QA | vios-consistency-qa, vios-be-lens, vios-nonverbal-lens | `qa-log.csv` row | — |
| 6 Sign-off | — | `signed_off_at` filled, ClickUp → Approved | approver |
| 7 Publish | — | Metricool; AI clips posted natively with the platform label | approver clicks |
| 8 Engage | vios-persona-voice | daily triage task → ClickUp Engagement list | approver sends |
| 9 Ads + report | vios-ads-audit, vios-monthly-report | weekly task → Ads list; monthly task → Claude Doc | performance lead; owner for spend |

Rules that hold at every stage: skills draft, humans publish; facts from `fact-sheet.md` only; consents before faces; AI disclosed from frame one.
