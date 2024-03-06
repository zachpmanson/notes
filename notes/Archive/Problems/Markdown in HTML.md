---
tags:
  - python
---

To include [[Markdown]] components within HTML elements within a Markdown file in Python Markdown you need to add the (official) extension [Markdown in HTML](https://python-markdown.github.io/extensions/md_in_html/#markdown-in-html "Permanent link") and an attribute.

```python
html_content = markdown.markdown(
	text.content,
	extensions=['md_in_html']
)
```

```html
<details markdown="1">
    <summary markdown="block">
		## Appendix: Some Generative Art
	</summary>
	
	Some images I generated with DALL·E:

	![](./lemur-pears.png)

	![](./cyberpunk-toadstool-explodes.png)
</details>
```

"1" uses the default behaviour of the element, "block" forces it to use block behaviour on the contents of the element, and "span" forces the element to use span behaviour on its contents.