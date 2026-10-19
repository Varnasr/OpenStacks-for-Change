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
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
OUT = ROOT / "data" / "repos.json"
TILE = re.compile(r'<a class="tile[^"]*"[^>]*>.*?</a>', re.S)
REPO = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# Repositories on the index that a repository-scoped token cannot read, with
# the reason. The weekly workflow passes secrets.GITHUB_TOKEN, which is scoped
# to this repository, so GET /repos on a private one elsewhere answers 404 and
# cannot be told apart from a repository that does not exist. That is why these
# are named rather than inferred: a 404 for anything not in here is still a
# failure, so a typo or a deleted repository is reported as loudly as before.
#
# This is why the workflow failed every Monday from 28 September 2026: the run
# of 22 September had been made by hand with a personal token, so the committed
# file held all 22 rows, and every scheduled run since 404'd on this one and
# exited 1. The file went 27 days without a refresh.
PRIVATE = {
    "Varnasr/whogavetheorder": "private; a repository-scoped token 404s on it",
}


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
    # Start from what is already there, so a repository this token cannot read
    # keeps the figures a previous run got for it instead of disappearing from
    # the file. Rebuilding from nothing is what made a partial run destructive.
    try:
        before = json.loads(OUT.read_text(encoding="utf-8")).get("repos") or {}
    except (OSError, ValueError):
        before = {}
    out = {"fetched": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
           "repos": dict(before)}
    failed, kept = [], []
    for full in repos_on_page():
        try:
            out["repos"][full] = fetch(full, token)
        except urllib.error.HTTPError as e:
            if e.code == 404 and full in PRIVATE:
                kept.append(f"{full} ({PRIVATE[full]})")
            else:
                failed.append(f"{full}: {e}")
        except Exception as e:  # noqa: BLE001
            failed.append(f"{full}: {e}")
    # A repository nothing on the page mentions any more should not linger.
    for gone in [k for k in out["repos"] if k not in repos_on_page()]:
        del out["repos"][gone]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out['repos'])} repositories")
    for k in kept:
        print(f"kept the previous row for {k}")
    for f in failed:
        print("failed:", f, file=sys.stderr)
    # Any failure is a failure. This used to be `failed and not out["repos"]`,
    # so the run only failed when *every* repository failed, and one that
    # failed on its own wrote a file missing that row and exited 0. That is how
    # Varnasr/whogavetheorder came to be absent from a committed data/repos.json
    # while its tile sat on the page: a partial write nothing reported.
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
