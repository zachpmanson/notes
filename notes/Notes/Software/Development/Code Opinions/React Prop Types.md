---
subtitle: React prop type definitions should be inline and anonymous
---

Unless you have a good reason. Only example I can think of is components sharing props (this is rare) or interface perf vs type perf (but I am yet to work on a codebase where that mattered).

```tsx
// BAD
type ComponentAProps = { 
  a: string;
  b: string;
}
function ComponentA({a, b}: ComponentAProps) {
	return <>{a} {b}</>
}

// BAD
function ComponentA(props: {a: number; b: string}) {
	const {a, b} = props;
	return <>{a} {b}</>
}

// I CAN LIVE WITH THIS BUT YOU'RE WEIRD
function ComponentA(props: {a: number; b:string}) {
	return <>{props.a} {props.b}</>
}

// LITERALLY THE WORST OF BOTH WORLDS YOU MASOCHIST
type ComponentAProps = { 
  a: string;
  b: string;
}
function ComponentA(props: ComponentAProps) {
	const {a, b} = props;
	return <>{a} {b}</>
}

// GOOD
function ComponentA({a, b}: {a: number; b:string}) {
	return <>{a} {b}</>
}
```

It is extremely rare that you need to use prop type definitions more that once, so the separate type definition is just adding boilerplate with no benefit. Yes I know that its annoying repeating the same thing twice in a row with the anonymous type, but its the best of a bunch of bad options. It should be maximally obvious what params a component needs.

Generally its good to keep types as close to their usage as possible.