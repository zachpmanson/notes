This displays a file and pipes it into VS Code.

```
git show $(git rev-list --max-count=1 --all -- src/components/overview/ComparisonSearchBar.tsx)^:src/components/overview/ComparisonSearchBar.tsx | code -
```

[From this](https://stackoverflow.com/a/19727752).