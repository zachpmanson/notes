A manifesto by Oliver Russell, [posted on 2023-02-23](https://leontrolski.github.io/cmd-click-manifesto.html).

---

*Or CTRL-click or META-click or whatever.*

1. Being able to CMD-click through code >> any other theoretical concerns.
2. CMD-clickability is the opposite of indirection - _how does this function work?_ CMD-click it.
3. Non-CMD-clickable codebases are filled with non-meaningful abstractions and tend to be longer.
4. Static analysis tooling should be easy to write.
5. Stack traces should correspond with the structure of the code.
6. Higher order functions break the golden property, use them as a last resort.
    
    ```python
    def do_something(data, f: Callable[...]):
        f(data)  # I can't CMD-click f
    ```
    
7. Trad Object Orientated code tends to break the golden property (this makes sense as [objects are closures](https://leontrolski.github.io/poor-mans-object.html#:~:text=objects%20are%20a%20poor%20man%27s%20closures%20are%20a%20poor%20man%27s%20objects)), use it as a last resort.
    
    ```python
    def do_something(a: Animal):
        a.meow()  # I can't CMD-click meow
    ```
    
    _This case it is ambiguous as `meow()` could be on any `Cat`, `Lion`, `Tiger`..._
8. Use enum-like information to distinguish between otherwise similar data.
    
    ```python
    class Cat(Animal): ...                # bad
    a = Animal(kind=AnimalKind.CAT, ...)  # good
    ```
    
9. Serializable enum-like [discriminants](https://basarat.gitbook.io/typescript/type-system/discriminated-unions) in data can be trivially plonked into databases, regurgitated via JSON, etc.
10. Choose behaviour based on data, not class hierarchies:
    
    ```python
    def do_something(data):
        if data.kind == Kind.A:
            g(data)  # I can CMD-click g
    ```
    
11. Say arbitrarily complicated things about data, rather than be constrained by inflexible heirarchies.
    
    ```python
    class Cat(Animal, FourLegged): ...                  # bad
    def has_even_number_of_legs(a: AnimalKind) -> bool  # good
    ```
    
12. Strong typing aids CMD-clickability, this property of typing is more valuable than correctness.
13. Microservices in and of themselves are not bad, however:
    1. Construct your codebase such that CMD-clicking _across_ a service boundary is as easy as _within_ a service.
    2. Typecheck service boundaries as you would any other code.
    3. Use correlation ids and a [Datadog](https://www.datadoghq.com/blog/request-log-correlation/)-like tool to make cross-service stack traces comprehensible for debugging production.
14. Where you might have to fall back on grepping - make it easy, use full literals:
    
    ```python
    @app.route(PREFIX + "/v1/add")          # bad
    @app.route("/payments/inbound/v1/add")  # good
    ```
    
15. Good code expresses the smallest possible state space the program could operate in - **YAGNI**.
    
    ```python
    def do_something(data, f: Callable[...]):
        # f could be anything - big state space
        f(data)
    
    def do_something(data, kind: Kind):
        # we enumerate the specific things we can do - small state space
        if kind == Kind.A:
            g(data)
        ...
    ```
    
16. Lean in on language features, don't introduce [unnecessary](https://github.com/gcanti/fp-ts) [abstractions](https://github.com/ingolemo/python-lenses).
17. There exists deep library code where we want to allow consumers to do anything (extensibility). In application development, this is the exception - you have control over the whole codebase, the code by its nature is extensible.
18. Ignore this manifesto sooner than code anything outright barbarous.