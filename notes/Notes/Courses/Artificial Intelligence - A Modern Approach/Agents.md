An agent is something that acts.  For computer agents this includes "operate autonomously, perceive their environment, persist over a prolonged time period, adapt to change, and create and pursue goals"

A rational agent is one that is able to operate when there is uncertainty.

> For each possible percept sequence, a rational agent should select an action that is ex- pected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

-- [[AIMI Chapter 02]]

An agent can perceive its environment with sensors and act upon the environment with actuators. Sensors perceive percepts. A percept sequence is everything an agent has ever perceived.  An agents behaviour can be described with agent function that maps any percept sequence to an action.

Agents have performance measures that are the goals they aim to achieve.  Often information gathering is a rational decision to make in order to achieve goals.

They exists within [[Task Environments]].

## Types of Agents

- **reflex agent**: if statements or lookup tables
- **model-based reflex agent**: reflex agent that has internal state and so can keep track of parts of the world it can't see yet
	- updating internal state also requires a transition model for how the world changes
	- needs a sensor model to interpret percept input into world information
- **goal based agent**: keeps track of world state and a set of goals it is trying to achieve, and is able to estimate how it actions will impact its goals. It may be able to engage in searching for and planning solutions 
- **utility-based agents**: based on a utility function that can rate the desirability of any given state based on performance measure, and then picks actions that produce the highest expected utility
- **learning agents**: an agent that builds, tests, critiques and iteratively improves other agents to solve a problem