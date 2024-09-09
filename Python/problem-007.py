# What is the 1001st prime number?

def n_prime(n):
    prime = [2]
    x = 3
    while len(prime) <= n - 1:
        for i in prime:
            if x % i == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    return prime[-1]

print(n_prime(10001)) # 104743
