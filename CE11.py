def factorial(n):

    if n < 2: 
        return 1
    res = n * factorial(n-1)

    return res

print(factorial(1))
print(factorial(2))
print(factorial(4))
print(factorial(7))
# factorial(1)