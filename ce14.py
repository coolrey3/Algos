def fib(n):
    
    if n <=2: return 1

    res = fib(n-1) + fib(n-2)

    return res

print(fib(4))
print(fib(10))
print(fib(28))
print(fib(35))
