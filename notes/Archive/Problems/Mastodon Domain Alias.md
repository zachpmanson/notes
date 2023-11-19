---
tags:
  - fediverse
  - dirty-hacks
---
You can use your custom domain as an alias to your Mastodon handle by using Webfinger without actually having your own Mastodon instance.

On your domain, set `GET https://<your-domain.com>/.well-known/webfinger?resource=acct:<accountname>@<server>` to be the same as `GET https://<your-mastodon-instance.com>/.well-known/webfinger?resource=acct:<accountname>@<server>`.

If you have a static site and don't want to set up query params, serving the same file at `/.well-known/webfinger` will make all usernames `@<any username>@your-domain.com` forward to the same account.

## Note for GitHub Pages

GitHub pages doesn't just serve arbitrary files, and won't just serve the JSON file `/.well-known/webfinger` without any file extension.  To serve the JSON file, you can serve it at `/.well-known/webfinger/index.json`.  You will also need to explicitly serve the `.well-known` folder using a `_config.yml` file in the root of of your repo:

```yaml
include: [".well-known"]
```

This is based on these two guides:

- [Mastodon on your own domain without hosting a server](https://blog.maartenballiauw.be/post/2022/11/05/mastodon-own-donain-without-hosting-server.html)
- [Using GitHub Pages to Setup an Alias on Mastodon](https://blog.netnerds.net/2022/11/alias-mastodon-github-pages/)

Hopefully Mastodon implements BlueSky-esque domain as username features.

May be able to get around the static hosting problems using [this, will need to investigate further](https://github.com/mastodon/mastodon/issues/2668#issuecomment-1342518861).  Or [this](https://gist.github.com/aaronpk/5846789).  Or [this](https://aeracode.org/2022/11/01/fediverse-custom-domains/), which [Simon Willison used](https://til.simonwillison.net/mastodon/custom-domain-mastodon).

To see this in practice, search for @zach@zachmanson.com on Mastodon.