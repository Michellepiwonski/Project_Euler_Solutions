# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 
# What is the 10,001st prime number?

def prime_gen():
    list_of_primes = []
    while len(list_of_primes) < 10001:
        p = 2
        for i in range(1, p+1):
            hold = []
            if p % i == 0:
                hold.append(i)
        if hold == [1, p]:
            list_of_primes.append(p)
        p += 1
    return list_of_primes[-1]

print(prime_gen())