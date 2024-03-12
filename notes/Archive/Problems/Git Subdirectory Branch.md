---
tags:
  - git
---
Mounting a [[git]] branch to a subdirectory.

Create an orphaned branch if it doesn't already exist, and remove any shared history with the trunk.
```sh
git checkout --orphan gh-pages
git reset --hard
git commit --allow-empty -m "Init"
git checkout master
```

Make the subdirectory that will host the branch.
```sh
mkdir site
git worktree add site gh-pages
```

Moving in and out of this directory should now switch branches.

To set up a subdirectory branch on a cloned git repo, only run the last two commands.

This site uses this set up for deploying to GitHub Pages.

## Links
 - [Source](http://sangsoonam.github.io/2019/02/08/using-git-worktree-to-deploy-github-pages.html)