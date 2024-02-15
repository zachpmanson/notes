[James Gosling on how Richard Stallman](https://www.youtube.com/watch?v=TJ6XHroNewc&t=10377s) stole the source code the emacs.  Transcribed [here](https://old.reddit.com/r/programming/comments/dhrcxw/james_gosling_on_how_richard_stallman_stole_his/f3qk4xh/) by /u/gschizas.  Richard Stallman's side of this story is told in Sam Williams' [*Free as in Freedom*](https://bzr.savannah.gnu.org/lh/books/revision/1#free-as-in-freedom-v2/chap06.tex) ([pdf version](https://sagitter.fedorapeople.org/faif-2.0.pdf)).

---

**Hsu**: So then your-- But your display algorithm got incorporated by Richard Stallman into GNU Emacs.

**Gosling**: Well, actually, it was more than that. He just took all of the source code.

**Hsu**: Oh, okay.

**Gosling**: Right. It was, it started out as all of the source code and he just edited the copyright notices.

**Hsu**: Really? So he just essentially stole your program.

**Gosling**: Yeah, so--

**Hsu**: <laughs\>

**Gosling**: Ah--

**Hsu**: And claimed it as his own?<laughs\>

**Gosling**: Yeah. So, so what had happened was I have this, like, point in my-- in grad school where I realize I'm either Mr. Emacs for life or I graduate. So I decided I wanted to graduate so I kind of went around to all the usual suspects and said, "Is there anybody willing to take over the maintenance of Emacs?" And, and everybody said, "Well, I really love Emacs and everybody here at," you know, MIT or UCLA or whatever, "We all love Emacs, but we actually have day jobs." And they-- And so I couldn't find anybody who would do it. I even asked Stallman and his, his answer wasn't just no, it was more like a frothing hell no. And, you know, mostly because it was for Unix.

**Hsu**: Mmm.

**Gosling**: And one of his big things was Unix and using Unix was, back then his attitude was that Unix was the spawn of the devil and he made that really clear. But I did find a couple of guys who were willing to do it but they would need to, like, earn money from it and I had, you know, from the very beginning been very careful about putting copyright notices on Emacs, you know, and the deal that I had with everybody was, you know, write me a letter and I'll send you a mag tape, you know, and the letter was basically agreeing to this license. And the reasons that I had done that was-- So this, this guy Mike Shamus, the guy who, the professor, the theory professor, he'd also gotten a law degree and had gotten involved in a bunch of intellectual property issues. And there was this weird thing that had happened at Carnegie Mellon where Carnegie Mellon was sort of unique in its sort of charter documents in that if a-- At a lot of universities if a student produces some piece of work it's partially owned by the university, so you just, you can't just give stuff away. And they usually have, you know, weird clauses that have evolved and for software around open source stuff that that way you can do it. But back then open source wasn't a thing, but you couldn't give stuff away. But at, but Carnegie Mellon was sort of unique in that it had these rules that said if a student produced some work then the student owned it, which was really strange. And but there had been this one case where Carnegie Mellon has, it's kind of a small university, but it's got sort of two world class departments. One is the School of Computer Science and the other is Performing Arts. And I mean, the Performing Arts Department there is just astonishing. But one of the students there, it was like their master's project or something, they wrote a rock opera and I think it was "Godspell," not exactly sure. But then that, but it turned into a big financial blockbuster and the university tried to retroactively change their rules about intellectual property and that turned into a big saga. And, and one of the things that came out of that was this sort of lingering apprehensiveness about intellectual property rights. And in the Computer Science Department, there was another student who had built a piece of software that had gotten really popular on the internet and it was a text formatter called Scribe. It was done by Brian Reed. And he also got into a bunch of, you know, the university tried to pull stunts with him. And so after that history, I decided that I should be careful and I talked to Mike Shamus about it and he said, "You know, do, you know, put this header on all your source files and make sure you get a letter back from folks that basically says that they acknowledge the dut-dut-dut-dut" and so I was really careful about that. But then when I had decided, you know, I wanted to graduate rather than being Mr. Emacs, I found these two guys who ran this little company called Unipress, it was literally two guys in a garage, and I said, "Look, this needs to be free for universities and not ridiculous for everybody else." And they said, you know, "Fine. We're just two guys in a garage. We don't need much. And this seems to be awfully popular, so we think we can actually, you know, pay our rent and feed ourselves." So that was fine and they were doing really well. And then Stallman freaks and he gets a copy of my source code, does a whole lot of editing. He doesn't actually-- You know, he edits, like, almost all of the copyright headers, but he doesn't edit all of them and he only kind of thinly edits it and then he re-releases it as GNU Emacs. And then IBM and Digital Equipment pick that up and start distributing it. So these, so the two guys in the garage who had been doing okay suddenly find that IBM and DEC are distributing their thing for free and they're dying. So they decided to sue DEC and IBM and they got a, you know, and that turned into a big, big court case. They won. It was kind of a pyrrhic victory. You know, so IBM and DEC paid them some damages, but that didn't stop GNU Emacs. You know, they didn't get GNU Emacs pulled, so it just sort of carried on and these guys sort of shifted their business, which always made me feel kind of bad for them because they really got shafted. And, yeah, so and at the very beginning of GNU Emacs it was literally line for line, I mean, they actually, you know, there were expert witnesses who, you know, by eyeball, you know, searched through the source code and went, "Yeah, it's the same." They actually found that some of the early GNU Emacs source files that were being distributed, they hadn't, he hadn't actually changed all of the copyright notices. So it was like, duh. But then it sort of took on its own life and it's become the GNU Emacs that everybody uses.

**Weber**: But Stallman was not involved. No one went after him because he had no money, right?

**Gosling**: Right. I mean, you can't sue a homeless person, right, which is, you know, he-- Yeah, he had sort of weird views on, you know, economic models at the time.

**Weber**: And personal hygiene.

**Gosling**: Yeah. Yeah. And, you know, I realize I'm a radical. I like to actually have a bed to sleep in and food and I will occasionally sleep in my office, but not as a regular thing. And I haven't done that for a long time.