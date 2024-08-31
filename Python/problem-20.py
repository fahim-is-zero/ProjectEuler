# Find the sum of the digits in the number 100!

import math

def fac_digit_sum(num):
    digit = []
    fact = math.factorial(num)

    for i in str(fact):
        digit.append(int(i))

    return sum(digit)

print(fac_digit_sum(100)) # 648
