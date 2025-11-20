Notes on various LLMs and the techniques used to make them.

> LLMs are better thought of as "calculators for words" - retrieval of facts is a by-product of how they are trained, but it's not their core competence at all.

--[Simon Willison](https://news.ycombinator.com/item?id=35396372) on HN, which he later [expanded on](https://simonwillison.net/2023/Apr/2/calculator-for-words/)

## LLM Families

![](https://raw.githubusercontent.com/pavo-etc/llm-family-tree/master/LLMfamily.drawio.png)  
[Source](https://github.com/pavo-etc/llm-family-tree)

A more comprehensive list of models:  
[2023 LifeArchitect.ai data (shared)](https://docs.google.com/spreadsheets/u/0/d/1O5KVQW1Hx5ZAkcg8AIRjbQLQzx2wVaLl0SqUu-ir9Fs/htmlview#gid=1158069878)

## Comparisons 

> > hyperopt:  
> > Does anyone know of any good test suites we can use to benchmark these local models? \[...\]
> 
> aiappreciator:  
> The simplest and quickest benchmark is to do a rap battle between GPT-4 and the local models. \[...\]
> 
> It is instantly clear how strong the model is relative to GPT-4.

--[this HN thread](https://news.ycombinator.com/item?id=35349853)

## Interesting Articles

- [We Have No Moat, And Neither Does OpenAI](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither), a leaked internal Google document about the success of open source models and how to change their approach against OpenAI
- [Kinds of Stealing](https://seths.blog/2025/11/kinds-of-stealing/)

## Links

- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM), a curated list of papers about large language models, especially relating to ChatGPT. It also contains frameworks for LLM training, tools to deploy LLM, courses and tutorials about LLM and all publicly available LLM checkpoints and APIs.
- [LLM Tracker](https://docs.google.com/spreadsheets/d/1kT4or6b0Fedd-W_jMwYpb63e1ZR3aePczz3zlbJW-Y4), a spreadsheet detailing the different LLMs and their properties
- [Brex's Prompt Engineering Guide](https://github.com/brexhq/prompt-engineering)
- [The Secret Sauce behind 100K context window in LLMs: all tricks in one place](https://blog.gopenai.com/how-to-speed-up-llms-and-use-100k-context-window-all-tricks-in-one-place-ffd40577b4c)