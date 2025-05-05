#!/usr/bin/python3
import sys  # Used to retrieve command-line arguments

# Function: factorial
# -------------------
# Description:
#   Computes the factorial of a non-negative integer using recursion.
#   The factorial of a number n (written as n!) is the product of all
#   positive integers from 1 to n. By definition, 0! = 1.
#
# Parameters:
#   n (int): A non-negative integer whose factorial is to be calculated.
#
# Returns:
#   int: The factorial of the input number n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve the input number from the command line, compute its factorial,
# and print the result
f = factorial(int(sys.argv[1]))
print(f)