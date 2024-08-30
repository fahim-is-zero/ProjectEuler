# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome(limit):
    largest_found = 0                               # Stores largest found palindrome from all combination
    for i in range(limit, 0, -1):
        for j in range(i, 0, -1):
            product = i * j
            if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
                    if product > largest_found:
                        largest_found = product
    return largest_found

print(largest_palindrome(999))  # 906609
