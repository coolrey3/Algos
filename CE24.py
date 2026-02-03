def linearSearch(arr, v):
    if arr == []:
        return False

    for i, x in enumerate(arr):
        if x == v:
            return i

    # if v in arr:
    #     return arr.index(v)

    return False


print(linearSearch([10, 15, 20, 25, 30], 15))
print(linearSearch([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4))
print(linearSearch([0], 0))
