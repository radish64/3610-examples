def mst_kruskal(graph):
	mst = []
	edges = []
	for node in range(len(graph)): #O(E+V)
		for neighbor, weight in graph[node]:
			if node < neighbor: #deduplication
				edges.append((weight,node,neighbor))
	edges.sort() #O(ElgV)
	ds = Disjointset()
	for node in range(len(graph)): #O(V)
		ds.make_set(node)
	#enter loop E times 
	for weight,node,neighbor in edges: 
		if ds.find(node) != ds.find(neighbor): #2E "find" calls
			#V-1 times (size of mst) = approx V "union" calls
			mst.append[(node,neighbor,weight)]
			ds.union(node,neighbor)
	return mst

#assume connected graph
#runtime: O(ElgV)

