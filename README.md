# ADGP120
Python Astar project

The program in it's current state does find the static goal of node [85] from the starting node [23], using the A Star algorithm.

The white nodes are walkable nodes, the red nodes are unwalkable nodes(and therefore untargetable for the path) The program highlights the path that it chooses from the white nodes, as the blue nodes.

The program also prints the list of nodes in the "parent" list.

The Astar algorithm that I implement in Python for ADGP120 is a pathfinding algorithm that could pass for AI or Artificial Inteligence.

An algorithm is something that should be implemented is such a way that it can just be called from the main, and it will run the algorithm(as in a class that can be created as an instance and use its own functions to complete its task). It should not be spaghetti code that is littered thoughout the main.

That algorithm should be as follows:

1: Add the starting node to the Open list.

2: Check the Open list for the node with the lowest F cost(this will be used as the current node)

3: Swap the current node to the closed list.

4: Check the current node for its adjacent nodes
(North, South, West, East, Northeast, Northwest, Southeast, Southwest.)
For all of these nodes, if the node is in the closed list, already in the open list, or not walkable, then ignore it. 
If the node passes the following tests, then add it to the Open list and set its parent to the current node.

5: Unless if the target is in the Open list, or the Open list is empty; Go back to step 2

6: If the Open list is empty, then the target is not able to be found.
   If the target is in the Open list, then you have found the path to the target and can backtrack your way using the nodes' parents from the goal node to the starting node.