def BinarySearch(arr, v):
    if arr == []:
        return -1

    mid = len(arr) // 2
    l = 0
    r = len(arr) - 1

    if v == arr[mid]:
        print("herte", mid)
        return mid

    while v != arr[mid] and l <= r:
        if v < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
        mid = (l + r) // 2
    print("index is a", mid)

    print(arr)
    if arr[mid] == v:
        return mid
    else:
        return -1


BinarySearch([2, 5, 6, 9, 13, 15, 28, 30], 30)
BinarySearch([1, 2, 3, 4, 5], 2)
BinarySearch([1, 2, 3, 4, 5], 3)
BinarySearch([1, 2, 3, 4, 5], 5)
BinarySearch([1, 2, 3, 4, 5], 6)
