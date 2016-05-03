import pygame as gfx
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Node:
	def __init__(self, x, y, id):
		self.parent = None		
		self.id = id
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
		#f is g + h
		self.g = None
		#g is the triangle thing with 0, 10, 14, and 20
		self.h = None
		#h is Manhattan

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
		
		while not self.OPEN and not self.Goal in self.OPEN:
			current = self.FindFScore(self.OPEN)
			self.FindAdj(current)
			self.OPEN.append(adj)
			self.OPEN.remove(current)
			self.CLOSED.append(current)
				
			
			
	#This is the f Score finder that Matthew that doesnt work.
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
		
	
	def FindAdj (self, CurrentNode):
		#for n in self.SearchSpace:
		rows = 10
		col = 10
		adj = []
		Current = CurrentNode.id
		North = CurrentNode.id - rows 
		South = CurrentNode.id + rows
		West = CurrentNode.id - 1
		East = CurrentNode.id + 1
		Northwest = CurrentNode.id - rows - 1
		Northeast = CurrentNode.id - rows + 1
		Southwest = CurrentNode.id + rows - 1
		Southeast = CurrentNode.id + rows + 1
		if CurrentNode.id % rows == 0:
			West = 200
			Northwest = 200
			Southwest = 200
		if CurrentNode.id % rows == (rows - 1):
			East = 200
			Northeast = 200
			Southeast = 200
		if id == 200:
			node.walkable = false
		
			
		adj = [Current,North,South,East,West,Northeast,Northwest,Southeast,Southwest]
		
		print "North: ", North, ", South: ", South, ", West: ", West, ", East: ", East
		print "Northwest: ", Northwest, ", Northeast: ", Northeast, ", Southeast: ", Southwest, ", Southeast: ", Southeast
	
	def FindFScore(array):
		for element in array:
			list.sort(array)
			return(array[0])
		print ("List: ", array[0])