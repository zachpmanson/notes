---
tags:
  - relics
---

An explanation of the existence of .DS_Store files in macOS by Arno Gourdol [posted on 2006-10-01](https://www.arno.org/on-the-origins-of-ds-store).

---

## If you are a Mac user, or if you have transferred files from Mac to Windows, you’re probably familiar with .DS_Store files. But where does this name come from?

Back in 1999 I was the technical lead for the Mac OS X Finder at Apple. At that time the Finder code base was some 8 years old and had reached the end of its useful life. Making any changes to it require huge engineering effort, and any changes usually broke two or three seemingly unrelated features. For Mac OS X we decided to rewrite the Finder from scratch.

Part of the work involved separating its user interface and its core functionality, the back-end. The back-end of the Finder enumerates files, watch for changes in the file system, deals with metadata, including icon locations and folder settings. Internally, those two components were known as Finder_FE and Finder_BE (Frontend and Backend).

However, we soon started realizing that the Finder backend would be useful outside of the Finder. Therefore, a plan was hatched to someday make it available as a public API. Since I had previously been responsible for naming Icon Services and Navigation Services, we decided to go with Desktop Services (at the time, we were also considering renaming the Finder to “Desktop”). Hence the name of the .DS_Store, for “Desktop Services Store”. We added a “.” in front of it so that it would be considered as an invisible file by Unix OS, including Mac OS.

Personally, I don’t think it’s a great name and I wish we had gone with something a bit more descriptive, but it’s too late for that :-)

There is also an unfortunate bug that is not fixed to this day that result in an excessive creation of .DS_Store file. Those files should only be created if the user actually makes adjustments to the view settings or set a manual location for icons in a folder. That’s unfortunately not what happens and visiting a folder pretty much guarantees that a .DS_Store file will get created

Incidentally, Finder_BE aka Desktop Services did end up being used by more than just the Finder: Navigation Services (the Open/Save dialog) now also make use of it, although it didn’t in the initial release of Mac OS. However, the Desktop Services API has still not been fully released.