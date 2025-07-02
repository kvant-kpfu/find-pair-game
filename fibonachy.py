def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + f(n - 2)

def sum_fib(l, r):
    total = 0
    n = 1
    while True:
        fib = f(n)
        if fib > r:
            break
        if fib >= l:
            total += fib
        n += 1
    return total

l = int(input())
r = int(input())
result = sum_fib(l, r)
print(result)