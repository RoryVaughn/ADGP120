import pygame
from Astar import *

def main():
	rows = 10
	col = 10
	id = 0
	#create the search space to look through
	searchSpace = []
	for x in range(col):
		for y in range(rows):
			print x, ",", y, "Index", id
			n = Node(x, y, id)
			id+=1
			#x goes right
			#y goes down
			
			unwalkable = True if (x >= 4 and x <= 20 and y >= 5 and y <= 14) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			n.setWalk(unwalkable)
			if n.id == 89:
				n.walkable = False
			searchSpace.append(n)
			
	dickbutt = Astar(searchSpace, searchSpace[77], searchSpace[98])
	
	#Thie following code is what sets the H value to all of the nodes
	c = 0
	for j in searchSpace:
		n.H = dickbutt.ManDis(searchSpace[77], searchSpace[c])
		c+=1
	#################################
	dickbutt.Run
	
	
	
	
	
	
	
	#dickbutt.ManDis (searchSpace[0], searchSpace[10])
	Node3 = Node (x -1,y -1,id -1)
	dickbutt.FindAdj (Node3)
	print(searchSpace[78].g)
	
	
	
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

