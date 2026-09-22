# Contributing

Thanks for helping make Databricks learning faster and clearer.

## Good contributions

- Correct a stale product name or behavior and link the official source.
- Add one focused example with expected results and cleanup steps.
- Improve a confusing explanation without adding jargon.
- Add a production caveat that prevents a realistic failure.

## Note format

Learning notes must begin with YAML frontmatter:

```yaml
---
title: Clear note title
aliases: []
tags: [databricks, topic]
difficulty: beginner
estimated_time: 10 minutes
updated: YYYY-MM-DD
---
```

Use Obsidian wikilinks for vault notes and normal Markdown links for external sources. Keep filenames stable because wikilinks depend on them.

## Before opening a pull request

```powershell
py scripts/validate_vault.py
```

Do not include workspace URLs, tokens, account identifiers, proprietary data, screenshots containing identities, or text copied from vendor documentation.

By contributing, you confirm you have the right to submit the work under the repository's applicable license: CC BY 4.0 for educational content and Apache-2.0 for code/configuration.
