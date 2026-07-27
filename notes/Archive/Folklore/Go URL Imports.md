---
subtitle: The Troubles of Go URL Imports
---
A great writeup by mort96 on [2026-05-16](https://news.ycombinator.com/item?id=48157827).

---

The core issue is philosophical. Whether you happen to have public infrastructure which provides a web front-end for your git repository, and what exact server that web front-end happens to be hosted on, ought to be completely incidental to compiling source code. But since you ask, Go is the best example of how this can go terribly wrong in practice, IMO. Here are just a few scattered pain points I've encountered:

* In order to follow convention, you need to decide on git web hosting infrastructure _before_ you start writing code. The tooling asks you for a URL the moment you run 'go mod init'. My preferred way of doing things is to start work on a project just on my computer and then maybe put it on one or more online git web host eventually, if the project goes anywhere. That order doesn't work with ideomatic Go. To work around this, I write mostly non-ideomatic Go where I use the name of the project instead of a URL as a package name.

* I view hosting infrastructure as incidental. I may throw a project on GitHub. I may change my mind and move it to Codeberg. I may move it to my own git forge. I may get tired of hosting my own git forge and move it to sr.ht. With Go, each of these moves requires a huge "touch a bunch of lines in every file" style commit if you're using the ideomatic "git web host as package identifier" style required to work with 'go get'. In other languages, it requires at most a readme change, and for dependencies, it requires at most a git submodule or package manifest change.

* Go requires that you use a Go-compatible git web host. Because Go decided to make URLs look like 'example.com/foo/bar/baz/qux', it has no way to determine which part of that is the git repo and which part is a subdirectory of the repo; should it 'git clone example.com/foo/bar/baz.git' and look at the 'qux' subfolder or should it 'git clone example.com/foo.git' and look for 'bar/baz/qux'? The only solution is for Go to make an HTTP request to 'example.com/foo/bar/baz/qux?go_get=1' and parse the response HTML and look for a Go-specific meta tag which tells Go what part is a git repo. This is an immense "layering violation" and extremely ugly hack in my opinion. This feels so unnecessary too, since this is an easily solvable problem: just make URLs look like 'example.com/foo/bar/baz:qux', so that Go knows to look for 'qux' in 'example.com/foo/bar/baz.git'.

* Private repos are a horrible experience. You need to convince Go to not look them up in Google's package checksum database, you need to convince Go to not get them from Google's caching infrastructure, you need to make a ~/.netrc file with credentials, you need a git host web frontend which understands and supports the way Go + .netrc makes authenticated GET requests. If any of these things are misconfigured, you get a cryptic error message about how terminal prompts are disabled on Google's servers. It's all very brittle and hard to debug, and the guidance has changed drastically over time (editing your global .gitignore to rewrite relevant HTTP sources to use SSH used to be the advice, but that had its own significant problems).

* It has the "feeling" of being decentralized since it's all just git URLs, but in reality, Go's tooling depends heavily on Google's centralized package cache and checksum infrastructure which has been introduced over time to smooth over foundational issues with the design.

I was once part of separating a complex project out of a company and moving it to its own infrastructure on a different domain name and git host. The Rust and C++ repositories were a breeze, just change the URL in a CI job. The node.js repositories required changing some references in the source code from one NPM org name to another but were otherwise painless. The Go repositories were absolute hell.

I have considered writing a blog post about all this.