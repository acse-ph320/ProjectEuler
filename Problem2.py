"""
Problem 2
Even Fibonacci numbers
https://projecteuler.net/problem=2
"""

a = 1
b = 2
c = 0
even_fib_sum = 0

while c < 4e6:
    if c % 2 == 0:
        even_fib_sum += c
    c = a + b
    a = b
    b = c

print(even_fib_sum)