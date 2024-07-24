To tell [[Notes/Software/Programs/Git/Git]] to ignore changes to a file, set the skip worktree option.

```sh
git update-index --skip-worktree filename
```

This will fail loudly when something inevitably go wrong and the file gets changed in an incompatible way, one way or another.

Then you can undo it:

```sh
git update-index --no-skip-worktree <file>
git add -p <file>
git update-index --skip-worktree <file>
```

Found [here](https://stackoverflow.com/questions/16598257/ignore-specific-changes-to-a-file-in-git-but-not-the-entire-file).