#can be done with a stack, we will do it recursively

def dfs(graph, start):
	time = 0
	prev - [-1] * len(graph)
	start_time = [-1] * len(graph)
	finish_time = [-1] * len(graph)
	def visit(vertex):
		start_time[vertex] = time
		time += 1
		#each edge considered once from each direction
		for neighbor in graph[vertex]:
			if prev[neighbor] == -1:
				prev[neighbor] = vertex
				visit(neighbor) #recursion
		finish_time[vertex] = time
		time += 1
	prev[start] = start
	visit(start)

#memory: O(V) (including recursion)
#runtime O(V+E) assuming connected
