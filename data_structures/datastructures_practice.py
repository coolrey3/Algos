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
        if self.length !=0:
            return 'Head: {} \nTail: {} Length: {}'.format(str(self.head),str(self.tail.data),str(self.length))
        else:
            return 'Linked List is Empty'
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
        if self.length == 0: return None

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
            elif current.next == None and self.length == 1:
                self.length -= 1
                self.head = None
                self.tail = None
            else:
                current = current.next
        print('Popping:',popNode)
        print('New Tail: ',self.tail)
        return popNode

    def shift(self):
        if self.length == 0: return None
        oldHead = self.head
        self.head = oldHead.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        oldHead.next = None
        return oldHead

    def unshift(self,node):
        if self.head == None:
            self.head =node
            self.tail = node
        else:
            oldHead = self.head
            self.head = node
            self.head.next = oldHead
            self.length += 1
        return self

    def get(self,index):
        if index >= self.length or index <= 0: return None
        i = 0
        current = self.head
        while i != index:
            current = current.next
            i += 1
        return current
    
    def set(self,index,data):
        current = self.get(index)
        current.data = data
        return current


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
print(ll.unshift(Node(99)))

print('before')
print(ll.get(4))
print()
print(ll.set(4,100))
print('after')

print(ll.get(4))
print()
print(ll)

# ll.head = first
# first.next = Node(14)
# first.next.next = Node(33)
# print()
# print(ll.head)
