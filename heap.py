#heapifying "down" from index i
def heapify(A, i, size):
	l = left(i)
	r = right(i)
	largest = i
	#short circuiting and - if l >= size, second condition isn't checked
	#this prevents an out of bounds error
	if l < size and A[l] > A[largest]:
		largest = l
	if r < size and A[r] > A[largest]:
		largest = r
	if i != largest
	A[i],A[largest] = A[largest],A[i]
	heapify(A, largest, size)
	#we coulda done this with a while loop to cut down on overhead

def remove_max(A,size):
	ret = A[0]
	A[0] = A[size-1]
	size = size-1
	heapify(A, 0, size)
	return ret
