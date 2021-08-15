class Node():

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None

#     def __repr__(self):
#         # for x in 
#         current = self.root
#         while current != None:
#             print( f'''{current.data}
#     / \\
# {current.left.data}    {current.right.data}
#             ''')
#             current = current.left
    
    def insert(self,data):

        node = Node(data)

        if self.root == None:
            self.root = node
            return self

        current = self.root

        while True:
            if node.data == current.data: break
            if node.data < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

        return self

    def find(self,val):
        ...

b = BinarySearchTree()
b.insert(15)
b.insert(5)
b.insert(5)
b.insert(11)
b.insert(17)
b.insert(33)
b.insert(30)
b.insert(0)
b.insert(2)
b.insert(45)
b.insert(25)
b.insert(41)

print(b.root.right.data)
print(b)

