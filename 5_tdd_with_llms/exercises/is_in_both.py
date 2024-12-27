""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""

def is_in_both(string, list1, list2):  
  """This function that takes in a string and two lists of strings and returns true if the items is_in_both_of the lists
  
  Parameters:
    string(str): first argument of the function
    list1 (list of str): second argument of the function
    list2 (list of str): third list of string
    Returns:
    Boolean(True): if the str is present in first and second list, False if otherwise
    
    Raises:
    AssertionError: if the first argument is not a string 
    AssertionError: if the second argument is not a list 
    AssertionError: if the third argument is not a list 
    AssertionError: if the elements in the second argument is not a string 
    AssertionError: if the elements in the third argument is not a string 
    
    Examples:
    >>> is_in_both('welcome', ['add', 'welcome', 'group 7'], ['welcome', 'hello', 'group'])
    True
    
    >>> is_in_both('rina', ['Curina', 'Terry', 'Mahdia'], ['Martha', 'Cathrina', 'rina'])
    True
  """
  assert isinstance(string, str), 'First argument must be a string'
  assert isinstance(list1, list), 'Second argument must be a list of strings'
  assert isinstance(list2, list), 'Third argument must be a list of strings'
  assert all(isinstance(item, str) for item in list1), 'All elements in the second argument must be strings'
  assert all(isinstance(item, str) for item in list2), 'All elements in the third argument must be strings'
    
  return string in list1 and string in list2
