def triangular(n) -> []:
    """
    Triangular number Series.
    A triangular number or triangle number counts the objects that can form an equilateral triangle.
    The nth triangle number is the number of dots or balls in a triangle with n dots on a side;
    it is the sum of the n natural numbers from 1 to n.

    The sequence of triangular numbers is: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ….

    Args:
        n: Max number to calculate ethe square serie

    Returns:
        Triangular Numbers Serie until n
    """
    return [int(x * (x+1)/2) for x in range(n)]
