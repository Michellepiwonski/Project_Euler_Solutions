# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 
# What is the 10,001st prime number?

def prime_gen():
    list_of_primes = []
    while len(list_of_primes) != 10001:
        i = 2
        x = 1
        while x <= i:
            factor_holder = []
            if i % x == 0:
                factor_holder.append(x)
            if factor_holder == [1, x]:
                list_of_primes.append(i)
            x += 1
        i += 1
    return list_of_primes[-1]

print(prime_gen())