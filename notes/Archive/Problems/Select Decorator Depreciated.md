---
tags:
  - javascript
---
In NGXS the `@Select` decorator has been depreciated because of limitation Angular places putting on decorator.  The `this.store.select()` idiom should be used instead.  To convert an existing codebase to the new idiom, the following regex can be used in VS Code Find/Replace:

```
// with \n between decorator name
@Select\((.*)\)\n(.*): Observable<(.*)>;$

// single line
@Select\((.*)\)(.*): Observable<(.*)>;$
```

```
$2 = this.store.select<$3>($1);
```

This was taken from [the NGXS GitHub issue comment](https://github.com/ngxs/store/issues/1854#issuecomment-1184855647) by [lehmstedt](https://github.com/lehmstedt).