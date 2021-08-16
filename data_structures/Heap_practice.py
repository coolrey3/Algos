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

mh = MaxBinaryHeap()
mh.insert(41)
mh.insert(39)
mh.insert(33)
mh.insert(18)
mh.insert(27)
mh.insert(12)
mh.insert(55)
mh.insert(1)
mh.insert(45)
mh.insert(199)
print(mh.values)