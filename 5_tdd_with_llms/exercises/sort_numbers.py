""" Sort Numbers

Write a function that takes in a list of numbers
It will return a new list with the same numbers from lowest to highest
-> this function does not have side effects

"""

def sort_numbers(list_of_numbers):
    """This function will return a new list with the same numbers from lowest to highest
    
    Parameters:
        list(int): the original list given by the user 
        new_list(int): new list with numbers from lowest to highest
        
    Returns:
        list(int): the list created from the original with numbers from lowest to highest
        
    Examples:
    >>> sort_numbers([1, 3, 4, 5, 5, 2])
    [1, 2, 3, 4, 5, 5]
    
    >>> sort_numbers([])
    []
    
    >>> sort_numbers([10, 5, 6, 7, -23])
    [-23, 5, 6, 7, 10]        
    
    """
    assert isinstance(list_of_numbers, list), 'argument for list_of_numbers must a list'
    
    return sorted(list_of_numbers)
  
  
print(sort_numbers([1, 4, 5, 10, -2]))
