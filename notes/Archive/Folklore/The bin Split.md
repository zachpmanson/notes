---
tags:
  - relics
---
[Rob Landley](http://landley.net/)'s explanation of the bin, sbin, usr/bin, usr/sbin split, taken from the [busybox mailing list](http://lists.busybox.net/pipermail/busybox/2010-December/074114.html).

---

```
From: Rob Landley <rob at landley.net>
Subject: Understanding the bin, sbin, usr/bin , usr/sbin split 
Date: Thu Dec 9 15:45:39 UTC 2010 

On Tuesday 30 November 2010 15:58:00 David Collier wrote:
> I see that busybox spreads it's links over these 4 directories.
>
> Is there a simple rule which decides which directory each link lives
> in.....
>
> For instance I see kill is in /bin and killall in /usr/bin.... I don't
> have a grip on what might be the logic for that.

You know how Ken Thompson and Dennis Ritchie created Unix on a PDP-7 in 1969?  
Well around 1971 they upgraded to a PDP-11 with a pair of RK05 disk packs (1.5 
megabytes each) for storage.

When the operating system grew too big to fit on the first RK05 disk pack (their 
root filesystem) they let it leak into the second one, which is where all the 
user home directories lived (which is why the mount was called /usr).  They 
replicated all the OS directories under there (/bin, /sbin, /lib, /tmp...) and 
wrote files to those new directories because their original disk was out of 
space.  When they got a third disk, they mounted it on /home and relocated all 
the user directories to there so the OS could consume all the space on both 
disks and grow to THREE WHOLE MEGABYTES (ooooh!).

Of course they made rules about "when the system first boots, it has to come up 
enough to be able to mount the second disk on /usr, so don't put things like 
the mount command /usr/bin or we'll have a chicken and egg problem bringing 
the system up."  Fairly straightforward.  Also fairly specific to v6 unix of 35 
years ago.

The /bin vs /usr/bin split (and all the others) is an artifact of this, a 
1970's implementation detail that got carried forward for decades by 
bureaucrats who never question _why_ they're doing things.  It stopped making 
any sense before Linux was ever invented, for multiple reasons:

1) Early system bringup is the provice of initrd and initramfs, which deals 
with the "this file is needed before that file" issues.  We've already _got_ a 
temporary system that boots the main system.

2) shared libraries (introduced by the Berkeley guys) prevent you from 
independently upgrading the /lib and /usr/bin parts.  They two partitions have 
to _match_ or they won't work.  This wasn't the case in 1974, back then they 
had a certain level of independence because everything was statically linked.

3) Cheap retail hard drives passed the 100 megabyte mark around 1990, and 
partition resizing software showed up somewhere around there (partition magic 
3.0 shipped in 1997).

Of course once the split existed, some people made other rules to justify it.  
Root was for the OS stuff you got from upstream and /usr was for your site-
local files.  Then / was for the stuff you got from AT&T and /usr was for the 
stuff that your distro like IBM AIX or Dec Ultrix or SGI Irix added to it, and 
/usr/local was for your specific installation's files.  Then somebody decided 
/usr/local wasn't a good place to install new packages, so let's add /opt!  
I'm still waiting for /opt/local to show up...

Of course given 30 years to fester, this split made some interesting distro-
specific rules show up and go away again, such as "/tmp is cleared between 
reboots but /usr/tmp isn't".  (Of course on Ubuntu /usr/tmp doesn't exist and 
on Gentoo /usr/tmp is a symlink to /var/tmp which now has the "not cleared 
between reboots" rule.  Yes all this predated tmpfs.  It has to do with read-
only root filesystems, /usr is always going to be read only in that case and 
/var is where your writable space is, / is _mostly_ read only except for bits 
of /etc which they tried to move to /var but really symlinking /etc to 
/var/etc happens more often than not...)

Standards bureaucracies like the Linux Foundation (which consumed the Free 
Standards Group in its' ever-growing accretion disk years ago) happily 
document and add to this sort of complexity without ever trying to understand 
why it was there in the first place.  'Ken and Dennis leaked their OS into the 
equivalent of home because an RK05 disk pack on the PDP-11 was too small" goes 
whoosh over their heads.

I'm pretty sure the busybox install just puts binaries wherever other versions 
of those binaries have historically gone.  There's no actual REASON for any of 
it anymore.  Personally, I symlink /bin /sbin and /lib to their /usr 
equivalents on systems I put together.  Embedded guys try to understand and 
simplify...

Rob
-- 
GPLv3: as worthy a successor as The Phantom Menace, as timely as Duke Nukem 
Forever, and as welcome as New Coke.
```
