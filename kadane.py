def max_subarray(A):
	max_local, max_global = A[0], A[0]
	for i in range(1, len(A)):
		#at each step, we can either:
		#add A[i] to best local solution involving A[i-1] from A[:i]
		#or start a new local solution at A[i]
		max_local = max(max_local + A[i], A[i])
		max_global = max(max_global, max_local)
	return max_global

B = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(B))

