[Rich Harris' bug report](https://github.com/sveltejs/svelte/issues/11052) on his own framework.

---
### Describe the bug

I'm a little shaken up. For as long as I've been programming, I thought that this...

```html
<div />
```

...was shorthand for this:

```html
<div></div>
```

[It turns out it's not.](https://jakearchibald.com/2023/against-self-closing-tags-in-html/) Self-closing tags just aren't a thing in HTML — the `/>` is simply ignored by browsers altogether. In other words, this...

```html
<div />hello!
```

...is equivalent to this — the `hello!` is _inside_ the div, not outside it:

```html
<div>hello!</div>
```

Svelte, however, treats `<div />` as `<div></div>`. For a framework that prides itself on being a superset of HTML, this is a glaring error.

## What should we do?

I think the right thing to do is ~~disallow~~ (_edit_: warn on) self-closing non-void HTML tags (this only applies to HTML, not other namespaces). This is a breaking change, but the alternatives are:

1. Continue to parse HTML incorrectly
2. Parse HTML correctly, treating `<div />` as `<div>`, which is also a breaking change but one that would be nightmarish to debug

Ideally we would also disallow self-closing void elements (i.e. `<input>` rather than `<input />`), but whether or not this is realistic depends on whether Prettier's current habit of adding an unnecessary `/>` to void elements prevents us from doing that.

### Reproduction

Navigate to `about:blank`, and do this:

```js
document.body.innerHTML = `<div />hello!`
console.log(document.querySelector('div').textContent);
```

Then, in a Svelte component, do this:

```svelte
<script>
  import { onMount } from 'svelte';

  let div;
	
  onMount(() => {
    console.log(div.textContent);
  });
</script>

<div bind:this={div} />hello!
```

In the first case, 'hello!' is logged. In the second case, the empty string is logged.

### Logs

_No response_

### System Info

```shell
This currently applies to all versions of Svelte
```

### Severity

annoyance