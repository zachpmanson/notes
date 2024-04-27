Task environment is the full scope of a problem [[agents]] must solve.  They are encapsulated by performance, environment, actuators, sensors. is the full scope of a problem an agent must solve.  They are encapsulated by performance, environment, actuators, sensors.

## Attributes of an Environments

They can be fully, partially, or not observable.

Environments can be deterministic or nondeterministic. Most real situations are so complex they may as well be nondeterministic.  Sometimes people say stochastic as a synonym of deterministic. [[Artificial Intelligence - A Modern Approach]] prefers stochastic to refer to models with explicit probabilities, and nondeterministic to refer to non-explicit probabilities.

They can be sequential or episodic, where classification tasks would be be episodic and a chess game would be sequential.

Single-agent or multi-agents. These can be cooperative or adversarial.

Static or dynamic (or semidynamic), does the environment change over time.

Discrete or continuous, which applies to the state mode, to time, to percepts, and to actions of the agent.

Known or unknown "laws of physics" of the environment.  E.g. does the chess model actually know the rules of chess.

## Representations of Task Environments

In order of increasing expressiveness:
- atomic, black box, not internal structure, only have a single discrete piece of information about the world
	- used by many standard search algorithms, hidden markov-models, markov decision processes
- factored, vector of attributes
	- used by constraint satisfaction algorithms, propositional logic, planning, Bayesian Networks
- structured, state has objects which have attributes and relationships with other objects
	- used by first-order logic, first-order probability models, NLP

More expressiveness means can capture complexity more concisely.

Representations can also be ranked on the distance between the concepts being represented and memory locations.  A localist representation is a 1:1 mapping of these, and a distributed representation is has the concepts spread over many variables and memory locations.  Distributed representations tend to be more robust if erroneous data comes in.

