---
subtitle: The real heroes.
---
Databases are pure joy when they are well-structured, and nightmares when they aren't.  All databases structure decays as a function of continued development over time.

Databases are their own little world, speaking their own [[SQL|little language]], following different rules to the rest of the [[software]] world. They are hard to version control, hard to scale, and hard to live without.
## Databases Management Systems

Someone else (someone smarter) did the hard work for us!

- [[Postgres]]
- [[SQLite]]

## Object Relational Mapper

Since databases usually only speak [[SQL]], a [[language]] that is not very nice to use, there have been many attempts at creating translation layers between database models and normal [[Programming Languages|programming language]] constructs. I have used a few of these.

- [[Prisma]]
	- Schema definition is really cool, with automatic diffing and migration creation. Having a single location for the entire database is nice.
	- Automatic type definitions are also really nice
	- It's custom querying syntax is fine for simpler queries, but it lets you fall to normal SQL easily.
	- Not having to manually write out models makes this very fun to use.
	- Because it limits the scope of what it attempts to do, it avoids the pitfalls of most ORMs
	- Doesn't do anything for data migrations, other than give you an SQL file to fill out yourself. I kind of... respect this more? Other data migration tools end up becoming this just nested within other languages constructs (looking at you Alembic)
		- procedural SQL is awful but also kind of the only thing you can trust
	- makes transactions very straightforward
- SQLAlchemy
	- uhhhh
	- Very big, tries to do a lot of different things.
	- Does an admirable job.
	- Suffers standard ORM problems, annoying to have to manually match Python objects to Database objects
	- Doesn't do shit for type definitions that I didn't write myself.
	- Custom query syntax allows you to do complex things, but requires a lot of relearning how to do things that would be very straightforward in SQL.
	- It gives you plenty of deep tools that let you shoot yourself in the foot.
	- this + Alembic for revisions is.... okay
		- it bothers me that it doesn't use timestamps in the filename of each revision
- TypeORM
	- similar to SQLAlchemy
	- really I just never want to have to use anything that requires manual model creation anymore

Really all I want is something that can automatically create type definitions for database tables and automatically create migrations that I can later edit. In terms of querying syntax, I only want to use it for simple queries, and prefer an ORM that knows this and gets out of my way when I want to rawdog the database. (this is why I like using Prisma)

## Interesting Links

- [Code in database vs. code in application](https://brandur.org/fragments/code-database-vs-app), a discussion on the pros and cons of having application login in triggers/stored procedures vs server code
