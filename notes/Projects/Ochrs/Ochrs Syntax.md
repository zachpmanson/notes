## Markdown Extensions

Ochrs has a few additions on top of normal [Python Markdown](https://python-markdown.github.io/).  These are the extensions being used by the parser:

<ochrs:md-extensions>

Most of these are officially supported, some are from [pymdownx](https://facelessuser.github.io/pymdown-extensions/), some are from the [third party extension list](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions), and some are custom extensions [included as part of Ochrs](https://github.com/pavo-etc/notes/tree/main/generator/extensions).

### Citations

CiteExtention is a custom extension that turns `-- Name Here`  into `<cite>Name here</cite>`.

## Backlinks

BacklinkExtension is an enhanced version of [WikiLinkExtension](https://python-markdown.github.io/extensions/wikilinks/) that supports aliased links and can include anchor links.

## Ochrs Variables

There are also build-time variables that you have access to on all pages.  The list of extensions above is one of these, generated at built-time by Ochrs.  The format to insert one of these variables is:

```
Some normal text <ochrs:example> some more text
```

Currently available Ochrs variables:

<ochrs:ochrs-vars>

## Tags

Ochrs will detect page tags in ochrs:tags if they are written in the following format:

    Tags: #tagname1 #tagname2

These will be collated on the [[tags]] page.  If any tags written in the Markdown source match the name of any individual page, that page (and its children) will all be assigned to that tag.  See [[Unix]] for this in action.