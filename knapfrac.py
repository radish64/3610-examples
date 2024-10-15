def knapsack_fractional(items, W):
	#sort by value/weight descending
	items.sort(
		key = lambda x: x[1]/x[0],
		reverse = True)
	total = 0
	for weight, value in items:
		if weight <= W:
			total += value
			W -= weight
		else:
			total += value * (W/weight)
			W = 0
			break
	return total

A = [(7, 42), (3,12), (4,40), (5,25)]

print(knapsack_fractional(A, 10))
