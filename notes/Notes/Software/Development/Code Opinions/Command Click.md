---
subtitle: If my editor can't tell me what type a variable is, someone has messed up
---

This means that inputs need type hints, and outputs can hopefully be type inferred.

 In [[Python]] especially this is frustrating because many libraries do not provide comprehensive type definitions that are automatically assigned (looking at you SQLAlchemy v1.4). This means you will have to  annotate yourself.

Life is so much better if you do this. For everyone involved. Turn on Pyright type checking, get angry when you see red squiggles.

```python
# VERY BAD
async def run(self, params={}):
	pass
```

Python makes `@dataclasses` and `TypedDict` (or better yet, Pydantic) really easy to use, I recommend them highly.

Further reading: [The CMD-Click Manifesto](https://leontrolski.github.io/cmd-click-manifesto.html)