def gcd(a,b):
	x,y = abs(a), abs(b)
	if y > x:
		x,y = y,x #swap
	while y > 0:
		r = x % y
		x,y = y,r
	return x #gcd(a,0) = a

print(gcd(12,64))
