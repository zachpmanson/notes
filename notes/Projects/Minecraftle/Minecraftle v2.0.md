---
tags:
  - posts
date: 2024-04-08
---
[[Minecraftle]] blew up!  At the time of writing it has had over 1 million players and seems to still be increasing.  Seems like it became popular thanks to a few YouTube videos and TikToks. This huge spike in players revealed how poorly made it all was.

The stats page in particular was poorly done.  Originally I had made the schema as simple as possible and only stored the record of each game in one big table. This worked for small player counts, but meant calculating rankings was quadratic so the stats page eventually 10+ seconds to load.  I only discovered this was happening when the database for [[Penultimate Guitar]] would be killed to allocate more resources every time someone loaded the stats page.  

Since rewriting the database meant I'd need to get rid of the entire backend, I decided this was the time to move away from Flask and static JavaScript and port it to Next.js.  I had been meaning to do this for a while.  The Vanilla JS I had been using prior was very janky and poorly made.  I was still unemployed at this time and had plenty of free time since most of my friends had left Melbourne to see their families for Christmas.

The new version of Minecraftle is deployed now on Vercel with a proper instance of Postgres for storing user scores. Rankings are still slow to calculate since all million+ players must be ordered, but they are calculated once per hour via a cronjob that refreshes a materialised view so the pageload is fast.  I'm sure I could do something clever here, chunking the calculations or having them incrementally calculated when a new game score is submitted, but this works for now.

Alongside this rewrite I was able to add a few long requested features, like a clear button.

## Mistakes

### Database Broke

I accidentally ran the migration script twice, once a few weeks prior to deployment to generate some test data and once on the day I deployed.  I forgot about the initial run in the intervening weeks.  Making matters worse, the second run used the old dump of the database, meaning that all scores were double what they were 3 weeks prior.  This was painful to diagnose as some scores had gone up while others had gone down.  I was eventually able to figure out what had happened thanks to [this bug report](https://github.com/zachpmanson/minecraftle/issues/34) which contained a screenshot of the scores the day before.  Thank you very much [suppergerrie2](https://github.com/suppergerrie2)!

### CDN vs Audio Files

![[mctl-routes.png]]

Back when Minecraftle was just a uni project, one of my teammates, Harrison Oates, added a button that would play in game audio from Minecraft.  This was cute and insignificant, to the point where I forgot it existed.  When I deployed on Vercel this became a problem since almost all my bandwidth (100GiB) was used by this single mp3 file! I removed this feature, but other static assets were going to use my remaining bandwidth.  I had to switch to running it on a new DigitalOcean droplet for the rest of the month.

Hopefully this are the last updates Minecraftle will need for a long time!


