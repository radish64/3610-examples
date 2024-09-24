def partition(A, low, high): #same code from quicksort.py
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
	
def quickselect(A,k): #kth entry is in A[low:high]
	low,high = 0, len(A)
	while True:
		mid = partition(A, low, high)
		if mid == k:
			return A[k]
		elif mid > k:
			high = mid
		else: #mid < k
			low = mid+1

B = {7,5,4,3,2,1}
x = quickselect(B,4)
print(x)
