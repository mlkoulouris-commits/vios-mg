#!/usr/bin/env python3
"""Vios plugin release helper. Run from anywhere; paths are resolved from this file.

  python scripts/release.py package <plugin> <version>   bump plugin.json + marketplace.json, rebuild <plugin>-<version>.plugin
  python scripts/release.py sync [plugin ...]            copy repo SKILL.md files into the installed Claude plugin cache (all three if none named)
  python scripts/release.py tasks                        copy setup/prompts/*.md over the live scheduled-task prompts
  python scripts/release.py status                       show repo version, packaged file and cache version per plugin

"package" is the proper route (then upload the .plugin file in Settings > Plugins and commit).
"sync" is the quick route: live at the next session, overwritten by the next upload, so edit the repo first.
"""
import json, os, re, shutil, sys, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN_DIR = REPO / "plugin"
MARKET = REPO / ".claude-plugin" / "marketplace.json"
PLUGINS = ["vios-core", "vios-brand", "vios-journey", "vios-marketing"]
HOME = Path.home()
CACHE_ROOT = Path(os.environ.get("APPDATA", HOME / "AppData" / "Roaming")) / "Claude" / "rpm"
TASK_ROOT = HOME / ".claude" / "scheduled-tasks"
PROMPTS = REPO / "setup" / "prompts"


def read_text(p: Path) -> str:
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


def write_like(p: Path, text: str) -> None:
    """Write text keeping the file's existing line endings (CRLF if it had them)."""
    crlf = p.exists() and b"\r\n" in p.read_bytes()
    p.write_bytes((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))


def plugin_json(name: str) -> Path:
    return PLUGIN_DIR / name / ".claude-plugin" / "plugin.json"


def repo_version(name: str) -> str:
    return json.loads(read_text(plugin_json(name)))["version"]


def find_cache(name: str):
    """The installed copy: the rpm folder whose plugin.json carries this name. Newest wins."""
    hits = []
    if not CACHE_ROOT.exists():
        return None
    for pj in CACHE_ROOT.glob("*/*/plugin_*/.claude-plugin/plugin.json"):
        try:
            if json.loads(read_text(pj)).get("name") == name:
                hits.append(pj.parent.parent)
        except Exception:
            pass
    return max(hits, key=lambda d: d.stat().st_mtime) if hits else None


def cmd_status(_args):
    for name in PLUGINS:
        pkg = sorted(PLUGIN_DIR.glob(f"{name}-*.plugin"))
        cache = find_cache(name)
        cv = json.loads(read_text(cache / ".claude-plugin" / "plugin.json"))["version"] if cache else "not installed"
        print(f"{name:16} repo {repo_version(name):7} packaged {', '.join(p.name for p in pkg) or '-':32} cache {cv}  {cache or ''}")


def cmd_package(args):
    if len(args) != 2:
        sys.exit("usage: release.py package <plugin> <version>")
    name, version = args
    if name not in PLUGINS:
        sys.exit(f"unknown plugin {name}; one of {PLUGINS}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        sys.exit("version must be x.y.z")
    pj = plugin_json(name)
    s = read_text(pj)
    s2 = re.sub(r'"version":\s*"[^"]+"', f'"version": "{version}"', s, count=1)
    write_like(pj, s2)
    m = read_text(MARKET)
    pat = re.compile(r'("name":\s*"%s".*?"version":\s*)"[^"]+"' % re.escape(name), re.S)
    m2, n = pat.subn(r'\1"%s"' % version, m, count=1)
    if n != 1:
        sys.exit(f"{name} not found in marketplace.json")
    write_like(MARKET, m2)
    for old in PLUGIN_DIR.glob(f"{name}-*.plugin"):
        old.unlink()
    out = PLUGIN_DIR / f"{name}-{version}.plugin"
    src = PLUGIN_DIR / name
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob("*")):
            if p.is_file() and p.name != ".DS_Store":
                z.write(p, p.relative_to(src).as_posix())
    print(f"{name} -> {version}: plugin.json and marketplace.json bumped, {out.name} rebuilt "
          f"({len(zipfile.ZipFile(out).namelist())} files)")
    print("next: Settings > Plugins > upload", out, "then commit; or run `release.py sync", name, "` for a cache-only update")


def cmd_sync(args):
    names = args or PLUGINS
    for name in names:
        cache = find_cache(name)
        if not cache:
            print(f"{name}: not installed, upload the .plugin file first")
            continue
        n = 0
        for folder in ("skills", "references"):
            root = PLUGIN_DIR / name / folder
            if not root.exists():
                continue
            for src in root.rglob("*"):
                if src.is_file():
                    dst = cache / folder / src.relative_to(root)
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    if not dst.exists() or dst.read_bytes().replace(b"\r\n", b"\n") != src.read_bytes().replace(b"\r\n", b"\n"):
                        shutil.copyfile(src, dst)
                        n += 1
        print(f"{name}: {n} file(s) updated in {cache}")
    print("start a new session for the change to load; the next upload of that plugin replaces the cache")


def cmd_tasks(_args):
    for src in sorted(PROMPTS.glob("*.md")):
        dst = TASK_ROOT / src.stem / "SKILL.md"
        if not dst.parent.exists():
            print(f"{src.stem}: no scheduled task on this machine, skipped")
            continue
        if read_text(dst) == read_text(src):
            print(f"{src.stem}: unchanged")
        else:
            write_like(dst, read_text(src))
            print(f"{src.stem}: live prompt updated")


if __name__ == "__main__":
    cmds = {"status": cmd_status, "package": cmd_package, "sync": cmd_sync, "tasks": cmd_tasks}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        sys.exit(__doc__)
    cmds[sys.argv[1]](sys.argv[2:])
