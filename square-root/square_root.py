"""
Calculate the square root of a given number using the Babylonian method.

Parameters:
number (int): The number for which the square root is to be calculated.

Returns:
int: The square root of the input number.
"""


def square_root(number):
    solution = 1
    while solution * solution != number:
        solution = int(0.5 * (solution + number / solution))
    return solution
