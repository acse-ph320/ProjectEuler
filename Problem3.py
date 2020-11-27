"""
Project Euler Problem 3
Largest Prime Factor: what is he largest prime factor of 600851475143
https://projecteuler.net/problem=3

"""


num = 10
prime_list = []


def is_it_prime(number):
    """
    function to check if a number is a prime number
    """
    counter = 2
    while counter <= round(number/2):
        if number % counter == 0:
            return(False)
        counter += 1
    else:
        return(True)


def highest_prime_factor(number):
    """
    Finds the highest prime factor of a number, if the number is prime this 
    function returns itself.
    """
    counter = 2
    while counter <= round(number/2):
        if number % counter == 0:
            factor = number/counter
            if is_it_prime(factor) == True:
                return(factor)
        counter += 1
    else:
        return(number)
