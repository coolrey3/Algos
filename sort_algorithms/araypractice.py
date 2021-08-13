# **********************************************************************************************
#* 1. Bubble Sort:
#*    Time Complexity : Best => O(n) , Worst & Average => O(n*n)
#*    Space Complexity: O(1) 
#*    Stablitiy       : Stable
#*    Is-In-Place     : In-Place	
#*    When to use     : 1. If array is of small size 
#* 		             2. If array is of large size but nearly sorted
#*    Remark          : Easiest to implement	
#*    Description:      Bubble sort compares each value in array to 
#*                      the one next to it and if first is smaller
#*                      than second, swaps the two. Loops over until
#*                      array is sorted

class BubbleSort():
    def __init__(self,arr):
        original = arr[:]   #copy input  for logging purposes
        sortComplete = False  # declare sortComplete to False
        while sortComplete != True:  #while sortComplete False loop 
            sortComplete=True        #set sortcomplete to true
            for x in range(len(arr)-1):  #iterate over range of array index
                if arr[x] > arr[x +1]:   #if current index greater than next
                    arr[x],arr[x+1] = arr[x+1], arr[x]  #swap values
                    sortComplete= False  #set sortComplete to False because list is not sorted
                                        #we know this because we just did 1 swap this iteration
        print('Input: ',original)
        print('Output: Bubble Sort: ',arr) 

bs = BubbleSort([4,6,2,34,76,31,3,9,8])

# **********************************************************************************************
#* 2. Selection Sort:
#*    Time Complexity : Best & Worst & Average => O(n*n)
#*    Space Complexity: O(1) 
#*    Stablitiy       : Not-Stable
#*    Is-In-Place     : In-Place
#*    When to use     : 1. If array is of small size
#* 		             2. To minimise the number of swaps
#*    Remarks         : Bubble sort has more number of swaps as compare to selection
#* 		             Sort but bubble sort has better best time complexity.
#* 		             It can also be implemented as stabaly.
#* 		             Selection sort makes O(n) swaps which is minimum among all sorting algorithms mentioned above.	
#*    Description:


# **********************************************************************************************
#* 3. Insertion Sort:
#*    Time Complexity : Best => O(n) , Worst & Average => O(n*n)
#*    Space Complexity: O(1) 
#*    Stablitiy       : Stable
#*    Is-In-Place     : In-Place
#*    When to use     : 1. If array is of small size and nearly sorted
#*    Remark          : Standard Libraray of C uses this algo when n becomes smaller
#* 		             than a threshold and for small size it is better than merge
#* 		             and quick sort becasue of low constant values and non
#*  		             recusive in nature.
#*    Description:

# **********************************************************************************************
#* 4. Heap Sort:
#*    Time Complexity : Best & Worst & Average => O(nLog(n))
#*    Space Complexity: O(1) 
#*    Stablitiy       : Not-Stable
#*    Is-In-Place     : In-Place
#*    When to use     : When the input array is large and stable sort is not 
#*                      required.		
#*    Remark          : It always guaranteed to be O(nLog(n)) with constant space 
#*                      which solves the problem of overflow of address space of a 
#*                      process which may occur in merge and quick sort(recursive stack).
#*    Description:

# **********************************************************************************************
#* 5. Counting Sort:
#*    Time Complexity : Best & Worst & Average => O(n+k)
#*    Space Complexity: O(n+k) 
#*    Stablitiy       : Not-Stable
#*    Is-In-Place     : In-Place
#*    Description:


# **********************************************************************************************
#* 6. Merge Sort:
#*    Time Complexity : Best & Worst & Average => O(nLog(n))
#*    Space Complexity: O(n) 
#*    Stablitiy       : Stable 
#*    Is-In-Place     : Not-In-Place
#*    Tag             : Divide & Conquer
#*    When to use     : 1.When we don't have random access(linked list)
#*                       [R.A like as we have in array]
#*                      2.When array is not to large.
#*    Description:


# **********************************************************************************************
#* 7. Quick Sort:
#*    Time Complexity : Best => O(nLog(n)) , Worst => O(n*n) 
#*    Space Complexity: O(n) 
#*    Stablitiy       : Not-Stable 
#*    Is-In-Place     : In-Place
#*    Tag             : Divide & Conquer
#*    When to use     : 1.It is prefered over merge sort for extremely large array
#*                      2.When you don't care about worst case complexity
#*    Description:

#* ----------------------------------------------------------------------------------------------
# **********************************************************************************************