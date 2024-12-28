""" Is in one

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _only one_ of the lists.

"""

def is_in_one(string, list1, list2):
    """ A function that takes in a string and two lists of strings 
    
    Parameters:
    string(str): first argument of the function
    list1(list of str): second argument of the function
    list2(list of str): third argument of the function
    
    Returns:
    Returns True if the string is present in only one of the strings
    
    Raises:
    AssertionError: if the first argument is not a string 
    AssertionError: if the second argument is not a list 
    AssertionError: if the third argument is not a list 
    AssertionError: if the elements in the second argument is not a string 
    AssertionError: if the elements in the third argument is not a string 
    
    Examples:
    >>> is_in_one('welcome', ['add', 'welcome', 'group 7'], ['run', 'hello', 'group'])
    True
    
    >>> is_in_one('rina', ['Curina', 'Terry', 'Mahdia'], ['Martha', 'Cathrina', 'desk'])
    True
    
    """
    assert isinstance(string, str), "First argument must be a string."
    assert isinstance(list1, list), "Second argument must be a list."
    assert isinstance(list2, list), "Third argument must be a list."
    assert all(isinstance(item, str) for item in list1), "All elements in the first list must be strings."
    assert all(isinstance(item, str) for item in list2), "All elements in the second list must be strings."
    
    in_list1 = string in list1
    in_list2 = string in list2

    return (in_list1 or in_list2) and not (in_list1 and in_list2)


print( is_in_one('welcome', ['add', 'welcome', 'group 7'], ['run', 'hello', 'group']))
