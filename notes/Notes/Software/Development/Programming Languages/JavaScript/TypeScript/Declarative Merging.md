Interfaces support declaration merging. If you declare an interface with the same name multiple times, they will automatically merge into one.

```ts
interface Person {
  name: string;
}

interface Person {
  age: number;
}

const person: Person = { name: "Alice", age: 25 }; // Valid
```

 Types do not support declaration merging. If you try to define the same type name more than once, you’ll get an error.

This feature seems kind of fucked. A beautiful footgun, as one of the few "advantages" of interfaces over types.

> TS is a superset of JS, and as a result they need some ways to model the dynamic-ness of Javascript. One common pattern in js was adding whatever methods to existing objects, often in plugin based systems -- express middleware that adds to the req object, custom jest assertions, or even just adding properties to the window object. Declaration merging is the only way to get those properties onto the existing object "safely"
> 
> It's a good thing to remember though that just because a language feature exists doesn't mean it should be used / abused. I would label merging as one of those that you wouldn't purposefully do in a TS codebase, only if you need to type some interop

-- [lams3b](https://www.reddit.com/r/typescript/comments/rbw0db/what_is_the_use_case_for_declaration_merging/hnqo6q7/)
