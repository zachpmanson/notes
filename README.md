# Ochrs

This is the repo for the Ochrs 2.0 static wiki generator and my personal Obsidian vault used to populate it.

It is built using the `generator.py` script, which traverses the `/notes` directory and writes it to a flat file structure in `/site`, which is a static site that can be served. I'm currently putting the `/site` directory into the `gh-pages` branch of this repo. The deployed version is accessible at [notes.zachmanson.com](https://notes.zachmanson.com).

## Markdown comments

Wrap text in `%%comment body%%` to omit it from generated pages and RSS
feeds. Comments can span multiple lines and paragraphs. Markdown, links, and
Ochrs functions inside comments are not processed. An unmatched opening `%%` is
left as literal text. Use inline or fenced code to show the syntax literally;
comments in indented text (including list continuations) are still removed.

Run the generator tests with:

```sh
nix develop --command uv run python -m unittest discover -s tests -v
```

More details on Ochrs can be found on the [deployed wiki page](https://notes.zachmanson.com/ochrs/) for it, or wherever the Ochrs.md file is in this repo.
