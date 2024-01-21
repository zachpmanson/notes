

Why doesn't React Native use JSX?  From a [GitHub issue on React Native TypeScript transformer](https://github.com/ds300/react-native-typescript-transformer/issues/46).

---

**[henrikra](https://github.com/henrikra)** commented [Feb 19, 2018](https://github.com/ds300/react-native-typescript-transformer/issues/46#issue-298217181)

I noticed from JSX [docs](https://www.typescriptlang.org/docs/handbook/jsx.html) that JSX has also option `react-native` for it.

Here are all three different modes for JSX

> TypeScript ships with three JSX modes: preserve, react, and react-native. These modes only affect the emit stage - type checking is unaffected. The preserve mode will keep the JSX as part of the output to be further consumed by another transform step (e.g. Babel). Additionally the output will have a .jsx file extension. The react mode will emit React.createElement, does not need to go through a JSX transformation before use, and the output will have a .js file extension. The react-native mode is the equivalent of preserve in that it keeps all JSX, but the output will instead have a .js file extension.

So why `react-native-typescript-transformer` is telling us to configure JSX to `react` instead of `react-native`. Are there some drawbacks etc? :D

---

**[ds300](https://github.com/ds300)** commented [Feb 19, 2018](https://github.com/ds300/react-native-typescript-transformer/issues/46#issuecomment-366646702) 

Hi Henrik,

Good question! I agree, the situation is a little confusing, ~~and the reason for it is historical rather than technical.~~ the reason for it is both historical and technical.

When React first appeared on the scene, most JS tooling was not compatible with the JSX syntax. To mitigate this, people would only put JSX syntax in files with the extension `.jsx`. Eventually the tooling caught up and now most of us put JSX in `.js` files as though it were part of the ECMAScript standard.

When TypeScript first added support for JSX, people were still using the `.jsx` extension a lot, so the TS crew made `.tsx` files compile to `.jsx` files. This is how the `--jsx react` option works.

The React Native ecosystem fully embraced the `.js` extension to the point that the bundler `metro` doesn't even support loading `.jsx` files. This posed a problem for people using TypeScript with React Native because TypeScript _only_ supported `.jsx` files. I can't actually remember how people would use TypeScript with React Native back in those days, but it was probably ugly.

The `--jsx react-native` option was added to let developers compile `.tsx` files to ordinary `.js` files.

_edit_: In addition, it leaves the `JSX` untouched, like the `preserve` option, because React Native used to provide error reports which rendered the JSX (maybe still does? I haven't seen them in forever).

At the time of writing, `react-native-typescript-transformer` uses Babel as a secondary compilation step, so it shouldn't matter whether you use `react`, `preserve`, or `react-native` :)