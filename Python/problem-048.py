# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + .... + 1000^1000  (n^n + ...)

def self_power(limit):
    total = 0
    n = 1

    for i in range(limit):
        total += (n+i)**(n+i)  # series : [n^n + (n+1)^(n+1) + (n+2)^(n+2) + .... (n+i)^(n+i)]

        str_total =str(total)
        last_ten_digits = str_total[-10:]  # Stores last ten digits

    print(last_ten_digits)

print(self_power(1000)) # 9110846700
