
def fibo(n):
    a, b = 0, 1
    for _ in range(n -1):
        a, b = b, a + b
    return b

def fibo_digits_idx(digits):
    idx = 1
    while not len(str(fibo(idx))) == digits:
        idx += 1
    return idx

print(fibo_digits_idx(1000))
