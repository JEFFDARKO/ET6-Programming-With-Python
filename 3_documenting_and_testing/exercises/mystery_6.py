def mystery_6(a, b):
    """Generates a list of `a` consecutive integers starting from `b`.

    Args:
        a (int): The number of integers to include in the list. 
        b (int): The starting integer for the sequence.

    Returns:
        list: A list of `a` consecutive integers, starting from `b`.

    Raises:
        ValueError: If `a` is negative.

    Examples:
        >>> mystery_6(5, 10)
        [10, 11, 12, 13, 14]
        >>> mystery_6(0, 7)
        []
        >>> mystery_6(3, -2)
        [-2, -1, 0]
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
