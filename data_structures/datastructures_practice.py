# Data value
# Pointer value
class Node():
    def __init__(self,data):
        self.data = data
        self.next=None
    def __repr__(self) :
        return 'Data: {} -> {}'.format(str(self.data),str(self.next))

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return 'Head: {} \nTail: {}'.format(str(self.head),str(self.tail.data))

    def push(self,node):
        
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length += 1
        
        else:
            self.length += 1
            self.tail.next = node
            self.tail = node


ll = SinglyLinkedList()
first = Node(5)
ll.push(first)
ll.push(Node(6))
ll.push(Node(9))
ll.push(Node(22))
ll.push(Node(31))
ll.push(Node(36))
ll.push(Node(45))
print(ll)
# ll.head = first
# first.next = Node(14)
# first.next.next = Node(33)
# print()
# print(ll.head)
