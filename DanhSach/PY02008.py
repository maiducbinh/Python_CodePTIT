from math import *

N = 10 ** 6
p = [1] * (N + 1)
prime = []
def sieve():
    p[0] = 0
    p[1] = 0
    for i in range(2, int(sqrt(N)) + 1):
        if p[i] == 1:
            for j in range(i * i, N + 1, i):
                p[j] = 0
    for i in range(N + 1):
        if p[i] == 1:
            prime.append(i)
sieve()
n, x = map(int, input().split())
print(x, end = " ")
for i in range(n):
    x = x + prime[i]
    print(x, end = " ")
