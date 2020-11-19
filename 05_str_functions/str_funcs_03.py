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



