SHELL := /usr/bin/env bash

ARGS ?=

.PHONY: setup build build-fast history generate static dev deploy update-notes clean format

## One-time setup: add the gh-pages worktree under ./site
setup:
	mkdir site
	@echo Adding worktree...
	git worktree add -b gh-pages ./site
	git fetch
	git branch --set-upstream-to=origin/gh-pages gh-pages
	@echo Pulling last site commit...
	cd site && git fetch && git reset --hard origin/gh-pages

## Full build: regenerate the history index, then generate the site
build: history generate static
	@echo Done!

## Build without regenerating the history index
build-fast: clean generate static
	@echo "Skipping history index creation"
	@echo Done!

## Regenerate history.csv (creation + last-modified dates per note)
history: clean
	@echo Creating history index...
	rm -f history.csv
	@set -e; find notes -name "*.md" | while read line; do \
	    echo -n "\"$$line\"," >> history.csv; \
	    git log --pretty=format:"%ai," --date=short --diff-filter=A -- "$$line" | tail -n1 >> history.csv; \
	    git log -1 --pretty=format:"%ai" --date=short -- "$$line" | tail -n1 >> history.csv; \
	    echo "" >> history.csv; \
	done
	@echo History index created!

# Run the generator (internal; use build / build-fast)
generate:
	@echo Generating...
	uv run main.py $(ARGS)
	@echo Generated!

# Copy static assets and site metadata into ./site (internal)
static:
	touch ./site/.nojekyll
	mkdir -p ./site/assets ./site/_static
	cp -R ./static/* ./site/_static/
	cp -R ./notes/Assets/* ./site/assets/
	echo "notes.zachmanson.com" > ./site/CNAME

# Empty the generated site directory (internal)
clean:
	rm -rf ./site/*

## Serve ./site locally and rebuild on source changes
dev:
	cd site && python3 -m http.server & \
	trap 'kill $$(jobs -p)' EXIT; \
	watchman-make -p '**/*.jinja' '**/*.py' '**/*.md' '**/*.css' -r '$(MAKE) build-fast'

## Format code
format:
	uv run ruff format .
	uv run ruff check --fix .

## Build the site and push it to the gh-pages branch
deploy:
	cd ./site/ && { git stash || true; } && { git stash drop || true; } && git pull
	@echo "Building..."
	$(MAKE) build
	cd ./site/ && git add . && \
	    git commit -m "gh-pages deployment $$(date -Iseconds)" && \
	    echo "Uploading to webserver..." && \
	    git push
