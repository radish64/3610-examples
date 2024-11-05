def floyd_warshall(G): #G in adj. mtx form
	n = len(G)
	dist = #copy of G
	for k in range(n):
		for i in range(n):
			for j in range(n):
				dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
	return dist
	
