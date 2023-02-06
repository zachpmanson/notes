#!/bin/bash
git pull
git add notes
git commit -m "Auto-commit notes update"
git push
. ./deploy.sh