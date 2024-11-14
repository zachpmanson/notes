[[Postgres]] in [[Docker]] is great. If you mount a folder to `/docker-entrypoint-initdb.d/` within the container, all `.sh` and `.sql` files will be [executed](https://github.com/docker-library/postgres/blob/master/docker-entrypoint.sh#L332). This is great! And it will only run if there is no existing database data volume, so its perfect for seeding databases.

A problem I ran into is that Postgres runs this during startup, which by default can't be detected by a CD pipeline, and the database cannot be connected until these scripts have completed. [Lots of people have had trouble with this.](https://github.com/docker-library/postgres/issues/146#issuecomment-341211148)

I used a [[Grep Timer]] to watch the logs for the 2 success messages and block the pipeline.

[Docker docs on this](https://docs.docker.com/guides/pre-seeding/#pre-seed-the-postgres-database-using-a-sql-script)
