class MaxBinaryHeap():
    def __init__(self) -> None:
        self.values = []
    
    def insert(self,data):

        self.values.append(data)
        if len(self.values) <= 1:
            return self

        lastidx = len(self.values)-1
        cur = lastidx
        
        def bubbleUp(current,node):

            parent = (current-1) // 2
            if node >= self.values[parent]:
                self.values[current] , self.values[parent] = self.values[parent], self.values[current]
                print('parent node larger, swapped :', parent)
                return parent
            else:
                return True

        while True:
            run =  bubbleUp(cur,data)
            cur = run
            if cur == 0 or  self.values[run] <= self.values[(run-1) // 2]:
                break
            print(cur) # sortComplete = True

        return self

    def remove(self):
        if len(self.values) == 0:
            return None

        lastidk = len(self.values)-1
        self.values[0],self.values[lastidk] = self.values[lastidk], self.values[0] 


        oldMax = self.values.pop()

        def sinkDown(node):
            l= node*2 +1
            r= node*2 +2

            if l >= len(self.values): return node,True
            if r >= len(self.values): childidx = l
            elif self.values[l] > self.values[r]:
                childidx = l
            else:
                childidx = r
            
            if self.values[childidx] >= self.values[node]:
                self.values[node], self.values[childidx]= self.values[childidx],self.values[node]
            else:
                return node,True
            return childidx,False

        current = 0
        status  = False
        while status != True:
            current,status = sinkDown(current)

        return oldMax

mh = MaxBinaryHeap()
mh.insert(41)
mh.insert(39)
mh.insert(33)
mh.insert(18)
mh.insert(27)
mh.insert(12)
mh.insert(55)
print(mh.values)
print(mh.remove())
print(mh.remove())
# mh.insert(1)
# mh.insert(45)
# mh.insert(199)
# mh.insert(3)
# mh.insert(210)
print(mh.values)