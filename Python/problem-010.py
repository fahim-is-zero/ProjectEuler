# Find the sum of all the primes below two million.


from math import floor, sqrt


def is_prime(n):  # explaination is on project euler website
    if n == 1:
        return False
    elif n < 4:  # 2 and 3
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:  # already excluded 4,6,8
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True

def sum_prime(limit):  # explaination is on project euler website
    sum = 5  # as 2 and 3 are prime
    num = 5 
    while num <= limit:
        if is_prime(num):
            sum += num
        num += 2
        if num <= limit and is_prime(num):
            sum += num
        num += 4
    return sum  


print(sum_prime(2000000)) # 142913828922
