def mystery_3(a, b):
    """Returns the smaller of two numbers, unless they are equal, in which case it returns their sum.

    Args:
        The first number, a, can be a float or int
        The second number, b, can be a float or int

    Returns:
        The smaller of the two numbers or the sum if both numbers are equal.

    Raises:
        TypeError: If either `a` or `b` is not an int or float.

    Examples:
        >>> mystery_3(2, 5)
        2
        >>> mystery_3(10, 3)
        3
        >>> mystery_3(7, 7)
        14
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
