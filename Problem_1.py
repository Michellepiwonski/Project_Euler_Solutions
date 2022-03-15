#Problem 1
#Multiples of 3 or 5
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_or_5():
    sum_of_multiples = 0
    for num in range(1, 1000):
            if num % 3 == 0 or num % 5 == 0:
                sum_of_multiples += num
    
    return sum_of_multiples 

print('The answer to problem 1 is ' + str(multiples_of_3_or_5()) + '.')