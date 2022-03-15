# Sum square difference 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_the_squares():
    squ_nums = []
    for n in range(1, 101):
        squ_nums.append(n ** 2)
    return sum(squ_nums)

def square_of_the_sum():
    sum_num = []
    for n in range(1, 101):
        sum_num.append(n)
    return (sum(sum_num)) ** 2

print('The answer to problem 6 is ' + str(square_of_the_sum() - sum_of_the_squares()) + '.')