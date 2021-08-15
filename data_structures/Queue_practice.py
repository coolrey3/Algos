
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self,data):

        node = Node(data)

        if self.first == None:
            self.first = node
            self.last = node
            # self.size += 1
            # return self.size
        else:        
            self.last.next = node
            self.last = node
        self.size += 1
        return node



    def dequeue(self):
        
        if self.first == None:
            return None

        temp = self.first

        
        if self.first == self.last:
            self.last = None

        self.first = temp.next
        temp.next = None
        self.size -= 1

        return self.first