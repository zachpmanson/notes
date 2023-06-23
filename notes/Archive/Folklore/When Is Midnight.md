Written by [Tom Christiansen](https://ell.stackexchange.com/posts/152729/timeline) at 2018-01-06T14:23:19Z.

---

**ᴛʟᴅʀ**: Virtually all style guides tell people to stop using the irresolvably ambiguous _twelve o’clock ᴀᴍ_ and _twelve o’clock ᴘᴍ_ in favor of _twelve o’clock noon_ and _twelve o’clock midnight_. That solves the **ordinals-vs-cardinals bug** that comes from numbering the hours of the day, but it still leaves you wondering which day midnight belongs to.

---

What you see with “11 ᴀᴍ + 1 hour == 12:00 ᴘᴍ” is largely an artifact of the way we keep time with a zero-based system on computers per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), and what happens when you map a zero-based 24-hour time like 00:00:00.00000 into a 12-hour ᴀᴍ/ᴘᴍ time, which is one-based.

In short, for quite a very long time (up to 2008 for at least one important U.S. government agency), it **_used to be_** that 11 ᴀᴍ and an hour was still considered 12 ᴀᴍ, even though a minute after that it became ᴘᴍ. In the same fashion, an hour after 11 ᴘᴍ was once considered 12 ᴘᴍ, and some people still interpret it that way, although computers are (now) required not to do so.

The hours of the calendar day used to work this way:

- ᴀᴍ: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- ᴘᴍ: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

That way everything made sense because an hour after eleven in the morning was still twelve in the morning, and an hour after eleven at night was still twelve at night.

But now with a zero-based system being used by computers, mapping that to the traditional English system yields the awkward progression:

- ᴀᴍ: 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
- ᴘᴍ: 12. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

This is unfortunate, and surprising as you notice. And not everyone does it that way, even though computers do.

That there is no consensus here about noon and midnight is the real problem. This notation has various issues and ambiguities because exactly noon is neither before noon nor after it. A similar problem exists for midnight. You are advised not to ever write ᴀᴍ or ᴘᴍ in conjunction with 12 o’clock because different people interpret noon and midnight differently.

How did this happen? That’s a longer story. Here's part of it.

---

This problem arises from a confusion between using a “traditional” one-based numbering system where one starts counting at one, and using a “modern” zero-based numbering system where one starts counting at zero. It’s like how the years of the twentieth century ran from 1901 up through and including 2000.

In short, the question is whether the hours run from one to twelve and there is no such thing as zero hours, or whether they run from zero to eleven and there is no such thing as twelve hours. Once you put XII on the clock, you risk confusion. And you have to put XII on the clock because there’s no Roman numeral representing zero.

That’s not a joke: it’s what’s happening here. Without zero, you have to go from I to XII. Behold the clock-face adorning Big Ben in London:

