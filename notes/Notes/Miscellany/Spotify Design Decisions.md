---
tags:
  - venting
---
This page is a list of design decisions made by Spotify that I consider shitty.  I'm sure some of them only A/B tested, coming and going silently, but some have lingered for years. In any case I have experienced (have been subjected to) all of these personally and they piss me off greatly.

See also: [Dear Spotify](https://www.todepond.com/wikiblogarden/work/dear-spotify/) by Lu Wilson
## Smart Shuffle Button Cycle Lock

Spotify has added a feature called Smart Shuffle that works like normal shuffling, but also added recommended songs in-between ever few tracks in the queue.  On paper I like this feature, though I have never found myself actually using it. I was introduced to it through the following infuriating UX.

I go the the Now Playing screen on the Android Spotify client. The playlist I am listening to is currently set to shuffle (regular shuffle), but I would like to turn off regular shuffle.  I press the button with a shuffle icon, which has for 10+ years been a single toggle that would instantly take effect.  Instead of a simple 2 option toggle, I find that it has been converted in to a 3 option cycle button, where pressing it cycles through the options of `Linear -> Shuffle -> Smart Shuffle -> Linear`.  I can see the thinking behind this decision though I don't like it since it breaks muscle memory established by this app for a decade and all other music playing applications.  That is not my issue though.

When you click the button and move the state from `Shuffle` to `Smart Shuffle`, the application begins loading the Smart Shuffle recommendations which means it must query Spotify servers, which is an operation that takes multiple seconds.  While this occurs, the button with a Shuffle icon becomes a button with a loading spinner, and becomes unclickable. I must wait multiple seconds before I can turn off Smart Shuffle.

`Linear -> Shuffle -> Loading (multiple seconds) -> Smart Shuffle -> Linear`

This is deeply infuriating.  I never even wanted to use Smart Shuffle in the first place and now I must wait for it.

This occurred every time I wanted to turn off  `Shuffle`.  Which is a lot.

As of 2024-01-21, this loading state of the button appears to have been removed, but the button still is a 3 option cycle which I dislike (though respect the elegance of).

## Overflow Menu Loading

For some godforsaken reason, the overflow menu for a track sometimes appears to require a network request before it can show.  If this request is slow, it will show a loading spinner in place of the menu, until the server responds.  Or in some cases, the **overflow menu will fail to load entirely**.  This is insane, since for the most part, the options on this menu are identical.  This is doubly insane since the menu can load without any issue what-so-ever in offline mode.

I have only ever experienced this issue on the Android mobile app, which for many years did not support swiping on a song to queue a song.  At this time you were only able to queue a song. through the overflow menu, which often times meant waiting multiple seconds for menu to appear.  God forbid you wanting to queue multiple songs in a row. Thankfully you can now bypass the menu loading by swiping a track to the right.

Oh wait!

## Can't Swipe to Queue on Blend Playlists

On Android you cannot swipe to queue a playlist if the playlist is a blend playlist??? Why would this screen use a different component to represent a list of songs to every other screen in the app? 

![[blend-swiping.webm]]

## Secret Sliding Menu

This one I only just noticed now while typing this post. There is a sliding menu that appears if you click on your profile picture in the corner of any of the 3 main screens.  It seems a bit sparse, like it would be better suited to being a drop down? In any case this menu can actually be accessed from any playlist folder screen as well, despite there being no indication of this.  This only seems to work on playlist folder screens though, as it doesn't work for any other subpages.

This one was annoying as I accidentally triggered in when attempting to swipe in from the left to go back a screen.

![[sliding-menu.webm]]

## Can't Swipe Up to Access Player

On Android you can swipe down on the player interface but you cannot swipe up to reveal it.  When you attempt this you will almost definitely skip the song that is currently playing, since the minimised version of the player only detects left and right swipes.

![[swipe-up.webm]]

## Unable to Remove DJ Shortcut On Desktop

On desktop they have added a link to the DJ feature at the top of Your Library, below pinned playlists.  Despite not being a playlist (nor a feature I use), it continues to appear even when you have set the filter to only show playlists.  As far as I know it cannot be removed?  But it can be pinned.  Despite already being permalocked to the top.
![[dj.png]]
The day after writing the previous paragraph, I noticed they had added the DJ to the same section in the mobile app, but long pressing the DJ icon shows you an option to hide it, which seems to have hidden it on all my devices.  Why is this option not available in the desktop client!

## Upcoming Complaints

- Smart Shuffle popup
- Rapidly toggling through Shuffle button states can cause the cycle to desync in strange ways
- Spotify (regular) Shuffle algorithm has some problems
