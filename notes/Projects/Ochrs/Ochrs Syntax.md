## Markdown Extensions

Ochrs has a few additions on top of normal [Python Markdown](https://python-markdown.github.io/).  These are the extensions being used by the parser:

<ochrs:md-extensions>

Most of these are officially supported, some are from [pymdownx](https://facelessuser.github.io/pymdown-extensions/), and some are from the [third party extension list](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions).

## Ochrs Variables

There are also run-time variables that you have access to on all pages.  The list of extensions above is one of these, generated at run-time by Ochrs.  The format to insert one of these variables is:

```
Some normal text <ochrs:example> some more text
```

Currently available Ochrs variables:

<ochrs:ochrs-vars>