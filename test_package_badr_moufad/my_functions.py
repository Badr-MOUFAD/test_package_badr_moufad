import numpy as np


def say_hello(username: str):
    """A function to greet a user

    Parameters
    ----------
    username : str
        the username

    Examples
    --------
    >>> say_hello("Badr MOUFAD")
    Hi there! Nice to meet you Badr MOUFAD
    """

    print(f"Hi there! Nice to meet you {username}")
    return


def say_joke():
    """A function to say a joke
    """

    print(f"Your as** is {np.random.rand()}\nAHAHAHAHA")
    return
