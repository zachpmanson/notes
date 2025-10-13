---
subtitle: Do not change the URL path if the screen hasn’t changed
---

For many screens we have a searchbar where you can select a location. If selecting the location doesn’t change the whole page, do not change the URL path, just update query params. Each URL route should reflect a whole page. This is particularly important in [[Next.js]] Pages Router as URL changes trigger full page rerenders no matter what. This will interrupt any an animations (and is inefficient).