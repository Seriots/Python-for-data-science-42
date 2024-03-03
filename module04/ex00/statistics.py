
def parse_args(func):
    """Decorator that checks if the args and kwargs are of the right type"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        try:
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError("All args values must be int or float")

            for _, value in kwargs.items():
                if not isinstance(value, str):
                    raise TypeError("All kwargs values must be str")
        except TypeError as e:
            print(e)
            return None

        return func(*args, **kwargs)

    return wrapper


@parse_args
def ft_statistics(*args: any, **kwargs: any) -> None:
    """Function that takes a list of numbers and a list of key
        args and displays some statistics based on the key args
    Args:
        *args: list of numbers
        **kwargs: list of key args
    key args:
        mean: the mean of the list
        median: the median of the list
        quartile: the quartiles of the list
        std: the standard deviation of the list
        var: the variance of the list
    Returns:
        None
    """
    for _, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")

        elif value == "mean":
            print(f"{value} : {sum(args) / len(args)}")

        elif value == "median":
            print(f"{value} : \
{(sorted(args)[len(args) // 2] + sorted(args)[(len(args) - 1) // 2]) / 2}")

        elif value == "quartile":
            quart1 = float(sorted(args)[len(args) // 4])
            quart3 = float(sorted(args)[int(len(args) / 4 * 3)])
            print(f"{value} : {[quart1, quart3]}")

        elif value == "std":
            mean = sum(args) / len(args)
            print(f"{(sum([(x - mean)**2 for x in args]) / len(args))**(1/2)}")

        elif value == "var":
            mean = sum(args) / len(args)
            print(f"{(sum([(x - mean)**2 for x in args]) / len(args))}")
