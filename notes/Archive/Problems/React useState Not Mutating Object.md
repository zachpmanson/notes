---
tags:
  - javascript
  - react
---

Just a footgun I ran into while working on the Threadlet dashboard.

If you do the following it will not work as expected:

```ts
function f() {
	const [a, setA] = useState({x: 1 , y: 2})
	setA((old) => {
		old.x = 4
		return old
	})
}
```


You should always return a wholly new object.

```ts
function f() {
	const [a, setA] = useState({x: 1 , y: 2})
	setA((old) => {
		n = {...old, x: 4}
		return n
	})
}
```