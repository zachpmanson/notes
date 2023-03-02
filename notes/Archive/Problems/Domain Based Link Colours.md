To make `<a>` tag colour depend on the domain the `href` attribute points to, you can use a CSS selector that checks from the start of the element.

```css
/* Internal links */
a[href^="/"] {
	color: purple;
}

/* Other Links */
a {
	color: blue;
}
```