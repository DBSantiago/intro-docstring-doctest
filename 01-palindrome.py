
def palindrome(sentence: str) -> bool:
    """
    Checks if a string is a palindrome or not.

    Args:
        sentence (string): String to evaluate.

    Returns:
        bool: True or False

    Examples:
        >>> palindrome('Anita lava la tina')
        True
        >>> palindrome('Codigo Facilito')
        False
        >>> palindrome('UwU')
        True
    """
    sentence = sentence.lower().replace(" ", "")
    return sentence == sentence[::-1]


# print(palindrome.__doc__)
# print(palindrome("Anita lava la tina"))
# print(palindrome("Codigo Facilito"))
# print(palindrome("UwU"))
