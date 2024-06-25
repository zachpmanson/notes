## Builtins

- `$?`
	- last commands exit code
 - CLI args can be accessed using `$0`, `$1`, `$2` ..., where `$0 == programname.

	```
	ls -l
	
	$0 == ls
	$1 == -l
	```

- `$#` is the number of arguments (excluding `$0`).
- `$IFS` is the internal field seperator, which determines characters than can be used to seperate arguments
	- By default this is `<space><tab><newline>`
	- can be edited to change this
- `cd`
	- change directory
	- leave blank to go to `~`
	- `cd -` to go previous directory
		- use this repeatedly to toggle between two dirs
## Variables

Variable assignments must not use spaces.  `$` can be used to get values from variables.

```sh
varname=variablevalue
var2name="value with spaces"

echo $varname
echo "some text $varname some more"
echo 'singlequotes $dont interpolate values'
echo "can wrap ${varname} in curly backets"
```

Backslashes can be used to escape characters.

To get the value of programs into text strings, wrap the commands in brackets.

```sh
echo "the time is now $(timenow)"
```

Variables are scoped to their script by default.  They can be exported so they can accessed externally or by child processes.

```sh
export PS1
```

### Variable Expansion

Curly brackets around a variable can be used in more complex ways:

```sh
echo "can wrap ${varname} in curly backets"
echo "can use hash to get ${#varname} in length of variable"
echo "can will use word instead of parameter if parameter is undefined or null ${parameter:-word}"
```

There are more of these, see [here](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html).

## `if` statements

From [here](https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs).

```sh
if
	command-list1
then
	conditional-commands1
elif
	command-list2
then
	conditional-commands2 
else
	conditional-commands3
fi
```

The `then` clause is executed if the exit code of `command-list1` is 0. The `command-list1` can be a sequence of one or more pipelines separated by one of the operators `;`, `&`, `&&`, `||` or newline.  There are some common idioms that are special cases of this:

### `[ ]`
 
```sh
if [ condition ]
```

This is equivalent to POSIX `test`, which can do a number of comparisons and evaluations.

### `[[ ]]`

```sh
if [[ condition ]]
```

This is an upgraded variation of `test`, which can do more advanced comparisons like wildcard string comparisons. Not POSIX.

- `[[ a < b ]]` will do string comparisons, not for numbers
- `[[ a -lt b ]]` this works for numbers, similar flags for `gt, ge, le, eq`

### `(( ))`

```sh
if ((condition))
```

This performs arithmetic, with the result being the exit code of the pipeline. Not POSIX.

### `( )`

```sh
if (command)
```

This runs the command as a subshell, which can limit side effects.

## Shell Arithmetic

- not very efficient
- should put substantial computing into other languages like Awk or Python
- `$((<expression>))` will evaluate the expression and return result to stdout

Operations

- - plus  
- - minus  
- - multiplication  
- / integer division  
- % remainder  
- > > right shift (/2 N )  
- << left shift (*2 N )  
- & bitwise AND  
- | bitwise OR  
- ~ bitwise NOT  
- ^ bitwise exclusive OR  
- && logical AND  
- || logical OR  
- ! logical NOT

## Globbing

A method of wildcard matching.
- `*`
	- matches any number of characters
- `?`
	- matches a single character
- `[ <letters> ]`
	- match 1 of these letters
- `[! <letters> ]`
	- match any one letter except those in range

## `case` statements

```sh
case <expression> in
	<pattern>[ | <pattern>...]) <statements>;;
esac
```

Pattern should be a glob pattern. `*` is used as the else statement as it will match everything.

## Loops

`break` and `continue` do what you'd expect.

### `for` loop

```sh
for <name> in <list> do
	<commands>
done
```

`list` is just a list of white-space seperated strings.  Good for use with globbing and file names, or reading through textfiles, especially when used in combination with `$IFS`.

`for` loops can also use this format ([[Bash]] only)

```sh
for ((init; check; step)); do
    body
done
```

### `while` loop

```sh
while [ condition ]; do
   <command3>
done
```

## `shift`

- shifts the argument to the current script one to the left
- reduces overall arg count by one

## Functions

```sh
function name {
	<commands>
	return [<exit status>]
}
```

Use $1, $2 for parameters.  $0 is the function name.

All variables are global unless `local` keyword is when declaring variable.

## Process Substitution

Process substitution allows you to replace an input and output file arguments, for example.

```sh
diff <(hexdump file1.bin) <(hexdump file2.bin)
```

```
cat file.txt | tee >(wc -l)
```

It's similar to using temporary files but nothing gets written to disk.

I learnt of process substitution from [this thread](https://wikis.world/@LucasWerkmeister/111278908490616471) ([unrolled](https://unroller.zachmanson.com/threads/https:/toot.cafe/@LucasWerkmeister@wikis.world/111278908477654325)).