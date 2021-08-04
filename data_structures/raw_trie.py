class createTrie():
    def __init__(self):
        x={}
        x ['root'] =''
        self.x = x
        self.x['child'] = []
        self.x['isWord'] = ''
        print(self.x)
        current = 0


    def newNode(self,child,isWord):
        if child not in self.x['child']:
            self.x['child'].append(child)
        if isWord == True:
            self.x['isWord'] = isWord
        print(self.x)

ct = createTrie()
ct.newNode('T', False)
ct.newNode('V', True)