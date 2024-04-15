---
tags:
  - react
  - nextjs
---
When changing query params, you can use a shallow push to avoid the page scrolling to the top.

```ts
router.push({ query: { mode: newTab } }, undefined, { shallow: true });
```