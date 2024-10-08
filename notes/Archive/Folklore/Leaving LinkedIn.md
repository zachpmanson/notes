Chris Krycho on working at LinkedIn, [released on 2024-03-04](https://corecursive.com/leaving-linkedin-with-chris-krycho/).

---
## Intro

**Adam:** Hello, and welcome to CoRecursive. I’m Adam Gordon Bell. Imagine that you’re at the forefront of shaping the front end for the world’s largest professional social network with like a billion users, LinkedIn, only to find yourself at a crossroads where your core values are just clashing with the demands of the job.

Today, we’re diving into the story of a senior staff engineer at LinkedIn who faced a real dilemma. And if you’re a loyal listener, you might recognize the guest.

**Chris:** There we go. Okay, those are running now. Crap. Did I screw up my ability to hear you?

**Adam:** Hello, hello, hello?

**Chris:** I did. Dang it. Hang on.

**Adam:** Hello, hello?

**Chris:** Yeah, yeah, we’re good now. Okay. Let’s try that again.

**Adam:** That’s Chris Krycho, and he was on the podcast some time ago talking about TypeScript. Today, though, he’s talking about his time at LinkedIn.

**Chris:** I loved my time at LinkedIn. It was great. And I’m really excited for where it takes me next, because I couldn’t do whatever it is I do next without that, including the bumpy parts, but also the really bright parts.

You know, you could come away from that whole difficult ending to the story thinking, wow, LinkedIn really sucked for Chris, but no, actually in the main, it was really great and I’m really glad of it. And even that bumpy ending, I’m glad of the lessons I learned and looking forward to where it takes me next.

**Adam:** So, yeah, about that bumpy ending. Chris worked at LinkedIn in a pretty important and senior role for close to five years. And he oversaw a bunch of important projects in the desktop app, what you see when you go to LinkedIn.com and in a non-mobile browser, that he worked on that. He led projects like modernizing just massive loads of JavaScript,

But let’s cut to the chase. Chris quit LinkedIn. And he quit out of frustration. That’s the story we’re going to unpack today. What it’s like to have a senior technical role at a place with thousands of devs. Right, how do you get big initiatives coordinating across many teams?

How do you get things like that done? How do you lead big projects? How do you improve a massive code base? Also, how do you balance sustainable development practices with a business need for speed? What if this thirst for velocity and speed of iteration clashes with your approach, and your values, and how you think things should be done?

How do you handle that conflict? And spoiler alert, it ends with Chris walking away from the job. That’s what we’re talking about today. But yeah, it all started in Sunnyvale.

## **First Days At LinkedIn**

**Chris:** It was almost exactly five years ago now. I started. The last days of January, 2019, which feels like a lot more than five years ago. Thanks COVID. But, uh, when I first got there, when you join a big company or good, healthy, small companies, there’s usually some variety of onboarding. So I spent a lot of time going through the onboarding classes, learning how all the different layers of the stack worked and all of that.

**Adam:** Chris was going to be working remotely from Colorado once he got going, but the first two weeks were onboarding, and the second of those two weeks was spending time with his team,

**Chris:** You know, sitting next to and chatting with people on my team, my manager, and a couple of the folks I, I worked with.

Even then, that team was a bit more distributed than most. So we had a couple people who worked in that little corner of cubicle land in the Sunnyvale office, and we had a couple people who lived in a corner of cubicle land in the SF office, and then we had one person working from Alaska, and then we had me, Actually working from Colorado remotely, which was very unusual for LinkedIn at the time we had, I think, under 100 engineers remote when I joined and thousands of engineers total.

**Adam:** For Chris, working at such a place was a big change.

## **Millions of Lines of Code**

**Chris:** The startup I’d been coming from had a relatively standard, relatively well-factored monolith backend, and then, you know, database and a handful of services here and there. And I got to LinkedIn and discovered, okay, number one, there are more people working on the front end client app that are employed by my previous employer. And there are more lines of code in this client app than exist at my previous employer in total. And there are thousands of services running in the backend and these monstrous API servers which absolutely dwarf anything we had at my previous employer, but that that’s just the API server for one and this is just the client you think of as LinkedIn.com and oh, by the way, we also have our ad selling platform. And oh, by the way, we also have LinkedIn Learning. And oh, by the way, we also and just the list goes on and on. And so one of the really strong, striking experiences was just repeatedly over and over again saying I’m I’m sorry, did you say insert number here?

My previous company had what I thought at the time was a pretty decent sized app, like 150,000 lines of code. And the LinkedIn front end, when I got there had 2 million, it’s just like, I’m, did you say million? Uh, that’s, that’s a lot.

That’s 20 times almost the size of my, how, how do you even build that? How long to build? Oh, 17 minutes for a new build. That’s, that’s not bad. We should probably make that better, but that’s not bad.

## **Infrastructure Team**

**Adam:** Chris’s team was called the Infrastructure Team, but this didn’t mean standing up servers. It was more like engineering enablement or developer experience. Chris’s job was to make the front end of LinkedIn’s massive desktop app easier to work on. And that’s well, well that’s a lot.

**Chris:** What does it mean to be serving and to some extent helping lead somewhere between 150 to 200 engineers committing to this app every quarter, uh, shipping more and more and more lines of code, just how do, how do you do anything at that scale where there are dozens of teams, hundreds of engineers trying to ship one cohesive product? Just kind of overwhelming at first the scale of all of that exciting also to be very clear It wasn’t like I was like, oh no, it was more like this is cool. But oh my gosh, there’s how do we do what and also then? You know you think about tech debt or tech success either one But at that scale all of those successes and problems are very much magnified.

So you’re like, oh We have two million lines worth of tech debt like whatever your tech debt problems are It’s multiplied by that rather than, you know, whatever your baseline is. And that’s, it’s a lot.

## **JS Modernization**

**Adam:** One of the first big changes that Chris helped with was introducing JavaScript classes. JavaScript had introduced classes, but they were using Ember, the framework, and their code needed some careful updating.

**Chris:** So how do we get 2 million lines of code to change how they author classes from, you know, pass an object literal into a function to, okay, now we’re going to use class foo extends subclass bar or superclass bar.

So that kind of thing was like, okay, we, we have code mods. But they’re not a hundred percent and there are complicated things about like, okay, if you take a native class from JavaScript and use it as a subclass of an old school Ember class? And then that is a subclass of a native class, so it’s kind of striped.

We, we came up with the fun name Zebra Striping for that. Like, if your classes look like a series of zebra stripes where some of them are white and some of them are black, think of that as, you know, old school classes versus modern JavaScript classes all the way along down. There were interrupt bugs because the, the old system was never designed to work with this.

And that gets it maybe one of the biggest pieces that I learned there. Is for a migration to work at that kind of scale it, it has to be as automatable as possible because otherwise it’ll, it’ll just never get done because the amount of work it would take to manually rewrite 2 million lines of code, it’s just going to take months and months of work, even if you could work on it full time and.

It’s totally unreasonable to ask a product team to stop work full time to go get some nice new syntax for their JavaScript. Even if it comes with performance benefits, even if it comes from end user experience benefits,

**Adam:** Oh, right. The product teams. Right. Chris’s team works on ways to improve developer experience, but they need everyone else on board. They need the product teams that are busy shipping features to help.

**Chris:** LinkedIn has a number of relatively well baked processes, always undergoing some degree of revision, but a number of well baked processes for. Wrangling large technical investments, and that dates back to when LinkedIn hit a scaling cliff on its monolith in the early 2010s and just had to go into a service oriented architecture, early microservices.

Mode because it just it could not scale a single monolith anymore at the point It was at and that was a tenth of the size that the user base is now and so on So they basically had to stop work for a year and they looked at that and you know I say stop work stop product work and they said we’re never we’re never gonna do this again It’s too expensive as a business to stop all work for a year.

And so we had a system For horizontal initiatives like that, and that’s what they were called, where horizontal meaning kind of cutting across large numbers of teams and you had to pitch them. There’s a committee that reviews them for the whole company and keeps the level of engagement there at a, you know.

10 percent of these teams commitment or lower so that you can just say, we’re not, we’re not going to spend 100 percent of all of the product teams working on the flagship app on your technical initiative.

**Adam:** Keeping it under 10 percent was tough, so the plan was to use a lot of automation and tooling to speed things up.

But first, they needed a green light from a senior VP, so they crafted a pitch.

**Chris:** So try to fit all of the wins and trade offs and how that makes business value sense and what the actual, what the technical outcomes are and what the then business outcomes are from those technical outcomes in one page. As an aside, LinkedIn had a hilarious culture of one pagers that were like three to six pages long.

**Adam:** are you saying you made a tool and then the specific teams kind of run the tool with the human in the loop and make sure, like,

**Chris:** Yes exactly, right now we also learned from some of those early phases that if If we didn’t have to get those specific teams to do it and we could do it for them. That was also better Because it’s a lot easier for a team to say. Yes I will review your prs and do a smoke test to make sure everything’s good Then it is to get them to sign up to say I will take a You know, a half a week or a week of my product shipping time to do these code mods.

If instead I can just say, Hey, I’ve got this automation. I’m going to run it on your code base. Here’s some training. So, you know, what the output is going to look like and how to work with it. And can you merge my PRs? Much easier, much easier to get buy in from them and especially their management than saying, Hey, can you do some work for us, please?

It took us 18 months end to end to do the Ember stuff. Uh, most of it was in a six month period, but you always have a long tail of teams that Ah, sorry, we have to delay this for two quarters. And another team that gets hit by, well, we would like to fund this, but actually the CEO himself just vetoed our attempted rollout of a new product design.

And we’re going to have to rebuild it from scratch. And sorry, when you go up against the CEO, you’ll lose. So your technical initiative, it’s important. We agree, but no, you can’t have that. Or the CEO wins.

## **TypeScript**

**Adam:** After that project’s success, Chris and his team had a clear next target. It was the flood of errors being generated in the front end.

**Chris:** Like most companies, LinkedIn has error logging for those kinds of things. Most, you know, your startup probably uses a ray gun or something like that to ingest those. LinkedIn has its own internal infrastructure because the prices for the levels of errors we were filing every, every hour would be exorbitant.

**Adam:** that’s wild. I guess there’s like an implication that there’s a lot of like maybe secondary code paths that are just broken. Uh, and that’s surprising to me.

**Chris:** I mean, I guess my snarky take is it shouldn’t be. It really shouldn’t be. It’s like, I mean, to make it a little less snarky and to really speak earnestly about this. When I look at software, a lot of software is bad. Broken in those ways and it’s not generally due to a lack of care on the part of engineers it’s usually down to a combination of structural factors of at least two sorts Sort one is what I think many of us are familiar with just in the form of business pressures of look We’ve got a ship this thing and in a lot of ways, that’s a really good forcing function Motivated engineers are often inclined to polishing for too long, and sometimes we just need to get the thing out into the world.

And that’s again, not necessarily.

bad, but it can mean that we cut corners and we compromise on quality and without a very strong and robust engineering culture that understands, yes, that’s a valuable trade off to make, but no, we can’t make it all the time or we’ll end up with ultimately Broken, janky user experiences that in the short term may not hurt us, but in the long term will actually hurt us as a business.

Even when you’re doing your best, you end up with code that is often subtly broken. So your smoke test might not catch it. Your attempt at QA might not catch it. It might be in an obscure path, but when you’ve got LinkedIn cross the billion members count sometime this past year.

Well, a billion members touching what by the time I left was the 3. 2 million lines of code in this mono repo, half of which is tests and half of which is production code. But like, it doesn’t matter how hard you have tried QA wise. There’s just going to be stuff that somebody thinks to do that. No one ever thought of that particular pathway in combination of stuff to test.

And so you end up with something that’s broken and maybe the page hangs, maybe it white screens on you, you know, somebody reloads

it or. in an app on a mobile device, they just kill the app and restart it and try to do it again. And well, we all know that turn it off and turn it on again, fixes a lot of problems because you get in out of those weird state bugs.

**Adam:** But there was a solution though. If you took those issues one by one and just imagined that instead you have been using TypeScript.

**Chris:** So one of the things we did is go and look at, okay, what’s our actual count of JavaScript errors that we know would be caught by this? There are some that you’re never going to catch.

TypeScript is complicated, JavaScript is complicated, but there were classes of errors that we could say, Look, if we actually do the whole migration, how many of these things will stop going to our logging infrastructure? And when you’re looking at a number that’s in the millions per day, you start to actually be able to talk real numbers of, hey, we could cut our logging volume from the application down by at least a quarter.

Uh, just get rid of 25%. The number’s probably higher than that. That’s a floor.

## **TypeScript Buy In**

**Adam:** So, Chris starts putting together a one pager on moving to TypeScript. The good news is, migrating to TypeScript can be done incrementally.

Lots of codebases have done it before. The bad news is, there’s no way it can fit in a 10 percent time budget. It’s just too large of a task.

But Chris’s document was convincing. TypeScript used to have this slogan, JavaScript that scales.

And with those millions of lines of code, with all of those errors, and going through them, it was pretty clear that LinkedIn needed those scaling benefits. And so, Chris skipped the horizontal initiatives, he, he sort of went grassroots, went bottom up.

**Chris:** Engineering managers would ask engineers on their team, okay, you’re advocating that we be early adopters for this, or that we make a significant investment here.

Why? That document would just get handed to them. And so it became a really useful tool to just have the information available in a relatively concise format that said, here are the problems it solves. Here are the wins it gives us. Here’s how it stacks up even in our hiring ability to compete with our peers who are trying to hire.

And then people could fit that into their mental box of here’s what the tool is. Here’s what it gives us. Here’s how that competes against other priorities. Okay. Yeah, this makes sense. And with that in place, then those conversations about prioritization of it versus other things became a lot easier. I think it became a lot easier for anybody to say, No, this, this is worthwhile. Okay, I get it.

**Adam:** That’s, yeah, that’s powerful. It’s like you’re like, Oh, I just told them something that was obviously true, and then people had to do it.

**Chris:** Yeah. Yeah, that’s right.

**Adam:** So, TypeScript takes off. And Chris becomes the go to guy for tough typing problems, need help with a tricky bit of TypeScripting, call Chris. But with this new free time, with this project underway, the next big issue lands on his desk. And this is where things start to spiral a little bit.

LinkedIn was the biggest user of EmberJS in the world. But they weren’t super thrilled about it. And it was a conflict. Chris felt it too. He was an open source Ember team member, a contributor. But at LinkedIn, as the DX guy, he saw a lot of mismatches.

**Chris:** But long story short, we ended up in a spot where my job a year and a half ago was figure out a plan to get us off of Ember and onto React.

And at the same time, we had senior leaders saying the cost of migrations at LinkedIn is too high. We, even with all these things you’ve been trying to do, all the things we talked about, about getting costs of migration lower, making it things that infrastructure platform kinds of teams do as much of themselves as possible.

It’s still too high. We feel like it is too much of a cost for our product velocity. Now, I would argue that some of the reasons for decreased product velocity are you have a 3 million line of code app that’s seven years old, that has a fair bit of debt piled into it. Both technical and product debt.

That’s just going to slow down over time. It’s very hard to keep up that kind of velocity permanently. And you can’t just change things because you’re going to break user things. So even the product design work is harder because how and where does it fit in the product is harder at that scale. But the message we were getting from leadership in any case was.

We want to see the cost of migrations be lower. So, how do you migrate 3 million lines of Ember code to React code in a way that’s low cost?

**Adam:** Think about this. This is a hard problem. Do a big migration, but don’t slow anybody down while you’re doing it.

## **The Slow Migration Plan**

**Chris:** We came up with a strategy that we thought answered the thing they were saying. And it was a roughly, we expected it to take three to five years. And three years was very optimistic.

Our thought was just double down hard on the automation side of it. Make this a thing that product teams basically never have to do a lot of work on. And at the, the idea was sequence it and chunk it up in ways, pull apart the threads of it so that you could tackle one chunk of it, do it end to end, and then move on to the next one.

And some of them could be parallelized. Some of them, not so much so figure out the sequencing, figure out the chunking, parallelize what you can change the build pipeline, change the data layer, change the routing layer, figure out a bridge for the reactivity system that understands how to handle the routing and the view layer, and then finally kind of flip the view layer in the reactivity system over from the ember.

Rendering and reactivity system, the react one at the very end, but in a way where you’ve written automation that can do it. So that was our pitch. It was, like I said, three to five years going to be a lot of work, but the idea was product teams will never really have to stop.

**Adam:** That’s a huge undertaking, like rebuilding a car piece by piece while driving it continuously on a long road trip. That would be impressive. But three to five years, that’s a really long time.

Meanwhile, while Chris’s team was prepping their plan for the engineering bosses, another team reached out. This team we’re going to call the Fingerguns team, not their real name, by the way. But they had a plan too, and they were tackling a similar problem.

**Chris:** Including what they framed differently. And in my view, correctly, as the thing that engineering leadership executive and otherwise really wanted, which was that word of velocity.

How do we ship features and ideas faster? How do we iterate faster? How do we take an idea from idea to A/B testing? Can, can we get that down to be a matter of weeks rather than months? Because. You know, it has been months. And they identified, okay, we have this split in our stacks. We have this big desktop stack.

We have a different mobile web stack. We have these long cycle times on our iOS and our Android apps. Can we get those times down? Down. And I think, in retrospect, they correctly identified that when our leadership was telling us migration fatigue, migration fatigue was a symptom.

And the actual problem they were really caring about was that. It was, can we focus on faster iteration, trying ideas, killing ideas if they’re not good ideas or they’re not working faster. And migrations get in the way of doing that because our engineers are spending 10 or 20 or 25 percent of their time on migrations and not on being able to iterate on these things.

And the plan we proposed didn’t address that at all.

And this other team came in with a pitch that was kind of a blow up the world pitch. It was, what if we rethink this all from the ground up?

## **The Finger Gun’s Plan**

**Chris:** It was completely what another colleague of mine once described as being in finger guns mode, meaning like, yeah, yeah, yeah, this is going to be awesome, man, kind of finger gunning at each other without answering any of the kinds of questions about what does it look to like to operate this when we’re trying to support hundreds and hundreds of engineers,

And I think it wouldn’t have made me so mad if they’d come in with an attitude of here’s an idea. But we recognize that there are things we’re going to miss because we’re used to supporting a dozen, not 180 and being 30 times as many engineers, just going to reshape things.

Sometimes that fresh perspective lets you come in and say, yeah, I hear you. And we do need to make sure we solve that problem. What if we try this and maybe it won’t work, but what if we try it? There’s a way to do that. The team that came in did not do that. They were like, nah, it just won’t be a problem, man. I was like, well, no, it, it will, maybe we can solve the problem. And I’m up, I’m totally up for you telling me, let’s try this way of solving the problem instead. But no, no, it will actually be a problem. We have a lot of experience to tell you from, from being in the trenches with it, this is a real problem. And so it was very much a case of. Trying to find ways to be collaborative while actually just being perpetually pretty frustrated that our message didn’t seem to be getting through to this other team. They’re like, no, there are concerns you really do actually need to care about here, and we’re happy to help you care about them, but we’re just fundamentally not sold on the thing you’re trying to sell because you’re not showing us, from our perspective, a seriousness about the problem space and the actual difficulty of what you’re trying to do here.

We think maybe it’s worth doing. But what about X and Y and Z? And just getting fundamentally blow it off kind of responses.

Mm like two investment advisors and the one is like, S&P 500 index fund and the other one’s like, Have you seen Bitcoin? NFTs? And like, they’re just like really pumped, right? And the enthusiasm is exciting.

**Adam:** Maybe that’s, maybe that’s too extreme of a dichotomy.

**Chris:** I mean, for whatever it’s worth, that is a perfect analogy to how we felt.

## **Plan Judgement**

**Adam:** So Chris is mad, he’s mad about this plan. He didn’t know that he could pitch a big idea, like, stop everything and start fresh on a huge project with the promise of speed later on. If he knew that, you could bet he’d have a plan, right? Maybe a less wild plan, maybe with more considerations, but it would certainly have a more aggressive timeline than the three to five years. But he didn’t even know stopping the world was an option.

And there’s there’s also sort of a cultural clash here to Jim, a top very senior engineer on the finger guns team. And Chris, they just don’t see eye to eye on a lot of things. They have fundamentally different views on what software engineering looks like.

And so Chris’s team presented their, you know, well thought out, very considered, albeit kind of dull and long term plan to engineering leadership.

**Chris:** Leadership hated it.

**Adam:** They probably have a hard time understanding a five year plan. Like,

**Chris:** Yeah. Yeah, I think that was a huge part of it, and we weren’t excited about the plan, which made it really hard to sell.

And it’s really hard to get a team of execs and leaders to be really excited about a team that the engineers are pitching as a, well, it’ll get the job done, kind of

like it solves all the things we think you asked us to solve.

We think it kind of sucks, but it sucks less than any of the other options that we can find.

**Adam:** So presumably, this is all sort of bubbling around at the exec level. People tossing around solutions to a fuzzy problem that started as, how Ember to React, but really the core thing was maybe about how do we change things so that we can pick up more speed? How do we get faster at making changes at LinkedIn?

And really, I imagine the execs have their own worries, right? They have numbers to hit. They have market pressures. They probably have pressures from Microsoft. A plan to ditch all the cruft that had built up over time. And a plan to gain velocity, to gain speed.

It must sound pretty good. And then Chris took some time off for Christmas.

## **On Call**

**Chris:** and I came back and discovered that we’d been having site up problems, where chunks of LinkedIn’s user base Would for up to about 20 minutes end up with a, Hey, sorry, something’s wrong and not see the linkedin.com page at all.

And well, I’ll tell you two things. One, I hate on call and ops kind of work. And two, I was the most senior engineer on the team and got tapped to do this. And it was a hundred percent on call and ops kind of work as we tried to get to the bottom of what. Those problems were so I basically I went on Christmas break frustrated and came back like okay.

I’ve taken a deep breath. I Can do this. We’ll figure out these dynamics with the other team and instead what happened was things are on fire And also this other thing is still going on in the background and now you get to spend three months doing the kind of work You hate most Trying to figure out what’s going wrong there

## **Memory Leaks**

**Adam:** So about the incident, LinkedIn had these sort of pre rendering services. They ran the client code with Node. js and sort of aggregated all the data from the backend and then they could send it to the client in one big request, bundling everything up for quick delivery right from the data center to the user.

But this had memory leaks and the services were going down.

**Chris:** So, we hit the point where those boxes started running out of memory, and we had a system designed to say, Ah, you’ve tripped over a limit memory usage wise. We’re just going to restart the box. reasonable. We had a couple things missing though.

One, there was no alerting for that. So no one was particularly getting alerted that like, Hey, you’re getting a lot of memory kills. I shouldn’t say there was no alerting. There was insufficient alerting on that. Second, there was a setting to say, How many of these containers can be restarted at the same time?

That setting was a key in a YAML file for configuration, and that key was typed

But at some point, someone set a value there that was a legitimate possible value, but was the, maybe the wrong value to have for this system.

And by maybe, I mean, definitely.

**Adam:** Specifically, the number was approximately the entire number of these services that was running. And they all, you know, start up at about the same time. They all get about the same amount of requests, so their memory all creeps up at about the same rate. Which sounds bad. And somebody might take notice of that memory creeping up.

Except, yeah. Insufficient alerting.

**Chris:** So this is growing and it had gotten bad enough that what we started seeing is anytime there was a long weekend or some reason why there was another kind of deployment pause for long enough, And this misconfigured toggle meant, whoops, we can restart them all at the same time. You know what happens when you restart all of your servers at the same time? Suddenly they’re not responding to user requests. And we would just end up with this kind of thundering herd problem where you’d take a bunch of them offline and that would increase the pressure on the rest of them.

So they would start increasing their memory usage faster because they’re getting more traffic. So washers repeat and we would end up taking down an entire data center worth of these servers. In the background, there had also been a rightsizing process where the idea was we’re going to drop the amount of CPU and memory usage across our fleet to try to avoid over provisioning where we think we’ve got sufficiently Large headroom that everything will be fine and we can save money on not buying new hardware if we don’t actually need it. way to think about the intersection of these things was that right sizing process brought down the ceiling and meanwhile the memory leaks were Raising the water level in the room and all of a sudden now the water’s at the ceiling and the combination of that with one bad configuration meant we were just hosed.

And so a bunch of other engineers and I were looking around saying, we need better alerting, better observability on this. We need more resiliency. There’s no reason that a node server running away should kill the host process that’s managing these node processes. Instead, we should kill the node process alert on that for that condition and restart the node process because then we don’t need to ever bring the container down and we never get into this situation.

**Adam:** It’s like, there’s not a, there’s five opportunities here where we can improve

**Chris:** Exactly, exactly. Failure is inevitable, right? Humans are going to make mistakes. Systems are going to experience power outages. Stuff is going to go wrong in the world. And so the way I think about software engineering. versus programming or hacking, or perhaps as a super set of those, is about designing systems that support engineers in doing their job of getting to those product outcomes.

do we have resiliency of multiple layers of places we can catch that something is wrong, Fix that the, the wrongness in a safe way here and alert and say, Hey, by the way, something changed and it’s going wrong now.

So when it happens, how do we make the system, both the technical side of it and the people side of it, able to respond well?

**Adam:** If you have the inclination, there’s a lot you can learn from an incident like this. Solve the problem, yes, but also improve the system. Prevent the problem from ever happening. One fail safe Chris explored is just falling back to client side fetching if these services were down.

Chris’s approach says a lot about him as an engineer. He’s all about, you know, not just the software, but the systems around it and how can we improve these things, right?

He even has a podcast called winning slowly. That’s all about steady gains and continuous improvement.

But yeah, the higher ups just wanted this incident closed. Maybe this was about the speed thing again, but whatever the cause, the incident meetings started to get a bit tense.

## **Incident Push Back**

**Chris:** So we had a Multiple times a week, stand up for it. What’s status? What have we made progress on?

Let’s report outward. Send info to execs, etc. about what progress we’ve made, etc. Ask for more help if we need it. And one of those, after a weekend where we had run a long experiment, found a new problem.

**Adam:** This was a bad time to find a new problem because a manager for the finger guns team Let’s just call him Dave had just taken over the incident response

**Chris:** He came in and pulled in a bunch of other people and those people were fine, but it was a case very clearly of I don’t trust you to solve this problem and I don’t trust any of your answers and so I’m going to pull in these other people to supersede you, which is frustrating in its own right.

**Adam:** That’s how Jim lands in the middle of the incident call meetings, and things only go downhill from there.

**Chris:** Why doesn’t Code Review just solve this? That was a direct quote from Jim. And my answer was, well it didn’t, and it won’t again in the future because people are going to make mistakes and just be better. Again, it’s not an answer, because what happens when it’s some junior on the rotation who thinks, yeah, that seems reasonable, and this PR was made by a very senior SRE?

Why am I going to question whether that value is reasonable? Like, yeah, there’s a bunch of boxes. That seems fine. Those kinds of things happen. And to that question of engineering systems, one of the things I think about a lot is, does our system only work or does this process only work? Or does this tool only succeed?

If I’m acting like a senior engineer, on his or her very best day or, or does it work if I’m a super junior engineer who’s having a bad day and we really want our systems to be workable for the latter case. And that helps all of us because sometimes, even though I’m a very senior engineer, sometimes I have bad days.

Sometimes my brain doesn’t feel like it’s working at all. Does the system still support me on those days or does it punish me? I really would like to not be punished.

## **Pressure mounts**

**Adam:** The incident was moving forward, but the pressure was mounting, and Chris felt like this group just didn’t understand the scope of the problem or appreciate his considered approach.

**Chris:** “And why isn’t this just getting solved?”

“And execs are unhappy with the rate of progress”

And it’s like, cause you’ve got seven years of piled up technical debt and lack of resiliency that we’re trying to fix and it, if it takes us three months. To fix seven years of negligence. I think that’s actually not too bad was kind of my take. Uh, I remember telling my old manager that that was easily the maddest I have ever been in any job ever was when the finger gun manager came in and was telling me I was not doing a good enough job because it was taking a while to fix these deep seated problems, and it, it really exacerbated my feelings around their, their other proposal of just kind of a lack of seriousness about engineering on this scale of, no, these, These things aren’t easy to solve.

We have an unbounded number of memory leaks to fix, and because of the way this particular memory leak was shaped, they were all references to the same core object. So you could fix one of them, and it didn’t change the behavior of the system. I was very frustrated. And in the background, this also kicked off the experiment for the alternative plan, which everybody bought in on and was like, yes, this is going to work.

And a bunch of engineers were like, but ‘what about’. No, thou shalt not ask, but ‘what about’.

## **ReOrg**

**Chris:** Around the same time, his group took over my group in a reorg hostile takeover. It was, it was a thing.

**Adam:** Ooh, he’s your manager now?

**Chris:** Yeah, he was my boss’s boss kind of situation So not my direct manager, which is good because I probably honestly would have quit on the spot we were in a like let’s so we can see You know, sometimes people get in a different role and they end up learning a bunch of new things.

## **Reflecting on Frustrations**

**Adam:** Maybe this would all work out for the best though, right? Chris is a reflective, thoughtful guy. He could think to himself, maybe I can learn from this new skip manager’s business focus. He knew this was a needs improvement area for him.

**Chris:** The things I was speaking about were real problems. And they really did make things better in ways that I think some people at LinkedIn really do appreciate and I think really do make a difference for people using LinkedIn. But they were never the thing that the business leadership was most concerned about at any given moment.

And that decoupling I think is a big part of Why we ended up in very different spots, and what made it hard to communicate the value of those things

**Adam:** And as Chris entered this more reflective state, reflecting on his frustrations, he noticed he had some weaknesses in building relationships. So many of my colleagues have personal relationships with folks that maybe I struggled even to connect with or figure out how to work with Because they’d see them in the cafeteria

Specifically, Chris is thinking of Jim.

**Chris:** other folks I talked to had less of that challenge. Some of it was just. You know, the way that particular engineer related to our corner of engineering, man, there were, there were some challenges, but there were people who had very good working relationships with him because they just end up sitting down with him in the cafeteria because it’d be a big group of people there.

And it does really help when you’re in the midst of some kind of heated technical argument or whatever to have had lunch with somebody. Uh, or, or otherwise to have built that relationship, but when you have a really strong in person culture and a very high, high percentage of your people are all in person that shows up in those kinds of things, because as a company culture, as a, an engineering culture, your norms are all around.

Yeah, we’ll see each other in the, the cafes and we’ll bump into each other in the halls and, you know, people would tell stories about ending up in the bathroom next to the CEO. Right. You know, that’s a funny dynamic and a funny place to, you know, look over and you’re washing your hands and there’s the CEO washing his hands.

I could see the difference it made to have had constant, just physical interaction with someone who ended up being an SVP of engineering or a principal engineer or whatever, that you just know those people.

**Adam:** This raises another point.

We’ve been focused on this technical clash, speed versus sustainability, but maybe it’s more of a social thing. People under pressure just not hearing each other. I mean, we only have Chris’s side of the story. Maybe this is all a social issue.

**Chris:** Charity Majors had a great quote in a recent article where she said, “At a sufficiently senior level, engineering, or manager, there are no purely social or purely technical problems.”

They’re all socio-technical, and you have to be able to identify where’s the blocker on this. Is it the social side, or the technical side, or usually some mix of the two, and what’s the proportion, and what do I need to do to solve this?

**Adam:** Yeah.

**Adam:** So maybe it’s both. Anyways, stepping back from the incident, Chris finds out that the Fingergun’s plan is gaining ground. It’s gaining traction. And it’s grown in scope. Now it’s about rewriting both the mobile and the desktop apps.

**Chris:** “We’re going to rethink everything about how we build all of our products at LinkedIn”, which that’s exciting. And there were some really interesting parts to that. And also one way of saying what happened was you could just say I and my manager and my team lost. And that would not be a false way of describing it.

But okay my pitch lost. Whatever. I just didn’t like it that much anyway. Can we make the, can we make your version good? Oh, you don’t even want to hear questions that read to you as anything but enthusiasm for this thing’s going to be great. And I’m like, I want to make it great, but we have to tackle these things to make, oh, you don’t even want to hear that.

Okay. Well, I can keep butting my head against this wall. I had conversations with that manager where I was told in literally so many words, ‘You’re too idealistic. You don’t care enough about the bottom line. You should change your values.’ And I was like, no, nope, that’s not how this is going to work, man. Uh, outside I did the politic.

I understand that perspective. I see where you’re coming from. And inside, the little flip switch in my head was flipping saying, ‘nope, nope, nope, warning alarms, klaxons going off all around me.’

**Adam:** Chris thought that their need for speed was blinding them to the real problem.

## **Speed has a Cost**

**Chris:** A lot of the problems we had in the codebases that we had were the direct result of overvaluing velocity and refusing to stop and say: This thing over here, this secondary path doesn’t work right. Let’s fix it or let’s get rid of it.

Either of those are good options, but refusing to do that and constantly just know we’ve got to ship the next feature and how fast can we get it out? And we’ve got to ship the next feature and how fast can we get it out? When velocity becomes the primary or driving value that everything else is subservient to, it leaves you in a spot where maybe you have good velocity initially, but you can’t sustain it over time.

It’s kind of the classic pattern, actually, for codebases as they age, is if you’re not continually investing in them, but you’re continually extending them, you end up exactly where we were. And the things that I saw being pitched were all about maximizing velocity and made no, not even a gesture at how are you going to handle these, these other things.

And I, I’ve kept mulling on it and I, I did my best to give it a fair shot of there’s some interesting ideas here. There’s some interesting technical directions here, but I was also remembering why I left my previous job, which it ultimately was a very bad case of burnout. Of the I’m having horrific migraines and the worst stomach pains I’ve ever had in my life and unable to exercise, uh, random outbursts of sobbing at random times, panic attacks. It was a bad time.

I don’t recommend burnout. It’s not fun.

And if I stay on this road, I know where that goes, and it’s a bad spot, and I don’t want to end up there again. And I can either stay in a world where I’m constantly working not to be angry, because I don’t, you know, I did my best not to stay angry in those times. But when the things that you’re running up against every day make it active work not to be angry, it makes your job not fun, to say the least.

And I can either, you know, try to turn this Titanic with my little rowboat over here and be mad that I’m failing. So that’s not going to work, like, shove it with your paddle, doesn’t, doesn’t turn the Titanic.

Or I can just say, ‘I’m just going to paddle that way.’ The Titanic thing implies that I think they’re heading for an iceberg. I mostly just mean the scale of the thing, not the iceberg side of it. I hope they don’t iceberg. That would be sad. You know, a Disney cruise liner. I’m not going to turn a Disney cruise liner with a rowboat and a paddle.

So I didn’t. I said, I’ve learned a ton. I have some idea of what it’s like to work on a three million lines of code app now that migrate a ton of TypeScript at a huge company and think about those big problems and now I can go do something else and not burn out and not be angry at my job every day or not be fighting not to be angry at my job every day.

I’m not going to spend years of my life trying to build in a way and on things that I ultimately don’t believe in.

Life’s too short. That would be a waste. Okay, this sucks, but I guess it’s time to walk away. Not, not out of spite or malice or any of that, but just saying we’re going different directions.

Maybe the values that this particular corner of LinkedIn was embracing at this particular find are not morally objectionable.

But they’re not mine.
