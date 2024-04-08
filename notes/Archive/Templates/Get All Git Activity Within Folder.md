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