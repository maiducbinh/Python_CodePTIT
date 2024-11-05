from math import *

p = [1] * (10 ** 6 + 1)
n = 10 ** 6
def sieve():
    p[0] = 0
    p[1] = 0
    for i in range(2, int(sqrt(n)) + 1):
        if p[i] == 1:
            for j in range(i * i, n + 1, i):
                p[j] = 0
def reverse(x):
    return int(str(x)[::-1])
sieve()
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n):
        j = reverse(i)
        if p[i] == 1 and p[j] == 1 and j < n and i < j:
            print(i, j, end = " ")
    print()