class MergeSort():

    def __init__(self,numberlist):
        print('MergeSort numberlist: \n',numberlist)
        print('--------------')
        self.numberlist = numberlist

    def sortAscending(self,array):

        if len(array) < 2:
            return
        else:
            middle = len(array) // 2
            # print(middle)
            firsthalf = array[:middle]
            secondhalf = array[middle:]

            print(firsthalf)
            print(secondhalf)
            print('************************')
            f = self.sortAscending(firsthalf)
            s = self.sortAscending(secondhalf)

            result = self.merge(firsthalf,secondhalf,self.numberlist)

        print(result)
        

    def merge(self, left,right,result):
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result[k] = left[i]
                # k+=1
                i+=1
            else:
                result[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            result[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            result[k] = right[j]
            j+=1
            k+=1
        return result

