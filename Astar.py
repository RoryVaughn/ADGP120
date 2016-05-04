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
				
		
	def ManDis (self, Node1, Node2):
		Xdis = abs(Node1.pos[0]-Node2.pos[0])
		Ydis = abs(Node1.pos[1]-Node2.pos[1])
		#print Xdis, ",", Ydis
		Node2.h = Xdis + Ydis
		
	
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
		neNode = SearchSpace[Northwest]
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
		
			
		node.adj = [North,South,East,West,Northeast,Northwest,Southeast,Southwest]
		
		
		
		for a in adj:
			if a in self.searchSpace:
				node.adj.append(self.SearchSpace[a])
				print(SearchSpace[a])
				
		#self.SearchSpace[adj[0]].g = 0
		#self.SearchSpace[adj[1]].g = 10
		#self.SearchSpace[adj[2]].g = 10
		#self.SearchSpace[adj[3]].g = 10
		#self.SearchSpace[adj[4]].g = 10
		#self.SearchSpace[adj[5]].g = 14
		#self.SearchSpace[adj[6]].g = 14
		#self.SearchSpace[adj[7]].g = 14
		#self.SearchSpace[adj[8]].g = 14
		
		print "North: ", North, ", South: ", South, ", West: ", West, ", East: ", East
		print "Northwest: ", Northwest, ", Northeast: ", Northeast, ", Southeast: ", Southwest, ", Southeast: ", Southeast
	
	def FindFScore(array):
		for element in array:
			list.sort(array)
			return(array[0])
		print ("List: ", array[0])