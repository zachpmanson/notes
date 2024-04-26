---
tags:
  - git
---


[Steve Losh's wisdom](https://stevelosh.com/blog/2013/04/git-koans/).

---

## Silence

A Python programmer handed her `~/.gitconfig` to Master Git. Among the many lines were the following:

```
[alias]
; Explicit is better than implicit.  If we want to merge
; we should do so ourselves.
pull = pull --ff-only
```

Master Git nodded. "`git pull origin master`," said the programmer.

Master Git pulled down the latest changes on `master` and automatically merged them with the programmer's changes.

"But Master Git, did I not say to only fast-forward in my configuration?!" she cried.

Master Git looked at her, nodded, and said nothing.

"Then why did you not warn me of a problem with my configuration?" she asked.

Master Git replied: "there was no problem."

Months later the programmer was reading `git --help config` for a different reason and found enlightenment.

## One Thing Well

A UNIX programmer was working in the cubicle farms. As she saw Master Git traveling down the path, she ran to meet him.

"It is an honor to meet you, Master Git!" she said. "I have been studying the UNIX way of designing programs that each do one thing well. Surely I can learn much from you."

"Surely," replied Master Git.

"How should I change to a different branch?" asked the programmer.

"Use `git checkout`."

"And how should I create a branch?"

"Use `git checkout`."

"And how should I update the contents of a single file in my working directory, without involving branches at all?"

"Use `git checkout`."

After this third answer, the programmer was enlightened.

## Only the Gods

The great historian was trying to unravel the intricacies of an incorrect merge that had happened many months ago. He made a pilgrimage to Master Git to ask for his help.

"Master Git," said the historian, "what is the nature of history?"

"History is immutable. To rewrite it later is to tamper with the very fabric of existence."

The historian nodded, then asked: "Is that why rebasing commits that have been pushed is discouraged?"

"Indeed," said Master Git.

"Splendid!" exclaimed the historian. "I have a historical record of a merge commit with two parents. How can I find out which branch each parent was originally made on?"

"History is ephemeral," replied Master Git, "the knowledge you seek can be answered only by the gods."

The historian hung his head as enlightenment crushed down upon him.

## The Hobgoblin

A novice was learning at the feet of Master Git. At the end of the lesson he looked through his notes and said, "Master, I have a few questions. May I ask them?"

Master Git nodded.

"How can I view a list of *all* tags?"

"`git tag`", replied Master Git.

"How can I view a list of *all* remotes?"

"`git remote -v`", replied Master Git.

"How can I view a list of *all* branches?"

"`git branch -a`", replied Master Git.

"And how can I view the current branch?"

"`git rev-parse --abbrev-ref HEAD`", replied Master Git.

"How can I delete a remote?"

"`git remote rm`", replied Master Git.

"And how can I delete a branch?"

"`git branch -d`", replied Master Git.

The novice thought for a few moments, then asked: "Surely some of these could be made more consistent, so as to be easier to remember in the heat of coding?"

Master Git snapped his fingers. A hobgoblin entered the room and ate the novice alive. In the afterlife, the novice was enlightened.

## The Long and Short of It

Master Git and a novice were walking along a bridge.

The novice, wanting to partake of Master Git's vast knowledge, said: "`git branch --help`".

Master Git sat down and lectured her on the seven forms of `git branch`, and their many options.

They resumed walking. A few minutes later they encountered an experienced developer traveling in the opposite direction. He bowed to Master Git and said "`git branch -h`". Master Git tersely informed him of the most common `git branch` options. The developer thanked him and continued on his way.

"Master," said the novice, "what is the nature of long and short options for commands? I thought they were equivalent, but when that developer used `-h` you said something different than when I said `--help`."

"Perspective is everything," answered the Master.

The novice was puzzled. She decided to experiment and said "`git -h branch`".

Master Git turned and threw himself off the railing, falling to his death on the rocks below.

Upon seeing this, the novice was enlightened.