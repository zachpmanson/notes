---
tags:
  - relics
---
On Unix systems a file can be hidden from `ls` and other applications by prefixing the filename with a period.  This was introduced in Unix Version 2 as a side-effect of adding  files `.` and `..` to support the new hierarchical filesystem.  To avoid these navigation files appearing in every directory when `ls` was executed, filenames with the first character `'.'` were filtered out.  This unintentionally hid other files with this prefix. Once this precedent was set, other programs implemented the same behaviour, which continues to this day.

More details on this can be read in [[Rob Pike's Lesson in Shortcuts]].