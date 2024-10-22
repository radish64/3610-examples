from collections import deque

def bfs(graph, start): #graph is a list of lists of edges, vertices are 0,1,...,n-1
	queue = deque([start])
	prev = [-1] * len(graph)
	prev[start] = start
	#enter this loop V times
	while len(queue) > 0:
		current = queue.popleft()
		#E (# of edges)
		for neighbor in graph[current]:
			if prev[neighbor] == -1:
				queue.append(neighbor)
				prev[neighbor] = current

#prev gives the "back edge" from each vertec to it parent in the BFS tree, -1 if it's not reachable
#memory = O(V)
#runtime = O(V+E)
