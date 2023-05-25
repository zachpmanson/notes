To include Markdown components within HTML elements within a Markdown file in Python Markdown you need to add an extension and an attribute.

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