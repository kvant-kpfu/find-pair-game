def sum_fib(l, r):
    total = 0
    a, b = 1, 1
    while a <= r:
        if a >= l:
            total += a
        a, b = b, a + b
    return total

l = int(input())
r = int(input())
result = sum_fib(l, r)
print(result+1)