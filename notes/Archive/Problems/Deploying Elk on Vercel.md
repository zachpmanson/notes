The [Elk](https://github.com/elk-zone/elk) [[Mastodon]] client is my preferred frontend, written in Nuxt. It has support for deploying seamlessly on Vercel but it needs access to a caching database.  By default it expects Cloudflare but it also supports Vercel KV (Redis) which is included in Vercel's free tier (hobby plan).

You will need to activate [Vercel KV](https://vercel.com/docs/storage/vercel-kv), start a db project and and get the `KV_REST_API_URL` and `KV_REST_API_TOKEN` values it provides. Then set these values for your deployment env.

```
NUXT_STORAGE_DRIVER=vercel
KV_REST_API_URL=...
KV_REST_API_TOKEN=...
```