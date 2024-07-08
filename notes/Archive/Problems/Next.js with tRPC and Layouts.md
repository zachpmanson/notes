---
tags:
  - nextjs
  - javascript
  - posts
date: 2024-07-04
---


An interesting type error arises if you use the standard advice for installing tRPC on an existing Next.js project that already has a layout applied.

Normally the advice for creating an app with a layout is to do this in your `src/pages/_app.tsx`:

```ts
// src/pages/_app.tsx

// ... imports go here

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page);
  return getLayout(
    <SessionProvider session={session}>
      <GlobalProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </GlobalProvider>
    </SessionProvider>
  );
}

export default App

```

This works pretty well.

The docs for tRPC suggest wrapping that export:

```ts
// src/pages/_app.tsx
import type { AppType } from 'next/app';
import { trpc } from '../utils/trpc';
const MyApp: AppType = ({ Component, pageProps }) => {
  return <Component {...pageProps} />;
};
export default trpc.withTRPC(MyApp);
```

Combining these seems simple:

```ts
// src/pages/_app.tsx

// ... imports go here

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page);
  return getLayout(
    <SessionProvider session={session}>
      <GlobalProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </GlobalProvider>
    </SessionProvider>
  );
}

export default trpc.withTRPC(App)
```

But this will throw a type error

![[trpc-typeerror.png]]

```ts
Argument of type '({ Component, pageProps }: AppPropsWithLayout) => ReactNode' is not assignable to parameter of type 'NextComponentType<any, any, any>'.
  Type '({ Component, pageProps }: AppPropsWithLayout) => ReactNode' is not assignable to type 'FunctionComponent<any> & { getInitialProps?(context: any): any; }'.
    Type '({ Component, pageProps }: AppPropsWithLayout) => ReactNode' is not assignable to type 'FunctionComponent<any>'.
      Type 'ReactNode' is not assignable to type 'ReactElement<any, any> | null'.
        Type 'undefined' is not assignable to type 'ReactElement<any, any> | null'.ts(2345)
```

This is because `getLayout` returns a `ReactNode`,  the tRPC wrapper expects `NextComponentType`, which means it expects a `ReactElement` to be returned?

What's the difference between a `ReactNode` and a `ReactElement`?

[This StackOverflow post](https://stackoverflow.com/a/58123882) has a great explanation.

> A [`ReactElement`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/9f855c408dac3c7b3bf0ed9d78242ce073c7aaf1/types/react/index.d.ts#L327) is an object with `type`, `props`, and `key` properties:  
> ...  
> A [`ReactNode`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/9f855c408dac3c7b3bf0ed9d78242ce073c7aaf1/types/react/index.d.ts#L478) is a `ReactElement`, `string`, `number`, `Iterable<ReactNode>`, `ReactPortal`, `boolean`, `null`, or `undefined`:

--[Géry Ogam](https://stackoverflow.com/users/2326961/g%c3%a9ry-ogam)

So  `ReactElement`  can be cast to `ReactNode`, but not the other way around.

There is a simple fix.  If you move the get layout call inside another React component, it will go back to being a `ReactElement`.

```ts
type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page);
  const layout = getLayout(
	<Layout>
	  <Component {...pageProps} />
	</Layout>
  );
  return (
    <SessionProvider session={session}>
      <GlobalProvider>
	    {layout}
      </GlobalProvider>
    </SessionProvider>
  );
}

export default trpc.withTRPC(App)
```

Lucky I was able to find [this tutorial](https://brockherion.dev/blog/posts/creating-per-page-layouts-with-nextjs-typescript-trcp-and-nextauth/) which mentions this exact footgun while I was working on adding tRPC to [[Penultimate Guitar]].