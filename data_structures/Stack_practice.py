class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"data: {self.data} -> {self.next}"


class Stack:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def __repr__(self):
        # current = self.first
        # while current != None:
        #     print(current)
        #     current = current.next
        return f"first: {self.first} \nlast: {self.last} \nsize: {self.size}"

    def push(self, node):
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp

        self.size += 1
        return self.size

    def pop(self):
        if self.first == None:
            return None

        temp = self.first
        self.first = temp.next
        temp.next = None

        self.size -= 1
        return temp


s = Stack()
s.push(Node(15))
s.push(Node(125))
s.push(Node(5))
s.push(Node(1))

# print(s.first.next)
print(s)
print()
print(s.pop())
print()
print(s)
