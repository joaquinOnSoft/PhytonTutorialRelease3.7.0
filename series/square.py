def square(n) -> []:
    """
    Square Numbers Series: it is quite self explanatory: 1, 4,9,16,25,36,49...
    Args:
        n: Max number to calculate ethe square serie

    Returns:
        Square Numbers Serie until n
    """
    return [x**2 for x in range(n)]
