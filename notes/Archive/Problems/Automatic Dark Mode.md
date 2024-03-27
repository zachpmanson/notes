CSS has an automatic dark mode, which works well if you use mostly unstyled HTML.

```css
:root {
  color-scheme: light dark; /* follows system theme */
  --primary: light-dark(#lightvalue, #darkvalue); /* var that switches based on theme */
}

@media (prefers-color-scheme: dark) {
  svg {
    filter: invert(1);
  }
  img[src$=".svg"] {
    filter: invert(1);
  }
}
```

Can be used in combination with `prefers-color-scheme` very simply.  I found out about this from [this site](https://www.htmhell.dev/adventcalendar/2022/19/) from [this post](https://merveilles.town/@thomasorus/112152071343936480).