[![Big Ben clockface subtitled DOMINE SALVAM FAC REGINAM NOSTRAM VICTORIAM PRIMAM](https://i.stack.imgur.com/JZAmPm.jpg)](https://i.stack.imgur.com/JZAmP.jpg)

When the bells of Big Ben — or any chiming clock that rings out the hours of the day — chimes with **one** bell, we know that the **first** hour has just been completed. As one commenter observes, having it ring zero bells wouldn’t tell people what time it is. You can’t go from ringing eleven bells one hour to not ringing any bells at all an hour later to then ringing one bell the hour following the one in which you failed to ring any bells at all. People wouldn’t be able to tell what time it was because of something they **didn’t** hear!

Imagine this dialogue:

> TOM: Oh good, it’s time for lunch!
> 
> JERRY: Oh really, and how do you know that?
> 
> TOM: Because it has to be noon, since I just now didn’t hear the clock!

# Ordinals versus Cardinals: First or Zero?

Alas this confusion of ordinals and cardinals starts young, back when we first teach our toddlers how to count items. When you number items using ordinal numbers, you have a first item, then a second item, then a third item. We teach our toddlers to start with _one, two, three_ instead of with _zero, one, two_. The concept of zero is more complicated than a two-year-old needs. If you with perfect accuracy tell them they’re in their third year instead of in their second year when they’re “two years old”, they won’t understand you. That certainly won’t make sense to them then, and for some it may never make sense.

If you think about it, we do the same thing with centuries and years as we do with hours and minutes. We think of there being a first second followed by a second second, and so on. Or that a century has a first year followed by a second year and so on.

Unfortunately, this confusion of ordinals and cardinals is seldom cleared up later in life, which is why we have so many people who cannot understand why if the year is 2018, that that represents the 21ˢᵗ century not the 20ᵗʰ century.

# _Romani ite domum_

The [Romans, who started this whole twelve-hour system](https://en.wikipedia.org/wiki/Roman_timekeeping) and who were notoriously weak on the notion of zeroes, always counted their hours ordinally not cardinally:

```
I     hora prima
II    hora secunda
III   hora tertia
IV    hora quarta
V     hora quinta
VI    hora sexta
VII   hora septima
VIII  hora octava
IX    hora nona
X     hora decima
XI    hora undecima
XII   hora duodecima
```

That is, they had a **first** hour (_hora prima_), a **second** hour (_hora secunda_), a **third** hour (_hora tertia_), a **fourth** hour (_hora quarta_), and so on and so forth.

When one divides a calendar day into two sets of twelve hours each, as the Romans first did and as the English-speaking world and many others still do, and you number those hours from one to twelve, it makes more sense for the sequence to be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 in both cases, not for the sequence to be 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 — since nobody in their right mind counts things that way: you don’t first have twelve things and then add one to it and have only one thing.

The Romans therefore had two pairs of hours, one set in the day and the other in the night, so hours numbering from _hora prima diei_ through _hora duodecima diei_ for the hours of the day on the one hand and hours numbering from _hora prima noctis_ through _hora duodecima noctis_ for the hours of the night on the second hand.

Swap out having a first and a second hand for having a “zeroth” hand and a first hand, and it’s no wonder people find your numbering system confusing!

# Standards, Standards, and More Standards

In the United Kingdom (UK), the National Physical Laboratory (NPL) takes care of the atomic clock that serves as the basis for all time in the UK. As you might imagine, they get asked about time quite frequently. For this reason [their FAQ](http://www.npl.co.uk/reference/faqs/is-midnight-12-am-or-12-pm-faq-time) reads (**_emphasis mine_**):

> ## Is midnight 12 a.m. or 12 p.m.? (FAQ - Time)
> 
> There is no confusion when using the words 12 noon (or midday) and 12 midnight, although the use of 12 midnight can raise the question of 'which day?'. To avoid confusion in, for example, an insurance certificate, it is always better to use the 24-hour clock, when 12:00 is 12 noon and, for example, 24:00 Sunday or 00:00 Monday both mean 12 midnight Sunday/Monday. It is common in transport timetables to use 23:59 Sunday or 00:01 Monday (in this example), or 11:59 p.m. or 12:01 a.m., to further reduce confusion.
> 
> **_There are no standards established for the meaning of 12 a.m. and 12 p.m._** It is often said that 12 a.m. Monday is midnight on Monday morning and 12 p.m. is midday. This puts all the times beginning with 12 and ending with a.m. in the same one-hour block, similarly with those ending with p.m. It can also be argued that by the time you have seen a clock showing 12:00 at mid-day it is already post meridiem, and similarly at midnight it is already ante meridiem. Times in the first hour of the day are sometimes given as, for example, 00:47 a.m., with 00:00 a.m. corresponding to midnight, but with a time twelve hours later given as 12:47 p.m.
> 
> Another convention sometimes used is that, since 12 noon is by definition neither ante meridiem (before noon) nor post meridiem (after noon), then 12 a.m. refers to midnight at the start of the specified day (00:00) and 12 p.m. to midnight at the end of that day (24:00). **_Given this ambiguity, the terms 12 a.m. and 12 p.m. should be avoided._**

So from this we’ve learnt two things of importance:

1. There are no standards established for the meaning of 12 a.m. and 12 p.m.
2. Given this ambiguity, the terms 12 a.m. and 12 p.m. should be avoided.

For some people, including [the United States Government Printing Office before 2008](https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight), the twelve hours **before** noon are numbered one o’clock ᴀᴍ up until twelve o’clock ᴀᴍ, and the twelve hours **after** noon are one o’clock ᴘᴍ up until twelve o’clock ᴘᴍ. Then in 2008, the US GPO switched things around.

The American institution corresponding to the UK’s NPL as Keepers of the Atomic Clock is the National Institute of Standards’ Physical Measurement Laboratory. They too have a [FAQ about noon and midnight](https://www.nist.gov/pml/time-and-frequency-division/times-day-faqs), wherein they write (**_emphasis again mine_**):

> ## Are noon and midnight referred to as 12 a.m. or 12 p.m.?
> 
> This is a tricky question because **_12 a.m. and 12 p.m. are ambiguous and should not be used._**
> 
> To illustrate this, consider that "a.m." and "p.m." are abbreviations for "ante meridiem" and "post meridiem," which mean "before noon" and "after noon," respectively. Since noon is neither before noon nor after noon, a designation of either a.m. or p.m. is incorrect. Also, midnight is both twelve hours before noon and twelve hours after noon.

But even once you do that, you still don’t know which day midnight belongs to.

> ## Is midnight the end of a day or the beginning of a day?
> 
> When someone refers to "midnight tonight" or "midnight last night" the reference of time is obvious. However, if a date/time is referred to as "at midnight on Friday, October 20th" the intention could be either midnight the beginning of the day or midnight at the end of the day.
> 
> To avoid ambiguity, specification of an event as occurring on a particular day at 11:59 p.m. or 12:01 a.m. is a good idea, especially legal documents such as contracts and insurance policies.

Their recommendation is never to write twelve o’clock at all since its confusion can be avoided simply by adding or subtracting a second, at which point you can now safely use ᴀᴍ and ᴘᴍ again.

Although another solution is to use a clearly zero-based time for the hours, that only works if everyone reading it **knows** it’s being used. If you just see a bare 5:00 you can’t know whether that’s really five in the morning or five in the afternoon. In most contexts there will be other non-clock hours present though, like 17:00, at which point you know which system you’re in: that’s not _seventeen o’clock_ (a mythical time **which does not exist**!) but rather _seventeen hundred hours_.

Just please don’t ask why non-ᴀᴍ/ᴘᴍ times are **read out _as though_ each hour were a hundred minutes long**, because I really don’t want to have discuss [metric timekeeping](https://en.wikipedia.org/wiki/Metric_time).