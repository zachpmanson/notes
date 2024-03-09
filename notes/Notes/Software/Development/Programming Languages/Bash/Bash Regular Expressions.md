Globbing is relatively simple.  More powerful string matcing can be done with regular expressions.  In [[Notes/Software/Unix/Unix]], modern regex style is derived from `ed` (a predecessor to `vi`).

## Syntax

| ed | shell | description |
| -- | ----- | ------------|
| `.` | `?` | single character |
| `[ ]` | `[ ]` | single from this set or range |
| `[^ ]` | `[^ ] | single character not in set/range |
| `*` |  | >=0 occurances of previous character |
| `.*` | `**` | >=0 occurances of any letter |
| `^` | | start of string |
| `$` | | end of string |
| `\` | `\` | escape character |
| `\( \)` | | capture match |


## Capturing Matches

`sed` and `grep` provide a way capturing a match and using it again later.

Using `\( \)` (up to 9 times), you can recall the captured text with `\1`, `\2` ...


