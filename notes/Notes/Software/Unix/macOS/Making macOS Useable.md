---
tags:
  - lists
  - macos
---
macOS is a lovely operative system except that it is missing so many basic usability features that macOS feels more like anemicOS.

## Must have

- No proper package manager  
   [Homebrew](https://brew.sh/) package manger
- No window tiling  
   [Amethyst](https://ianyh.com/amethyst/) tiling window manager
- Can't set  3 finger tap on touchpad to middle click  
   [MiddleClick](https://github.com/artginzburg/MiddleClick-Ventura)
- Setting trackpad scrolling direction and mouse scrollwheel scrolling direction independently  
   [Scroll Reverser](https://pilotmoon.com/scrollreverser/)
- No path in Finder  
  `Cmd+Alt+P` to toggle path bar

## Nice to have

- ~~[Caffeine](https://intelliscapesolutions.com/apps/caffeine) - keeps screen awake while active~~ Not needed, macOS `caffeinate` command handles this
- [AltTab](https://alt-tab-macos.netlify.app/) - makes alt+tab behaviour sane, more like Windows/Linux

## Do it

```sh
brew install \
--cask amethyst \
--cask --no-quarantine middleclick \
--cask scroll-reverser \
--cask alt-tab
```

## Remapping

I am currently trialing disabling Cmd+Q as I hit it accidentally too often. Using the System Settings Keyboard Shortcuts options, I have changed Cmd+Q to Invert Screen Colours and switched Cmd+Opt+Q to quit.