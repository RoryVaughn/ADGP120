import pygame as gfx
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
		self.pos = (x, y)
		self.xPos = x
		self.yPos = y
		self.f = None
		self.g = None
		self.h = None

	def draw(self, screen, color):
		margin = self.margin
		color = WHITE if (self.walkable) else (255,0,0)
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, val):
		self.h = val
	def setG(self, val):
		self.g = val

class Astar:
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []		
		self.Start = Start
		self.Goal = Goal
		self.SearchSpace = SearchSpace
		self.currentNode = Start
		
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
			
	def LowestF(self, Nodes):
		lowestF = -1
		nodeWithLowestF = None
		for node in Nodes:
			if(node.f > lowestF):
				lowestF = node.f
				nodeWithLowestF = node
		return nodeWithLowestF
		
	def ManDis (self, Node1, Node2):
		Xdis = abs(Node1.pos[0]-Node2.pos[0])
		Ydis = abs(Node1.pos[1]-Node2.pos[1])
		print Xdis, ",", Ydis
		return Xdis, Ydis
	
	#def FindAdj (self):
		#for n in self.SearchSpace:
			
			
		
	
	

def FindFScore(array):
	for element in array:
		list.sort(array)
	print ("List: ", array[0])
	
#FindFScore(Node)