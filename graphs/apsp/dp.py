def apsp(G): #O(V^4)
	n = len(G)
	L = #copy of G
	for i in range(n-1):
		L = extend_paths(L,G)
	return L


def apsp_faster(G): #O(V^3lgV)
	n = len(G)
	L = #copy of G
	i = i
	while i < n:
		L = extend_paths(L,L)
		i = 2*i
	return L

def extend_paths(A,B): #O(n^3)
	#return the matrix product AB
	#w/ min/sum instead of sum/product
	n = len(A)
	C = empty_graph(n)
	for i in range(n): #i-th row of A
		for j in range (n): #j-th col of B
			for k in range (n) #a_ik, b_kj
				C[i][j] = min(C([i][j], A[i][k] + B[k][j]))
	return C
