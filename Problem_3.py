# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def factor_gen(n):
    i = 1
    list_of_factors = []
    while i <= n:
        if n % i == 0:
            list_of_factors.append(i)
        i += 1
    return list_of_factors

def is_prime(l):
    primes = []
    for x in l:
        factors_of_factors = []
        i = 1
        while i <= x:
            if x % i == 0:
                factors_of_factors.append(i)
            i += 1
        if factors_of_factors == [1, x]:
            primes.append(x)
    
    return primes

print(max(is_prime(factor_gen(___))))