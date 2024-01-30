Sometimes alembic revisions get into a borked state.  There should only ever be one record in the alembic_version table. If there isn't, remove more recent ones

The error looks vaguely like:

```
FAILED: Requested revision xxxx overlaps with other requested revisions yyyy
```

[Source](https://stackoverflow.com/a/57240912)

