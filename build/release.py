#!/usr/bin/env python3
"""Legt für jedes Tool, dessen Version (build/toolkit.json) noch kein Release hat, ein GitHub-Release an.

Usage:  python3 build/release.py            (nach Commit + Push; braucht die gh-CLI)
Tag: <tool-id>-v<version>, Anhang: die gebaute HTML-Datei, Text: der passende Abschnitt aus changelog/<tool-id>.md.
Ablauf für eine neue Version: Tool ändern -> Version in toolkit.json erhöhen -> Abschnitt "## <version> – …" im
Changelog ergänzen -> build.py + hub.py -> commit/push -> release.py. Ältere Releases bleiben unverändert erhalten.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "build" / "toolkit.json").read_text(encoding="utf-8"))


def notes(tool_id, version):
    md = (ROOT / "changelog" / f"{tool_id}.md").read_text(encoding="utf-8")
    m = re.search(rf"^## {re.escape(version)} .*?(?=^## |\Z)", md, flags=re.M | re.S)
    if not m:
        raise SystemExit(f"Kein Abschnitt '## {version}' in changelog/{tool_id}.md")
    return m.group(0).strip()


def exists(tag):
    return subprocess.run(["gh", "release", "view", tag], cwd=ROOT, capture_output=True).returncode == 0


def release(tag, title, body, files, target="main", latest=False):
    """files: Liste (Quelle, Name im Release)."""
    if exists(tag):
        print(f"= {tag} (vorhanden)")
        return
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for src, name in files:
            dst = Path(tmp) / name
            if isinstance(src, bytes):
                dst.write_bytes(src)
            else:
                shutil.copy(src, dst)
            paths.append(str(dst))
        sha = subprocess.run(["git", "rev-parse", target], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        subprocess.run(["gh", "release", "create", tag, *paths, "--target", sha, "--title", title,
                        "--notes", body, f"--latest={'true' if latest else 'false'}"], cwd=ROOT, check=True)
    print(f"+ {tag}")


def main():
    for t in CFG["tools"]:
        v = t["version"]
        files = [(ROOT / "tools" / f'{t["id"]}.html', f'{t["id"]}-v{v}.html')]
        if t.get("en_file"):
            files.append((ROOT / "tools" / t["en_file"], f'{Path(t["en_file"]).stem}-v{v}.html'))
        body = (notes(t["id"], v) + f'\n\n---\nLive: https://milad-karami.github.io/lean-ci-kaizen-tools/tools/{t["id"]}.html'
                f' · Vollständiges Änderungsprotokoll: [changelog/{t["id"]}.md](https://github.com/milad-karami/lean-ci-kaizen-tools/blob/main/changelog/{t["id"]}.md)')
        release(f'{t["id"]}-v{v}', f'{t["de"]} {v} – {t["version_name"]}', body, files)


if __name__ == "__main__" and "--check" in sys.argv:
    for t in CFG["tools"]:
        assert notes(t["id"], t["version"]).startswith(f'## {t["version"]} ')
    print("ok: alle Changelog-Abschnitte vorhanden")
elif __name__ == "__main__":
    main()
