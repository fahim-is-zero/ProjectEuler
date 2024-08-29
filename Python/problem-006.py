# Difference between the sum of the squares of the first 100 natural numbers and the square of the sum.

def sum_square(limit):
    num = list(range(1, limit + 1))  # same as ( n(n+1)/2 )^2
    return (sum(num))**2

def square_sum(limit):
    return ( (limit*(limit + 1)*(2 * limit + 1)) / 6 )  # Formula : n(n+1)(2n+1)/6

def diff_series(limit):
    result = sum_square(limit) - square_sum(limit)
    return result

print(diff_series(100)) # 25164150 
