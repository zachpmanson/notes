---
subtitle: YouTube Actually Has Zero 9s of Availability
tags:
  - posts
date: 2026-11-16
---

YouTube RSS returns 404 and 500 errors a quarter of the time.

![[youtube-down.png]]

The 6 feeds in the screenshot above were being polled at 15 minute intervals, which is aggressive but that was the point. [Some RSS readers do poll that aggressively](https://www.jefftk.com/p/looking-at-rss-user-agents) for better or for worse. My first assumption is this is some kind of rate limiting, but there's no backoff instruction in the headers, no 429 or 503. The failed requests return 404 most of the time, and occasionally 500? I assume feed readers are not be set up to interpret 404 as *let's begin exponential backoff*.

This is nasty because it means that if you've already got some feeds subscribed, existing polling may have already exhausted your quota and adding a new feed can fail with 404, likely resulting in your reader rejecting the feed outright. This problem was the reason I started monitoring it, intermittent failures when adding new feeds.

![[uptime.svg]]

96% of the failures happen between 15:00-17:00 in my timezone. I started tracking this on 2026-09-14 in Melbourne, meaning that I have readings before and after a local daylight savings shift. Following the DST shift, the problems start to happen around an hour earlier UTC. Adjusting everything to UTC reveals that the problems seem always seem to go away at 07:00, until 2026-11-02 when the problems start to go away at 08:00 UTC, lining up with the US Pacific timezone's daylight savings shift, so I guess 07:00 US Pacific is when the rate limit quotas get reset? That still doesn't explain the occasional 500 errors.

In any case, YouTube should return 429 or 503 when rate limiting instead of 404.  I assume the rate limit is accumulative, so having 1 feed polling 100 times a day would be as bad as 50 feeds polling twice a day. I'll play around with this in the future, but if this is the case, it makes YouTube RSS less and less usable as you subscribe to more feeds. 15 minute polling is excessive, but I was running into problems in Nextcloud News, which has a default polling rate of 1 hour.[^rachel] Assuming it's just naively counting requests, I would only need 24 channels to bring the feeds to 75% uptime. Given that at the time of writing I have 306 subscriptions[^subs], adding new feeds would fail the majority of the day, and I assume many feeds would not get updated since a single poll would trip the rate limit quota. Until YouTube makes their feeds have suggest backing off[^fear], migrating to YouTube to RSS is untenable.[^protip]

[^reader]: NetNewsWire, then Nextcloud News, now Nextcloud News as a backend + my custom client Dripfeed.
[^rachel]: I'm sure rachelbythebay would disapprove.
[^subs]: Yes I recognise this is ludicrous, I don't watch the vast majority of these. I'm overdue for a cull and a severe detox. YouTube is my vice, do not ask my about my screen time for it. My transition to RSS was supposed to be part of limiting my intake, since my RSS frontend Dripfeed was can to limit the amount you can actually consume.
[^fear]: I'm actually scared to point this out, if someone at Google sees this they are far more likely to decommission the RSS feeds than fix them.
[^protip]: Protip for YouTube RSS feeds: YouTube lists this URL format as the channel URL `feeds/videos.xml?channel_id=UCG<channel_id>`. If you change it to `/feeds/videos.xml?playlist_id=UULFG<channel_id>` you get a feed excluding YouTube Shorts.