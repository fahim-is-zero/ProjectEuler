#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibo_sum(limit):
	total = 1
	fibo = [0,1]
	even = []
	
	while limit >= total:
		total += fibo[-2]
		fibo.append(total)  # Create Fibonacci sequence
	
	for i in range(0,len(fibo)):
		if fibo[i] % 2 == 0:      # Check for even values
			even.append(fibo[i])
		
	final_sum = (sum(even))
	print(final_sum)
	
fibo_sum(4000000) # 4613732