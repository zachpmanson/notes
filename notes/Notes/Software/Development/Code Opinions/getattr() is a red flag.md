
The only time I can think you might want to use this is when we have split table that share parent super class e.g. `BaseUsage`, `Usage`, `GasUsage`, `LPGUsage` . 

(to be fair, I believe that we generally want to avoid needing that kind of abstraction in the future)

Other than that, why do you need `getattr()` ? Is there a better way of referencing the attribute, that doesn’t break VS Code type inference?

Reflection is powerful and also may be a sign you’ve gone too far.

This is cursed, do not do this:

```python
...
    def per_day_metric(self, metric: Literal["spend", "rev", "client_saved", "usage"] = "spend", **kwargs):
        if metric == "spend":
            return getattr(self, "per_day_spend")(**kwargs)
        else:
            return getattr(self, f"per_day_{metric}")
...