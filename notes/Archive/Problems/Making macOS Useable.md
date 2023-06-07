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

- [Caffiene](https://intelliscapesolutions.com/apps/caffeine) - keeps screen awake while active

## Do it

```sh
brew install \
--cask amethyst \
--cask --no-quarantine middleclick \
--cask scroll-reverser \
--cask caffeine
```

Tags: #lists #macos