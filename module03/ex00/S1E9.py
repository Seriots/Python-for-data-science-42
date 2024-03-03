from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for a character"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a new character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill off a character."""
        self.is_alive = False


class Stark(Character):
    """A class representing the Stark family
        Or when bad things happen to good people."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a new Stark character."""
        super().__init__(first_name, is_alive)
