# Client folder template

Copy this folder to `clients/<slug>/`. Files follow the `vios-guardrails` client file convention.

- `consents/`, `data/` and media in `character-sheet/` are gitignored. Keep them in the client's Google Drive folder and link it from `accounts.md`.
- `data/YYYY-MM/` holds raw pulls named `<source>_<pulled-at>.csv`.
- `qa-log.csv`: one row per QA attempt. Scheduling requires `signed_off_at`.

- `content/YYYY-MM/` holds drafts and QA verdicts (tracked); `data/YYYY-MM/` holds raw pulls (gitignored).
