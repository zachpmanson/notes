#!/usr/bin/env bash
cd ./site/
git stash
git stash drop
set -e
git pull
cd ../
echo "Building..."
./build.sh
cd ./site/
git add .
DATE=$(date -Iseconds)
git commit -m "gh-pages deployment $DATE"
echo "Uploading to webserver..."
git push
