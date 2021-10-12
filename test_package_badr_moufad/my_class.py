from test_package_badr_moufad.my_functions import say_hello, say_joke


class Person:
    """A person class to interact with a user
    """

    def __init__(self, username: str) -> None:
        """constructor of the class

        Parameters
        ----------
        username : str
            the name of the user

        Examples
        --------
        >>> print("This is an example")
        This is an example
        """

        self.username = username

    def greet(self) -> None:
        """To greet user
        """

        say_hello(self.username)

    def joke(self) -> None:
        """To tell a joke
        """

        say_joke()
