---
title: Unity Catalog Essentials
aliases: [Unity Catalog Basics]
tags: [databricks, unity-catalog, governance, beginner]
difficulty: beginner
estimated_time: 30 minutes
updated: 2026-09-22
---

# Unity Catalog Essentials

## The namespace

The default governed table name has three parts:

```text
catalog.schema.object
main.training.orders
```

- **Catalog:** primary isolation and organization boundary.
- **Schema:** grouping inside a catalog.
- **Object:** table, view, volume, function, model, or another securable.

Unity Catalog also provides discovery, lineage, auditing, tags/classification, sharing, and governance for data and AI assets.

## Minimum access chain

To query a table, a principal generally needs permission to use the containing catalog and schema plus permission on the object:

```sql
GRANT USE CATALOG ON CATALOG main TO `data_analysts`;
GRANT USE SCHEMA ON SCHEMA main.training TO `data_analysts`;
GRANT SELECT ON TABLE main.training.orders TO `data_analysts`;
```

Names and privilege options vary by object. Test with a non-admin identity.

## Production rules

- Assign privileges and ownership to account-level groups, not individuals.
- Grant the least privilege needed for a role.
- Prefer managed tables and volumes for governed lifecycle.
- Use volumes for non-tabular files that still need governance.
- Add descriptions and tags so discovery is part of delivery.
- Keep raw cloud credentials away from users and notebooks.
- Use workspace bindings or stronger isolation only when the requirement justifies it.

## Object choice

| Need | Object |
|---|---|
| Structured queryable data | Table or view |
| Governed non-tabular files | Volume |
| Reusable governed logic | Function |
| Governed ML model | Registered model |
| External system federation | Connection / foreign catalog where supported |

## Checkpoint

Why can `SELECT` alone be insufficient? A user also needs visibility/use privileges through the catalog and schema hierarchy.

Next: [[07 - Jobs, Pipelines, and Operations]]. For depth: [[Unity Catalog Governance]].
