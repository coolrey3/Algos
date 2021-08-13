def merge( nums1, m, nums2, n) :
    
    i = 0
    j = 0
    
    while j < len(nums2):
        if nums2[j] > nums1[i] and nums1[i] != 0:
            i += 1
            if i == m+j:
                nums1[m+j] = nums2[j]
            else:   
                continue
        elif nums2[j] <= nums1[i] or nums1[i] == 0:
            # shift to rights and assign instead of insert
            nums1.insert(i,nums2[j])
            i =0
        # if 
        j+=1
    print(nums1)
        
def nestedLoop(n):
    lowest = 0
    for num in range(len(n)-1):
        for j in (range(num +1, len(n)-1)):
            if n[j] < n[lowest] :
                lowest = j
        print('lowest number is {} at index {}: '.format(n[lowest],lowest))


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

        # class Solution:
    def removeDuplicates(self, nums):
        # print(nums)

        count = 0
        j = 1
        while j != len(nums): #until j counter gets to end
            for i in range(len(nums)-1): # for each value in length arr
                # print(i)
                if nums[i] == nums[j] and nums[i] != '_': 
                    count += 1
                    nums[i] = '_'
                    for x in range(i,len(nums)-1):
                        nums[x],nums[x+1] = nums[x+1],nums[x]
                elif nums[i] == nums[i-1] and nums[i] != '_': 
                    count += 1
                    nums[i] = '_'
                    for x in range(i,len(nums)-1):
                        nums[x],nums[x+1] = nums[x+1],nums[x]
                j += 1

        # print('counter: ',count)
        last = len(nums)-count
        final = nums[:last]
        print(nums)
        return len(final)
                
# input: array int
# output: array with duplicates removed
# may need double pointer 


array = [7,5,6,1,4]
# merge([1,2,3,0,0,0],3,[2,5,6],3)
# i = insertionSort(array)
# i.removeDuplicates(array)
nestedLoop(array)