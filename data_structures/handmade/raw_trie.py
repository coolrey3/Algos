class Node:  # define node class
    def __init__(self, data):  # initiate with data parameter
        self.data = data  # set data of node from parameter
        self.child = None  # set child of node
        self.word = False

    def __repr__(self):
        return self.data


class Trie:
    def __init__(self):
        self.root = None
        self.children = []

    def __repr__(self):
        node = self.root
        word = []
        words = []
        while node is not None:
            word.append(node.data)
            if node.word == True:
                temp = ""
                for x in word:
                    temp += x
                words.append(temp)

            node = node.child
        print(" -> ".join(word))
        print(self.children)
        return str(words)


node1 = Node("c")
node2 = Node("a")
node3 = Node("t")
node4 = Node("c")
node5 = Node("h")
node6 = Node("e")
node7 = Node("r")
node5.word = True
node7.word = True
node1.child = node2
node2.child = node3
node3.child = node4
node4.child = node5
node5.child = node6
node6.child = node7

trie1 = Trie()
trie1.children.append("c")
trie1.children.append("t")
trie1.root = node1
print(trie1)
