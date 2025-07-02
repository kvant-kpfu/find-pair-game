n=int(input())
def isPrime(m):
    d = 2
    while m % d != 0:
        d += 1
    return d == m
print(isPrime(n))