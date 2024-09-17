def merge(L,R): #L,R are sorted lists
	A = []
	i, j = 0, 0
	while i < len(L) and j < len(R):
		if L[i] <= R[j]:
			A.append(L[i])
			i = i + 1
		else:
			A.append(R[i])
			j = j + 1
	while i < len(L):
		A.append(L[i])
		i = i + 1
	while j < len(R):
		A.append(R[j])
		j = j + 1
	return A

def merge_sort(A):
	if len(A) <= 1:
		return A
	mid = len(A) // 2
	#in python these make copies of list, but we don't need copies since nothing is overwritten
	L = merge_sort(A[:mid])
	R = merge_sort(A[mid:])
	return merge(L,R)

#test code
B = [7,2,3,8,4,5,1,6]
B = merge_sort(B)

for x in B:
	print(x)
