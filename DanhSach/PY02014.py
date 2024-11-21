from math import *
N = 10 ** 5
p = [1] * (N + 1)
p[0] = 0
p[1] = 0
prime = []
for i in range(2, N + 1):
    if p[i]:
        prime.append(i)
        for j in range(i * i, N + 1, i):
            p[j] = 0

n = int(input())
a = list(map(int, input().split()))
s = 0
for i in a:
    d = 10 ** 9
    for j in prime:
        d = min(d, abs(i - j))
    s = max(s, d)
print(s)