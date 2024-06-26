From [Raymond Chen's post](https://devblogs.microsoft.com/oldnewthing/20131008-00/?p=3003) on The Old New thing on Bill Gates writing FAT on a plane, posted on 2013-10-08.

--- 

When you wrote code for 16-bit Windows, one of the things you spent time doing as part of performance tuning was deciding which functions should be grouped together in which segments.

Code in 16-bit Windows executed out of code segments, each of which could be up to 64KB in size. When a code segment was loaded from disk, the entire segment was loaded, and when it was discarded, the entire segment was discarded. This meant that you could affect your application’s performance in significant ways by choosing which functions go in which segments.

For example, it was to your advantage to keep functions that are called at the same time in the same segment, so that they would be loaded as a unit (saving I/O time). If you chose poorly and put unrelated functions in the same segment, then calling any function in the segment caused all the functions to be loaded, which was a waste of I/O since you loaded a bunch of functions you didn’t need.

Even if the functions were called at the same time, you also had to keep an eye on their popularity. If you have one function that is called frequently and another that is called infrequently (but always preceded by a call to the first function), the less popular function will ride the coattails of his roommate and remain loaded in memory. This creates unnecessary memory pressure that could cause a function which is moderately-frequently-called to be discarded to make room.

Creating lots of small segments allowed your memory usage to be managed with finer granularity, but it also costs you in general overhead as well as I/O, because each segment load was a new round trip to the disk. You therefore had to balance memory cost against I/O cost.

The process of optimizing the grouping of functions into segments was known as *segment tuning*.

During the development of Windows 3.0, it was customary to have regular meetings with Bill Gates to brief him on the status of the project. At one of the reviews, the topic was performance, and Bill complained, “You guys are spending all this time with your segment tuning tinkering. I could teach a twelve-year-old to segment-tune. I want to see some *real* optimization, not this segment tuning nonsense. I wrote FAT on an airplane, for heaven’s sake.”

(I can’t believe I had to write this: This is a dramatization, not a courtroom transcript.)

This “I wrote FAT on an airplane” line was apparently one Bill used when he wanted to complain that what other people was doing wasn’t Real Programming. But this time, the development manager decided she’d had enough.

“Fine, Bill. We’ll set you up with a machine fully enlisted in the Windows source code, and you can help us out with some of your programming magic, why don’t you.”

This shut him up.