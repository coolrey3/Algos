class Node():
    def __init__(self, data,priority):
        self.data = data
        self.priority = priority
        


#  dequeu does not consider insertion order for siblings, only checking prio
class PriorityQueue():
    def __init__(self) -> None:
        self.values = []
    
    def enqueue(self,val, priority):

        data = Node(val,priority)
        self.values.append(data)
        if len(self.values) <= 1:
            return self

        lastidx = len(self.values)-1
        cur = lastidx
        
        def bubbleUp(current,node):

            parent = (current-1) // 2
            if node.priority <= self.values[parent].priority:
                self.values[current] , self.values[parent] = self.values[parent], self.values[current]
                # print('parent node larger, swapped :', parent)
                return parent
            else:
                return True

        while True:
            run =  bubbleUp(cur,data)
            cur = run
            if cur == 0 or  self.values[run].priority >= self.values[(run-1) // 2].priority:
                break
            print(cur) # sortComplete = True

        return self

    def dequeue(self):
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
            elif self.values[l].priority < self.values[r].priority:
                childidx = l
            else:
                childidx = r
            
            if self.values[childidx].priority <= self.values[node].priority:
                self.values[node], self.values[childidx]= self.values[childidx],self.values[node]
            else:
                return node,True
            return childidx,False

        current = 0
        status  = False
        while status != True:
            current,status = sinkDown(current)

        return oldMax.data, oldMax.priority

er = PriorityQueue()
er.enqueue('common cold',5)
er.enqueue('gun shot wound',1)
er.enqueue('high fever',4)
er.enqueue('broken arm',2)
er.enqueue('glass in foot',3)
er.enqueue('stabbed',1)
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())