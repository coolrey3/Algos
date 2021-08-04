class LinkedList():
    def __init__(self):
        # self.newLL()
        l= {}
        self.l = l
        self.l['first'] = ''
        self.l['last'] = ''
        self.l['nodes'] = []
        print(self.l)
    
    def newLL(self,first= '',last = ''):
        self.l['first'] = first
        self.l['last'] = last

    def newNode(self,value=''):
        node = {}
        node['value'] = value
        
        if self.l['first'] == '':
            self.l['first'] = node['value']
            self.l['nodes'].append(node)
        else:
            self.l['nodes'].append(node)
        print(self.l)

        secondLastIndex = len(self.l['nodes'])-2
        print(self.l['nodes'][secondLastIndex]['value'])
        if len(self.l['nodes'])  >= 1 :
            node['next'] = self.l['nodes'][secondLastIndex]['value']

ll = LinkedList()
ll.newNode(5)
ll.newNode(1)
ll.newNode(3)
ll.newNode(4)

