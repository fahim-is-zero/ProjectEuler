# What is the sum of the digits of the number 2^1000

def power_digit_sum(power):
    result = (2 ** power)
    sum = 0
    for i in str(result):
        sum += int(i)     # add digits
    print(sum)

power_digit_sum(1000) # 1366
