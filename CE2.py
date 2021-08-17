def countUniqueValues(n):
    temp = set(n)
    print(len(temp))

def cuv2Pointers(n):
    if n == []:
        print(0)
        return 0

    i = 0
    j = 0
    # for x in range(len(n)):
    checked = []
    while j != len(n):
        if n[i] not in checked:
            checked.append(n[i])
        if n[i] == n[j]:
            j += 1  
            i += 1
        else:
            j += 1  
    # print(checked)
    print(len(checked))


cuv2Pointers([1,1,1,1,1,2])
cuv2Pointers([1,2,3,4,4,4,7,7,12,12,13])
cuv2Pointers([])
cuv2Pointers([-2,-1,-1,0,1])
# countUniqueValues([1,1,1,1,1,2])