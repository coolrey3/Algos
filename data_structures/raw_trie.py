class Node():   #define node class
    def __init__(self,data):    #initiate with data parameter
        self.data = data        #set data of node from parameter
        self.child = None       #set child of node
        self.word = False

    def __repr__(self):
        return '{} -> {}'.format(self.data,self.child)
        # return '{} -> {}'.format(self.data,self.child)

class Trie():
    def __init__(self):
        self.root = None

    def __repr__(self):
        node = self.root
        children = None
        # while self.root is not None:
        # children.append(str(node.child))
        #     node = node.child
        # return str(self.root) + "->".join(children)
        return str(self.root) 

node1 = Node('c')
node2 = Node('a')
node3 = Node('t')
node4 = Node('c')
node5 = Node('h')
node1.child = node2
node2.child = node3
node3.child = node4
node4.child = node5

trie1 = Trie()
trie1.root = node1
print(trie1)
