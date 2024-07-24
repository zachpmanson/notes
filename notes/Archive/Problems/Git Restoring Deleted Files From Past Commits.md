---
tags:
  - git
---
From [this StackOverflow answer](https://stackoverflow.com/a/1113140).

---

Find the last commit that affected the given path. As the file isn't in the HEAD commit, that previous commit must have deleted it.

```bash
git rev-list -n 1 HEAD -- <file_path>
```

Then checkout the version at the commit before, using the caret (`^`) symbol:

```bash
git checkout <deleting_commit>^ -- <file_path>
```

Or in one command, if `$file` is the file in question.

```bash
git checkout $(git rev-list -n 1 HEAD -- "$file")^ -- "$file"
```

---

If you are using zsh and have the EXTENDED_GLOB option enabled, the caret symbol won't work. You can use `~1` instead.

```bash
git checkout $(git rev-list -n 1 HEAD -- "$file")~1 -- "$file"
```