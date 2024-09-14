# Find the sum of all the primes below two million.

def sum_prime(lim):
    prime = [2]
    total = 2
    x = 3
    while x <= lim:
        for i in prime:
            if x % i == 0:
                x += 2
                break
        else:
            prime.append(x)
            total += x
            x += 2
    return total

print(sum_prime(10)) # takes time (360s) # 142913828922

