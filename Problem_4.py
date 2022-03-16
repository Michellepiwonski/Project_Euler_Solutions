# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverser(n):
    return n [::-1]

def palindrome():
    palindrome_list=[]
    a = 999
    while a >= 1:
        b = 999
        while b >= 1:
            if str(a * b) == reverser(str(a * b)):
                palindrome_list.append(a * b)
            b -= 1
        a -= 1
    return max(palindrome_list)

print(palindrome())