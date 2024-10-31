def dijkstra(graph, source):
	dist = [float('inf')] * len(graph)
	prev = [None] * len(graph)
	visited = set()
	while len(visited) < len(graph): #enter V times, visit all nodes once
		current = min_unvisited() #abstractly written - think about how to implement this
		visited.add(current)
		for (neighbor, weight) in graph[current]: #enter E times, we relax each edge once
			if weight + dist[current] < dist[neighbor]: #relax this edge
				prev[neighbor] = current
				dist[neighbor] = weight + dist[current]
				#decrease value of an element on a min-heap
				decrease_key()

#Runtime: 
	#O(V^2+E) with linear search
	#O(ElgV) with a heap and connected graph
