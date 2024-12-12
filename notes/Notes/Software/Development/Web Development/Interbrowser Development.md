For the most part browsers and their APIs are cross compatible, but there are a few differences that need to be paid attention to.

## Clipboard API

*As of 2024-09-04*

Firefox and Chrome have different permission requirements to access the clipboard. I think Firefox is more standards compliant here?

## Currency Formatting

*As of 2024-12-12*

```js
const formatted = `${amount.toLocaleString(undefined, {
	style: "currency",
	currency: "AUD",
})}`;
// In Firefox when in Australia: $10.00
// In Chrome when in Australia: A$10.00

const formatted = `${amount.toLocaleString("en-AU", {
	style: "currency",
	currency: "AUD",
})}`;
// In Firefox when in Australia: $10.00
// In Chrome when in Australia: $10.00
```