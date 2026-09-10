"""Write data/repos.json: stars, last push and open issues for every repository on the index.

    GITHUB_TOKEN=... python scripts/repo_stats.py

Reads index.html, finds every github.com/<owner>/<repo> a tile mentions,
asks the GitHub API for each, and writes the result. The page reads the
file at load and shows the last-push month on each tile, and the star count
where it is ten or more. A weekly workflow runs this and commits the file.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
OUT = ROOT / "data" / "repos.json"
TILE = re.compile(r'<a class="tile[^"]*"[^>]*>.*?</a>', re.S)
REPO = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def repos_on_page() -> list[str]:
    html = INDEX.read_text(encoding="utf-8")
    seen: list[str] = []
    for tile in TILE.findall(html):
        for full in REPO.findall(tile):
            full = full.rstrip(".")
            if full not in seen:
                seen.append(full)
    return seen


def fetch(full: str, token: str | None) -> dict:
    req = urllib.request.Request(f"https://api.github.com/repos/{full}",
                                 headers={"Accept": "application/vnd.github+json",
                                          "User-Agent": "openstacks-index"})
    if token:
        req.add_header("Authorization", f"token {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    return {"stars": d.get("stargazers_count", 0), "pushed_at": (d.get("pushed_at") or "")[:10],
            "open_issues": d.get("open_issues_count", 0), "archived": bool(d.get("archived")),
            "language": d.get("language") or ""}


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_PAT")
    out = {"fetched": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "repos": {}}
    failed = []
    for full in repos_on_page():
        try:
            out["repos"][full] = fetch(full, token)
        except Exception as e:  # noqa: BLE001
            failed.append(f"{full}: {e}")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out['repos'])} repositories")
    for f in failed:
        print("failed:", f, file=sys.stderr)
    return 1 if failed and not out["repos"] else 0


if __name__ == "__main__":
    sys.exit(main())
