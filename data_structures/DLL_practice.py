
class Node():
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
    
    def  __repr__(self):
        return "{} -> {}".format(self.data,self.next)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def  __repr__(self):
        return "Length: {} \n Head: {} -> {}".format(self.length,self.head.data,self.head.next)

    def push(self,node):

        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return self
        
        currentTail = self.tail
        currentTail.next = node
        self.tail  = node
        self.tail.previous = currentTail

        self.length += 1

first = Node(5)
dl= DoublyLinkedList()
dl.push(first)
dl.push(Node(199))

print(dl)
print(dl.tail)