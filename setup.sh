#!/usr/bin/env bash
mkdir site
git worktree add -b gh-pages ./site
it branch --set-upstream-to=origin/gh-pages gh-pages

python3 -m venv venv 
. ./venv/bin/activate
python3 -m pip install -r generator/requirements.txt
