{% include mathjax.html %} 

Advent of Code Day 3 {#aoc-2022-3}
======================================

Both solutions to this can be done primarily by splitting the input, either by splitting the string in Part 1 or grouping indices in Part 2, 
and then using set intersections to find the character solution. Once done, the integer solution to each sub-problem is a mapping from the 
character to the integer counterpart. Modern computers store $A = 65$ and $a = 97$ with subsequent characters being offset by these bases. 
Using this, the transformation from characters to integers is
\begin{equation}f(x) = \begin{cases} x - 96 & \text{if } x > 96 \\\\ x - 38 & \text{otherwise.} \end{cases}.\end{equation}
The final solution is just the sum of the integer solutions.
