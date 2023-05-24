## File Permissions

Permissions have 3 kinds of access:

- r - read access
- w - write/modify access
- x - execute permission

3 user sets:

- u - user, file owner
- g - group
- o - everyone else

These are presented like this in `ls`:

```
-rw- --- ---
```


Directories are the same but are preceeded with a `d`:

```
drw- --- ---
```

Setting file permissions can be done with `chmod`  
- `chmod <octal mode> <files>`
	- silly to use this 2023 except in shell scripts, but even then
	- each group of 3 permission is views a 3 bits of an octal number
		- 100 r perm
		- 010 w perm
		- 001 x perm
- `chmod <symbolic mode> <files>`
	- `chmod <user sets><+|-><perms> <files>`
	- `chmod go+r file.txt`
	- may require multiple calls

## Input/Output

Unix views all files as characters/bytes, leaving interpretation up to the programs.

- default input is stdin (file descriptor 0), which is mapped to the keyboard by default.
- default output is stdout (file descriptor 1), which is the screen
- default error output is stderr (filedescriptor 2), which also goes to the screen
	- this allows errors to be seperately directed

### Redirection

stdin/stdout/stderr can be redirected to other files
- `<` redirects stdin to file 
- `>` redirects stdout to file
- `>>` redirects stdout to append to a file
- `2>` redirects stderr to file

### Piping

stdout/stderr can be redirected to other programs inputs, rather than files using piping.

```
date | wc
```

`|` only applies to stdout, but `2> errors |` works equivalently for errors.

## Scripts

Scripts are files that contains sets of commands on consecutive lives that can be repeatedly run.

The first line of a script says what interpreter should be used to execute the script.

```sh
#!/usr/bin/env bash
```

Script needs to be made executable

```sh
chmod u+x script.sh
```

From here [[Bash]] takes overs.