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

    def dfsRecursive(self,start):
        visited = []
        result = []
        current = start
        visited.append(current)

        def dfs(current):
            cur = self.adjacenyList.get(current)
            if cur != []:
                for x in cur:
                    if x not in visited :
                        visited.append(x)
                        print(x)
                        dfs(x)
                return x

        dfs(current)
        
        return visited

        

g =Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('B','D')
g.addEdge('E','C')
g.addEdge('D','E')
g.addEdge('D','F')
g.addEdge('E','F')
print(g.adjacenyList)
# g.removeEdge('Miami', 'New York')

# g.removeVertex('Miami')

print(g.adjacenyList)

g.dfsRecursive('E')