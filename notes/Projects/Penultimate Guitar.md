---
tags:
  - nextjs
  - prisma
---
Penultimate Guitar is an alternate frontend for Ultimate Guitar that focuses on mobile usability and Spotify integration.  All features are available on mobile*.

It is built with TypeScript, Next.js, and Tailwind and deployed on Vercel.  It works in tandem with a Postgres instance on a DigitalOcean through Prisma.  The source code takes a lot of inspiration from [[Alculator]].

Features include:

- importing Spotify playlists, will find the highest rated chords for all songs in playlist
- chord tooltips
- transposing
- autoscrolling
- saving tabs to home
- organising saved tabs into folders

The source code is available [here](https://github.com/pavo-etc/penultimate-guitar).  The deployed version can be found [here](https://pg.zachmanson.com).

Chord tooltips are only possible through [chords-db](https://github.com/tombatossals/chords-db) and [react-chords](https://github.com/tombatossals/react-chords), both by David Rubert.

---

\* Except chord tooltip inversions, though its only because I haven't thought of a simple interface for it yet