#archangel maze challenge

'''
A maze consists of a block of cells, defined as a n by m matrix. The cells within the maze are
either X, O, or S. An S denotes the starting point, an O denotes an open cell which can be
passed through, and an X denotes a wall, which cannot be passed through. The game is
complete when the S reaches the edge of the maze. Consider the following example of a 6 *
5 maze:
XOXXXX
XOXOOX
XOXOXX
XOOOSX
XXXXXX
Write code in a language of your choice which will solve mazes similar to the one in the
example above. You do not have to find the shortest path to the exit.
Optional bonus tasks you could attempt or describe how you would approach:
● Find the shortest path
● Find all paths
● Optimise your algorithm to find a path (any path) as quickly as possible
● Expand to three dimensional mazes
Deliver as source code with a readme explaining how to execute it.
It is expected to spend no more than a few hours on this task.
'''


'''
Hayder's solution. 

I looked at a number of potential algorithms for graph/tree traversal. 

I chose the D* Lite as it combines A* with incremental search to shorten the path. 

I could have written an implementation, but there's already a decent example on github 
which can be found here. 

https://github.com/samdjstephens/pydstarlite


'''

