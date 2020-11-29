"""
Project Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5

"""

counter = 20


def is_divisible_by_all(number):
    for i in range(20, 0, -1):
        if number % i != 0:
            return(False)
    else:
        return(True)


def find_lowest():
    counter = 20
    while is_divisible_by_all(counter) == False:
        counter += 20
    return(counter)


print(find_lowest())