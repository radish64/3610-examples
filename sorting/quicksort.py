def partition(A, low, high):
	pivot = A[high-1] #pivot is last value
	i = low
	for j in range(low, high-1):
		#consider a[j], if smaller than pivot, swap with A[i], increment i
		if A[j] <= pivot:
			A[i],A[j] = A[j],A[i]
			i = i + 1
	#end of loop, swap pivot with A[i]
	A[high-1],A[i] = A[i],A[high-1]
	return i

def quicksort(A,low,high):
	if high-low <= 1:
		return
	mid = partition(A,low,high)
	#A[mid] is in its correct location in sorted array
	#sort left and right
	quicksort(A, low, mid - 1)
	quicksort(A, mid + 1, high)


B = [3,4,5,1,2]
quicksort(B,0,len(B))

for x in B:
	print(x)
