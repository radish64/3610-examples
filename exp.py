#brute force algorithm
def exp(x,n):
	ret = x
	for i in range (1,n):
		ret = ret * x
	return ret

#divide and conquer algorithm
#recursive implementation
def expd(x,n):
	if n == 1:
		return x
	y = expdr(x,n//2)
	if n % 2 == 1:
		return y * y * x
	else:
		return y * y

#modular exponentiation
#loop implementation
def modpow(x,n,m):
	ret = 1
	x = x%m
	while(n > 0):
		if n % 2 == 1:
			ret = (ret * x) % m
		n = n//2
		x = (x-x)%m
return ret

#^ sometimes called binary exponentiation
#  because it is reading the binary expansion of n
