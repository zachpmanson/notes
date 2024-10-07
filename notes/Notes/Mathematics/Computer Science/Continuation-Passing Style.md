> In functional programming, continuation-passing style (CPS) is a style of programming in which control is passed explicitly in the form of a continuation. This is contrasted with direct style, which is the usual style of programming

-- [Wikipedia](https://en.wikipedia.org/wiki/Continuation-passing_style)

A function **foo** written in CPS style takes a callback **bar**, and **bar** is executed as the return value of **foo**.  The callback **bar** is called a *continuation* function. The continuation function is a tail call.

## Gleam

Gleam has an interesting syntactic sugar around this pattern with the `use` keyword:

```
// standard callback
f(a, fn(b) { g(b) })

// with use
use b <- f(a)
g(b)
```

Sort of an inverted callback.  A callback function  is a function definition stored in variable for later execution when its arguments have been computed; CPS stores a set of arguments that can be bound to a function, and that function will be executed when the arguments are calculated.