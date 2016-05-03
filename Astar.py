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
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
			
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
		adj = [Current,North,South,East,West,Northeast,Northwest,Southeast,Southwest]
		if id == 200:
			node.walkable = false
		print "North: ", North, ", South: ", South, ", West: ", West, ", East: ", East
		print "Northwest: ", Northwest, ", Northeast: ", Northeast, ", Southeast: ", Southwest, ", Southeast: ", Southeast
	
	def FindFScore(array):
		for element in array:
			list.sort(array)
		print ("List: ", array[0])
		
#1) Add the starting square (or node) to the open list.
#2) Repeat the following:
#a) Look for the lowest F cost square on the open list. We refer to this as the current square.
#b) Switch it to the closed list.
#c) For each of the 8 squares adjacent to this current square …
#If it is not walkable or if it is on the closed list, ignore it. Otherwise do the following.           
#If it isn’t on the open list, add it to the open list. Make the current square the parent of this square. Record the F, G, and H costs of the square. 
#If it is on the open list already, check to see if this path to that square is better, using G cost as the measure. A lower G cost means that this is a better path. If so, change the parent of the square to the current square, and recalculate the G and F scores of the square.
#If you are keeping your open list sorted by F score, you may need to resort the list to account for the change.
#d) Stop when you:
#Add the target square to the closed list, in which case the path has been found (see note below), or
#Fail to find the target square, and the open list is empty. In this case, there is no path.   
#3) Save the path. Working backwards from the target square, 
#go from each square to its parent square until you reach the starting square. That is your path. 