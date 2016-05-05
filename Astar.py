import pygame as gfx
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Node:
	def __init__(self, M_x, M_y, M_id):
		self.parent = None		
		self.id = M_id
		self.color = WHITE
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  M_x + self.margin
		self.top = (self.margin + self.height) *  M_y + self.margin
		self.walkable = True
		self.pos = (M_x, M_y)
		self.xPos = M_x
		self.yPos = M_y
		self.f = 0
		#f is g + h
		self.g = 0
		#g is the triangle thing with 0, 10, 14, and 20
		self.h = 0
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
	def __init__(self, M_SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []		
		self.Start = Start
		self.Goal = Goal
		self.SearchSpace = M_SearchSpace
		self.currentNode = Start
		
		
	def ManDis (self, Node1, Node2):
		Xdis = abs(Node1.pos[0]-Node2.pos[0])
		Ydis = abs(Node1.pos[1]-Node2.pos[1])
		#print Xdis, ",", Ydis
		Node2.h = Xdis + Ydis
		
	def Start(self):
		#sets the current node to the starting node.
		self.currentNode = self.start
		#Add to the Open List
		self.OPEN.append(self.currentNode)
		FindAdj(self.currentNode)
		
			
		
		self.OPEN.remove(self.currentNode)
		self.CLOSED.append(self.currentNode)
		
		
		
	
	
			

	
	
	def FindAdj (self, CurrentNode):
		node = CurrentNode
		
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
		neNode = self.SearchSpace[Northeast]
		nwNode = self.SearchSpace[Northwest]
		sNode = self.SearchSpace[South]
		swNode = self.SearchSpace[Southwest]
		eNode = self.SearchSpace[East]
		seNode = self.SearchSpace[Southeast]
		nNode = self.SearchSpace[North]
		wNode = self.SearchSpace[West]
		
		
		
		if CurrentNode.id % rows == 0:
			West = 200
			Northwest = 200
			Southwest = 200
		if CurrentNode.id % rows == (rows - 1):
			East = 200
			Northeast = 200
			Southeast = 200
		if id == 200:
			node.walkable = False
		
			
		node.adj = [North,South,East,West,Northeast,Northwest,Southeast,Southwest]
		
		neNode.g = 14
		eNode.g = 10
		seNode.g = 14
		swNode.g = 14
		sNode.g = 10
		nNode.g = 10
		nwNode.g = 14
		wNode.g = 10
		
		print "North: ", North, ", South: ", South, ", West: ", West, ", East: ", East
		print "Northwest: ", Northwest, ", Northeast: ", Northeast, ", Southeast: ", Southwest, ", Southeast: ", Southeast
		return North,South,East, West, Northeast, Northwest, Southwest, Southeast
	def FindFScore(array):
		for element in array:
			list.sort(array)
			return(array[0])
		print ("List: ", array[0])