from math import *
n = int(input())
cnt = 0
sr = int(sqrt(n))
p = [i for i in range(sr + 1)]
for i in range(2, int(sqrt(sr)) + 1):
    if p[i] == i:
        for j in range(i * i, sr + 1, i):
            if p[j] == j:
                p[j] = i
cnt = 0
for i in range(2 , sr + 1):
    x = p[i]
    y = p[i // x]
    if x * y == i and x != y and y != 1:
        cnt += 1
    elif x == i and x ** 8 <= n:
        cnt += 1
print(cnt)