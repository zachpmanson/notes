A [response]() by oraguy to the thread [Ask HN: What's the largest amount of bad code you have ever seen work?](https://news.ycombinator.com/item?id=18442637).

---

Oracle Database 12.2.

It is close to 25 million lines of C code.

What an unimaginable horror! You can't change a single line of code in the product without breaking 1000s of existing tests. Generations of programmers have worked on that code under difficult deadlines and filled the code with all kinds of crap.

Very complex pieces of logic, memory management, context switching, etc. are all held together with thousands of flags. The whole code is ridden with mysterious macros that one cannot decipher without picking a notebook and expanding relevant pats of the macros by hand. It can take a day to two days to really understand what a macro does.

Sometimes one needs to understand the values and the effects of 20 different flag to predict how the code would behave in different situations. Sometimes 100s too! I am not exaggerating.

The only reason why this product is still surviving and still works is due to literally millions of tests!

Here is how the life of an Oracle Database developer is:

- Start working on a new bug.

- Spend two weeks trying to understand the 20 different flags that interact in mysterious ways to cause this bag.

- Add one more flag to handle the new special scenario. Add a few more lines of code that checks this flag and works around the problematic situation and avoids the bug.

- Submit the changes to a test farm consisting of about 100 to 200 servers that would compile the code, build a new Oracle DB, and run the millions of tests in a distributed fashion.

- Go home. Come the next day and work on something else. The tests can take 20 hours to 30 hours to complete.

- Go home. Come the next day and check your farm test results. On a good day, there would be about 100 failing tests. On a bad day, there would be about 1000 failing tests. Pick some of these tests randomly and try to understand what went wrong with your assumptions. Maybe there are some 10 more flags to consider to truly understand the nature of the bug.

- Add a few more flags in an attempt to fix the issue. Submit the changes again for testing. Wait another 20 to 30 hours.

- Rinse and repeat for another two weeks until you get the mysterious incantation of the combination of flags right.

- Finally one fine day you would succeed with 0 tests failing.

- Add a hundred more tests for your new change to ensure that the next developer who has the misfortune of touching this new piece of code never ends up breaking your fix.

- Submit the work for one final round of testing. Then submit it for review. The review itself may take another 2 weeks to 2 months. So now move on to the next bug to work on.

- After 2 weeks to 2 months, when everything is complete, the code would be finally merged into the main branch.

The above is a non-exaggerated description of the life of a programmer in Oracle fixing a bug. Now imagine what horror it is going to be to develop a new feature. It takes 6 months to a year (sometimes two years!) to develop a single small feature (say something like adding a new mode of authentication like support for AD authentication).

The fact that this product even works is nothing short of a miracle!

I don't work for Oracle anymore. Will never work for Oracle again!