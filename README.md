Reassurance/warning: The amount of code you have to write for this assignment is small, but it can be confusing if you're shaky on the concept of reduction. Start early. Ask questions, if the ideas are not clear.

The goal is to implement N-Coloring by reducing it to SAT, then use a SAT library to solve the problem. Most of the code is provided for you; you just have to fill in a few spots.

You start with an undirected graph. The problem is to determine if it's possible to color each of the vertices with one of N colors, such that no two connected vertices have the same color. (Fun fact: 2-colorable graphs are bipartite graphs.)

The reduction works like this: For each vertex in the graph, create a collection of N variables in the SAT problem that encode the color of that vertex. In particular, variable N × i + c should be true iff vertex "i" is colored "c". The "names" of the vertices are just numbers (1, 2, ..., |V|). The "names" of the SAT variables are also just numbers. You shouldn't need to think about these numbers much if you use the supplied "var" function correctly.

The generated SAT formula needs three collections of clauses to implement Coloring properly:

It is necessary to enforce that at least one of each vertex's color variables is true.
It is necessary to enforce that at most one of each vertex's color variables is true.
For each edge it is necessary to enforce that the vertices on either side of that edge do not have the same color.
The first two clauses/collections of clauses together ensure that a satisfying assignment will correspond to each vertex having a color.

The third collection of clauses ensure that the adjacent color condition is enforced.

There are 5 "TODO"s in the skeleton code that you have to fill in.

You need to make two interesting (but don't go overboard) graphs as tests. You're not expected to make input generators for this one (but that would be fun).

See the recently created Discussion, if you're having trouble installing pycosat.


