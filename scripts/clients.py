#!/usr/bin/env python3
"""Vios client status helper. Reads clients/<slug>/status.json and open-facts.md; never writes ClickUp itself.

  python scripts/clients.py status [slug]        the six-line status card (all clients if no slug)
  python scripts/clients.py check [slug]         validate status.json against setup/status.schema.json (light, no jsonschema dependency)
  python scripts/clients.py facts <slug>         ClickUp task.create_many body for the open rows of open-facts.md (paste into the connector)
  python scripts/clients.py new <slug> "<Name>"  create clients/<slug>/ from templates/client/ with status.json filled in
  python scripts/clients.py pdf <slug> <file.md> [Title] [Kind]   render a client deliverable, Vios-branded, to clients/<slug>/deliverables/<Title>.pdf (headless Edge; pip install markdown). Kind = cover label (Proposal, Brand Book, Report)

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


BRAND = REPO / "setup" / "brand"
PDF_CSS = """
@page { size: A4; margin: 14mm 18mm 12mm 18mm; }
@page :first { margin: 0; }
html { -webkit-print-color-adjust: exact; }
body { font-family: Roboto, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #333; margin: 0; }
.cover { position: relative; width: 210mm; height: 297mm; margin: 0; padding: 26mm 22mm; box-sizing: border-box; background: #503629; color: #fff; page-break-after: always; }
.cover img { width: 52mm; display: block; }
.cover .kind { margin-top: 48mm; font-size: 11pt; letter-spacing: 0.18em; text-transform: uppercase; color: #d9cbb8; font-weight: 400; }
.cover h1 { font-size: 30pt; font-weight: 300; line-height: 1.15; margin: 6mm 0 0; color: #fff; max-width: 140mm; }
.cover .sub { margin-top: 8mm; font-size: 12pt; font-weight: 300; color: #e8dfd3; max-width: 140mm; }
.cover .foot { position: absolute; left: 22mm; right: 22mm; bottom: 22mm; font-size: 9.5pt; color: #d9cbb8; border-top: 1px solid #7a6150; padding-top: 4mm; display: flex; justify-content: space-between; }
.page { width: 100%; border-collapse: collapse; margin: 0; } .page > thead > tr > td, .page > tfoot > tr > td, .page > tbody > tr > td { padding: 0; border: 0; background: none; }
.hdr { height: 8mm; margin-bottom: 8mm; border-bottom: 1px solid #e6ddd1; display: flex; justify-content: space-between; align-items: center; font-size: 8pt; color: #88704f; letter-spacing: 0.08em; text-transform: uppercase; }
.hdr img { height: 6.5mm; }
.ftr { margin-top: 6mm; font-size: 8pt; color: #88704f; border-top: 1px solid #e6ddd1; padding-top: 2mm; display: flex; justify-content: space-between; }
h1 { font-size: 20pt; font-weight: 300; color: #503629; margin: 0 0 6mm; }
h2 { font-size: 15pt; font-weight: 400; color: #503629; margin: 10mm 0 3mm; padding-bottom: 1.5mm; border-bottom: 1.5px solid #88704f; page-break-before: always; page-break-after: avoid; }
h2.first, .compact h2 { page-break-before: auto; } h2.first { margin-top: 0; }
h3 { font-size: 12pt; font-weight: 500; color: #503629; margin: 7mm 0 2mm; page-break-after: avoid; }
h4 { font-size: 10.5pt; font-weight: 700; color: #503629; margin: 5mm 0 1.5mm; }
p { margin: 0 0 2.6mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 5mm; font-size: 9.5pt; }
th { background: #503629; color: #fff; font-weight: 500; text-align: left; padding: 2.2mm 2.5mm; border: 0; }
td { padding: 2mm 2.5mm; border-bottom: 1px solid #e6ddd1; vertical-align: top; }
tr:nth-child(even) td { background: #f7f4ef; }
tr { page-break-inside: avoid; }
em { color: #6b5c4e; } strong { color: #503629; }
code { font-family: Consolas, monospace; font-size: 8.8pt; color: #503629; background: #f3efe9; padding: 0 1mm; }
blockquote { border-left: 3px solid #88704f; background: #f7f4ef; margin: 3mm 0; padding: 2.5mm 4mm; color: #4a4038; }
hr { border: 0; border-top: 1px solid #e6ddd1; margin: 6mm 0; }
ul, ol { margin: 0 0 3mm; padding-left: 5mm; } li { margin-bottom: 1mm; }
a { color: #88704f; text-decoration: none; }
"""

EDGE = [Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"), Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe")]


def _client_name(slug: str) -> str:
    try:
        return json.loads(read(CLIENTS / slug / "status.json"))["name"]
    except Exception:
        return slug


def pdf(slug: str, md_file: str, title: str | None = None, kind: str | None = None) -> Path:
    """Markdown -> branded HTML (Vios cover, running header/footer) -> PDF via headless Edge. The HTML is kept beside the PDF."""
    import html as htmlmod
    import subprocess
    try:
        import markdown
    except ImportError:
        sys.exit("pip install markdown")
    src = Path(md_file) if Path(md_file).is_absolute() else CLIENTS / slug / md_file
    out_dir = CLIENTS / slug / "deliverables"
    out_dir.mkdir(exist_ok=True)
    name = title or src.stem
    lines = read(src).splitlines()
    heading = next((l[2:].strip() for l in lines if l.startswith("# ")), name)
    # the H1 goes on the cover; a plain line right after it becomes the cover subtitle
    body_lines, sub, seen_h1 = [], "", False
    for l in lines:
        if not seen_h1 and l.startswith("# "):
            seen_h1 = True
            continue
        if seen_h1 and not sub and not body_lines:
            if not l.strip():
                continue
            if not l.startswith(("|", "#", "-", "*", ">", "<")):
                sub = l.strip()
                continue
        body_lines.append(l)
    body = markdown.markdown("\n".join(body_lines), extensions=["tables", "fenced_code"])
    body = body.replace("<h2>", '<h2 class="first">', 1)
    compact = len(" ".join(body_lines).split()) < 1500  # short documents flow; long ones get a page per section
    client = _client_name(slug)
    kind = kind or ("Proposal" if "proposal" in src.name.lower() else "Deliverable")
    logo_w = (BRAND / "vios-logo-inverted-crop.png").resolve().as_uri()
    logo_b = (BRAND / "vios-logo-crop.png").resolve().as_uri()
    today = date.today().strftime("%d %B %Y")
    esc = htmlmod.escape
    html = (
        "<!doctype html><html><head><meta charset='utf-8'><title>" + esc(heading) + "</title>"
        "<link rel='preconnect' href='https://fonts.googleapis.com'>"
        "<link href='https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap' rel='stylesheet'>"
        "<style>" + PDF_CSS + "</style></head><body>"
        "<div class='cover'><img src='" + logo_w + "' alt='Vios'>"
        "<div class='kind'>" + esc(kind) + " · " + esc(client) + "</div>"
        "<h1>" + esc(heading) + "</h1>"
        "<div class='sub'>" + esc(sub) + "</div>"
        "<div class='foot'><span>VIOS Practice · Meaningful Gastronomy</span><span>" + today + "</span></div></div>"
        "<table class='page'><thead><tr><td><div class='hdr'><img src='" + logo_b + "' alt=''><span>" + esc(client) + " · " + esc(heading)[:70] + "</span></div></td></tr></thead>"
        "<tfoot><tr><td><div class='ftr'><span>VIOS Meaningful Gastronomy · vios-mg.com</span><span>Prepared for " + esc(client) + " · " + today + " · confidential</span></div></td></tr></tfoot>"
        "<tbody><tr><td><div class='body" + (" compact" if compact else "") + "'>" + body + "</div></td></tr></tbody></table></body></html>"
    )
    html_path = out_dir / f"{name}.html"
    html_path.write_text(html, encoding="utf-8")
    edge = next((e for e in EDGE if e.exists()), None)
    if not edge:
        sys.exit(f"Edge not found; open {html_path} and print to PDF")
    pdf_path = out_dir / f"{name}.pdf"
    subprocess.run([str(edge), "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000", f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()], check=True, capture_output=True, timeout=180)
    print(pdf_path)
    return pdf_path


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
    elif cmd == "pdf":
        pdf(argv[2], argv[3], argv[4] if len(argv) > 4 else None, argv[5] if len(argv) > 5 else None)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
