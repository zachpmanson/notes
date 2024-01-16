An essay on the pressures of software engineering compared to other fields, written by [Shawn McKay](https://shmck.substack.com/p/no-dogs-were-harmed-in-the-making), posted to Substack on 2023-11-03.

--- 
# No dogs were harmed in the making of this app

### A reminder of how good we have it as software developers, or perhaps how hard it is for everyone else.

Every profession has its own dance with disaster. Physicians’ diagnosis, accountants’ audit, and writers? They proofread. But for us software developers, we engage in a peculiar kind of sorcery known as "debugging." It’s a delicate art that lets us wade through the rivers of time, witnessing the world through the eyes of a computer, understanding our coded creations at every step.

The Friday before it all began had an air of triumph about it. I leaned back in my swivel chair and announced to my boss with a confident smile, "The geolocated photos feature is ready to launch on Monday." I'd poured my coder's soul into our React Native mobile app, meticulously testing it on Android and the iOS beta - it seemed flawless. It wasn’t.

But what I'm about to tell you isn't just a story. It's a descent into a week-long abyss from 2016, when the magical toolset for debugging turned its back on me, leaving me to navigate the labyrinth of my own code, blind. This is a tale of digital ghosts in the machine, and the relentless hunt that ensued to exorcise them. It’s also a story about good people.

## **Monday**

After releasing the Android beta, I was surprised and confused: the images simply wouldn't upload. A conundrum wrapped in an enigma, especially given the seamless performance on Android in the sanctuary of my local testing environment, not to mention the iOS beta that sprinted without so much as a hiccup.

I re-uploaded a version with improved error handling, but image uploads were failing without any feedback. You see, normally code screams its errors at you in red text - silence is the goal. Here silence was the problem.

Each new iteration of the app, laden with potential solutions, demanded an hour to upload to the Play Store before it could face judgment. Like clockwork, I uploaded new guesses while I prepared for the next. I was running out of ideas and under pressure to deliver.

## Tuesday

By the second day, I was reminded that insanity is doing the same thing repeatedly and expecting different results. Nothing was working.

A kindred spirit, one of the embedded engineers approached me. "I know how you feel. I've been there."

"Oh?" I replied.

He explained, "We regularly ship firmware updates to remote equipment. Once in a while, a node would become unresponsive after an update."

Curious, I asked, "So how do you figure out what went wrong?"

He replied, "We have to remotely retrieve the equipment and have it sent back to us for analysis. Sometimes, it takes months to determine what might have gone wrong."

Realizing that my feedback loops were significantly shorter, I felt better knowing that at least I could put out a number of attempts each day.

## Wednesday

By Wednesday, a seed of doubt had started growing in my mind. I started to question if software development was the right career path for me.

One of the sympathetic hardware engineers approached me. "I know how you feel. I've been there."

"Oh?"

"We often release new hardware remotely, hoping it will remain functional for years. But sometimes design flaws in the hardware only become apparent after enduring multiple seasons. Things break."

"So, how do you figure out what went wrong?" I asked.

"We receive old equipment through the mail, and we attempt to incorporate fixes for the next generations. However, there are times when we add a feature and it turns out to be an even worse bug. One time we added ventilation holes to reduce heat, but they were just big enough for wasps to nest in. We can conduct tests in the lab, but the ultimate test is out in the field."

I started to realize how ambiguous problems were much more of a challenge. Maybe mobile development wasn’t so bad - at least my code either worked or didn’t.

## Thursday

By Thursday, I began to worry about my own job security. I had been spinning on a feature I said I would ship 3 days ago.

The CEO approached and sat down at my desk. I expected the worst. "I understand how you feel, I've been there”.

"Oh?" I asked, surprised.

"Before I started this company, I was a chemist working on my PhD dissertation," he explained. "I was granted a large amount of funding for an expensive chemical to conduct a series of experiments. But weeks into the experiments, it appeared that the results had failed due to experimental error."

"So, how did you figure out what went wrong?" I asked.

"I didn't.” My CEO continued, “When they asked me what I would do differently to prevent repeating the error, I couldn't even provide an answer. Somehow, and to my surprise, I still received the second round of funding."

I fully expected to be in trouble for delaying delivery. I’ve found few leaders demonstrate a level of empathy to bring you back up when you’re feeling down.

## Thursday Evening

On Thursday evening, I went out for sushi with some friends and shared my recent frustration with them.

One of my veterinarian friends chimed in, "I know exactly how you feel. I had a similar problem today."

"Oh, really?" I asked.

She continued, "Earlier today, an owner brought in their elderly, sick dog. I suggested taking an x-ray, but the owner declined due to the cost."

"So, how did you figure out what was wrong with the dog?"

She replied, "The best I could do was feel the dog's stomach from the outside. I felt something large. We performed surgery to remove what turned out to be a corn cob, but without an x-ray, I can’t even be sure that was the extent of the problem."

For the past week, I had been hyper-focused on getting this mobile app out the door, as if nothing else mattered. But I needed to remind myself that, in the big picture, software development isn't usually about life-or-death situations. The stakes aren't typically that high.

---

## Friday

By Friday morning, I noticed a discrepancy in the Android docs and my codebase. What had caused me to spin in circles for a week? A single character.

I sent a message to my friend, "Cracked it at last. It was the letter 'E'."

> For the curious, the image mime type was set to "jpg" but should have been"jpeg" - even though the files were saved as `.jpg`. (See [Stack Overflow](https://stackoverflow.com/questions/33692835/is-the-mime-type-image-jpg-the-same-as-image-jpeg) for details).

She texted back, "Appreciate the update. I needed a bit of positivity today."

I frowned, puzzled. "Why, what's up?"

Her response was simple and somber: "The corn cob dog passed away this morning."

Perhaps software development wasn’t right for me, but it didn’t seem like other professions looked much better.

---

As software developers, it’s easy to overlook the privileges we enjoy. We have the unique ability to delve deep into intricate processes, monitor real-time activities, log what’s happening, and even pause time with a debugger. This remarkable capability is not only cheap but fast, bordering on thoughtless.

While many other professions struggle to understand and resolve their issues, we have the advantage of being able to experiment multiple times a day with just a few clicks.

I am grateful every day for the debugging tools that we have at our disposal.