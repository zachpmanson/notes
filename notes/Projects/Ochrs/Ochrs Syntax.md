## Markdown Extensions

Ochrs has a few additions on top of normal [Python Markdown](https://python-markdown.github.io/).  These are the extensions being used by the parser:

<ochrs:md-extensions>

Most of these are officially supported, some are from [pymdownx](https://facelessuser.github.io/pymdown-extensions/), and some are from the [third party extension list](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions).

### Citations

CiteExtention turns `-- Name Here`  into `<cite>Name here</cite>`. 

## Ochrs Variables

There are also run-time variables that you have access to on all pages.  The list of extensions above is one of these, generated at run-time by Ochrs.  The format to insert one of these variables is:

```
Some normal text <ochrs:example> some more text
```

Currently available Ochrs variables:

<ochrs:ochrs-vars>

## Tags

Ochrs will detect page tags in ochrs:tags if they are written in the following format:

    Tags: #tagname1 #tagname2

These will be collated on the [[tags]] page.

