---
tags:
  - python
---
The first time I used [[Obsidian]] I immediately knew I wanted all my notes to be written using it, and began work on porting my [[Ochrs]] 1.0 site to be generated from an Obsidian vault.

[Ochrs 2.0](https://github.com/pavo-etc/notes/tree/main/generator) is a rewrite of the original in Python. While this loses the purity that C provides, it also makes it pleasant and flexible.  It has proper [[Markdown]] support, code highlighting, and is designed to use an Obsidian vault as the content source.  The appearance of the website is extremely similar to the original and is much simpler to customise using jinja templates.

The code itself is similar to [[ironprof]], a simple static site generator script I wrote for my [personal site](https://zachmanson.com) that recursively builds jinja templates and converts Markdown into blogposts.

Ochrs 2.0 uses Python-Markdown for all parsing, and introduces a few [[Ochrs Syntax|custom syntax]] behaviours on top of this.  The [[stylesheet]] shows how all common elements look. 
