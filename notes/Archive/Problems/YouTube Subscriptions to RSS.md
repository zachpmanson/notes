Navigate to [the channel list](https://www.youtube.com/feed/channels), add the following script as a bookmarklet. This function is adapted from [this repo](https://github.com/jeb5/YouTube-Subscriptions-RSS) with the addition of a second folder that excludes shorts.

```js
(function () {
  (async () => {
    const t = document.createElement("dialog"),
      n = document.createElement("label"),
      o = document.createElement("progress");
    ((t.style.cssText = "display: flex; flex-direction: column; gap: 15px; padding: 20px;"),
      t.appendChild(n),
      t.appendChild(o),
      document.querySelector("ytd-app").appendChild(t),
      t.showModal(),
      (n.innerText = "Loading subscriptions..."));
    const l = document.getElementById("content");
    let i;
    do {
      ((i = l.offsetHeight), window.scrollBy(0, 1e5), await new Promise((e) => setTimeout(e, 500)));
    } while (null != l.querySelector("#spinnerContainer.active") || l.offsetHeight > i);  
    try {
      const t = [...l.querySelectorAll("ytd-browse:not([hidden]) #main-link.channel-link")];
      ((o.max = t.length), (o.value = 0));
      const items = [];
      for (e of t) {
        n.innerText = `Fetching URLS... (${o.value}/${o.max})`;
        try {
          const t = e.querySelector("yt-formatted-string.ytd-channel-name").innerText,
            n = await fetch(e.href);
          if (!n.ok) {
            console.error(`Couldn't fetch channel page for ${t}`);
            continue;
          }
          const o = (await n.text()).match(
            /<link\srel="alternate"\stype="application\/rss\+xml"\stitle="RSS"\shref="(.+?)"/,
          );
          if (null == o) {
            console.error(`Couldn't find RSS feed for ${t}`);
            continue;
          }
          items.push([o[1], t, e.href]);
        } finally {
          (o.value++, o.replaceWith(o));
        }
      }
      0 == t.length && alert("Couldn't find any subscriptions");
      const r = t.length - items.length;
      r > 0 && alert(`${r} channel${r > 1 ? "s" : ""} couldn't be fetched. Check the console for more info.`);
      const a = (e) =>
        e.replace(/[<>&'"]/g, (e) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;", "'": "&apos;", '"': "&quot;" })[e]);
      if (items.length > 0) {
        console.log(items.map(([e]) => e).join("\n"));
        let e = `<?xml version="1.0" encoding="UTF-8"?>\n<opml version="1.0">\n\t<head>\n\t\t<title>YouTube Subscriptions as RSS</title>\n\t</head>\n\t<body>\n\t\t<outline text="YouTube Subscriptions">${items.map(([e, t, n]) => `\n\t\t\t<outline type="rss" text="${a(t)}" title="${a(t)}" xmlUrl="${e}" htmlUrl="${n}"/>`).join("")}\n\t\t</outline>\n\t\t<outline text="YouTube Subscription Videos">${items.map(([e, t, n]) => `\n\t\t\t<outline type="rss" text="${a(t)}" title="${a(t).replace("channel_id=UC","playlist_id=UULF")}" xmlUrl="${e}" htmlUrl="${n}"/>`).join("")}\n\t\t</outline>\n\t</body>\n</opml>`;
        const t = window.URL.createObjectURL(new Blob([e], { type: "text/plain" })),
          n = document.createElement("a");
        (n.setAttribute("download", "youtube_subs.opml"),
          n.setAttribute("href", t),
          (n.dataset.downloadurl = `text/plain:youtube_subs.opml:${t}`),
          n.click());
      }
    } catch (e) {
      (console.error(e), alert("Something went wrong. Check the console for more info."));
    } finally {
      (t.close(), t.remove());
    }
  })();
})();

```