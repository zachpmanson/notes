sed (stream editor) is an editing language for manipulating text files.  It performs editing on the fly, intended to work as part of Unix pipelines that reads lines one by one from files.  It performs functions on lines and sending the lines to stdout. Functions are applied sequentially, and they accumulate in complexity quickly.  Breaking it up into smaller scripts can keep the complexity down.

## Syntax

`sed <options> <file>`

- `-e <sed operation>` a single edit to apply to the file(s), can have multiple `-e` calls
- `-f <file of sed ops>`
- `-n` transformed output not send to stdout

## Inline

Simple actions can be specified inline using `-e`.

```sh
sed -e "s/[()]/ & /g" -e "s/ */ /g*" file.txt
```

This places places a space around all occurrences of `(` and `)`.

`g` means global, applies to every instance on the line rather than just the first of every line.

This is tedious

## Script

Can put text manipulations into a sed script invoked with `-f`.  Comment lines begin with `#` 

Command format:
```
[<address>[, <address>]] <function> [<args>]
```


## Addresses

Addresses are a range of lines to apply the function to. Without an address, the function is applied to all lines.

```
<address><op>
42p
```

```
<address>,<address><op>
50,100p
```

`!` inverts the selection.

```
!30p
```

Address variants:

- line num
- `.` current line
- `$` last input line
- `0` before first line
- context address specified by regex
- simple arithmetic on an address

## Commands

- regex replacements `s/<regex>/<replacement>/[g]`
	- `g` make it global
	- `&` in replacment means "the entire captured text"
- delete `d`
- print `p`
	- must be used with `-n`
- print (include  non-printables and fold lines) `l`

