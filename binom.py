#slow algorithm that recalculates stuff
def binom(n,k):	#0 <= k <= n
	if k == 0 or k == n:
		return 1
	return binom(n-1,k-1)+binom(n-1,k)

#easier to write and prove correct
memo={}
def binom_memoized(n,k):
	if k == n or k == 0:
		return 1
 	#memo is a map object that stores key-value pairs, and keys() is its set of keys.
	#(n,k) is a tuple in Python, ordered pair
	if (n,k) in memo.keys():
		return memo[(n,k)]
	memo[(n,k)] = binom_memoized(n-1,k-1)+binom_memoized(n-1,k)

#less overhead because there's no map table
def binom_table(n,k):
	dp = [[0]*(k+1) for x in range (n+1)] #make an (n+1) * (k+1) list
	for i in range(n+1):
		dp[i][0] = 1
	for i in range(1,n+1):
		for j in range(1, max(i+1,k)):
			dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
	return dp[n][k]

def binom_table_incorrect(n,k):
	dp = ([0] * k+1)*n+1
	# L = [0,0,0,...,0] k+1 times
	# L * n+1 = [L,L,L,...,L] n+1 times
	#these Ls are all references to the same list object - modifying one modifies them all
