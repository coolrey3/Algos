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


    def practice(self):
        arr = self.numberlist
        for x in range(1,len(arr)): # for each number in array input
            current = arr[x] # current set to input arr[x] index 
            for j in range(x-1,-1,-1): # for range in everything to left of current
                if arr[j] > current: # if current in sorted array is greater than current in unsorted
                    arr[j+1] = arr[j]  # current in sorted +1 equal to current ( shifting to right in order)
                else:
                    arr[j+1] = current  # current in sorted is smaller than current unsorted,placing current unsorted next to current sorted
                    break
                arr[j] = current #assign place in sorted to current in correct index ( only runs if less than to replace value)
        print(arr)



array1 = [9,6,4,7,5,2,9,4,2,6,4,1,9,2]
t=InsertionSort(array1)
t.sortAscending()
# v = sorted(array1)
# print(v)
# if c == v:
#     print('true')




