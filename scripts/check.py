#!/usr/bin/env python3
"""Checks for the family index.

    python3 scripts/check.py

No network. This page is the family's front door, so the failure that matters
is the index and the data behind it disagreeing about what exists.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
checks = 0


def check(name, ok, detail=''):
    global checks
    checks += 1
    if not ok:
        errors.append('%s: %s' % (name, detail))


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as fh:
        return fh.read()


def main():
    index = read('index.html')
    data = json.loads(read('data/repos.json'))

    check('data/repos.json carries a fetch date',
          re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(data.get('fetched', ''))),
          '%r' % data.get('fetched'))

    # repo_stats.py reads the repositories out of the tiles on this page, so
    # the two cannot disagree unless a fetch failed. One that failed on its own
    # used to write the file anyway and exit 0, which left a tile on the page
    # with no row behind it and nothing saying so.
    tiles = re.findall(r'<a class="tile[^"]*"[^>]*>.*?</a>', index, re.S)
    check('the page has tiles', tiles, 'none matched, so this check sees nothing')
    linked = []
    for tile in tiles:
        for full in re.findall(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', tile):
            full = full.rstrip('.')
            if full not in linked:
                linked.append(full)

    rows = data.get('repos', {})
    rowless = [r for r in linked if r not in rows]
    check('every repository linked from a tile has a row', not rowless,
          '%s: a fetch failed and the file was written anyway' % rowless)
    extra = sorted(r for r in rows if r not in linked)
    check('no row outlives its tile', not extra,
          '%s in data/repos.json and on no tile' % extra)

    for full, row in sorted(rows.items()):
        for field in ('stars', 'open_issues', 'archived', 'language', 'pushed_at'):
            check('%s carries %s' % (full, field), field in row, 'absent')
        check('%s pushed_at is a date' % full,
              re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(row.get('pushed_at', ''))),
              '%r' % row.get('pushed_at'))

    # A tile marked live points at a site. A tile whose status says archived
    # or retired should not claim to be active in the same markup.
    for tile in tiles:
        name = re.search(r'<h3>([^<]+)</h3>', tile)
        name = name.group(1) if name else '(unnamed tile)'
        status = re.search(r'data-s="([a-z]+)"', tile)
        check('%s declares a status' % name, status is not None, 'no data-s attribute')
        if status:
            check('%s status is one the page styles' % name,
                  status.group(1) in {'active', 'stable', 'retired', 'archived'},
                  '%r' % status.group(1))

    for page in ('index.html',):
        check('%s sets a viewport' % page,
              re.search(r'<meta[^>]*name=["\']?viewport', read(page), re.I) is not None,
              'a phone lays the page out at desktop width and zooms out')

    if errors:
        print('FAIL: %d of %d checks' % (len(errors), checks))
        for e in errors:
            print('  - %s' % e)
        return 1
    print('PASS: %d checks (%d tiles, %d repositories)' % (checks, len(tiles), len(rows)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
