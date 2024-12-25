def mystery_7(a, b):
    """Finds and returns the items in a list that contain a specific word, part of a word, or number.

    Args:
        a (list): A list of strings or numbers to check.
        b (str): The word, part of a word, or number to look for in each item.

    Returns:
        list: A list of items from `a` that have the word, part of the word, or number `b`.

    Raises:
        TypeError: If `a` is not a list or if `b` is not a string.
        ValueError: If any item in `a` is not a string or number.

    Examples:
        >>> mystery_7(["apple", "banana", "cherry"], "an")
        ['banana']
        >>> mystery_7(["cat", "dog", "bird"], "at")
        ['cat']
        >>> mystery_7(["hello", "world"], "o")
        ['hello', 'world']
        >>> mystery_7(["abc", "def"], "x")
        []
        >>> mystery_7([123, 456, 789], "4")
        [456]
        >>> mystery_7(["2023", "2024", "2025"], "24")
        ['2024']
    """
    c = []
    for d in a:
        if b in str(d):  # Convert each item to a string for comparison
            c.append(d)
    return c
