# OpenStacks-for-Change

Shared engineering standard: @.claude/engineering-standards.md. It applies to all work in this repository. This file adds what is specific to the project, and wins where the two disagree.

The index of the OpenStacks family (openstacks.dev): InsightStack, FieldStack
and EquityStack, with SignalStack beside them. PolicyStack is superseded by
PolicyDhara; RootStack, BridgeStack and ViewStack are archived.
`MAINTENANCE.md` is the family's maintenance policy, and `docs/` holds the
architecture, data standards and stack guide.

## Commands

```bash
python3 scripts/check.py      # run by CI
```

`repo-stats.yml` runs weekly and pushes a commit. The link check runs twice a
year in its own workflow.

## The weekly stats run failed every Monday for a month, and the page went stale

`repo-stats.yml` refreshes `data/repos.json` and commits it, and the index reads
that file at load to put a last-commit month and a star count on each tile. It
passes `secrets.GITHUB_TOKEN`, which is scoped to this repository. One of the 22
repositories the index names, `Varnasr/whogavetheorder`, is private, and
`GET /repos` on a private repository elsewhere answers **404** to a scoped
token, deliberately, so that a token cannot be used to discover that a private
repository exists.

`scripts/repo_stats.py` had been changed, correctly, to fail on any failure: it
used to exit 0 on a partial fetch and commit a file with that row missing, which
is how whogavetheorder once vanished from the data while its tile sat on the
page. Making it loud was right. Nothing then fixed the cause, so every scheduled
run from 28 September 2026 exited 1, the commit step never ran, and
`data/repos.json` kept the `fetched: 2026-09-22` it got from a run somebody made
by hand with a personal token. On 19 October all 22 rows were out of date.

Two changes. `PRIVATE` names the repositories a scoped token cannot read, with
the reason, so a 404 on one of those keeps the previous row and a 404 on
anything else still fails: a deleted or mistyped repository is reported as
loudly as before. And the script now starts from the file already on disk rather
than an empty dict, so a repository it cannot read keeps the figures a previous
run got for it instead of disappearing, while a repository no tile mentions any
more is still dropped.

Both branches were tested against a real `HTTPError 404`, because they cannot be
reached by removing the token in the agent sandbox: the proxy there injects
GitHub credentials, so no request to `api.github.com` is ever unauthenticated
and a private repository answers 200. An unlisted repository gets 403 from that
proxy rather than 404 from GitHub, which is the sandbox and not the case this
guards.
