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
that file at load to put a last-push month and a star count on each tile. It
passes `secrets.GITHUB_TOKEN`, which is scoped to this repository. One of the 22
repositories the index named then, `Varnasr/whogavetheorder`, was private, and
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

On 21 November 2026 the GitHub API reported `Varnasr/whogavetheorder` public
(`private: false`), so it was taken out of `PRIVATE`, which is now empty. The
behaviour stays: a 404 on a repository listed there keeps its previous row, and
a 404 on anything else fails the run. If a tile ever names a private repository
again, list it there with the reason.

Both branches were tested against a real `HTTPError 404`, because they cannot be
reached by removing the token in the agent sandbox: the proxy there injects
GitHub credentials, so no request to `api.github.com` is ever unauthenticated
and a private repository answers 200. An unlisted repository gets 403 from that
proxy rather than 404 from GitHub, which is the sandbox and not the case this
guards.

## The counts on the tiles had drifted, and nothing compared them (21 November 2026)

A tile repeats numbers that live in other repositories: maps, case studies,
generators, terms. On 21 November 2026 an audit read each number against the
repository's own data on its default branch and found the page behind on most
of them. Two had been corrected in `README.md` and `docs/STACK_GUIDE.md` on
6 November (#70) and left as they were on `index.html`, so the page and its own
README disagreed for two weeks. `scripts/check.py` passed throughout, because
it compared tiles with `data/repos.json` and read no description.

What was corrected, each from the file named in `data/claims.json`:

- How India Lives 205 maps to 259, and its 106 interactive indicators added.
- Industry Conglomerates Tracker 444 projects to 386, and 1999 to 1998 for the
  first year, both from the CSV.
- Dev Case Studies 200 to 208. Development Discourses "500+" to 687, with its
  address changed to devdiscourses.impactmojo.in.
- DevData Practice 10 generators and 350k+ rows to 36 and 840,000+.
- ImpactLex "390+ terms" to 494. "Merged from 20 course lexicons" was removed
  because no file confirms it: the snapshot lists 10 course slugs.
- "Bihar Electoral Dashboard" at forindia.netlify.app became Off the Roll at
  offtheroll.in, with its public repository `Varnasr/INDIA-DATA`, so the tile
  now gets a last-push month.
- WhoGaveTheOrder no longer claims a chain-of-command map, a page removed on
  23 September 2026. CandidateDossier no longer claims LaTeX or Netlify
  Functions: the PDF comes from the browser's print dialogue.
- Five tiles with a working site gained `data-live` and the site's address:
  Bihar Parichay, Dev Case Studies, DevData Practice, The Measurement Trap and
  CandidateDossier. The hero's count of live sites went from 18 to 23.
- In `docs/`: "five toolkits" to four, FieldStack taken off the Stata row, and
  the sentence saying the toolkits had gone untouched for a year removed.

`data/claims.json` now holds every count a tile states, with the file it was
read from and the day. `scripts/check.py` fails if a tile states a count with
no entry, or if the tile, `README.md` or `docs/STACK_GUIDE.md` stops saying a
count that has one. Three faults were injected and each failed: a changed
figure on a tile, a new unsourced count on a tile, and an old figure put back
in the README. **The check cannot see the other repositories**, so it does not
know when a count there moves. To change a count, read it from that
repository's data, change `data/claims.json` first, then the text.

Left for the owner, and not changed: whether to add tiles for public
repositories that have none (WomenOnRecord, Chromalie) or for JanVayu and
Impact Mojo; PolicyStack, which is listed as retired and archived and is not
archived on GitHub; the label count (four on the page, three in `README.md`
and `MAINTENANCE.md`); `MAINTENANCE.md` saying a Stable repository has no CI
beyond a link check while all four stacks run tests; `CITATION.cff`; and the
fact that Netlify publishes the repository root, so `/CLAUDE.md` and
`/scripts/check.py` answer 200.

## Robots and sitemap

`robots.txt` and `sitemap.xml` are kept by hand at the root. The sitemap lists only pages that can be indexed, in the address the live site answers 200 for (`/` for the home page, no `.html` for the others), so `support.html`, which is `noindex`, stays out. A new indexable page needs a sitemap entry and its own `<link rel="canonical">`; `scripts/check.py` fails on a missing entry, an address with no file, or a missing canonical.
