class BubbleSort():
    def __init__(self,numberlist):
        print('Raw numberlist: ',numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self):
        isSorted = {}
        sortComplete = False
        while sortComplete == False:
            for x in range(len(self.numberlist)-1):
                if self.numberlist[x] > self.numberlist[x+1]:
                    self.swap(self.numberlist,x,x+1)
                    # self.numberlist[x] , self.numberlist[x + 1] = self.numberlist[x + 1],self.numberlist[x]
                    isSorted[x] = False
                else:
                    isSorted[x] = True
            if False not in isSorted.values():
                sortComplete = True
        print('Array sorted with Bubble Sort-Ascending:\n',self.numberlist)
        return self.numberlist

    def sortDescending(self):
        isSorted = {}
        sortComplete = False
        while sortComplete == False:
            for x in range(0,len(self.numberlist)-1):
                if self.numberlist[x] < self.numberlist[x+1]:
                    self.swap(self.numberlist,x,x+1)
                    # self.numberlist[x] , self.numberlist[x + 1] = self.numberlist[x + 1],self.numberlist[x]
                    isSorted[x] = False
                else:
                    isSorted[x] = True
            if False not in isSorted.values():
                sortComplete = True
        print('Array sorted with Bubble Sort-Descending:\n',self.numberlist)
        return self.numberlist

    def swap(self,array,index1,index2):
        array[index1] , array[index2] = array[index2],array[index1]
        return


