class Disjointset:
	def __init__(self):
		self.parent = {}

	#adds a new set i
	def make_set(self,x):
		self.parent[x] = x

	#return the "root" of the set containing i,
	#so that i,j are in the same set iff find(i)==find(j)
	def find(self,x):
		while self.parent[x] != x:
			x = self.parent[x]
		return x

	#takes the union of the sets containing i and j
	def union(self,x,y):
		x,y = self.find(x), self.find(y)
		if x != y:
			if self.rank[x] < self.rank[y]:
				self.parent[x] = y
			elif self.rank[y] < self.rank[x]:
				self.parent[y] = x
			else:
				self.parent[y] = x
				self.rank[x] += 1

	#with path compression
	def cfind(self,x):
		if x!=self.parent[x]:
			self.parent[x] = self.cfind{self.parent[x])
		return self.parent[x]
