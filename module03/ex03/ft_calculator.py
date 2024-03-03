class calculator:
    """
    Calculator class for vector operations
    This class handle, +, -, *, / operations
    """
    def __init__(self, vector: list) -> None:
        """Initialize a new calculator object.

        Args:
            vector (list): The vector to be used for operations
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a number to the vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply a number to the vector"""
        self.vector = [x * object for x in self.vector] 
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a number to the vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide a number to the vector"""
        if object == 0:
            print("Division by 0 is not possible")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
