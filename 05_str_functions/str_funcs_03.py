# string exercises with decisions

def checkends(s):
    """
    This function takes in a string s and returns 
    True if the first character in s is the same 
    as the last character in s. 
    It returns False otherwise

    Args:
        s (str): a string to be checked

    Returns:
        bool: True is first char ==  last char
    """
    return s[0] == s[-1]


def catdog(s):
    """
    Return True if the string "cat" and "dog" 
    appear the same number of times in the given string.
    
    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True

    Args:
        s (str): str for processing

    Returns:
        bool: True if 'cat' and 'dog' appear the same
              number of times as substrings in the string  
    """
    cat_count = 0
    dog_count = 0
    return cat_count == dog_count







