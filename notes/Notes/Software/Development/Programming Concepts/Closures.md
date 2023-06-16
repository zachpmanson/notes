Closures are local variable scopes that can persist even after code execution has moved outside of the original block.  As long as a reference to the persisting scope is present in the external code execution context, variables from that scope can be accessed.  This allows functions to be portable and used in ways they otherwise cannot.

Example from [this excellent StackOverflow answer](https://stackoverflow.com/a/7464475).

```javascript
outer = () => {
  let a = 1;
  let inner = () => {
    console.log(a);
  }
  return inner; // this returns a function
}

let fnc = outer(); // execute outer to get inner 
fnc();
```

Languages that support closures usually have garbage collection, as languages that "run-time memory model allocates all automatic variables on a linear stack" (see [Wikipedia](https://en.wikipedia.org/wiki/Closure_(computer_programming)#Implementation_and_theory)) will deallocate locally scoped pointers automatically.  Languages that support closures include JavaScript, Python and Swift.  Other languages are capable of emulating this behaviour with similar such as anonymous inner classes in Java <8 (closures were added with lambda functions in Java 8).