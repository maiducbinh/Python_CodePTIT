from math import *

p = [0] * (10 ** 6 + 1)
n = 10 ** 6
def sieve():
    for i in range(2, n + 1):
        p[i] = 1
    for i in range(2, int(sqrt(n)) + 1):
        if p[i] == 1:
            for j in range(i * i, n + 1, i):
                p[j] = 0

sieve()
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n - 6):
        if p[i] == 1 and p[i + 6] == 1 and (p[i + 2] == 1 or p[i + 4] == 1):
            cnt += 1
    print(cnt)