#!/bin/bash
git stash
set -e
git pull
git stash apply
git add notes
git commit -m "Auto-commit notes update"
git push
./deploy.sh