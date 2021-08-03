class BubbleSort():
    def __init__(self,numberlist):
        print(numberlist)
        print('--------------')
        self.numberlist = numberlist
        sorted = False
        self.sorted = sorted

    def sort(self):
        while self.sorted == False:
            for x in range(len(self.numberlist)-1):
                # print(x)
                if self.numberlist[x] > self.numberlist[x+1]:
                    self.numberlist[x] , self.numberlist[x + 1] = self.numberlist[x + 1],self.numberlist[x]
            
            if self.numberlist == self.numberlist.sort():
                self.sorted = True
            

        print(self.numberlist)
        return self.numberlist

bs = BubbleSort([5,3,6,2,1,7,9])
bs.sort()