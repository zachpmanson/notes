---
tags:
  - posts
date: 2023-06-19
subtitle: Reviews and advice for all Computer Science, Cyber Security, and Data Science units I completed at UWA.
---

> Yea as long as you do all the work and watch all the lectures you’ll be chilling

-- [seph](https://discord.com/channels/586127025228742656/586575812455563269/783525026573451334)

I did my [[Computer Science]] degree from 2020 to 2023, coming out with a BSc. Computer Science, Cybersecurity, minoring in Data Science. I have omitted statistics units because I have nothing intelligible to say about them[^1].

Just do [Coders For Causes](https://codersforcauses.org/), you will learn more in that than entire semesters of this degree. **Learn how to use [[Notes/Software/Programs/Git/Git]] as fast as possible** then force all your group project members to use it. Narrow down your problems as much as possible, then google the most generic possible description of it. If you see someone using semicolons mid-sentence regularly it's probably [[Christ McDonald|Chris McDonald]].

![[uwa-cits.png]]

## First Year Units

CITS1001 Software Engineering with Java (called Object Oriented Programming when I took it in 2020):

- serves as the introduction to programming for many students
- actively bad introduction to programming
- spends time describing the conceptual model of objects and encapsulation before describing variables and if statements
- class only uses BlueJ (yuck) and as such never teaches you to use a main function. Met students who had completed the class and were still incapable of actually running a Java program
- glad that it is being replaced with CITS2005

CITS1003 Intro to Cybersecurity:

- extremely fun introduction to basic cybersecurity concepts
- main project was a semester long CTF
- perhaps a bit light on content but gives a good taste of the major

CITS1401 Computational Thinking with Python:

- much better intro to programming
- weirdly speedruns 2 years of Computer Science ATAR in the first lesson for no reason
- took 3 weeks to get to if statements in Python which is pretty poor
- decent intro though

CITS1402 Relational Databases

- dead boring but theres no way not to be, it's databases

## Second Year Units

CITS2002 Systems Programming

- Chris McDonald is an excellent lecturer
- good introduction to [[C]]
- challenging projects but you learn a lot
- very rewarding
- this and CITS2200 have the highest kill rate for comsci degrees <sup>[citation needed]</sup>. partially because they are hard, partially because the previous units did a pretty bad job preparing students for them

[[CITS2003]] Open Source Tools & Scripting

- teaches [[Bash]] and [[Unix]] which are important and only orthogonally explained in CITS2002
- teaches [[sed]] and [[awk]] relatively well
- includes [[Make]] for some reason, no reason literally cut this its covered in CITS2002 and is actually relevant there
- also includes [[Notes/Software/Programs/Git/Git]] but never actually requires its use so it feels useless even though it is most students first introduction to it. git should be in CITS1401.
- somehow manages to completely screw up the assessments every year
- see [[Michael Wise Quotes]]

CITS2200 Data Structures & Algorithms

- necessary evil
- teaches important concepts effectively, relatively dry though
- assessments are done in Java and this leads to many stupid problems

CITS2211 Discrete Structures

- the theoretical basis of what a computer actually is
- very interesting but also very hard
- very disconnected from the rest of the degree sadly

CITS2402 Introduction to Data Science

- actual waste of time
- you can learn this entire unit in a day but watching some tutorials on matplotlib, numpy and pandas
- feels like watching a fireship video at 0.005 speed

## Third Year Units

CITS3001 Algorithms, [[Agents]] & Artificial Intelligence

- so much wasted potential
- could be one of the most interesting units in the whole degree, seems like it was before my time
- tries to cover so much but ends up covering very little effectively
- main project was a disaster in 2022

CITS3002 Computer Networks

- Taught by Oppy himself
- Very interesting content, well taught
- projects get your hands dirty with creating actual protocols and working with sockets
- few things were more satisfying in the entire degree than actually running my final project for this over the internet between me and my partners houses and watching it run
- spiritual sequel to Systems Programming

CITS3003 Graphics and Animation[^2]

- abandoned
- feels like it was really interesting in 2009, but the unit coordinator who cared about it has since left and now it wanders the optional units lists like a zombie
- project hasn't changed majorly in 10 years, though it has gotten more convoluted
  - there are certainly past versions of it on github if you are so inclined
- soulless, out of date, and wasted potential as it could be one of the most interesting units

CITS3006 Penetration Testing

- amazing
- final assessment is literally break into this VM, then secure it and swap with other groups
- good balance of pratical and theoretical
- Jin Hong is fantastic
- lab instructors are all great
- had one lecture that wasn't allowed to be recorded because it taught actual live vulnerabilities in UWA systems, excellent, all units should have one of these
- best unit in the whole course

CITS3007 Secure Coding

- the worst C unit by default, only because the others are just so good
- teaches you how to write vulnerable C code, and how to turn off compiler safety checks
- is geniunely interesting
- Arran Stuart is great, seems like the lecturer who is most in touch with modern software engineering?

CITS3401 Data Warehousing

- actual trash
- feels like I learnt 5 things about large scale data storage and nothing else
- project is an arbitrary mess
- pratical side of the unit is a joke
- got really interesting for 2 weeks when it completely switches gears to talk about graph databases but then lets you down again

CITS3403 Agile [[Web Development]]

- really fun and very practical
- FIRST ACTUAL USE OF [[Notes/Software/Programs/Git/Git]] (do no wait till third year, learn this in year 1 semester 1) how did it take this long
- well taught
- [very](https://minecraftle.zachmanson.com) [[Minecraftle|fun project]]

CITS3200 Professional Computing

- your capstone project with an actual client, aka gambling your marks
- if your client is chill you will do well, if not you are ruined
  - e.g. my team shipped actual malware and got a HD
- teams are allocated based on having an even WAM spread so get hyped for mark rubber-banding
- there are lectures
  - 2/10 lectures will be valuable
  - 3/10 will be companies hyping themselves up
  - 4/10 will be inane ethics bullshit
  - 1/10 will be alleged war criminals
- all prior units have not adequately prepared you for this, go learn django or [[React]] because you are very likely going to need to know these. if you are wondering if you should make a web app you should probably just make a web app

## Miscellaneous Advice

Labs are the only thing in the degree you can't get from youtube or the [[Internet]]. If you are bad, actually do the labs, go in and ask the instructors questions. It's annoying but they can help you bridge the gap between trash and passing.

Learn how to use the command line ASAP. Learn git. Seriously go learn git. So many people I met couldn't use git in their third year. How they made it that far sending code snippets over discord is beyond me. Bully everyone you know into using git. You will actually lose 20% mark if you don't use git+github for a group project because you will waste so much time trying to coordinate the project. If git is hurting your brain try using GitHub Desktop which makes it a bit easier to use for newcomers.

Have other hobbies. Doesn't matter what they are but gaming doesn't count if it's your only hobby.

Go to social events with clubs. The specific club doesn't matter, they are all fine. Alcohol helps, if you are so inclined (science union pub crawls are great). It's very easy in computer science to not make actually make any friends and do everything online. But you will need friends to not be sad and die alone.

If you've made it this far, here's [another opinionated essay on university](https://guzey.com/college).

[^1]: When I started my degree I was enrolled in Computer Science and Data Science as my majors. Data Science units come in two forms at UWA, the computer science ones and the statistics ones. The computer science ones were a somewhat random grab-bag of CITS units, all in Python.  They tended to be relatively easy coding and not very deep.  The STAT units, to me, were HARD. The code was all in R, which is a language made by mathematicians not computer scientists and it shows. You can use it to do some very powerful data manipulation very easily, it has incredible libraries for data processing and visualisation, but holy shit writing it breaks my brain and all I did was remember the 8 functions we had been taught in labs and remember which params needed to be switched out. Every two weeks there would be a "lab report" which was a worksheet based on the lessons where you do some data processing in R.  These would **always** take me a full week to complete, which mostly consisted of trial and erroring the functions we had been taught until I had some data that kinda looked like it could mean something if you squinted just right (just like actual data scientists I suppose).  I felt like the classes were taught poorly by angry men. The time spent on the foundational concepts never made sense to me, and did not make sense to any of the other students in my class that I spoke to.  Inexplicably, I did well in pretty much all of the STAT units despite never understanding what I was doing or the underlying mathematical concepts. **Being able to do well while understanding nothing, to me, is the biggest indicator a class is worthless.**  I came to feel that these classes only provided me stress and drew time away from other classes that I actually cared about. At least they were cheap.

[^2]: This unit is so decrepit that as of 2024-08-09 the [course website](https://teaching.csse.uwa.edu.au/units/CITS3003/) doesn't even have CSS anymore