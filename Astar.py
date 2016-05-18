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
		self.partOfPath = False
		#f is g + h
		self.g = 0
		#g is the triangle thing with 0, 10, 14, and 20
		self.h = 0
		#h is Manhattan

	def draw(self, screen, color):
		margin = self.margin
		color = WHITE if (self.walkable) else (255,0,0)
		if(self.partOfPath == True):
			color = (0,120,120)
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
		
	def getF(self):
		return self.h + self.g
		
	def setH(self, val):
		self.h = val
		
	def setG(self, val):
		self.g = val
		
	def Fkey(Node):
		return getF(Node)

class Astar(object):
	def __init__(self, M_SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []		
		self.Start = Start
		self.Goal = Goal
		self.Parents = []
		self.SearchSpace = M_SearchSpace
		self.currentNode = Start
		self.Path = []
		for i in self.SearchSpace:
			i.h = self.Manhattan_Distance(i, self.Goal)
		
	def Manhattan_Distance(self, current, goal):
		return self.ManDis(current, goal)
	
	def Run(self):
		open = self.OPEN
		closed = self.CLOSED
		start = self.Start
		goal = self.Goal
		open.append(start)
		#THIS IS THE ASTAR LOOP
		while open:#while open is not empty
			current = self.FindLowestF(open)
			#finds lowest F and sorts by lowest F
			closed.append(current)	
			#Adds the current node to the closed 
			open.remove(current)
			#removes the current node from the open list.
			self.FindAdj(current)
			#checks the 8 adjacent squares unless if they are not walkable, or in the closed list.
			#if it isnt already in the open list it adds it there.
			#then makes it the parent of the current square.
			if goal in open:
				print "Goal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				break
			if open is None:
				print "No goal :("
				break
				#stops the loop when the goal is in the open list bescause the path has been found
				#or stops when every checkable node in range has been chacked and the goal node is not reachable.

	
		
	def GeneratePath (self):
		path = []
		next = self.Goal
		print "The Path that was found is: "
		while(next != None): 
			path.append(next)
			print ("Node (index)->"), next.id
			next.partOfPath = True  # decide whether to turn the node blue
			#self.Path.append(next) #adds the correct nodes to the path list for the final path.
			next = next.parent #tracks the list of parents in order to back track though the list of parented nodes.
		return path
	
	def ManDis (self, Node1, Node2):
		Xdis = abs(Node1.xPos- Node2.xPos)
		Ydis = abs(Node1.yPos- Node2.yPos)
		return Xdis*10 + Ydis*10 #Returns the Manhattan Distance or H score of a node from the starting square.

	def FindAdj (self, CurrentNode):
		
		rows = 10
		col = 10
		adj = []
		North 		= CurrentNode.id - rows 
		South 		= CurrentNode.id + rows
		West 		= CurrentNode.id - 1
		East 		= CurrentNode.id + 1
		Northwest 	= CurrentNode.id - rows - 1
		Northeast 	= CurrentNode.id - rows + 1
		Southwest 	= CurrentNode.id + rows - 1
		Southeast 	= CurrentNode.id + rows + 1
		
		#Resets the g score for all of the adjacent Nodes
		self.SearchSpace[Northwest].g = 14
		self.SearchSpace[Northeast].g = 14
		self.SearchSpace[Southeast].g = 14
		self.SearchSpace[Southwest].g = 14
		self.SearchSpace[North].g = 10
		self.SearchSpace[South].g = 10
		self.SearchSpace[East].g = 10
		self.SearchSpace[West].g = 10
		
		if CurrentNode.id % rows != 0:	#left check
			if(self.SearchSpace[East].walkable == True and self.SearchSpace[East] not in self.CLOSED and self.SearchSpace[East] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[East]) #add East node to the open list
				self.SearchSpace[East].parent = CurrentNode #sets the parent of the East node as the current node
				
		if CurrentNode.id % rows != 9:	# Right Check
			if(self.SearchSpace[West].walkable == True and self.SearchSpace[West] not in self.CLOSED and self.SearchSpace[West] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[West]) #add West node to the open list
				self.SearchSpace[West].parent = CurrentNode #sets the parent of the West node as the current node
				
		if CurrentNode.id > rows - 1:	# North check
			if(self.SearchSpace[North].walkable == True and self.SearchSpace[North] not in self.CLOSED and self.SearchSpace[North] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[North]) #add North node to the open list
				self.SearchSpace[North].parent = CurrentNode #sets the parent of the North node as the current node
				
		if CurrentNode.id < 90:		# South Check
			if(self.SearchSpace[South].walkable == True and self.SearchSpace[South] not in self.CLOSED and self.SearchSpace[South] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[South]) #add South node to the open list
				self.SearchSpace[South].parent = CurrentNode #sets the parent of the South node as the current node
				
		if CurrentNode.id < 90 and CurrentNode.id % rows != 9:	# Southwest Check
			if(self.SearchSpace[Southwest].walkable == True and self.SearchSpace[Southwest] not in self.CLOSED and self.SearchSpace[Southwest] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[Southwest]) #add Southwest node to the open list
				self.SearchSpace[Southwest].parent = CurrentNode #sets the parent of the Southwest node as the current node
				
		if CurrentNode.id < 90 and CurrentNode.id % rows != 0:	# Southeast Check
			if(self.SearchSpace[Southeast].walkable == True and self.SearchSpace[Southeast] not in self.CLOSED and self.SearchSpace[Southeast] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[Southeast]) #add Southeast node to the open list
				self.SearchSpace[Southeast].parent = CurrentNode #sets the parent of the Southeast node as the current node
				
		if CurrentNode.id > rows - 1 and CurrentNode.id % rows != 0:	# NorthEast
			if(self.SearchSpace[Northeast].walkable == True and self.SearchSpace[Northeast] not in self.CLOSED and self.SearchSpace[Northeast] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[Northeast]) #add Northeast node to the open list
				self.SearchSpace[Northeast].parent = CurrentNode #sets the parent of the Northeast node as the current node
				
		if CurrentNode.id > rows - 1 and CurrentNode.id % rows != 9:	#NorthWest
			if(self.SearchSpace[Northwest].walkable == True and self.SearchSpace[Northwest] not in self.CLOSED and self.SearchSpace[Northwest] not in self.OPEN):
				self.OPEN.append(self.SearchSpace[Northwest]) #add Northwest node to the open list
				self.SearchSpace[Northwest].parent = CurrentNode #sets the parent of the Northwest node as the current node
	
	
	
	def FindLowestF(self, list):	
		LowF = None 
		for a in list:	#Repeats the loop for the amount of nodes in the open list
			if LowF == None: #sets the first node to a.
				LowF = a		
			elif(a.getF() < LowF.getF()): #checks through the list in order to get the lowest F Value.
				Lowf = a #The final value that makes it through the list will be the return value.
		return LowF
		
		#Matthews stuff
		#self.OPEN.sort(key = lambda x : x.f)
		#return self.OPEN[0]