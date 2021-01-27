import random

rand_list = ["Noob",
             True,
             2,
             3.1987,
             (1, 2),
             ['a', 'b']
             ]

def mod(a_list):
    """
    (list of obj)
    Prints out the index, value and type of
    each object in the list
    """
    a_list.pop()
    print("Done")


if __name__ == "__main__":
    print(f"List is {rand_list}")
    mod(rand_list)
    print(f"List is {rand_list}")
    mod(rand_list)
    print(f"List is {rand_list}")
    mod(rand_list)
    print(f"List is {rand_list}")
