def find_max(A):
	best = A[0]
	for i in range(1, len(A)):
		if A[i] > best:
			best = A[i]
	return best

A = [1, 2, 3, 4]

print(find_max(A))

