# What is the 1001st prime number?


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

def n_prime(n_th):  # explaination is on project euler website
    count = 1  # we know that 2 is prime
    num = 1
    while count != n_th:
        num += 2
        if is_prime(num):
            count += 1
    return num



print(n_prime(10001))  # 104743
