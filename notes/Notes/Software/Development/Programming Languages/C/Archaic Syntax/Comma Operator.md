Comma is an operator than can be applied to expression in C, where the first argument is evaluated and then ignored, and the second value is returned.

```
int a = (1, 2);
// a == 2

int b = (a+1, a);
// b = 3
```

It is analogous to a semicolon, separating expressions rather than statements.  It has the lowest precedence of any C operator.

It has few uses, such as:

- being passed into macro function substitutions to allow multiple expressions where only 1 would normally be usable
- in a `for`/`if` block condition where a preceding operation is necessary and block scoping is desired 

Thanks to its inclusion in C, is persists in C++ and [[JavaScript]]