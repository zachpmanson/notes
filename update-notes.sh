#!/usr/bin/env bash
set -e
git pull --autostash

if [[ $(git status --porcelain) ]]; then
    g add -N notes # add new files as tracked files
    # if there are changes to notes, commit them and push them
    FILESCHANGED=$(git diff --name-only notes | sed 's/.*/"&"/' | xargs -n1 basename | sed 's/\.md//' | tr "\n" " ")
    CLEANFILENAMES=${FILESCHANGED% }
    git add notes
    git commit -m "Update notes: $CLEANFILENAMES"
    git push
    echo "Commited notes to main branch"
else
    echo "No changes to notes"
fi

./deploy.sh
