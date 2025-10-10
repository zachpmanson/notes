---
subtitle: If you do not have request validation I do not trust you
---

Do not create API endpoints that do not validate query params or request body. 
Do not create API endpoints that do not validate query params or request body.
Do not create API endpoints that do not validate query params or request body.
Do not create API endpoints that do not validate query params or request body.

If there isn’t a class definition with a Pydantic model in it or a Yup/Zod definition, ask yourself why. You better have a very good reason. This is as much for security as it is for convenience. If I can’t instantly tell what params your query needs, you have made a mistake.

This also forces you to be typesafe. Perhaps this is an extension of [[Command Click]].

```python
# BAD - No human should ever have to do this
data_type = params.get("type", None)
test_date_str = params.get("date", None)
site_id = params.get("site_id", None)
channels_str = params.get("channels", None)
last_active_price = params.get("last_active_price", None)
meter_num = params.get("meter_num", None)
identity = params.get("identity", None)
on_at = params.get("on_at", 0)
off_at = params.get("off_at", 0)
is_all_day = params.get("is_all_day", "no")
experiment_type = params.get("experiment_type", "sum")
```

