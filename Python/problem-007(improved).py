rom math import floor, sqrt


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
        r = floor(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True

def n_prime(n_th):
    count = 1 
    num = 1
    while count != n_th:
        num += 2
        if is_prime(num):
            count += 1
    return num



print(n_prime(10001))
