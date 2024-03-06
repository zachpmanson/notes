---
subtitle: A wiki generator.
tags:
  - python
---

This website is generated with Ochrs, which began as a fork of [Nchrs](https://nchrs.xyz), which itself began as a fork of [XXIIVV](https://wiki.xxiivv.com/site/home.html).

## Ochrs 1.0

The initial implementation of Ochrs was forked from Nchrs since Nchrs had forked XXIIVV before XXIIVV underwent from C to Uxntal.  Uxntal is very interesting but not a language I actually know how to write or maintain. I [forked](https://github.com/pavo-etc/legacy-notes) Nchrs and maintained it for a while, but after a while its limitations started to irk me. Its implementation of [[Markdown]] was iffy at best (this led to me calling it Markdownish) and there were myriad edge cases that cropped up as I added more pages. The program was also written in C89 and had manually reimplemented many of the string functions that would become standard in later revisions of the language. This combined with the original author's allergy to comments led to things like this being the best documentation in the entire program:

```C
int cisp(char c) { return c == ' ' || c == '\t' || c == '\n' || c == '\r'; } /* char is space */
int cial(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }/* char is alpha */
int cinu(char c) { return c >= '0' && c <= '9'; } /* char is num */
int clca(int c) { return c >= 'A' && c <= 'Z' ? c + ('a' - 'A') : c; } /* char to lowercase */
int cuca(char c) { return c >= 'a' && c <= 'z' ? c - ('a' - 'A') : c; } /* char to uppercase */
int spad(char *s, char c) { int i = 0; while (s[i] && s[i] == c && s[++i]) { ; } return i; } /* string count padding */
int slen(char *s) { int i = 0; while (s[i] && s[++i]) { ; } return i; } /* string length */
char *suca(char *s) { int i = 0; char c; while ((c = s[i])) s[i++] = cuca(c);return s; } /* string to uppercase */
char *slca(char *s) { int i = 0; char c; while ((c = s[i])) { s[i++] = clca(c); } return s; } /* string to lowercase */
int scmp(char *a, char *b) { int i = 0; while (a[i] == b[i]) if (!a[i++]) return 1; return 0; } /* string compare */
char *scpy(char *src, char *dst, int len) { int i = 0; while ((dst[i] = src[i]) && i < len - 2) i++; dst[i + 1] = '\0'; return dst; } /* string copy */
int sint(char *s, int len) { int n = 0, i = 0; while (s[i] && i < len && (s[i] >= '0' && s[i] <= '9')) n = n * 10 + (s[i++] - '0'); return n; } /* string to num */
char *scsw(char *s, char a, char b) { int i = 0; char c; while ((c = s[i])) s[i++] = c == a ? b : c; return s; } /* string char swap */
int sian(char *s) { int i = 0; char c; while ((c = s[i++])) if (!cial(c) && !cinu(c) && !cisp(c)) return 0; return 1; } /* string is alphanum */
int scin(char *s, char c) { int i = 0; while (s[i]) if (s[i++] == c) return i - 1; return -1; } /* string char index */
int ssin(char *s, char *ss) { int a = 0, b = 0; while (s[a]) { if (s[a] == ss[b]) { if (!ss[b + 1]) return a - b; b++; } else b = 0; a++; } return -1; } /* string substring index */
char *strm(char *s) { char *end; while (cisp(*s)) s++; if (*s == 0) return s; end = s + slen(s) - 1; while (end > s && cisp(*end)) end--; end[1] = '\0'; return s; }
int surl(char *s) { return ssin(s, "://") >= 0 || ssin(s, "../") >= 0; } /* string is url */
char *sstr(char *src, char *dst, int from, int to) { int i; char *a = (char *)src + from, *b = (char *)dst; for(i = 0; i < to; i++) b[i] = a[i]; dst[to] = '\0'; return dst; }
char *ccat(char *dst, char c) { int len = slen(dst); dst[len] = c; dst[len + 1] = '\0'; return dst; }
char *scat(char *dst, const char *src) { char *ptr = dst + slen(dst); while (*src) { *ptr++ = *src++; } *ptr = '\0'; return dst; }
```

This is best described as "technically functional, but unpleasant".

Another issue I ran into was the requirement for all pages to be contained within a single file, `lexicon.ndbl`.  Each page had a line limit which could be mitigated by including external files using the `{^text filename}` and `{^html filename}` idioms.  There was no support for Markdown in external files, and I had no interest in writing a Markdown parser in C, or porting the existing Markdownish parser to work on external files.

## Ochrs 2.0

The first time I used [[Obsidian]] I immediately knew I wanted all my notes to be written using it, and began work on porting my Ochrs 1.0 site to be generated from an Obsidian vault.

[Ochrs 2.0](https://github.com/pavo-etc/notes/tree/main/generator) is a rewrite of the original in Python. While this loses the purity that C provides, it also makes it pleasant and flexible.  It has proper Markdown support, code highlighting, and is designed to use an Obsidian vault as the content source.  The appearance of the website is extremely similar to the original and is much simpler to customise using jinja templates.

The code itself is similar to [[ironprof]], a simple static site generator script I wrote for my [personal site](https://zachmanson.com) that recursively builds jinja templates and converts Markdown into blogposts.

Ochrs 2.0 uses Python-Markdown for all parsing, and introduces a few [[Ochrs Syntax|custom syntax]] behaviours on top of this.  The [[stylesheet]] shows how all common elements look. 

## ochrs-deploy

Ochrs Deploy is a simple Obsidian plugin I made to add a button to the Obsidian left panel to run the `update-notes.sh` script.  Its a bit hacky but does technically work. It isn't in the Obsidian plugin directory (yet), but can be downloaded and added from the [repo](https://github.com/pavo-etc/ochrs-deploy).

