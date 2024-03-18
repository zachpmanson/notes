---

tags:

- relics

---
> #### 1.8: What's the `auto` keyword good for?
>
>Declaring vehicles.

-- [Infrequently Asked Questions in comp.lang.c](https://www.seebs.net/faqs/c-iaq.html)

The `auto` keyword in C is one of four storage classes a variable can have, the others being `register`, `static`, and `extern`.  Storage classes defined the scope and lifetime of variables.

>  `auto` is the default storage class for local variables. 
>  
> `register` is used to define local variables that should be stored in a register instead of RAM
>
> `static` is the default storage class for global variables
>
> `extern` defines a global variable that is visible to ALL object modules

-- [University of Queensland COMP2303 C Reference](http://web.archive.org/web/20130927234242/http://itee.uq.edu.au/~comp2303/Leslie_C_ref/C/CONCEPT/storage_class.html)

Since the `auto` class is the same as a local variable's default behaviour, there is no reason to use it.  All programs using the `auto` keyword would be identical if `auto` was omitted. 

## Why does it exist then

It is a relic from the preceeding B language,  where the `auto` keyword was required to declare local variables.  Many B programs were ported to C so the `auto` keyword was included to improve backwards compatibility, allowing programmers at the time to avoid needing to remove all auto references in their codebases.

[This thread](https://stackoverflow.com/questions/2192547/where-is-the-c-auto-keyword-used) on StackOverflow contains more details on this.