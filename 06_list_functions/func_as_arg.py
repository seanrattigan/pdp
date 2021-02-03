# @Author:srattigan
# @Date:2021-02-03 11:48:27
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-03 11:48:27


def shout(txt):
    """changes the arg to all uppercase and returns

    Args:
        txt (str): any string

    Returns:
        [str]: a uppercased str
    """
    return

def whisper(txt):
    """changes the arg to all lowercase and returns

    Args:
        txt (str): any string

    Returns:
        [str]: a lowercased str
    """
    return

def reverse_it(txt):
    """Takes a str and reverses it char by char (using a list)

    Args:
        txt (str): any str
    Returns:
        [str]: a reversed str
    """
    pass
    

def process_text(txt, func):
    """Takes a str and processes it with the func supplied

    Args:
        txt (str): any str
        func (function): a text processor
    """
    new_text = func(txt)
    print(new_text)


def print_info(f):
    print(f.__name__)
    print(f.__doc__)


if __name__ == "__main__":
    process_text("Hello", shout)
    print_info(shout)
    print_info(reverse_it)
