import pygame
from Astar import *
from random import randint

def main():
	rows = 10
	col = 10
	id = 0
	neighbors = []
	#create the search space to look through
	searchSpace = []
	for y in range(col):
		for x in range(rows):
			n = Node(x, y, id)
			id+=1
			#x goes right
			#y goes down
			
			unwalkable = True if (x >= 1 and x <= 8 and y >= 1 and y <= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			n.setWalk(unwalkable)
			
			for x in range(rows):
				if n.id == randint(40,60): #randomly sets unwalkable nodes in the 4th, 5th, and 6th row
					n.walkable = False
			
			searchSpace.append(n) #adds the nodes to the searchspace
	

	Instance = Astar(searchSpace, searchSpace[23], searchSpace[85])
	# This creates the Astar and sets seachspace, the start node, and the goal node.
	
	#The following code is what sets the H value to all of the nodes
	c = 0 # c is the index of the node that the h score will be set to.
	for j in searchSpace: #for each node in search space (0-99)
		n.H = Instance.ManDis(searchSpace[23], searchSpace[c]) #Gets the Manhattand Distance AKA the H score
		c+=1

#############################################################

	start = searchSpace[23]
	Instance.OPEN.append(start) # Adds the start node to the open list
	
	#THIS IS THE ASTAR LOOP
	while Instance.OPEN:
		current = Instance.FindLowestF(Instance.OPEN)
		#finds lowest F and sorts by lowest F
		Instance.CLOSED.append(current)	
		#Adds the current node to the closed 
		Instance.OPEN.remove(current)
		#removes the current node from the open list.
		Instance.FindAdj(current)
		#checks the 8 adjacent squares unless if they are not walkable, or in the closed list.
		#if it isnt already in the open list it adds it there.
		#then makes it the parent of the current square.
		if Instance.Goal in Instance.OPEN or Instance.OPEN[0] == None:
			break;
			#stops the loop when the goal is in the open list bescause the path has been found
			#or stops when every checkable node in range has been chacked and the goal node is not reachable.

	print "Goal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
###############################################################
	Instance.GeneratePath()
	
	# Initialize pygame
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [700, 500]
	screen = pygame.display.set_mode(WINDOW_SIZE)
	

	# Set title of screen
	pygame.display.set_caption("Astar")

	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	# -------- Main Program Loop -----------
	while not done:
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT:  # If user clicked clrwssddfdose
				done = True	 # Flag that we are done so we exit this loop

		# Set the screen background
		screen.fill((0,0,0))
 
		for i in searchSpace:
			i.draw(screen, (255,255,255))
			
			
		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()

