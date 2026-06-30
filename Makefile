# Ochrs static wiki generator
#
# Migrated from the *.sh scripts. Each target mirrors a former script:
#   setup        <- setup.sh         (one-time gh-pages worktree setup)
#   build        <- build.sh         (full build, regenerates history index)
#   build-fast   <- build.sh -f      (build, skip history index)
#   history      <- build.sh         (regenerate history.csv only)
#   dev          <- dev.sh           (serve + rebuild on change)
#   deploy       <- deploy.sh        (build and push the gh-pages site)
#   update-notes <- update-notes.sh  (commit note changes, then deploy)
#
# Pass extra args to the generator with ARGS, e.g. `make build ARGS=foo`.

.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
SHELL := /usr/bin/env bash

ARGS ?=

.PHONY: setup build build-fast history static dev deploy update-notes clean

## One-time setup: add the gh-pages worktree under ./site
setup:
	mkdir site
	echo Adding worktree...
	git worktree add -b gh-pages ./site
	git fetch
	git branch --set-upstream-to=origin/gh-pages gh-pages
	echo Pulling last site commit...
	cd site
	git fetch
	git reset --hard origin/gh-pages

## Full build: regenerate the history index, then generate the site
build: history generate static
	echo Done!

## Build without regenerating the history index
build-fast:
	echo "Skipping history index creation"
	$(MAKE) generate static
	echo Done!

## Regenerate history.csv (creation + last-modified dates per note)
history: clean
	echo Creating history index...
	rm -f history.csv
	find notes -name "*.md" | while read line; do
	    echo -n "\"$$line\"," >> history.csv
	    git log --pretty=format:"%ai," --date=short --diff-filter=A -- "$$line" | tail -n1 >> history.csv
	    git log -1 --pretty=format:"%ai" --date=short -- "$$line" | tail -n1 >> history.csv
	    echo "" >> history.csv
	done
	echo History index created!

# Run the generator (internal; use build / build-fast)
generate:
	echo Generating...
	uv run main.py $(ARGS)
	echo Generated!

# Copy static assets and site metadata into ./site (internal)
static:
	touch ./site/.nojekyll
	mkdir -p ./site/media ./site/_static
	cp -R ./static/* ./site/_static/
	cp -R ./notes/Media/* ./site/media/
	echo "notes.zachmanson.com" > ./site/CNAME

# Empty the generated site directory (internal)
clean:
	rm -rf ./site/*

## Serve ./site locally and rebuild on source changes
dev:
	cd site && python3 -m http.server &
	trap 'kill $$(jobs -p)' EXIT
	watchman-make -p '**/*.jinja' '**/*.py' '**/*.md' '**/*.css' -r 'clear; $(MAKE) build'

## Build the site and push it to the gh-pages branch
deploy:
	cd ./site/
	git stash || true
	git stash drop || true
	git pull
	cd ../
	echo "Building..."
	$(MAKE) build
	cd ./site/
	git add .
	git commit -m "gh-pages deployment $$(date -Iseconds)"
	echo "Uploading to webserver..."
	git push

## Commit any note changes on main, then deploy the site
update-notes:
	git pull --autostash
	if [[ $$(git status --porcelain) ]]; then
	    git add -N notes # add new files as tracked files
	    FILESCHANGED=$$(git diff --name-only notes | sed 's/.*/"&"/' | xargs -n1 basename | sed 's/\.md//' | tr "\n" " ")
	    CLEANFILENAMES=$${FILESCHANGED% }
	    git add notes
	    git commit -m "Update notes: $$CLEANFILENAMES"
	    git push
	    echo "Commited notes to main branch"
	else
	    echo "No changes to notes"
	fi
	$(MAKE) deploy
