When programs conclude they return an exit status.

 - 0 is success, else is failure
 - positive integers represent an error state, usually 1 is used
 - in [[Bash]], `$?` can be used to access last commands exit status

A helpful resources outside of man pages:

- [tldr.sh](https://tldr.sh/)
	- web client [tldr.inbrowser.app](https://tldr.inbrowser.app/)

## Useful Programs
 
- `apropos <search>`
	- searches man page titles
- `cut [-d <delim>] -f <fields to remain> <files>`
	- takes ASCII structured file seperated by a delimiter like `TAB` and cut returns the fields indicated 
	- `cut -d "," -f 1,5-7 datafile.csv`
- `paste [-d <sep>] <files>`
	- steps through multiple files in parallel
	- delimiter is what seperates each line from each file e.g.
- `tr <options> <string1> <string>`
	- converts characters in first string to characters in the second string
	- takes from stdin
	- `-c` complement the first string
	- `-s` squeeze character repetitions of string1 characters into a single occurance ("####" -> "#")
	- `tr '[A-Z]' '[a-z]' < file.txt`
- `comm [<output options>] <file1> <file2>`
	- two sorted files are compared, 3 columns are produced
	- col 1 contains only lines unique to file1
	- col 2 contains only lines unique to file2
	- col 3 contains common lines
	- `-1` suppress col 1
	- `-2` duh
	- `-3` duh
- `uniq <file>`
	- compresses adjacent repeated lines into a  single line
	- `-c` outputs the counts of the number of copies
- `sort [options] <file>`
	- outputs to stdout
	- `-u` removes duplicate entries
	- `-t <char>` used as field seperator, `TAB` is default
	- `-k` can sort on a particular column of structured file
- `basename /path/file.txt`
	- strips the directory and file extensions from a path
- `grep [options] <pattern string> <file>`
	- searches for patterns in one or more files
	- returns matches to stdout
	- returns 0 on successful find, else 1
- `test <expression>`
	- does conditional checks for a number of common operations
	- some examples
		- `-e FileName` FileName exists
		- `-b Filename` Returns a True exit value if the specified FileName exists and is a block special file
		- `-c FileName` - FileName is a character special file
		- `-d FileName` FileName is a directory
		- `-f FileName` FileName is a regular file
		- `-g FileName` FileName's Set Group ID bit is set
		- `-h FileName` FileName is a symbolic link
		- `-k FileName` FileName's sticky bit is set
		- `-L FileName` FileName is a symbolic link
		- `-p FileName` FileName is a named pipe (FIFO)
		- `-r FileName` FileName is readable by the current process
		- `-s FileName` FileName has a size greater than 0
		- `-t FileDescriptor` FileDescriptor is open and associated with a terminal
		- `-u FileName` FileName's Set User ID bit is set
- `find [options] <path> [<expression>]`
	- recursively searches for file patterns
	- `-name <pattern>` test file name matches pattern
	- `-type <c>` type of file is specified by `d/f/l`
	- `-newer <file>` test file has been accessed more recently than `<file>` was modified
	- `-print` prints the full path name of file
	- `-exec <command>` execute command on all files found (like JS `.map()`) 
		- command terminated with `\;`
		- `{}` refers to file found
	- `-ok <command>` same as command except user is prompted first
	- `-perm <mode>` finds only files with certain permissions
		- `mode` can be octal or symbolic
- `diff <file1> <file2>`
	- shows the differences between to files
- `grep [<options>] <regex> <file>`
	- `-i` case insensitive
	- `-n` prepend numbers of matching lines
	- `-v` invert match so only non-matching lines reported
- [[sed]]