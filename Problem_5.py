# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
    for n in range(2, 1000000000):
        if n % 11 == 0:
            if n % 12 == 0:
                if n % 13 == 0:
                    if n % 14 == 0:
                        if n % 15 == 0:
                            if n % 16 == 0:
                                if n % 17 == 0:
                                    if n % 18 == 0:
                                        if n % 19 == 0:
                                            if n % 20 == 0:
                                                return n
print('The solution to problem 5 is ' + str(smallest_multiple()) + '.')