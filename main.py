class ArrayRepeater:
    """
    repeats iterable forever, like itertools.cycle
    """
    def __init__(self, values):
        self.values = values
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.values):
            self.current = 0
        value = self.values[self.current]
        self.current += 1
        return value


ar = ArrayRepeater([1, 2, 3])

a = list("hello")
print(list(zip(a, ar)))

