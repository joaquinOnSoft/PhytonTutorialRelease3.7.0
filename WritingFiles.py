import random


def write_binary_file(filnename: str):
    """
    Write 10 bytes (number from 0 to 9) in a binary file
    Args:
        filnename: file nale

    Returns: None

    """
    with open(filnename, "wb") as f:
        for i in range(10):
            f.write(bytearray([i]))

    f.close()


def read_finary_file(filename: str) -> list:
    numbers = []
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            byte = f.read(1)
            numbers.append(int.from_bytes(byte, "big"))
    f.close()

    return numbers


write_binary_file("binary.dat")
numbers = read_finary_file("binary.dat")
print(numbers)
