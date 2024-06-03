## Variables

Uses sigils for scoping.   This is just a language convention, but libraries often provide names based on these patterns so they are effectively language features.

- `x` is a local variable (or something other than a variable).
- `$x` is a global variable.
- `@x` is an instance variable.
- `@@x` is a class variable.

Uses sigils for typing sometimes. This is just a convention I think.

- `varname?` means boolean
- `action!` means potentially dangerous?

`:name` is a "symbol".  Symbols are immutable values where any two symbols given the same name will be identical. Makes comparisons quicker since its just a pointer check.  [More details](https://stackoverflow.com/questions/6337897/what-is-the-colon-operator-in-ruby0).

## Blocks

`begin`/`rescue` blocks are similar to `try`/`catch` blocks in other languages.

```ruby
begin
  # Code that may raise an exception
rescue SomeException => e
  # Handle SomeException
rescue AnotherException => e
  # Handle AnotherException
else
  # Code to run if no exceptions occurred
end
```

You can omit `begin` if you attach the `rescue` block to a method

```ruby
  def authenticate_jwt
    token = request.headers['Authorization'] || ''
    token = token.delete_prefix('Bearer ')

    @jwt_payload = JWT.decode(token, nil, false).first
  rescue JWT::DecodeError
    head(:unauthorized)
  end
```

## Misc Syntax

`::` is used to access values from a namespace.

```ruby
NameOfNamespace::Child

# force usage of global namespace
::Time.zone.now
```