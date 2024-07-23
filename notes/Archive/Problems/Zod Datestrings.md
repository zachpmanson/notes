To make zod only accept valid datestrings (YYYY-MM-DD), use:

```js
const schema = z.object({
  date: z.string().pipe(z.coerce.date()),
})
```