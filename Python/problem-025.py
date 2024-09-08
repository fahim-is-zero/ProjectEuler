# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibo(n):
    """returns n-th fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n -1):
        a, b = b, a + b
    return b

def fibo_digits_idx(digits):
    idx = 1
    while not len(str(fibo(idx))) == digits:  # checks the lenth of fibonacci num
        idx += 1
    return idx

print(fibo_digits_idx(1000))  # 4782
