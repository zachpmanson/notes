Tests that mock many things are fragile. It will be unavoidable that you will need to mock side effects ([[Avoid Side Effects]]) such as network calls, but every mocked function is something that can (will) break in the future, likely in a way that is hard to detect.

I have seen far too many unit tests that boil down to "call function A, mock all the functions that function A calls". Tests like this are shallow, and will not last.

When you [[Favour Immutablility]], your functions become easier to reason about, and often easier to test, since you have fewer side effects and your test can validate the return object.