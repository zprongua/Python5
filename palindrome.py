def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    newValue = value.replace(' ', '').lower()
    return newValue[::-1].__eq__(newValue)