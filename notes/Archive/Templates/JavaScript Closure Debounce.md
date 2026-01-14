An elegant [[JavaScript]] debounce function, I saw [here](https://simonwillison.net/2025/Dec/27/textarea-my/#atom-everything).

```js
function debounce(ms, fn) {
  let timer
  return (...args) => {
    clearTimeout(timer)
    timer = setTimeout(() => fn(...args), ms)
  }
}

```