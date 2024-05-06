#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given integer.

    Parameters:
    - n (int): The integer for which factorial is to be calculated.

    Returns:
    - int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate factorial of the integer passed as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)
