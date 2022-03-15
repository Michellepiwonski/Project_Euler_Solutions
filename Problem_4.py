# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverser(n):
    return n [::-1]

def palindrome():
    a = 999
    b = 999
    while b >= 1:
        while a >= 1:
            if str(a * b) == reverser(str(a * b)):
                return str(a * b)
            a -= 1
        b -= 1

print(palindrome())