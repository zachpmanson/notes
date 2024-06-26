#!/usr/bin/env bash
set -e
source ./venv/bin/activate
rm -rf ./site/*


# skip creating history index if -f flag is passed
if [ "$1" == "-f" ]; then
    echo "Skipping history index creation"
    shift
else
    # Create history index
    echo Creating history index...
    rm -f history.csv
    find notes -name "*.md" | while read line; do
        echo -n "\"$line\"," >> history.csv
        git log --pretty=format:"%ai," --date=short --diff-filter=A -- "$line" | tail -n1  >> history.csv
        git log -1 --pretty=format:"%ai" --date=short -- "$line" | tail -n1  >> history.csv
        echo "" >> history.csv
    done
    echo History index created!
fi

echo Activated venv
echo Generating...
python3 ./generator/generator.py $1
echo Generated!
deactivate
echo Deactivated venv
mkdir -p ./site/media ./site/static
cp -R ./static/* ./site/static/
cp -R ./notes/Media/* ./site/media/
echo "notes.zachmanson.com" >./site/CNAME
echo Done!
