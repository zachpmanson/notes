---
tags:
  - venting
---
This page is a list of design decisions made by Spotify that I consider shitty.  I'm sure some of them only A/B tested, coming and going silently, but some have lingered for years. In any case I have experienced (have been subjected to) all of these personally and they piss me off greatly.
## Smart Shuffle Button Cycle Lock

Spotify has added a feature called Smart Shuffle that works like normal shuffling, but also added recommended songs in-between ever few tracks in the queue.  On paper I like this feature, though I have never found myself actually using it. I was introduced to it through the following infuriating UX.

I go the the Now Playing screen on the Android Spotify client. The playlist I am listening to is currently set to shuffle (regular shuffle), but I would like to turn off regular shuffle.  I press the button with a shuffle icon, which has for 10+ years been a single toggle that would instantly take effect.  Instead of a simple 2 option toggle, I find that it has been converted in to a 3 option cycle button, where pressing it cycles through the options of `Linear -> Shuffle -> Smart Shuffle -> Linear`.  I can see the thinking behind this decision though I don't like it since it breaks muscle memory established by this app for a decade and all other music playing applications.  That is not my issue though.

When you click the button and move the state from `Shuffle` to `Smart Shuffle`, the application begins loading the Smart Shuffle recommendations which means it must query Spotify servers, which is an operation that takes multiple seconds.  While this occurs, the button with a Shuffle icon becomes a button with a loading spinner, and becomes unclickable. I must wait multiple seconds before I can turn off Smart Shuffle.

`Linear -> Shuffle -> Loading (multiple seconds) -> Smart Shuffle -> Linear`

This is deeply infuriating.  I never even wanted to use Smart Shuffle in the first place and now I must wait for it.

This occurred every time I wanted to turn off  `Shuffle`.  Which is a lot.

As of 2024-01-21, this loading state of the button appears to have been removed, but the button still is a 3 option cycle which I dislike (though respect the elegance of).

## Upcoming Complains

Stay tuned!

- Smart Shuffle popup
- Rapidly toggling through Shuffle button states can cause the cycle to desync in strange ways
- Can't swipe right to add track to queue in a Blend playlist (Android)
- Can swipe down to dismiss Now Playing screen but cannot swipe up to make it appear again (just skips to next track) (Android)
- Spotify (regular) Shuffle algorithm has some problems
- For some god forsaken reason, clicking the overflow menu in a song sometimes fires requires a network request so it has to LOAD and can even FAIL ENTIRELY (Android)
