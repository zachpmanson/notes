---
subtitle: Penultimate Guitar is an alternate frontend for Ultimate Guitar.
---
It focuses on mobile usability and Spotify integration.  All features are available on mobile*.

It is built with [[TypeScript]], Next.js, and Tailwind and deployed on Vercel. It works in tandem with a Postgres instance on a DigitalOcean through [[Prisma]].  The source code takes a lot of inspiration from [[Alculator]]. Over time I've added account syncing with Spotify OAuth using NextAuth, and migrated the backend to tRPC.

Features include:

- saving favourite tabs to device, or to your account
- Spotify login (alpha), allowing you to import playlists and sync saved tabs across devices
	- when Spotify playlist are imported, the highest rated chords for all songs in playlist will be found
- chord tooltips
- transposing
- autoscrolling
- saving tabs to home

The source code is available [here](https://github.com/pavo-etc/penultimate-guitar).  The deployed version can be found [here](https://pg.zachmanson.com).

Chord tooltips are only possible through [chords-db](https://github.com/tombatossals/chords-db) and [react-chords](https://github.com/tombatossals/react-chords), both by David Rubert.

I built it because I was mad at how poor Ultimate Guitar is on mobile devices.

---

\* Except chord tooltip inversions, though its only because I haven't thought of a simple interface for it yet