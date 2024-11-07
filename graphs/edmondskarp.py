from collections import deque

def edmonds_karp(graph, source, sink):
	n = len(graph)
	prev = [-1] * n
	total_flow = 0
	rcap = {i:{} for i in range(n)} #residual capacities
	for u in range(n):
		for v,weight in graph[u]:
			rcap[u][v] = weight
			rcap[v][u] = 0
	while bfs(graph, source, sink, rcap, prev): #O(V^2)
		path_flow = float('inf') #min rcap along shortest path
		v = sink
		while v != source:
			#work backwards along a flow-augmenting path
			path_flow = min(path_flow, rcap[prev[v]][v])
			v = prev[v]
		total_flow += path_flow
		v = sink
		while v != source:
			#augment along the path
			u = prev[v]
			rcap[u][v] -= path_flow
			rcap[v][u] -= path_flow
			v = u
	return total_flow

def bfs(graph, source, sink, rcap, prev): #O(V+E) = O(E)
	n = len(graph)
	visited = [False] * n
	queue = deque()
	queue.append(source)
	visited[source] = True
	while len(queue) > 0 and not visited[sink]:
		current = deque.popleft()
		for i in range (n):
			#assume this is implemented more efficiently
			if i in rcap[current]:
				if rcap[current][i] > 0 and not visited[i]:
					visited[i] = True;
					queue.append(i)
					prev[i] = current
	return visited[sink]

