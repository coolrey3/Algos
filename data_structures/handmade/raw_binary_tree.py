# Define class of Node
# declare a data value
# declare a left child
# declare a right child

# Define the class BinaryTree
# declare a root variable


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __repr__(self):
        return self.data


class BinaryTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        node = self.root
        # print(node)
        i = 0
        print("RIGHT EXPANDED")
        while node is not None:
            print(self.printChildren(node, i, "right"))
            # if node.lchild is not None:
            # node = node.lchild
            # if node.rchild is not None:
            node = node.rchild
            #     noder = node.rchild
            i += 1
        j = 0
        node = self.root
        print("LEFT EXPANDED")
        while node is not None:
            print(self.printChildren(node, j, "left"))
            node = node.lchild
            j += 1

        print("*************************")

        return self.root.data
        # return self.printChildren(node,1)

    def printChildren(self, node, x, direction):
        if node is not None:
            # print('from inside ',node)
            # if node.rchild and node.lchild is not None:\
            if x < 1:
                return "\t  {}{}  \n \t{}{}   {}".format("        " * x, node, "   " * x, node.lchild, node.rchild)
            else:
                if direction == "right":
                    return "\t{}{} {}".format("   " * x, node.lchild, node.rchild)
                if direction == "left":
                    return "    {}{} {}".format("   " * x, node.lchild, node.rchild)


bt = BinaryTree()
node1 = Node("10")
node2 = Node("20")
node3 = Node("30")
node4 = Node("4")
node5 = Node("5")
node6 = Node("40")
node7 = Node("1")
node8 = Node("5")

bt.root = node1
node1.lchild = node4
node1.rchild = node3

node3.lchild = node2
node3.rchild = node6

node4.lchild = node7
node4.rchild = node8

print(bt)

# print(bt.printChildren(node1))
# print(bt.printChildren(node2))
# print(bt.printChildren(node3))
