# Author: Makaliah Dickinson
# Date: 7/5/2020
# Description: The first and second numbers in the Fibonacci sequence are both 1. After that, each subsequent number is
#              the sum of the two preceding numbers. The first several numbers in the sequence are: 1, 1, 2, 3, 5, 8,
#              13, 21, 34, 55, 89, etc. Write a function named fib that takes a positive integer parameter and returns
#              the number at that position of the Fibonacci sequence. For example fib(1) = 1, fib(3) = 2, fib(10) = 55,
#              etc. Your function does not need to print anything out - just return a value.
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#Testing the function here. ignore/remove the code below if not required.
print(fib(1))
print(fib(3))
print(fib(10))
