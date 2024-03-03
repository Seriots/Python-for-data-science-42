from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The king of the seven kingdoms"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a new King character."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get the eyes color of the king"""
        print("eyes getter")
        return (self.eyes)

    def set_eyes(self, eyes_color: str):
        """Set the eyes color of the king"""
        print("eyes setter")
        self.eyes = eyes_color

    def get_hairs(self):
        """Set the hairs color of the king"""
        print("hairs getter")
        return (self.hairs)

    def set_hairs(self, hairs_color: str):
        """Set the hairs color of the king"""
        print("hairs setter")
        self.hairs = hairs_color

    _hairs = property(get_hairs, set_hairs)
    _eyes = property(get_eyes, set_eyes)
