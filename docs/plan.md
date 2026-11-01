# Department plan — social media management, fully digital

Bottom line: the Vios methodology already defines the pipeline. The department gives every stage
one system of record, one tool, and one named approver. The client folder is the single source of
truth; everything else reads from it or writes to it.

## Stage → skill → tool → approver

| # | Stage | Skill | Tool / system of record | Approver |
| --- | --- | --- | --- | --- |
| 1 | Intake and diagnosis | `vios-brand-diagnosis` | Claude Doc deliverable → `clients/<slug>/diagnosis.md` | Account manager |
| 2 | Persona | `vios-persona-builder` | `persona-bible.md`, `character-sheet/`, `consents/` (Drive) | Account manager + client owner |
| 3 | Facts and brand | guardrails convention | `fact-sheet.md`, `brand-book.md`, `accounts.md`, Canva brand kit | Account manager |
| 4 | Month plan | `vios-content-calendar` | Metricool planner + ClickUp list "Content" (one task per post) | Content lead |
| 5 | Copy | `vios-persona-voice` | ClickUp task description, status Draft → QA | Content lead |
| 6 | Video and visuals | `vios-video-script`, `vios-nonverbal-lens` | ElevenLabs flows (persona only), Canva / Adobe Express for stills | Content lead |
| 7 | QA gate | `vios-consistency-qa`, `vios-be-lens` | `qa-log.csv` row with `signed_off_at`; ClickUp status Approved | Named approver on Bible front page |
| 8 | Publish | hard line 10 | Metricool scheduling; ClickUp status Scheduled → Published | Approver clicks |
| 9 | Engagement | `vios-persona-voice`, hard line 11 | `instagram` plugin (comments + DMs), Metricool inbox; escalations by Gmail | Approver per reply batch |
| 10 | Paid | `vios-ad-factory`, `vios-ads-audit` | Meta Ads + Google Ads via Windsor.ai; `ads-plan.md` | Performance lead + client owner for spend |
| 11 | Measure | `vios-monthly-report` | Metricool analytics, Windsor.ai, Memento bookings/covers, GBP; `data/YYYY-MM/` | Performance lead |
| 12 | Automation | scheduled tasks | `setup/scheduled-tasks.md` (daily triage, weekly audit, monthly calendar and report, quarterly review) | Account manager owns the schedule |

## Roles (minimum three, one person can hold two)

- **Account manager**: owns the client folder, the approver role, consents, data-sharing decisions.
- **Content lead**: calendar, copy, video, QA gate.
- **Performance lead**: ads plan, weekly audit, monthly report numbers.

## Tool ecosystem

| Need | Tool | Status in personal account (2026-10-29) | Corporate account |
| --- | --- | --- | --- |
| Method | `vios-core` + `vios-brand` + `vios-marketing` plugins (`vios-journey` planned) | marketing 0.2.0 enabled; split into three in the repo 2026-11-01, packaged files in `plugin/`, to upload | enable all from the repo marketplace, core first |
| Documents for clients | Claude Docs | connected | connected by default |
| Client files | this repo + Google Drive | repo created; Drive connected | clone repo; connect Drive |
| Tasks and approvals | ClickUp | connected; structure created from `setup/clickup.json` | recreate from `setup/clickup.json` |
| Scheduling and analytics | Metricool | connected; brand 7633845 has no network linked yet | connect networks per brand |
| Engagement | `instagram` plugin | not enabled | enable |
| Ads data | Windsor.ai plugin | not enabled | enable |
| Visuals | Canva, Adobe Express | Canva needs OAuth; Express connected | authorise both |
| Persona video / voice | ElevenLabs creative flows | connected | connect |
| Email escalations | Gmail | connected | corporate mailbox |
| Venue data | Memento (bookings, covers, marketing spine) | live | same |
| Automation | Claude scheduled tasks | created from `setup/scheduled-tasks.md` | recreate |

## Build phases

1. **Week 1 (now)**: repo, template, Stochna folder, ClickUp space, scheduled tasks. Enable
   `instagram` and Windsor.ai plugins, authorise Canva, connect Stochna's networks in Metricool.
2. **Week 2**: one full cycle on Stochna: calendar → copy → QA → Metricool → engagement replies.
3. **Week 3**: scheduled tasks run unattended; add Atelier (Baci, Lab) as client two.
4. **Week 4**: SOP revised from the pilot log; migrate to the corporate account (`docs/migration.md`).

## Open decisions

- Engagement plugin: `instagram` (direct Graph API, tokens stay with you) chosen over Buzzfy (hosted).
- CRM: none for now; Memento's bookings and covers are the revenue link. HubSpot only if a client needs email campaigns.
- Consents and stills: Google Drive, never git.
