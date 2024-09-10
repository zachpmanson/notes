---
tags:
  - prisma
---
If you are making a table for use with Prisma, it must have a unique constraint on the primary key.  pgAdmin 4 is not capable of this, so you must write the constraint manually or write it into the `schema.prisma` file and `prisma db push` it.

This functionality[ is being added in pgAdmin 6.8](https://stackoverflow.com/questions/71348468/how-to-add-unique-key-constraint-on-column-in-table-in-erd-tool-in-pgadmin4).
