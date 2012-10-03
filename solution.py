'''
Yuval Gnessin
10/2/2012
This file implements a solution to the Vertical Brands Programming Challenge:

Description:
A robot is located at the top-left corner of a 4x4 grid. The robot can move either
up, down, left, or right, but can not visit the same spot twice. The robot is trying 
to reach the bottom-right corner of the grid.

Output sample:
Print out the unique number of ways the robot can reach its destination.

Directions:
Use your favorite programming language.
The best way to submit a solution is by sending us a GitHub project link.
Feel free to clarify anything in the problem description.
'''
import sys
import queue

# Solves the above problem for a general case M x N grid using BFS
def count_paths(m, n):
    num_paths = 0
    fringe = queue.Queue()
    fringe.push(((0,0),[]))
    
    while True:
        if fringe.is_empty(): 
            break
        node = fringe.pop()
        state, path = node[0], node[1]
        
        if state in path: 
            continue
        path.append(state)
        
        if state == (m-1, n-1):
            num_paths += 1
            
        for new_state in get_next_states(state, m, n):
            fringe.push((new_state, path[:]))
            
    return num_paths
            
# Helper function
# Returns a list of valid states that follow from the given state
def get_next_states(state, m, n):
    states = []
    x, y = state[0], state[1]
    
    for nextx, nexty in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if nextx >= 0 and nexty >= 0 and nextx < m and nexty < n:
            states.append((nextx, nexty))
        
    return states
 

if len(sys.argv) == 3:
    M, N = sys.argv[1], sys.argv[2]
    print "Unique paths in a %s x %s matrix: %s" % (M, N, count_paths(int(M), int(N)))
else:
    print "Unique paths in a 4 x 4 matrix: %s" % count_paths(4, 4)