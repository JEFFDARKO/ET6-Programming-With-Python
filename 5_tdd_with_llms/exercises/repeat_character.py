""" Repeat Character

Write a function that takes in a string, a single character, and a number. 
The function returns a string with each occurrence of the character repeated n times.

"""
def repeat_character(text, char_to_repeat, repetitions):
    """The function returns a string with each occurrence of the character repeated n times.

    Parameters:
        text (str): we will repeat the character in this string
        char_to_repeat (str): this is the character we want to repeat
        repetitions (int): how many times to repeat the character

    Returns:
        string: the string with a single character repeated

    Raises:
        AssertionError: if the first argument is not a string
        AssertionError: if the second argument is not a single character
        AssertionError: if the third argument is not an integer  

    >>> repeat_character('omnia', 'm', 7)
    'ommmmmmmnia'

    >>> repeat_character('Jola-Moses', 's', 2)
    'Jola-Mossess'

    >>> repeat_character('Hasa', 'e', 99999999)
    'Hasan'

    >>> repeat_character('Rafaa', 'a', 3)
    'Raaafaaaaa'
    """
    
    
    assert repetitions >= 0, 'repetitions cannot be less than 0'
    
    repeated_text = ""

    for char in text:
        if char != char_to_repeat:
            repeated_text += char
        else:
            repeated_text += char_to_repeat * repetitions

    return repeated_text
