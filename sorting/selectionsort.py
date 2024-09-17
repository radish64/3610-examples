def selection_sort(A):
	for i in range(len(A), 0, -1): #count down to 0
		best = 0
		for j in range(1, i):
			if A[j] > A[best]:
				best = j
		A[best], A[i-1] = A[i-1], A[best]

A = [4, 3, 2, 1]

selection_sort(A)

for x in A:
	print(x)
