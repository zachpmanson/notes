Being able to run a text search over a codebase is extremely valuable. This is especially true at API borders (service boundaries), where one project will call another project and you need to switch codebases to find where that API definition is. Often the only decent way to find the relevant function in these circumstances is string matching (or extremely consistent file structures which we currently do not have).

If I am in [Frontend](https://www.notion.so/Frontend-1a6657e5d53f4e01a6d97ed8b30ab276?pvs=21) and I can see some data is coming from an API called `GET /api/client/foo/bar` it is much quicker for me to track down the API definition with a search for `"client/foo/bar"` than any other method. So [Backend](https://www.notion.so/Backend-ec9cc4fb92eb42e5966fc492b5b83acb?pvs=21) will need to have `"client/foo/bar"` as a full string.

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