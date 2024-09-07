# Which starting number, under one million, produces the longest chain? (Longest Collatz Sequence)

# issue : slow, takes 10+ sec


def collatz_chain_count(num):
	n = num
	counter = 1
	while n > 1:
		if n % 2 == 0:
			n //= 2   # same as n /= 2 but since n is odd, so n //= 2 is same as n /= 2 (n//=2 is faster)
			counter += 1
		else:
			n = 3 * n + 1
			counter += 1
	return counter
	

def longest_collatz(limit):
	longest_chain = 0
	num = 0
	for i in range(1, limit + 1):
		temp_terms = collatz_chain_count(i)
		if temp_terms > longest_chain:
			longest_chain = temp_terms
			num = i
	return f"{num} has the longest chain and it's {longest_chain} terms"

print(longest_collatz(1000000))  # 837799
