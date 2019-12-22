#Fibonacci numbers module


def fib(n):
    numbers = []

    a, b = 0, 1
    while a < n:
        numbers.append(a)
        a, b = b, a + b

    return numbers


def print_fib(n):
    """
    Print the Fibonacci sequence until n
    Args:
        n: Max number to calculate the Fibonacci sequence
    """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

