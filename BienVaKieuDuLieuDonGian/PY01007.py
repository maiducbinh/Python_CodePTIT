from math import *
for _ in range(int(input())):
    n, x, m = map(float, input().split())
    x /= 100
    k = log(m / n, x + 1)
    if k != int(k):
        k = (int(k) + 1)
    print(int(k))