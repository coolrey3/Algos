class InsertionSort():

    def __init__(self,numberlist):
        print('InsertionSort numberlist: ',numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self):
        for x in range(1,len(self.numberlist)):
            current = self.numberlist[x]
            j = x-1
            while j >= 0 and self.numberlist[j] > current:
                self.numberlist[j+1] = self.numberlist[j]
                j-= 1
            self.numberlist[j+1] =current
        print(self.numberlist)

