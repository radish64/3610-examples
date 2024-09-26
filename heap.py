#this entire file is lowkey psuedocode
#we didn't write the left(), right(), or parent() functions


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

def heapify_up(A, i): #don't need size
	if i == 0:
		return
	p = parent(i)
	if A[i] > A[p]:
		A[i],A[p] = A[p],A[i]
		heapify-up(A,p)

def insert(A, size, val): #runtime is O(lgn)
	A[size] = val
	heapify-up(A,size)

def make_heap(A): #turn the list A into a heap
	for i in range(1, len(A)):
		heapify-up(A,i)

#"smart" selection sort where finding max takes O(lgn) time instead of O(n) time
def heapsort(A):
	make_heap(A)
	for size in range(len(A), 0, -1): #n iterations; lgn + lgn(n-1) + lgn(n-2) + ... + lg(1) = O(nlgn)
		A[size-1] = remove_max(A,size)

def make_heap_fast(A): #last internal node
	for i in range(parent(len(A)-1), -1, -1):
		heapify(A,i,len(A))
	
