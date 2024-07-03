XML has the concept of self-closing tags, where a tag can end with a `/` and then omit its closing tag, containing no content beyond the tag name and attributes. While it share a lot of DNA with XML, HTML doesn't actually support self closing tags, ignoring any slash at the end of a tag. These pairs are all semantically identical.

```html
<br>
<br />

<img>
<img />

<div>
<div />
```

That the first two are HTML void tags, meaning that they do not need a closing tag, so self-closing the tag is just a style choice. The last one is a problem, since `div` is not a void tag.  This is the problem that was discovered by Rich Harris in his issue [[Svelte parses HTML all wrong]].

I cannot imagine a sane human who would intent for `<div />` to mean "the start of a div", and I don't not think we should enable this.  Ideally I would want warnings or errors to appear in all cases where this would matter.

An interesting detail is that the general way self-closing tags are used in HTML is slightly different from in XML. XML traditionally does not put a space before the closing tag.

```html
<xmltagname/>

<htmltagname />
```

> In XML, it would generally be formatted like `<this/>`, without the space before the `/`, but Netscape Navigator 4 couldn't cope with `<input type="text"/>`, where the `/` immediately followed an attribute, so the spec recommended a space before the `/`.

-- [The case against self-closing tags in HTML](https://jakearchibald.com/2023/against-self-closing-tags-in-html/)

This style difference is still present to this day, even in HTML derivations that do not require it like JSX.