---
subtitle: Name prefixes are good (sometimes)
---
It can be very useful to use a prefix when naming things, for example when you have many similar variables that you need to easily tell apart or a list of files of different kinds so you can group them together alphabetically.

A great example of this is found in the SvelteKit file route naming conventions, where all files related to routing are prefixed with a `+` so they all appear together at the top in a folder.

A time where name prefixes are not useful is when differentiating variable types, for example prefixing interfaces with `I` (aka Hungarian notation). This is not useful as my editor should be able to provide me this information very clearly. In the case of interfaces, VS Code highlights them in a special color, and will vomit errors if you misuse an interface as a variable. This convention is a relic of the days of yore, before decent language servers and usable IDEs. If we ever start writing a project in C++ I am willing to reconsider this stance.

Yes I know this is a convention in C# but it is not in TypeScript, and in the past has been [specifically disavowed](https://web.archive.org/web/20150515151542/http://www.typescriptlang.org/Handbook#writing-dts-files)by the TypeScript team in the past (which is saying a lot since both languages were designed by the same guy):

> ### Naming Conventions
> 
> In general, do not prefix interfaces with I (e.g. IColor). Because the concept of an interface in TypeScript is much more broad than in C# or Java, the IFoo naming convention is not broadly useful.

-- TypeScript handbook, 2015

If your editor can’t easily show you what type your variable is, you have made a mistake already.