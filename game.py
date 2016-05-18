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
			print x, ",", y, "Index", id
			n = Node(x, y, id)
			id+=1
			#x goes right
			#y goes down
			
			#unwalkable = True if (x >= 1 and x <= 8 and y >= 1 and y <= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			#n.setWalk(unwalkable)
			
			#for x in range(rows):
				#if n.id == randint(40,60):
					#n.walkable = False
			
			searchSpace.append(n)
	

	Instance = Astar(searchSpace, searchSpace[23], searchSpace[85])
	
	
	#The following code is what sets the H value to all of the nodes
	c = 0
	for j in searchSpace:
		n.H = Instance.ManDis(searchSpace[23], searchSpace[c])
		c+=1
	
	#################################
	'''
	Instance.OPEN.append(searchSpace[23])
	Finished = False
							#
	variable = Instance.FindLowestF(Instance.OPEN)
	#finds lowest F and sorts by lowest F.
	print variable
	Instance.CLOSED.append(variable)
	Instance.Parents.append(variable)
		#adds the (current node) to the closed list.
	neighbors = Instance.FindAdj (variable)
		#finds the neighbors of the current node.
	print neighbors
	Instance.OPEN.remove(variable)
		#removes the current node from the open list.
	Instance.OPEN.append(neighbors)
	#if Instance.CLOSED == searchSpace[85] or Instance.OPEN == None:
			#Finished = True
	print(Instance.Parents)
		#adds the neigbor nodes to the open list.
	'''
	start = searchSpace[23]
	Instance.OPEN.append(start)
	
	Finished = False
	#while Finished == False:
	while Instance.OPEN:
		current = Instance.FindLowestF()
		#finds lowest F and sorts by lowest F
		Instance.CLOSED.append(current)		
		Instance.FindAdj(current)
		
		Instance.OPEN.remove(current)
		
		if Instance.Goal in Instance.OPEN or Instance.OPEN[0] == None:
			break;

	print "Goal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	
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


	#while not over:
		#variable = Instance.FindFScore(Instance.OPEN)
		#finds lowest F and sorts by lowest F.
		#print variable
		#Instance.CLOSED.append(variable)
		#adds the lowers(current node) to the closed list.
	
		#print Instance.OPEN[0]
		#neighbors = Instance.FindAdj (variable)
		#finds the neighbors of the current node.
		#print neighbors
		#Instance.OPEN.remove(variable)
		#removes the current node from the open list.
		#Instance.OPEN.append(neighbors)
		#adds the neigbor nodes to the open list.
		
		#if searchSpace[85] in Instance.CLOSED:
		#	over = True
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

