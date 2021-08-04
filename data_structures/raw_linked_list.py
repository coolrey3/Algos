class Node:                 # define Node Class
    def __init__(self, data): #initialize a new node that takes data parameter
        self.data = data    # assign data value via parameter to this node
        self.next = None    #assign pointer to next node(defaults to none)

    def __repr__(self):     #modify string representation when printed 
        return self.data    #return data value when printing node

class LinkedList:           # define LinkedList Class
    def __init__(self):     #initialize linked list, no parameters
        self.head = None    # assign head of linked list to None when initialized

    def __repr__(self):     #modify string representation when printed (otherwise prints object location in memory)
        node = self.head    #assign head of linked list to node
        nodes = []          #create empty array for child nodes
        while node is not None:     #iterate while head node is not None
            nodes.append(node.data) #append nodes array with node data
            node = node.next        #head node set to next node (only once)
        nodes.append("None")        #append None to end of nodes array
        return " -> ".join(nodes)   #return the list of array with -> between each item

llist = LinkedList()        #instantiate linkedlist class

first_node = Node('a')      #instantiate Node class
# print(first_node)
# print(llist)
llist.head = first_node     #assign head of linkedlist to first node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)

# node = Node()
# node.newNode(ll,5)
# ll.newNode(5)
# ll.newNode(1)
# ll.newNode(3)
# ll.newNode(4)

