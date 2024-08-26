---
tags:
  - relics
subtitle: Arrow Assignment vs. Equals Assignment
---
A post by 2011-09-02 on the differences between assignment syntax in [[R]].

---

A recent [thread](https://stat.ethz.ch/pipermail/r-help/2008-December/182730.html) on the r-help mailing list raises a common question for beginning R users: should you use = (equals) or <- (back arrow) for assignments?  In R, both of the following statements have the effect of assigning the value 3 to the variable x:

```
x = 3  
  
x <- 3
```

So if they have the same effect, does it matter which you use?

A little history before we continue: when the R language (and S before it) was first created, <- was the only choice of assignment operator.  This is a hangover from the language [APL](https://en.wikipedia.org/wiki/APL_%28programming_language%29), where the arrow notation was used to distinguish assignment (assign the value 3 to x) from equality (is x equal to 3?). (Professor Ripley reminds me that on APL keyboards there was an actual key on the keyboard with the arrow symbol on it, so the arrow was a single keystroke back then. The same was true of the AT&T terminals first used for the predecessors of S as described in the [Blue Book](https://www.amazon.com/New-Language-Programming-Environment-Analysis/dp/0534091938/ref=sr_1_1?ie=UTF8&s=books&qid=1236786811&sr=8-1).) However many modern languages (such as C, for example) use = for assignment, so beginners using R often found the arrow notation cumbersome, and were prone to use = by mistake.  But R uses = for yet another purpose: associating function arguments with values (as in pnorm(1, sd=2), to set the standard deviation to 2).

To make things easier for new users familiar with languages like C, R [added the capability in 2001](http://developer.r-project.org/equalAssign.html) to also allow = be used as an assignment operator, on the basis that the intent (assignment or association) is usually clear by context.  So,

```
x = 3
```

clearly means "assign 3 to x", whereas

```
f(x = 3)
```

clearly means "call function f, setting the argument x to 3".

There is one case where ambiguity might occur: if you wanted to assign a variable during a function call. The only way to do this in modern versions of R is:

```
f(x <- 3)
```

which means "assign 3 to x, and call f with the first argument set to the value 3".  This is a contrived example though, and never really occurs in real-world programming.  [UPDATE: In fact, constructs like this are best avoided for reasons given in the comments below.]

So, back to the original question: should you use = or <- for assignment?  It really boils down to preference.  Many people are more used to using = for assignment, and it's one less keystroke if you want to save on typing.  On the other hand, many R traditionalists prefer <- for clarity, and if you plan to share or publish your code, other might find code using = for assignment hard to read. Personally, I prefer the arrow notation, with a space on either side.

So, long story short: it's really up to you.