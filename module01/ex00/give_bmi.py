def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """Compute the BMI for each pair of height/weight

    Args:
        height (list[int  |  float]): A list of height in meters
        weight (list[int  |  float]): A list of weight in kilograms

    Returns:
        list[int | float]: The BMI conputation for each pair of height/weight

    Errors:
        If the two list are not the same size, an AssertException is raise
    """
    try:
        assert len(height) == len(weight), \
            "AssertionError: list must be the same size"

        assert all([type(x) in [int, float] for x in height + weight]), \
            "AssertionError: list must contain only int or float"

    except AssertionError as e:
        print(e)
        return []

    return [weight / (height ** 2) for weight, height in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Compare each value in BMI list with the limit

    Args:
        bmi (list[int  |  float]): A list of computed BMI
        limit (int): The limit to apply to each value in BMI list,
                        if the value is greater than the limit,
                        the result will be True, otherwise False

    Returns:
        list[bool]: A list of bool for each value in BMI list
                         computed with the limit
    """
    try:
        assert all([type(x) in [int, float] for x in bmi]), \
            "AssertionError: list must contain only int or float"

        assert isinstance(limit, int), \
            "AssertionError: limit must be an integer"
    except AssertionError as e:
        print(e)
        return []

    return [True if value > limit else False for value in bmi]
