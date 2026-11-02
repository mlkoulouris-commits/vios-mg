#!/usr/bin/env python3
"""Vios client status helper. Reads clients/<slug>/status.json and open-facts.md; never writes ClickUp itself.

  python scripts/clients.py status [slug]        the six-line status card (all clients if no slug)
  python scripts/clients.py check [slug]         validate status.json against setup/status.schema.json (light, no jsonschema dependency)
  python scripts/clients.py facts <slug>         ClickUp task.create_many body for the open rows of open-facts.md (paste into the connector)
  python scripts/clients.py new <slug> "<Name>"  create clients/<slug>/ from templates/client/ with status.json filled in

Skills call `status` at the start of a step and update status.json at the end; /vios <client> is the front door.
"""
import json, re, shutil, sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CLIENTS = REPO / "clients"
SCHEMA = REPO / "setup" / "status.schema.json"
TEMPLATE = REPO / "templates" / "client"
CLICKUP = REPO / "setup" / "clickup.json"


def read(p: Path) -> str:
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


def load_status(slug: str) -> dict:
    p = CLIENTS / slug / "status.json"
    if not p.exists():
        sys.exit(f"{slug}: no status.json (run: clients.py new {slug} \"<Name>\" or copy templates/client/status.json)")
    return json.loads(read(p))


def open_facts(slug: str) -> list[dict]:
    """Rows of open-facts.md whose last cell (answer / closed on) is empty."""
    p = CLIENTS / slug / "open-facts.md"
    if not p.exists():
        return []
    rows = []
    for line in read(p).splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 6:
            continue
        fact, blocks, holds, asked, due, answer = cells[:6]
        if answer:
            continue
        rows.append({"n": int(m.group(1)), "fact": fact, "blocks": blocks, "holds": holds, "asked": asked, "due": due})
    return rows


def card(slug: str) -> str:
    s = load_status(slug)
    facts = open_facts(slug)
    stages = " · ".join(
        f"{k.split(' ', 1)[-1]} {v['scope']}/{v['status']}" for k, v in s["stages"].items() if v["scope"] != "out"
    )
    blockers = s.get("blockers") or []
    lines = [
        f"**{s['name']}** — {s['current_stage']} · approver: {s['approver']} · updated {s['updated']}",
        f"Proposal: {s['proposal']['status']}" + (f" (v{s['proposal']['version']})" if s['proposal'].get('version') else "") + f" · marketing loop: {s['marketing_loop']}",
        f"Stages: {stages}",
        f"Blocked by: " + ("; ".join(f"{b['what']} ({b['holds']})" for b in blockers[:3]) if blockers else "nothing") + (f" +{len(blockers)-3} more" if len(blockers) > 3 else ""),
        f"Open facts: {len(facts)}" + (f", {sum(1 for f in facts if f['due'] and f['due'] <= date.today().isoformat())} overdue" if facts else ""),
        f"Next: {s['next_action']['what']}  →  {s['next_action']['skill']}",
    ]
    return "\n".join(lines)


def check(slug: str) -> list[str]:
    schema = json.loads(read(SCHEMA))
    s = load_status(slug)
    errs = [f"missing {k}" for k in schema["required"] if k not in s]
    enums = {
        "marketing_loop": schema["properties"]["marketing_loop"]["enum"],
        "current_stage": schema["properties"]["current_stage"]["enum"],
    }
    for k, allowed in enums.items():
        if s.get(k) not in allowed:
            errs.append(f"{k}={s.get(k)!r} not in {allowed}")
    st = schema["properties"]["stages"]["additionalProperties"]["properties"]
    for name, v in s.get("stages", {}).items():
        if v.get("scope") not in st["scope"]["enum"]:
            errs.append(f"stages.{name}.scope={v.get('scope')!r}")
        if v.get("status") not in st["status"]["enum"]:
            errs.append(f"stages.{name}.status={v.get('status')!r}")
        for d, dv in v.get("deliverables", {}).items():
            if dv.get("status") not in st["deliverables"]["additionalProperties"]["properties"]["status"]["enum"]:
                errs.append(f"stages.{name}.deliverables.{d}.status={dv.get('status')!r}")
    if s.get("proposal", {}).get("status") not in schema["properties"]["proposal"]["properties"]["status"]["enum"]:
        errs.append(f"proposal.status={s.get('proposal', {}).get('status')!r}")
    for b in s.get("blockers", []):
        if "what" not in b or "holds" not in b:
            errs.append(f"blocker without what/holds: {b}")
    if s.get("client") != slug:
        errs.append(f"client={s.get('client')!r} != folder {slug}")
    return errs


def facts_payload(slug: str) -> dict:
    """task.create_many body for the client's '<Client> — Open facts' list. Names: '#n [holder] fact', cut at 110 chars."""
    tasks = []
    for f in open_facts(slug):
        name = f"#{f['n']} [{f['holds']}] {f['fact']}"
        if len(name) > 110:
            name = name[:107].rstrip() + "…"
        t = {"name": name, "status_label": "draft", "description": f"Blocks: {f['blocks']}\nHolds: {f['holds']}\nRow {f['n']} of clients/{slug}/open-facts.md"}
        if re.match(r"^\d{4}-\d{2}-\d{2}$", f["due"]):
            t["due_date"] = f["due"] + "T00:00:00Z"
            t["due_date_time"] = False
        tasks.append(t)
    return {"tasks": tasks}


def new_client(slug: str, name: str) -> None:
    dest = CLIENTS / slug
    if dest.exists():
        sys.exit(f"{dest} exists")
    shutil.copytree(TEMPLATE, dest)
    p = dest / "status.json"
    s = json.loads(read(p))
    s.update({"client": slug, "name": name, "updated": date.today().isoformat()})
    p.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"created {dest}")


def slugs() -> list[str]:
    return sorted(d.name for d in CLIENTS.iterdir() if (d / "status.json").exists())


def main(argv: list[str]) -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1251
    cmd = argv[1] if len(argv) > 1 else "status"
    if cmd == "status":
        for slug in ([argv[2]] if len(argv) > 2 else slugs()):
            print(card(slug)); print()
    elif cmd == "check":
        bad = 0
        for slug in ([argv[2]] if len(argv) > 2 else slugs()):
            errs = check(slug)
            print(f"{slug}: " + ("ok" if not errs else "; ".join(errs)))
            bad += bool(errs)
        sys.exit(1 if bad else 0)
    elif cmd == "facts":
        print(json.dumps(facts_payload(argv[2]), ensure_ascii=False))
    elif cmd == "new":
        new_client(argv[2], argv[3])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
