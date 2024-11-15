from math import *

for _ in range(int(input())):
    n = int(input())
    s = str(n)[::-1]
    m = int(s)
    if gcd(n, m) == 1:
        print("YES")
    else:
        print("NO")