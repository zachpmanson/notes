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
DATE=$(2023-11-20T05:03:57+00:00)
git commit -m "gh-pages deployment $DATE"
echo "Uploading to webserver..."
git push
