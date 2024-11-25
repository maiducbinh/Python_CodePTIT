from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if prime(a[i]):
        b.append(a[i])
b.sort()
for i in range(n):
    if prime(a[i]):
        print(b[0], end = " ")
        b.pop(0)
    else:
        print(a[i], end = " ")    