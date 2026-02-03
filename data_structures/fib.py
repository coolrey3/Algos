stored = {}


def fib(n):
    # result = None
    if n <= 2:
        return 1

    if n not in stored:
        result = fib(n - 1) + fib(n - 2)
        stored[n] = result
    else:
        val = stored[n]
        return val
    return result


def fibBUp(n, memo=[None]):
    if len(memo) <= 2:
        memo = memo * n
    # print(memo)
    if memo[n - 1] != None:
        return memo[n - 1]
    if n <= 2:
        return 1
    result = fibBUp(n - 1, memo) + fibBUp(n - 2, memo)
    memo[n - 1] = result
    return result


# print(fib(3000))
print(fibBUp(100))
