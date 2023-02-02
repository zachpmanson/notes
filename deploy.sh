#!/bin/bash
cd ./site/
git stash
git stash drop
git pull
cd ../
echo "Building..."
./build.sh
#rsync -rvhP --inplace  --include=".htaccess" --exclude={'.*','src'} $HOME/projects/c/ochrs/ uberspace:html/
cd ../site/
git add -A
git commit -m "gh-pages deployment"
echo "Uploading to webserver..."
git push