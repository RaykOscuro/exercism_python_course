def square_of_sum(number):
    """
    Calculate the square of the sum of numbers up to a given number.

    Parameters:
    number (int): The input number up to which the sum is calculated.

    Returns:
    int: The square of the sum of numbers up to the input number.
    """
    sum = 0
    for x in range(number):
        sum += (x+1)
    return sum**2


def sum_of_squares(number):
    """
    Calculate the sum of squares up to a given number.

    Parameters:
    number (int): The number up to which the sum of squares will be calculated.

    Returns:
    int: The sum of the squares up to the given number.
    """
    sum = 0
    for x in range(number):
        sum += (x+1)**2
    return sum


def difference_of_squares(number):
    """
    Calculate the difference between the square of the sum and the sum of the squares for a given number.
    
    Parameters:
    number (int): The input number for which the calculation is performed.
    
    Returns:
    int: The difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
