Make is a language/program that is designed to simplify compiling and linking C programs by automating the process and only recompiling files that have actually been modified.

Need to have `Makefile` in the project, run with `make` command.

Has 2 kinds of components, rules and variables.

## Rules

```make
<target(s)>: <prerequisites>
	<commands>
```

Can have multiple targets seperated by spaces, but don't.
Commands appear on successive lines, beginning with TAB.

## Variables

```make
<name> = <string>
```

Use `$( )` to insert the value into rules.

`%` is the equivalent of `.*`.

## Built-ins

- `$@` - target
- `$<` - first precondition
- `$^` - a list of all preconditions (space seperated)
- `$*` - wildcard pattern match result

## Special Targets

There exist targets that are not compiled but useful for other purposes.

`.PRECIOUS` allows files to be ignored when cleaning up intermediate files.  Useful for keeping files that are heavy to compute.

## Invokation Args

- `-j <N>` makes N targets run in parallel
- `-k` continue even if errors occur