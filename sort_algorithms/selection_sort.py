# selection sort selects the minimum value in array and sorts it in the 
# first index and does the same after each iteration for i+1 to end of array


class SelectionSort():

    def __init__(self,numberlist):
        print('SelectionSort numberlist: ',numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self):
        for x in range(len(self.numberlist)):
            print('x  is ',x)
            minimum = min(self.numberlist[x:])
            print('Remaining list is:', (self.numberlist[x:]))
            print('Minimum Number in array: ',minimum)
            temp = self.numberlist[x:].index(minimum) +x
            print('index of minimum number is:', temp)
            print(self.numberlist)

            if minimum != self.numberlist[x]:
                self.numberlist[temp] ,self.numberlist[x]= self.numberlist[x], self.numberlist[temp]
