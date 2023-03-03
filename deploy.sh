#!/bin/bash
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
git commit -m "gh-pages deployment"
echo "Uploading to webserver..."
git push