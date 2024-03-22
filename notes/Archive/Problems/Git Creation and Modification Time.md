---
tags:
  - git
---

[[Git/Git]] does not include creation time and modification time in file metadata, but you can use the git commit history to retrieve similar results.

File creation date:

```sh
git log --pretty=format:"%ad," --date=short --diff-filter=A -- "$file"
```

File update date:

```sh
git log -1 --pretty=format:"%ad" --date=short -- "$line"
```
