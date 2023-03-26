Learnings from setting up Postgres on a DigitalOcean droplet for [[Penultimate Guitar]].  This was done on trackstar-22, so should presumably work on any Ubuntu 22.04 instance.

1. Install postgres. This will add a `postgres` user account to the system. I set up another user account to interact with the database, in this case called `pg-user`.
2. Using `psql`, create a database that will be used for your application.
3. Whiler running `pg-user`, in `psql`, run `\password` and set a password for this account to interact with Postgres.  This password should not use an `@`, as it will conflict with the connection string later. 
4. Grant the user account access to the database with the SQL command. 

    ```sql
    GRANT ALL PRIVILEGES ON DATABASE "my_db" to my_user;
    ```

5. Modify `/etc/postgresql/14/main/pg_hba.conf` (or equivalent). Set the `ADDRESS` field for IPv4 connections to this:

    ```
    # IPv4 local connections:
    host    all             all             0.0.0.0/0              scram-sha-256
    ```

5. Modify  `/etc/postgresql/14/main/postgresql.conf`.  Set `listening_addresses` to all:

    ```
    # - Connection Settings -
    listen_addresses = '*'
    ```

6. Restart Postgres `systemctl restart postgres`
7. In the Prisma application, set up Prisma normally.  The connection string in `.env` should be this format:

    ```
    postgresql://pg-user:passwd@example.com:5432/db?schema=public
    ```

8. Push the schema designed in `prisma/schema.prisma` using the command `npx prisma db push`.
9. If this succeed, Prisma can now effectively connect to the database!

Tags: #self-hosting #linux