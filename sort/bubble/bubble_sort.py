class BubbleSort():
    def __init__(self,numberlist):
        print(numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self):
        solved = sorted(self.numberlist)
        sortComplete = False
        while sortComplete == False:
            for x in range(len(self.numberlist)-1):
                if self.numberlist[x] > self.numberlist[x+1]:
                    self.numberlist[x] , self.numberlist[x + 1] = self.numberlist[x + 1],self.numberlist[x]
            
            if self.numberlist == solved:
                sortComplete = True
           

        print('Array sorted: ',self.numberlist)
        return self.numberlist

bs = BubbleSort([6,4,3,7,4,3,2,7,4,3,6,7,8,4,2,0])
bs.sortAscending()
