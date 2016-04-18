import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
width = 20
height = 20
margin = 5
left = (margin + width) *  margin
top = (margin + height) *  margin

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
	pygame.draw.rect(screen, WHITE, (left , top, width, height))
	
        if event.type == pygame.QUIT:
            done = True
 
   
 
    
    screen.fill(BLACK)
 
    
 
   
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()