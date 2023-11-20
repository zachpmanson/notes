#!/usr/bin/env bash
set -e
source ./venv/bin/activate
rm -rf ./site/*
echo Activated venv
python3 ./generator/generator.py $1
echo Generated!
deactivate
echo Deactivated venv
mkdir -p ./site/media ./site/static
cp -R ./static/* ./site/static/
cp -R ./notes/Media/* ./site/media/
echo "notes.zachmanson.com" >./site/CNAME
echo Done!
