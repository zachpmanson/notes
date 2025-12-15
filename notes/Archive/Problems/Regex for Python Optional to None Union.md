For VS Code find and replace regex for [[Python]] type hints.

```
Optional\[((?:[^[\]]|\[(?:[^[\]]|\[[^\]]*\])*\])*)\]

$1 | None
```