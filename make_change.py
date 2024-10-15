def make_change(amount, coins): #assume 1 is in coins
	coins.sort(reverse = True)
	change = []
	for coin in coins:
		while amount >= coin:
			change.append(coin)
			amount -= coin
	return change

A = [1,5,10,25]

print(make_change(37, A))
