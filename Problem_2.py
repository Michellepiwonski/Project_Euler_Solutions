#Problem 2
#Even Fibonacci numbers
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Find Fibonacci sequence <= 4,000,000

def FibSeq():
    FibNums = [1, 2]
    n = 1
    while (FibNums[n-1] + FibNums[n]) <= 4000000:
        FibNums.append(FibNums[n-1] + FibNums[n])
        n += 1
       
    return FibNums
    
#Find the sum of even Fibbonacci numbers <= 4,000,000
def EvenFibSeq():
    sum_of_even_fibs = 0
    for num in FibSeq():
    	if num % 2 == 0:
        	sum_of_even_fibs += num
    return sum_of_even_fibs

print('The answer to problem 2 is ' + str(EvenFibSeq()) + '.')