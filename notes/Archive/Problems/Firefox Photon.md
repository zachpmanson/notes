---
tags:
  - dirty-hacks
---
Styling Firefox Proton to resemble Firefox Photon.

Originally tested on Firefox 91, confirmed working on Firefox 104.

Firefox Proton
![[firefox-proton.png]]

Firefox Photon
![[firefox-photon.png]]


Firefox Proton brought many lovely features, but I deeply prefer the Photon tab design.  Luckily, Proton supports applying CSS styling to window elements like the tab bar.

1. Open `about:config`
2. Find for `toolkit.legacyUserProfileCustomizations.stylesheets`, set its value to true.
3. Open `about:support` and go to the directory marked "Profile Directory" or "Profile Folder".
4. Create file `<profile directory>/chrome/userChrome.css` with custom stylesheet, e.g.
```css
.tab-background {
	border-radius: 0px 0px !important;
	margin-bottom: 0px !important;
	margin-top: 0px !important;
}

.tabbrowser-tab:not([selected=true]):not([multiselected=true]) .tab-background {
	background-color: color-mix(in srgb, currentColor 0%, transparent);
}
```
5. Restart Firefox

![[firefox-proton-modded.png]]

## Links
 - [Source](https://superuser.com/questions/1653533/how-to-switch-back-to-firefox-old-style-of-tabs/1669549#1669549)
 - [Someone doing it even better](https://github.com/black7375/Firefox-UI-Fix)
 - [Firefox UI History](https://github.com/black7375/Firefox-UI-Fix/wiki/%5BArticle%5D-0.-Firefox-UI-UX-history)