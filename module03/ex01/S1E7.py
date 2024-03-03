from S1E9 import Character


class Baratheon(Character):
    """A class representing the Baratheon family

    Inner class of Character
    Add the family name, eyes and hairs to the character
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize a new Baratheon character."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the character."""
        return \
            (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return a string representation of the character."""
        return \
            (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """A class representing the Lannister family

    Inner class of Character
    Add the family name, eyes and hairs to the character
    Add a static method to create a Lannister character
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize a new Lannister character."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(
            cls: Character,
            first_name: str,
            is_alive: bool = True
            ) -> Character:
        """Class method to create a Lannister character

        Args:
            cls (Character): Lannister class
            first_name (str): Name of the character
            is_alive (bool, optional): Set if is alive. Defaults to True.

        Returns:
            Character: An instance of Lannister
        """
        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """Return a string representation of the character."""
        return \
            (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return a string representation of the character."""
        return \
            (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")
