
def check_if_in(word: str, char: str):
    """Checks to see if a char appears in a word

    Args:
        word (str): a word
        char (str): a single character

    Returns:
        bool: True if the char is found, False otherwise
    """
    return char in word


print(check_if_in("Banana", "a"))  # True
print(check_if_in("Banana", "x"))  # False
