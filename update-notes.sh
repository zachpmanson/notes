#!/bin/bash
git stash
git pull
git stash apply
git add notes
git commit -m "Auto-commit notes update"
git push
. ./deploy.sh