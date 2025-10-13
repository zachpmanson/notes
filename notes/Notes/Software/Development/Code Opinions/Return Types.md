---
subtitle: Functions return types should not change depending on parameters
---
Functions should return `None`, return `SomeType | None` or `SomeType` . `SomeType` can be a tuple, but that tuple should always have the same number of arguments. Flags like `calculate_cost(return_as_float=True)` should not exist. If you must have multiple versions of the same function with slightly different return signatures, I should be able to access everything in a typesafe way. This either means there should be

- `@typing.overload` decorators providing all the typesafe variants of the function
- 1 function containing the core logic and a other functions that wraps it and does type conversion (Both should have type inference or type hints.)