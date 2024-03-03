def check_input(func) -> object:
    """Decorator that checks if the input is of the right type"""
    def wrapper(x: int | float) -> object | None:
        """Wrapper function"""
        if not isinstance(x, (int, float)):
            print(f"Invalid input: {x}")
            return None
        return func(x)
    return wrapper


@check_input
def square(x: int | float) -> int | float:
    """Return x squared"""
    return x ** 2


@check_input
def pow(x: int | float) -> int | float:
    """Return x to the power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that takes no arguments and returns
        the result of applying the function to the current value of x

    Args:
        x (int | float): value to be used in the function
        function (_type_): function to be used

    Returns:
        object: Callable function
    """
    count = 0
    current_value = x

    def inner() -> float:
        nonlocal count
        nonlocal current_value
        current_value = function(current_value)
        count += 1

        return current_value
    return inner
