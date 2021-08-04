from sort_algorithms.bubble_sort import * 
from sort_algorithms.selection_sort import * 
from sort_algorithms.insertion_sort import * 
from sort_algorithms.merge_sort import * 

array = [4,5,3,1,9,8,7]

# bs = BubbleSort(array)
# bs.sortAscending()
# bs.sortDescending()

# ss = SelectionSort(array)
# ss.sortAscending()

# ins = InsertionSort(array)
# ins.sortAscending()

ms = MergeSort(array)
ms.sortAscending(array)