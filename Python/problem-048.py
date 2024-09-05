def self_power(limit):
    total = 0
    n = 1

    for i in range(limit):
        total += (n+i)**(n+i)  # series : [n^n + (n+1)^(n+1) + (n+2)^(n+2) + .... (n+i)^(n+i)]

        str_total =str(total)
        last_ten_digits = str_total[-10:] 
    print(last_ten_digits)

print(self_power(1000)) 
