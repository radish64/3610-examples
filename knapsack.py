def knapsack(items, W): #items = (weight, value) pairs, w = capacity
	n = len(items)
	dp = [[0] * (W+1) for _ in range (n+1)] #n+1 * W array, init to 0
	for i in range(1, n+1):
		weight = items[i-1][0]
		value = items[i-1][1]
		for w in range (W+1):
			if weight > w: #can't include!
				dp[i][w] = dp[i-1][w]

			else:
				dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
	return dp[n][W]

A = [(1,5),(10,10)]

print(knapsack(A, 10))
