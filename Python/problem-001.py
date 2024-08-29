#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multi(num):
	numbers = [ ]
	
	for i in range(1, num):
		if (i % 3 == 0) or (i % 5 == 0):
			numbers.append(i)
		else:
			pass
	print(sum(numbers))

	
sum_multi(1000) # 2331168