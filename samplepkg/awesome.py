class AwesomeClass:
    def __init__(self, x=1, y=2):
        """A class that does awesome stuff.

        :param x: An awesome argument
        :param y: Another awesome argument
        """
        self.x = x
        self.y = y

    def awesome_method(self, z):
        """Method that does the awesome stuff.

        :param z: Some argument.
        :return: The awesome computation result
        """
        return self.x + self.y + z
