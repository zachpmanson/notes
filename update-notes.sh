#!/bin/bash
set -e
git pull

if [[ `git status --porcelain` ]]; then
    # if there are changes to notes, commit them and push them
    git add notes
    git commit -m "Auto-commit notes update"
    git push
    echo "Commited notes to main branch"
else
    echo "No changes to notes"
fi

./deploy.sh
