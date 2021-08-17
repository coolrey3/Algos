def prodOfArray(a):

    if a == []:
        return 1

    x = a.pop(0)
    res = x * prodOfArray(a)
        
    return res


print(prodOfArray([1,2,3]))
print(prodOfArray([1,2,3,10]))