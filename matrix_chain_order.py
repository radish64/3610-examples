def matrix_chain_order(p): #p is a list of matrix dimensions p_0, p_1, ... p_n
	n = len(p) - 1
	m = [[0]*n for i in range(n)] #nxn array
	for size in range(2, n+1):
		for i in range(0, n+1-size):
			j = i + (size - 1) #ending point A_i A_i+1 ... A_j } size # of matrices
			m[i][j] = float('inf')
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
				if q < m[i][j]:
					m[i][j] = q

	return m[0][n-1]


p = [5,5,2,5]
print(matrix_chain_order(p))

