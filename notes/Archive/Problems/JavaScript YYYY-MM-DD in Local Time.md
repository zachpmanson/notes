---
tags:
  - dirty-hacks
---
The [[Notes/Software/Development/Programming Languages/JavaScript/JavaScript]] [[datetime]] library is anemic.  If you need the current date in the user's locale written in YYYY-MM-DD, use this fun hack:

```
let currentDate = new Date().toLocaleString("sv").slice(0, 10);
```

"sv" means Sweden, and in Sweden the locale string is formatted "2023-11-05 00:18:41".

Found this solution on [StackOverflow by Tom](https://stackoverflow.com/a/58614322) when making [[Minecraftle]] work across timezones.
