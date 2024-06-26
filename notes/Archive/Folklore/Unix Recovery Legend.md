This classic article from Mario Wolczko first appeared on Usenet in 1986.

---

Have you ever left your terminal logged in, only to find when you came back to it that a (supposed) friend had typed "`rm -rf ~/*`" and was hovering over the keyboard with threats along the lines of "*lend me a fiver 'til Thursday, or I hit return*"? Undoubtedly the person in question would not have had the nerve to inflict such a trauma upon you, and was doing it in jest. So you've probably never experienced the worst of such disasters....

It was a quiet Wednesday afternoon. Wednesday, 1st October, 15:15 BST, to be precise, when Peter, an office-mate of mine, leaned away from his terminal and said to me, "*Mario, I'm having a little trouble sending mail.*" Knowing that msg was capable of confusing even the most capable of people, I sauntered over to his terminal to see what was wrong. A strange error message of the form (I forget the exact details) "`cannot access /foo/bar for userid 147`" had been issued by msg. My first thought was "*Who's userid 147?; the sender of the message, the destination, or what?*" So I leant over to another terminal, already logged in, and typed

```
grep 147 /etc/passwd
```

only to receive the response

```
/etc/passwd: No such file or directory.
```

Instantly, I guessed that something was amiss. This was confirmed when in response to

```
ls /etc
```

I got

```
ls: not found.
```

I suggested to Peter that it would be a good idea not to try anything for a while, and went off to find our system manager.

When I arrived at his office, his door was ajar, and within ten seconds I realised what the problem was. James, our manager, was sat down, head in hands, hands between knees, as one whose world has just come to an end. Our newly-appointed system programmer, Neil, was beside him, gazing listlessly at the screen of his terminal. And at the top of the screen I spied the following lines:

```
# cd  
# rm -rf *
```

Oh, shit, I thought. That would just about explain it.

I can't remember what happened in the succeeding minutes; my memory is just a blur. I do remember trying `ls` (again), `ps`, who and maybe a few other commands beside, all to no avail. The next thing I remember was being at my terminal again (a multi-window graphics terminal), and typing

```
cd /  
echo *
```

I owe a debt of thanks to David Korn for making `echo` a built-in of his shell; needless to say, `/bin`, together with` /bin/echo`, had been deleted. What transpired in the next few minutes was that `/dev`,` /etc` and `/lib` had also gone in their entirety; fortunately Neil had interrupted rm while it was somewhere down below `/news`, and `/tmp`, `/usr`and `/users` were all untouched.

Meanwhile James had made for our tape cupboard and had retrieved what claimed to be a dump tape of the root filesystem, taken four weeks earlier. The pressing question was, "*How do we recover the contents of the tape?*". Not only had we lost `/etc/restore`, but all of the device entries for the tape deck had vanished. And where does `mknod` live? You guessed it, `/etc`. How about recovery across Ethernet of any of this from another VAX? Well, /bin/tar had gone, and thoughtfully the Berkeley people had put rcp in `/bin` in the 4.3 distribution. What's more, none of the Ether stuff wanted to know without `/etc/hosts` at least. We found a version of `cpio` in `/usr/local`, but that was unlikely to do us any good without a tape deck.

Alternatively, we could get the boot tape out and rebuild the root filesystem, but neither James nor Neil had done that before, and we weren't sure that the first thing to happen would be that the whole disk would be re-formatted, losing all our user files. (We take dumps of the user files every Thursday; by Murphy's Law this had to happen on a Wednesday). Another solution might be to borrow a disk from another VAX, boot off that, and tidy up later, but that would have entailed calling the DEC engineer out, at the very least. We had a number of users in the final throes of writing up PhD theses and the loss of a maybe a weeks' work (not to mention the machine down time) was unthinkable.

So, what to do? The next idea was to write a program to make a device descriptor for the tape deck, but we all know where `cc`, as and `ld` live. Or maybe make skeletal entries for `/etc/passwd`, `/etc/hosts` and so on, so that `/usr/bin/ftp` would work. By sheer luck, I had a `gnuemacs` still running in one of my windows, which we could use to create `passwd`, etc., but the first step was to create a directory to put them in. Of course `/bin/mkdir` had gone, and so had `/bin/mv`, so we couldn't rename `/tmp` to `/etc`. However, this looked like a reasonable line of attack.

By now we had been joined by Alasdair, our resident UNIX guru, and as luck would have it, someone who knows VAX assembler. So our plan became this: write a program in assembler which would either rename `/tmp` to `/etc`, or make `/etc`, assemble it on another VAX, `uuencode` it, type in the uuencoded file using my gnu, `uudecode` it (some bright spark had thought to put `uudecode` in `/usr/bin`), run it, and hey presto, it would all be plain sailing from there. By yet another miracle of good fortune, the terminal from which the damage had been done was still `su`'d to root (su is in `/bin`, remember?), so at least we stood a chance of all this working.

Off we set on our merry way, and within only an hour we had managed to concoct the dozen or so lines of assembler to create `/etc`. The stripped binary was only 76 bytes long, so we converted it to hex (slightly more readable than the output of uuencode), and typed it in using my editor. If any of you ever have the same problem, here's the hex for future reference:

```
070100002c000000000000000000000000000000000000000000000000000000  
0000dd8fff010000dd8f27000000fb02ef07000000fb01ef070000000000bc8f  
8800040000bc012f65746300
```

I had a handy program around (doesn't everybody?) for converting ASCII hex to binary, and the output of `/usr/bin/sum` tallied with our original binary. But hang on---how do you set execute permission without `/bin/chmod`? A few seconds thought (which as usual, lasted a couple of minutes) suggested that we write the binary on top of an already existing binary, owned by me...problem solved. So along we trotted to the terminal with the root login, carefully remembered to set the umask to 0 (so that I could create files in it using my gnu), and ran the binary. So now we had a `/etc`, writable by all. From there it was but a few easy steps to creating `passwd`, `hosts`, `services`, `protocols`, (etc), and then `ftp` was willing to play ball. Then we recovered the contents of /bin across the ether (it's amazing how much you come to miss `ls` after just a few, short hours), and selected files from `/etc`. The key file was `/etc/rrestore`, with which we recovered `/dev` from the dump tape, and the rest is history.

Now, you're asking yourself (as I am), what's the moral of this story? Well, for one thing, you must always remember the immortal words, **DON'T PANIC**. Our initial reaction was to reboot the machine and try everything as single user, but it's unlikely it would have come up without `/etc/init` and `/bin/sh`. Rational thought saved us from this one.

The next thing to remember is that UNIX tools really can be put to unusual purposes. Even without my gnuemacs, we could have survived by using, say, `/usr/bin/grep` as a substitute for `/bin/cat`.

And the final thing is, it's amazing how much of the system you can delete without it falling apart completely. Apart from the fact that nobody could login (`/bin/login`?), and most of the useful commands had gone, everything else seemed normal. Of course, some things can't stand life without say `/etc/termcap`, or `/dev/kmem`, or `/etc/utmp`, but by and large it all hangs together.

I shall leave you with this question: if you were placed in the same situation, and had the presence of mind that always comes with hindsight, could you have got out of it in a simpler or easier way? Answers on a postage stamp to:

```
Mario Wolczko
------------------------------------------------------------------------
Dept. of Computer Science       ARPA:   miw%uk.ac.man.cs.ux@cs.ucl.ac.uk
The University                  USENET: mcvax!ukc!man.cs.ux!miw
Manchester M13 9PL              JANET:  miw@uk.ac.man.cs.ux
U.K.                            061-273 7121 x 5699
------------------------------------------------------------------------
```