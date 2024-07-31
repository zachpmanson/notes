---
tags:
  - javascript
  - nextjs
  - venting
---
When building Next@14.0.3 application, for some reason the application would work fine in `yarn dev`, build successfully but show up completely blank when running.

One of the errors in console that appeared is that `Math.sqrt` was undefined? What?

Turns out something in crypto-js@4.1.1 is broken in the normal packing process, and it only shows up client-side after build.

This can be solved by letting crypto-js be transpiled by Next.js.

```js
/** @type {import('next').NextConfig} */

// eslint-disable-next-line import/no-extraneous-dependencies
const withBundleAnalyzer = require("@next/bundle-analyzer")({
  enabled: process.env.ANALYZE === "true",
});

const nextConfig = withBundleAnalyzer({
  reactStrictMode: true,
  output: "standalone",
  transpilePackages: ["crypto-js"],
});

module.exports = nextConfig;
```

I found this [solution here](https://github.com/brix/crypto-js/issues/477#issuecomment-1835435744).