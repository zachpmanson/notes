Steve Yegge story of working on an operating system for Geoworks, and how the choice of language lots to beautiful but ineffectual work.

Originally post [on his site](http://steve-yegge.blogspot.com/2008/05/dynamic-languages-strike-back.html), I became aware of it on [HN](https://news.ycombinator.com/item?id=36570062).

---

OK: I went to the University of Washington and \[then] I got hired by this company called Geoworks, doing assembly-language programming, and I did it for five years. To us, the Geoworkers, we wrote a whole operating system, the libraries, drivers, apps, you know: a desktop operating system in assembly. 8086 assembly! It wasn't even good assembly! We had four registers! \[Plus the] si \[register] if you counted, you know, if you counted 386, right? It was horrible.

I mean, actually we kind of liked it. It was Object-Oriented Assembly. It's amazing what you can talk yourself into liking, which is the real irony of all this. And to us, C++ was the ultimate in Roman decadence. I mean, it was equivalent to going and vomiting so you could eat more. They had IF! We had jump CX zero! Right? They had "Objects". Well we did too, but I mean they had syntax for it, right? I mean it was all just such weeniness. And we knew that we could outperform any compiler out there because at the time, we could!

So what happened? Well, they went bankrupt. Why? Now I'm probably disagreeing – I know for a fact that I'm disagreeing with every Geoworker out there. I'm the only one that holds this belief. But it's because we wrote fifteen million lines of 8086 assembly language. We had really good tools, world class tools: trust me, you need 'em. But at some point, man...

The problem is, picture an ant walking across your garage floor, trying to make a straight line of it. It ain't gonna make a straight line. And you know this because you have perspective. You can see the ant walking around, going hee hee hee, look at him locally optimize for that rock, and now he's going off this way, right?

This is what we were, when we were writing this giant assembly-language system. Because what happened was, Microsoft eventually released a platform for mobile devices that was much faster than ours. OK? And I started going in with my debugger, going, what? What is up with this? This rendering is just really slow, it's like sluggish, you know. And I went in and found out that some title bar was getting rendered 140 times every time you refreshed the screen. It wasn't just the title bar. Everything was getting called multiple times.

Because we couldn't see how the system worked anymore!

Small systems are not only easier to optimize, they're possible to optimize. And I mean globally optimize.