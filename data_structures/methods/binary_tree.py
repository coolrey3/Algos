from binarytree import Node
# Create root
root = Node(4)
# Create nodes
node1 = Node(1)
node5 = Node(5)

# assign children to root
root.left = node1
root.right = node5

node0 = Node(0)
node3 = Node(3)
node1.left = node0
node1.right = node3

node5.left = Node(5)
node5.right = Node(10)

# Getting binary tree
print('Binary Tree: ',root)

# Getting list of nodes
print('List of nodes :', list(root))

# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)
print()
# Checking tree properties
print('Size of tree :', root.size)
print('Height of tree :', root.height)
print()

# Get all properties at once

def fancy():
    for k,v in root.properties.items():
        print("{} : {}".format(k , v))

print('Properties of tree : \n', fancy())
