def bellmanford(graph,source):
	n = len(graph)
	dist = [float('inf')] * n
	prev = [None] * n
	dist[source] = 0
	for i in range(n-1): #V-1 times
		for node in range(n): #V times
			for neighbor,weight in graph[node]: #E times for each outermost loop
				#"relax" node --weight--> neighbor
				if dist[node] + weight < dist[neighbor]:
					dist[neighbor] = dist[node] + weight
					prev[neighbor] = node
	#only necessary if G has any negative weights
	for node in range(n):
		for neighbor,weight in graph[node]:
			if dist[node] + weight < dist[neighbor]:
				return False #negative weight cycle detected!

#runtime: O(V*E)
#memory:  O(V)
