Awk, named for its creators and for the animal the auk, is a little language.
It has a few variants.

- AWK - Bell Labs, 1977
- Gawk - [[GNU]] awk, 1988
- Nawk - New awk, 1993
- Mawk - Mark Brennan's awk intepreter, in Ubuntu

A view of pattern action rules that are applied to lines from an input file.

Awk rules are put into an awk script or embedded to commands.  Syntax is based on C.  Where [[sed]] operates on lines, awk operates on fields in lines.

## Rules and Fields

A rule is 1+ awk statements  enclosed in parentheses `{ }`, which can be preceded by a pattern to filter lines.  Rules without patterns are applied to all lines.

awk regards input lines as a sequence of split on field seperators, by default space or tab.

- `$0` is whole line
- `$1` is first field, etc

### Special Rules

`BEGIN {<actions>}` is executed before first line is read
`END {<actions>}` is executed after last line is read

## Gawk command options

- `-F <char>` set char to be field seperator
- `-f <file>` takes rules from the file
- `-v <variable>=<value>` create a variable

## Variables

- type depends on usage
- string is default, intial value is `""`, sometimes casted to 0
- can be used just by invoking name, no `$` required 

Built in vars:

- ARGC Command-line argument count  
- ARGV Array of command-line arguments  
- FILENAME Name of input file (there may be several)  
- FNR Index of line in current file  
- FS Input field separator (default blank, tab)  
- NF Number of fields in the current line  
- NR Index of current line (from start of first file)  
- OFS Output field separator (default blank)

Assignment returns the value like C.  Also has compound assignment like C, `+=`, `-=` etc.

## Arithmetic

- has + - \* / % ^ ++x x++
- better than [[Bash]]
- has some maths functions, sin/cos/tan

Uses `;` to seperate commands, double quotes for strings.

## Commands

- `print [expression list] [> <expression>] | [| <expression>]`
	- without expression, prints `$0`
	- options `>` will pipe to file
	- expression must eval to string
	- you can pipe to other shell commands with the `|`

## Conditionals

`[<test>] {<statements>}`

Prefixing a set of actions with a test which

## Loop

Uses C style for loops.

```awk
for (i=0; i < 10; i++) {
	<statements>
}
```



## Functions

### Built-in Functions

- `length(<string>)`
- `substr(s,m,n)` - equivalent to `s[m:m+n]`
- `sprintf(fmt, expr)` - like `printf` but returns rather than prints
- `sub(r,t,s)` - sub t into s for first occurance of regex r
- `gsub(r,t,s)` - `sub()` but global
- `system(cmd)` - shell out, useful for things like [[Bash]] `sort`
- `printf()` - its like C
	- `%[<output width>[.<precision>]]<format letter>`
	- format letters:
		- c - char
		- s - string
		- d - int
		- e - scientific (default 6 decimal places) 
		- f - float (default 6 decimal places)
		- g - e or f, whichever is shorter with 0 removed

### User Defined Functions

```awk
function name(arg1, arg2) {
 # pretty straightforward
}
```

All awk variables are global **except function parameters.**

Scalar parameters are all pass by value, arrays are pass by reference.

## Conditional Rules

```awk
<condition> { <rules> }
NF == 4 {print NF}

# use ~ for regex comparison
$3~/^8/ {print}
```

`BEGIN` and  `END` are merely special cases of this.  Standard C comparison syntax otherwise applies. `~` for regex and `!~` for inverse regex.

## Arrays

Arrays are actually just dictionaries.  Awk will fill in gaps with undefined if you assign to a high number.  Elements can be deleted with `delete arr[5]`.

You can test key inclusion using `k in arr`.  Is equivalent to `arr[k] != ""`.

Can traverse array with `for (k in arr)`.  Array order is not guaranteed.