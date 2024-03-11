#!/usr/bin/env bash
set -e
mkdir site
echo Adding worktree...
git worktree add -b gh-pages ./site
git fetch
git branch --set-upstream-to=origin/gh-pages gh-pages

echo Pulling last site commit...
cd site
git reset --hard origin/gh-pages
cd ..


python3 -m venv venv 
. ./venv/bin/activate
python3 -m pip install -r generator/requirements.txt
