""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""
def sum_evens_and_odds(numbers):
    """This function takes a list of numbers and returns a dictionary with sums of the even and odd numbers in the list
    
    Parameters:
    numbers(list): list of numbers
    
    Returns:
    dict: a dictionary with the sum of the even and odd numbers
    
    Raises:
    AssertionError: if the argument is not a list
    
    Examples:
    >>> sum_evens_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9])
    {'evens': 20, 'odds': 25}
    
    >>> sum_evens_and_odds([10, 20, 30, 40, 50, 60, 70, 80, 90])
    {'evens': 450, 'odds': 0}
    
    >>> sum_evens_and_odds([1, 3, 5, 7, 9])
    {'evens': 0, 'odds': 25}
    
    """
    assert isinstance(numbers, list), 'argument for numbers must be a list'
    
    even_sum = 0
    odd_sum = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
            
    return {'evens': even_sum, 'odds': odd_sum}
