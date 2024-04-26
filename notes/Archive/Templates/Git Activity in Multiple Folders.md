---
subtitle: A template for listing all the commits you did on a certain date.
date: 2024-04-22
tags:
  - posts
  - git
---
A script I like to drop into my projects folders to see what I was working on for a given day.

```sh
day=$1
repo_folder=~/projects
for dir in "$repo_folder"/*/; do
    # Check if the directory is a git repository
    if [ -d "$dir/.git" ]; then
        cd $dir
        git log --after="$day 00:00" --before="$day 23:59?" --author="Zach"
    fi
done
```