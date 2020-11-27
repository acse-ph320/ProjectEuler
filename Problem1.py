"""
Project Euler Problem 1
Multiples of 3 & 5 less than 100
https://projecteuler.net/problem=1
"""

multiples = []

for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

print(multiples)