xp>Unix is user-friendly — it's just choosy about who its friends are.

-- The Art of UNIX Programming (2003) by Eric S. Raymond

Created in 1969 at AT&T Bell Labs to run on departmental computers for the PDP-11.  It used 16-bit words and had 64KiB/128KiB RAM.

It was initially written in ASM, but sparked the creation of C which was designed to make Unix development easier.

## Philosophy

* smaller kernel, a master process which provides services to system and user processes
* a simple datatype (text) and simple interprocess communication 
  * allows chaining of processes
* seperation between ordinary users and superusers using privileges
* files 
  * almost everything is a file 
    * processes are files
    * directories are files that point to other files
  * files are just sequences of bytes

## Basics

* filenames 
  * extensions are conventional, not required
  * filenames can be any non-whitespace character (sus)
  * current dir is `.`, parent is `..`
  * dotfiles are hidden
* commands 
  * `<commandname> [<options>] [<objects>]`
* shell 
  * the program that handles command interpretation
  * shell locates commands and objects
  * you can chain commands into shell scripts 
    * first was Bourne Shell `sh` in 1976
    * followed by [[Bash|Bourne Again Shell]] `bash` in 1989
    * Korn Shell `ksh` in 1983

## Environment Variables

Environment variables are defined by the system and will be will be passed to the shell.

* system path is stored in env var `PATH`, list of dirs seperated by `:`, usually contains the following paths 
	* `/bin` 
		* top level system commands
		* `cat`, `echo`
	* `/usr/bin` 
		* system level commands that generally come with the system but may need to be installed
		* `python`, `gcc`
		* `usr` stands for Unix System Resources
	* `/usr/local/bin` 
		* programs that you have installed for all users of your system locally
		* `pip3`, `ps2pdf`
	* `~/bin` 
		- a users programs
	* `.`
		* current directory
* `CDPATH` 
	* all locations that cd can direct you to
	* similar to `PATH`
* `PS1` 
	* shell prompt text
* `umask 077` 
	* permissions applied to files on creation

More environment variables can be setup in the `~/.profile` executable.

