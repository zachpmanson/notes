---
subtitle:
---
Immutability in calculations is so so so much easier to reason about. Unless there are hardware/performance constraints, err towards immutability.

For any given function, you do not have to worry about your objects being mutated, only the return value of the function. All the logic that matters to the function you are looking at is within the function itself.