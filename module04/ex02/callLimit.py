
def check_input(func) -> object:
    """Decorator that checks if the input is of the right type"""
    def wrapper(x: int) -> object | None:
        """Wrapper function"""
        if not isinstance(x, int):
            print(f"Invalid input: {x}")
            return None
        return func(x)
    return wrapper


@check_input
def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called"""
    count = 0

    def callLimiter(function):
        """Wrapper function"""

        def limit_function(*args: any, **kwds: any):
            """Wrapper function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <{function.__name__} at \
{hex(id(function))}> call too many times")
                return None
        return limit_function
    return callLimiter
