---
subtitle: Only use a getter when you care about the setter
---

I know that it looks prettier when the getter is simple:

```python
class User:
	first_name: str
	last_name: str
	
	def full_name_1(self):
		return f"{self.first_name} + {self.last_name}"
		
	@property.getter
	def full_name_2(self):
		return f"{self.first_name} + {self.last_name}"


User.full_name_1
User.full_name_2()
```
 
but the bigger impact is obscuring the fact that you are making a function call.

The real power of `@property` is not the getter, but the setter.

You can define a custom setter with validation logic OR
You can intentionally leave out a setter so that an attribute is read only:

```python
class X:
	_name = 5
	@property.getter
	def name():
		return self._name
```

If you are not doing either of these things, property is just hiding a function call which may contain side effect, which is a practice I consider dangerous. I have seen network calls hidden get behind @property. Never do this.
