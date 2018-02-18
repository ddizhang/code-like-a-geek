class Vertex:
	def __init__(self, key):
		self.key = key
		self.connectTo = {}
		# used in bfs
		self.status = 'initial'
		self.pred = None
		self.dist = 0

	# nbr is a vertex object
	def addNeighbor(self, nbr, weight):
		self.connectTo[nbr] = weight

	def getNeighbors(self):
		return self.connectTo



class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertex = 0

	def addVertex(self, key):
		newVert = Vertex(key)
		self.vertList[key] = newVert
		self.numVertex += 1
		return newVert

	def getVertex(self, key):
		return self.vertex[key]

	def __contains__(self, key):
		return key in self.vertList

	def addEdge(self, fr, to, cost = 0):
		if fr not in self:
			self.addVertex(fr)
		if to not in self:
			self.addVertex(to)

		fr_vert = self.vertList[fr]
		fr_vert.addNeighbor(self.vertList[to], cost)

