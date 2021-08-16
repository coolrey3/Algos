class Node():
    def __init__(self):
        pass

class Graph():
    def __init__(self):
        self.adjacenyList = {}

    def addVertex(self,key):
        if key in self.adjacenyList:
            return
        self.adjacenyList[key] = []

    def addEdge(self,v1,v2):
        self.adjacenyList[v1].append(v2)
        self.adjacenyList[v2].append(v1)

    def removeEdge(self,v1,v2):
        self.adjacenyList[v1].remove(v2)
        self.adjacenyList[v2].remove(v1)

    def removeVertex(self,v1):
        r = self.adjacenyList.get(v1)
        for x in r:
            self.adjacenyList[x].remove(v1)
        self.adjacenyList.pop(v1)
        # print(r)
        

g =Graph()
g.addVertex('Tokyo')
g.addVertex('Alanta')
g.addVertex('Miami')
g.addVertex('New York')
g.addEdge('Miami','Alanta')
g.addEdge('Miami','New York')
print(g.adjacenyList)
g.removeEdge('Miami', 'New York')

g.removeVertex('Miami')

print(g.adjacenyList)