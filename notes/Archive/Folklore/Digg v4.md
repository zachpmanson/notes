Posted by philovivero on [HN on 2023-06-06](https://news.ycombinator.com/item?id=36217321).

---

I wasn't a Digg founder, but I worked with them from the earliest days on Digg until its downfall.

The real story is probably way more interesting than anyone really would guess. I'll summarise it as so:

What made Digg work really was one guy who was a machine. He would vet all the stories, infiltrate all the SEO networks, and basically keep subverting them to keep the Digg front-page usable. Digg had an algorithm, but it was basically just a simple algorithm that helped this one dude 10x his productivity and keep the quality up.

Google came to buy Digg, but figured out that really it's just a dude who works 22 hours a day that keeps the quality up, and all that talk of an algorithm was smoke and mirrors to trick the SEO guys into thinking it was something they could game (they could not, which is why front page was so high quality for so many years). Google walked.

Then the founders realised if they ever wanted to get any serious money out of this thing, they had to fix that. So they developed "real algorithms" that independently attempted to do what this one dude was doing, to surface good/interesting content.

They thought they'd succeeded, or market pressures forced their hand, whatever. So they rolled it along with a catastrophic UI/UX and back-end tech rewrite all rolled up into one.

It was a total shit-show. I was involved in the "old" MySQL stack, and watched them totally fuck it up with beta software that wasn't ready for production (Cassandra, at the time, was not what it is today).

The algorithm to figure out what's cool and what isn't wasn't as good as the dude who worked 22 hours a day, and without his very heavy input, it just basically rehashed all the shit that was popular somewhere else a few days earlier.

So you ended up with a site that was ugly, fuxed, no-one in the existing wanted, and with a bland boring bunch of stories on the front-page, which was not at all compelling for anyone new showing up to check stuff out.

Instead of taking this massive slap to the face constructively, the founders doubled-down. And now here we are.

To be clear, much of the tech behind Digg was very interesting, the work Owen and many other engineers did was very interesting. The algorithm was all smoke and mirrors, though. And Kevin and his little circle of buddies were all crap engineers that tanked the business with their hubris and inexperience.

---

Replying to self to answer thread questioners. No. Owen was the engineering powerhouse. Kevin was the PR front-man (the pretty face). Ron (Gorodetzsky) was the DevOps mastermind.

Who I am referring to was named Amar (his name is common enough I don't think I'm outing him). He was the SEO whisperer and "algorithm." He was literally like a spy. He would infiltrate the awful groups trying to game the front page and trick them into giving him enough info that he could identify their campaigns early, and kill them. All the while pretending to be an SEO loser like them.

There were a few other amazing people behind the scenes. I'm actually leaving out myself and my group because who wants some dude to blow his own horn? But many of us did amazing things.

There were also literally dozens of guys super high-up that were useless. Not because they were dumb, but they were too full of hubris and thought they had expertise where they didn't. Like Kevin Rose should have realised being a nice guy was his strength, and stay out of engineering, because he started dabbling in it, promoting the wrong people and ideas for the wrong reasons, and the next thing you know... BOOM. Implosion.

I even catch myself calling some of the people who were in K.Rose's event horizon "idiots" or "stupid" but when I really think about it honestly, they were reasonably bright but just given poor incentives. Hey, this NoSQL thing is awesome! Let's replace the entire (functional) MySQL portion with Cassandra. Yeah! After seven beers and two joints, this sounds like an amazing idea. Let's do it!

No.

If you find yourself, or your company founder, doing things like this, sell your equity position for whatever it's worth at that moment. Do not HODL. SELL and SHORT.