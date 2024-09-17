def binary_search(A, target):
	low, high = 0, len(A) # searching A[low:high]
	while low < high:
		mid = low + (high - low) // 2 #int division
		if A[mid] == target:
			return True
		elif A[mid] < target:
			low = mid + 1
		else:
			high = mid 
	return False


A = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(A, 3))
