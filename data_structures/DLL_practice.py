class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return f"{self.data} -> {self.next}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        if self.head != None:
            return f"Length: {self.length} \nHead: {self.head.data} -> {self.head.next}\nTail: {self.tail}"
        else:
            return "List empty"

    def push(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return self

        currentTail = self.tail
        currentTail.next = node
        self.tail = node
        self.tail.previous = currentTail

        self.length += 1

    def pop(self):
        poppedNode = self.tail

        if self.head == None:
            return self

        if self.length == 1:
            self.head = None
            self.tail = None
            return self

        self.tail = poppedNode.previous
        self.tail.next = None
        self.length -= 1
        poppedNode.previous = None
        return poppedNode

    def shift(self):
        if self.length == 0:
            return None

        shiftedNode = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return shiftedNode

        self.head = shiftedNode.next
        shiftedNode.next = None
        self.head.previous = None
        self.length -= 1
        return shiftedNode

    def unshift(self, node):
        if self.head == None:
            self.push(node)
            return self

        self.head.previous = node
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        mid = self.length // 2
        if index <= mid:
            i = 0
            current = self.head
            while i != index:
                current = current.next
                i += 1
            print("from beginning")
            print(current)
            return current

        else:
            i = self.length - 1
            current = self.tail
            while i != index:
                current = current.previous
                i -= 1
            print("from end")
            print(current)
            return current

    def set(self, index, data):
        current = self.get(index)
        if current:
            current.data = data
        else:
            return None


first = Node(5)
dl = DoublyLinkedList()
dl.push(first)
dl.push(Node(199))
print(dl)

dl.push(Node("last"))
# # dl.pop()
# print(dl.pop().previous)
dl.unshift(Node(55))

print(dl)
print()

dl.get(3)
dl.set(3, 420)
dl.get(3)
print(dl)
