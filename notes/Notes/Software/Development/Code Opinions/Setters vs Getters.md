---
subtitle: "`@property` getter should not have logic"
---

I know that it looks pretty for `def method(self): return f"{self.first_name} + {self.last_name}"` to be `User.full_name` rather than `User.full_name()`, but the bigger impact is obscuring the fact that you are making a function call. 

The power of `@property` is not the getter, but the setter.

You can define a custom setter with validation logic OR
You can intentionally leave out a setter so that an attribute is read only:

```python
class X:
	_name = 5
	@property
	def name():
		return self._name
```

If you are not doing either of these things, property is just hiding a function call, which is a practice I consider dangerous. I have seen prosebit hide network calls behind @property. Never do this.
