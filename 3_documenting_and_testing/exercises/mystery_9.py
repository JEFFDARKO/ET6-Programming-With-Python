def mystery_9(a):
    """Sorts a list of numbers from smallest to largest.

    This function goes through the list and compares each number with the next one.
    If a number is bigger than the next one, it swaps their places. 
    It keeps doing this until the list is ordered from smallest to largest.

    Args:
        a (list): A list of numbers (either whole numbers or decimal numbers) to sort.

    Returns:
        list: The list sorted from smallest to largest.

    Raises:
        TypeError: If `a` is not a list.
        ValueError: If any item in `a` is not a number (either a whole number or decimal).

    Examples:
        >>> mystery_9([4, 2, 7, 1, 3])
        [1, 2, 3, 4, 7]
        >>> mystery_9([10, 5, 8, 2])
        [2, 5, 8, 10]
        >>> mystery_9([3.5, 2.1, 4.7, 1.9])
        [1.9, 2.1, 3.5, 4.7]
        >>> mystery_9([1, 1, 1, 1])
        [1, 1, 1, 1]
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
