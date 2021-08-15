class Node():

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None
    
    def insert(self,data):

        node = Node(data)

        if self.root == None:
            self.root = node
            return self

        current = self.root

        while True:
            if node.data < current.data:
                if current.left == None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                else:
                    current = current.right

        return self

b = BinarySearchTree()
b.insert(15)
b.insert(5)
b.insert(3)
b.insert(2)
b.insert(45)
b.insert(25)
b.insert(41)

print(b.root.right.data)