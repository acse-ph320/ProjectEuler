"""
The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is, 3025 - 385 = 2640

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6

"""

squared_sum = 0
num_sum = 0

for i in range(101):
    squared_sum += i**2
    num_sum += i

ans = num_sum**2 - squared_sum
print(ans)
