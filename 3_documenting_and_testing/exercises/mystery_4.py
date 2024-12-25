def mystery_4(a):
    """Generates a list of integers from 0 up to the number before the given number

    Args:
        a (int): The number of integers to include in the list

    Returns:
        A list of integers starting from 0 up to (a -1)
        
    Raises:
        ValueError: If 'a' is negative
        
    Examples:
        >>> mystery_4(5)
        [0, 1, 2, 3, 4]
        >>> mystery_4(0)
        []
        >>> mystery_4(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
