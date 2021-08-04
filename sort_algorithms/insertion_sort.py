class InsertionSort():

    def __init__(self,numberlist):
        print('InsertionSort numberlist: \n',numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self):
        for x in range(1,len(self.numberlist)):
            current = self.numberlist[x]
            previous = x-1
            while previous >= 0 and self.numberlist[previous] > current:
                self.numberlist[previous+1] = self.numberlist[previous]
                previous-= 1
            self.numberlist[previous+1] =current
        print(self.numberlist)

