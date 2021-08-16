class Node():

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

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
        
        if self.root == None: return None

        current = self.root
        count = 0
        found = False

        while current and found != True:
            if val == current.data:
                found = True
                break
            if val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right
            count += 1
        if found == True:
            print(f'found in {count} steps')
            return True
        else:
            return False

    def breadth(self):
        visited = []
        queue = []
        current = self.root
        queue.append(current)

        while queue:
            if current.left:
                queue.append(current.left)
                print(current.left.data)
            if current.right != None:
                queue.append(current.right)
                print(current.right.data)

            visited.append(queue.pop(0)) or None
            if queue:
                current = queue[0]
        return visited

    def dfsPre(self):
        
        visited = []
        current = self.root

        def dfsPreHelper(current):
                visited.append(current)
                if current.left: dfsPreHelper(current.left)
                if current.right: dfsPreHelper(current.right)

        dfsPreHelper(current)
        return visited

    def dfsPost(self):
        
        visited = []
        current = self.root

        def dfsPostHelper(current):
                if current.left: dfsPostHelper(current.left)
                if current.right: dfsPostHelper(current.right)
                visited.append(current)

        dfsPostHelper(current)
        return visited

    def dfsinOrder(self):
        
        visited = []
        current = self.root

        def dfsInOrderHelper(current):
                if current.left: dfsInOrderHelper(current.left)
                visited.append(current)
                if current.right: dfsInOrderHelper(current.right)

        dfsInOrderHelper(current)
        return visited


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
b.insert(1)

# print(b.root.right.data)
print(b.find(17))


print(b.dfsinOrder())
print()

# [15, 5, 17, 0, 11, 33, 2, 30, 45, 1, 25, 41]