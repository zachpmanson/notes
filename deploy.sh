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
DATE=$(date --iso-8601=seconds -u)
git commit -m "gh-pages deployment $DATE"
echo "Uploading to webserver..."
git push
