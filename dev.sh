#!/usr/bin/env bash
cd site
python3 -m http.server &
cd ..
watchman-make -p '**/*.jinja' '**/*.py' '**/*.md' -r 'clear; ./build.sh'
trap 'kill $(jobs -p)' EXIT
