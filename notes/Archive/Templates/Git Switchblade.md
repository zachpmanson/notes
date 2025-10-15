A script that will attempt to stash changes on your current branch when you switch(blade), and will restore those changes when you switch(blade) back.

```bash
#!/usr/bin/env bash


TARGET=$1

if [ -z "$TARGET" ]; then
  echo "Error: No target branch specified." >&2
  echo "Usage: git switchblade <branch-name>" >&2
  exit 1
fi

CURR=$(git rev-parse --abbrev-ref HEAD)
git stash push -u -m "switchblade on $CURR"
git switch $TARGET

STASH_ID=$(git stash list | grep "switchblade on $TARGET"| head -n 1 | cut -d: -f1)

# Check if a stash identifier was found
if [ -n "$STASH_ID" ]; then
  echo "Found matching stash: $STASH_ID. Popping it..."
  git stash pop "$STASH_ID"
else
  echo "No stash found containing the word 'switchblade'."
fi

```