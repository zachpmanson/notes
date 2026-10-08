---
date: 2026-10-05
tags:
  - posts
---

Everyone says they want a pure chronological feed but the dream breaks as soon as one of your feeds posts 20x more often as the rest.

This applies on small scales and big, ABC News drowns out my daily posting friend the same way my daily posting friend drowns out my quarterly posting friend. What I want is frequency weighted chronological feeds. Infrequent feeds should be boosted, frequent feeds should be dragged down, but two feeds of similar frequency should come out approximately chronological.

After a bunch of experimentation, here is the algorithm I landed on:

```
actual_age = hours since post was published
gap = average hours between posts of feed

multiplier = clamp((72 / max(0.1, gap))^2.5, 0.0001, 100)
effective_age = actual_age * multiplier
```

I have implemented this in my RSS reader Dripfeed as *Sort by Rarity*, where each feed is given a rarity score, and that is used to scale the real age of each post within the feed. The scaled age, aka effective age, gets sorted chronologically.  RSS is particularly well suited to this since each pull of an RSS feed comes with the latest 20 posts which is plenty to put together a moving average.

Gap is constant per feed, but will change a little with every new post.  72 hours is the midpoint I settled on. Feeds that post more often that this are punished, feeds less often than that are rewarded. The clamp puts limits on how much something can be scaled by this method, scaling is  "saturated" by that point, where all things return to pure chronological.

Within the clamp this is an inverse power law, so relative differences in most frequency are treated with equal scaling differences. If feed A's frequency is 2x feed B's frequency, feed A will get ≈5.7x the scaling. This applies to all timespans, if feed A posts daily and feed B bi-daily, or feed A is monthly and feed B is bi-monthly. The curve gets even sharper as the frequency ratio grows.

This is quite aggressive scaling, but that's what I want.  A monthly post will stay at the top of the feed for weeks, only being outranked by other more recent monthly posts. At the time of writing Dan Luu published a post 15 days ago that still has an effective age of 8 min because he posts once every 29 days. That's so rare that it overpowers even my monthly feeds. There are 2 other elements that are needed to make this algorithm work nicely.

1. Priority queue showing all unread items before all read items
2. [[Explicit reading]]

Here's how different kinds of feeds get treated by this formula:

| Feed                          | Avg Gap | Multiplier   | Effective age after 1m | 5m  | 30m | 1h  | 6h  | 24h  | 72h  | 1wk  | 2wk    |
| ----------------------------- | ------- | ------------ | ---------------------- | --- | --- | --- | --- | ---- | ---- | ---- | ------ |
| Hourly (ABC News)             | <2h     | 100 (capped) | 2h                     | 8h  | 2d  | 4d  | 25d | 100d | 300d | 700d | 1,400d |
| Multi-daily (Daring Fireball) | 6–8h    | 100 (capped) | 2h                     | 8h  | 2d  | 4d  | 25d | 100d | 300d | 700d | 1,400d |
| Daily (SMBC)                  | 24h     | 15.59        | 16m                    | 78m | 8h  | 16h | 4d  | 16d  | 47d  | 109d | 218d   |
| Weekly (Friend’s Letterboxd)  | 7d      | 0.12         | 7s                     | 36s | 4m  | 7m  | 43m | 3h   | 9h   | 20h  | 40h    |
| Monthly (Friend’s Blog)       | 30d     | 0.0032       | 0s                     | 1s  | 6s  | 11s | 1m  | 5m   | 14m  | 32m  | 64m    |

The majority of my feeds are quite rare, collectively there's enough that they push down the hyper-posters. The more niche something is the more you see it. That's perfect! That's exactly what I want. Surface the weird and the rare.

![[rarity-buckets.png]]

## BYO Algorithm

I came to this equation after playing around with many different options in a little RSS feed testbed I spun up. Experimenting with different half-lives and sharper power laws let me tune it just how I wanted, with a simulated feed live. This was fun and a bit eye opening to how poor pure chronological feeds are.

![[rarity-tester.png]]

[I recommend some playing around with it](https://github.com/zachpmanson/dripfeed/tree/master/tools/rarity-tester) if you want to implement something similar, my scaling might be a bit strong for your taste. Bring your own OPML file.

Now that I've done it, I lament every app that doesn't let me pick my own algorithm.

![[rarity chart.png]]