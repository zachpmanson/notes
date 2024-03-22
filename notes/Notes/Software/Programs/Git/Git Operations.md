---
tags:
  - git
---

## New Computer

Setting global [[Git/Git]] config options:

```sh
git config --global user.name "name"
git config --global user.email "email"
```

Setting the `git lola` alias:

Add the following to `~/.gitconfig`.

```
[alias]
	lol = log --graph --decorate --pretty=oneline --abbrev-commit
	lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
[color]
	branch = auto
	diff = auto
	interactive = auto
	status = auto
```

## Mistakes

Amend last commit with current changes:

```sh
git commit --amend --no-edit
```

Reset N commits:

```sh
# soft
git reset HEAD~N
# hard
git reset HEAD~1 --hard
```

## Checkout Branch from GitHub Fork

```sh
git remote add coworker https://path/to/coworkers/repo.git
git fetch coworker
git checkout --track coworker/foo

# then in future
git checkout foo
git pull
```

From this [answer on StackOverflow](https://stackoverflow.com/a/5884825).

## Checkout Switch

Switching to `-` will switch you back to the previous branch, similar to `cd -`.

```
git checkout main
git checkout develop
git checkout -
git checkout -
```
