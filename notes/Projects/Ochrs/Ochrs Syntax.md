## Markdown Extensions

[[Ochrs]] has a few additions on top of normal [Python Markdown](https://python-markdown.github.io/). These are the extensions being used by the parser:

<ochrs:md-extensions>

Most of these are officially supported, some are from [pymdownx](https://facelessuser.github.io/pymdown-extensions/), some are from the [third party extension list](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions), and some are custom extensions [included as part of Ochrs](https://github.com/pavo-etc/notes/tree/main/generator/extensions).

## Footnotes

The footnotes extension allows plain HTML style footnotes to be automatically generated, and hopefully parsed by [[RSS]] readers.  The syntax is:

```
Some text with a footnote[^1] and a footnote with a label [^label]

[^1]: The footnote
[^label]: Footnote with label
```

### Citations

CiteExtention is a custom extension that turns `-- Name Here` into `<cite>Name here</cite>`.

## Backlinks

BacklinkExtension is an enhanced version of [WikiLinkExtension](https://python-markdown.github.io/extensions/wikilinks/) that supports aliased links and can include anchor links.

## Build-Time Functions

There are also build-time functions that you have access to on all pages. The list of extensions above is one of these, generated at built-time by Ochrs. The format to insert one of these functions is:

```
Some normal text <ochrs:example> some more text
```

Currently available Ochrs functions:

<ochrs:ochrs-funcs>

This are parsed prior to [[Markdown]] generation, so will take precedence over any Markdown syntax.

## Tags

Ochrs detects array of tags in the YAML frontmatter of a Markdown file. They should be in the following format.

```yaml
---
tags:
  - relics
  - unix
---
```

These can be displayed in the using the `ochrs:tags` function.

These will be collated on the [[tags]] page. If any tags written in the Markdown source match the name of any individual page, that page (and its children) will all be assigned to that tag. See [[Unix]] for this in action.

## Chronological Feeds

Ochrs can produce chronological list of posts using tags.  This can be used to produce a blog like interface and RSS feeds.  Any page can be included in a chronological feed by assigning it 1+ tags, and then adding a date property to the frontmatter of the Markdown.  The date will be used as the publishing date whenever it is ranked chronologically.

Each tag will have an RSS feed populated with all pages with that tag and a date attribute, which can be seen on that [[Tags]] page.

To show a chronological feed within a page use the `chrono` build-time function and pass in the desired tag name e.g.`ochrs:chrono:tagname`. See [[Posts]] for this in action.

## Children Visibility

A given page's children can be hidden by default by passing in the `children: false` in the frontmatter.  This is useful for blog-style pages where the children will be contained within the chronological feed.  See [[Posts]] for this in action.

When a page is navigated to, its siblings will always appear, even if their shared parent has `children: false` set.