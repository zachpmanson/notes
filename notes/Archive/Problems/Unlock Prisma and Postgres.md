---
tags:
  - prisma
---

Often after a prisma migration on a postgres instance, further migrations won't work citing some random error.  This can be fixed with this magic incantation into psql.

```sql
SELECT pg_terminate_backend(PSA.pid)
FROM pg_locks AS PL
    INNER JOIN pg_stat_activity AS PSA ON PSA.pid = PL.pid
WHERE PSA.state LIKE 'idle'
    AND PL.objid IN (72707369);
```

[Original source](https://stackoverflow.com/questions/76450818/supabase-prisma-migrate-dev-sometimes-times-out-postgres-advisory-lock/76467171#76467171)