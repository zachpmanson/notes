---
subtitle: An internet that could have been.
date: 2025-10-02
tags:
  - posts
---
A Wikipedia article that makes me sad is the one on [Feed URI scheme](https://en.wikipedia.org/wiki/Feed_URI_scheme). It is a draft proposal from 2003 for a URI scheme designed to link to [[RSS]]/Atom Readers directly to a feed. 

A link that looks like this [`feed://notes.zachmanson.com/posts.xml`](feed://notes.zachmanson.com/posts.xml) can be clicked on and will open directly a feed aggregator, no matter the origin of the link. This is essentially a **subscribe button for the whole internet**. 

It never made it to official status, and the Wikipedia page listing programs that support it was last updated in 2006. The software cited is NetNewsWire, FeedDemon, Flock, and Safari(‽‽‽‽). Of these, FeedDemon was discontinued in June 2013, Flock was a browser that was discontinued in 2011, Safari support was removed at some point after 2007[^1].

NetNewsWire still exists, actively supported and of extremely high quality. At the time of writing it is what I use for following feeds. 19 years later, it still supports `feed://` links! It works great. I wish this was more common.

I discovered that Pocket Casts, my longtime podcast app[^2] also supports `feed://` links, interpreting the link as a podcast feed, though it seemed unable to differentiate podcast feeds from text feeds.

In honour of this I have added a subscribe link to this website!


[^1]: [As stated by Jens Alfke](https://lobste.rs/c/d29mru), a former Apple developer, who developed the feature with Ricci Adams. The comment also mentions that the feed reader was supported in Apple Mail, although I do not know if Apple Mail supported `feed://` links.

[^2]: I purchased Pocket Casts in 2016. They have gone through a few owners and a few pricing structure changes in that time. In my 9 years of using it I've never seen an ad, until last week. Comments by Matt Mullenweg on HN imply this might be erroneous, but I have my doubts. If the ads persist, I will find a fork or create my own.