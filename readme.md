x goes first
approx 2 * 3**9 == 39_366 possible states
terminal states have gain of 1, 0, or -1

the fitness of a no choice move
```
p(hap) = p0hap + p0mid*p0sad + p0mid^2*p0hap + p0mid^3 * p0sad ...
       = p0hap/(1-p0mid^2) + p0mid*p0sad/(1-pmid^2)
```
we can check this
```
phap + psad = p0hap/(1-p0mid^2) + p0sad/(1-p0mid^2) + p0mid*p0sad/(1-pmid^2) + p0mid*p0hap/(1-pmid^2)
            = (1 - p0mid)/(1-p0mid^2) + p0mid(1 - p0mid)/(1-p0mid^2)
            = 1
```

if we had a playbook, we could evaluate its efficacy with a solver

To make a move, you need to know what your opponent would do if you :/.
However, to make a move from the same board state,
your opponent needs to know what you would do from that board state.
To plan a move, for each choice, assume that your opponent saw you move and get :/
and now assumes you would make the same move again until you didn't :/.
You can now determine their optimal strategy under that assumption,
and find out which original move gives them the worst optimal strategy.