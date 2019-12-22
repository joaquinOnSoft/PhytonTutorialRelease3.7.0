class Reverse:
    def __init__(self, string: str):
        self.string = string
        self.lenght = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.lenght > 0:
            self.lenght -= 1
            return self.string[self.lenght]
        else:
            raise StopIteration
