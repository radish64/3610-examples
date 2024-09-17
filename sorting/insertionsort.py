def insertion_sort(A):
	for i in range (1, len(A)):
		j = i
		val = A[j] # value to be inserted
		while j > 0 and A[j-1] > val: #shift all elements of A[:i]
			A[j] = A[j-1]	#right by 1 until val >= A[j-1]
			j = j - 1		
		A[j] = val			#then set A[j] = val
		
A = [4,3,2,1]

insertion_sort(A)

for x in A:
	print(x)
