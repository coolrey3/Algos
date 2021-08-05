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

    def sort(self):
        A = self.numberlist
        # itterate over list from index 1 to end
        # counter to 0
        # compare current value with previous, if previous is bigger 
        # insert to right of sorted portion
        
        for x in range(1,len(A)):
            current = A[x]
            for j in range(x-1,-1,-1):
                if A[j] > current:
                    A[j+1] = A[j]
                else:
                    A[j+1] = current
                    break
                A[j] = current
        print(A)
        return A

array1 = [9,6,4,7,5,2,9,4,2,6,4,1,9,2]
t=InsertionSort(array1)
c = t.sort()
v = sorted(array1)
print(v)
if c == v:
    print('true')




