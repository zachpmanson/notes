#!/usr/bin/env bash

source ./venv/bin/activate
echo Activated venv
python3 ./generator/generator.py
deactivate
echo Deactivated venv
cp -R ./notes/Media ./site/Media 
echo Done!