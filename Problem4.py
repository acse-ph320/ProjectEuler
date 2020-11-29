"""
Project Euler Problem 4
Largest palindrome product:
A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
https://projecteuler.net/problem=4

"""

def check_palindrome(number):
    """
    checks if a number is a palindrome
    """
    digits = [int(i) for i in str(number)]
    for i in range(len(digits)):
        if digits[i] != digits[-i-1]:
            return False
    else:
        return True


def largest_palindrome_multiple():
    largest_multiple = 999*999
    palindromes = []
    for i in range(largest_multiple, 99, -1):
        for j in range(largest_multiple, 99, -1):
            number = i*j
            if check_palindrome(number):
                palindromes.append(i*j)
        
    return(max(palindromes))

print(largest_palindrome_multiple())