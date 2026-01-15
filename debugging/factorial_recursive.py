#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function Description:
        This function computes the factorial of the given integer n recursively.
        The factorial of 0 is defined as 1. For n > 0, it multiplies n by factorial(n-1).

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command line argument, calculate factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)

