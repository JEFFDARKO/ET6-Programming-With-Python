def mystery_2(a):
    """ 
    Returns the length of the input object, or None if it is empty.

    Arguments:
        a can be int or an iterable doc type: The input object whose length is to be determined. 
        It can be a string, list, tuple, or other iterable object.

    Returns:
        int or None: 
            - The length of the input object if it is non-empty.
            - None if the input object is empty.

    Example:
        >>> mystery_2([1, 2, 3])
        3
        >>> mystery_2("Jeffery")
        7
        >>> mystery_2([1, 2])
        2
    """
    if len(a) == 0:
        return None

    return len(a)
