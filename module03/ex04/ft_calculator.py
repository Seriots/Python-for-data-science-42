class calculator:
    """
    Calculator class for vector operations between two vectors
    This class handle, dotproduct, add, sub operations
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors"""
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors"""
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors"""
        print(f"Sous Vecotr is: {[float(x - y) for x, y in zip(V1, V2)]}")
