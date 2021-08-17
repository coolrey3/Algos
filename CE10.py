def power(base, x):
    
    if x == 0:
        return 1 
    res = base * power(base,x-1)
    
    # print(res)
    return res

print(power(2,0))
print(power(2,2))
print(power(2,4))
