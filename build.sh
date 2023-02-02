#!/usr/bin/env bash

source ./venv/bin/activate
rm ./site/*.html
echo Activated venv
python3 ./generator/generator.py
deactivate
echo Deactivated venv
mkdir -p ./site/static/media
rm -r ./site/static/*
cp -R ./static/ ./site/static/
cp -R ./notes/Media/ ./site/static/media/
echo Done!