## New Computer

Setting global git config options:

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

