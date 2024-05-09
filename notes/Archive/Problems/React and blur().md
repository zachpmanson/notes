In TypeScript, for some reason, `event.target` doesn't natively have a `blur()` method.  You need to ensure that is a `HTMLElement` type.

```ts
if (element.target instanceof HTMLElement) {
    element.activeElement.blur();
}
```

[Source](https://github.com/Microsoft/TypeScript/issues/5901#issuecomment-431649653)