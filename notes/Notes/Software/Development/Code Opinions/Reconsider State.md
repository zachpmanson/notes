---
subtitle: It is extremely unlikely that your calculation needs state
---

Do you have some numbers and you need them to turn into some other kinds of numbers? [[Avoid State]]. When I say state, I don't mean a short lived variable to store a value before you loop over something, I mean a class attributed that is mutated in X number of times across different methods.

A good rule of thumb is "all stateful variables this function uses should be declared within this function and all mutations should be visible by reading this function"
