Complexity classes are sets of computational problems, organised by the resources required to solve them.  Most commonly this involves decision problems solvable using Turing machines and the relative time and memory problems would require under that model.

## Properties

### Hardness
A problem X is hard for class C is every problem in C can be polynomial-time reduced to X, meaning no problem in C is harder than X.  Any algorithm that can solve X can solve all problems in C.

### Completeness
A problem X is complete for class C if it is hard for C and contained within C.  This makes X the hardest possible problem within C (or one of many equally hard hardest problems in C).

## Classes
These are in order of hardness, according to L = SL ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE = NPSPACE.

### L
Class L is the set of decision problems that can be solved by a deterministic Turing machine using a **l**ogarithmic amount of memory.  An example of this kind of problem is detemining whether a graph has a directed cycle. It is also called LSPACE.

#### SL
Class SL (**s**ymmetric **l**ogspace) is the set of problems that can reduced to USTCON (undirected s-t connectivity, aka the **undirected reachability problem**).  USTCON is the problem of determining whether there exists a path between two vertices in an undirected graph.  This problem is SL-complete.

SL was first defined in 1982 by Harry R. Lewis and Christos Papadimitriou.  It was originally distinct from L since USTCON wasmconsidered NL at the time but didn't seem to require non-determinisim.  They defined the symmetric Turing machine and used it to define SL.  They showed that USTCON was complete for SL and proved that L ⊆ SL ⊆ NL.

In October 2004 Omer Reingold proved that SL = L and as a consequence, symmetric Turing machines are equivalent to deterministic Turing machines when limited to log space.

### NL
Class NL is the set of decision problems that can be solved by a **n**on-deterministic Turing machine using a **l**ogarithmic amount of memory. An example of an NL problem is the STCON (directed s-t connectivity aka the **directed reachability problem**), which is NL-complete.

### P
Class P is the set of decision problems that are solvable on a deterministic Turing machine in **p**olynomial time.  These problems are generally considered to be tractable.  This class is  also called PTIME.  An example of a P problem is determining if a number is prime.

### NP
Class NP is the set of decision problems that are solvable on a **n**on-deterministic Turing machine in **p**olynomial time.  It is an open question whether `P = NP`, though it's widely believed that `P != NP`.  An example of an NP problem is the travelling salesman problem.

#### NP-Intermediate
Problems that aren't P but also aren't NP-complete are NP-intermediate. P = NP iff NP-intermediate is empty.  Some problems that are considered good candidates for being NP-intermediate are the graph isomorphism problem, factoring, and computing the discrete logarithm.

We haven't actually definitively proved this class exists.

#### NP-Complete
There are many important NP-complete problems.  Famous examples include the travelling salesman problem (TSP), the knapsack problem and the boolean satisfiability problem.   Many important problems have been shown to be NP-complete, and no fast algorithm for any of them is known

## Links
- [Wikipedia's list of complexity classes](https://en.wikipedia.org/wiki/List_of_complexity_classes)

