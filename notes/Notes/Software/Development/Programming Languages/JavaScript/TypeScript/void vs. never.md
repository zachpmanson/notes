> - A function that doesn't explicitly return a value **implicitly returns** the value `undefined` in JavaScript. Although we typically say that such a function "doesn't return anything", it returns. We usually ignore the return value in these cases. Such a function is inferred to have a `void` return type in TypeScript.
> - A function that has a `never` return type **never returns**. It doesn't return `undefined`, either. The function doesn't have a normal completion, which means it throws an error or never finishes running at all.

-- [Marius Shulz](https://mariusschulz.com/blog/the-never-type-in-typescript#the-difference-between-never-and-void)

> Another important difference between `void` and `never` is how they interact with other types. `void` can be used as the return type for functions that return `undefined`, while `never` can be used as the return type for functions that throw errors or have infinite loops. However, `void` cannot be used as a subtype of other types, while `never` can be used as a subtype of all types.

-- [Sumit Kumar Singh](https://designtechworld.medium.com/never-vs-void-in-typescript-understanding-key-differences-1e5e22c57ea8)