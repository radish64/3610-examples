import heapq
class Node:
	def __init__(self, value, freq):
		self.value = value
		self.freq = freq
		self.left = None 
		self.right = None

	#less than - overrides "<" operator
	#called when "self < other" is executed
	#note: in Python, overriding "<" also implicitly defines ">"
	def __lt__(self, other): 
		return self.freq < other.freq

#total runtime is O(n) + O(n) + nO(lgn) = O(nlgn)
#memory is O(n) (to assign contents of tree)
def huffman(chars): #chars = val, freq pairs
	nodes = []

	for val, freq in chars:
		nodes.append(Node(val,freq))

	heapq.heapify(nodes) #min-heaps, O(n)

	while len(nodes) > 1: #loop executed n-1 times
		#nodes starts w/ length n, ends w/ length 1, each loop decrements by 1
		left = heapq.heappop(nodes)	#O(lgn)
		right = heapq.heappop(nodes) #O(lgn)
		merged = Node(None, left.freq + right.freq) #constant time
		merged.left, merged.right = left, right	#constant time
		heapq.heappush(nodes,merged) #O(lgn)

	return nodes[0]

A = [('a',45), ('b',13), ('c',12), ('d',16), ('e',9), ('f',5)]
print(huffman(A))
