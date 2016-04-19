import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = WHITE
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		self.f = None
		self.g = None
		self.h = None

	def draw(self, screen, color):
		margin = self.margin
		color = (0, 0, 255) if (self.walkable) else (255,0,0)
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, val):
		self.h = val
	def setG(self, val):
		self.g = val

		
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)

screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Astar")
 

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
	
while not done:
    #Main event loop
	#
	
    for event in pygame.event.get():
	
	
        if event.type == pygame.QUIT:
            done = True
 
   
 
    
    screen.fill(BLACK)
 
    
 
   
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()