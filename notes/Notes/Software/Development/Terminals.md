---
tags:
  - relics
---

> A terminal is a physical device with a keyboard and screen connected to a computer running various OS types. A tty is the Unix device name for a physical or virtual terminal connection. A shell is the Unix command interpreter. A console is a generic term for a primary i/o device or interface. In unix terms the console is where the boot/startup messages are sent to. After bootup the console effectively becomes a terminal.

-- [/u/oscarboom](https://www.reddit.com/r/programming/comments/41u5hw/what_is_the_exact_difference_between_a_terminal_a/cz5ejh6/)

```
//===========================\\
||          Terminal         ||
||             |-----------| ||
|| Keyboard--->|   Input   |-++->|---|   |-------|
||             |-----------| ||  |tty|<=>| shell |       
||         |---------|<------++--|---|   |-------|
|| Print<--|  Output |       ||
||         |---------|       ||
||                           ||
\\===========================//
```

-- [/u/lookmeat](https://www.reddit.com/r/programming/comments/41u5hw/what_is_the_exact_difference_between_a_terminal_a/cz5mgts/)
