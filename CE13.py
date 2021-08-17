def recursiveRange(n):
    if n == 0:
        return 0
    res = n +recursiveRange(n-1)

    return res

print(recursiveRange(6))
print(recursiveRange(10))