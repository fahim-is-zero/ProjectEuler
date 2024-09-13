from math import floor


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(n**(0.5))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True

def sum_prime(limit): 
    sum = 5 
    num = 5 
    while num <= limit:
        if is_prime(num):
            sum += num
        num += 2
        if num <= limit and is_prime(num):
            sum += num
        num += 4
    return sum  


print(sum_prime(2000000))
