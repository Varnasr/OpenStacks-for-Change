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
