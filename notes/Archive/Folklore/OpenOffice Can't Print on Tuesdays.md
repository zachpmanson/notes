A bizarre bug report thread on OpenOffice.  The [first report](https://bugs.launchpad.net/ubuntu/+source/cupsys/+bug/255161/) and [the solution](https://bugs.launchpad.net/ubuntu/+source/cupsys/+bug/255161/comments/28).

---

Bug #255161 reported by [abrianb](https://launchpad.net/~abrianb2003) on 2008-08-05

```
I am unable to print from open office, I tried reinstalling open office but it did not work. I use a brother mfc240c printer and I am running Hardy. Printing from other apps has not been an issue.

The problem is in openoffice2.4. I'am running Hardy 8.04 When I click print the box opens that allows me to choose print properties. I have looked to make sure things like paper size was correct. When I click print I get nothing. Nothing lights on the printer no message. Open office behaves just like it has printed and yet nothing prints. My printer is a Brother MFC-240C. It prints fine from other apps, Firefox, Evince no problem.
```

<27 comments skipped>

[Steve (paddy-stevepaine)](https://launchpad.net/~paddy-stevepaine) wrote on 2009-04-28:

```

What a fascinating bug!! My wife has complained that open office will never print on Tuesdays!?! Then she demonstrated it. Sure enough, won't print on Tuesday. Other applications print. I think this is the same bug. Here is my guess:

Print to a postscript file. Observe the line:  
   %%CreationDate: (Tue Mar 3 19:47:42 2009)

Change "Tue" to anything else:  
   %%CreationDate: (XTue Mar 3 19:47:42 2009)

Save the file and it prints. Tools like evince work because they simply omit the "CreationDate" tag to begin with.

Now something odd happens when my cups script (I am using the Brother MFC420CN) copies the file to a temp file. Some of the code is rearranged, not sure how or why, but it uses a command called "file" to identify the file as "PostScript". This check would work on the original file you printed, but by the time it runs the check on the temp file, it misidentifies. Normally it would return:

   PostScript document text conforming at level 3.0

But there is another check that happens before the PostScript check. If it finds "Tue" at the fourth byte of the file, it identifies it as:

   Jan 22 14:32:44 MET 1991\011Erlang JAM file - version 4.2

So it's not a problem w/ openoffice.org, cups, or the brother printer drivers. It is a bug in the `file` utility, and documented at [https://bugs.launchpad.net/ubuntu/+source/file/+bug/248619](https://bugs.launchpad.net/ubuntu/+source/file/+bug/248619).

Now, I cannot recommend a fix, but here is my workaround hack:  
make a change in file /usr/local/Brother/lpd/filterMFC420CN

change:  
  cat > $INPUT_TEMP

to:  
  cat | sed -e 's/^%%CreationDate: (Tue/%%CreationDate: (tue/' > $INPUT_TEMP

This will identify a pattern that matches "%%CreationDate: (Tue" at the start of a line, and change "Tue" to "tue".

```