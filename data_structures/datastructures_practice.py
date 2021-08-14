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
        return 'Head: {} \nTail: {} Length: {}'.format(str(self.head),str(self.tail.data),str(self.length))

    def push(self,node):
        
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length += 1
        
        else:
            self.length += 1
            self.tail.next = node
            self.tail = node
        return self

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def pop(self):
        current = self.head
        tempTail = self.tail
        popNode = None
        while current != None:
            # print(current.data)
            if current.next == tempTail:
                popNode = current.next
                self.tail = current
                self.tail.next = None
                self.length -= 1
            else:
                current = current.next
        print('Popping:',popNode)
        print('New Tail: ',self.tail)
        return popNode


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
print()
# ll.traverse()
ll.pop()
print()
print(ll)

# ll.head = first
# first.next = Node(14)
# first.next.next = Node(33)
# print()
# print(ll.head)
