---
tags:
  - posts
date: 2024-11-13
---


Grep can be used as a timer, and can be blocking.

This will block until the logs print accept connections twice, or 500 seconds elapses, with an return code to match. Good for blocking a CD pipeline until a certain log has been output.

```
( docker compose logs postgres -f & ) | timeout 500 grep -m2 "accept connections"
```

I came across this when using initdb.d with [[Docker]] and [[Postgres]]. initdb.d will run init scripts when the Postgres container is started, but these are internal to the container, so do not block `docker start` or `docker compose up`.  Despite this, Postgres cannot be connected to until the init scripts have completed. A quirk of the way the Postgres process in the container runs is that it starts up, loads the script, then restarts. This prints "postgres is ready to accept connections" twice, but only the second time indicates that Postgres is actually ready. This little grep timer was a simple way to block the CD pipeline.

I adapted it from [this](https://github.com/docker-library/postgres/issues/146#issuecomment-482393929).