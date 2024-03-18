---
tags:
  - python
---
ironprof is a simple static site generator written in Python that I use to build my [personal site](https://zachmanson.com).  It started as a tool to automate the conversion of my blog posts from [[Markdown]] to HTML and eventually grew to become the primary build tool for the entire site.  Prior to this I was using [[the Poor Man's Static Site Generator]] script to generate the post pages.

Once I had set up a way of building [simple reusable components with jinja](https://zachmanson.com/blog/jinja-components/) I retooled it to traverse the entire site directory and convert `.jinja` files to `.html` files. The generator has full Markdown support, with code highlighting and building [[RSS]] feeds.

The repo for the generator is in my [site's source](https://github.com/pavo-etc/pavo-etc.github.io/).