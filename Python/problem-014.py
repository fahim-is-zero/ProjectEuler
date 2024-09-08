# Which starting number, under one million, produces the longest chain? (Longest Collatz Sequence)


cache_values = {1 : 1}  # num : chain (stores result) 

def collatz_chain_count(n):
	if n > 0:
		if n in cache_values.keys():
			return cache_values[n]

		if n % 2 == 0:
			cache_values[n] = collatz_chain_count(n/2) + 1  # collatz(n) = collatz(n/2) + 1 if n is even. More explaination on project euler website
		else:
			cache_values[n] = collatz_chain_count((3*n+1)/2) + 2  # collatz(n) = collatz((3n+1)/2) + 2 if n is odd. More explaination on project euler website
		return cache_values[n]
	else:
		return "invalid number"
	

def longest_collatz(limit):
	longest_chain = 0
	num = 0
	for i in range(int(limit / 2), limit):
		temp_terms = collatz_chain_count(i)
		if temp_terms > longest_chain:
			longest_chain = temp_terms
			num = i
	return f"{num} has the longest chain and it's {longest_chain} terms"

print(longest_collatz(1000000))  # 837799
