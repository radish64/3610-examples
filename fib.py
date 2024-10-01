def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1) + fib(n-2)

def fibm(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n in memo.keys():
		return memo[n]
	ret = fibm(n-1) + fibm(n-2)
	memo[n] = ret
	return ret

def fibt(n):
	dp = [0] * (n+1)
	dp[1] = 1
	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]
