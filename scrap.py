class insertionSort():
    def __init__(self,A):
        for x in range(1,len(A)):
            current = A[x]
            for j in range(x-1,-1,-1):
                if A[j+1] < A[j]:
                    A[j+1] = A[j]
                else:
                    A[j+1] = current
                    break
                A[j] = current
        print(A)

array = [1,6,6,8,1,2,87,4,3,54,69]
isort = insertionSort(array)
