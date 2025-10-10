Being able to run a text search over a codebase is extremely valuable. This is especially true at API borders (service boundaries), where one project will call another project and you need to switch codebases to find where that API definition is. Often the only decent way to find the relevant function in these circumstances is string matching (or extremely consistent file structures which we currently do not have).

If I am in frontend and I can see some data is coming from an API called `GET /api/client/foo/bar` it is much quicker for me to track down the API definition with a search for `"client/foo/bar"` than any other method. So backend will need to have `"client/foo/bar"` as a full string.

```python
# BAD
router = APIRouter(prefix="/v1/usage-test")

@router.get("/result-calculation")
async def get(request: Request):
    ...
    
# GOOD
router = APIRouter()

@router.get("/v1/usage-test/result-calculation")
async def get(request: Request):
    ...
     
```

Further reading: https://morizbuesing.com/blog/greppability-code-metric/