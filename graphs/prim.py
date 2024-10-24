#graph is a list of lists of edges, each edge is (neighbor, wieght)
def prim(graph):
	start_node = 0
	S = set([start_node])
	A = []
	edge_heap = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]
	heapq.heapify(edge_heap)
	#enter up to e times
	while len(edge_heap) > 0 and len(A) < len(graph)-1:
		weight,source,target = heapq.heappop(edge_heap) #lg e
		if target not in S:
			A.append((source,target))
			S.add(target)
			for(neighbor,weight) in graph[target]:
				heapq.heappush((weight,target,neighbor)) #lg e
	return A

#assume G is connected, E >= V-1
#memory is O(E), since every edge can be on the heap (up to twice)
#runtime is ElgE + ElgE = O(ElgE) (pop + push)

