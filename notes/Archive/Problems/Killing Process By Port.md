From [StackOverflow](https://stackoverflow.com/a/32592965).

```sh
kill $(lsof -t -i:$portnum)
```