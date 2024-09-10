---
tags:
  - self-hosting
  - posts
  - venting
date: 2024-05-01
subtitle: Just use FolderSync.
---
Nextcloud is excellent, and its Android app is great.  I found the app's Auto-Upload feature to be nigh unusable.

I have 20GiB+ of photos on my phone and would like a backup.  My primary Nextcloud account is synced to my PCs, so any file added to it will be downloaded to all devices.  I don't need local access to these photos on all my PCs, so I created a seperate Nextcloud account just for camera roll uploads. If I needed to access these photos from a PC I could log in to the Nextcloud web interface with the camera roll account.

Attempting to use Auto-Upload on my phone's Camera folder was messy.  It kept uploading photos to the wrong Nextcloud account, incorrectly counting how many files there were, and did not supporting bidirectional sync.  It was unpredictable how long it would take to actually trigger an upload, not having a manual way of starting one.  It also limited automatic uploads to a single folder. These issues were all seperate from the fact that the UI was extremely glitchy as it tried to show 20GiB of photos.

I found using [FolderSync](https://www.tacit.dk/foldersync) a much better experience.  It let me set up bidirectional sync between custom Nextcloud folders and local folders, let me choose cadence for syncing (with many configuration options like only allowing upload when charging) and allowed me to manually trigger a sync.  The premium version is absolutely worth it.  I'm only scratching the surface of what it can do here, but for my needs it's perfect.
