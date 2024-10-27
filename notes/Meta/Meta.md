---
subtitle: About this site.
---
I needed a place to dump hypertext and occasionally images.  This is that!

This site is generated with [[Ochrs]] and written primarily in [[Obsidian]].  It contains my personal notes, [[posts|blog]] and [[archive]]. It is [open source](https://github.com/zachpmanson/notes).

## Structure

This site has several overlapping structures, and I'd like to be consistent about how I use them. This section is an attempt to codify that. Each structure exists in  the Obsidian version of this site and the HTML version.

There is:

- Tree directory structure
	- e.g.  [[Projects]]>[[Ochrs]]>[[Ochrs Syntax]]
	- each page can only belong to 1 directory
	- in the [[Obsidian]] vault this site is written in, this is the directory structure of the [[Markdown]] files
	- in the [[HTML]] version of this site, this is the navigation that can be done using the links in the header
- Backlinks
	- these are arbitrary bidirectional links that form a network of pages within the wiki
	- work the same in Obsidian and HTML
- Tags
	- e.g. [#relics](/tags#relics), [#venting](/tags#venting)
	- each page can have many tags
	- these use the Obsidian YAML tags syntax, can be searched
	- in HTML these are all collected on the [[tags]] page
	- if a page exists with the same name as a tag, that tag is automatically applied to that page and it's children in the HTML version
- Chronological feeds
	-  e.g. [[Posts]]
	- these pages contain a list of other pages that have a given tag (such as [#posts](/tags#posts)) and a publish date, ordered chronologically
	- these are only visible in the HTML version of the site
	- each of these has a corresponding RSS feed
	- sort of just tags that have been elevated to feed status
	- basing this on tags means that any page can be included anywhere in the directory structure, and any page can be included in many feeds simultaneously

How I want to use these:

- Tree directory structure
	- says what a page is
	- e.g. pages in [[Archive]]>[[Problems]] are archived solutions to problems I've had, no matter their topic
- Backlinks
	- ad-hoc links between pages, more of a method of random exploration than navigation
	- the kind of links you'd only want to follow if you actually were reading the content of the page
- Tags
	- says what topics a page covers
	- any topic that is common enough that a person may want to see all of the writing on a particular topic no matter what the page is
	- e.g. the [#venting](/tags#venting) tag contains all pages that contain venting
- Chronological feeds
	- only to elevate tags to create a blog-style interface
	- e.g. [[Posts]]

Yes I know that [all you need is links](https://www.kevinslin.com/notes/kugez1yd9e5frboplescdvd/).