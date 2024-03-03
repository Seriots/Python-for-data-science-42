
def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the list from start to end

    Args:
        family (list): The list to slice
        start (int): The first index to include in the slice
        end (int): The last index in the slice (excluded)

    Returns:
        list: The new list sliced from start to end
    """

    try:
        assert isinstance(family, list), \
            "AssertionError: family must be a list"
    except AssertionError as e:
        print(e)
        return []
    if len(family) == 0:
        return []
    size = len(family[0])

    try:
        assert isinstance(start, int), \
            "AssertionError: start must be an integer"

        assert isinstance(end, int), \
            "AssertionError: end must be an integer"

        assert all([len(x) == size for x in family]), \
            "AssertionError: All elements in the list must have the same size"

    except AssertionError as e:
        print(e)
        return []

    print(f"My shape is : ({len(family)}, {size})")
    # out = family[start:end]
    out = family[slice(start, end)]
    print(f"My new shape is : ({len(out)}, {size})")

    return out
