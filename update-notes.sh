#!/bin/bash
git fetch
git stash
set -e
git pull
git stash apply


if [[ `git status --porcelain` ]]; then
    # if there are changes to notes, commit them and push them
    git add notes
    git commit -m "Auto-commit notes update"
    git push
    echo "Commited notes to main branch"
# else
  # No changes
fi

./deploy.sh
