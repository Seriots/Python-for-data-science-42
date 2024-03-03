
class ft_filter:
    def __init__(self, func, input):
        """
        @Brief          Constructor
        @Param func:    function to apply
        @Param input:   list of inputs
        @Returns        None
        """
        self.index = 0
        self.stock = [x for x in input if func(x)]

    def __iter__(self):
        """
        @Returns    ft_filter: return itself
        """
        return self

    def __next__(self):
        """
        @Brief          __next__ method
        @Exception      StopIteration: if index is greater
                            than the length of the stock
        @Returns        the next element of the stock
        """
        if self.index >= len(self.stock):
            raise StopIteration
        self.index += 1
        return self.stock[self.index-1]

    def __str__(self):
        """
        @Returns        str: string representation of the object
        """
        return str(f"<ft_filter object at {hex(id(self))}>")
