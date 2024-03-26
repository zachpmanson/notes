---
tags:
  - dirty-hacks
  - javascript
  - nextjs
  - prisma
  - postgres
  - react
  - python
---
![[dotgrid-24G03-011888.svg]]

Minecraftle is a game fusing the gameplay of Wordle with crafting recipes from Minecraft.  It started as a university project I worked on in 2022 in a small team for [CITS3403](https://teaching.csse.uwa.edu.au/units/CITS3403/) (one of the better units in [[UWA Computer Science]]).

It was initially built with Vanilla [[JavaScript]]+Flask with a SQLite database, with the [live version](https://minecraftle.zachmanson.com) deployed with nginx on DigitalOcean.  v2 was fully rebuilt in Next.js and hosted on Vercel, with a Postgres instance hosted on DigitalOcean.

We received the top mark for the project and I continued development after we submitted it.  The source code is publicly available on the [repo](https://github.com/pavo-etc/minecraftle).  Since initial submission I've made a number of changes, some of which are enumerated [[Minecraftle v1.1]].

The game has daily puzzles and global leaderboards, with over 1M total players count at the time of writing.

![[minecraftle.png]]