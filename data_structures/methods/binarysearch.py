from binarytree import bst

# Create random binary search tree
# of any height

root = bst()
print("BST of any height: \n", root)

# Create random BST of given height
root2 = bst(height=4)
print("BST of given height: \n", root2)

# Create a random perfect BST of given height
root3 = bst(height=3, is_perfect=True)
print("Perfect BST of given height: \n", root3)
