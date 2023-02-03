#!/bin/bash
cd ./site/
git stash
git stash drop
git pull
cd ../
echo "Building..."
./build.sh
cd ./site/
git add -A
git commit -m "gh-pages deployment"
echo "Uploading to webserver..."
git push