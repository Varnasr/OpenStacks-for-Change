# Maintenance policy

How this family of repositories is kept alive, and — more importantly — how it is kept **cheap to keep alive**.

The guiding principle: *a repository should cost nothing to own when nobody is touching it.* Anything that generates recurring work without generating recurring value gets removed, not scheduled.

---

## Status labels

Every repository carries exactly one status. It belongs in the GitHub repo description and at the top of the README.

| Label | Commitment | What it means in practice |
|---|---|---|
| **Active** | Real | Under current development. Issues and PRs get a response within days. CI runs and is expected to pass. Dependencies are kept current. |
| **Stable** | Bounded | Works and is correct, but is not being developed. Bug reports welcome; feature requests likely declined. No CI beyond a link check. Dependencies are pinned and left alone. |
| **Retired** | None | Archived on GitHub, read-only. Kept public so links, citations, and forks keep working. Never deleted. |

There is no "early stage," no "coming soon," and no "planned." Those labels described intentions rather than states, and they aged badly — a repo marked early-stage in 2025 was still marked early-stage in 2026.

## The rules

**1. Never publish a roadmap for work that isn't underway.**
ClimateStack, EduStack, SocialStack, and InfraStack sat on a public roadmap for a year without a line of code. A roadmap entry is a promise to a reader; an idea is not. Ideas go in a private note, or in an issue labelled `idea` that nobody is waiting on.

**2. Retire coupled multi-repo systems first.**
The costliest thing here was never the research code — Stata and R scripts do not rot. It was RootStack → BridgeStack → ViewStack: three repos that only worked together, carrying Docker, FastAPI, npm lockfiles, Vite, and Dependabot between them. A three-repo system needs three times the upkeep and delivers value only when all three run. Retired.

**3. Prefer one self-contained repo over an ecosystem.**
The newer projects — How India Lives, Dev Case Studies, PolicyDhara — each live in a single repo with their own site and no shared dependencies. They have needed far less maintenance than the eight-stack family and reach readers more directly. When in doubt, build the standalone thing.

**4. CI must earn its place.**
A Stable repo needs at most a periodic link check. It does not need a changelog generator, a test matrix, or a lint job. Every workflow is something that can break and demand attention on a Tuesday evening. Delete the ones that aren't catching real problems.

**5. Community health files live in one place.**
[`Varnasr/.github`](https://github.com/Varnasr/.github) supplies CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, and issue templates to every repo automatically. Do not copy them into individual repos — that turns one edit into nine, and leaves broken relative links behind when files are removed.

**6. Links to money and identity get checked.**
Sponsor links, personal domains, and newsletter URLs break silently and embarrass loudly. They are the only external links worth checking on a schedule.

**7. Archiving is not deletion.**
Archived repos stay public, searchable, forkable, and citable. There is no reason to hesitate: retiring a repo costs the reader nothing and saves the maintainer everything.

## The routine

Twice a year is enough. Roughly thirty minutes.

- [ ] Check that every status label still tells the truth. Demote anything that hasn't been touched in a year from Active to Stable.
- [ ] Run a link check across READMEs and the landing page. Fix or remove dead links.
- [ ] Confirm the live sites still resolve: [openstacks.dev](https://openstacks.dev), [impactmojo.in](https://www.impactmojo.in), [janvayu.in](https://www.janvayu.in), [whatcounts.in](https://whatcounts.in/).
- [ ] Close issues nobody has engaged with in a year. An issue with no comments and no external interest is a note to self, not a task.
- [ ] Bump the `version` and `date-released` in each `CITATION.cff` that changed.
- [ ] Ask of every Active repo: *is this still true?* If not, demote it.

Nothing on this list needs doing between those two sittings. That is the point.

## What is deliberately not done

- **No dependency upgrade treadmill on Stable repos.** Pinned dependencies that worked in 2026 will still work. If a security advisory lands on something that processes untrusted input, act on it; otherwise leave it.
- **No response-time commitment on Stable repos.** Weeks, not days. Saying so up front is kinder than silence.
- **No cross-repo consistency projects.** Standardising directory layouts across nine repos was proposed twice and finished zero times. Consistency is worth having when it falls out of doing the work, not as the work.

---

*Last reviewed: August 2026.*
