def rodcut(n, pieces):
	#pieces is a list [(l_1,p_1), ...,] of length k
	dp = [0] * (n+1)
	for i in range (1, n+1):
		for l,p in prices:
			if i >= l:
				dp[i] = max(dp[i],dp[i-l]+p)
	return dp[n]
