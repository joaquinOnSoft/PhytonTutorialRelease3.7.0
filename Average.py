import doctest


def average(values: []) -> float:
    return sum(values) / len(values)


doctest.testmod()
