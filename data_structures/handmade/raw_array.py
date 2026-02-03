class RawArray:
    def __init__(self):
        x = []
        self.x = x
        ...

    def insert(self, value):
        self.x.append(value)
        return self.x

    def insertAt(self, value, index):
        self.x.insert(index, value)
        return self.x

    def removeAt(self, index):
        self.x.pop(index)

    def print(self):
        print(self.x)

    def max(self):
        print(max(self.x))


numbers = RawArray()
numbers.insert(4)
numbers.insert(2)
numbers.insert(8)
numbers.insertAt(9, 1)
numbers.max()
numbers.print()
numbers.removeAt(2)
numbers.print()
