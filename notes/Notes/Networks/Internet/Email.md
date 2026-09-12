---
subtitle: Email is just paper that can teleport.
date: 2026-09-12
tags:
  - posts
---
Email is infuriating until you realise it's just paper that can teleport, and each reply is also just paper, and it has all the same strengths and weaknesses of letters written on paper.

Which makes it immediately clear why email is so bad at being a group chat.

## Where Email Works

For 1:1 conversations, email is pretty good. Similar to how me and my friend April sending letters to each other is pretty good. Lets assume April and I keep copies of the letters we send each other for future reference, and now all of the following holds up:

- all participants know the full and consistent conversation history
- we can read the conversation in chronological order and everything makes sense
- I can send attachments like photos and we both have copies of them
- we could start multiple conversations in parallel based on subject and it could work decently
	- it has the potential to be confusing but we could make it work if we were strict about discussing specific topics in specific threads
	- even if I wanted to reply to an older message, as long as its in the same subject thread its easy to know what I'm referencing by quoting the relevant passages
- if April and I both send messages at the same time, its straightforward to figure out that both of our messages were written without the context of the other based on timestamps and content

## The Cracks Form

Me and April are very happy with a 6 month long chain discussing Lego Star Wars The Complete Saga when I realise my friend Ben might have something to add. Email offers two ways to add Ben to the conversation, a) reply to the existing thread and add Ben as recipient or b) forward the latest message to Ben. Both of these have pros and cons but both lead to the same core problem. 

Ben won't get all 6 months of emails properly, both of the options will only send Ben 1 email. But fear not, my email client of choice injects a quote of the message it is a reply to, and April's client does the same thing, so the message Ben gets will contain 6 months worth of nested quoted emails which he can read in reverse order to catch up to the conversation. This is a bit annoying in format, but more importantly it's fragile.

The quoted section is just a convention, every email client does it slightly differently, and it's exposed in the email editor UI so I could alter the quoted text[^annotations] and Ben would be none the wiser. If I deleted the quoted text in an email to April 2 months ago[^partial-quoting], then that would break the quoting chain for all future emails and Ben would not see any messages before that deletion, and wouldn't know there were any older than 2 months.

This problem is more or less exactly the same problems you would run into on paper. April and I send letters for 6 months, I want to get Ben's thoughts so I need to send him a copy of every letter April and I have sent on the subject. I could alter the emails and Ben wouldn't know, or I could send him a subset of the chain and he wouldn't know. He just has to trust that I'm sharing everything he needs. The only difference is email adds quotes automatically-ish, a fragile automation of me walking around my house finding all the letters in the thread and making photocopies.

Then Ben writes his reply, and sends a copy to me and and to April, hopefully using the same subject line so we know it's related to our existing thread. We continue on, all future messages contain all 3 of us as recipients and we continue our discussion.

Adding Ben to the chain worked, but there were several places context could have been lost and would be invisible to Ben:
- if the quote history was removed anywhere in the previous messages
- if quote history was tampered with Ben will be missing the original copy
- attachments from earlier in the chain may not be preserved in Ben's copy
- if I forward email X in the chain to Ben, then April sends me message Y in the chain, then Ben sends his reply Z, Ben will miss message Y from April
- if subject names were not preserved well enough our email clients may not recognise that new messages were part of existing threads[^references]
- if a second email thread is started, we need to remember that Ben is involved now
- if the conversation history forks (2 messages both reply to the same parent message), the email quoting section going forward may be missing that other branch of messages
- if someone presses Reply instead of Reply All, someone is going to miss a message

In a 1:1 conversation these aren't really issues, and even a 3 person chain is doable, but each additional person increases the chain increases the surface area for something to go wrong.

## It Breaks

In professional settings, email chains get ridiculous. Even if your company does all of its internal communications through Slack et al., email is needed to talk to other organisations. In my work it's common for me to be forwarded an email thread that started 9 months ago, with dozens participants, 3 organisations, with broken quoting history, that is actually only 1 of the 4 threads on the project, each containing a different subset of recipients. The chance that I am missing context asymptotically approaches 100%.

Whenever this would happen I would tear my hair out trying to understand who said what to who and I would inevitably lose track of who is in which thread. Have you ever tried to reconstruct the timeline of 2 parallel email chains you've been forwarded?[^timezones] I don't recommend it.

This is a diagram of all of the emails for a particular project at work involving 3 companies and 28 participants. Note that this is just the messages I am privy to, there are many more that I cannot see because the email chain quoting broke months before I was added to any of the threads. Also note that empty circles are messages that I only have access to via unspooling quote sections, they were not actually sent to me.

![[email-diagram.svg]]

Half the messages in the chain were never sent to me! Until I made this visualisation I had no clue how complex this was, all I knew is that I was struggling to comprehend it.

I thought there was some true understanding that I was missing, how can the whole world run on this system where I have to read quoted threads backwards, ignore bloated email signatures and mangled quotes? There must be a system behind this that I'm just not getting.

But no. There is no system.[^well]

## It's just paper

Of course paper than can teleport doesn't work as a group chat. How could it! How could you expect it to. Anyone can address any piece of paper to anyone, anyone can quote or not quote the context, anyone can alter the context it contains. It's actually insane that it works as well as it does. The email standard is the ultimate *building the plane in midair*, where attachments are bolted on as inline text and CC is actually the same as TO[^bcc] and forwarding is guaranteed to mangle whatever thread it contains. Quoting is an informal convention[^html], every client does it differently. It's just paper. It's just paper. It's just paper. 

If you treat email like a group chat you will never be happy. [But I'm not going to let that stop me](https://github.com/zachpmanson/chainmail).



[annotations]: Some people use this as a feature where they annotate the quote of email they are replying to. I hate this but it's common.
[partial-quoting]: Apple Mail makes this easy to do by highlighting text before you press reply. Given this has the potential to break downstream forwarding I think this is an anti-feature.
[timezones]: Email clients often don't include the timezone a quote is from, so sometimes it is actually impossible to determine the timeline of a conversation from the context you have
[html]: It's formalised for plain text email but not for [[HTML]] email. HTML is too powerful for email. I would want GFM email, that's my dream amount of formatting. Nobody needs `div` in an email.
[bcc]: I don't even know how BCC works and I have no plans to.
[well]: There's 18 different systems that all might make sense if they were the only system but each mail client does it differently and the underlying quoting mechanism is so dodgy that it can't be trusted so it's better as a user to pretend there is no system.