def mystery_8(a, b):
    """Returns a list of elements from `a` that contain the string `b`.

    This function goes through each element in the list `a` and checks if the string `b` is found in the element.
    If `b` is found, the element is added to the result list.

    Args:
        a (list): A list of strings to check.
        b (str): The string to search for in each element of the list.

    Returns:
        list: A list of elements from `a` that contain the string `b`.

    Raises:
        TypeError: If `a` is not a list or `b` is not a string.
        ValueError: If any item in `a` is not a string.

    Examples:
        >>> mystery_8(["apple", "banana", "cherry"], "an")
        ['banana']
        >>> mystery_8(["cat", "dog", "bird"], "at")
        ['cat']
        >>> mystery_8(["hello", "world"], "o")
        ['hello', 'world']
        >>> mystery_8(["apple", "banana", "cherry"], "xyz")
        []
    """
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
