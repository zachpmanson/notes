ReAct prompting is a technique that allows LLMs to outsource tasks to specialised tools to expand their capabilities. This works by prompting the LLM to respond in a thought/act/observation loop, where it follows this chain of events (taken from [here](https://interconnected.org/home/2023/03/16/singularity)):

> Thought: Let’s think step by step. I need to find out X and then do Y.
> Act: Search Wikipedia for X
> *LLM waits for response*.
> Observation: From the Wikipedia page I have learnt that …
> Thought: So the answer is …

The act clause is the LLM selecting from a limited number of options that is has been informed of ahead of time, such as searching Wikipedia, entering a calculation into a calculator, searching a database etc.. A ReAct harness program will detect the act clause, take the action, and feed the result back into LLM.  The LLM then uses this data to inform its answer.  This is similar to how Bing Chat's Sydney AI works.

Here is an example flow by Simon Willison:

> > **Question:** Population of Paris, squared? 
> > **Thought:** I should look up the population of paris and then multiply it
> > **Action:** search_wikipedia: Paris
>
>Then it stops. Your code harness for the model reads that last line, sees the action and goes and executes an API call against Wikipedia. It continues the dialog with the model like this:
>
> > **Observation:** <truncated content from the Wikipedia page, including the 2,248,780 population figure>
> 
> The model continues:
>
>> **Thought:** Paris population is 2,248,780 I should square that
>> **Action:** calculator: 2248780 ** 2
>
>Control is handed back to the harness, which passes that to a calculator and returns:
>
>> **Observation:** 5057011488400
>
>The model then provides the answer:
>
>> **Answer:** The population of Paris squared is 5,057,011,488,400

This allows the capabilities of the LLM to be expanded extremely easily.  This is Willison's  example prompt to set up this user flow for a [toy implementation](https://til.simonwillison.net/llms/python-react-pattern):

```
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.
Your available actions are:
calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary
wikipedia:
e.g. wikipedia: Django
Returns a summary from searching Wikipedia
simon_blog_search:
e.g. simon_blog_search: Django
Search Simon's blog for that term
Always look things up on Wikipedia if you have the opportunity to do so.
Example session:
Question: What is the capital of France?
Thought: I should look up France on Wikipedia
Action: wikipedia: France
PAUSE
You will be called again with this:
Observation: France is a country. The capital is Paris.
You then output:
Answer: The capital of France is Paris
```

LangChain's codebase provides [more examples with greater detail](https://github.com/hwchase17/langchain/blob/2f6833d4334f762d2abb070a5e1496fc560c5435/langchain/agents/react/wiki_prompt.py#L5).

## Links

- [ReAct website](https://react-lm.github.io/)
- [LangChain](https://github.com/hwchase17/langchain), a python library for connecting LLMs to other tools
- [The surprising ease and effectiveness of AI in a loop](https://interconnected.org/home/2023/03/16/singularity)
	- interesting dicussion of ReAct using [LangChain](https://langchain.readthedocs.io/en/latest/)
- [Could you train a ChatGPT-beating model for $85,000 and run it in a browser?](https://simonwillison.net/2023/Mar/17/beat-chatgpt-in-a-browser/)
	- discusses alpaca.cpp, ReAct prompting and the ability to easily expand the capabilities of LLMs, even basic ones
	- includes a basic ReAct prompting script with ChatGPT APIs
- [Fuzzy API composition: querying NBA stats with GPT-3 + Statmuse + Langchain](https://www.geoffreylitt.com/2023/01/29/fun-with-compositional-llms-querying-basketball-stats-with-gpt-3-statmuse-langchain.html)
	- ReAct prompting in use
- [Build a GitHub Support Bot with GPT3, LangChain, and Python](https://dagster.io/blog/chatgpt-langchain)