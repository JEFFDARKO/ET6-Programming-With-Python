def mystery_1(a, b):
    """ 
    Takes two arguments and adds them together.

    Arguments:
        Both arguments, 'a' and 'b', can be float, int, or string.
        a = int, float, string
        b = int, float, string

    Returns:
        int, float, or str: The sum of `a` and `b`. If both are numbers, their sum is returned.
                            If both are strings, their concatenation is returned.

    Raises:
        TypeError: if 'a' and 'b' are of different data types.

    Example:
        >>> mystery_1(3, 5)
        8
        >>> mystery_1("Hello, ", "world!")
        'Hello, world!'
    """
    return a + b
