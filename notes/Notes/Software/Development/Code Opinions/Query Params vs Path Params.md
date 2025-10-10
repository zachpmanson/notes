---
subtitle: Prefer query params/request body to URL params
---

Putting variables into the URL path is inflexible and makes parsing things quite confusing. Query params are much easier to change down the line.

```bash
# BAD
/api/sites/<site_id>/<energy_type>/<time_resolution>
/api/sites/102/elec/monthly

# GOOD
/api/site?site_id=<site_id>&energy_type=<energy_type>&resolution=<time_resolution>
/api/site?site_id=102&energy_type=elec&resolution=monthly
```

Slightly unrelated, but also note that DELETE endpoints can only have query params, not a JSON body. Isn't that strange.