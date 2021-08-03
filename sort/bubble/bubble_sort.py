class BubbleSort():
    def __init__(self,numberlist):
        print(numberlist)
        print('--------------')
        self.numberlist = numberlist
        self.solved = sorted(self.numberlist)

    def sortAscending(self):
        sorted = False
        while sorted == False:
            for x in range(len(self.numberlist)-1):
                # print(x)
                if self.numberlist[x] > self.numberlist[x+1]:
                    self.numberlist[x] , self.numberlist[x + 1] = self.numberlist[x + 1],self.numberlist[x]
            
            if self.numberlist == self.solved:
                sorted = True
            # else:
            #     print('still not sorted')
                # print(self.numberlist)
            

        print('Array sorted: ',self.numberlist)
        return self.numberlist

bs = BubbleSort([5,3,6,2,1,7,9])
bs.sortAscending()
