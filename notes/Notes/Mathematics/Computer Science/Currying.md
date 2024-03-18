> In [[mathematics]] and [[computer science]], currying is the technique of translating a function that takes multiple arguments into a sequence of families of functions, each taking a single argument.

-- [Currying on Wikipedia](https://en.wikipedia.org/wiki/Currying)

Here's some currying in Python:

```python
def f(a,b,c):
	return a * b * c

def fA(a):
	def fB(b):
		def fC(c):
			return f(a,b,c)
		return fC
	return fB


fA(1)(2)(3) == f(1,2,3)

f_2 = fA(1)

f_2(3) == f(1,2,3)
```

There are many contexts where only single argument functions can be used.  Currying allows multi-argument functions to be used in these contexts.

Currying is named after Haskell Curry, though the concept was first developed by Moses Schönfinkel.